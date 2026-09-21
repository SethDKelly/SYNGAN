"""Evaluation semantic validation and durable Evidence finding primitives."""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import StrEnum
from hashlib import sha256

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


class EvaluationStatus(StrEnum):
    COMMITTED = "committed"
    EVALUATING = "evaluating"
    COMPLETED = "completed"
    COMPLETED_WITH_LIMITATIONS = "completed-with-limitations"
    FAILED = "failed"
    CANCELLED = "cancelled"


class FindingDisposition(StrEnum):
    SATISFIED = "satisfied"
    VIOLATED = "violated"
    ESTIMATE = "estimate"
    COMPARATIVE = "comparative"
    RISK = "risk"
    INDETERMINATE = "indeterminate"
    DIAGNOSTIC = "diagnostic"


class ClaimStrength(StrEnum):
    EXHAUSTIVE = "exhaustive"
    DETERMINISTIC_BOUNDED = "deterministic-bounded"
    STATISTICAL = "statistical"
    APPROXIMATE = "approximate"
    DIAGNOSTIC = "diagnostic"
    INDETERMINATE = "indeterminate"


class EvidenceApplicability(StrEnum):
    APPLICABLE = "applicable"
    SUPERSEDED = "superseded"
    STALE = "stale"
    INAPPLICABLE = "inapplicable"
    INVALIDATED = "invalidated"


@dataclass(frozen=True, slots=True)
class EvaluationAggregate:
    evaluation_commitment: TypedReference
    criterion_references: tuple[TypedReference, ...]
    subject_reference: TypedReference
    method_reference: TypedReference
    baseline_references: tuple[TypedReference, ...] = ()
    status: EvaluationStatus = EvaluationStatus.COMMITTED
    evidence_references: tuple[TypedReference, ...] = ()
    limitations: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        self.evaluation_commitment.require_exact_binding()
        self.subject_reference.require_exact_binding()
        self.method_reference.require_exact_binding()
        if not self.criterion_references:
            raise ValueError("Evaluation requires at least one Criterion reference")
        for reference in (
            *self.criterion_references,
            *self.baseline_references,
            *self.evidence_references,
        ):
            reference.require_exact_binding()
        if len(set(self.criterion_references)) != len(self.criterion_references):
            raise ValueError("Evaluation Criterion references must be unique")
        if len(set(self.evidence_references)) != len(self.evidence_references):
            raise ValueError("Evaluation Evidence references must be unique")
        if (
            self.status
            in {
                EvaluationStatus.COMPLETED,
                EvaluationStatus.COMPLETED_WITH_LIMITATIONS,
            }
            and not self.evidence_references
        ):
            raise ValueError("completed Evidence-producing Evaluation requires Evidence")

    @property
    def terminal(self) -> bool:
        return self.status in {
            EvaluationStatus.COMPLETED,
            EvaluationStatus.COMPLETED_WITH_LIMITATIONS,
            EvaluationStatus.FAILED,
            EvaluationStatus.CANCELLED,
        }

    def activate(self) -> EvaluationAggregate:
        if self.status is not EvaluationStatus.COMMITTED:
            raise ValueError("only committed Evaluation may become evaluating")
        return replace(self, status=EvaluationStatus.EVALUATING)

    def complete(
        self,
        evidence_references: tuple[TypedReference, ...],
        *,
        limitations: tuple[str, ...] = (),
    ) -> EvaluationAggregate:
        if self.status not in {
            EvaluationStatus.COMMITTED,
            EvaluationStatus.EVALUATING,
        }:
            raise ValueError("Evaluation is not eligible for completion")
        if not evidence_references:
            raise ValueError("completed Evidence-producing Evaluation requires findings")
        for reference in evidence_references:
            reference.require_exact_binding()
        status = (
            EvaluationStatus.COMPLETED_WITH_LIMITATIONS
            if limitations
            else EvaluationStatus.COMPLETED
        )
        return replace(
            self,
            status=status,
            evidence_references=evidence_references,
            limitations=limitations,
        )

    def fail(self) -> EvaluationAggregate:
        if self.terminal:
            raise ValueError("terminal Evaluation cannot fail again")
        return replace(self, status=EvaluationStatus.FAILED)

    def cancel(self) -> EvaluationAggregate:
        if self.terminal:
            raise ValueError("terminal Evaluation cannot be cancelled")
        return replace(self, status=EvaluationStatus.CANCELLED)


