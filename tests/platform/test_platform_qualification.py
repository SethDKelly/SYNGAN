from __future__ import annotations

from dataclasses import dataclass, field

import pytest

from syngan.adapters.reference_platform import StaticPlatformCapabilityProvider
from syngan.application.observability import (
    RequiredTelemetryUnavailable,
    emit_telemetry,
)
from syngan.application.platform_qualification import (
    assess_platform_compatibility,
    qualify_support,
)
from syngan.foundation.identity import (
    AuthorityScope,
    CommitmentSnapshotId,
    LogicalId,
    ResourceKey,
    ResourceKind,
    TypedReference,
)
from syngan.foundation.observability import (
    TelemetryContext,
    TelemetryDeliveryStatus,
    TelemetryEvent,
)
from syngan.foundation.platform import (
    BenchmarkEvidence,
    CapabilityAssertion,
    CapabilityAvailability,
    CapabilityEvidenceStrength,
    CapabilityFallback,
    CapabilityMode,
    CapabilityRequirement,
    CompatibilityOutcome,
    PlatformCapability,
    PlatformQualificationContext,
    SupportLevel,
    WorkloadProfile,
)
from syngan.ports.observability import TelemetryUnavailable

pytestmark = [pytest.mark.provider, pytest.mark.scale]

SCOPE = AuthorityScope("test")


def exact(kind: str, resource_id: str) -> TypedReference:
    return TypedReference(
        key=ResourceKey(SCOPE, ResourceKind(kind), LogicalId(resource_id)),
        commitment_snapshot_id=CommitmentSnapshotId(f"{resource_id}-snapshot"),
    )


def context(
    provider: str = "reference",
    environment: str = "local",
    adapter: str = "reference-adapter-v1",
    configuration: str = "config-a",
) -> PlatformQualificationContext:
    return PlatformQualificationContext(provider, environment, adapter, configuration)


def present(
    capability: PlatformCapability,
    *,
    ctx: PlatformQualificationContext | None = None,
    strength: CapabilityEvidenceStrength = CapabilityEvidenceStrength.VERIFIED,
    limitations: tuple[str, ...] = (),
    mode: CapabilityMode = CapabilityMode.NATIVE,
    current: bool = True,
) -> CapabilityAssertion:
    actual = ctx or context()
    return CapabilityAssertion(
        context=actual,
        capability=capability,
        availability=CapabilityAvailability.PRESENT,
        mode=mode,
        evidence_strength=strength,
        guarantee=f"{capability.value}-guarantee",
        evidence_reference=f"evidence-{capability.value}",
        limitations=limitations,
        current=current,
    )


def absent(
    capability: PlatformCapability,
    *,
    ctx: PlatformQualificationContext | None = None,
) -> CapabilityAssertion:
    return CapabilityAssertion(
        context=ctx or context(),
        capability=capability,
        availability=CapabilityAvailability.ABSENT,
        mode=CapabilityMode.FALLBACK_REQUIRED,
        evidence_strength=CapabilityEvidenceStrength.VERIFIED,
    )


def complete_workload() -> WorkloadProfile:
    return WorkloadProfile(
        row_count=1_000_000,
        input_bytes=512_000_000,
        column_count=48,
        cardinality_profile="mixed-cardinality",
        skew_profile="moderate-skew",
        input_partitions=128,
        output_partitions=128,
        learned_state_bytes=64_000_000,
        worker_count=8,
        worker_cores=4,
        worker_memory_bytes=16_000_000_000,
        accelerator_profile="none",
        shuffle_bytes=900_000_000,
        evaluation_coverage="full-constraint-statistical-quality",
        concurrent_executions=4,
        external_service_profile="none",
    )


def benchmark(
    *,
    ctx: PlatformQualificationContext | None = None,
    profile: str = "reference-profile",
    workload: WorkloadProfile | None = None,
    accepted: bool = True,
    driver_proportional: bool = False,
) -> BenchmarkEvidence:
    return BenchmarkEvidence(
        context=ctx or context(),
        support_profile_id=profile,
        workload=workload or complete_workload(),
        syngan_build="commit-abc",
        runtime_profile="python-3.11-local",
        adapter_build="reference-adapter-v1",
        evidence_reference="benchmark-run-set-1",
        run_count=5,
        metric_summary=(("runtime_seconds", 10.0), ("driver_peak_bytes", 1000.0)),
        acceptance_passed=accepted,
        source_size_proportional_single_process_stage=driver_proportional,
    )


def test_provider_brand_without_capability_evidence_is_indeterminate() -> None:
    ctx = context(provider="famous-managed-platform")
    result = assess_platform_compatibility(
        ctx,
        (
            CapabilityRequirement(
                PlatformCapability.EXACT_SOURCE_SNAPSHOT_READ,
                CapabilityEvidenceStrength.VERIFIED,
            ),
        ),
        (),
    )

    assert result.outcome is CompatibilityOutcome.INDETERMINATE
    assert result.unresolved_capabilities == (
        PlatformCapability.EXACT_SOURCE_SNAPSHOT_READ,
    )


