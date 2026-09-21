"""Application planning for Strategy realization beneath semantic activity authority."""

from __future__ import annotations

from dataclasses import dataclass

from syngan.domain.learning_state import LearnedStateRecord, LearnedStateStatus
from syngan.foundation.identity import TypedReference
from syngan.foundation.runtime import (
    GenerationBasisKind,
    ImplementationBinding,
    LearningRequirement,
    RuntimeClosureAssessment,
    RuntimeRealizationPlan,
    StrategyRuntimeRequirements,
    build_runtime_plan,
)


@dataclass(frozen=True, slots=True)
class GenerationRuntimeContext:
    basis_kind: GenerationBasisKind
    learned_state: LearnedStateRecord | None = None
    direct_input_references: tuple[TypedReference, ...] = ()
    accept_restricted_learned_state: bool = False


def prepare_learning_plan(
    learning_commitment: TypedReference,
    strategy: StrategyRuntimeRequirements,
    binding: ImplementationBinding,
    closure: RuntimeClosureAssessment,
    source_references: tuple[TypedReference, ...],
) -> RuntimeRealizationPlan:
    learning_commitment.require_exact_binding()
    if strategy.learning_requirement is LearningRequirement.NONE:
        raise ValueError("direct-only Strategy does not permit fabricated Learning")
    if not source_references:
        raise ValueError("Learning runtime planning requires exact source references")
    for reference in source_references:
        reference.require_exact_binding()
    return build_runtime_plan(
        activity_reference=learning_commitment,
        strategy=strategy,
        binding=binding,
        closure=closure,
        direct_input_references=source_references,
    )


def prepare_generation_plan(
    generation_commitment: TypedReference,
    strategy: StrategyRuntimeRequirements,
    binding: ImplementationBinding,
    closure: RuntimeClosureAssessment,
    context: GenerationRuntimeContext,
) -> RuntimeRealizationPlan:
    generation_commitment.require_exact_binding()

    if context.basis_kind is GenerationBasisKind.DIRECT:
        if context.learned_state is not None:
            raise ValueError("direct Generation cannot bind Learned State")
        if strategy.learning_requirement is LearningRequirement.REQUIRED:
            raise ValueError("Strategy requires Learned State for Generation")
        for reference in context.direct_input_references:
            reference.require_exact_binding()
        return build_runtime_plan(
            activity_reference=generation_commitment,
            strategy=strategy,
            binding=binding,
            closure=closure,
            direct_input_references=context.direct_input_references,
        )

    if context.learned_state is None:
        raise ValueError("Learned-State Generation requires an exact Learned State")
    if strategy.learning_requirement is LearningRequirement.NONE:
        raise ValueError("direct-only Strategy cannot fabricate Learned-State use")

    state = context.learned_state
    if state.strategy_reference != strategy.strategy_reference:
        raise ValueError("Learned State was produced under a different Strategy revision")
    if state.status is LearnedStateStatus.INVALIDATED:
        raise ValueError("invalidated Learned State is ineligible for new Generation")
    if state.status is LearnedStateStatus.RETIRED:
        raise ValueError("retired Learned State is not eligible for ordinary new Generation")
    if state.status is LearnedStateStatus.RESTRICTED:
        if not context.accept_restricted_learned_state:
            raise ValueError("restricted Learned State requires explicit limitation acceptance")
        if not state.limitations:
            raise ValueError("restricted Learned State lost its explicit limitation")

    return build_runtime_plan(
        activity_reference=generation_commitment,
        strategy=strategy,
        binding=binding,
        closure=closure,
        learned_state_reference=state.reference,
        direct_input_references=context.direct_input_references,
    )
