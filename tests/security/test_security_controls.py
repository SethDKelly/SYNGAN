from __future__ import annotations

from dataclasses import dataclass, field

import pytest

from syngan.application.security import (
    AuthorizationDenied,
    AuthorizationIndeterminate,
    SecurityCompatibilityError,
    SecurityService,
    ensure_dependency_profile_security,
)
from syngan.domain.provenance import (
    HistoricalKnowledgeBasis,
    HistoricalReferenceView,
    HistoricalResolution,
)
from syngan.foundation.identity import (
    AuthorityScope,
    CommitmentSnapshotId,
    LogicalId,
    ResourceKey,
    ResourceKind,
    TypedReference,
)
from syngan.foundation.representation import EncodedPayload
from syngan.foundation.runtime import (
    DependencyProfile,
    DependencyRequirement,
    DependencyResolution,
)
from syngan.foundation.security import (
    AuthorizationDecision,
    AuthorizationOutcome,
    AuthorizationRequest,
    CapabilityRequirement,
    DependencySecurityFacts,
    DependencyTrustState,
    DisclosureState,
    EgressCategory,
    IntegrityState,
    NetworkPosture,
    PrincipalKind,
    PrincipalRef,
    ProtectedTarget,
    SecretMaterial,
    SecretRef,
    SecurityAction,
    SecurityAuditEvent,
    SecurityExecutionProfile,
)

pytestmark = pytest.mark.security

SCOPE = AuthorityScope("test")


def exact(kind: str, resource_id: str) -> TypedReference:
    return TypedReference(
        key=ResourceKey(SCOPE, ResourceKind(kind), LogicalId(resource_id)),
        commitment_snapshot_id=CommitmentSnapshotId(f"{resource_id}-snapshot"),
    )


def principal() -> PrincipalRef:
    return PrincipalRef("user-1", PrincipalKind.HUMAN, "tenant-a")


def target(kind: str = "generation", resource_id: str = "g1") -> ProtectedTarget:
    return ProtectedTarget(exact(kind, resource_id), "tenant-a")


@dataclass
class RuleAuthority:
    rules: dict[SecurityAction, AuthorizationDecision]

    def authorize(self, request: AuthorizationRequest) -> AuthorizationDecision:
        return self.rules.get(
            request.action,
            AuthorizationDecision(
                AuthorizationOutcome.DENY,
                decision_reference="deny-default",
                reason_code="not-permitted",
            ),
        )


@dataclass
class RecordingAudit:
    events: list[SecurityAuditEvent] = field(default_factory=list)

    def emit(self, event: SecurityAuditEvent) -> None:
        self.events.append(event)


@dataclass
class StaticSecretBroker:
    material: SecretMaterial
    calls: int = 0

    def resolve(self, secret_ref: SecretRef) -> SecretMaterial:
        self.calls += 1
        return self.material


def permit(reference: str) -> AuthorizationDecision:
    return AuthorizationDecision(
        AuthorizationOutcome.PERMIT,
        decision_reference=reference,
    )


def test_action_authorization_is_distinct_and_indeterminate_fails_closed() -> None:
    service = SecurityService(
        RuleAuthority(
            {
                SecurityAction.LEARNED_STATE_USE: permit("use-ok"),
                SecurityAction.LEARNED_STATE_RAW_READ: AuthorizationDecision(
                    AuthorizationOutcome.DENY,
                    decision_reference="raw-deny",
                ),
                SecurityAction.LEARNED_STATE_EXPORT: AuthorizationDecision(
                    AuthorizationOutcome.INDETERMINATE,
                    decision_reference="export-unknown",
                ),
            }
        )
    )
    resource = target("learned-state", "ls1")

    service.authorize(
        AuthorizationRequest(principal(), SecurityAction.LEARNED_STATE_USE, resource)
    )
    with pytest.raises(AuthorizationDenied):
        service.authorize(
            AuthorizationRequest(
                principal(),
                SecurityAction.LEARNED_STATE_RAW_READ,
                resource,
            )
        )
    with pytest.raises(AuthorizationIndeterminate):
        service.authorize(
            AuthorizationRequest(
                principal(),
                SecurityAction.LEARNED_STATE_EXPORT,
                resource,
            )
        )


def test_conditional_authorization_requires_explicit_satisfaction() -> None:
    decision = AuthorizationDecision(
        AuthorizationOutcome.PERMIT_WITH_CONDITIONS,
        decision_reference="conditional",
        conditions=("aggregate-only",),
    )
    service = SecurityService(RuleAuthority({SecurityAction.EGRESS_TRANSMIT: decision}))
    request = AuthorizationRequest(
        principal(),
        SecurityAction.EGRESS_TRANSMIT,
        target(),
        destination="service-a",
        egress_category=EgressCategory.SOURCE_DERIVED,
    )

    with pytest.raises(AuthorizationDenied, match="conditions"):
        service.authorize(request)
    service.authorize(request, satisfied_conditions=("aggregate-only",))


