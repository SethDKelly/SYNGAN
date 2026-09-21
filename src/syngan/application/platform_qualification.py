"""Platform capability negotiation and layered support qualification."""

from __future__ import annotations

from syngan.foundation.platform import (
    BenchmarkEvidence,
    CapabilityAssertion,
    CapabilityAvailability,
    CapabilityFallback,
    CapabilityMode,
    CapabilityRequirement,
    CompatibilityOutcome,
    PlatformCapability,
    PlatformCompatibilityAssessment,
    PlatformQualificationContext,
    SupportLevel,
    SupportQualification,
)


def assess_platform_compatibility(
    context: PlatformQualificationContext,
    requirements: tuple[CapabilityRequirement, ...],
    assertions: tuple[CapabilityAssertion, ...],
    fallbacks: tuple[CapabilityFallback, ...] = (),
) -> PlatformCompatibilityAssessment:
    by_capability = {
        assertion.capability: assertion for assertion in assertions if assertion.context == context
    }
    fallback_by_capability = {fallback.capability: fallback for fallback in fallbacks}
    if len(by_capability) != len(
        [assertion for assertion in assertions if assertion.context == context]
    ):
        raise ValueError("capability assertions must be unique within a qualification context")
    if len(fallback_by_capability) != len(fallbacks):
        raise ValueError("capability fallbacks must be unique by capability")

    direct: list[PlatformCapability] = []
    via_fallback: list[PlatformCapability] = []
    limitations: list[str] = []
    unresolved: list[PlatformCapability] = []
    incompatible: list[PlatformCapability] = []

    for requirement in requirements:
        assertion = by_capability.get(requirement.capability)
        if assertion is None:
            unresolved.append(requirement.capability)
            continue
        if not assertion.current:
            unresolved.append(requirement.capability)
            continue
        if assertion.availability is CapabilityAvailability.INDETERMINATE:
            unresolved.append(requirement.capability)
            continue

        if assertion.availability is CapabilityAvailability.ABSENT:
            fallback = fallback_by_capability.get(requirement.capability)
            if fallback is None:
                incompatible.append(requirement.capability)
                continue
            if not fallback.semantics_preserving:
                incompatible.append(requirement.capability)
                continue
            if fallback.evidence_strength < requirement.minimum_evidence_strength:
                unresolved.append(requirement.capability)
                continue
            if fallback.limitations and not requirement.allow_limitations:
                incompatible.append(requirement.capability)
                continue
            via_fallback.append(requirement.capability)
            limitations.extend(fallback.limitations)
            continue

        if assertion.evidence_strength < requirement.minimum_evidence_strength:
            unresolved.append(requirement.capability)
            continue
        if assertion.mode is CapabilityMode.FALLBACK_REQUIRED:
            fallback = fallback_by_capability.get(requirement.capability)
            if fallback is None or not fallback.semantics_preserving:
                incompatible.append(requirement.capability)
                continue
            if fallback.evidence_strength < requirement.minimum_evidence_strength:
                unresolved.append(requirement.capability)
                continue
            if fallback.limitations and not requirement.allow_limitations:
                incompatible.append(requirement.capability)
                continue
            via_fallback.append(requirement.capability)
            limitations.extend((*assertion.limitations, *fallback.limitations))
            continue
        if assertion.limitations and not requirement.allow_limitations:
            incompatible.append(requirement.capability)
            continue
        direct.append(requirement.capability)
        limitations.extend(assertion.limitations)

    if incompatible:
        outcome = CompatibilityOutcome.INCOMPATIBLE
    elif unresolved:
        outcome = CompatibilityOutcome.INDETERMINATE
    elif limitations:
        outcome = CompatibilityOutcome.LIMITED
    elif via_fallback:
        outcome = CompatibilityOutcome.FALLBACK
    else:
        outcome = CompatibilityOutcome.DIRECT

    return PlatformCompatibilityAssessment(
        context=context,
        outcome=outcome,
        direct_capabilities=tuple(direct),
        fallback_capabilities=tuple(via_fallback),
        limitations=tuple(dict.fromkeys(limitations)),
        unresolved_capabilities=tuple(unresolved),
        incompatible_capabilities=tuple(incompatible),
    )


def qualify_support(
    context: PlatformQualificationContext,
    support_profile_id: str,
    *,
    architecture_compatible: bool,
    adapter_implemented: bool,
    conformance_evidence_reference: str | None = None,
    benchmark_evidence: BenchmarkEvidence | None = None,
) -> SupportQualification:
    evidence: list[str] = []
    limitations: list[str] = []

    if not architecture_compatible:
        return SupportQualification(context, support_profile_id, SupportLevel.UNQUALIFIED)

    level = SupportLevel.ARCHITECTURALLY_COMPATIBLE
    if not adapter_implemented:
        return SupportQualification(context, support_profile_id, level)

    level = SupportLevel.IMPLEMENTED
    if conformance_evidence_reference is None:
        return SupportQualification(context, support_profile_id, level)
    evidence.append(conformance_evidence_reference)
    level = SupportLevel.CONFORMANCE_VERIFIED

    if benchmark_evidence is None:
        return SupportQualification(
            context,
            support_profile_id,
            level,
            evidence_references=tuple(evidence),
        )
    if benchmark_evidence.context != context:
        raise ValueError("benchmark evidence belongs to a different platform context")
    if benchmark_evidence.support_profile_id != support_profile_id:
        raise ValueError("benchmark evidence belongs to a different support profile")

    evidence.append(benchmark_evidence.evidence_reference)
    limitations.extend(benchmark_evidence.limitations)

    if not benchmark_evidence.workload.complete_for_scale_qualification:
        limitations.append("scale-workload-profile-incomplete")
    elif benchmark_evidence.source_size_proportional_single_process_stage:
        limitations.append("source-size-proportional-single-process-stage")
    elif not benchmark_evidence.acceptance_passed:
        limitations.append("benchmark-acceptance-not-met")
    else:
        level = SupportLevel.SCALE_QUALIFIED

    return SupportQualification(
        context,
        support_profile_id,
        level,
        evidence_references=tuple(evidence),
        limitations=tuple(dict.fromkeys(limitations)),
    )
