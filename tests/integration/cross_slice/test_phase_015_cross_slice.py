from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

import pytest

from syngan.adapters.sqlite_control_store import SQLiteControlStore
from syngan.application.evidence_history import EvidenceHistoryService
from syngan.application.platform_qualification import (
    assess_platform_compatibility,
    qualify_support,
)
from syngan.application.runtime_planning import (
    GenerationRuntimeContext,
    prepare_generation_plan,
)
from syngan.application.security import (
    SecurityCompatibilityError,
    SecurityService,
    ensure_dependency_profile_security,
)
from syngan.domain.evaluation_evidence import (
    ClaimStrength,
    EvaluationAggregate,
    EvaluationResult,
    EvidenceApplicability,
    FindingDisposition,
    FindingDraft,
)
from syngan.domain.execution import (
    AttemptStatus,
    ExecutionAggregate,
    ExecutionStatus,
    ProviderObservation,
)
from syngan.domain.generation_data import GenerationDataState
from syngan.domain.learning_state import LearnedStateRecord
from syngan.domain.provenance import (
    HistoricalKnowledgeBasis,
    HistoricalReferenceView,
    HistoricalResolution,
)
from syngan.foundation import platform as platform_contracts
from syngan.foundation import security as security_contracts
from syngan.foundation.data_state import (
    LogicalScope,
    SemanticBinding,
    TopologyDescriptor,
    TopologyHint,
)
from syngan.foundation.identity import (
    AuthorityScope,
    CommitmentSnapshotId,
    LogicalId,
    RecoveryFrontier,
    ResourceKey,
    ResourceKind,
    SemanticRevisionId,
    TypedReference,
)
from syngan.foundation.platform import (
    BenchmarkEvidence,
    CapabilityAssertion,
    CapabilityAvailability,
    CapabilityEvidenceStrength,
    CapabilityFallback,
    CapabilityMode,
    CompatibilityOutcome,
    PlatformCapability,
    PlatformQualificationContext,
    SupportLevel,
    WorkloadProfile,
)
from syngan.foundation.representation import EncodedPayload
from syngan.foundation.runtime import (
    DependencyProfile,
    GenerationBasisKind,
    ImplementationBinding,
    LearningRequirement,
    RuntimeClosureAssessment,
    RuntimeRoleResolution,
    StrategyRuntimeRequirements,
    assess_runtime_closure,
)
from syngan.foundation.security import (
    AuthorizationDecision,
    AuthorizationOutcome,
    AuthorizationRequest,
    DisclosureState,
    NetworkPosture,
    PrincipalKind,
    PrincipalRef,
    ProtectedTarget,
    SecurityAction,
    SecurityExecutionProfile,
)

pytestmark = pytest.mark.integration

ROOT = Path(__file__).resolve().parents[3]
SCOPE = AuthorityScope("phase-015-j")
FRONTIER = RecoveryFrontier(0)

SCENARIO_COVERAGE = {
    "S01": "direct-generation-family",
    "S02": "learned-state-generation-family",
    "S03": "structured-topology-evidence-composition",
    "S04": "self-contained-no-egress-composition",
    "S05": "evaluation-outcome-semantics",
    "S06": "evidence-invalidation-history",
    "S07": "provider-unknown-execution-separation",
    "S08": "recovery-frontier-stale-authority",
    "S09": "partial-history-disclosure",
    "S10": "scale-approximation-qualification",
    "S11": "provider-capability-portability",
    "S12": "protected-existence-authorization",
    "S13": "external-export-authority",
    "S14": "combined-adversarial-composition",
}


def commitment(kind: str, resource_id: str) -> TypedReference:
    return TypedReference(
        key=ResourceKey(SCOPE, ResourceKind(kind), LogicalId(resource_id)),
        commitment_snapshot_id=CommitmentSnapshotId(f"{resource_id}-commitment"),
    )


def revision(kind: str, resource_id: str, value: str = "r1") -> TypedReference:
    return TypedReference(
        key=ResourceKey(SCOPE, ResourceKind(kind), LogicalId(resource_id)),
        revision_id=SemanticRevisionId(value),
    )


def topology() -> TopologyDescriptor:
    return TopologyDescriptor(
        scopes=(LogicalScope("customers"), LogicalScope("orders")),
        semantic_bindings=(
            SemanticBinding(
                role="data-meaning",
                reference=revision("data-meaning", "meaning-1"),
                scope_ids=("customers", "orders"),
            ),
        ),
        hints=(TopologyHint.MULTI_TABLE,),
        requires_coordinated_cut=True,
    )