@dataclass(frozen=True, slots=True)
class FindingDraft:
    slot: str
    criterion_reference: TypedReference
    disposition: FindingDisposition
    result: EncodedPayload
    logical_scope: str
    claim_strength: ClaimStrength
    supported_claim_strengths: tuple[ClaimStrength, ...]
    uncertainty: EncodedPayload | None = None
    limitations: tuple[str, ...] = ()
    baseline_references: tuple[TypedReference, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "slot", _token(self.slot, "finding slot"))
        object.__setattr__(
            self,
            "logical_scope",
            _token(self.logical_scope, "finding logical scope"),
        )
        self.criterion_reference.require_exact_binding()
        for reference in self.baseline_references:
            reference.require_exact_binding()
        if not self.supported_claim_strengths:
            raise ValueError("finding must declare supported claim strengths")
        if self.claim_strength not in self.supported_claim_strengths:
            raise ValueError("finding claim strength exceeds normalized method support")


@dataclass(frozen=True, slots=True)
class EvaluationResult:
    evaluation_commitment: TypedReference
    criterion_references: tuple[TypedReference, ...]
    subject_reference: TypedReference
    method_reference: TypedReference
    findings: tuple[FindingDraft, ...]
    assumptions_valid: bool
    interpretable: bool
    limitations: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        self.evaluation_commitment.require_exact_binding()
        self.subject_reference.require_exact_binding()
        self.method_reference.require_exact_binding()
        for reference in self.criterion_references:
            reference.require_exact_binding()
        slots = tuple(finding.slot for finding in self.findings)
        if len(set(slots)) != len(slots):
            raise ValueError("Evaluation result finding slots must be unique")


@dataclass(frozen=True, slots=True)
class EvidenceFinding:
    reference: TypedReference
    producing_evaluation: TypedReference
    criterion_reference: TypedReference
    subject_reference: TypedReference
    method_reference: TypedReference
    slot: str
    disposition: FindingDisposition
    result: EncodedPayload
    logical_scope: str
    claim_strength: ClaimStrength
    uncertainty: EncodedPayload | None = None
    limitations: tuple[str, ...] = ()
    baseline_references: tuple[TypedReference, ...] = ()

    def __post_init__(self) -> None:
        self.reference.require_exact_binding()
        self.producing_evaluation.require_exact_binding()
        self.criterion_reference.require_exact_binding()
        self.subject_reference.require_exact_binding()
        self.method_reference.require_exact_binding()
        object.__setattr__(self, "slot", _token(self.slot, "finding slot"))
        object.__setattr__(
            self,
            "logical_scope",
            _token(self.logical_scope, "finding logical scope"),
        )
        for reference in self.baseline_references:
            reference.require_exact_binding()


@dataclass(frozen=True, slots=True)
class EvidenceApplicabilityState:
    evidence_reference: TypedReference
    status: EvidenceApplicability = EvidenceApplicability.APPLICABLE
    reasons: tuple[str, ...] = ()
    replacement_references: tuple[TypedReference, ...] = ()

    def __post_init__(self) -> None:
        self.evidence_reference.require_exact_binding()
        for reference in self.replacement_references:
            reference.require_exact_binding()

    def with_status(
        self,
        status: EvidenceApplicability,
        *,
        reasons: tuple[str, ...] = (),
        replacement_references: tuple[TypedReference, ...] = (),
    ) -> EvidenceApplicabilityState:
        if status is EvidenceApplicability.APPLICABLE:
            if reasons or replacement_references:
                raise ValueError("applicable Evidence cannot carry replacement reasons")
        return replace(
            self,
            status=status,
            reasons=reasons,
            replacement_references=replacement_references,
        )


