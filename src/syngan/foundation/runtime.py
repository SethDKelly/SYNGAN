"""Provider-neutral Strategy binding, dependency closure, and runtime-plan primitives.

These types are downstream realization roles. They do not own Strategy, Learning,
Learned State, Generation, Execution, Evidence, or provider semantics.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from enum import StrEnum

from syngan.foundation.identity import TypedReference


def _token(value: str, label: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{label} must be non-empty")
    if any(character.isspace() for character in normalized):
        raise ValueError(f"{label} must not contain whitespace")
    return normalized


class DependencyProfile(StrEnum):
    SELF_CONTAINED = "self-contained"
    LOCAL_ARTIFACT = "local-artifact"
    ACQUISITION_NETWORK = "acquisition-network"
    RUNTIME_NETWORK = "runtime-network"


class LearningRequirement(StrEnum):
    REQUIRED = "required"
    OPTIONAL = "optional"
    NONE = "none"


class RuntimeClosureStatus(StrEnum):
    SATISFIED = "satisfied"
    SATISFIED_WITH_LIMITATIONS = "satisfied-with-limitations"
    INCOMPLETE = "incomplete"
    INCOMPATIBLE = "incompatible"
    INDETERMINATE = "indeterminate"


class GenerationBasisKind(StrEnum):
    DIRECT = "direct"
    LEARNED_STATE = "learned-state"


@dataclass(frozen=True, slots=True)
class StrategyRuntimeRequirements:
    strategy_reference: TypedReference
    dependency_profile: DependencyProfile
    learning_requirement: LearningRequirement
    required_roles: tuple[str, ...]
    source_derived_text_capable: bool = False

    def __post_init__(self) -> None:
        self.strategy_reference.require_exact_revision()
        roles = tuple(_token(role, "runtime role") for role in self.required_roles)
        if not roles:
            raise ValueError("Strategy runtime requirements need at least one runtime role")
        if len(set(roles)) != len(roles):
            raise ValueError("Strategy runtime roles must be unique")
        object.__setattr__(self, "required_roles", roles)


@dataclass(frozen=True, slots=True)
class DependencyRequirement:
    component_id: str
    allowed_identities: tuple[str, ...]
    required_roles: tuple[str, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "component_id", _token(self.component_id, "component id"))
        identities = tuple(
            _token(identity, "allowed dependency identity") for identity in self.allowed_identities
        )
        roles = tuple(_token(role, "dependency runtime role") for role in self.required_roles)
        if not identities:
            raise ValueError("dependency requirement needs at least one allowed identity")
        if not roles:
            raise ValueError("dependency requirement needs at least one runtime role")
        if len(set(identities)) != len(identities):
            raise ValueError("allowed dependency identities must be unique")
        if len(set(roles)) != len(roles):
            raise ValueError("dependency runtime roles must be unique")
        object.__setattr__(self, "allowed_identities", identities)
        object.__setattr__(self, "required_roles", roles)


@dataclass(frozen=True, slots=True)
class ImplementationBinding:
    binding_id: str
    strategy_reference: TypedReference
    build_identity: str
    dependency_profile: DependencyProfile
    required_roles: tuple[str, ...]
    dependency_requirements: tuple[DependencyRequirement, ...] = ()
    limitations: tuple[str, ...] = ()
    source_derived_text_capable: bool = False

    def __post_init__(self) -> None:
        object.__setattr__(self, "binding_id", _token(self.binding_id, "binding id"))
        self.strategy_reference.require_exact_revision()
        object.__setattr__(self, "build_identity", _token(self.build_identity, "build identity"))
        roles = tuple(_token(role, "binding runtime role") for role in self.required_roles)
        if not roles:
            raise ValueError("implementation binding needs at least one runtime role")
        if len(set(roles)) != len(roles):
            raise ValueError("implementation binding runtime roles must be unique")
        requirement_ids = tuple(item.component_id for item in self.dependency_requirements)
        if len(set(requirement_ids)) != len(requirement_ids):
            raise ValueError("dependency requirement component ids must be unique")
        known_roles = set(roles)
        for requirement in self.dependency_requirements:
            unknown = set(requirement.required_roles) - known_roles
            if unknown:
                raise ValueError(
                    f"dependency requirement uses unknown binding roles: {sorted(unknown)}"
                )
        object.__setattr__(self, "required_roles", roles)
        object.__setattr__(
            self,
            "limitations",
            tuple(_token(item, "binding limitation") for item in self.limitations),
        )


@dataclass(frozen=True, slots=True)
class DependencyResolution:
    component_id: str
    exact_identity: str | None
    available: bool
    runtime_compatible: bool | None
    eligible_roles: tuple[str, ...]
    acquired_during_material_execution: bool = False

    def __post_init__(self) -> None:
        object.__setattr__(self, "component_id", _token(self.component_id, "component id"))
        if self.exact_identity is not None:
            object.__setattr__(
                self,
                "exact_identity",
                _token(self.exact_identity, "resolved dependency identity"),
            )
        roles = tuple(_token(role, "eligible runtime role") for role in self.eligible_roles)
        if len(set(roles)) != len(roles):
            raise ValueError("eligible runtime roles must be unique")
        object.__setattr__(self, "eligible_roles", roles)


@dataclass(frozen=True, slots=True)
class RuntimeRoleResolution:
    role_id: str
    environment_identity: str | None
    available: bool
    runtime_compatible: bool | None

    def __post_init__(self) -> None:
        object.__setattr__(self, "role_id", _token(self.role_id, "runtime role"))
        if self.environment_identity is not None:
            object.__setattr__(
                self,
                "environment_identity",
                _token(self.environment_identity, "runtime environment identity"),
            )


@dataclass(frozen=True, slots=True)
class RuntimeClosureAssessment:
    status: RuntimeClosureStatus
    closure_identity: str | None
    exact_dependency_identities: tuple[tuple[str, str], ...]
    exact_role_environment_identities: tuple[tuple[str, str], ...] = ()
    missing_components: tuple[str, ...] = ()
    incompatible_components: tuple[str, ...] = ()
    indeterminate_components: tuple[str, ...] = ()
    incomplete_roles: tuple[str, ...] = ()
    incompatible_roles: tuple[str, ...] = ()
    indeterminate_roles: tuple[str, ...] = ()
    limitations: tuple[str, ...] = ()

    @property
    def ready(self) -> bool:
        return self.status in {
            RuntimeClosureStatus.SATISFIED,
            RuntimeClosureStatus.SATISFIED_WITH_LIMITATIONS,
        }


@dataclass(frozen=True, slots=True)
class RuntimeRealizationPlan:
    activity_reference: TypedReference
    strategy_reference: TypedReference
    binding_id: str
    build_identity: str
    dependency_profile: DependencyProfile
    closure_identity: str
    exact_dependency_identities: tuple[tuple[str, str], ...]
    exact_role_environment_identities: tuple[tuple[str, str], ...]
    runtime_roles: tuple[str, ...]
    learned_state_reference: TypedReference | None = None
    direct_input_references: tuple[TypedReference, ...] = ()
    limitations: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        self.activity_reference.require_exact_binding()
        self.strategy_reference.require_exact_revision()
        object.__setattr__(self, "binding_id", _token(self.binding_id, "binding id"))
        object.__setattr__(self, "build_identity", _token(self.build_identity, "build identity"))
        object.__setattr__(
            self,
            "closure_identity",
            _token(self.closure_identity, "runtime closure identity"),
        )
        if self.learned_state_reference is not None:
            self.learned_state_reference.require_exact_binding()
        for reference in self.direct_input_references:
            reference.require_exact_binding()


def _profile_compatible(
    semantic_profile: DependencyProfile,
    binding_profile: DependencyProfile,
) -> bool:
    if semantic_profile is DependencyProfile.SELF_CONTAINED:
        return binding_profile is DependencyProfile.SELF_CONTAINED
    if semantic_profile is DependencyProfile.LOCAL_ARTIFACT:
        return binding_profile in {
            DependencyProfile.SELF_CONTAINED,
            DependencyProfile.LOCAL_ARTIFACT,
        }
    if semantic_profile is DependencyProfile.ACQUISITION_NETWORK:
        return binding_profile in {
            DependencyProfile.SELF_CONTAINED,
            DependencyProfile.LOCAL_ARTIFACT,
            DependencyProfile.ACQUISITION_NETWORK,
        }
    return binding_profile is DependencyProfile.RUNTIME_NETWORK


def assess_runtime_closure(
    strategy: StrategyRuntimeRequirements,
    binding: ImplementationBinding,
    resolutions: tuple[DependencyResolution, ...],
    role_resolutions: tuple[RuntimeRoleResolution, ...],
) -> RuntimeClosureAssessment:
    if binding.strategy_reference != strategy.strategy_reference:
        raise ValueError("implementation binding targets a different Strategy revision")
    if not _profile_compatible(strategy.dependency_profile, binding.dependency_profile):
        return RuntimeClosureAssessment(
            status=RuntimeClosureStatus.INCOMPATIBLE,
            closure_identity=None,
            exact_dependency_identities=(),
            limitations=("binding broadens Strategy dependency/network profile",),
        )
    missing_roles = tuple(sorted(set(strategy.required_roles) - set(binding.required_roles)))
    if missing_roles:
        return RuntimeClosureAssessment(
            status=RuntimeClosureStatus.INCOMPATIBLE,
            closure_identity=None,
            exact_dependency_identities=(),
            incomplete_roles=missing_roles,
        )
    if strategy.source_derived_text_capable and not binding.source_derived_text_capable:
        return RuntimeClosureAssessment(
            status=RuntimeClosureStatus.INCOMPATIBLE,
            closure_identity=None,
            exact_dependency_identities=(),
            limitations=("binding lacks required source-derived text capability",),
        )

    by_component = {item.component_id: item for item in resolutions}
    by_role = {item.role_id: item for item in role_resolutions}
    if len(by_role) != len(role_resolutions):
        raise ValueError("runtime role resolutions must be unique")

    missing: list[str] = []
    incompatible: list[str] = []
    indeterminate: list[str] = []
    incomplete_roles: set[str] = set()
    incompatible_roles: set[str] = set()
    indeterminate_roles: set[str] = set()
    identities: list[tuple[str, str]] = []
    environment_identities: list[tuple[str, str]] = []

    for role_id in binding.required_roles:
        role_resolution = by_role.get(role_id)
        if (
            role_resolution is None
            or not role_resolution.available
            or role_resolution.environment_identity is None
        ):
            incomplete_roles.add(role_id)
            continue
        if role_resolution.runtime_compatible is None:
            indeterminate_roles.add(role_id)
            continue
        if not role_resolution.runtime_compatible:
            incompatible_roles.add(role_id)
            continue
        environment_identities.append((role_id, role_resolution.environment_identity))

    for requirement in binding.dependency_requirements:
        dependency_resolution = by_component.get(requirement.component_id)
        if (
            dependency_resolution is None
            or not dependency_resolution.available
            or dependency_resolution.exact_identity is None
        ):
            missing.append(requirement.component_id)
            continue
        if dependency_resolution.acquired_during_material_execution:
            incompatible.append(requirement.component_id)
            continue
        if dependency_resolution.exact_identity not in requirement.allowed_identities:
            incompatible.append(requirement.component_id)
            continue
        if dependency_resolution.runtime_compatible is None:
            indeterminate.append(requirement.component_id)
            continue
        if not dependency_resolution.runtime_compatible:
            incompatible.append(requirement.component_id)
            continue
        unavailable_roles = set(requirement.required_roles) - set(
            dependency_resolution.eligible_roles
        )
        if unavailable_roles:
            incomplete_roles.update(unavailable_roles)
            continue
        identities.append((requirement.component_id, dependency_resolution.exact_identity))

    if incompatible or incompatible_roles:
        status = RuntimeClosureStatus.INCOMPATIBLE
    elif missing or incomplete_roles:
        status = RuntimeClosureStatus.INCOMPLETE
    elif indeterminate or indeterminate_roles:
        status = RuntimeClosureStatus.INDETERMINATE
    else:
        status = (
            RuntimeClosureStatus.SATISFIED_WITH_LIMITATIONS
            if binding.limitations
            else RuntimeClosureStatus.SATISFIED
        )

    closure_identity: str | None = None
    exact_identities = tuple(sorted(identities))
    exact_role_identities = tuple(sorted(environment_identities))
    if status in {
        RuntimeClosureStatus.SATISFIED,
        RuntimeClosureStatus.SATISFIED_WITH_LIMITATIONS,
    }:
        material = [
            binding.binding_id,
            binding.build_identity,
            binding.dependency_profile.value,
            *binding.required_roles,
        ]
        material.extend(f"{component}={identity}" for component, identity in exact_identities)
        material.extend(f"role:{role}={identity}" for role, identity in exact_role_identities)
        closure_identity = hashlib.sha256("\n".join(material).encode("utf-8")).hexdigest()

    return RuntimeClosureAssessment(
        status=status,
        closure_identity=closure_identity,
        exact_dependency_identities=exact_identities,
        exact_role_environment_identities=exact_role_identities,
        missing_components=tuple(sorted(missing)),
        incompatible_components=tuple(sorted(incompatible)),
        indeterminate_components=tuple(sorted(indeterminate)),
        incomplete_roles=tuple(sorted(incomplete_roles)),
        incompatible_roles=tuple(sorted(incompatible_roles)),
        indeterminate_roles=tuple(sorted(indeterminate_roles)),
        limitations=binding.limitations,
    )


def build_runtime_plan(
    activity_reference: TypedReference,
    strategy: StrategyRuntimeRequirements,
    binding: ImplementationBinding,
    closure: RuntimeClosureAssessment,
    *,
    learned_state_reference: TypedReference | None = None,
    direct_input_references: tuple[TypedReference, ...] = (),
) -> RuntimeRealizationPlan:
    if not closure.ready or closure.closure_identity is None:
        raise ValueError(f"runtime closure is not ready: {closure.status.value}")
    if binding.strategy_reference != strategy.strategy_reference:
        raise ValueError("implementation binding no longer matches Strategy revision")
    return RuntimeRealizationPlan(
        activity_reference=activity_reference,
        strategy_reference=strategy.strategy_reference,
        binding_id=binding.binding_id,
        build_identity=binding.build_identity,
        dependency_profile=binding.dependency_profile,
        closure_identity=closure.closure_identity,
        exact_dependency_identities=closure.exact_dependency_identities,
        exact_role_environment_identities=closure.exact_role_environment_identities,
        runtime_roles=binding.required_roles,
        learned_state_reference=learned_state_reference,
        direct_input_references=direct_input_references,
        limitations=closure.limitations,
    )