def runtime_closure(
    strategy: StrategyRuntimeRequirements,
    binding: ImplementationBinding,
) -> RuntimeClosureAssessment:
    return assess_runtime_closure(
        strategy,
        binding,
        (),
        (
            RuntimeRoleResolution(
                role_id="local-worker",
                environment_identity="python-3.11-reference",
                available=True,
                runtime_compatible=True,
            ),
        ),
    )


def platform_context() -> PlatformQualificationContext:
    return PlatformQualificationContext(
        provider_id="reference",
        environment_id="local-reference",
        adapter_id="reference-platform-v1",
        configuration_id="offline-config",
    )


def platform_assertion(
    capability: PlatformCapability,
    *,
    current: bool = True,
) -> CapabilityAssertion:
    return CapabilityAssertion(
        context=platform_context(),
        capability=capability,
        availability=CapabilityAvailability.PRESENT,
        mode=CapabilityMode.NATIVE,
        evidence_strength=CapabilityEvidenceStrength.VERIFIED,
        guarantee=f"{capability.value}-guarantee",
        evidence_reference=f"{capability.value}-evidence",
        current=current,
    )


@dataclass
class RuleAuthority:
    rules: dict[SecurityAction, AuthorizationDecision]

    def authorize(self, request: AuthorizationRequest) -> AuthorizationDecision:
        return self.rules.get(
            request.action,
            AuthorizationDecision(
                AuthorizationOutcome.DENY,
                decision_reference="default-deny",
                reason_code="not-permitted",
            ),
        )


def permit(action: SecurityAction) -> tuple[SecurityAction, AuthorizationDecision]:
    return (
        action,
        AuthorizationDecision(
            AuthorizationOutcome.PERMIT,
            decision_reference=f"permit-{action.value.replace('.', '-')}",
        ),
    )


def principal() -> PrincipalRef:
    return PrincipalRef("integration-user", PrincipalKind.HUMAN, "tenant-a")


def test_c9_accounts_for_entire_phase_014_f_scenario_registry() -> None:
    with (ROOT / "verification.toml").open("rb") as handle:
        manifest = tomllib.load(handle)

    assert set(manifest["scenarios"]) == set(SCENARIO_COVERAGE)
    assert all(SCENARIO_COVERAGE.values())


def test_s01_s02_direct_and_learned_state_generation_remain_distinct() -> None:
    source = commitment("source-state", "source-1")
    generation = commitment("generation", "generation-1")

    direct_strategy = StrategyRuntimeRequirements(
        strategy_reference=revision("synthesis-strategy", "direct-strategy"),
        dependency_profile=DependencyProfile.SELF_CONTAINED,
        learning_requirement=LearningRequirement.NONE,
        required_roles=("local-worker",),
    )
    direct_binding = ImplementationBinding(
        binding_id="direct-binding",
        strategy_reference=direct_strategy.strategy_reference,
        build_identity="direct-build-v1",
        dependency_profile=DependencyProfile.SELF_CONTAINED,
        required_roles=("local-worker",),
    )
    direct_plan = prepare_generation_plan(
        generation,
        direct_strategy,
        direct_binding,
        runtime_closure(direct_strategy, direct_binding),
        GenerationRuntimeContext(
            basis_kind=GenerationBasisKind.DIRECT,
            direct_input_references=(source,),
        ),
    )

    learned_strategy = StrategyRuntimeRequirements(
        strategy_reference=revision("synthesis-strategy", "learned-strategy"),
        dependency_profile=DependencyProfile.SELF_CONTAINED,
        learning_requirement=LearningRequirement.REQUIRED,
        required_roles=("local-worker",),
    )
    learned_binding = ImplementationBinding(
        binding_id="learned-binding",
        strategy_reference=learned_strategy.strategy_reference,
        build_identity="learned-build-v1",
        dependency_profile=DependencyProfile.SELF_CONTAINED,
        required_roles=("local-worker",),
    )
    learned_state = LearnedStateRecord(
        reference=revision("learned-state", "state-1"),
        producing_learning_reference=commitment("learning", "learning-1"),
        strategy_reference=learned_strategy.strategy_reference,
        material_reference=commitment("learned-state-material", "material-1"),
        dependency_references=(),
    )
    learned_plan = prepare_generation_plan(
        generation,
        learned_strategy,
        learned_binding,
        runtime_closure(learned_strategy, learned_binding),
        GenerationRuntimeContext(
            basis_kind=GenerationBasisKind.LEARNED_STATE,
            learned_state=learned_state,
        ),
    )

    assert direct_plan.learned_state_reference is None
    assert direct_plan.direct_input_references == (source,)
    assert learned_plan.learned_state_reference == learned_state.reference
    assert learned_plan.direct_input_references == ()


