from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from syngan.adapters.sqlite_control_store import SQLiteControlStore
from syngan.foundation.identity import (
    AuthorityScope,
    LogicalId,
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
    CoordinationIntentState,
    CurrentStateConflict,
    ImmutableRecordConflict,
    RecoveryFrontierConflict,
    ResolutionStatus,
    UnsupportedMigrationRevision,
)

pytestmark = pytest.mark.integration

SCHEMA = RepresentationSchemaVersion(1)
FRONTIER_0 = RecoveryFrontier(0)


def payload(**values: str | int | bool | None) -> EncodedPayload:
    return EncodedPayload.from_object(dict(values))


def key(scope: str = "test", resource_id: str = "resource-1") -> ResourceKey:
    return ResourceKey(
        scope=AuthorityScope(scope),
        kind=ResourceKind("test-owner"),
        resource_id=LogicalId(resource_id),
    )


def exact_reference(revision: str, resource_id: str = "resource-1") -> TypedReference:
    return TypedReference(
        key=key(resource_id=resource_id),
        revision_id=SemanticRevisionId(revision),
    )


def test_exact_revision_resolution_never_substitutes_latest(tmp_path: Path) -> None:
    database = tmp_path / "control.sqlite"
    with SQLiteControlStore(database, AuthorityScope("test")) as store:
        r1 = exact_reference("r1")
        r2 = exact_reference("r2")
        store.put_immutable_revision(r1, SCHEMA, payload(name="one"), FRONTIER_0)
        store.put_immutable_revision(r2, SCHEMA, payload(name="two"), FRONTIER_0)

        assert store.resolve_immutable_revision(r1).record is not None
        assert store.resolve_immutable_revision(r1).record.payload == payload(name="one")
        assert store.resolve_immutable_revision(r2).record is not None
        assert store.resolve_immutable_revision(r2).record.payload == payload(name="two")

        missing = exact_reference("r3")
        assert store.resolve_immutable_revision(missing).status is ResolutionStatus.ABSENT

        with pytest.raises(ValueError):
            store.resolve_immutable_revision(TypedReference(key=key()))


def test_immutable_revision_idempotency_conflict_and_tombstone(tmp_path: Path) -> None:
    with SQLiteControlStore(tmp_path / "control.sqlite", AuthorityScope("test")) as store:
        reference = exact_reference("r1")
        record = store.put_immutable_revision(reference, SCHEMA, payload(value=1), FRONTIER_0)
        repeated = store.put_immutable_revision(reference, SCHEMA, payload(value=1), FRONTIER_0)

        assert repeated == record
        with pytest.raises(ImmutableRecordConflict):
            store.put_immutable_revision(reference, SCHEMA, payload(value=2), FRONTIER_0)

        store.mark_immutable_revision_unavailable(reference, FRONTIER_0)
        resolution = store.resolve_immutable_revision(reference)
        assert resolution.status is ResolutionStatus.UNAVAILABLE
        assert resolution.record is None

        with pytest.raises(ImmutableRecordConflict):
            store.put_immutable_revision(reference, SCHEMA, payload(value=1), FRONTIER_0)


def test_current_state_uses_cas_and_append_preserving_history(tmp_path: Path) -> None:
    with SQLiteControlStore(tmp_path / "control.sqlite", AuthorityScope("test")) as store:
        resource = key()
        created = store.create_current_state(
            resource,
            SCHEMA,
            payload(state="draft"),
            FRONTIER_0,
            LogicalId("transition-create"),
            "created",
            payload(reason="test"),
        )
        assert created.state_version == StateVersion(0)

        updated = store.compare_and_swap_current_state(
            resource,
            StateVersion(0),
            FRONTIER_0,
            SCHEMA,
            payload(state="ready"),
            LogicalId("transition-ready"),
            "owner-transition",
            payload(reason="owner-approved"),
        )
        assert updated.state_version == StateVersion(1)

        with pytest.raises(CurrentStateConflict):
            store.compare_and_swap_current_state(
                resource,
                StateVersion(0),
                FRONTIER_0,
                SCHEMA,
                payload(state="stale"),
                LogicalId("transition-stale"),
                "owner-transition",
                payload(reason="stale"),
            )

        history = store.list_transition_history(resource)
        assert [entry.transition_id.value for entry in history] == [
            "transition-create",
            "transition-ready",
        ]
        assert history[0].from_state_version is None
        assert history[1].from_state_version == StateVersion(0)
        assert history[1].to_state_version == StateVersion(1)


