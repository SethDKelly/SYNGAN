"""Durable application coordination for Learning and Learned State."""

from __future__ import annotations

from dataclasses import dataclass

from syngan.domain.learning_state import (
    LearnedStateMaterialDescriptor,
    LearnedStateRecord,
    LearnedStateStatus,
    LearningAggregate,
    LearningStatus,
    learned_state_from_payload,
    learned_state_key,
    learned_state_material_to_payload,
    learned_state_to_payload,
    learning_from_payload,
    learning_state_key,
    learning_to_payload,
)
from syngan.foundation.identity import (
    LogicalId,
    RecoveryFrontier,
    RepresentationSchemaVersion,
    StateVersion,
    TypedReference,
)
from syngan.foundation.representation import EncodedPayload
from syngan.ports.control_store import (
    ControlStore,
    CurrentStateConflict,
    RecordNotFound,
    ResolutionStatus,
)

_SCHEMA = RepresentationSchemaVersion(1)


@dataclass(frozen=True, slots=True)
class LearningSnapshot:
    state: LearningAggregate
    state_version: StateVersion


@dataclass(frozen=True, slots=True)
class LearnedStateSnapshot:
    state: LearnedStateRecord
    state_version: StateVersion


class LearningStateService:
    """Persist Learning and Learned State without transferring semantic ownership to storage."""

    def __init__(self, store: ControlStore) -> None:
        self._store = store

    def initialize_learning(
        self,
        learning: LearningAggregate,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> LearningSnapshot:
        record = self._store.create_current_state(
            key=learning_state_key(learning.learning_commitment),
            schema_version=_SCHEMA,
            payload=learning_to_payload(learning),
            authority_frontier=authority_frontier,
            transition_id=transition_id,
            transition_kind="learning-initialized",
            transition_detail=EncodedPayload.from_object(
                {"learning_id": learning.learning_commitment.key.resource_id.value}
            ),
        )
        return LearningSnapshot(
            state=learning_from_payload(record.payload),
            state_version=record.state_version,
        )

    def load_learning(self, learning_commitment: TypedReference) -> LearningSnapshot:
        record = self._store.get_current_state(learning_state_key(learning_commitment))
        if record is None:
            raise RecordNotFound("Learning state record does not exist")
        state = learning_from_payload(record.payload)
        if state.learning_commitment != learning_commitment:
            raise ValueError("stored Learning state does not match requested commitment")
        return LearningSnapshot(state=state, state_version=record.state_version)

    def activate_learning(
        self,
        learning_commitment: TypedReference,
        expected_state_version: StateVersion,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> LearningSnapshot:
        snapshot = self._load_expected_learning(
            learning_commitment,
            expected_state_version,
        )
        return self._persist_learning(
            snapshot,
            snapshot.state.activate(),
            authority_frontier,
            transition_id,
            "learning-activated",
            EncodedPayload.from_object({}),
        )

    def establish_learned_state(
        self,
        learning_commitment: TypedReference,
        expected_learning_state_version: StateVersion,
        learned_state: LearnedStateRecord,
        material: LearnedStateMaterialDescriptor,
        authority_frontier: RecoveryFrontier,
        learned_state_transition_id: LogicalId,
        learning_transition_id: LogicalId,
        intent_id: LogicalId,
    ) -> tuple[LearningSnapshot, LearnedStateSnapshot]:
        learning = self._load_expected_learning(
            learning_commitment,
            expected_learning_state_version,
        )
        if learning.state.status not in {
            LearningStatus.COMMITTED,
            LearningStatus.ACTIVE,
        }:
            raise ValueError("only committed or active Learning can establish Learned State")
        if learned_state.producing_learning_reference != learning_commitment:
            raise ValueError("Learned State producing Learning does not match")
        if learned_state.strategy_reference != learning.state.strategy_reference:
            raise ValueError("Learned State Strategy does not match producing Learning")
        if learned_state.material_reference != material.reference:
            raise ValueError("Learned State material reference does not match descriptor")
        if learned_state.dependency_references != material.dependency_references:
            raise ValueError("Learned State dependency references do not match material descriptor")

        self._store.put_coordination_intent(
            intent_id=intent_id,
            source=learning_commitment,
            intent_kind="establish-learned-state",
            payload=EncodedPayload.from_object(
                {
                    "learned_state_reference": learned_state.reference.require_exact_binding()[1],
                    "material_reference": material.reference.require_exact_binding()[1],
                }
            ),
            authority_frontier=authority_frontier,
        )
        self._store.put_immutable_binding(
            reference=material.reference,
            schema_version=_SCHEMA,
            payload=learned_state_material_to_payload(material),
            authority_frontier=authority_frontier,
        )

        state_snapshot = self._ensure_learned_state_record(
            learned_state,
            authority_frontier,
            learned_state_transition_id,
        )
        next_learning = learning.state.complete(learned_state.reference)
        learning_snapshot = self._persist_learning(
            learning,
            next_learning,
            authority_frontier,
            learning_transition_id,
            "learning-completed",
            EncodedPayload.from_object(
                {"learned_state_reference": learned_state.reference.require_exact_binding()[1]}
            ),
        )
        self._store.acknowledge_coordination_intent(intent_id, authority_frontier)
        return learning_snapshot, state_snapshot

    def load_learned_state(self, reference: TypedReference) -> LearnedStateSnapshot:
        record = self._store.get_current_state(learned_state_key(reference))
        if record is None:
            raise RecordNotFound("Learned State record does not exist")
        state = learned_state_from_payload(record.payload)
        if state.reference != reference:
            raise ValueError("stored Learned State does not match requested reference")

        producing = self.load_learning(state.producing_learning_reference)
        if producing.state.status is not LearningStatus.COMPLETED:
            raise RecordNotFound("Learned State is not semantically established")
        if producing.state.learned_state_reference != reference:
            raise RecordNotFound("Learning does not establish the requested Learned State")

        material = self._store.resolve_immutable_binding(state.material_reference)
        if material.status is not ResolutionStatus.RESOLVED or material.record is None:
            raise RecordNotFound("Learned State material is not exactly resolvable")

        return LearnedStateSnapshot(state=state, state_version=record.state_version)

    def change_learned_state_status(
        self,
        reference: TypedReference,
        expected_state_version: StateVersion,
        status: LearnedStateStatus,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
        *,
        limitations: tuple[str, ...] | None = None,
    ) -> LearnedStateSnapshot:
        snapshot = self.load_learned_state(reference)
        if snapshot.state_version != expected_state_version:
            raise CurrentStateConflict(
                f"expected Learned-State version {expected_state_version.value}, "
                f"found {snapshot.state_version.value}"
            )
        next_state = snapshot.state.with_status(status, limitations=limitations)
        record = self._store.compare_and_swap_current_state(
            key=learned_state_key(reference),
            expected_state_version=snapshot.state_version,
            authority_frontier=authority_frontier,
            schema_version=_SCHEMA,
            payload=learned_state_to_payload(next_state),
            transition_id=transition_id,
            transition_kind="learned-state-status-changed",
            transition_detail=EncodedPayload.from_object({"status": status.value}),
        )
        return LearnedStateSnapshot(
            state=learned_state_from_payload(record.payload),
            state_version=record.state_version,
        )

    def fail_learning(
        self,
        learning_commitment: TypedReference,
        expected_state_version: StateVersion,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> LearningSnapshot:
        snapshot = self._load_expected_learning(
            learning_commitment,
            expected_state_version,
        )
        return self._persist_learning(
            snapshot,
            snapshot.state.fail(),
            authority_frontier,
            transition_id,
            "learning-failed",
            EncodedPayload.from_object({}),
        )

    def cancel_learning(
        self,
        learning_commitment: TypedReference,
        expected_state_version: StateVersion,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> LearningSnapshot:
        snapshot = self._load_expected_learning(
            learning_commitment,
            expected_state_version,
        )
        return self._persist_learning(
            snapshot,
            snapshot.state.cancel(),
            authority_frontier,
            transition_id,
            "learning-cancelled",
            EncodedPayload.from_object({}),
        )

    def _ensure_learned_state_record(
        self,
        learned_state: LearnedStateRecord,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> LearnedStateSnapshot:
        key = learned_state_key(learned_state.reference)
        existing = self._store.get_current_state(key)
        payload = learned_state_to_payload(learned_state)
        if existing is not None:
            existing_state = learned_state_from_payload(existing.payload)
            if existing_state != learned_state:
                raise CurrentStateConflict("Learned State identity already has conflicting state")
            return LearnedStateSnapshot(
                state=existing_state,
                state_version=existing.state_version,
            )

        record = self._store.create_current_state(
            key=key,
            schema_version=_SCHEMA,
            payload=payload,
            authority_frontier=authority_frontier,
            transition_id=transition_id,
            transition_kind="learned-state-established",
            transition_detail=EncodedPayload.from_object(
                {"learning_id": learned_state.producing_learning_reference.key.resource_id.value}
            ),
        )
        return LearnedStateSnapshot(
            state=learned_state_from_payload(record.payload),
            state_version=record.state_version,
        )

    def _load_expected_learning(
        self,
        learning_commitment: TypedReference,
        expected_state_version: StateVersion,
    ) -> LearningSnapshot:
        snapshot = self.load_learning(learning_commitment)
        if snapshot.state_version != expected_state_version:
            raise CurrentStateConflict(
                f"expected Learning version {expected_state_version.value}, "
                f"found {snapshot.state_version.value}"
            )
        return snapshot

    def _persist_learning(
        self,
        snapshot: LearningSnapshot,
        next_state: LearningAggregate,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
        transition_kind: str,
        transition_detail: EncodedPayload,
    ) -> LearningSnapshot:
        record = self._store.compare_and_swap_current_state(
            key=learning_state_key(snapshot.state.learning_commitment),
            expected_state_version=snapshot.state_version,
            authority_frontier=authority_frontier,
            schema_version=_SCHEMA,
            payload=learning_to_payload(next_state),
            transition_id=transition_id,
            transition_kind=transition_kind,
            transition_detail=transition_detail,
        )
        return LearningSnapshot(
            state=learning_from_payload(record.payload),
            state_version=record.state_version,
        )
