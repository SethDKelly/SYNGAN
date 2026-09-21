"""SQLite reference adapter for durable control-state persistence."""

from __future__ import annotations

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import cast

from syngan.foundation.identity import (
    AuthorityScope,
    LogicalId,
    MigrationRevision,
    RecoveryFrontier,
    RepresentationSchemaVersion,
    ResourceKey,
    ResourceKind,
    SemanticRevisionId,
    StateVersion,
    TypedReference,
)
from syngan.foundation.representation import EncodedPayload
from syngan.ports.control_store import (
    AuthorityScopeMismatch,
    CoordinationIntentConflict,
    CoordinationIntentRecord,
    CoordinationIntentState,
    CurrentStateConflict,
    CurrentStateRecord,
    ImmutableRecordConflict,
    ImmutableRevisionRecord,
    RecordNotFound,
    RecoveryFrontierConflict,
    ResolutionStatus,
    RevisionResolution,
    TransitionRecord,
    UnsupportedMigrationRevision,
)

_SCHEMA_REVISION = MigrationRevision(1)


def _transition_kind(value: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError("transition kind must be non-empty")
    return normalized


def _intent_kind(value: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError("intent kind must be non-empty")
    return normalized


class SQLiteControlStore:
    """Portable durable reference implementation of the control-store contract."""

    def __init__(self, path: str | Path, authority_scope: AuthorityScope) -> None:
        self._scope = authority_scope
        self._connection = sqlite3.connect(str(path), isolation_level=None)
        self._connection.row_factory = sqlite3.Row
        self._connection.execute("PRAGMA foreign_keys = ON")
        try:
            self._bootstrap()
        except Exception:
            self._connection.close()
            raise

    def close(self) -> None:
        self._connection.close()

    def __enter__(self) -> SQLiteControlStore:
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        self.close()

    @contextmanager
    def _transaction(self) -> Iterator[None]:
        self._connection.execute("BEGIN IMMEDIATE")
        try:
            yield
        except Exception:
            self._connection.rollback()
            raise
        else:
            self._connection.commit()

    def _bootstrap(self) -> None:
        with self._transaction():
            self._connection.execute(
                """
                CREATE TABLE IF NOT EXISTS control_metadata (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                )
                """
            )
            existing_scope = self._metadata("authority_scope")
            if existing_scope is None:
                self._set_metadata("authority_scope", self._scope.value)
                self._set_metadata("migration_revision", str(_SCHEMA_REVISION.value))
                self._set_metadata("recovery_frontier", "0")
            elif existing_scope != self._scope.value:
                raise AuthorityScopeMismatch(
                    f"store scope {existing_scope!r} does not match {self._scope.value!r}"
                )

            revision_text = self._metadata("migration_revision")
            if revision_text is None:
                raise UnsupportedMigrationRevision("store migration revision is missing")
            revision = int(revision_text)
            if revision > _SCHEMA_REVISION.value:
                raise UnsupportedMigrationRevision(
                    f"store revision {revision} is newer than supported "
                    f"{_SCHEMA_REVISION.value}"
                )
            if revision < _SCHEMA_REVISION.value:
                raise UnsupportedMigrationRevision(
                    f"store revision {revision} requires an unsupported migration path"
                )

            self._connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS immutable_revisions (
                    scope TEXT NOT NULL,
                    resource_kind TEXT NOT NULL,
                    resource_id TEXT NOT NULL,
                    revision_id TEXT NOT NULL,
                    schema_version INTEGER NOT NULL,
                    payload_json TEXT,
                    availability TEXT NOT NULL,
                    PRIMARY KEY (scope, resource_kind, resource_id, revision_id)
                );

                CREATE TABLE IF NOT EXISTS current_states (
                    scope TEXT NOT NULL,
                    resource_kind TEXT NOT NULL,
                    resource_id TEXT NOT NULL,
                    state_version INTEGER NOT NULL,
                    schema_version INTEGER NOT NULL,
                    last_recovery_frontier INTEGER NOT NULL,
                    payload_json TEXT NOT NULL,
                    PRIMARY KEY (scope, resource_kind, resource_id)
                );

                CREATE TABLE IF NOT EXISTS transition_history (
                    sequence INTEGER PRIMARY KEY AUTOINCREMENT,
                    transition_id TEXT NOT NULL UNIQUE,
                    scope TEXT NOT NULL,
                    resource_kind TEXT NOT NULL,
                    resource_id TEXT NOT NULL,
                    from_state_version INTEGER,
                    to_state_version INTEGER NOT NULL,
                    recovery_frontier INTEGER NOT NULL,
                    transition_kind TEXT NOT NULL,
                    detail_json TEXT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_transition_history_resource
                ON transition_history (
                    scope,
                    resource_kind,
                    resource_id,
                    sequence
                );

                CREATE TABLE IF NOT EXISTS coordination_intents (
                    intent_id TEXT PRIMARY KEY,
                    source_scope TEXT NOT NULL,
                    source_kind TEXT NOT NULL,
                    source_resource_id TEXT NOT NULL,
                    source_revision_id TEXT,
                    intent_kind TEXT NOT NULL,
                    payload_json TEXT NOT NULL,
                    recovery_frontier INTEGER NOT NULL,
                    state TEXT NOT NULL
                );
                """
            )

    def _metadata(self, key: str) -> str | None:
        row = self._connection.execute(
            "SELECT value FROM control_metadata WHERE key = ?", (key,)
        ).fetchone()
        if row is None:
            return None
        return cast(str, row["value"])

    def _set_metadata(self, key: str, value: str) -> None:
        self._connection.execute(
            """
            INSERT INTO control_metadata(key, value)
            VALUES (?, ?)
            ON CONFLICT(key) DO UPDATE SET value = excluded.value
            """,
            (key, value),
        )

    def _assert_scope(self, key: ResourceKey) -> None:
        if key.scope != self._scope:
            raise AuthorityScopeMismatch(
                f"resource scope {key.scope.value!r} does not match store scope "
                f"{self._scope.value!r}"
            )

    def _current_frontier_value(self) -> int:
        value = self._metadata("recovery_frontier")
        if value is None:
            raise RecoveryFrontierConflict("store recovery frontier is missing")
        return int(value)

    def _assert_frontier(self, authority_frontier: RecoveryFrontier) -> None:
        current = self._current_frontier_value()
        if authority_frontier.value != current:
            raise RecoveryFrontierConflict(
                f"recovery frontier {authority_frontier.value} is stale; current is {current}"
            )

    def migration_revision(self) -> MigrationRevision:
        value = self._metadata("migration_revision")
        if value is None:
            raise UnsupportedMigrationRevision("store migration revision is missing")
        return MigrationRevision(int(value))

    def current_recovery_frontier(self) -> RecoveryFrontier:
        return RecoveryFrontier(self._current_frontier_value())

    def advance_recovery_frontier(
        self, expected: RecoveryFrontier, new: RecoveryFrontier
    ) -> RecoveryFrontier:
        if new.value <= expected.value:
            raise RecoveryFrontierConflict("new recovery frontier must advance")

        with self._transaction():
            self._assert_frontier(expected)
            self._set_metadata("recovery_frontier", str(new.value))

        return new

    def put_immutable_revision(
        self,
        reference: TypedReference,
        schema_version: RepresentationSchemaVersion,
        payload: EncodedPayload,
        authority_frontier: RecoveryFrontier,
    ) -> ImmutableRevisionRecord:
        revision = reference.require_exact_revision()
        self._assert_scope(reference.key)

        with self._transaction():
            self._assert_frontier(authority_frontier)
            row = self._connection.execute(
                """
                SELECT schema_version, payload_json, availability
                FROM immutable_revisions
                WHERE scope = ?
                  AND resource_kind = ?
                  AND resource_id = ?
                  AND revision_id = ?
                """,
                (
                    reference.key.scope.value,
                    reference.key.kind.value,
                    reference.key.resource_id.value,
                    revision.value,
                ),
            ).fetchone()

            if row is not None:
                availability = cast(str, row["availability"])
                existing_schema = int(cast(int, row["schema_version"]))
                existing_payload = cast(str | None, row["payload_json"])
                if (
                    availability == "available"
                    and existing_schema == schema_version.value
                    and existing_payload == payload.json_text
                ):
                    return ImmutableRevisionRecord(reference, schema_version, payload)
                raise ImmutableRecordConflict(
                    "immutable revision identity already exists with different content"
                )

            self._connection.execute(
                """
                INSERT INTO immutable_revisions(
                    scope,
                    resource_kind,
                    resource_id,
                    revision_id,
                    schema_version,
                    payload_json,
                    availability
                )
                VALUES (?, ?, ?, ?, ?, ?, 'available')
                """,
                (
                    reference.key.scope.value,
                    reference.key.kind.value,
                    reference.key.resource_id.value,
                    revision.value,
                    schema_version.value,
                    payload.json_text,
                ),
            )

        return ImmutableRevisionRecord(reference, schema_version, payload)

    def resolve_immutable_revision(self, reference: TypedReference) -> RevisionResolution:
        revision = reference.require_exact_revision()
        self._assert_scope(reference.key)
        row = self._connection.execute(
            """
            SELECT schema_version, payload_json, availability
            FROM immutable_revisions
            WHERE scope = ?
              AND resource_kind = ?
              AND resource_id = ?
              AND revision_id = ?
            """,
            (
                reference.key.scope.value,
                reference.key.kind.value,
                reference.key.resource_id.value,
                revision.value,
            ),
        ).fetchone()

        if row is None:
            return RevisionResolution(ResolutionStatus.ABSENT)

        availability = cast(str, row["availability"])
        if availability == "unavailable":
            return RevisionResolution(ResolutionStatus.UNAVAILABLE)

        payload_text = cast(str | None, row["payload_json"])
        if payload_text is None:
            raise ImmutableRecordConflict("available immutable revision has no payload")

        record = ImmutableRevisionRecord(
            reference=reference,
            schema_version=RepresentationSchemaVersion(int(cast(int, row["schema_version"]))),
            payload=EncodedPayload(payload_text),
        )
        return RevisionResolution(ResolutionStatus.RESOLVED, record)

    def mark_immutable_revision_unavailable(
        self, reference: TypedReference, authority_frontier: RecoveryFrontier
    ) -> None:
        revision = reference.require_exact_revision()
        self._assert_scope(reference.key)

        with self._transaction():
            self._assert_frontier(authority_frontier)
            row = self._connection.execute(
                """
                SELECT availability
                FROM immutable_revisions
                WHERE scope = ?
                  AND resource_kind = ?
                  AND resource_id = ?
                  AND revision_id = ?
                """,
                (
                    reference.key.scope.value,
                    reference.key.kind.value,
                    reference.key.resource_id.value,
                    revision.value,
                ),
            ).fetchone()
            if row is None:
                raise RecordNotFound("immutable revision does not exist")
            if cast(str, row["availability"]) == "unavailable":
                return
            self._connection.execute(
                """
                UPDATE immutable_revisions
                SET payload_json = NULL,
                    availability = 'unavailable'
                WHERE scope = ?
                  AND resource_kind = ?
                  AND resource_id = ?
                  AND revision_id = ?
                """,
                (
                    reference.key.scope.value,
                    reference.key.kind.value,
                    reference.key.resource_id.value,
                    revision.value,
                ),
            )

    def create_current_state(
        self,
        key: ResourceKey,
        schema_version: RepresentationSchemaVersion,
        payload: EncodedPayload,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
        transition_kind: str,
        transition_detail: EncodedPayload,
    ) -> CurrentStateRecord:
        self._assert_scope(key)
        kind = _transition_kind(transition_kind)
        state_version = StateVersion(0)

        try:
            with self._transaction():
                self._assert_frontier(authority_frontier)
                self._connection.execute(
                    """
                    INSERT INTO current_states(
                        scope,
                        resource_kind,
                        resource_id,
                        state_version,
                        schema_version,
                        last_recovery_frontier,
                        payload_json
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        key.scope.value,
                        key.kind.value,
                        key.resource_id.value,
                        state_version.value,
                        schema_version.value,
                        authority_frontier.value,
                        payload.json_text,
                    ),
                )
                self._insert_transition(
                    transition_id=transition_id,
                    key=key,
                    from_version=None,
                    to_version=state_version,
                    recovery_frontier=authority_frontier,
                    transition_kind=kind,
                    detail=transition_detail,
                )
        except sqlite3.IntegrityError as exc:
            raise CurrentStateConflict("current state or transition identity already exists") from exc

        return CurrentStateRecord(
            key=key,
            state_version=state_version,
            schema_version=schema_version,
            last_recovery_frontier=authority_frontier,
            payload=payload,
        )

    def get_current_state(self, key: ResourceKey) -> CurrentStateRecord | None:
        self._assert_scope(key)
        row = self._connection.execute(
            """
            SELECT state_version, schema_version, last_recovery_frontier, payload_json
            FROM current_states
            WHERE scope = ?
              AND resource_kind = ?
              AND resource_id = ?
            """,
            (key.scope.value, key.kind.value, key.resource_id.value),
        ).fetchone()
        if row is None:
            return None
        return CurrentStateRecord(
            key=key,
            state_version=StateVersion(int(cast(int, row["state_version"]))),
            schema_version=RepresentationSchemaVersion(int(cast(int, row["schema_version"]))),
            last_recovery_frontier=RecoveryFrontier(
                int(cast(int, row["last_recovery_frontier"]))
            ),
            payload=EncodedPayload(cast(str, row["payload_json"])),
        )

    def compare_and_swap_current_state(
        self,
        key: ResourceKey,
        expected_state_version: StateVersion,
        authority_frontier: RecoveryFrontier,
        schema_version: RepresentationSchemaVersion,
        payload: EncodedPayload,
        transition_id: LogicalId,
        transition_kind: str,
        transition_detail: EncodedPayload,
    ) -> CurrentStateRecord:
        self._assert_scope(key)
        kind = _transition_kind(transition_kind)
        new_version = expected_state_version.next()

        try:
            with self._transaction():
                self._assert_frontier(authority_frontier)
                current = self._connection.execute(
                    """
                    SELECT state_version
                    FROM current_states
                    WHERE scope = ?
                      AND resource_kind = ?
                      AND resource_id = ?
                    """,
                    (key.scope.value, key.kind.value, key.resource_id.value),
                ).fetchone()
                if current is None:
                    raise RecordNotFound("current state does not exist")
                actual_version = StateVersion(int(cast(int, current["state_version"])))
                if actual_version != expected_state_version:
                    raise CurrentStateConflict(
                        f"stale state version {expected_state_version.value}; "
                        f"current is {actual_version.value}"
                    )

                updated = self._connection.execute(
                    """
                    UPDATE current_states
                    SET state_version = ?,
                        schema_version = ?,
                        last_recovery_frontier = ?,
                        payload_json = ?
                    WHERE scope = ?
                      AND resource_kind = ?
                      AND resource_id = ?
                      AND state_version = ?
                    """,
                    (
                        new_version.value,
                        schema_version.value,
                        authority_frontier.value,
                        payload.json_text,
                        key.scope.value,
                        key.kind.value,
                        key.resource_id.value,
                        expected_state_version.value,
                    ),
                )
                if updated.rowcount != 1:
                    raise CurrentStateConflict("current state changed during compare-and-set")

                self._insert_transition(
                    transition_id=transition_id,
                    key=key,
                    from_version=expected_state_version,
                    to_version=new_version,
                    recovery_frontier=authority_frontier,
                    transition_kind=kind,
                    detail=transition_detail,
                )
        except sqlite3.IntegrityError as exc:
            raise CurrentStateConflict("transition identity already exists") from exc

        return CurrentStateRecord(
            key=key,
            state_version=new_version,
            schema_version=schema_version,
            last_recovery_frontier=authority_frontier,
            payload=payload,
        )

    def _insert_transition(
        self,
        transition_id: LogicalId,
        key: ResourceKey,
        from_version: StateVersion | None,
        to_version: StateVersion,
        recovery_frontier: RecoveryFrontier,
        transition_kind: str,
        detail: EncodedPayload,
    ) -> None:
        self._connection.execute(
            """
            INSERT INTO transition_history(
                transition_id,
                scope,
                resource_kind,
                resource_id,
                from_state_version,
                to_state_version,
                recovery_frontier,
                transition_kind,
                detail_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                transition_id.value,
                key.scope.value,
                key.kind.value,
                key.resource_id.value,
                from_version.value if from_version is not None else None,
                to_version.value,
                recovery_frontier.value,
                transition_kind,
                detail.json_text,
            ),
        )

    def list_transition_history(self, key: ResourceKey) -> tuple[TransitionRecord, ...]:
        self._assert_scope(key)
        rows = self._connection.execute(
            """
            SELECT
                transition_id,
                from_state_version,
                to_state_version,
                recovery_frontier,
                transition_kind,
                detail_json
            FROM transition_history
            WHERE scope = ?
              AND resource_kind = ?
              AND resource_id = ?
            ORDER BY sequence
            """,
            (key.scope.value, key.kind.value, key.resource_id.value),
        ).fetchall()

        records: list[TransitionRecord] = []
        for row in rows:
            from_value = cast(int | None, row["from_state_version"])
            records.append(
                TransitionRecord(
                    transition_id=LogicalId(cast(str, row["transition_id"])),
                    key=key,
                    from_state_version=StateVersion(from_value) if from_value is not None else None,
                    to_state_version=StateVersion(int(cast(int, row["to_state_version"]))),
                    recovery_frontier=RecoveryFrontier(
                        int(cast(int, row["recovery_frontier"]))
                    ),
                    transition_kind=cast(str, row["transition_kind"]),
                    detail=EncodedPayload(cast(str, row["detail_json"])),
                )
            )
        return tuple(records)

    def put_coordination_intent(
        self,
        intent_id: LogicalId,
        source: TypedReference,
        intent_kind: str,
        payload: EncodedPayload,
        authority_frontier: RecoveryFrontier,
    ) -> CoordinationIntentRecord:
        self._assert_scope(source.key)
        kind = _intent_kind(intent_kind)

        with self._transaction():
            self._assert_frontier(authority_frontier)
            row = self._connection.execute(
                """
                SELECT
                    source_scope,
                    source_kind,
                    source_resource_id,
                    source_revision_id,
                    intent_kind,
                    payload_json,
                    recovery_frontier,
                    state
                FROM coordination_intents
                WHERE intent_id = ?
                """,
                (intent_id.value,),
            ).fetchone()

            if row is not None:
                existing = self._coordination_intent_from_row(intent_id, row)
                if (
                    existing.source == source
                    and existing.intent_kind == kind
                    and existing.payload == payload
                    and existing.recovery_frontier == authority_frontier
                ):
                    return existing
                raise CoordinationIntentConflict(
                    "coordination intent identity already exists with different content"
                )

            self._connection.execute(
                """
                INSERT INTO coordination_intents(
                    intent_id,
                    source_scope,
                    source_kind,
                    source_resource_id,
                    source_revision_id,
                    intent_kind,
                    payload_json,
                    recovery_frontier,
                    state
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    intent_id.value,
                    source.key.scope.value,
                    source.key.kind.value,
                    source.key.resource_id.value,
                    source.revision_id.value if source.revision_id is not None else None,
                    kind,
                    payload.json_text,
                    authority_frontier.value,
                    CoordinationIntentState.PENDING.value,
                ),
            )

        return CoordinationIntentRecord(
            intent_id=intent_id,
            source=source,
            intent_kind=kind,
            payload=payload,
            recovery_frontier=authority_frontier,
            state=CoordinationIntentState.PENDING,
        )

    def get_coordination_intent(self, intent_id: LogicalId) -> CoordinationIntentRecord | None:
        row = self._connection.execute(
            """
            SELECT
                source_scope,
                source_kind,
                source_resource_id,
                source_revision_id,
                intent_kind,
                payload_json,
                recovery_frontier,
                state
            FROM coordination_intents
            WHERE intent_id = ?
            """,
            (intent_id.value,),
        ).fetchone()
        if row is None:
            return None
        return self._coordination_intent_from_row(intent_id, row)

    def acknowledge_coordination_intent(
        self, intent_id: LogicalId, authority_frontier: RecoveryFrontier
    ) -> CoordinationIntentRecord:
        with self._transaction():
            self._assert_frontier(authority_frontier)
            row = self._connection.execute(
                """
                SELECT
                    source_scope,
                    source_kind,
                    source_resource_id,
                    source_revision_id,
                    intent_kind,
                    payload_json,
                    recovery_frontier,
                    state
                FROM coordination_intents
                WHERE intent_id = ?
                """,
                (intent_id.value,),
            ).fetchone()
            if row is None:
                raise RecordNotFound("coordination intent does not exist")
            existing = self._coordination_intent_from_row(intent_id, row)
            if existing.state is CoordinationIntentState.ACKNOWLEDGED:
                return existing
            self._connection.execute(
                """
                UPDATE coordination_intents
                SET state = ?
                WHERE intent_id = ?
                """,
                (CoordinationIntentState.ACKNOWLEDGED.value, intent_id.value),
            )

        return CoordinationIntentRecord(
            intent_id=existing.intent_id,
            source=existing.source,
            intent_kind=existing.intent_kind,
            payload=existing.payload,
            recovery_frontier=existing.recovery_frontier,
            state=CoordinationIntentState.ACKNOWLEDGED,
        )

    def _coordination_intent_from_row(
        self, intent_id: LogicalId, row: sqlite3.Row
    ) -> CoordinationIntentRecord:
        source = TypedReference(
            key=ResourceKey(
                scope=AuthorityScope(cast(str, row["source_scope"])),
                kind=ResourceKind(cast(str, row["source_kind"])),
                resource_id=LogicalId(cast(str, row["source_resource_id"])),
            ),
            revision_id=(
                SemanticRevisionId(cast(str, row["source_revision_id"]))
                if row["source_revision_id"] is not None
                else None
            ),
        )
        self._assert_scope(source.key)
        return CoordinationIntentRecord(
            intent_id=intent_id,
            source=source,
            intent_kind=cast(str, row["intent_kind"]),
            payload=EncodedPayload(cast(str, row["payload_json"])),
            recovery_frontier=RecoveryFrontier(int(cast(int, row["recovery_frontier"]))),
            state=CoordinationIntentState(cast(str, row["state"])),
        )