def test_offline_no_egress_profile_cannot_be_widened_by_permission() -> None:
    service = SecurityService(
        RuleAuthority(
            {
                SecurityAction.NETWORK_CALL: permit("network-permit"),
                SecurityAction.EGRESS_TRANSMIT: permit("egress-permit"),
            }
        )
    )
    profile = SecurityExecutionProfile(
        "offline",
        NetworkPosture.OFFLINE_NO_EGRESS,
        allowed_dependency_provider_classes=("local",),
    )

    with pytest.raises(SecurityCompatibilityError, match="offline/no-egress"):
        service.compose_capability_grant(
            principal(),
            exact("attempt", "a1"),
            (
                CapabilityRequirement(
                    SecurityAction.NETWORK_CALL,
                    target(),
                    destination="remote-service",
                ),
            ),
            profile,
        )

    with pytest.raises(SecurityCompatibilityError):
        ensure_dependency_profile_security(DependencyProfile.RUNTIME_NETWORK, profile)


def test_network_profile_scopes_destination_and_egress_category() -> None:
    service = SecurityService(
        RuleAuthority(
            {
                SecurityAction.NETWORK_CALL: permit("network"),
                SecurityAction.EGRESS_TRANSMIT: permit("egress"),
            }
        )
    )
    profile = SecurityExecutionProfile(
        "bounded-network",
        NetworkPosture.RUNTIME_NETWORK,
        allowed_dependency_provider_classes=("private",),
        allowed_destinations=("approved-service",),
        allowed_egress_categories=(EgressCategory.NON_SENSITIVE_METADATA,),
    )

    grant = service.compose_capability_grant(
        principal(),
        exact("attempt", "a1"),
        (
            CapabilityRequirement(
                SecurityAction.NETWORK_CALL,
                target(),
                destination="approved-service",
            ),
            CapabilityRequirement(
                SecurityAction.EGRESS_TRANSMIT,
                target(),
                destination="approved-service",
                egress_category=EgressCategory.NON_SENSITIVE_METADATA,
            ),
        ),
        profile,
    )
    assert grant.decision_references == ("network", "egress")

    with pytest.raises(SecurityCompatibilityError, match="egress category"):
        service.compose_capability_grant(
            principal(),
            exact("attempt", "a2"),
            (
                CapabilityRequirement(
                    SecurityAction.EGRESS_TRANSMIT,
                    target(),
                    destination="approved-service",
                    egress_category=EgressCategory.SOURCE_RECORDS,
                ),
            ),
            profile,
        )


def test_dependency_presence_integrity_trust_authorization_are_independent() -> None:
    service = SecurityService(
        RuleAuthority({SecurityAction.DEPENDENCY_USE: permit("dependency-use")})
    )
    requirement = DependencyRequirement("model", ("sha256:good",), ("worker",))
    resolution = DependencyResolution(
        component_id="model",
        exact_identity="sha256:good",
        available=True,
        runtime_compatible=True,
        eligible_roles=("worker",),
    )
    profile = SecurityExecutionProfile(
        "private",
        NetworkPosture.LOCAL_ONLY,
        allowed_dependency_provider_classes=("private-registry",),
    )
    untrusted = DependencySecurityFacts(
        component_id="model",
        exact_identity="sha256:good",
        provider_class="private-registry",
        integrity=IntegrityState.VERIFIED,
        trust=DependencyTrustState.UNTRUSTED,
    )

    assessment = service.assess_dependency(
        principal(),
        target("dependency", "model"),
        requirement,
        resolution,
        untrusted,
        profile,
    )
    assert assessment.authorized is True
    assert assessment.identity_match is True
    assert assessment.permitted is False
    assert "dependency trust not established" in assessment.reasons

    trusted = DependencySecurityFacts(
        component_id="model",
        exact_identity="sha256:good",
        provider_class="private-registry",
        integrity=IntegrityState.VERIFIED,
        trust=DependencyTrustState.TRUSTED,
    )
    assessment = service.assess_dependency(
        principal(),
        target("dependency", "model"),
        requirement,
        resolution,
        trusted,
        profile,
    )
    assert assessment.permitted is True