def test_absent_required_capability_without_fallback_is_incompatible() -> None:
    ctx = context()
    capability = PlatformCapability.EXACT_SOURCE_SNAPSHOT_READ
    result = assess_platform_compatibility(
        ctx,
        (CapabilityRequirement(capability),),
        (absent(capability),),
    )

    assert result.outcome is CompatibilityOutcome.INCOMPATIBLE
    assert result.incompatible_capabilities == (capability,)


def test_stale_or_weak_capability_evidence_does_not_become_current_proof() -> None:
    ctx = context()
    capability = PlatformCapability.WRITER_FENCING

    stale = assess_platform_compatibility(
        ctx,
        (CapabilityRequirement(capability),),
        (present(capability, current=False),),
    )
    weak = assess_platform_compatibility(
        ctx,
        (
            CapabilityRequirement(
                capability,
                CapabilityEvidenceStrength.VERIFIED,
            ),
        ),
        (
            present(
                capability,
                strength=CapabilityEvidenceStrength.DECLARED,
            ),
        ),
    )

    assert stale.outcome is CompatibilityOutcome.INDETERMINATE
    assert weak.outcome is CompatibilityOutcome.INDETERMINATE


def test_semantics_preserving_fallback_is_explicit_portability() -> None:
    ctx = context()
    capability = PlatformCapability.EXACT_SOURCE_SNAPSHOT_READ
    fallback = CapabilityFallback(
        capability=capability,
        fallback_id="materialize-exact-snapshot",
        semantics_preserving=True,
        evidence_strength=CapabilityEvidenceStrength.VERIFIED,
        evidence_reference="snapshot-fallback-conformance",
    )

    result = assess_platform_compatibility(
        ctx,
        (
            CapabilityRequirement(
                capability,
                CapabilityEvidenceStrength.VERIFIED,
            ),
        ),
        (absent(capability),),
        (fallback,),
    )

    assert result.outcome is CompatibilityOutcome.FALLBACK
    assert result.fallback_capabilities == (capability,)


def test_non_preserving_fallback_is_rejected() -> None:
    ctx = context()
    capability = PlatformCapability.EXACT_SOURCE_SNAPSHOT_READ
    fallback = CapabilityFallback(
        capability=capability,
        fallback_id="use-latest-table",
        semantics_preserving=False,
        evidence_strength=CapabilityEvidenceStrength.VERIFIED,
        evidence_reference="latest-table-is-not-exact",
    )

    result = assess_platform_compatibility(
        ctx,
        (CapabilityRequirement(capability),),
        (absent(capability),),
        (fallback,),
    )

    assert result.outcome is CompatibilityOutcome.INCOMPATIBLE


def test_accepted_limitations_remain_visible() -> None:
    ctx = context()
    capability = PlatformCapability.WORKLOAD_CANCELLATION
    assertion = present(
        capability,
        limitations=("best-effort-physical-cancel",),
    )

    rejected = assess_platform_compatibility(
        ctx,
        (CapabilityRequirement(capability, allow_limitations=False),),
        (assertion,),
    )
    accepted = assess_platform_compatibility(
        ctx,
        (CapabilityRequirement(capability, allow_limitations=True),),
        (assertion,),
    )

    assert rejected.outcome is CompatibilityOutcome.INCOMPATIBLE
    assert accepted.outcome is CompatibilityOutcome.LIMITED
    assert accepted.limitations == ("best-effort-physical-cancel",)


def test_reference_adapter_is_context_scoped_not_brand_inferred() -> None:
    ctx = context()
    assertion = present(PlatformCapability.WORKLOAD_SUBMISSION)
    provider = StaticPlatformCapabilityProvider(ctx, (assertion,))

    assert provider.describe_capabilities(ctx) == (assertion,)
    assert provider.describe_capabilities(context(environment="other")) == ()


@dataclass
class RecordingSink:
    events: list[TelemetryEvent] = field(default_factory=list)

    def emit(self, event: TelemetryEvent) -> None:
        self.events.append(event)


class UnavailableSink:
    def emit(self, event: TelemetryEvent) -> None:
        raise TelemetryUnavailable("collector unavailable")


def test_platform_correlation_never_replaces_syngan_identity() -> None:
    execution = exact("execution", "ex1")
    attempt = exact("attempt", "a1")
    telemetry = TelemetryContext(
        execution_reference=execution,
        attempt_reference=attempt,
        platform_correlation="provider-run-77",
    )

    assert telemetry.execution_reference == execution
    assert telemetry.attempt_reference == attempt
    assert telemetry.platform_correlation == "provider-run-77"


