"""Generation-owned candidate and completed-output representation state."""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import StrEnum

from syngan.foundation.data_state import (
    TopologyDescriptor,
    topology_from_payload,
    topology_to_payload,
)
from syngan.foundation.identity import (
    CommitmentSnapshotId,
    LogicalId,
    ResourceKey,
    ResourceKind,
    TypedReference,
)
from syngan.foundation.representation import (
    EncodedPayload,
    JsonObject,
    JsonValue,
    decode_reference,
    encode_reference,
)

_GENERATION_DATA_STATE_KIND = ResourceKind("generation-data-state")
_GENERATION_PHYSICAL_SUBJECT_KIND = ResourceKind("generation-physical-subject")


def _reference_object(reference: TypedReference) -> JsonObject:
    return EncodedPayload(encode_reference(reference)).as_object()


def _reference_from_value(value: JsonValue, label: str) -> TypedReference:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be a reference object")
    return decode_reference(EncodedPayload.from_object(value).json_text)


class CandidateStatus(StrEnum):
    OPEN = "open"
    SEALED = "sealed"
    QUARANTINED = "quarantined"
    ABANDONED = "abandoned"
    PROMOTED = "promoted"


@dataclass(frozen=True, slots=True)
class GenerationCandidate:
    candidate_id: LogicalId
    status: CandidateStatus
    sealed_subject_reference: TypedReference | None = None

    def __post_init__(self) -> None:
        if self.status in {CandidateStatus.SEALED, CandidateStatus.PROMOTED}:
            if self.sealed_subject_reference is None:
                raise ValueError(
                    f"{self.status.value} candidate requires a sealed subject reference"
                )
        if self.sealed_subject_reference is not None:
            if self.sealed_subject_reference.commitment_snapshot_id is None:
                raise ValueError("candidate sealed subject must use an exact commitment snapshot")
            if self.sealed_subject_reference.revision_id is not None:
                raise ValueError("candidate sealed subject cannot use semantic revision identity")


@dataclass(frozen=True, slots=True)
class CompletedOutputBinding:
    output_id: LogicalId
    candidate_id: LogicalId
    sealed_subject_reference: TypedReference
    completion_basis_references: tuple[TypedReference, ...]

    def __post_init__(self) -> None:
        if not self.sealed_subject_reference.is_exact_binding:
            raise ValueError("completed output must bind an exact sealed physical subject")
        if not all(reference.is_exact_binding for reference in self.completion_basis_references):
            raise ValueError("completion basis references must be exact")


@dataclass(frozen=True, slots=True)
class GenerationDataState:
    generation_commitment: TypedReference
    topology: TopologyDescriptor
    candidates: tuple[GenerationCandidate, ...] = ()
    completed_output: CompletedOutputBinding | None = None

    def __post_init__(self) -> None:
        if not self.generation_commitment.is_exact_binding:
            raise ValueError("Generation data state requires an exact Generation commitment")
        self.topology.require_semantic_role("data-meaning")
        candidate_ids = tuple(candidate.candidate_id.value for candidate in self.candidates)
        if len(set(candidate_ids)) != len(candidate_ids):
            raise ValueError("Generation candidate ids must be unique")
        if self.completed_output is not None:
            matches = [
                candidate
                for candidate in self.candidates
                if candidate.candidate_id == self.completed_output.candidate_id
            ]
            if len(matches) != 1:
                raise ValueError("completed output candidate must exist exactly once")
            candidate = matches[0]
            if candidate.status is not CandidateStatus.PROMOTED:
                raise ValueError("completed output candidate must be promoted")
            if candidate.sealed_subject_reference != self.completed_output.sealed_subject_reference:
                raise ValueError("completed output must retain the promoted candidate subject")

    def candidate(self, candidate_id: LogicalId) -> GenerationCandidate:
        for candidate in self.candidates:
            if candidate.candidate_id == candidate_id:
                return candidate
        raise ValueError(f"unknown Generation candidate: {candidate_id.value}")

    def add_candidate(self, candidate_id: LogicalId) -> GenerationDataState:
        if any(candidate.candidate_id == candidate_id for candidate in self.candidates):
            raise ValueError(f"Generation candidate already exists: {candidate_id.value}")
        return replace(
            self,
            candidates=(
                *self.candidates,
                GenerationCandidate(candidate_id=candidate_id, status=CandidateStatus.OPEN),
            ),
        )

    def seal_candidate(
        self,
        candidate_id: LogicalId,
        sealed_subject_reference: TypedReference,
    ) -> GenerationDataState:
        candidate = self.candidate(candidate_id)
        if candidate.status is not CandidateStatus.OPEN:
            raise ValueError("only an open candidate can be sealed")
        updated = replace(
            candidate,
            status=CandidateStatus.SEALED,
            sealed_subject_reference=sealed_subject_reference,
        )
        return self._replace_candidate(updated)

    def quarantine_candidate(self, candidate_id: LogicalId) -> GenerationDataState:
        candidate = self.candidate(candidate_id)
        if candidate.status is CandidateStatus.PROMOTED:
            raise ValueError("a promoted candidate cannot be quarantined")
        return self._replace_candidate(replace(candidate, status=CandidateStatus.QUARANTINED))

    def abandon_candidate(self, candidate_id: LogicalId) -> GenerationDataState:
        candidate = self.candidate(candidate_id)
        if candidate.status is CandidateStatus.PROMOTED:
            raise ValueError("a promoted candidate cannot be abandoned")
        return self._replace_candidate(replace(candidate, status=CandidateStatus.ABANDONED))

    def promote_owner_validated_candidate(
        self,
        candidate_id: LogicalId,
        output_id: LogicalId,
        completion_basis_references: tuple[TypedReference, ...] = (),
    ) -> GenerationDataState:
        if self.completed_output is not None:
            raise ValueError("Generation already has a completed output")
        candidate = self.candidate(candidate_id)
        if candidate.status is not CandidateStatus.SEALED:
            raise ValueError("only a sealed candidate can be promoted")
        if candidate.sealed_subject_reference is None:
            raise AssertionError("sealed candidate lost its exact physical subject")
        if not all(reference.is_exact_binding for reference in completion_basis_references):
            raise ValueError("completion basis references must be exact")

        promoted = replace(candidate, status=CandidateStatus.PROMOTED)
        completed = CompletedOutputBinding(
            output_id=output_id,
            candidate_id=candidate_id,
            sealed_subject_reference=candidate.sealed_subject_reference,
            completion_basis_references=completion_basis_references,
        )
        state = self._replace_candidate(promoted)
        return replace(state, completed_output=completed)

    def _replace_candidate(self, updated: GenerationCandidate) -> GenerationDataState:
        candidates = tuple(
            updated if candidate.candidate_id == updated.candidate_id else candidate
            for candidate in self.candidates
        )
        return replace(self, candidates=candidates)


