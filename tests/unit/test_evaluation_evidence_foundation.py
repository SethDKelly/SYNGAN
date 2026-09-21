from __future__ import annotations

import pytest

from syngan.domain.evaluation_evidence import (
    ClaimStrength,
    EvidenceApplicability,
    EvidenceApplicabilityState,
    EvaluationAggregate,
    EvaluationStatus,
    FindingDisposition,
    FindingDraft,
    evidence_reference,
)
from syngan.domain.provenance import (
    HistoricalKnowledgeBasis,
    ProvenanceAssertion,
    ProvenanceRelationship,
    provenance_reference,
)
from syngan.foundation.identity import (
    AuthorityScope,
    CommitmentSnapshotId,
    LogicalId,
    ResourceKey,
    ResourceKind,
    SemanticRevisionId,
    TypedReference,
)
from syngan.foundation.representation import EncodedPayload

SCOPE = AuthorityScope("test")


def commitment(kind: str, resource_id: str) -> TypedReference:
    return TypedReference(
        key=ResourceKey(
            scope=SCOPE,
            kind=ResourceKind(kind),
            resource_id=LogicalId(resource_id),
        ),
        commitment_snapshot_id=CommitmentSnapshotId(f"{resource_id}-commitment"),
    )


def revision(kind: str, resource_id: str, revision_id: str = "r1") -> TypedReference:
    return TypedReference(
        key=ResourceKey(
            scope=SCOPE,
            kind=ResourceKind(kind),
            resource_id=LogicalId(resource_id),
        ),
        revision_id=SemanticRevisionId(revision_id),
    )


def evaluation() -> EvaluationAggregate:
    return EvaluationAggregate(
        evaluation_commitment=commitment("evaluation", "evaluation-1"),
        criterion_references=(revision("criterion", "criterion-1"),),
        subject_reference=commitment("generation-physical-subject", "subject-1"),
        method_reference=revision("evaluation-method", "method-1"),
        baseline_references=(commitment("baseline", "baseline-1"),),
    )


def test_completed_evaluation_requires_evidence() -> None:
    state = evaluation().activate()

    with pytest.raises(ValueError, match="requires findings"):
        state.complete(())


def test_negative_and_indeterminate_findings_are_valid_evidence_forms() -> None:
    criterion = revision("criterion", "criterion-1")

    violated = FindingDraft(
        slot="constraint-check",
        criterion_reference=criterion,
        disposition=FindingDisposition.VIOLATED,
        result=EncodedPayload.from_object({"violations": 2}),
        logical_scope="full-output",
        claim_strength=ClaimStrength.EXHAUSTIVE,
        supported_claim_strengths=(ClaimStrength.EXHAUSTIVE,),
    )
    indeterminate = FindingDraft(
        slot="risk-estimate",
        criterion_reference=criterion,
        disposition=FindingDisposition.INDETERMINATE,
        result=EncodedPayload.from_object({"estimate": 0.42}),
        logical_scope="sample",
        claim_strength=ClaimStrength.STATISTICAL,
        supported_claim_strengths=(ClaimStrength.STATISTICAL,),
        uncertainty=EncodedPayload.from_object({"confidence": 0.95}),
    )

    assert violated.disposition is FindingDisposition.VIOLATED
    assert indeterminate.disposition is FindingDisposition.INDETERMINATE


def test_finding_cannot_claim_unsupported_strength() -> None:
    with pytest.raises(ValueError, match="claim strength"):
        FindingDraft(
            slot="sample",
            criterion_reference=revision("criterion", "criterion-1"),
            disposition=FindingDisposition.SATISFIED,
            result=EncodedPayload.from_object({"violations": 0}),
            logical_scope="sample",
            claim_strength=ClaimStrength.EXHAUSTIVE,
            supported_claim_strengths=(ClaimStrength.STATISTICAL,),
        )


def test_evidence_identity_is_stable_per_evaluation_and_slot() -> None:
    reference = evaluation().evaluation_commitment

    first = evidence_reference(reference, "finding-a")
    repeated = evidence_reference(reference, "finding-a")
    other = evidence_reference(reference, "finding-b")

    assert first == repeated
    assert first != other
    assert first.is_exact_binding


def test_applicability_changes_do_not_change_evidence_identity() -> None:
    reference = evidence_reference(evaluation().evaluation_commitment, "finding-a")
    current = EvidenceApplicabilityState(reference)

    invalid = current.with_status(
        EvidenceApplicability.INVALIDATED,
        reasons=("method defect",),
    )

    assert invalid.evidence_reference == reference
    assert invalid.status is EvidenceApplicability.INVALIDATED
    assert current.status is EvidenceApplicability.APPLICABLE


def test_unknown_basis_cannot_establish_canonical_provenance() -> None:
    evidence = evidence_reference(evaluation().evaluation_commitment, "finding-a")
    assertion_ref = provenance_reference(evidence, LogicalId("assertion-1"))

    with pytest.raises(ValueError, match="unknown basis"):
        ProvenanceAssertion(
            reference=assertion_ref,
            relationship=ProvenanceRelationship.PRODUCED_BY,
            subject_references=(evidence,),
            object_references=(evaluation().evaluation_commitment,),
            basis=HistoricalKnowledgeBasis.UNKNOWN,
            qualifiers=EncodedPayload.from_object({}),
        )


def test_evaluation_completion_preserves_limitations() -> None:
    state = evaluation().activate()
    reference = evidence_reference(state.evaluation_commitment, "finding-a")

    completed = state.complete((reference,), limitations=("sampled",))

    assert completed.status is EvaluationStatus.COMPLETED_WITH_LIMITATIONS
    assert completed.limitations == ("sampled",)