def evaluation_state_key(reference: TypedReference) -> ResourceKey:
    reference.require_exact_binding()
    return ResourceKey(
        scope=reference.key.scope,
        kind=ResourceKind("evaluation"),
        resource_id=reference.key.resource_id,
    )


def _finding_identity(evaluation_reference: TypedReference, slot: str) -> str:
    exact_kind, exact_id = evaluation_reference.require_exact_binding()
    raw = "|".join(
        (
            evaluation_reference.key.scope.value,
            evaluation_reference.key.kind.value,
            evaluation_reference.key.resource_id.value,
            exact_kind,
            exact_id,
            _token(slot, "finding slot"),
        )
    )
    return sha256(raw.encode("utf-8")).hexdigest()[:32]


def evidence_reference(
    evaluation_reference: TypedReference,
    slot: str,
) -> TypedReference:
    token = _finding_identity(evaluation_reference, slot)
    return TypedReference(
        key=ResourceKey(
            scope=evaluation_reference.key.scope,
            kind=ResourceKind("evidence"),
            resource_id=LogicalId(f"evidence-{token}"),
        ),
        commitment_snapshot_id=CommitmentSnapshotId(f"finding-{token}"),
    )


def evidence_applicability_key(reference: TypedReference) -> ResourceKey:
    reference.require_exact_binding()
    return ResourceKey(
        scope=reference.key.scope,
        kind=ResourceKind("evidence-applicability"),
        resource_id=reference.key.resource_id,
    )


def evaluation_to_payload(state: EvaluationAggregate) -> EncodedPayload:
    return EncodedPayload.from_object(
        {
            "evaluation_commitment": _reference_object(state.evaluation_commitment),
            "criterion_references": [
                _reference_object(reference) for reference in state.criterion_references
            ],
            "subject_reference": _reference_object(state.subject_reference),
            "method_reference": _reference_object(state.method_reference),
            "baseline_references": [
                _reference_object(reference) for reference in state.baseline_references
            ],
            "status": state.status.value,
            "evidence_references": [
                _reference_object(reference) for reference in state.evidence_references
            ],
            "limitations": list(state.limitations),
        }
    )


def evaluation_from_payload(payload: EncodedPayload) -> EvaluationAggregate:
    value = payload.as_object()
    criteria = value.get("criterion_references")
    baselines = value.get("baseline_references")
    evidence = value.get("evidence_references")
    limitations = value.get("limitations")
    status = value.get("status")
    if not isinstance(criteria, list) or not isinstance(baselines, list):
        raise ValueError("Evaluation reference collections must be lists")
    if not isinstance(evidence, list) or not isinstance(limitations, list):
        raise ValueError("Evaluation Evidence/limitations must be lists")
    if not isinstance(status, str) or not all(isinstance(item, str) for item in limitations):
        raise ValueError("Evaluation status/limitations are malformed")
    return EvaluationAggregate(
        evaluation_commitment=_reference_from_value(
            value.get("evaluation_commitment"), "Evaluation commitment"
        ),
        criterion_references=tuple(
            _reference_from_value(item, "Criterion reference") for item in criteria
        ),
        subject_reference=_reference_from_value(value.get("subject_reference"), "subject"),
        method_reference=_reference_from_value(value.get("method_reference"), "method"),
        baseline_references=tuple(
            _reference_from_value(item, "baseline reference") for item in baselines
        ),
        status=EvaluationStatus(status),
        evidence_references=tuple(
            _reference_from_value(item, "Evidence reference") for item in evidence
        ),
        limitations=tuple(str(item) for item in limitations),
    )


