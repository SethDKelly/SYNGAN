"""Typed Provenance, historical-read, and derived reproducibility primitives."""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import StrEnum

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


def _token(value: str, label: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{label} must be non-empty")
    if any(character.isspace() for character in normalized):
        raise ValueError(f"{label} must not contain whitespace")
    return normalized


def _reference_object(reference: TypedReference) -> JsonObject:
    return EncodedPayload(encode_reference(reference)).as_object()


def _reference_from_value(value: JsonValue, label: str) -> TypedReference:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be a reference object")
    return decode_reference(EncodedPayload.from_object(value).json_text)


class ProvenanceRelationship(StrEnum):
    PRODUCED_BY = "produced-by"
    ANSWERS_CRITERION = "answers-criterion"
    EVALUATED_SUBJECT = "evaluated-subject"
    BOUND_BY = "bound-by"
    DERIVED_FROM = "derived-from"
    USED = "used"
    DEPENDED_ON = "depended-on"
    REALIZED_BY = "realized-by"
    RECOVERED_FROM = "recovered-from"
    RESUMED_FROM = "resumed-from"
    USED_FOR_COMPLETION = "used-for-completion"
    SUPERSEDES = "supersedes"


class HistoricalKnowledgeBasis(StrEnum):
    DIRECT = "direct"
    RECONSTRUCTED = "reconstructed"
    PARTIAL = "partial"
    UNKNOWN = "unknown"


class ProvenanceStatus(StrEnum):
    ACTIVE = "active"
    SUPERSEDED = "superseded"
    INVALIDATED = "invalidated"


class HistoricalResolution(StrEnum):
    RESOLVED = "resolved"
    KNOWN_UNAVAILABLE = "known-unavailable"
    UNKNOWN = "unknown"
    INVALID = "invalid"
    WITHHELD = "withheld"


class ReproductionClass(StrEnum):
    EXACT_DETERMINISTIC = "exact-deterministic"
    SEMANTIC = "semantic"
    STATISTICAL = "statistical"
    BOUNDED_APPROXIMATE = "bounded-approximate"
    COMPARATIVE = "comparative"
    NOT_REPRODUCIBLE = "not-reproducible"


class CurrentFeasibility(StrEnum):
    FEASIBLE = "feasible"
    INFEASIBLE = "infeasible"
    INDETERMINATE = "indeterminate"


class Assessability(StrEnum):
    COMPLETE = "complete"
    LIMITED = "limited"
    INDETERMINATE = "indeterminate"


@dataclass(frozen=True, slots=True)
class ProvenanceAssertion:
    reference: TypedReference
    relationship: ProvenanceRelationship
    subject_references: tuple[TypedReference, ...]
    object_references: tuple[TypedReference, ...]
    basis: HistoricalKnowledgeBasis
    qualifiers: EncodedPayload

    def __post_init__(self) -> None:
        self.reference.require_exact_binding()
        if not self.subject_references or not self.object_references:
            raise ValueError("Provenance assertion requires subject and object references")
        for reference in (*self.subject_references, *self.object_references):
            reference.require_exact_binding()
        if self.basis is HistoricalKnowledgeBasis.UNKNOWN:
            raise ValueError("unknown basis cannot establish canonical Provenance")


@dataclass(frozen=True, slots=True)
class ProvenanceAssertionState:
    assertion_reference: TypedReference
    status: ProvenanceStatus = ProvenanceStatus.ACTIVE
    reasons: tuple[str, ...] = ()
    replacement_reference: TypedReference | None = None

    def __post_init__(self) -> None:
        self.assertion_reference.require_exact_binding()
        if self.replacement_reference is not None:
            self.replacement_reference.require_exact_binding()

    def with_status(
        self,
        status: ProvenanceStatus,
        *,
        reasons: tuple[str, ...] = (),
        replacement_reference: TypedReference | None = None,
    ) -> ProvenanceAssertionState:
        if status is ProvenanceStatus.ACTIVE and (reasons or replacement_reference is not None):
            raise ValueError("active Provenance assertion cannot carry correction metadata")
        return replace(
            self,
            status=status,
            reasons=reasons,
            replacement_reference=replacement_reference,
        )


@dataclass(frozen=True, slots=True)
class HistoricalReferenceView:
    reference: TypedReference
    knowledge_basis: HistoricalKnowledgeBasis
    resolution: HistoricalResolution
    payload: EncodedPayload | None = None

    def __post_init__(self) -> None:
        self.reference.require_exact_binding()
        if self.resolution is HistoricalResolution.RESOLVED and self.payload is None:
            raise ValueError("resolved historical reference requires payload")
        if self.resolution is not HistoricalResolution.RESOLVED and self.payload is not None:
            raise ValueError("unresolved historical reference cannot carry payload")


@dataclass(frozen=True, slots=True)
class HistoricalAssertionView:
    assertion: ProvenanceAssertion
    state: ProvenanceAssertionState
    subjects: tuple[HistoricalReferenceView, ...]
    objects: tuple[HistoricalReferenceView, ...]


@dataclass(frozen=True, slots=True)
class ReproducibilityAssessment:
    target_reference: TypedReference
    historical_supportability: ReproductionClass
    current_feasibility: CurrentFeasibility
    assessability: Assessability
    reasons: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        self.target_reference.require_exact_binding()


def provenance_reference(
    scope_reference: TypedReference,
    assertion_id: LogicalId,
) -> TypedReference:
    scope_reference.require_exact_binding()
    return TypedReference(
        key=ResourceKey(
            scope=scope_reference.key.scope,
            kind=ResourceKind("provenance-assertion"),
            resource_id=assertion_id,
        ),
        commitment_snapshot_id=CommitmentSnapshotId(f"assertion-{assertion_id.value}"),
    )


def provenance_state_key(reference: TypedReference) -> ResourceKey:
    reference.require_exact_binding()
    return ResourceKey(
        scope=reference.key.scope,
        kind=ResourceKind("provenance-status"),
        resource_id=reference.key.resource_id,
    )


def provenance_to_payload(assertion: ProvenanceAssertion) -> EncodedPayload:
    return EncodedPayload.from_object(
        {
            "reference": _reference_object(assertion.reference),
            "relationship": assertion.relationship.value,
            "subject_references": [
                _reference_object(reference) for reference in assertion.subject_references
            ],
            "object_references": [
                _reference_object(reference) for reference in assertion.object_references
            ],
            "basis": assertion.basis.value,
            "qualifiers": assertion.qualifiers.as_object(),
        }
    )


def provenance_from_payload(payload: EncodedPayload) -> ProvenanceAssertion:
    value = payload.as_object()
    relationship = value.get("relationship")
    subjects = value.get("subject_references")
    objects = value.get("object_references")
    basis = value.get("basis")
    qualifiers = value.get("qualifiers")
    if not isinstance(relationship, str) or not isinstance(basis, str):
        raise ValueError("Provenance relationship/basis are malformed")
    if not isinstance(subjects, list) or not isinstance(objects, list):
        raise ValueError("Provenance reference collections must be lists")
    if not isinstance(qualifiers, dict):
        raise ValueError("Provenance qualifiers must be an object")
    return ProvenanceAssertion(
        reference=_reference_from_value(value.get("reference"), "Provenance reference"),
        relationship=ProvenanceRelationship(relationship),
        subject_references=tuple(
            _reference_from_value(item, "Provenance subject") for item in subjects
        ),
        object_references=tuple(
            _reference_from_value(item, "Provenance object") for item in objects
        ),
        basis=HistoricalKnowledgeBasis(basis),
        qualifiers=EncodedPayload.from_object(qualifiers),
    )


def provenance_state_to_payload(state: ProvenanceAssertionState) -> EncodedPayload:
    return EncodedPayload.from_object(
        {
            "assertion_reference": _reference_object(state.assertion_reference),
            "status": state.status.value,
            "reasons": list(state.reasons),
            "replacement_reference": (
                _reference_object(state.replacement_reference)
                if state.replacement_reference is not None
                else None
            ),
        }
    )


def provenance_state_from_payload(payload: EncodedPayload) -> ProvenanceAssertionState:
    value = payload.as_object()
    status = value.get("status")
    reasons = value.get("reasons")
    replacement = value.get("replacement_reference")
    if not isinstance(status, str) or not isinstance(reasons, list):
        raise ValueError("Provenance state is malformed")
    return ProvenanceAssertionState(
        assertion_reference=_reference_from_value(
            value.get("assertion_reference"), "Provenance assertion"
        ),
        status=ProvenanceStatus(status),
        reasons=tuple(str(item) for item in reasons),
        replacement_reference=(
            _reference_from_value(replacement, "replacement Provenance")
            if replacement is not None
            else None
        ),
    )