def test_optional_telemetry_failure_is_non_authoritative() -> None:
    event = TelemetryEvent(
        "runtime.progress",
        TelemetryContext(attempt_reference=exact("attempt", "a1")),
        measurements=(("fraction", 0.5),),
    )

    unavailable = emit_telemetry(event, UnavailableSink())
    absent_sink = emit_telemetry(event, None)
    recorded = RecordingSink()
    delivered = emit_telemetry(event, recorded)

    assert unavailable.status is TelemetryDeliveryStatus.UNAVAILABLE
    assert absent_sink.status is TelemetryDeliveryStatus.UNAVAILABLE
    assert delivered.status is TelemetryDeliveryStatus.DELIVERED
    assert recorded.events == [event]

    with pytest.raises(RequiredTelemetryUnavailable):
        emit_telemetry(event, UnavailableSink(), required=True)


def test_telemetry_rejects_secret_bearing_field_names() -> None:
    with pytest.raises(ValueError, match="secret-bearing"):
        TelemetryEvent(
            "runtime.call",
            TelemetryContext(),
            attributes=(("api_token", "do-not-log"),),
        )


def test_support_qualification_cannot_skip_evidence_levels() -> None:
    ctx = context()

    architecture_only = qualify_support(
        ctx,
        "reference-profile",
        architecture_compatible=True,
        adapter_implemented=False,
        conformance_evidence_reference="ignored-without-adapter",
        benchmark_evidence=benchmark(),
    )
    implemented = qualify_support(
        ctx,
        "reference-profile",
        architecture_compatible=True,
        adapter_implemented=True,
    )
    conformance = qualify_support(
        ctx,
        "reference-profile",
        architecture_compatible=True,
        adapter_implemented=True,
        conformance_evidence_reference="provider-conformance-suite",
    )

    assert architecture_only.level is SupportLevel.ARCHITECTURALLY_COMPATIBLE
    assert implemented.level is SupportLevel.IMPLEMENTED
    assert conformance.level is SupportLevel.CONFORMANCE_VERIFIED


def test_row_count_only_benchmark_does_not_create_scale_qualification() -> None:
    ctx = context()
    evidence = benchmark(workload=WorkloadProfile(row_count=100_000_000))

    result = qualify_support(
        ctx,
        "reference-profile",
        architecture_compatible=True,
        adapter_implemented=True,
        conformance_evidence_reference="provider-conformance-suite",
        benchmark_evidence=evidence,
    )

    assert result.level is SupportLevel.CONFORMANCE_VERIFIED
    assert "scale-workload-profile-incomplete" in result.limitations


def test_driver_local_proportional_stage_blocks_scale_qualification() -> None:
    ctx = context()
    evidence = benchmark(driver_proportional=True)

    result = qualify_support(
        ctx,
        "reference-profile",
        architecture_compatible=True,
        adapter_implemented=True,
        conformance_evidence_reference="provider-conformance-suite",
        benchmark_evidence=evidence,
    )

    assert result.level is SupportLevel.CONFORMANCE_VERIFIED
    assert "source-size-proportional-single-process-stage" in result.limitations


def test_complete_accepted_benchmark_can_establish_scale_qualification() -> None:
    ctx = context()
    evidence = benchmark()

    result = qualify_support(
        ctx,
        "reference-profile",
        architecture_compatible=True,
        adapter_implemented=True,
        conformance_evidence_reference="provider-conformance-suite",
        benchmark_evidence=evidence,
    )

    assert result.level is SupportLevel.SCALE_QUALIFIED
    assert result.evidence_references == (
        "provider-conformance-suite",
        "benchmark-run-set-1",
    )


def test_support_evidence_cannot_be_reused_across_context_or_profile() -> None:
    ctx = context()
    other_context = context(environment="other")

    with pytest.raises(ValueError, match="different platform context"):
        qualify_support(
            other_context,
            "reference-profile",
            architecture_compatible=True,
            adapter_implemented=True,
            conformance_evidence_reference="provider-conformance-suite",
            benchmark_evidence=benchmark(ctx=ctx),
        )

    with pytest.raises(ValueError, match="different support profile"):
        qualify_support(
            ctx,
            "other-profile",
            architecture_compatible=True,
            adapter_implemented=True,
            conformance_evidence_reference="provider-conformance-suite",
            benchmark_evidence=benchmark(ctx=ctx, profile="reference-profile"),
        )


def test_failed_benchmark_acceptance_remains_conformance_verified_only() -> None:
    ctx = context()
    result = qualify_support(
        ctx,
        "reference-profile",
        architecture_compatible=True,
        adapter_implemented=True,
        conformance_evidence_reference="provider-conformance-suite",
        benchmark_evidence=benchmark(accepted=False),
    )

    assert result.level is SupportLevel.CONFORMANCE_VERIFIED
    assert "benchmark-acceptance-not-met" in result.limitations
