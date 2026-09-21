"""Durable control-store contracts.

The store persists owner-approved state. It does not validate concept-specific transition legality.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Protocol

from syngan.foundation.identity import (
    LogicalId,
    MigrationRevision,
    RecoveryFrontier,
    RepresentationSchemaVersion,
    ResourceKey,
    StateVersion,
    TypedReference,
)
from syngan.foundation.representation import EncodedPayload


class ControlStoreError(RuntimeError):
    """Base control-store failure."""


class AuthorityScopeMismatch(ControlStoreError):
    """A reference/store authority scope does not match."""


class ImmutableRecordConflict(ControlStoreError):
    """An immutable identity was reused with conflicting content."""


class CurrentStateConflict(ControlStoreError):
    """Current owner state cannot be mutated from the supplied observation."""


class RecoveryFrontierConflict(ControlStoreError):
    """Mutation authority does not match the current recovery frontier."""


class CoordinationIntentConflict(ControlStoreError):
    """A coordination-intent identity was reused with conflicting content."""


class RecordNotFound(ControlStoreError):
    """A requested control record does not exist."""


class UnsupportedMigrationRevision(ControlStoreError):
    """The durable store schema is newer than this implementation supports."""


class ResolutionStatus(StrEnum):
    RESOLVED = "resolved"
    UNAVAILABLE = "unavailable"
    ABSENT = "absent"


class CoordinationIntentState(StrEnum):
    PENDING = "pending"
    ACKNOWLEDGED = "acknowledged"


@dataclass(frozen=True, slots=True)
class ImmutableRevisionRecord:
    reference: TypedReference
    schema_version: RepresentationSchemaVersion
    payload: EncodedPayload


@dataclass(frozen=True, slots=True)
class RevisionResolution:
    status: ResolutionStatus
    record: ImmutableRevisionRecord | None = None


@dataclass(frozen=True, slots=True)
class CurrentStateRecord:
    key: ResourceKey
    state_version: StateVersion
    schema_version: RepresentationSchemaVersion
    last_recovery_frontier: RecoveryFrontier
    payload: EncodedPayload


@dataclass(frozen=True, slots=True)
class TransitionRecord:
    transition_id: LogicalId
    key: ResourceKey
    from_state_version: StateVersion | None
    to_state_version: StateVersion
    recovery_frontier: RecoveryFrontier
    transition_kind: str
    detail: EncodedPayload


@dataclass(frozen=True, slots=True)
class CoordinationIntentRecord:
    intent_id: LogicalId
    source: TypedReference
    intent_kind: str
    payload: EncodedPayload
    recovery_frontier: RecoveryFrontier
    state: CoordinationIntentState


class ControlStore(Protocol):
    def migration_revision(self) -> MigrationRevision: ...

    def current_recovery_frontier(self) -> RecoveryFrontier: ...

    def advance_recovery_frontier(
        self, expected: RecoveryFrontier, new: RecoveryFrontier
    ) -> RecoveryFrontier: ...

    def put_immutable_revision(
        self,
        reference: TypedReference,
        schema_version: RepresentationSchemaVersion,
        payload: EncodedPayload,
        authority_frontier: RecoveryFrontier,
    ) -> ImmutableRevisionRecord: ...

    def resolve_immutable_revision(self, reference: TypedReference) -> RevisionResolution: ...

    def mark_immutable_revision_unavailable(
        self, reference: TypedReference, authority_frontier: RecoveryFrontier
    ) -> None: ...

    def create_current_state(
        self,
        key: ResourceKey,
        schema_version: RepresentationSchemaVersion,
        payload: EncodedPayload,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
        transition_kind: str,
        transition_detail: EncodedPayload,
    ) -> CurrentStateRecord: ...

    def get_current_state(self, key: ResourceKey) -> CurrentStateRecord | None: ...

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
    ) -> CurrentStateRecord: ...

    def list_transition_history(self, key: ResourceKey) -> tuple[TransitionRecord, ...]: ...

    def put_coordination_intent(
        self,
        intent_id: LogicalId,
        source: TypedReference,
        intent_kind: str,
        payload: EncodedPayload,
        authority_frontier: RecoveryFrontier,
    ) -> CoordinationIntentRecord: ...

    def get_coordination_intent(self, intent_id: LogicalId) -> CoordinationIntentRecord | None: ...

    def acknowledge_coordination_intent(
        self, intent_id: LogicalId, authority_frontier: RecoveryFrontier
    ) -> CoordinationIntentRecord: ...

    def close(self) -> None: ...
