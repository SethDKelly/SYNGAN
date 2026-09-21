"""Application-level security composition without acquiring semantic domain authority."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from syngan.domain.provenance import HistoricalReferenceView, HistoricalResolution
from syngan.foundation.identity import TypedReference
from syngan.foundation.runtime import DependencyProfile, DependencyRequirement, DependencyResolution
from syngan.foundation.security import (
    AuthorizationDecision,
    AuthorizationOutcome,
    AuthorizationRequest,
    CapabilityGrant,
    CapabilityRequirement,
    DependencySecurityAssessment,
    DependencySecurityFacts,
    DependencyTrustState,
    DisclosureState,
    DisclosureView,
    EgressCategory,
    IntegrityState,
    NetworkPosture,
    PrincipalRef,
    ProtectedTarget,
    SecretMaterial,
    SecretRef,
    SecurityAction,
    SecurityAuditEvent,
    SecurityExecutionProfile,
)
from syngan.ports.security import AuthorizationAuthority, SecretBroker, SecurityAuditSink


class AuthorizationDenied(PermissionError):
    pass


class AuthorizationIndeterminate(PermissionError):
    pass


class SecurityCompatibilityError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class AuthorizedDecision:
    request: AuthorizationRequest
    decision: AuthorizationDecision


class SecurityService:
    """Coordinate current policy decisions and scoped runtime authority."""

    def __init__(
        self,
        authority: AuthorizationAuthority,
        *,
        audit_sink: SecurityAuditSink | None = None,
        secret_broker: SecretBroker | None = None,
    ) -> None:
        self._authority = authority
        self._audit = audit_sink
        self._secrets = secret_broker

    def authorize(
        self,
        request: AuthorizationRequest,
        *,
        satisfied_conditions: tuple[str, ...] = (),
    ) -> AuthorizedDecision:
        decision = self._authority.authorize(request)
        self._audit_decision(request, decision)

        if decision.outcome is AuthorizationOutcome.DENY:
            raise AuthorizationDenied(decision.reason_code or "authorization denied")
        if decision.outcome is AuthorizationOutcome.INDETERMINATE:
            raise AuthorizationIndeterminate(
                decision.reason_code or "authorization indeterminate"
            )
        if decision.outcome is AuthorizationOutcome.PERMIT_WITH_CONDITIONS:
            missing = set(decision.conditions) - set(satisfied_conditions)
            if missing:
                raise AuthorizationDenied(
                    f"authorization conditions are not satisfied: {sorted(missing)}"
                )
        if decision.decision_reference is None:
            raise ValueError("permitted action requires an audit-safe decision reference")
        return AuthorizedDecision(request, decision)

    def compose_capability_grant(
        self,
        principal: PrincipalRef,
        attempt_reference: TypedReference,
        requirements: tuple[CapabilityRequirement, ...],
        profile: SecurityExecutionProfile,
        *,
        satisfied_conditions: tuple[str, ...] = (),
    ) -> CapabilityGrant:
        attempt_reference.require_exact_binding()
        decisions: list[str] = []
        for requirement in requirements:
            self._require_profile_compatibility(requirement, profile)
            request = AuthorizationRequest(
                principal=principal,
                action=requirement.action,
                target=requirement.target,
                destination=requirement.destination,
                egress_category=requirement.egress_category,
            )
            authorized = self.authorize(
                request,
                satisfied_conditions=satisfied_conditions,
            )
            assert authorized.decision.decision_reference is not None
            decisions.append(authorized.decision.decision_reference)

        return CapabilityGrant(
            principal=principal,
            attempt_reference=attempt_reference,
            requirements=requirements,
            decision_references=tuple(decisions),
        )

    def assess_dependency(
        self,
        principal: PrincipalRef,
        target: ProtectedTarget,
        requirement: DependencyRequirement,
        resolution: DependencyResolution,
        security: DependencySecurityFacts,
        profile: SecurityExecutionProfile,
    ) -> DependencySecurityAssessment:
        reasons: list[str] = []
        identity_match = (
            resolution.exact_identity is not None
            and resolution.exact_identity in requirement.allowed_identities
            and resolution.exact_identity == security.exact_identity
        )
        if not resolution.available:
            reasons.append("dependency unavailable")
        if not identity_match:
            reasons.append("dependency identity mismatch")
        if resolution.runtime_compatible is not True:
            reasons.append("runtime compatibility not established")
        if resolution.acquired_during_material_execution:
            reasons.append("runtime dependency acquisition is prohibited")
        if security.integrity is not IntegrityState.VERIFIED:
            reasons.append("dependency integrity not verified")
        if security.trust is not DependencyTrustState.TRUSTED:
            reasons.append("dependency trust not established")

        profile_compatible = security.provider_class in profile.allowed_dependency_provider_classes
        if not profile_compatible:
            reasons.append("dependency provider is not allowed by the security profile")

        authorized = False
        try:
            self.authorize(
                AuthorizationRequest(
                    principal=principal,
                    action=SecurityAction.DEPENDENCY_USE,
                    target=target,
                )
            )
            authorized = True
        except (AuthorizationDenied, AuthorizationIndeterminate):
            reasons.append("dependency use is not currently authorized")

        permitted = not reasons
        return DependencySecurityAssessment(
            component_id=requirement.component_id,
            permitted=permitted,
            identity_match=identity_match,
            integrity=security.integrity,
            trust=security.trust,
            authorized=authorized,
            profile_compatible=profile_compatible,
            reasons=tuple(reasons),
        )

    def resolve_secret(
        self,
        principal: PrincipalRef,
        attempt_target: ProtectedTarget,
        secret_ref: SecretRef,
    ) -> SecretMaterial:
        if self._secrets is None:
            raise RuntimeError("no secret broker is configured")
        if secret_ref.security_domain != attempt_target.security_domain:
            raise SecurityCompatibilityError("secret and Attempt security domains differ")
        self.authorize(
            AuthorizationRequest(
                principal=principal,
                action=SecurityAction.SECRET_RESOLVE,
                target=attempt_target,
            )
        )
        return self._secrets.resolve(secret_ref)

    def disclose(
        self,
        principal: PrincipalRef,
        target: ProtectedTarget,
        *,
        exists: bool,
        detail_supplier: Callable[[], object],
        summary_supplier: Callable[[], object] | None = None,
    ) -> DisclosureView:
        existence_request = AuthorizationRequest(
            principal=principal,
            action=SecurityAction.CONTROL_INSPECT,
            target=target,
        )
        existence_decision = self._authority.authorize(existence_request)
        self._audit_decision(existence_request, existence_decision)

        if existence_decision.outcome not in {
            AuthorizationOutcome.PERMIT,
            AuthorizationOutcome.PERMIT_WITH_CONDITIONS,
        }:
            return DisclosureView(DisclosureState.WITHHELD)
        if not exists:
            return DisclosureView(DisclosureState.ABSENT, reference=target.reference)

        detail_request = AuthorizationRequest(
            principal=principal,
            action=SecurityAction.HISTORY_TRAVERSE,
            target=target,
        )
        detail_decision = self._authority.authorize(detail_request)
        self._audit_decision(detail_request, detail_decision)

        if detail_decision.outcome is AuthorizationOutcome.PERMIT:
            return DisclosureView(
                DisclosureState.RESOLVED,
                reference=target.reference,
                detail=detail_supplier(),
            )
        if (
            detail_decision.outcome is AuthorizationOutcome.PERMIT_WITH_CONDITIONS
            and summary_supplier is not None
        ):
            return DisclosureView(
                DisclosureState.REDACTED,
                reference=target.reference,
                detail=summary_supplier(),
            )
        return DisclosureView(DisclosureState.WITHHELD, reference=target.reference)

    def disclose_historical_reference(
        self,
        principal: PrincipalRef,
        target: ProtectedTarget,
        view: HistoricalReferenceView,
    ) -> HistoricalReferenceView:
        decision = self._authority.authorize(
            AuthorizationRequest(
                principal=principal,
                action=SecurityAction.HISTORY_TRAVERSE,
                target=target,
            )
        )
        if decision.outcome is not AuthorizationOutcome.PERMIT:
            return HistoricalReferenceView(
                reference=view.reference,
                knowledge_basis=view.knowledge_basis,
                resolution=HistoricalResolution.WITHHELD,
            )
        return view

    def _require_profile_compatibility(
        self,
        requirement: CapabilityRequirement,
        profile: SecurityExecutionProfile,
    ) -> None:
        if requirement.action in {
            SecurityAction.NETWORK_CALL,
            SecurityAction.EGRESS_TRANSMIT,
        }:
            if profile.network_posture is NetworkPosture.OFFLINE_NO_EGRESS:
                raise SecurityCompatibilityError(
                    "offline/no-egress profile cannot compose network capability"
                )
            assert requirement.destination is not None
            if requirement.destination not in profile.allowed_destinations:
                raise SecurityCompatibilityError("destination is not allowed by security profile")
            if (
                requirement.action is SecurityAction.EGRESS_TRANSMIT
                and requirement.egress_category not in profile.allowed_egress_categories
            ):
                raise SecurityCompatibilityError(
                    "egress category is not allowed by security profile"
                )

    def _audit_decision(
        self,
        request: AuthorizationRequest,
        decision: AuthorizationDecision,
    ) -> None:
        if self._audit is None:
            return
        self._audit.emit(
            SecurityAuditEvent(
                principal_id=request.principal.principal_id,
                action=request.action,
                target_reference=request.target.reference,
                outcome=decision.outcome,
                decision_reference=decision.decision_reference,
                reason_code=decision.reason_code,
            )
        )


def ensure_dependency_profile_security(
    dependency_profile: DependencyProfile,
    security_profile: SecurityExecutionProfile,
) -> None:
    if dependency_profile is DependencyProfile.SELF_CONTAINED:
        return
    if (
        security_profile.network_posture is NetworkPosture.OFFLINE_NO_EGRESS
        and dependency_profile
        in {DependencyProfile.ACQUISITION_NETWORK, DependencyProfile.RUNTIME_NETWORK}
    ):
        raise SecurityCompatibilityError(
            "offline/no-egress security profile cannot widen dependency network semantics"
        )