def evidence_to_payload(finding: EvidenceFinding) -> EncodedPayload:
    return EncodedPayload.from_object(
        {
            "reference": _reference_object(finding.reference),
            "producing_evaluation": _reference_object(finding.producing_evaluation),
            "criterion_reference": _reference_object(finding.criterion_reference),
            "subject_reference": _reference_object(finding.subject_reference),
            "method_reference": _reference_object(finding.method_reference),
            "slot": finding.slot,
            "disposition": finding.disposition.value,
            "result": finding.result.as_object(),
            "logical_scope": finding.logical_scope,
            "claim_strength": finding.claim_strength.value,
            "uncertainty": (
                finding.uncertainty.as_object() if finding.uncertainty is not None else None
            ),
            "limitations": list(finding.limitations),
            "baseline_references": [
                _reference_object(reference) for reference in finding.baseline_references
            ],
        }
    )


def evidence_from_payload(payload: EncodedPayload) -> EvidenceFinding:
    value = payload.as_object()
    baselines = value.get("baseline_references")
    limitations = value.get("limitations")
    result = value.get("result")
    uncertainty = value.get("uncertainty")
    if not isinstance(baselines, list) or not isinstance(limitations, list):
        raise ValueError("Evidence baseline/limitations must be lists")
    if not isinstance(result, dict):
        raise ValueError("Evidence result must be an object")
    if uncertainty is not None and not isinstance(uncertainty, dict):
        raise ValueError("Evidence uncertainty must be an object or null")
    slot = value.get("slot")
    scope = value.get("logical_scope")
    disposition = value.get("disposition")
    strength = value.get("claim_strength")
    if not all(isinstance(item, str) for item in (slot, scope, disposition, strength)):
        raise ValueError("Evidence scalar fields are malformed")
    return EvidenceFinding(
        reference=_reference_from_value(value.get("reference"), "Evidence reference"),
        producing_evaluation=_reference_from_value(
            value.get("producing_evaluation"), "producing Evaluation"
        ),
        criterion_reference=_reference_from_value(value.get("criterion_reference"), "Criterion"),
        subject_reference=_reference_from_value(value.get("subject_reference"), "subject"),
        method_reference=_reference_from_value(value.get("method_reference"), "method"),
        slot=str(slot),
        disposition=FindingDisposition(str(disposition)),
        result=EncodedPayload.from_object(result),
        logical_scope=str(scope),
        claim_strength=ClaimStrength(str(strength)),
        uncertainty=(EncodedPayload.from_object(uncertainty) if uncertainty is not None else None),
        limitations=tuple(str(item) for item in limitations),
        baseline_references=tuple(
            _reference_from_value(item, "baseline reference") for item in baselines
        ),
    )


def applicability_to_payload(state: EvidenceApplicabilityState) -> EncodedPayload:
    return EncodedPayload.from_object(
        {
            "evidence_reference": _reference_object(state.evidence_reference),
            "status": state.status.value,
            "reasons": list(state.reasons),
            "replacement_references": [
                _reference_object(reference) for reference in state.replacement_references
            ],
        }
    )


def applicability_from_payload(payload: EncodedPayload) -> EvidenceApplicabilityState:
    value = payload.as_object()
    status = value.get("status")
    reasons = value.get("reasons")
    replacements = value.get("replacement_references")
    if not isinstance(status, str) or not isinstance(reasons, list):
        raise ValueError("Evidence applicability status/reasons are malformed")
    if not isinstance(replacements, list):
        raise ValueError("Evidence replacement references must be a list")
    return EvidenceApplicabilityState(
        evidence_reference=_reference_from_value(
            value.get("evidence_reference"), "Evidence reference"
        ),
        status=EvidenceApplicability(status),
        reasons=tuple(str(item) for item in reasons),
        replacement_references=tuple(
            _reference_from_value(item, "replacement Evidence") for item in replacements
        ),
    )
