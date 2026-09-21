from __future__ import annotations

from pathlib import Path

import pytest

from syngan.adapters.sqlite_control_store import SQLiteControlStore
from syngan.application.evidence_history import EvidenceHistoryService
from syngan.domain.evaluation_evidence import (
    ClaimStrength,
    EvaluationAggregate,
    EvaluationResult,
    EvidenceApplicability,
    FindingDisposition,
    FindingDraft,
)
from syngan.domain.generation_data import GenerationDataState
from syngan.domain.provenance import (
    Assessability,
    CurrentFeasibility,
    HistoricalKnowledgeBasis,
    HistoricalResolution,
    ProvenanceAssertion,
    ProvenanceRelationship,
    ProvenanceStatus,
    ReproductionClass,
    provenance_reference,
)
from syngan.foundation.data_state import (
    LogicalScope,
    SemanticBinding,
    TopologyDescriptor,
)
from syngan.foundation.identity import (
    AuthorityScope,
    CommitmentSnapshotId,
    LogicalId,
    RecoveryFrontier,
    ResourceKey,
    ResourceKind,
    SemanticRevisionId,
    StateVersion,
    TypedReference,
)
from syngan.foundation.representation import EncodedPayload

pytestmark = pytest.mark.integration

SCOPE = AuthorityScope("test")
FRONTIER = RecoveryFrontier(0)


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


def result(*, limitations: tuple[str, ...] = ()) -> EvaluationResult:
    criterion = revision("criterion", "criterion-1")
    baseline = commitment("baseline", "baseline-1")
    return EvaluationResult(
        evaluation_commitment=commitment("evaluation", "evaluation-1"),
        criterion_references=(criterion,),
        subject_reference=commitment("generation-physical-subject", "subject-1"),
        method_reference=revision("evaluation-method", "method-1"),
        assumptions_valid=True,
        interpretable=True,
        limitations=limitations,
        findings=(
            FindingDraft(
                slot="constraint-check",
                criterion_reference=criterion,
                disposition=FindingDisposition.VIOLATED,
                result=EncodedPayload.from_object({"violations": 2}),
                logical_scope="full-output",
                claim_strength=ClaimStrength.EXHAUSTIVE,
                supported_claim_strengths=(ClaimStrength.EXHAUSTIVE,),
                baseline_references=(baseline,),
            ),
            FindingDraft(
                slot="risk-estimate",
                criterion_reference=criterion,
                disposition=FindingDisposition.INDETERMINATE,
                result=EncodedPayload.from_object({"estimate": 0.42}),
                logical_scope="sample",
                claim_strength=ClaimStrength.STATISTICAL,
                supported_claim_strengths=(ClaimStrength.STATISTICAL,),
                uncertainty=EncodedPayload.from_object({"confidence": 0.95}),
                limitations=("wide-interval",),
                baseline_references=(baseline,),
            ),
        ),
    )


def test_evaluation_establishes_multiple_evidence_with_required_provenance(
    tmp_path: Path,
) -> None:
    with SQLiteControlStore(tmp_path / "control.sqlite", SCOPE) as store:
        service = EvidenceHistoryService(store)
        snapshot = service.initialize_evaluation(
            evaluation(),
            FRONTIER,
            LogicalId("evaluation-create"),
        )
        snapshot = service.activate_evaluation(
            snapshot.state.evaluation_commitment,
            snapshot.state_version,
            FRONTIER,
            LogicalId("evaluation-active"),
        )

        completed, findings = service.complete_with_findings(
            snapshot.state.evaluation_commitment,
            snapshot.state_version,
            result(),
            FRONTIER,
            LogicalId("evaluation-complete"),
            LogicalId("evaluation-evidence-intent"),
        )

        assert len(findings) == 2
        assert len(completed.state.evidence_references) == 2
        assert completed.state.limitations == ("wide-interval",)
        assert findings[0].finding.disposition is FindingDisposition.VIOLATED
        assert findings[1].finding.disposition is FindingDisposition.INDETERMINATE
        assert findings[0].applicability.status is EvidenceApplicability.APPLICABLE

        evidence = findings[0].finding.reference
        expected_relationships = {
            "producer": ProvenanceRelationship.PRODUCED_BY,
            "criterion": ProvenanceRelationship.ANSWERS_CRITERION,
            "subject": ProvenanceRelationship.EVALUATED_SUBJECT,
        }
        assertions = {}
        for suffix, relationship in expected_relationships.items():
            assertion_id = LogicalId(f"{evidence.key.resource_id.value}-{suffix}")
            provenance_snapshot = service.load_provenance(
                provenance_reference(evidence, assertion_id)
            )
            assert provenance_snapshot.assertion.relationship is relationship
            assertions[suffix] = provenance_snapshot

        view = service.compose_assertion(assertions["producer"].assertion.reference)
        assert view.assertion.basis is HistoricalKnowledgeBasis.DIRECT
        assert view.subjects[0].resolution is HistoricalResolution.RESOLVED
        assert view.objects[0].resolution is HistoricalResolution.RESOLVED


