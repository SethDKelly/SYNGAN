---
type: Implementation Authority
title: Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan
status: active
---

# Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan

## Purpose

Define the concrete **future implementation plan** for SYNGAN's dependency-resolution, offline/no-egress, authorization, redaction, secret-delegation, security-audit, and enterprise isolation boundaries.

This document translates the accepted Phase 004-H security architecture into implementation-ready future roles that bind the durable control/data/runtime/recovery/history surfaces planned in 005-D through 005-H without turning security policy into a new SYNGAN domain concept.

**Phase 005 remains planning-only.** This plan does not create production source, authentication/authorization code, policy engines, secret-manager adapters, dependency repositories, firewalls, network controls, security tables, migrations, tests, CI workflows, or deployment infrastructure.

## Governing authority

005-I is downstream of:

- [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md);
- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](../architecture/dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md);
- [Network and External Dependency Policy](../authority/network-external-dependency-policy.md);
- [005-B Verification Strategy](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [005-C Source Topology](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md);
- [005-D Public Resource/Control-Plane Plan](public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md);
- [005-E Spark Data Boundary Plan](spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md);
- [005-F Runtime/SPI/Learned-State Plan](strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md);
- [005-G Execution/Recovery Plan](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-plan.md);
- [005-H Evidence/Provenance/History Plan](evaluation-evidence-provenance-historical-query-reproducibility-plan.md).

The governing implementation-planning rule is:

> **Future security enforcement SHALL preserve four separately inspectable boundaries: what a committed activity semantically requires, what the current environment can resolve and verify, what current policy authorizes, and what bounded capabilities the exact Attempt receives. Permission may block a valid commitment, but it may never silently broaden or reinterpret that commitment.**

## Planning-only and Jackson-methodology boundary

005-I SHALL NOT be interpreted as permission to begin production implementation.

Names such as `DependencyRequirementRef`, `DependencyResolution`, `AuthorizationDecision`, `CapabilityGrant`, `SecretRef`, and `DisclosureDecision` below identify accepted future implementation roles and intended contracts only.

Completion of 005-I means this slice's future implementation contract is specified. It does **not** mean the Jackson-style concept/design program is complete or that implementation should begin. 005-K remains responsible for an explicit methodology-completeness decision.

## Accepted future implementation choices

005-I accepts the following baseline:

- dependency declaration, dependency resolution, integrity/authenticity verification, trust/approval, activity compatibility, current authorization, and runtime capability issuance remain separate typed steps;
- `DependencyRequirementRef` and exact resolved dependency identities use the 005-D durable-reference/version model rather than mutable paths/tags as historical identity;
- dependency resolution is a port-driven application service; provider-specific registries, artifact stores, package indexes, model hubs, and catalogs remain adapters;
- runtime resolution never auto-installs packages, auto-downloads models, silently contacts public registries, or changes to hosted/remote fallback;
- an explicit provisioning/acquisition workflow may prepare dependencies before committed execution, but acquisition success does not imply trust, compatibility, or authorization;
- offline/no-egress is represented as an explicit deployment/activity security profile and is enforced through multiple seams rather than one Boolean or one firewall assumption;
- network connectivity, permitted destination, egress category, source/security domain, and action authorization remain separate values;
- a committed `EgressPlan` declares potential/required transmission semantics but is not itself permission to transmit;
- runtime receives only Attempt-scoped capability grants derived from `semantic requirement ∩ current authorization ∩ deployment capability`;
- durable resource handles remain identifiers and never bearer credentials;
- short-lived credential/secret material is resolved through a secret broker at use time and MUST NOT enter canonical resources, runtime invocation persistence, Provenance, Evidence, manifests, checkpoint metadata, or ordinary logs;
- runtime extension discovery/loading remains subject to current trust/authorization policy before third-party code is imported/executed;
- risky Learned-State codecs/deserializers declared by 005-F can be denied or confined by policy rather than normalized as trusted merely because the codec is installed;
- current authorization is re-evaluated for sensitive retry/resume/use/export/history actions after revocation or policy change;
- authorization failure does not rewrite historical commitments, Evidence, Provenance, Execution history, or prior promotion basis;
- cancellation/fencing from 005-G and authorization revocation remain complementary controls;
- control-plane resources, data-plane payloads, Evidence diagnostics, Provenance traversals, reverse indexes, counts, comparison output, and reproducibility explanations are all within the security boundary;
- redaction/withholding is performed as an authorized view transformation and never by mutating canonical history or replacing protected values with misleading `null`;
- disclosure preserves the distinction among absent, unknown/indeterminate, unavailable, withheld, redacted/authorized-summary, and invalid states;
- existence itself may be protected; the API must not always reveal that a resource/edge/count exists and then merely hide its fields;
- security audit is a separate subsystem from Provenance and telemetry; only material audit references are linked into Provenance/history when required;
- tenant/security-domain context is explicit in authorization/capability/query/cache/index keys and must not be inferred only from database placement;
- base/core SYNGAN remains usable with local/no-network implementations of these ports; no hosted IAM/policy/secret service becomes mandatory core semantics;
- 005-I selects no specific identity provider, RBAC/ABAC engine, OPA/Cedar policy engine, secret manager, KMS, DLP product, artifact-signing system, service mesh, firewall, Unity Catalog, cloud IAM, or tenant technology. Concrete mappings remain 005-J responsibility.

## Future package ownership

005-I refines the 005-C topology with future responsibilities equivalent to:

```text
src/syngan/
├── ports/
│   └── security/
│       ├── dependencies.py
│       ├── authorization.py
│       ├── capabilities.py
│       ├── secrets.py
│       ├── disclosure.py
│       ├── audit.py
│       └── trust.py
├── application/
│   └── security/
│       ├── resolve_dependency.py
│       ├── authorize_action.py
│       ├── compose_capabilities.py
│       ├── authorize_egress.py
│       ├── disclose.py
│       └── audit.py
├── api/
│   └── security_views.py
└── adapters/
    └── security/
        ├── local/
        ├── identity/
        ├── policy/
        ├── secrets/
        ├── artifacts/
        └── audit/
```

Exact leaf-file spelling may change during a later coding phase. The critical ownership rule is that application/core code depends on security/dependency **ports**, while enterprise/vendor security systems remain adapters.

No generic `SecurityContext` or service locator may absorb all policy, dependency, identity, secret, capability, and disclosure semantics.

## Security/domain boundary

005-I does not introduce a new domain concept for:

```text
Security
Policy
Authorization
Authentication
Principal
Role
Permission
Capability
Dependency Resolution
Trust
Approval
Egress
Secret
Credential
Redaction
Tenant
Security Domain
Audit Event
```

These remain cross-cutting implementation/integration mechanisms around the accepted concepts.

The domain/application layer may use typed security decisions to decide whether an operation may currently proceed, but security policy does not acquire ownership over Learning, Generation, Evaluation, Evidence, Execution, Provenance, or another concept's lifecycle meaning.

## Principal and security-domain plan

### `PrincipalRef`

Future authorization calls use a bounded verified principal reference supplied by trusted deployment/identity infrastructure.

It must be capable of representing at least:

- interactive human/user identity;
- service/workload identity;
- delegated service action tied to a parent activity/Attempt;
- tenant/security-domain/environment context.

A runtime plugin's self-asserted user identifier is not trusted authentication evidence.

### Security-domain context

Every security-sensitive action carries an explicit security-domain/tenant context where the deployment requires isolation.

Global ResourceId uniqueness does not grant cross-domain resolution or access.

Caches, projections, dependency caches, extension catalogs, materialized history indexes, and result memoization must include the relevant security-domain boundary in their key/partitioning policy whenever cross-domain reuse would otherwise leak information.

### Authentication boundary

Authentication/proof of identity is supplied by trusted platform infrastructure and adapted into `PrincipalRef`/verified request context.

SYNGAN's core does not implement password/OIDC/SAML/Kerberos/etc. semantics as domain behavior.

## Dependency requirement plan

### `DependencyRequirementRef`

005-I reserves a future durable/referenceable requirement role using the 005-D identity model where a stable requirement must be bound historically.

A requirement descriptor contains bounded facts equivalent to:

```text
requirement ref / role
required exact identity or explicitly allowed compatible range
representation/version constraints
expected integrity/authenticity basis
allowed resolver/provider classes
acquisition-vs-runtime timing
network profile
egress categories possibly involved
portability/reproducibility requirements
implementation binding / Learned-State / method role
```

A requirement may be embedded in/referenced by Strategy implementation bindings, Evaluation-method bindings, Learned-State representations, or activity commitments as appropriate.

### Mutable locators are not exact dependency identity

Values such as:

```text
models/latest
pypi:package-name
registry:stable
https://host/current-model
```

are locators unless the provider supplies an immutable identity/version contract strong enough for the exact historical requirement.

The future implementation must retain both locator/provider information and exact resolved identity when they differ.

## Dependency resolution plan

### `DependencyResolution`

A future resolution result is a contextual typed value, not a domain resource by default.

It preserves enough independent axes equivalent to:

```text
requirement ref
resolved exact dependency ref / identity
locator/provider
availability
identity match
integrity/authenticity verification
trust/approval
runtime/activity compatibility
current authorization
acquisition state
network/egress requirements
limitations
```

The implementation must distinguish at least:

```text
missing
wrong_identity
integrity_unverified_or_failed
untrusted_or_unapproved
incompatible
unauthorized
resolved_permitted
indeterminate
```

These states may coexist across separate fields rather than one flat enum.

### Resolver port

A future `DependencyResolver`/equivalent port may:

- locate an exact dependency from approved providers;
- resolve immutable provider identity;
- report availability;
- fetch bounded metadata needed for verification;
- expose whether acquisition would be required.

It does not decide enterprise trust or authorization merely because the artifact exists.

### Trust/integrity ports

Separate ports/results cover:

- byte/content integrity where applicable;
- signature/attestation/authenticity when available;
- organization-specific trust/approval;
- optional malware/SBOM/supply-chain decisions supplied by deployment integrations.

005-I plans the seam but does not mandate a signing/scanning technology.

## Explicit acquisition/provisioning plan

Dependency acquisition is a pre-runtime provisioning action, separate from committed Learning/Generation/Evaluation realization.

A future acquisition request/result records or resolves bounded facts equivalent to:

```text
requirement
source provider
expected identity/version
network requirement
data/config information transmitted during acquisition
local destination/security domain
integrity/authenticity result
approval/trust result
final exact dependency identity
```

Rules:

- missing runtime dependency produces an explicit resolution failure/readiness blocker;
- runtime plugin discovery/loading does not call package managers or public model hubs automatically;
- a local cache may satisfy a requirement only when exact identity/integrity/trust/authorization checks still pass;
- acquiring bytes does not automatically mark them usable;
- provisioning tools remain deployment/tooling concerns rather than runtime semantic fallback.

## Offline/no-egress profile plan

### Security profile

005-I plans an immutable/contextual deployment/activity security profile equivalent to:

```text
SecurityExecutionProfile
    network posture
    allowed dependency provider classes
    allowed destination classes
    egress-category policy refs
    secret-provider policy
    audit requirements
    runtime containment requirements
```

This is implementation/configuration state, not a domain concept or universal resource status.

At minimum the future implementation supports a first-class `offline_no_egress` profile for supported core structured/tabular workflows.

### Offline/no-egress readiness

For that profile, readiness requires that:

- required package/runtime components are already locally/private provisioned;
- all material dependencies resolve through approved local/private providers;
- selected runtime bindings do not require remote inference/service calls;
- telemetry/export does not require outbound connectivity;
- runtime can be launched without ambient outbound network authority;
- required secrets/credentials can be supplied without external public acquisition;
- deployment enforcement can satisfy the declared containment strength.

The profile is not satisfied merely because the machine happens to have no current Internet route.

### Defense-in-depth seams

Future enforcement occurs at multiple levels:

```text
commit/readiness compatibility
        ↓
dependency resolver/provider selection
        ↓
authorization decision
        ↓
Attempt capability composition
        ↓
data/dependency/network/secret ports
        ↓
deployment network/sandbox enforcement (005-J)
        ↓
security audit/monitoring
```

A later deployment adapter must report when it cannot enforce a promised no-egress/no-network constraint strongly enough.

## Egress model

### `EgressCategory`

The future implementation preserves typed categories equivalent to:

```text
network_no_content
non_sensitive_metadata
source_derived
source_records
generated_records
```

Deployments may refine these, but core security logic cannot collapse policy-relevant categories into one `network_allowed` Boolean.

### `EgressPlan`

A committed/runtime binding may resolve an immutable egress plan containing bounded facts equivalent to:

```text
destination/provider exact identity or approved class
service/action/protocol role
egress category
source/security-domain context
transformation/aggregation boundary when relevant
purpose/runtime role
expected direction
committed network posture
```

The plan declares what the selected implementation may require. It is not an authorization grant.

### Egress authorization

Immediately before a material outbound action, the framework/runtime capability layer evaluates the exact action against:

- committed EgressPlan;
- current principal/service identity;
- current policy;
- current destination identity;
- data/egress category;
- deployment capability.

A protected action with indeterminate/unavailable authorization fails closed unless an explicit still-valid cached/leased policy mechanism accepted by the deployment governs the case.

005-I does not define that cache/lease TTL; 005-J may map it to platform policy capabilities.

### No silent egress-plan widening

If runtime attempts undeclared outbound behavior, the implementation must block/report it where enforceable.

If the behavior is actually required for execution, the current implementation binding/activity is incompatible; the system must not mutate the commitment or EgressPlan in place.

## Authorization action model

### `SecurityAction`

005-I plans a stable namespaced action vocabulary rather than one `can_access(resource)` permission.

Initial action families must cover equivalents of:

```text
spec.create / spec.edit / activity.commit
execution.start / retry / resume / cancel
dependency.resolve / use / acquire
source.read
learned_state.use / inspect / raw_read / export
candidate.write / checkpoint.write / diagnostic.write
control.inspect
output.read / output.export
evidence.read / evidence.diagnostic_read
history.traverse / compare / reproducibility
provenance.correct
resource.restrict / retire / invalidate
security.admin / audit.read
network.call / egress.transmit
secret.resolve
```

Exact stable spelling becomes a compatibility contract when implemented.

The action model must permit an actor to inspect a safe Generation summary without automatically granting source-row access, Learned-State raw payload access, output export, sensitive diagnostics, or full reverse Provenance traversal.

### `AuthorizationRequest`

A future request carries bounded exact context equivalent to:

```text
principal/service/delegation refs
action
exact ResourceRef/HistoricalRef/target
security domain / tenant
data/egress category when material
destination/provider when material
activity/Execution/Attempt context when material
current policy context references
```

### `AuthorizationDecision`

A decision preserves at least:

```text
permit
deny
indeterminate
permit_with_conditions
```

plus bounded reason/policy-decision references safe for the caller's disclosure context.

The decision is contextual/current state and is not a new lifecycle state on the target resource.

## Commit-time versus use-time authorization

A successful commit authorization does not mint permanent future access.

Sensitive operations are re-authorized at use time, especially:

- source reads;
- dependency/Learned-State loading;
- unsafe codec/deserializer execution;
- runtime network/egress;
- retry/resume after policy change;
- result/diagnostic read or export;
- Provenance/history traversal;
- reproducibility prerequisite disclosure;
- provenance correction/administrative action.

If permission changes after commitment:

```text
historical commitment unchanged
current action denied/blocked
no substitute source/dependency/path
```

This distinction must be visible in Execution/readiness/history rather than rewritten into semantic compatibility.

## Attempt-scoped capability delegation

### `CapabilityGrant`

A future capability grant is a short-lived operational authorization artifact scoped to one principal/service context and normally one Execution/Attempt.

It may authorize exact operations such as:

```text
read SourceStateRef S7
read LearnedStateRepresentationRef LS9/R2
read dependency D3
write Attempt-local candidate C8
commit checkpoint CP-family under WriterFence F11
use approved remote client R4 for aggregate-only egress
resolve SecretRef K6
emit bounded progress events
```

The capability grant is not canonical historical domain state and is not a bearer value stored in ordinary resource objects.

### Composition rule

The future composer computes no broader than:

```text
required runtime capability
∩ current authorization
∩ deployment capability
```

A user having broad network permission does not enlarge an offline/no-egress commitment.

A committed network requirement does not create permission if current policy denies it.

### Runtime port injection

005-F runtime port bundles are completed by 005-I with narrow capabilities/services such as:

- authorized exact data reader;
- authorized dependency reader;
- fenced candidate/checkpoint/diagnostic writer;
- approved remote-method client;
- secret-resolution facade;
- progress/audit emitter.

Runtime adapters do not receive generic database credentials, unrestricted network clients, or broad canonical repositories.

## Secret and credential plan

### `SecretRef`

Canonical/runtime planning state may contain only a non-secret reference such as:

```text
SecretRef
    provider kind
    secret logical name/ref
    intended service/role
    security domain
```

where disclosure of even the logical ref is itself authorized.

### Secret broker

A future `SecretBroker`/equivalent port:

1. authorizes `secret.resolve` for the exact Attempt/service role;
2. resolves the non-secret `SecretRef` through the configured provider;
3. returns a short-lived/in-memory credential/capability to the consuming adapter;
4. prevents ordinary logging/persistence of the bearer value;
5. allows provider rotation without rewriting semantic commitments when effective dependency/service identity is unchanged.

### Persistence prohibition

Bearer values MUST NOT be persisted in:

- commitments;
- RuntimeInvocationRef payloads;
- ResourceHandle values;
- ProvenanceAssertions;
- EvidenceFindings;
- manifests/component indexes;
- Checkpoint descriptors;
- operation idempotency records;
- ordinary logs/traces;
- extension binding records.

A leaked secret is a security incident/audit concern, not a Provenance correction event.

## Runtime extension/code-loading security

005-F entry-point or explicit extension providers are executable third-party code and therefore participate in trust policy.

Future loading sequence is equivalent to:

```text
discover metadata
    ↓
resolve exact package/build identity
    ↓
verify integrity/trust/approval
    ↓
authorize loading in current security domain
    ↓
import/instantiate provider
```

Metadata enumeration does not imply permission to import code.

Unsafe codecs/state representations must similarly declare code-execution/deserialization risk and may require explicit trust/authorization before loading.

The implementation must be able to report `installed but unauthorized/untrusted` distinctly from `not installed` and `incompatible`.

## Data-plane access plan

### Source/reference reads

A runtime receives an exact authorized reader scoped to the committed `SourceStateRef`/reference rather than a generic catalog credential where practical.

Underlying row/column/object-storage policies may be delegated to the platform, but the SYNGAN capability/request still binds the exact intended resource/action.

### Learned-State access

Security distinguishes at least:

```text
use/load through runtime
inspect bounded metadata
read raw state payload
export state
```

Permission to generate using a Learned State does not automatically grant raw parameter/file download.

### Candidate/output access

Permission to write an Attempt-local Generation candidate does not imply permission to read/export it.

Generation semantic completion does not imply output export permission.

### Diagnostics

Permission to read an Evidence finding summary does not automatically grant access to exact diagnostic snapshots, source-derived examples, attack traces, or other protected supporting data.

Checkpoints/intermediates inherit relevant sensitivity and are not presumed safe merely because they are operational artifacts.

## Control-plane and historical-query security

Bounded control records may still expose sensitive facts such as:

- source/dependency identities;
- tenant/security-domain membership;
- implementation binding;
- activity existence;
- Evidence result;
- Provenance neighborhood/graph shape;
- failed/denied operations;
- reproducibility prerequisites.

Security therefore applies to control metadata, not only bulk data.

### Canonical history access

005-H query composition must authorize the target and each material disclosure category required to render the answer.

A request to explain one output may require distinct decisions for:

- target existence/summary;
- incoming/outgoing Provenance edges;
- neighboring resource existence;
- neighbor fields;
- Execution/recovery details;
- Evidence details;
- diagnostic links;
- dependency identities;
- current availability/reproducibility reasons.

### Projection/index access

Derived indexes are inside the security boundary.

A protected canonical resource cannot be leaked through:

```text
reverse lookup
adjacency list
count
pagination total
autocomplete/search hit
comparison field
reproducibility reason
cache key
error message
query timing where material
```

005-I plans a `SecurityFilteredHistoryQuery`/equivalent composition seam where authorization is applied before or during traversal/projection assembly, not as a superficial final string-redaction pass.

Concrete strategies—security-partitioned indexes, query predicates, protected materialized views, post-filtering with side-channel controls—remain 005-J/provider implementation choices.

## Disclosure/redaction plan

### `DisclosureState`

Future response/view logic must preserve at least:

```text
resolved
absent
unknown_or_indeterminate
unavailable
withheld
redacted_or_authorized_summary
invalid
```

005-H's corrected/superseded historical status remains a separate historical assertion/property rather than disclosure state.

### Existence protection

If policy permits saying that a resource/edge exists but hides its content, the view may return `withheld`/authorized summary.

If existence itself is protected, the implementation must not leak a distinct "exists but forbidden" response to unauthorized callers.

The exact indistinguishability/error strategy is deployment/security-policy dependent, but APIs must provide enough structured internal state to implement it without corrupting canonical truth.

### Redaction is view-time transformation

Redaction never mutates canonical Evidence, Provenance, commitment, or resource fields.

The disclosure layer may:

- omit protected fields;
- return an authorized summary;
- replace a value with an explicit redacted marker where existence disclosure is allowed;
- withhold an entire relationship/path;
- suppress counts/totals where necessary.

It MUST NOT fabricate a false value or convert protected-but-existing data to semantic `absent`.

## Reproducibility disclosure plan

005-H separates historical support class from current feasibility. 005-I adds disclosure rules around the prerequisite/reason graph.

A user may be authorized to learn:

```text
historical support: statistical
current feasibility: blocked
```

without being authorized to learn the exact secret dependency or source responsible.

The future `ReproducibilityAssessment` view therefore supports reason entries with disclosure forms equivalent to:

```text
full reason
policy-safe category/summary
withheld reason
```

and must not infer `absent` because a prerequisite is hidden.

## Retry/resume/revocation integration

005-G same-commitment retry/resume retains semantic bindings but does not retain eternal authorization.

Before a new Attempt or sensitive resumed action, future application logic re-evaluates as applicable:

- principal/service authorization;
- source read permission;
- Learned-State use/load permission;
- dependency trust/approval/authorization;
- secret availability;
- network/egress permission;
- checkpoint access;
- candidate/output/diagnostic target permission;
- extension/code-loading trust;
- history/Provenance write authorization.

A valid checkpoint may therefore be semantically resumable but currently blocked by security policy.

### Revocation plus fencing

Authorization revocation and 005-G fencing solve different problems:

```text
revocation
→ stop granting/renewing protected capabilities
→ request provider/runtime cancellation where possible

fencing
→ reject stale framework-owned mutation even if old process continues
```

A conforming implementation uses both where necessary.

A later authorization grant cannot resurrect an already-cancelled/fenced Attempt's old mutation authority; continuation follows ordinary 005-G recovery rules.

## Authorization-service uncertainty

If a protected action requires current authorization and the policy/identity service is unavailable or returns indeterminate, the default planned behavior is fail closed.

Deployments may later support explicitly governed cached/leased decisions where organizational policy permits, but the cache must preserve:

- decision identity/version;
- scope/action/resource;
- validity/expiry;
- security domain;
- material conditions.

005-I does not mandate cached authorization and no core flow relies on it.

## Security audit plan

### Audit versus Provenance versus telemetry

The future implementation keeps three channels separate:

```text
Provenance
    material derivation / binding / realization relationships

Security audit
    allowed/denied sensitive actions and policy/security events

Telemetry
    operational diagnostics / metrics / traces
```

A security audit record does not become Provenance merely because it names a resource, and a telemetry log cannot authorize an action.

### `SecurityAuditSink`

A future audit port accepts bounded structured events for material actions such as:

- authorization decision used for high-consequence action;
- denied source/dependency/Learned-State/output/diagnostic/history access;
- dependency approval/trust failure;
- secret resolution;
- egress permit/deny/block;
- cross-domain access attempt;
- security administration/provenance correction;
- policy change affecting retry/resume;
- undeclared egress/runtime behavior.

Audit retention/immutability technology and whether a particular action requires synchronous audit durability remain enterprise/deployment policy decisions for 005-J.

### Material audit references in history

Where a material transition's defensibility requires a policy/audit decision reference, Provenance/history may retain a bounded non-secret reference to that decision.

It does not copy full access logs into canonical Provenance.

## Multi-tenant and isolation plan

Every deployment supporting multiple security domains/tenants must prove isolation across:

- control-store queries;
- source/output/state references;
- candidate/checkpoint workspaces;
- dependency/artifact caches;
- runtime extension catalogs;
- projections/history indexes;
- observability labels/logs;
- secret resolution;
- temporary scratch;
- provider correlation/search.

Cross-domain deduplication/cache reuse is permitted only when policy explicitly allows it and exact content/trust/retention implications are understood.

A shared database or object store does not by itself mean resources are mutually visible.

## Persistence impact plan

Future bounded control responsibilities may include equivalents of:

```text
dependency_requirement
dependency_resolution_reference / historical binding
egress_plan
security_profile reference
non-secret secret_ref
material authorization/audit decision reference
security-domain/tenant reference on protected resources
```

Most current authorization decisions, short-lived capabilities, bearer credentials, and detailed security audit events should **not** live in ordinary canonical resource tables.

Where historical reproducibility or material transition audit requires preserving a security/dependency fact, persist only the bounded non-secret identity/reference necessary for that purpose.

No SQL schema or migration is created during Phase 005.

## API and error-surface plan

Future APIs must distinguish security/dependency failures from semantic incompatibility and ordinary absence.

Structured error/problem families should preserve equivalents of:

```text
DependencyMissing
DependencyIdentityMismatch
DependencyIntegrityFailure
DependencyUntrusted
DependencyIncompatible
DependencyUnauthorized
NetworkProhibited
EgressProhibited
AuthorizationDenied
AuthorizationIndeterminate
SecretUnavailable
SecretDenied
SourceReadDenied
LearnedStateUseDenied
OutputAccessDenied
HistoryDisclosureWithheld
CrossDomainAccessDenied
UndeclaredEgressAttempt
SecurityEnforcementInsufficient
```

Errors shown to callers are disclosure-filtered; internal operational/audit records may retain more detail when authorized.

No error code may reveal protected resource existence merely for diagnostic convenience when existence itself is confidential.

## Verification mapping

005-I primarily owns future **V9 — dependency/security/offline/no-egress/disclosure verification** and materially contributes to V2/V3/V7/V8/V10/V11.

The future slice directly maps to:

```text
AF-02  portable/offline dependency isolation
AF-11  protected history/query paths honor authorization
AF-12  no hidden acquisition/remote fallback/telemetry
AF-14  provider fallback preserves semantics/security posture
AF-15  secrets excluded from canonical state/logs
AF-16  disclosure-state distinctions preserved
AF-17  protected historical refs never resolve through latest/substitution
AF-18  security/dependency transition consistency survives crash/retry
```

It also reinforces AF-07/09/10/20 where fencing, semantic completion, projections, and platform identities intersect security.

### Required future deterministic/contract scenarios

At minimum:

- permission broader than committed no-egress posture does not create network capability;
- committed network requirement plus current deny produces blocked execution, not silent fallback;
- dependency exists but is wrong identity;
- dependency identity is valid but untrusted;
- trusted dependency is currently unauthorized;
- missing dependency never triggers auto-download;
- extension entry point exists but cannot be imported before trust/authorization;
- unsafe StateCodec is denied in a restrictive profile;
- handle possession without authorization cannot read resource;
- Learned-State `use` does not imply raw payload/export;
- candidate write does not imply candidate read/export;
- Evidence summary does not imply diagnostic access;
- retry/resume re-authorizes after policy change;
- revocation stops new capability issuance while stale writer remains fenced;
- secret bearer values never enter serialized invocation/history/logs;
- redaction preserves existing-versus-absent semantics correctly;
- unauthorized explain/reverse lookup cannot reveal protected neighbors/counts;
- reproducibility reason may be withheld without changing support/feasibility classification;
- cross-domain cache/index resolution is rejected;
- auth-service indeterminate fails closed for protected action;
- offline profile completes supported core verification with outbound sockets denied.

### Future integration/security scenarios

- local/private dependency provider satisfies offline profile with no public registry calls;
- platform-backed identity maps verified human/service/delegated principals correctly;
- secret broker supplies short-lived credential only to the intended Attempt/service;
- network/egress containment blocks undeclared destination even when runtime library attempts it;
- security audit records denied/allowed material actions without becoming Provenance;
- query projection/index security matches canonical-resource disclosure decisions;
- tenant isolation holds across control/data/history/cache boundaries.

## Future implementation sequence

Only after a later phase explicitly authorizes coding:

```text
I1  principal/security-domain/action/disclosure value contracts
I2  dependency requirement/resolution/trust ports and exact-identity binding
I3  explicit acquisition/provisioning interfaces and local provider profile
I4  authorization request/decision ports + action vocabulary
I5  Attempt-scoped capability composition and runtime-port injection
I6  SecretRef/broker and unsafe-codec/extension-loading policy seams
I7  egress plan/categories + offline/no-egress enforcement path
I8  control/data/history redaction and protected-query composition
I9  security audit + revocation/retry/fencing integration
I10 V9 conformance/failure/security/offline verification profiles
```

None of I1-I10 is executed during Phase 005.

## Deferred ownership

005-I leaves to:

- 005-J — concrete platform identity/IAM, secret manager, private artifact/package distribution, network isolation/firewall, storage/catalog authorization, workload identity, policy-engine, audit sink, encryption and tenant-isolation mappings;
- 005-J — compatibility/support declaration when a platform cannot strongly enforce an offline/no-egress/sandbox requirement;
- 005-K — cross-slice security/dependency ordering, backlog closure and Jackson-methodology completeness audit;
- later explicit implementation authority — actual production code, configuration and infrastructure.

## No upstream revision required

005-I requires no change to the eleven accepted concepts, fifteen synchronizations, Phase 003 experience contract, Phase 004 architecture/ADR set, or 005-C through 005-H implementation-planning authority.

No new architecture ADR is required.

## Exit criteria

- [x] planning-only/Jackson-methodology boundary preserved;
- [x] dependency requirement/resolution/trust/authorization distinctions mapped;
- [x] mutable locator versus exact dependency identity rule preserved;
- [x] explicit acquisition/no-hidden-download plan defined;
- [x] offline/no-egress profile and defense-in-depth seams defined;
- [x] egress categories/plan/current authorization separated;
- [x] action-oriented authorization request/decision model defined;
- [x] commit-time versus use-time authorization separated;
- [x] Attempt-scoped capability composition defined;
- [x] resource handles kept non-bearer;
- [x] SecretRef/broker and bearer-persistence prohibition defined;
- [x] extension/unsafe-codec trust-loading seam defined;
- [x] source/Learned-State/candidate/output/diagnostic access distinctions defined;
- [x] canonical history + projection/index disclosure security defined;
- [x] redaction/withholding/existence-protection semantics defined;
- [x] reproducibility disclosure seam defined;
- [x] revocation/retry/fencing interaction defined;
- [x] security audit separated from Provenance/telemetry;
- [x] tenant/security-domain isolation obligations defined;
- [x] persistence/API/error impacts mapped;
- [x] V9/fitness obligations mapped;
- [x] future I1-I10 coding sequence defined without execution.

## Exit decision

**005-I — implementation plan complete; no production implementation performed.**

Next:

**005-J — Deployment/Platform Adapters, Observability, Compatibility, Scale & Performance Implementation Plan**.