def test_s03_s05_s06_topology_evidence_and_invalidation_compose(
    tmp_path: Path,
) -> None:
    generation_ref = commitment("generation", "generation-1")
    state = GenerationDataState(generation_ref, topology())
    candidate = LogicalId("candidate-1")
    sealed = commitment("generation-physical-subject", "candidate-1")

    with SQLiteControlStore(tmp_path / "control.sqlite", SCOPE) as store:
        evidence_service = EvidenceHistoryService(store)
        evaluation = EvaluationAggregate(
            evaluation_commitment=commitment("evaluation", "evaluation-1"),
            criterion_references=(revision("criterion", "criterion-1"),),
            subject_reference=sealed,
            method_reference=revision("evaluation-method", "method-1"),
        )
        snapshot = evidence_service.initialize_evaluation(
            evaluation,
            FRONTIER,
            LogicalId("evaluation-create"),
        )
        result = EvaluationResult(
            evaluation_commitment=evaluation.evaluation_commitment,
            criterion_references=evaluation.criterion_references,
            subject_reference=sealed,
            method_reference=evaluation.method_reference,
            assumptions_valid=True,
            interpretable=True,
            findings=(
                FindingDraft(
                    slot="whole-topology",
                    criterion_reference=evaluation.criterion_references[0],
                    disposition=FindingDisposition.SATISFIED,
                    result=EncodedPayload.from_object({"violations": 0}),
                    logical_scope="customers+orders",
                    claim_strength=ClaimStrength.EXHAUSTIVE,
                    supported_claim_strengths=(ClaimStrength.EXHAUSTIVE,),
                ),
            ),
        )
        completed, findings = evidence_service.complete_with_findings(
            evaluation.evaluation_commitment,
            snapshot.state_version,
            result,
            FRONTIER,
            LogicalId("evaluation-complete"),
            LogicalId("evidence-intent"),
        )
        evidence = findings[0].finding.reference

        state = state.add_candidate(candidate)
        state = state.seal_candidate(candidate, sealed)
        state = state.promote_owner_validated_candidate(
            candidate,
            LogicalId("output-1"),
            (evidence,),
        )
        evidence_service.record_generation_evidence_use(
            generation_ref,
            (evidence,),
            LogicalId("generation-evidence-basis"),
            FRONTIER,
        )
        evidence_service.change_evidence_applicability(
            evidence,
            findings[0].applicability_state_version,
            EvidenceApplicability.INVALIDATED,
            FRONTIER,
            LogicalId("invalidate-evidence"),
            reasons=("later-method-defect",),
        )

        assert completed.state.evidence_references == (evidence,)
        assert state.completed_output is not None
        assert state.completed_output.completion_basis_references == (evidence,)
        assert state.topology.scope_ids == ("customers", "orders")
        with pytest.raises(ValueError, match="not currently applicable"):
            evidence_service.resolve_applicable_evidence((evidence,))

        with pytest.raises(ValueError, match="requires findings"):
            evaluation.complete(())


