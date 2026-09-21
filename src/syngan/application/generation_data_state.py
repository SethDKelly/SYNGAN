"""Application coordination for Generation-owned distributed data state."""

from __future__ import annotations

from dataclasses import dataclass

from syngan.domain.generation_data import (
    GenerationDataState,
    generation_data_state_from_payload,
    generation_data_state_key,
    generation_data_state_to_payload,
    generation_physical_subject_reference,
)
from syngan.foundation.data_state import (
    SealedPhysicalSubject,
    sealed_subject_from_payload,
    sealed_subject_to_payload,
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
class GenerationDataStateSnapshot:
    state: GenerationDataState
    state_version: StateVersion


class GenerationDataStateService:
    """Persist Generation data-state while leaving physical/provider work outside this layer."""

    def __init__(self, store: ControlStore) -> None:
        self._store = store

    def initialize(
        self,
        state: GenerationDataState,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> GenerationDataStateSnapshot:
        key = generation_data_state_key(state.generation_commitment)
        record = self._store.create_current_state(
            key=key,
            schema_version=_SCHEMA,
            payload=generation_data_state_to_payload(state),
            authority_frontier=authority_frontier,
            transition_id=transition_id,
            transition_kind="generation-data-state-initialized",
            transition_detail=EncodedPayload.from_object(
                {"generation_id": state.generation_commitment.key.resource_id.value}
            ),
        )
        return GenerationDataStateSnapshot(
            state=generation_data_state_from_payload(record.payload),
            state_version=record.state_version,
        )

    def load(self, generation_commitment: TypedReference) -> GenerationDataStateSnapshot:
        record = self._store.get_current_state(generation_data_state_key(generation_commitment))
        if record is None:
            raise RecordNotFound("Generation data-state record does not exist")
        state = generation_data_state_from_payload(record.payload)
        if state.generation_commitment != generation_commitment:
            raise ValueError("stored Generation data state does not match requested commitment")
        return GenerationDataStateSnapshot(state=state, state_version=record.state_version)

    def register_candidate(
        self,
        generation_commitment: TypedReference,
        expected_state_version: StateVersion,
        candidate_id: LogicalId,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> GenerationDataStateSnapshot:
        snapshot = self._load_expected(generation_commitment, expected_state_version)
        next_state = snapshot.state.add_candidate(candidate_id)
        return self._persist_transition(
            snapshot,
            next_state,
            authority_frontier,
            transition_id,
            "candidate-registered",
            EncodedPayload.from_object({"candidate_id": candidate_id.value}),
        )

    def seal_candidate(
        self,
        generation_commitment: TypedReference,
        expected_state_version: StateVersion,
        candidate_id: LogicalId,
        subject: SealedPhysicalSubject,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> GenerationDataStateSnapshot:
        snapshot = self._load_expected(generation_commitment, expected_state_version)
        if subject.topology != snapshot.state.topology:
            raise ValueError(
                "sealed physical subject topology does not match Generation commitment"
            )
        seal_id = subject.reference.commitment_snapshot_id
        if seal_id is None:
            raise AssertionError("sealed physical subject lost commitment snapshot identity")
        expected_reference = generation_physical_subject_reference(
            generation_commitment,
            candidate_id,
            seal_id,
        )
        if subject.reference != expected_reference:
            raise ValueError("sealed physical subject identity does not match Generation candidate")

        self._store.put_immutable_binding(
            reference=subject.reference,
            schema_version=_SCHEMA,
            payload=sealed_subject_to_payload(subject),
            authority_frontier=authority_frontier,
        )
        next_state = snapshot.state.seal_candidate(candidate_id, subject.reference)
        return self._persist_transition(
            snapshot,
            next_state,
            authority_frontier,
            transition_id,
            "candidate-sealed",
            EncodedPayload.from_object(
                {
                    "candidate_id": candidate_id.value,
                    "sealed_subject_reference": subject.reference.require_exact_binding()[1],
                }
            ),
        )

    def promote_owner_validated_candidate(
        self,
        generation_commitment: TypedReference,
        expected_state_version: StateVersion,
        candidate_id: LogicalId,
        output_id: LogicalId,
        completion_basis_references: tuple[TypedReference, ...],
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> GenerationDataStateSnapshot:
        snapshot = self._load_expected(generation_commitment, expected_state_version)
        candidate = snapshot.state.candidate(candidate_id)
        if candidate.sealed_subject_reference is None:
            raise ValueError("candidate has no sealed physical subject")
        resolution = self._store.resolve_immutable_binding(candidate.sealed_subject_reference)
        if resolution.status is not ResolutionStatus.RESOLVED or resolution.record is None:
            raise ValueError("sealed candidate subject is not exactly resolvable")
        subject = sealed_subject_from_payload(resolution.record.payload)
        if subject.reference != candidate.sealed_subject_reference:
            raise ValueError("resolved physical subject identity does not match candidate binding")
        if subject.topology != snapshot.state.topology:
            raise ValueError(
                "resolved physical subject topology does not match Generation commitment"
            )

        next_state = snapshot.state.promote_owner_validated_candidate(
            candidate_id=candidate_id,
            output_id=output_id,
            completion_basis_references=completion_basis_references,
        )
        return self._persist_transition(
            snapshot,
            next_state,
            authority_frontier,
            transition_id,
            "candidate-promoted",
            EncodedPayload.from_object(
                {
                    "candidate_id": candidate_id.value,
                    "output_id": output_id.value,
                }
            ),
        )

    def quarantine_candidate(
        self,
        generation_commitment: TypedReference,
        expected_state_version: StateVersion,
        candidate_id: LogicalId,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> GenerationDataStateSnapshot:
        snapshot = self._load_expected(generation_commitment, expected_state_version)
        return self._persist_transition(
            snapshot,
            snapshot.state.quarantine_candidate(candidate_id),
            authority_frontier,
            transition_id,
            "candidate-quarantined",
            EncodedPayload.from_object({"candidate_id": candidate_id.value}),
        )

    def abandon_candidate(
        self,
        generation_commitment: TypedReference,
        expected_state_version: StateVersion,
        candidate_id: LogicalId,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> GenerationDataStateSnapshot:
        snapshot = self._load_expected(generation_commitment, expected_state_version)
        return self._persist_transition(
            snapshot,
            snapshot.state.abandon_candidate(candidate_id),
            authority_frontier,
            transition_id,
            "candidate-abandoned",
            EncodedPayload.from_object({"candidate_id": candidate_id.value}),
        )

    def _load_expected(
        self,
        generation_commitment: TypedReference,
        expected_state_version: StateVersion,
    ) -> GenerationDataStateSnapshot:
        snapshot = self.load(generation_commitment)
        if snapshot.state_version != expected_state_version:
            raise CurrentStateConflict(
                f"expected Generation data-state version {expected_state_version.value}, "
                f"found {snapshot.state_version.value}"
            )
        return snapshot

    def _persist_transition(
        self,
        snapshot: GenerationDataStateSnapshot,
        next_state: GenerationDataState,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
        transition_kind: str,
        transition_detail: EncodedPayload,
    ) -> GenerationDataStateSnapshot:
        record = self._store.compare_and_swap_current_state(
            key=generation_data_state_key(snapshot.state.generation_commitment),
            expected_state_version=snapshot.state_version,
            authority_frontier=authority_frontier,
            schema_version=_SCHEMA,
            payload=generation_data_state_to_payload(next_state),
            transition_id=transition_id,
            transition_kind=transition_kind,
            transition_detail=transition_detail,
        )
        return GenerationDataStateSnapshot(
            state=generation_data_state_from_payload(record.payload),
            state_version=record.state_version,
        )
