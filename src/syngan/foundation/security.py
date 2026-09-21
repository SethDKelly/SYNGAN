"""Provider-neutral security, disclosure, dependency-trust, and no-egress primitives.

These values are cross-cutting realization contracts. They do not create a Security,
Policy, Authorization, Trust, Egress, Secret, or Tenant domain concept.
"""

from __future__ import annotations

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


class PrincipalKind(StrEnum):
    HUMAN = "human"
    SERVICE = "service"
    DELEGATED = "delegated"


class SecurityAction(StrEnum):
    ACTIVITY_COMMIT = "activity.commit"
    EXECUTION_START = "execution.start"
    EXECUTION_RETRY = "execution.retry"
    EXECUTION_RESUME = "execution.resume"
    EXECUTION_CANCEL = "execution.cancel"
    DEPENDENCY_RESOLVE = "dependency.resolve"
    DEPENDENCY_USE = "dependency.use"
    DEPENDENCY_ACQUIRE = "dependency.acquire"
    SOURCE_READ = "source.read"
    LEARNED_STATE_USE = "learned_state.use"
    LEARNED_STATE_INSPECT = "learned_state.inspect"
    LEARNED_STATE_RAW_READ = "learned_state.raw_read"
    LEARNED_STATE_EXPORT = "learned_state.export"
    CANDIDATE_WRITE = "candidate.write"
    CHECKPOINT_WRITE = "checkpoint.write"
    DIAGNOSTIC_WRITE = "diagnostic.write"
    CONTROL_INSPECT = "control.inspect"
    OUTPUT_READ = "output.read"
    OUTPUT_EXPORT = "output.export"
    EVIDENCE_READ = "evidence.read"
    EVIDENCE_DIAGNOSTIC_READ = "evidence.diagnostic_read"
    HISTORY_TRAVERSE = "history.traverse"
    HISTORY_COMPARE = "history.compare"
    REPRODUCIBILITY_ASSESS = "reproducibility.assess"
    PROVENANCE_CORRECT = "provenance.correct"
    NETWORK_CALL = "network.call"
    EGRESS_TRANSMIT = "egress.transmit"
    SECRET_RESOLVE = "secret.resolve"
    AUDIT_READ = "audit.read"


class AuthorizationOutcome(StrEnum):
    PERMIT = "permit"
    DENY = "deny"
    INDETERMINATE = "indeterminate"
    PERMIT_WITH_CONDITIONS = "permit-with-conditions"


class DisclosureState(StrEnum):
    RESOLVED = "resolved"
    ABSENT = "absent"
    UNKNOWN = "unknown"
    UNAVAILABLE = "unavailable"
    WITHHELD = "withheld"
    REDACTED = "redacted"
    INVALID = "invalid"


class NetworkPosture(StrEnum):
    OFFLINE_NO_EGRESS = "offline-no-egress"
    LOCAL_ONLY = "local-only"
    RUNTIME_NETWORK = "runtime-network"


class EgressCategory(StrEnum):
    NETWORK_NO_CONTENT = "network-no-content"
    NON_SENSITIVE_METADATA = "non-sensitive-metadata"
    SOURCE_DERIVED = "source-derived"
    SOURCE_RECORDS = "source-records"
    GENERATED_RECORDS = "generated-records"


class DependencyTrustState(StrEnum):
    TRUSTED = "trusted"
    UNTRUSTED = "untrusted"
    INDETERMINATE = "indeterminate"


class IntegrityState(StrEnum):
    VERIFIED = "verified"
    FAILED = "failed"
    INDETERMINATE = "indeterminate"


@dataclass(frozen=True, slots=True)
class PrincipalRef:
    principal_id: str
    kind: PrincipalKind
    security_domain: str
    delegated_from: TypedReference | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "principal_id", _token(self.principal_id, "principal id"))
        object.__setattr__(
            self, "security_domain", _token(self.security_domain, "security domain")
        )
        if self.kind is PrincipalKind.DELEGATED and self.delegated_from is None:
            raise ValueError("delegated principal requires parent activity/Attempt reference")
        if self.delegated_from is not None:
            self.delegated_from.require_exact_binding()


@dataclass(frozen=True, slots=True)
class ProtectedTarget:
    reference: TypedReference
    security_domain: str

    def __post_init__(self) -> None:
        self.reference.require_exact_binding()
        object.__setattr__(
            self, "security_domain", _token(self.security_domain, "target security domain")
        )


@dataclass(frozen=True, slots=True)
class AuthorizationRequest:
    principal: PrincipalRef
    action: SecurityAction
    target: ProtectedTarget
    destination: str | None = None
    egress_category: EgressCategory | None = None

    def __post_init__(self) -> None:
        if self.destination is not None:
            object.__setattr__(self, "destination", _token(self.destination, "destination"))