def test_s04_s10_s11_no_egress_portability_and_scale_cannot_weaken_commitment() -> None:
    offline = SecurityExecutionProfile(
        "offline",
        NetworkPosture.OFFLINE_NO_EGRESS,
        allowed_dependency_provider_classes=("local",),
    )
    ensure_dependency_profile_security(DependencyProfile.SELF_CONTAINED, offline)
    with pytest.raises(SecurityCompatibilityError, match="cannot widen"):
        ensure_dependency_profile_security(DependencyProfile.RUNTIME_NETWORK, offline)

    capability = PlatformCapability.EXACT_SOURCE_SNAPSHOT_READ
    absent = CapabilityAssertion(
        context=platform_context(),
        capability=capability,
        availability=CapabilityAvailability.ABSENT,
        mode=CapabilityMode.FALLBACK_REQUIRED,
        evidence_strength=CapabilityEvidenceStrength.VERIFIED,
    )
    fallback = CapabilityFallback(
        capability=capability,
        fallback_id="materialize-exact-snapshot",
        semantics_preserving=True,
        evidence_strength=CapabilityEvidenceStrength.VERIFIED,
        evidence_reference="snapshot-fallback-proof",
    )
    compatibility = assess_platform_compatibility(
        platform_context(),
        (
            platform_contracts.CapabilityRequirement(
                capability,
                CapabilityEvidenceStrength.VERIFIED,
            ),
        ),
        (absent,),
        (fallback,),
    )
    assert compatibility.outcome is CompatibilityOutcome.FALLBACK

    stale = assess_platform_compatibility(
        platform_context(),
        (
            platform_contracts.CapabilityRequirement(
                PlatformCapability.OUTBOUND_NETWORK_ENFORCEMENT,
                CapabilityEvidenceStrength.VERIFIED,
            ),
        ),
        (
            platform_assertion(
                PlatformCapability.OUTBOUND_NETWORK_ENFORCEMENT,
                current=False,
            ),
        ),
    )
    assert stale.outcome is CompatibilityOutcome.INDETERMINATE

    row_count_only = BenchmarkEvidence(
        context=platform_context(),
        support_profile_id="reference-profile",
        workload=WorkloadProfile(row_count=100_000_000),
        syngan_build="commit-reference",
        runtime_profile="local-reference",
        adapter_build="reference-platform-v1",
        evidence_reference="row-count-only",
        run_count=3,
        metric_summary=(("runtime_seconds", 1.0),),
        acceptance_passed=True,
    )
    support = qualify_support(
        platform_context(),
        "reference-profile",
        architecture_compatible=True,
        adapter_implemented=True,
        conformance_evidence_reference="reference-conformance",
        benchmark_evidence=row_count_only,
    )
    assert support.level is SupportLevel.CONFORMANCE_VERIFIED
    assert "scale-workload-profile-incomplete" in support.limitations


def test_s07_s08_provider_observation_and_recovery_remain_below_semantic_authority() -> None:
    activity = commitment("generation", "generation-1")
    execution = ExecutionAggregate(
        execution_reference=commitment("execution", "execution-1"),
        activity_reference=activity,
        authority_frontier=FRONTIER,
    )
    attempt_id = LogicalId("attempt-1")
    plan_ref = commitment("runtime-plan", "plan-1")

    execution = execution.prepare_attempt(attempt_id, plan_ref, FRONTIER)
    execution = execution.activate_attempt(attempt_id, FRONTIER)
    execution = execution.record_provider_observation(
        attempt_id,
        ProviderObservation.SUCCEEDED,
        FRONTIER,
        correlation="provider-run-77",
    )

    assert execution.status is ExecutionStatus.RUNNING
    assert execution.attempt(attempt_id).provider_observation is ProviderObservation.SUCCEEDED

    execution = execution.record_attempt_outcome(
        attempt_id,
        AttemptStatus.INDETERMINATE,
        FRONTIER,
    )
    recovered = execution.adopt_recovery_frontier(RecoveryFrontier(1))

    assert recovered.authority_frontier == RecoveryFrontier(1)
    assert recovered.status is ExecutionStatus.READY
    assert recovered.current_attempt_id is None
    assert recovered.attempt(attempt_id).status is AttemptStatus.FENCED

    with pytest.raises(ValueError, match="does not match current authority"):
        recovered.prepare_attempt(
            LogicalId("attempt-stale"),
            commitment("runtime-plan", "plan-stale"),
            FRONTIER,
        )


def test_s09_s12_history_disclosure_preserves_canonical_truth_and_protected_existence() -> None:
    historical = commitment("evidence", "evidence-1")
    canonical = HistoricalReferenceView(
        reference=historical,
        knowledge_basis=HistoricalKnowledgeBasis.DIRECT,
        resolution=HistoricalResolution.RESOLVED,
        payload=EncodedPayload.from_object({"finding": "protected"}),
    )
    rules = dict(
        [
            (
                SecurityAction.HISTORY_TRAVERSE,
                AuthorizationDecision(
                    AuthorizationOutcome.DENY,
                    decision_reference="history-deny",
                ),
            ),
            (
                SecurityAction.CONTROL_INSPECT,
                AuthorizationDecision(
                    AuthorizationOutcome.DENY,
                    decision_reference="existence-deny",
                ),
            ),
        ]
    )
    service = SecurityService(RuleAuthority(rules))
    target = ProtectedTarget(historical, "tenant-a")

    projected = service.disclose_historical_reference(principal(), target, canonical)
    existing = service.disclose(
        principal(),
        target,
        exists=True,
        detail_supplier=lambda: {"finding": "protected"},
    )
    absent = service.disclose(
        principal(),
        target,
        exists=False,
        detail_supplier=lambda: {"finding": "protected"},
    )

    assert projected.resolution is HistoricalResolution.WITHHELD
    assert canonical.resolution is HistoricalResolution.RESOLVED
    assert canonical.payload is not None
    assert existing.state is DisclosureState.WITHHELD
    assert absent.state is DisclosureState.WITHHELD
    assert existing.reference is None
    assert absent.reference is None