def test_hidden_runtime_dependency_acquisition_is_rejected() -> None:
    service = SecurityService(
        RuleAuthority({SecurityAction.DEPENDENCY_USE: permit("dependency-use")})
    )
    requirement = DependencyRequirement("model", ("sha256:good",), ("worker",))
    resolution = DependencyResolution(
        component_id="model",
        exact_identity="sha256:good",
        available=True,
        runtime_compatible=True,
        eligible_roles=("worker",),
        acquired_during_material_execution=True,
    )
    security = DependencySecurityFacts(
        "model",
        "sha256:good",
        "local",
        IntegrityState.VERIFIED,
        DependencyTrustState.TRUSTED,
    )
    profile = SecurityExecutionProfile(
        "offline",
        NetworkPosture.OFFLINE_NO_EGRESS,
        allowed_dependency_provider_classes=("local",),
    )

    assessment = service.assess_dependency(
        principal(),
        target("dependency", "model"),
        requirement,
        resolution,
        security,
        profile,
    )
    assert assessment.permitted is False
    assert "runtime dependency acquisition is prohibited" in assessment.reasons


def test_protected_existence_can_hide_existing_and_absent_targets_identically() -> None:
    service = SecurityService(
        RuleAuthority(
            {
                SecurityAction.CONTROL_INSPECT: AuthorizationDecision(
                    AuthorizationOutcome.DENY,
                    decision_reference="existence-denied",
                )
            }
        )
    )
    protected = target("evidence", "ev1")

    existing = service.disclose(
        principal(),
        protected,
        exists=True,
        detail_supplier=lambda: {"secret": 1},
    )
    absent = service.disclose(
        principal(),
        protected,
        exists=False,
        detail_supplier=lambda: {"secret": 1},
    )

    assert existing == DisclosureState.WITHHELD or existing.state is DisclosureState.WITHHELD
    assert absent.state is DisclosureState.WITHHELD
    assert existing.reference is None
    assert absent.reference is None


def test_authorized_summary_does_not_mutate_canonical_detail() -> None:
    canonical = {"examples": ["protected-row"], "count": 1}
    service = SecurityService(
        RuleAuthority(
            {
                SecurityAction.CONTROL_INSPECT: permit("existence"),
                SecurityAction.HISTORY_TRAVERSE: AuthorizationDecision(
                    AuthorizationOutcome.PERMIT_WITH_CONDITIONS,
                    decision_reference="summary-only",
                    conditions=("summary-only",),
                ),
            }
        )
    )

    view = service.disclose(
        principal(),
        target("evidence", "ev1"),
        exists=True,
        detail_supplier=lambda: canonical,
        summary_supplier=lambda: {"count": canonical["count"]},
    )

    assert view.state is DisclosureState.REDACTED
    assert view.detail == {"count": 1}
    assert canonical == {"examples": ["protected-row"], "count": 1}


def test_historical_reference_projects_to_withheld_without_history_rewrite() -> None:
    reference = exact("evidence", "ev1")
    canonical = HistoricalReferenceView(
        reference=reference,
        knowledge_basis=HistoricalKnowledgeBasis.DIRECT,
        resolution=HistoricalResolution.RESOLVED,
        payload=EncodedPayload.from_object({"result": "protected"}),
    )
    service = SecurityService(
        RuleAuthority(
            {
                SecurityAction.HISTORY_TRAVERSE: AuthorizationDecision(
                    AuthorizationOutcome.DENY,
                    decision_reference="history-deny",
                )
            }
        )
    )

    projected = service.disclose_historical_reference(
        principal(),
        ProtectedTarget(reference, "tenant-a"),
        canonical,
    )

    assert projected.resolution is HistoricalResolution.WITHHELD
    assert projected.payload is None
    assert canonical.resolution is HistoricalResolution.RESOLVED
    assert canonical.payload is not None


def test_secret_resolution_reauthorizes_and_bearer_is_redacted() -> None:
    broker = StaticSecretBroker(SecretMaterial("super-secret"))
    audit = RecordingAudit()
    service = SecurityService(
        RuleAuthority({SecurityAction.SECRET_RESOLVE: permit("secret-use")}),
        audit_sink=audit,
        secret_broker=broker,
    )
    secret_ref = SecretRef("local-vault", "api-key", "remote-method", "tenant-a")

    material = service.resolve_secret(
        principal(),
        target("attempt", "a1"),
        secret_ref,
    )

    assert material.value == "super-secret"
    assert repr(material) == "SecretMaterial(<redacted>)"
    assert broker.calls == 1
    assert audit.events[0].action is SecurityAction.SECRET_RESOLVE
    assert "super-secret" not in repr(audit.events[0])


def test_resource_handle_possession_is_not_authorization() -> None:
    resource = target("output", "o1")
    service = SecurityService(
        RuleAuthority(
            {
                SecurityAction.OUTPUT_READ: AuthorizationDecision(
                    AuthorizationOutcome.DENY,
                    decision_reference="output-deny",
                )
            }
        )
    )

    with pytest.raises(AuthorizationDenied):
        service.authorize(
            AuthorizationRequest(principal(), SecurityAction.OUTPUT_READ, resource)
        )