def test_invalid_result_context_does_not_complete_evaluation(tmp_path: Path) -> None:
    bad = EvaluationResult(
        evaluation_commitment=commitment("evaluation", "evaluation-1"),
        criterion_references=(revision("criterion", "criterion-1"),),
        subject_reference=commitment("generation-physical-subject", "wrong-subject"),
        method_reference=revision("evaluation-method", "method-1"),
        findings=result().findings,
        assumptions_valid=True,
        interpretable=True,
    )

    with SQLiteControlStore(tmp_path / "control.sqlite", SCOPE) as store:
        service = EvidenceHistoryService(store)
        snapshot = service.initialize_evaluation(
            evaluation(),
            FRONTIER,
            LogicalId("evaluation-create"),
        )

        with pytest.raises(ValueError, match="subject"):
            service.complete_with_findings(
                snapshot.state.evaluation_commitment,
                snapshot.state_version,
                bad,
                FRONTIER,
                LogicalId("evaluation-complete"),
                LogicalId("evaluation-evidence-intent"),
            )

        current = service.load_evaluation(snapshot.state.evaluation_commitment)
        assert current.state_version == StateVersion(0)
        assert current.state.evidence_references == ()


def test_evidence_applicability_changes_without_rewriting_finding(tmp_path: Path) -> None:
    with SQLiteControlStore(tmp_path / "control.sqlite", SCOPE) as store:
        service = EvidenceHistoryService(store)
        snapshot = service.initialize_evaluation(
            evaluation(),
            FRONTIER,
            LogicalId("evaluation-create"),
        )
        completed, findings = service.complete_with_findings(
            snapshot.state.evaluation_commitment,
            snapshot.state_version,
            result(),
            FRONTIER,
            LogicalId("evaluation-complete"),
            LogicalId("evaluation-evidence-intent"),
        )
        assert completed.state.evidence_references

        before = findings[0]
        changed = service.change_evidence_applicability(
            before.finding.reference,
            before.applicability_state_version,
            EvidenceApplicability.INVALIDATED,
            FRONTIER,
            LogicalId("invalidate-evidence"),
            reasons=("method-defect",),
        )
        after = service.load_evidence(before.finding.reference)

        assert changed.applicability.status is EvidenceApplicability.INVALIDATED
        assert after.finding == before.finding
        assert after.applicability.reasons == ("method-defect",)


def test_generation_completion_basis_remains_exact_after_evidence_invalidation(
    tmp_path: Path,
) -> None:
    with SQLiteControlStore(tmp_path / "control.sqlite", SCOPE) as store:
        service = EvidenceHistoryService(store)
        snapshot = service.initialize_evaluation(
            evaluation(),
            FRONTIER,
            LogicalId("evaluation-create"),
        )
        _, findings = service.complete_with_findings(
            snapshot.state.evaluation_commitment,
            snapshot.state_version,
            result(),
            FRONTIER,
            LogicalId("evaluation-complete"),
            LogicalId("evaluation-evidence-intent"),
        )
        evidence = findings[0].finding.reference

        topology = TopologyDescriptor(
            scopes=(LogicalScope("rows"),),
            semantic_bindings=(
                SemanticBinding(
                    role="data-meaning",
                    reference=revision("data-meaning", "meaning-1"),
                    scope_ids=("rows",),
                ),
            ),
        )
        generation = GenerationDataState(
            generation_commitment=commitment("generation", "generation-1"),
            topology=topology,
        )
        candidate = LogicalId("candidate-1")
        generation = generation.add_candidate(candidate)
        sealed = commitment("generation-physical-subject", "candidate-1")
        generation = generation.seal_candidate(candidate, sealed)
        generation = generation.promote_owner_validated_candidate(
            candidate,
            LogicalId("output-1"),
            (evidence,),
        )

        use = service.record_generation_evidence_use(
            generation.generation_commitment,
            (evidence,),
            LogicalId("generation-evidence-use"),
            FRONTIER,
        )
        assert use.assertion.relationship is ProvenanceRelationship.USED_FOR_COMPLETION
        assert use.assertion.object_references == (evidence,)

        service.change_evidence_applicability(
            evidence,
            findings[0].applicability_state_version,
            EvidenceApplicability.INVALIDATED,
            FRONTIER,
            LogicalId("invalidate-evidence"),
            reasons=("later-defect",),
        )

        assert generation.completed_output is not None
        assert generation.completed_output.completion_basis_references == (evidence,)
        with pytest.raises(ValueError, match="not currently applicable"):
            service.resolve_applicable_evidence((evidence,))
        with pytest.raises(ValueError, match="not currently applicable"):
            service.record_generation_evidence_use(
                generation.generation_commitment,
                (evidence,),
                LogicalId("late-generation-evidence-use"),
                FRONTIER,
            )