def test_s13_generation_completion_does_not_grant_external_export() -> None:
    generation_ref = commitment("generation", "generation-1")
    state = GenerationDataState(generation_ref, topology())
    candidate = LogicalId("candidate-1")
    sealed = commitment("generation-physical-subject", "candidate-1")
    state = state.add_candidate(candidate).seal_candidate(candidate, sealed)
    state = state.promote_owner_validated_candidate(candidate, LogicalId("output-1"))

    rules = dict(
        [
            (
                SecurityAction.OUTPUT_EXPORT,
                AuthorizationDecision(
                    AuthorizationOutcome.DENY,
                    decision_reference="export-denied",
                ),
            )
        ]
    )
    security = SecurityService(RuleAuthority(rules))
    output_target = ProtectedTarget(sealed, "tenant-a")

    assert state.completed_output is not None
    with pytest.raises(PermissionError):
        security.authorize(
            AuthorizationRequest(
                principal(),
                SecurityAction.OUTPUT_EXPORT,
                output_target,
            )
        )
    assert state.completed_output.sealed_subject_reference == sealed


def test_s14_combined_adversarial_composition_keeps_independent_axes() -> None:
    generation_ref = commitment("generation", "generation-1")
    evidence_ref = commitment("evidence", "evidence-1")
    attempt_ref = commitment("attempt", "attempt-1")

    state = GenerationDataState(generation_ref, topology())
    candidate = LogicalId("candidate-1")
    sealed = commitment("generation-physical-subject", "candidate-1")
    state = state.add_candidate(candidate).seal_candidate(candidate, sealed)
    state = state.promote_owner_validated_candidate(
        candidate,
        LogicalId("output-1"),
        (evidence_ref,),
    )

    historical = HistoricalReferenceView(
        evidence_ref,
        HistoricalKnowledgeBasis.RECONSTRUCTED,
        HistoricalResolution.KNOWN_UNAVAILABLE,
    )
    security = SecurityService(
        RuleAuthority(
            dict(
                [
                    (
                        SecurityAction.HISTORY_TRAVERSE,
                        AuthorizationDecision(
                            AuthorizationOutcome.DENY,
                            decision_reference="history-withheld",
                        ),
                    ),
                    permit(SecurityAction.LEARNED_STATE_USE),
                ]
            )
        )
    )
    withheld = security.disclose_historical_reference(
        principal(),
        ProtectedTarget(evidence_ref, "tenant-a"),
        historical,
    )

    offline = SecurityExecutionProfile(
        "offline",
        NetworkPosture.OFFLINE_NO_EGRESS,
        allowed_dependency_provider_classes=("local",),
    )
    grant = security.compose_capability_grant(
        principal(),
        attempt_ref,
        (
            security_contracts.CapabilityRequirement(
                SecurityAction.LEARNED_STATE_USE,
                ProtectedTarget(commitment("learned-state", "state-1"), "tenant-a"),
            ),
        ),
        offline,
    )

    platform = assess_platform_compatibility(
        platform_context(),
        (
            platform_contracts.CapabilityRequirement(
                PlatformCapability.WRITER_FENCING,
                CapabilityEvidenceStrength.VERIFIED,
            ),
        ),
        (
            platform_assertion(
                PlatformCapability.WRITER_FENCING,
                current=False,
            ),
        ),
    )

    assert state.completed_output is not None
    assert state.completed_output.completion_basis_references == (evidence_ref,)
    assert historical.resolution is HistoricalResolution.KNOWN_UNAVAILABLE
    assert withheld.resolution is HistoricalResolution.WITHHELD
    assert grant.attempt_reference == attempt_ref
    assert platform.outcome is CompatibilityOutcome.INDETERMINATE
