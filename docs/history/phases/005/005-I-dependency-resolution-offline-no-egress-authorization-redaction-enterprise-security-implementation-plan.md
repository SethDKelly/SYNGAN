---
type: Phase Record
title: 005-I — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan
status: complete
---

# 005-I — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan

## Objective

Translate the accepted 004-H enterprise-security architecture plus the concrete 005-D through 005-H control/data/runtime/recovery/history plans into a concrete **future implementation plan** for dependency resolution, offline/no-egress operation, authorization, capability delegation, secret handling, redaction/disclosure, security audit and tenant/security-domain isolation.

**No production implementation is authorized or performed by this phase.** Phase 005 remains planning-only.

## Entry authority

005-I is downstream of:

- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](../../architecture/dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md);
- [005-B Verification Strategy](../../implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [005-D Public Resource/Control-Plane Plan](../../implementation/public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md);
- [005-E Spark Data Boundary Plan](../../implementation/spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md);
- [005-F Runtime/SPI/Learned-State Plan](../../implementation/strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md);
- [005-G Execution/Recovery Plan](../../implementation/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-plan.md);
- [005-H Evidence/Provenance/History Plan](../../implementation/evaluation-evidence-provenance-historical-query-reproducibility-plan.md).

## Canonical authority created

005-I establishes:

[Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan](../../implementation/dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security-plan.md).

## Planning-only clarification

005-I creates no security package, authentication/authorization code, policy integration, dependency/artifact resolver, secret-manager adapter, network controls, security SQL tables/migrations, security tests, CI workflows, or deployment infrastructure.

All package paths, ports, action names, value roles, error families and I1-I10 steps are future implementation contracts only.

005-I also does not imply Jackson-style design completion. 005-K must still make an explicit methodology-completeness decision before any later phase may authorize coding.

## Core security decisions

Accepted future implementation rules include:

- semantic dependency/network/egress requirements remain separate from current environmental resolution, trust/approval, authorization and runtime capability issuance;
- exact dependency identity is distinct from mutable path/tag/URI/package/model aliases;
- resolver existence does not imply integrity, trust, compatibility or authorization;
- runtime never auto-installs packages, downloads models, queries public registries, enables telemetry, or falls back to a remote service silently;
- explicit acquisition/provisioning is separate from committed runtime and still requires integrity/trust/authorization before use;
- supported core workflows have a first-class offline/no-egress profile after approved local/private provisioning;
- network availability, destination, egress category, security domain and current authorization remain separate;
- committed EgressPlan declares expected behavior but does not authorize transmission;
- action-specific authorization replaces a universal resource permission Boolean;
- commit-time authorization is not permanent future permission; sensitive use/retry/resume/export/history actions re-authorize;
- runtime capabilities are bounded by semantic requirement ∩ current authorization ∩ deployment capability;
- durable handles/refs never function as bearer credentials;
- short-lived secret/credential values are resolved at use time and excluded from canonical resources/history/manifests/checkpoints/logs;
- extension-provider loading and unsafe Learned-State codec/deserialization are trust/authorization-sensitive executable actions;
- authorization revocation may block continuation without rewriting historical commitments or results;
- authorization revocation and 005-G fencing remain complementary controls;
- source, Learned-State, candidate/output, diagnostics, control metadata, Evidence, Provenance, query projections and reproducibility explanations all participate in disclosure policy;
- redaction/withholding is view-time and cannot rewrite canonical history or collapse protected existence into semantic absence;
- derived indexes/counts/reverse lookup/search are inside the security boundary;
- security audit remains distinct from Provenance and telemetry;
- tenant/security-domain context is explicit across resource actions, caches/indexes and runtime capability composition;
- no specific enterprise IAM/policy/secret/network/KMS/catalog/DLP/security product is selected by 005-I.

## Future contract roles

005-I plans future value/port responsibilities equivalent to:

```text
PrincipalRef
SecurityAction
AuthorizationRequest
AuthorizationDecision
DependencyRequirementRef
DependencyResolution
SecurityExecutionProfile
EgressCategory
EgressPlan
CapabilityGrant
SecretRef
DisclosureState
SecurityAuditSink
```

These are implementation/integration contracts, not new accepted domain concepts.

## Dependency-resolution plan

A future dependency resolution retains independent facts for:

```text
availability
exact identity match
integrity/authenticity
trust/approval
activity/runtime compatibility
current authorization
network/egress requirements
```

and preserves failures such as missing, wrong identity, integrity failure/unverified, untrusted, incompatible, unauthorized and indeterminate.

Mutable locators remain locators unless the provider establishes exact immutable identity strong enough for historical/reproducibility requirements.

A resolver may locate and describe an artifact but cannot make it trusted or authorized merely by returning it.

## Explicit acquisition/offline plan

Dependency acquisition is planned as explicit provisioning outside committed runtime.

The future `offline_no_egress` profile requires approved package/runtime/dependency components to be provisioned locally/private, no hidden remote inference/service dependency, no externally required telemetry, and deployment enforcement capable of preventing ambient outbound access to the declared strength.

Enforcement is defense-in-depth across readiness, dependency provider selection, authorization, Attempt capability composition, narrow runtime ports, deployment controls and audit.

## Egress plan

The future implementation preserves typed categories equivalent to:

```text
network_no_content
non_sensitive_metadata
source_derived
source_records
generated_records
```

and one immutable committed/runtime `EgressPlan` identifying approved/required destination/service role, category, source/security domain, purpose and network posture.

Before actual transmission, current authorization evaluates the exact action. A protected indeterminate decision fails closed.

Runtime undeclared egress does not widen the plan automatically; it is blocked/reported and may make the current binding/activity incompatible.

## Authorization/capability plan

005-I defines an action-oriented future authorization vocabulary covering commit/start/retry/resume/cancel, dependency resolution/use/acquisition, source read, Learned-State use/raw-read/export, candidate/checkpoint/diagnostic writes, output read/export, Evidence/diagnostics, history traversal/comparison/reproducibility, Provenance correction, network/egress, secret resolution and administrative/security actions.

A future AuthorizationRequest includes verified principal/service/delegation, exact resource/action, security domain/tenant and material data/egress/activity context.

AuthorizationDecision preserves permit, deny, indeterminate and permit-with-conditions.

An Attempt receives only narrow runtime capabilities for exact data/state/dependency reads, fenced writes, approved remote calls and secret resolution. Runtime adapters do not receive broad database credentials or unrestricted network/canonical-state access.

## Secret/code-loading plan

Future canonical state may persist only non-secret `SecretRef` values where allowed.

A SecretBroker authorizes and resolves short-lived credentials at use time. Bearer values cannot be persisted in commitments, runtime invocation state, handles, Provenance, Evidence, manifests, checkpoint metadata, idempotency records, extension bindings or ordinary logs.

Installed/discovered extension code and Learned-State codecs remain subject to integrity/trust/authorization before import/deserialization. `installed` is distinct from `trusted`, `authorized`, and `compatible`.

## Data/control/history access plan

Security distinguishes Learned-State use from metadata inspection, raw state read and export; candidate write from candidate read/export; Evidence summary from diagnostic access; and Generation completion from output export.

Control-plane identities/relationships may themselves be sensitive.

005-H history/query services therefore authorize target existence, edge/path traversal, neighboring resources/fields, counts, Execution details, diagnostics, dependencies and reproducibility reasons rather than applying one final response redaction after unrestricted traversal.

Derived search/index/cache views remain subject to the same disclosure boundary as canonical records.

## Disclosure/redaction plan

Future response logic preserves equivalents of:

```text
resolved
absent
unknown_or_indeterminate
unavailable
withheld
redacted_or_authorized_summary
invalid
```

Protected resource/edge existence may itself be hidden according to policy.

Redaction is view-time only. It may omit fields, return an authorized summary, withhold an entire path or suppress counts, but cannot fabricate values or rewrite protected existence as semantic absence.

Reproducibility reasons may similarly be full, policy-safe summaries or withheld without altering the underlying support/feasibility classification.

## Revocation/recovery plan

005-G retry/resume preserves committed semantics but must revalidate current authorization for sensitive actions.

A semantically valid checkpoint may be currently blocked because source/dependency/secret/Learned-State/network authorization changed.

Revocation stops new capability issuance/renewal and may trigger cancellation; 005-G WriterFence continues to prevent stale authoritative mutation even if an old physical process remains alive.

A later grant does not revive a cancelled/fenced Attempt's old authority.

## Audit/tenant-isolation plan

Security audit records material permitted/denied access, trust failures, secret resolution, egress decisions, cross-domain attempts, administrative actions and policy changes separately from Provenance and operational telemetry.

Only bounded material audit references enter canonical history when necessary for explanation/reproducibility.

Multi-domain deployments must prove isolation across control queries, data/state refs, candidate/checkpoint workspaces, dependency caches, runtime extension catalogs, history indexes, observability, secrets, scratch and provider correlation.

## Persistence impact plan

Future bounded canonical/reference state may include equivalents of:

```text
dependency requirement
dependency exact historical binding
egress plan
security profile reference
non-secret secret ref
security-domain/tenant reference
material authorization/audit decision ref
```

Detailed current authorization decisions, capability tokens, bearer credentials and broad security audit logs normally remain outside ordinary canonical resource tables.

No migration is created during Phase 005.

## Verification mapping

005-I primarily owns future V9 and directly maps:

```text
AF-02  portable/offline dependency isolation
AF-11  protected history/query paths honor authorization
AF-12  no hidden acquisition/remote fallback/telemetry
AF-14  provider fallback preserves semantics/security posture
AF-15  secrets excluded from canonical state/logs
AF-16  disclosure-state distinctions preserved
AF-17  exact/protected historical refs do not substitute current aliases
AF-18  dependency/security transition consistency survives retry/crash
```

Required future scenarios cover no-egress versus broad permission, denied network-required commitment, missing/wrong/untrusted/unauthorized dependencies, lazy extension trust, unsafe codec denial, non-bearer handles, Learned-State use/raw-export separation, candidate write/read separation, Evidence diagnostic protection, retry reauthorization, revocation plus fencing, secret leakage prevention, truthful redaction, protected reverse-query/count behavior, withheld reproducibility reasons, cross-domain isolation, fail-closed auth uncertainty and socket-denied offline execution.

## Future implementation sequence

Only after a later phase explicitly authorizes coding:

```text
I1  principal/security-domain/action/disclosure contracts
I2  dependency requirement/resolution/trust/exact-identity binding
I3  explicit acquisition/provisioning + local provider profile
I4  authorization request/decision ports and action vocabulary
I5  Attempt-scoped capability composition/runtime injection
I6  SecretRef/broker + extension/unsafe-codec trust seams
I7  EgressPlan/categories + offline/no-egress path
I8  control/data/history redaction and protected-query composition
I9  security audit + revocation/retry/fencing integration
I10 V9 conformance/failure/offline/security verification
```

None of I1-I10 is executed during Phase 005.

## Deferred ownership

005-I leaves concrete identity/IAM, policy engine, secret manager, private package/artifact distribution, network isolation, storage/catalog authorization, workload identity, audit sink, encryption and tenant platform mappings to 005-J.

005-K remains responsible for the final cross-slice/Jackson-methodology completeness audit.

## No upstream revision required

005-I requires no change to the eleven accepted concepts, fifteen synchronizations, Phase 003 experience contract, Phase 004 architecture/ADR set, or 005-C through 005-H implementation-planning authority.

No new architecture ADR is required.

## Exit criteria

- [x] planning-only/Jackson-methodology boundary preserved;
- [x] dependency resolution/trust/auth distinctions mapped;
- [x] exact dependency identity preserved;
- [x] explicit acquisition/no-hidden-download plan defined;
- [x] offline/no-egress defense-in-depth plan defined;
- [x] egress plan/current authorization separated;
- [x] action-oriented authorization defined;
- [x] Attempt-scoped capability composition defined;
- [x] non-bearer resource handle rule preserved;
- [x] secret broker/bearer-persistence prohibition defined;
- [x] extension/unsafe-codec trust-loading seam defined;
- [x] data/state/output/diagnostic access distinctions defined;
- [x] history/projection/index disclosure security defined;
- [x] redaction/existence-protection semantics defined;
- [x] reproducibility disclosure defined;
- [x] revocation/retry/fencing interaction defined;
- [x] security audit and tenant isolation mapped;
- [x] persistence/API/error impacts mapped;
- [x] V9/fitness obligations mapped;
- [x] future I1-I10 coding sequence defined without execution.

## Exit decision

**005-I — implementation plan complete; no production implementation performed.**

Next:

**005-J — Deployment/Platform Adapters, Observability, Compatibility, Scale & Performance Implementation Plan**.