@dataclass(frozen=True, slots=True)
class AuthorizationDecision:
    outcome: AuthorizationOutcome
    decision_reference: str | None = None
    conditions: tuple[str, ...] = ()
    reason_code: str | None = None

    def __post_init__(self) -> None:
        if self.decision_reference is not None:
            object.__setattr__(
                self,
                "decision_reference",
                _token(self.decision_reference, "authorization decision reference"),
            )
        normalized = tuple(_token(item, "authorization condition") for item in self.conditions)
        object.__setattr__(self, "conditions", normalized)
        if self.reason_code is not None:
            object.__setattr__(self, "reason_code", _token(self.reason_code, "reason code"))
        if self.outcome is AuthorizationOutcome.PERMIT_WITH_CONDITIONS and not normalized:
            raise ValueError("conditional permit requires at least one condition")
        if self.outcome is not AuthorizationOutcome.PERMIT_WITH_CONDITIONS and normalized:
            raise ValueError("only conditional permit may carry conditions")


@dataclass(frozen=True, slots=True)
class SecurityExecutionProfile:
    profile_id: str
    network_posture: NetworkPosture
    allowed_dependency_provider_classes: tuple[str, ...] = ()
    allowed_destinations: tuple[str, ...] = ()
    allowed_egress_categories: tuple[EgressCategory, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "profile_id", _token(self.profile_id, "security profile id"))
        providers = tuple(
            _token(item, "dependency provider class")
            for item in self.allowed_dependency_provider_classes
        )
        destinations = tuple(_token(item, "destination") for item in self.allowed_destinations)
        object.__setattr__(self, "allowed_dependency_provider_classes", providers)
        object.__setattr__(self, "allowed_destinations", destinations)
        if self.network_posture is NetworkPosture.OFFLINE_NO_EGRESS:
            if destinations or self.allowed_egress_categories:
                raise ValueError("offline/no-egress profile cannot allow destinations or egress")


@dataclass(frozen=True, slots=True)
class CapabilityRequirement:
    action: SecurityAction
    target: ProtectedTarget
    destination: str | None = None
    egress_category: EgressCategory | None = None

    def __post_init__(self) -> None:
        if self.destination is not None:
            object.__setattr__(self, "destination", _token(self.destination, "destination"))
        if self.action is SecurityAction.EGRESS_TRANSMIT:
            if self.destination is None or self.egress_category is None:
                raise ValueError("egress capability requires destination and category")
        if self.action is SecurityAction.NETWORK_CALL and self.destination is None:
            raise ValueError("network capability requires a destination")


@dataclass(frozen=True, slots=True)
class CapabilityGrant:
    principal: PrincipalRef
    attempt_reference: TypedReference
    requirements: tuple[CapabilityRequirement, ...]
    decision_references: tuple[str, ...]

    def __post_init__(self) -> None:
        self.attempt_reference.require_exact_binding()
        if len(self.requirements) != len(self.decision_references):
            raise ValueError("each granted capability requires one decision reference")


@dataclass(frozen=True, slots=True)
class DependencySecurityFacts:
    component_id: str
    exact_identity: str
    provider_class: str
    integrity: IntegrityState
    trust: DependencyTrustState

    def __post_init__(self) -> None:
        object.__setattr__(self, "component_id", _token(self.component_id, "component id"))
        object.__setattr__(
            self, "exact_identity", _token(self.exact_identity, "dependency identity")
        )
        object.__setattr__(
            self, "provider_class", _token(self.provider_class, "dependency provider class")
        )


@dataclass(frozen=True, slots=True)
class DependencySecurityAssessment:
    component_id: str
    permitted: bool
    identity_match: bool
    integrity: IntegrityState
    trust: DependencyTrustState
    authorized: bool
    profile_compatible: bool
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class SecretRef:
    provider_kind: str
    logical_name: str
    service_role: str
    security_domain: str

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "provider_kind",
            _token(self.provider_kind, "secret provider kind"),
        )
        object.__setattr__(
            self,
            "logical_name",
            _token(self.logical_name, "secret logical name"),
        )
        object.__setattr__(
            self,
            "service_role",
            _token(self.service_role, "secret service role"),
        )
        object.__setattr__(
            self, "security_domain", _token(self.security_domain, "secret security domain")
        )


@dataclass(frozen=True, slots=True, repr=False)
class SecretMaterial:
    value: str

    def __post_init__(self) -> None:
        if not self.value:
            raise ValueError("secret material must be non-empty")

    def __repr__(self) -> str:
        return "SecretMaterial(<redacted>)"


@dataclass(frozen=True, slots=True)
class DisclosureView:
    state: DisclosureState
    reference: TypedReference | None = None
    detail: object | None = None

    def __post_init__(self) -> None:
        if self.reference is not None:
            self.reference.require_exact_binding()
        if self.state is DisclosureState.RESOLVED and self.detail is None:
            raise ValueError("resolved disclosure requires detail")
        if (
            self.state in {DisclosureState.ABSENT, DisclosureState.WITHHELD}
            and self.detail is not None
        ):
            raise ValueError(
                "absent/withheld disclosure cannot carry protected detail"
            )


@dataclass(frozen=True, slots=True)
class SecurityAuditEvent:
    principal_id: str
    action: SecurityAction
    target_reference: TypedReference
    outcome: AuthorizationOutcome
    decision_reference: str | None = None
    reason_code: str | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "principal_id", _token(self.principal_id, "audit principal id"))
        self.target_reference.require_exact_binding()