def generation_data_state_key(generation_commitment: TypedReference) -> ResourceKey:
    return ResourceKey(
        scope=generation_commitment.key.scope,
        kind=_GENERATION_DATA_STATE_KIND,
        resource_id=generation_commitment.key.resource_id,
    )


def generation_physical_subject_reference(
    generation_commitment: TypedReference,
    candidate_id: LogicalId,
    seal_id: CommitmentSnapshotId,
) -> TypedReference:
    return TypedReference(
        key=ResourceKey(
            scope=generation_commitment.key.scope,
            kind=_GENERATION_PHYSICAL_SUBJECT_KIND,
            resource_id=candidate_id,
        ),
        commitment_snapshot_id=seal_id,
    )


def generation_data_state_to_payload(state: GenerationDataState) -> EncodedPayload:
    candidates: list[JsonValue] = []
    for candidate in state.candidates:
        candidates.append(
            {
                "candidate_id": candidate.candidate_id.value,
                "status": candidate.status.value,
                "sealed_subject_reference": (
                    _reference_object(candidate.sealed_subject_reference)
                    if candidate.sealed_subject_reference is not None
                    else None
                ),
            }
        )

    completed: JsonValue = None
    if state.completed_output is not None:
        completed = {
            "output_id": state.completed_output.output_id.value,
            "candidate_id": state.completed_output.candidate_id.value,
            "sealed_subject_reference": _reference_object(
                state.completed_output.sealed_subject_reference
            ),
            "completion_basis_references": [
                _reference_object(reference)
                for reference in state.completed_output.completion_basis_references
            ],
        }

    return EncodedPayload.from_object(
        {
            "generation_commitment": _reference_object(state.generation_commitment),
            "topology": topology_to_payload(state.topology).as_object(),
            "candidates": candidates,
            "completed_output": completed,
        }
    )


def generation_data_state_from_payload(payload: EncodedPayload) -> GenerationDataState:
    value = payload.as_object()
    topology_value = value.get("topology")
    candidates_value = value.get("candidates")
    completed_value = value.get("completed_output")
    if not isinstance(topology_value, dict):
        raise ValueError("Generation topology must be an object")
    if not isinstance(candidates_value, list):
        raise ValueError("Generation candidates must be a list")

    candidates: list[GenerationCandidate] = []
    for item in candidates_value:
        if not isinstance(item, dict):
            raise ValueError("Generation candidate must be an object")
        candidate_id = item.get("candidate_id")
        status = item.get("status")
        if not isinstance(candidate_id, str) or not isinstance(status, str):
            raise ValueError("Generation candidate id and status must be strings")
        subject_value = item.get("sealed_subject_reference")
        subject_reference = (
            _reference_from_value(subject_value, "candidate sealed subject")
            if subject_value is not None
            else None
        )
        candidates.append(
            GenerationCandidate(
                candidate_id=LogicalId(candidate_id),
                status=CandidateStatus(status),
                sealed_subject_reference=subject_reference,
            )
        )

    completed: CompletedOutputBinding | None = None
    if completed_value is not None:
        if not isinstance(completed_value, dict):
            raise ValueError("completed output must be an object or null")
        output_id = completed_value.get("output_id")
        candidate_id = completed_value.get("candidate_id")
        basis_value = completed_value.get("completion_basis_references")
        if not isinstance(output_id, str) or not isinstance(candidate_id, str):
            raise ValueError("completed output ids must be strings")
        if not isinstance(basis_value, list):
            raise ValueError("completion basis references must be a list")
        completed = CompletedOutputBinding(
            output_id=LogicalId(output_id),
            candidate_id=LogicalId(candidate_id),
            sealed_subject_reference=_reference_from_value(
                completed_value.get("sealed_subject_reference"),
                "completed output sealed subject",
            ),
            completion_basis_references=tuple(
                _reference_from_value(item, "completion basis reference") for item in basis_value
            ),
        )

    return GenerationDataState(
        generation_commitment=_reference_from_value(
            value.get("generation_commitment"), "Generation commitment"
        ),
        topology=topology_from_payload(
            EncodedPayload.from_object(topology_value)
        ),
        candidates=tuple(candidates),
        completed_output=completed,
    )