def test_history_append_failure_rolls_back_current_state_update(tmp_path: Path) -> None:
    with SQLiteControlStore(tmp_path / "control.sqlite", AuthorityScope("test")) as store:
        resource = key()
        duplicate_transition = LogicalId("same-transition")
        store.create_current_state(
            resource,
            SCHEMA,
            payload(state="initial"),
            FRONTIER_0,
            duplicate_transition,
            "created",
            payload(step=0),
        )

        with pytest.raises(CurrentStateConflict):
            store.compare_and_swap_current_state(
                resource,
                StateVersion(0),
                FRONTIER_0,
                SCHEMA,
                payload(state="must-rollback"),
                duplicate_transition,
                "owner-transition",
                payload(step=1),
            )

        current = store.get_current_state(resource)
        assert current is not None
        assert current.state_version == StateVersion(0)
        assert current.payload == payload(state="initial")
        assert len(store.list_transition_history(resource)) == 1


def test_recovery_frontier_qualifies_all_canonical_mutations(tmp_path: Path) -> None:
    with SQLiteControlStore(tmp_path / "control.sqlite", AuthorityScope("test")) as store:
        resource = key()
        store.create_current_state(
            resource,
            SCHEMA,
            payload(state="initial"),
            FRONTIER_0,
            LogicalId("create"),
            "created",
            payload(step=0),
        )

        frontier_1 = store.advance_recovery_frontier(FRONTIER_0, RecoveryFrontier(1))
        assert frontier_1 == RecoveryFrontier(1)

        with pytest.raises(RecoveryFrontierConflict):
            store.compare_and_swap_current_state(
                resource,
                StateVersion(0),
                FRONTIER_0,
                SCHEMA,
                payload(state="stale-authority"),
                LogicalId("stale-write"),
                "owner-transition",
                payload(step=1),
            )

        updated = store.compare_and_swap_current_state(
            resource,
            StateVersion(0),
            frontier_1,
            SCHEMA,
            payload(state="current-authority"),
            LogicalId("current-write"),
            "owner-transition",
            payload(step=2),
        )
        assert updated.last_recovery_frontier == frontier_1

        with pytest.raises(RecoveryFrontierConflict):
            store.put_immutable_revision(
                exact_reference("late-r1", resource_id="other"),
                SCHEMA,
                payload(value=1),
                FRONTIER_0,
            )

        with pytest.raises(RecoveryFrontierConflict):
            store.advance_recovery_frontier(FRONTIER_0, RecoveryFrontier(2))


def test_file_backed_store_reopens_durably_and_rejects_wrong_scope(tmp_path: Path) -> None:
    database = tmp_path / "control.sqlite"
    resource = key()

    with SQLiteControlStore(database, AuthorityScope("test")) as store:
        store.create_current_state(
            resource,
            SCHEMA,
            payload(state="durable"),
            FRONTIER_0,
            LogicalId("create"),
            "created",
            payload(step=0),
        )

    with SQLiteControlStore(database, AuthorityScope("test")) as reopened:
        current = reopened.get_current_state(resource)
        assert current is not None
        assert current.payload == payload(state="durable")

    with pytest.raises(AuthorityScopeMismatch):
        SQLiteControlStore(database, AuthorityScope("clone"))


def test_future_migration_revision_is_rejected(tmp_path: Path) -> None:
    database = tmp_path / "future.sqlite"
    connection = sqlite3.connect(database)
    connection.execute("CREATE TABLE control_metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
    connection.execute(
        "INSERT INTO control_metadata(key, value) VALUES ('authority_scope', 'test')"
    )
    connection.execute(
        "INSERT INTO control_metadata(key, value) VALUES ('migration_revision', '99')"
    )
    connection.execute("INSERT INTO control_metadata(key, value) VALUES ('recovery_frontier', '0')")
    connection.commit()
    connection.close()

    with pytest.raises(UnsupportedMigrationRevision):
        SQLiteControlStore(database, AuthorityScope("test"))


def test_coordination_intent_is_idempotent_technical_state_not_semantic_success(
    tmp_path: Path,
) -> None:
    with SQLiteControlStore(tmp_path / "control.sqlite", AuthorityScope("test")) as store:
        intent_id = LogicalId("intent-1")
        source = exact_reference("r1")
        first = store.put_coordination_intent(
            intent_id,
            source,
            "follow-up",
            payload(target="external-boundary"),
            FRONTIER_0,
        )
        repeated = store.put_coordination_intent(
            intent_id,
            source,
            "follow-up",
            payload(target="external-boundary"),
            FRONTIER_0,
        )

        assert repeated == first
        assert first.state is CoordinationIntentState.PENDING

        with pytest.raises(CoordinationIntentConflict):
            store.put_coordination_intent(
                intent_id,
                source,
                "different",
                payload(target="external-boundary"),
                FRONTIER_0,
            )

        acknowledged = store.acknowledge_coordination_intent(intent_id, FRONTIER_0)
        assert acknowledged.state is CoordinationIntentState.ACKNOWLEDGED
        assert acknowledged.intent_kind == "follow-up"