def test_historical_resolution_and_reproducibility_keep_independent_axes(
    tmp_path: Path,
) -> None:
    with SQLiteControlStore(tmp_path / "control.sqlite", SCOPE) as store:
        service = EvidenceHistoryService(store)
        snapshot = service.initialize_evaluation(
            evaluation(),
            FRONTIER,
            LogicalId("evaluation-create"),
        )
        _, findings = service.complete_with_findings(
            snapshot.state.evaluation_commitment,
            snapshot.state_version,
            result(),
            FRONTIER,
            LogicalId("evaluation-complete"),
            LogicalId("evaluation-evidence-intent"),
        )
        evidence = findings[0].finding.reference

        direct = service.resolve_historical_reference(
            evidence,
            HistoricalKnowledgeBasis.DIRECT,
        )
        assert direct.resolution is HistoricalResolution.RESOLVED

        store.mark_immutable_binding_unavailable(evidence, FRONTIER)
        unavailable = service.resolve_historical_reference(
            evidence,
            HistoricalKnowledgeBasis.DIRECT,
        )
        assert unavailable.knowledge_basis is HistoricalKnowledgeBasis.DIRECT
        assert unavailable.resolution is HistoricalResolution.KNOWN_UNAVAILABLE

        assessment = service.assess_reproducibility(
            snapshot.state.evaluation_commitment,
            ReproductionClass.COMPARATIVE,
            (evidence,),
            historical_conditions_preserved=True,
            environment_eligible=True,
            assessability=Assessability.LIMITED,
        )
        assert assessment.historical_supportability is ReproductionClass.COMPARATIVE
        assert assessment.current_feasibility is CurrentFeasibility.INFEASIBLE
        assert assessment.assessability is Assessability.LIMITED


def test_missing_payload_is_unknown_not_historical_absence(tmp_path: Path) -> None:
    with SQLiteControlStore(tmp_path / "control.sqlite", SCOPE) as store:
        service = EvidenceHistoryService(store)
        reference = commitment("external-history", "known-id")

        view = service.resolve_historical_reference(
            reference,
            HistoricalKnowledgeBasis.RECONSTRUCTED,
        )

        assert view.knowledge_basis is HistoricalKnowledgeBasis.RECONSTRUCTED
        assert view.resolution is HistoricalResolution.UNKNOWN


def test_reconstructed_provenance_can_be_superseded_without_history_rewrite(
    tmp_path: Path,
) -> None:
    with SQLiteControlStore(tmp_path / "control.sqlite", SCOPE) as store:
        service = EvidenceHistoryService(store)
        source = commitment("historical-source", "source-1")
        target = commitment("historical-target", "target-1")

        first_ref = provenance_reference(source, LogicalId("reconstructed-1"))
        replacement_ref = provenance_reference(source, LogicalId("reconstructed-2"))
        first = ProvenanceAssertion(
            reference=first_ref,
            relationship=ProvenanceRelationship.DERIVED_FROM,
            subject_references=(target,),
            object_references=(source,),
            basis=HistoricalKnowledgeBasis.RECONSTRUCTED,
            qualifiers=EncodedPayload.from_object({"basis": "recovery-evidence"}),
        )
        replacement = ProvenanceAssertion(
            reference=replacement_ref,
            relationship=ProvenanceRelationship.DERIVED_FROM,
            subject_references=(target,),
            object_references=(source,),
            basis=HistoricalKnowledgeBasis.DIRECT,
            qualifiers=EncodedPayload.from_object({"basis": "canonical-record"}),
        )
        first_snapshot = service.record_provenance(first, FRONTIER)
        service.record_provenance(replacement, FRONTIER)

        changed = service.change_provenance_status(
            first_ref,
            first_snapshot.state_version,
            ProvenanceStatus.SUPERSEDED,
            FRONTIER,
            LogicalId("supersede-provenance"),
            reasons=("canonical-record-recovered",),
            replacement_reference=replacement_ref,
        )

        assert changed.state.status is ProvenanceStatus.SUPERSEDED
        assert changed.state.replacement_reference == replacement_ref
        retained = service.load_provenance(first_ref)
        assert retained.assertion == first
        assert retained.assertion.basis is HistoricalKnowledgeBasis.RECONSTRUCTED
