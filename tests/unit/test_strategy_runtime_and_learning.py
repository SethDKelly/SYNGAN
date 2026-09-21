from __future__ import annotations

import pytest

from syngan.adapters.reference_source_derived_text import (
    generate_source_derived_text,
    generate_source_derived_text_direct,
    learn_source_derived_text,
    reference_source_derived_binding,
    source_derived_text_state_from_payload,
    source_derived_text_state_to_payload,
)
from syngan.application.runtime_planning import (
    GenerationRuntimeContext,
    prepare_generation_plan,
    prepare_learning_plan,
)
from syngan.domain.learning_state import (
    LearnedStateRecord,
    LearnedStateStatus,
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
from syngan.foundation.runtime import (
    DependencyProfile,
    DependencyRequirement,
    DependencyResolution,
    GenerationBasisKind,
    ImplementationBinding,
    LearningRequirement,
    RuntimeClosureStatus,
    RuntimeRoleResolution,
    StrategyRuntimeRequirements,
    assess_runtime_closure,
)


def _revision(kind: str, resource_id: str, revision: str) -> TypedReference:
    return TypedReference(
        key=ResourceKey(
            scope=AuthorityScope("test"),
            kind=ResourceKind(kind),
            resource_id=LogicalId(resource_id),
        ),
        revision_id=SemanticRevisionId(revision),
    )


def _commitment(kind: str, resource_id: str, snapshot: str) -> TypedReference:
    return TypedReference(
        key=ResourceKey(
            scope=AuthorityScope("test"),
            kind=ResourceKind(kind),
            resource_id=LogicalId(resource_id),
        ),
        commitment_snapshot_id=CommitmentSnapshotId(snapshot),
    )


def _role() -> tuple[RuntimeRoleResolution, ...]:
    return (
        RuntimeRoleResolution(
            role_id="local-worker",
            environment_identity="python-3.11-portable",
            available=True,
            runtime_compatible=True,
        ),
    )


def _strategy(
    learning: LearningRequirement = LearningRequirement.OPTIONAL,
    profile: DependencyProfile = DependencyProfile.SELF_CONTAINED,
) -> StrategyRuntimeRequirements:
    return StrategyRuntimeRequirements(
        strategy_reference=_revision("synthesis-strategy", "strategy-1", "r1"),
        dependency_profile=profile,
        learning_requirement=learning,
        required_roles=("local-worker",),
        source_derived_text_capable=True,
    )


def test_reference_binding_satisfies_self_contained_source_derived_strategy() -> None:
    strategy = _strategy()
    binding = reference_source_derived_binding(strategy.strategy_reference)

    closure = assess_runtime_closure(strategy, binding, (), _role())

    assert closure.status is RuntimeClosureStatus.SATISFIED_WITH_LIMITATIONS
    assert closure.ready
    assert closure.closure_identity is not None
    assert closure.exact_dependency_identities == ()
    assert closure.exact_role_environment_identities == (("local-worker", "python-3.11-portable"),)


def test_runtime_role_closure_is_required_even_without_external_dependencies() -> None:
    strategy = _strategy()
    binding = reference_source_derived_binding(strategy.strategy_reference)

    closure = assess_runtime_closure(strategy, binding, (), ())

    assert closure.status is RuntimeClosureStatus.INCOMPLETE
    assert closure.incomplete_roles == ("local-worker",)


def test_binding_must_target_the_exact_strategy_revision() -> None:
    strategy = _strategy()
    other_strategy = _revision("synthesis-strategy", "strategy-1", "r2")
    binding = reference_source_derived_binding(other_strategy)

    with pytest.raises(ValueError, match="different Strategy revision"):
        assess_runtime_closure(strategy, binding, (), _role())


def test_binding_cannot_broaden_self_contained_strategy_to_runtime_network() -> None:
    strategy = _strategy()
    binding = ImplementationBinding(
        binding_id="remote",
        strategy_reference=strategy.strategy_reference,
        build_identity="remote-v1",
        dependency_profile=DependencyProfile.RUNTIME_NETWORK,
        required_roles=("local-worker",),
        source_derived_text_capable=True,
    )

    closure = assess_runtime_closure(strategy, binding, (), _role())

    assert closure.status is RuntimeClosureStatus.INCOMPATIBLE
    assert not closure.ready


def test_dependency_closure_distinguishes_missing_indeterminate_and_role_incomplete() -> None:
    strategy = _strategy()
    requirement = DependencyRequirement(
        component_id="codec",
        allowed_identities=("codec-v1",),
        required_roles=("local-worker",),
    )
    binding = ImplementationBinding(
        binding_id="binding",
        strategy_reference=strategy.strategy_reference,
        build_identity="binding-v1",
        dependency_profile=DependencyProfile.SELF_CONTAINED,
        required_roles=("local-worker",),
        dependency_requirements=(requirement,),
        source_derived_text_capable=True,
    )

    missing = assess_runtime_closure(strategy, binding, (), _role())
    assert missing.status is RuntimeClosureStatus.INCOMPLETE
    assert missing.missing_components == ("codec",)

    indeterminate = assess_runtime_closure(
        strategy,
        binding,
        (
            DependencyResolution(
                component_id="codec",
                exact_identity="codec-v1",
                available=True,
                runtime_compatible=None,
                eligible_roles=("local-worker",),
            ),
        ),
        _role(),
    )
    assert indeterminate.status is RuntimeClosureStatus.INDETERMINATE

    wrong_role = assess_runtime_closure(
        strategy,
        binding,
        (
            DependencyResolution(
                component_id="codec",
                exact_identity="codec-v1",
                available=True,
                runtime_compatible=True,
                eligible_roles=("coordinator",),
            ),
        ),
        _role(),
    )
    assert wrong_role.status is RuntimeClosureStatus.INCOMPLETE
    assert wrong_role.incomplete_roles == ("local-worker",)


def test_runtime_acquisition_is_not_automatic_repair() -> None:
    strategy = _strategy(profile=DependencyProfile.ACQUISITION_NETWORK)
    requirement = DependencyRequirement(
        component_id="artifact",
        allowed_identities=("artifact-v1",),
        required_roles=("local-worker",),
    )
    binding = ImplementationBinding(
        binding_id="binding",
        strategy_reference=strategy.strategy_reference,
        build_identity="binding-v1",
        dependency_profile=DependencyProfile.ACQUISITION_NETWORK,
        required_roles=("local-worker",),
        dependency_requirements=(requirement,),
        source_derived_text_capable=True,
    )
    closure = assess_runtime_closure(
        strategy,
        binding,
        (
            DependencyResolution(
                component_id="artifact",
                exact_identity="artifact-v1",
                available=True,
                runtime_compatible=True,
                eligible_roles=("local-worker",),
                acquired_during_material_execution=True,
            ),
        ),
        _role(),
    )

    assert closure.status is RuntimeClosureStatus.INCOMPATIBLE


def test_direct_generation_does_not_fabricate_learning_or_learned_state() -> None:
    strategy = _strategy(learning=LearningRequirement.NONE)
    binding = reference_source_derived_binding(strategy.strategy_reference)
    closure = assess_runtime_closure(strategy, binding, (), _role())
    source = _commitment("source-state", "source-1", "s1")

    plan = prepare_generation_plan(
        generation_commitment=_commitment("generation", "generation-1", "g1"),
        strategy=strategy,
        binding=binding,
        closure=closure,
        context=GenerationRuntimeContext(
            basis_kind=GenerationBasisKind.DIRECT,
            direct_input_references=(source,),
        ),
    )

    assert plan.learned_state_reference is None
    assert plan.direct_input_references == (source,)

    with pytest.raises(ValueError, match="fabricated Learning"):
        prepare_learning_plan(
            _commitment("learning", "learning-1", "l1"),
            strategy,
            binding,
            closure,
            (source,),
        )


def test_required_learning_strategy_rejects_direct_generation() -> None:
    strategy = _strategy(learning=LearningRequirement.REQUIRED)
    binding = reference_source_derived_binding(strategy.strategy_reference)
    closure = assess_runtime_closure(strategy, binding, (), _role())

    with pytest.raises(ValueError, match="requires Learned State"):
        prepare_generation_plan(
            generation_commitment=_commitment("generation", "generation-1", "g1"),
            strategy=strategy,
            binding=binding,
            closure=closure,
            context=GenerationRuntimeContext(basis_kind=GenerationBasisKind.DIRECT),
        )


def test_learned_state_reuse_rejects_invalidated_and_requires_restriction_acceptance() -> None:
    strategy = _strategy(learning=LearningRequirement.OPTIONAL)
    binding = reference_source_derived_binding(strategy.strategy_reference)
    closure = assess_runtime_closure(strategy, binding, (), _role())
    state = LearnedStateRecord(
        reference=_revision("learned-state", "state-1", "ls1"),
        producing_learning_reference=_commitment("learning", "learning-1", "l1"),
        strategy_reference=strategy.strategy_reference,
        material_reference=_commitment("learned-state-material", "material-1", "m1"),
        dependency_references=(),
    )

    invalidated = state.with_status(LearnedStateStatus.INVALIDATED)
    with pytest.raises(ValueError, match="invalidated"):
        prepare_generation_plan(
            _commitment("generation", "generation-1", "g1"),
            strategy,
            binding,
            closure,
            GenerationRuntimeContext(
                basis_kind=GenerationBasisKind.LEARNED_STATE,
                learned_state=invalidated,
            ),
        )

    restricted = state.with_status(
        LearnedStateStatus.RESTRICTED,
        limitations=("approved-regions-only",),
    )
    with pytest.raises(ValueError, match="explicit limitation acceptance"):
        prepare_generation_plan(
            _commitment("generation", "generation-1", "g1"),
            strategy,
            binding,
            closure,
            GenerationRuntimeContext(
                basis_kind=GenerationBasisKind.LEARNED_STATE,
                learned_state=restricted,
            ),
        )

    plan = prepare_generation_plan(
        _commitment("generation", "generation-1", "g1"),
        strategy,
        binding,
        closure,
        GenerationRuntimeContext(
            basis_kind=GenerationBasisKind.LEARNED_STATE,
            learned_state=restricted,
            accept_restricted_learned_state=True,
        ),
    )
    assert plan.learned_state_reference == restricted.reference


def test_source_derived_text_reference_is_bounded_round_trippable_and_deterministic() -> None:
    values = ("alpha", "beta", "alpha", "gamma", "delta")
    state = learn_source_derived_text(values, max_distinct_values=3)

    assert state.observed_count == 5
    assert state.truncated
    assert len(state.weighted_values) == 3
    assert (
        source_derived_text_state_from_payload(source_derived_text_state_to_payload(state)) == state
    )

    first = generate_source_derived_text(state, count=12, seed=17)
    second = generate_source_derived_text(state, count=12, seed=17)
    assert first == second
    assert set(first).issubset({value for value, _ in state.weighted_values})

    direct = generate_source_derived_text_direct(
        values,
        count=12,
        seed=17,
        max_distinct_values=3,
    )
    assert direct == first
