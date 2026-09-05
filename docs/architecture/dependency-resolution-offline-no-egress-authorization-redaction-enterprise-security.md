---
type: Architecture Authority
title: Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture
status: active
---

# Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture

## Purpose

Define the enterprise security architecture by which SYNGAN resolves and verifies dependencies, preserves an offline/no-egress core, authorizes actor and service actions, delegates only bounded runtime capabilities, protects sensitive source-derived state, redacts or withholds protected details truthfully, prevents query/index leakage, and records enough security-relevant history for audit and reproducibility without turning security policy into a new domain concept or allowing authorization machinery to rewrite canonical semantic history.

This document establishes the canonical Phase 004-H architecture downstream of the accepted Network and External Dependency Policy, Phase 003 enterprise-safety experience, and the Phase 004 identity, data-plane, runtime, Execution, Evidence, Provenance, and historical-query architecture.

It defines:

- dependency declaration, discovery, resolution, verification, trust and permission boundaries;
- acquisition-time versus runtime-network behavior;
- offline/no-egress runtime composition;
- action-oriented authorization contracts;
- principal/service/delegation boundaries;
- scoped data/dependency/network/secret capabilities;
- egress-plan representation and enforcement;
- sensitive control-plane/data-plane access;
- redaction, withholding and non-disclosure semantics;
- historical-query/projection authorization;
- secret/credential handling;
- revocation, retry/recovery and policy-change interaction;
- security/audit history and Provenance boundaries;
- multi-security-domain and tenant-isolation obligations.

It does **not** select RBAC versus ABAC, OPA/Cedar, IAM provider, Unity Catalog, cloud KMS, secret manager, service mesh, network firewall, DLP engine, artifact repository, package-signing system, encryption product, identity provider, or deployment topology.

## Governing authority

This architecture remains downstream of:

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md);
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](public-api-resource-handle-workflow-semantic-mapping.md);
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md);
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md);
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](strategy-extension-learning-generation-evaluation-runtime-adapter.md);
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md);
- [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](evaluation-evidence-provenance-reproducibility-historical-query.md);
- [Network and External Dependency Policy](../authority/network-external-dependency-policy.md);
- [Enterprise Dependency, Offline/No-Egress & Safety Experience](../experience/enterprise-dependency-offline-no-egress-safety.md);
- [Reproducibility Contract](../authority/reproducibility-contract.md);
- accepted concept ownership and [Core Synchronizations](../synchronizations/core-synchronizations.md).

## Primary decision

SYNGAN SHALL separate **semantic/dependency declaration**, **environmental resolution**, **current authorization**, and **runtime capability**.

Conceptually:

```text
Strategy / method / activity commitment
required dependency + network + egress semantics
                     ↓
Dependency resolution
exact identity / availability / integrity / compatibility
                     ↓
Authorization / policy decision
principal + action + resource + environment + data/egress context
                     ↓
Scoped runtime capabilities
exact data reads / dependency reads / writes / network / secrets
                     ↓
Execution / Attempt
runtime adapter receives only approved capabilities
                     ↓
material security / dependency facts
Provenance + security audit as applicable
```

These responsibilities MUST NOT collapse into one `allowed=true` or `secure=true` value.

The architecture adopts the following governing rule:

> **Committed dependency/network/egress semantics define what an activity is allowed to mean; current authorization determines whether a particular actor/service may perform an action now; runtime receives only the bounded capabilities needed to realize both.**

A later authorization grant MUST NOT silently broaden a committed no-network/no-egress activity. A later revocation MAY block future access, retry, continuation, or another action without rewriting the historical commitment.

## Security authority boundary

### Security policy is external/cross-cutting authority

SYNGAN consumes authorization, trust, classification and deployment-policy decisions, but Phase 004-H does not introduce a standalone `Security`, `Policy`, `Authorization`, `Artifact Approval`, `Data Classification`, `Trust`, or `Egress` domain concept.

External enterprise authority may determine:

- who may create/inspect/operate on a resource;
- which source or output may be read;
- whether a Learned State may be loaded/exported;
- which dependencies may be used;
- whether package/artifact acquisition is permitted;
- whether outbound network communication is permitted;
- which categories of information may cross a boundary;
- which destinations/providers are allowed;
- which diagnostic/Provenance details may be disclosed;
- which operator actions are permitted.

SYNGAN preserves the result/context required to enforce and explain these decisions without taking ownership of the organization's policy itself.

### Policy decisions do not redefine semantic compatibility

For example:

```text
Strategy semantic compatibility: compatible
Dependency identity: verified
Current enterprise permission: denied
```

is valid.

Likewise:

```text
Current permission: granted
Strategy incompatible with committed no-egress posture
```

remains incompatible.

Permission does not make an incompatible Strategy semantically compatible, and compatibility does not imply permission.

## Dependency requirement and resolution architecture

### Required dependency descriptor

A Strategy implementation binding, Evaluation method binding, Learned State representation or committed activity may reference a dependency requirement containing or resolving enough information equivalent to:

```text
dependency requirement identity
semantic/runtime role
required identity constraints
compatible representation/version range where explicitly allowed
expected integrity/authenticity basis
resolver kind / allowed source classes
network profile
possible egress behavior
runtime/acquisition timing
material portability/reproducibility requirements
```

The descriptor is architecture/integration state and does not become a domain concept.

### Resolution is separate from requirement

Dependency resolution answers which actual dependency instance, if any, satisfies the requirement in the current environment.

A resolution record/view SHOULD preserve distinctions equivalent to:

- required identity;
- resolved concrete identity;
- locator/provider;
- current availability;
- integrity/authenticity verification state;
- semantic/runtime compatibility;
- trust/approval decision reference where applicable;
- acquisition state;
- network profile actually required;
- current authorization result;
- limitations/indeterminacy.

The following are different states:

```text
missing
found but wrong identity
found and identity verified but unapproved
found and approved but incompatible runtime
found and compatible but current actor unauthorized
resolved and permitted
indeterminate
```

### Mutable locator never substitutes for exact identity

A path, URI, registry tag, package name, endpoint or model alias is a locator unless the provider contract itself establishes immutable identity strongly enough for the required historical/reproducibility semantics.

For example:

```text
models/latest
```

cannot silently satisfy a commitment to artifact `B3/H7` merely because it currently resolves to a usable file.

### Resolver does not own trust or authorization

A dependency resolver may discover and verify an artifact. Discovery does not imply approval.

Conceptually:

```text
resolver: B3/H7 exists here
integrity verifier: bytes match H7
trust authority: H7 is approved for this environment/purpose
activity compatibility: this exact B3 can realize the commitment
authorization: this service/actor may use it now
```

A future implementation may combine calls for efficiency, but the semantic distinctions remain inspectable.

## Artifact/package acquisition architecture

### Acquisition is explicit provisioning activity

If a dependency must be acquired, acquisition is distinct from Learning/Generation/Evaluation runtime realization.

A compliant acquisition flow preserves enough information equivalent to:

```text
required dependency
source/provider
expected identity/version
network requirement
information sent during acquisition
local destination/security domain
integrity/authenticity verification
approval/trust result
availability after provisioning
```

### No hidden acquisition

A runtime adapter, plugin loader or dependency resolver MUST NOT silently:

- download a model because a cache missed;
- install a package because an entry point is absent;
- contact a public model hub to identify an artifact;
- query a remote registry when the committed profile is local-only;
- switch to hosted inference because local execution failed;
- enable telemetry to complete dependency resolution.

An absent approved dependency produces an explicit resolution/readiness/operational failure according to lifecycle context.

### Acquired artifact is not trusted merely because acquisition succeeded

Downloaded/provisioned material MAY require integrity, authenticity, malware/supply-chain or organization-specific approval checks before becoming an eligible resolved dependency.

004-H requires a trust-verification port/result boundary but does not select signing, attestation, SBOM, scanning or repository technology.

### Package installation and runtime execution remain distinct

An installed extension package may be discoverable yet unauthorized for a particular source/security domain/activity.

Likewise a trusted implementation package does not make all dependencies or remote services it can access automatically trusted.

## Offline/no-egress composition

### Offline-capable core

Supported core structured/tabular workflows MUST remain composable so that, after package/runtime and explicitly approved local dependencies are provisioned:

- no outbound network capability is required;
- automatic dependency acquisition is disabled/absent;
- remote inference/service calls are unavailable;
- telemetry does not require external transmission;
- dependency resolution can use approved local providers;
- runtime adapters cannot obtain network authority merely because the host has connectivity.

### No-egress is stronger than no-network in semantic intent

A deployment may allow control/network connectivity while forbidding sensitive content egress.

Therefore architecture preserves separately:

```text
network connectivity capability
approved remote destination/service
egress category
source/security-domain context
payload/derivation category
authorization decision
```

A generic `network_enabled=true` is insufficient.

### Defense in depth

Offline/no-egress guarantees SHOULD be enforceable at multiple boundaries:

1. **pre-commit compatibility** — reject declared network/egress requirements incompatible with the selected activity profile;
2. **dependency resolution** — do not resolve through forbidden remote providers;
3. **runtime capability composition** — do not inject network/egress capability when not authorized;
4. **data/dependency ports** — allow only exact approved reads/writes/destinations;
5. **deployment enforcement** — network/sandbox/firewall/service-mesh/cloud controls SHOULD prevent bypass where practical;
6. **audit/monitoring** — undeclared/blocked access attempts remain diagnosable.

004-I will map these obligations to deployment/platform mechanisms.

## Egress architecture

### Egress categories remain typed

The architecture preserves at least the Phase 003 distinctions:

1. network activity without dataset/content egress;
2. non-sensitive metadata/configuration transfer;
3. source-derived information transfer;
4. source-record transfer;
5. generated-record transfer.

Additional enterprise classifications MAY refine these categories, but implementations MUST NOT collapse them into one Boolean when policy distinguishes them.

### Egress plan

A network-capable committed activity SHOULD carry or resolve an immutable egress plan sufficient to state, where material:

```text
destination/provider identity
action/protocol/service role
data/egress category
subject/source security domain
transformation/aggregation boundary if relevant
purpose/runtime role
expected direction
committed network profile
```

The plan declares what the activity may require. It does not itself authorize transmission.

### Egress decision

Before a material transmission, authorization evaluates the specific egress action against current policy and the committed plan.

A decision may be equivalent to:

- permit;
- deny;
- indeterminate/unavailable;
- permit under explicit bounded conditions.

An indeterminate decision for a protected transmission fails closed.

### Runtime egress capability

Runtime code SHOULD receive a framework-supplied outbound capability/client/sink scoped to approved destinations and data categories rather than unrestricted ambient network access where technically feasible.

For example:

```text
Evaluation adapter
   receives remote_method_client(destination=R7,
                                 egress=aggregate-summary-only)
```

rather than:

```text
Evaluation adapter
   inherits broad cloud credentials + unrestricted socket/network authority
```

A runtime/library that cannot be constrained at the process API level must be contained by deployment-level egress controls and its limitation reflected in compatibility/security review.

### Undeclared egress is an operational/security defect

If runtime attempts an outbound action not represented by the committed/declaration context, SYNGAN MUST NOT silently expand the egress plan.

The action is blocked where enforceable and reported as a policy/runtime defect. If the behavior is necessary to proceed, the current commitment is incompatible and a new explicit activity/implementation binding may be required.

## Authorization architecture

### Authorization is action-oriented

Authorization decisions SHALL be contextual to an action rather than represented as one global resource permission.

Relevant action classes include, where applicable:

- create/edit a draft specification;
- commit Learning/Generation/Evaluation;
- start/retry/resume/cancel Execution;
- resolve/use a dependency;
- read source/reference data;
- load Learned State payload;
- write candidate/checkpoint/diagnostic material;
- inspect semantic/control-plane metadata;
- read completed output payload;
- read sensitive Evidence diagnostics;
- traverse Provenance/historical queries;
- export/transmit source-derived/generated material;
- restrict/retire/invalidate resources where the canonical owner allows it;
- perform provenance correction;
- perform administrative/security operations.

A user who can inspect a Generation summary need not be able to read its source rows, Learned State, candidate output, diagnostics, or full Provenance.

### Principal and execution identity

Authorization context should support at least:

- human/user principal where an interactive actor initiates an action;
- service/workload principal used by SYNGAN control-plane/runtime components;
- delegated identity/capability connecting a service action to its authorized parent activity;
- security domain/tenant/environment context;
- resource identity/action;
- relevant policy attributes/classification references.

The exact identity-provider and token formats are deferred.

### Authentication is upstream infrastructure

004-H assumes principals can be authenticated by a trusted platform/identity layer. SYNGAN does not implement identity proof semantics as a domain concept.

Adapters receive verified principal/service context through ports; they MUST NOT trust self-asserted user IDs from arbitrary plugin/runtime payloads as authorization authority.

### Commit-time authorization and use-time authorization are different

An actor may be authorized to commit work at time T1. That permission does not create a permanent transferable right to all future actions.

Sensitive operations MAY require fresh authorization at execution/use time, particularly:

- reading source/reference data;
- resolving/loading restricted dependencies or Learned State;
- runtime network/egress;
- reading sensitive output/diagnostics;
- retry/resume after policy change;
- export/transmission;
- historical/query access.

The commitment preserves what was intended/allowed semantically; current authorization controls whether the action can occur now.

### Revocation does not rewrite history

If access is revoked after commitment:

```text
Generation G42 committed under no-egress profile
source read later revoked
```

G42 remains historically committed under its original semantics.

Current execution/retry may become blocked or fail according to its lifecycle because the required authorized action can no longer occur.

The system MUST NOT silently substitute another source, dependency or less-protected path to continue.

### Authorization decision reference/history

For security-sensitive material transitions, SYNGAN SHOULD preserve a bounded audit reference equivalent to:

```text
principal/service identity or audit-safe reference
action
resource/security domain
decision outcome
policy/authority decision identifier or version where available
time/context
material conditions
```

This may live in a security audit subsystem and be referenced from Provenance when materially needed. Provenance itself does not become a full access log.

## Capability delegation architecture

### Long-lived resource handles are not credentials

A public `GenerationHandle`, `LearnedStateHandle`, `EvidenceHandle`, output handle or Provenance reference identifies a resource. Possessing or serializing the handle MUST NOT by itself grant permission to read or mutate that resource.

A handle can outlive an authorization session. Operations re-authorize under current context.

### Runtime receives scoped capabilities

When Execution launches an Attempt, the control/application layer resolves the authorized capability set needed by the immutable runtime invocation.

Capabilities may cover:

- read exact source/reference snapshot;
- read exact Learned State/dependency components;
- write Attempt-local scratch;
- write current fenced candidate/checkpoint/diagnostic sink;
- call an approved remote dependency;
- retrieve a scoped secret/credential;
- emit bounded progress/health events.

A runtime implementation SHOULD NOT receive generic database credentials or broad repository access to canonical SYNGAN state.

### Delegation is bounded by semantic commitment and authorization

A delegated capability must be no broader than both:

1. what the committed activity/runtime invocation semantically requires; and
2. what current enterprise authorization permits.

Conceptually:

```text
runtime capability = semantic requirement ∩ current authorization ∩ deployment capability
```

A permission broader than the commitment does not enlarge the runtime capability.

### Capabilities are short-lived/non-canonical

Credential/token/capability values are operational security material, not semantic historical identity.

They SHOULD be short-lived, revocable where platform supports it, and excluded from ordinary resource serialization, logs, Evidence, Provenance and reproducibility payloads.

Historical state retains the dependency/service/authorization context needed for explanation, not bearer secrets.

## Data-plane authorization

### Source/reference reads

Data resolvers SHOULD open an exact source-state reference under a bounded delegated access context rather than give runtime plugins ambient catalog/storage credentials.

Authorization applies to the exact resource/security domain being read and MAY be independently enforced by the underlying storage/catalog platform.

### Learned State reads

Learned State may encode sensitive source-derived information. Authorization to generate using a Learned State need not imply permission to download/export its raw representation.

Architecture SHOULD permit different actions such as:

```text
use LS17 for approved Generation
inspect LS17 metadata
read/download LS17 payload
export LS17 outside security domain
```

with distinct authorization decisions.

### Candidate and completed output

Authorization to write a Generation candidate does not imply authorization to inspect/export candidate contents.

Likewise Generation semantic completion does not grant external release/export permission.

Completed output read/export MAY be independently governed by current external authority.

### Evaluation diagnostics

Evidence summary access and raw diagnostic access are separate operations.

A reviewer may be allowed to inspect:

```text
Evidence: elevated disclosure risk
```

without receiving nearest-neighbor/source examples that produced the finding.

### Checkpoints and intermediate state

Checkpoints, scratch state and partial candidate data inherit sensitivity from their source/activity context unless stronger classification is established explicitly.

Temporary status does not make them less sensitive.

## Control-plane authorization

Control-plane resources may themselves contain protected identities or relationships.

Access checks may apply independently to:

- commitment specifications;
- Data Meaning/Constraint/Strategy bindings;
- source/dependency identifiers;
- Execution/Attempt details;
- Evidence findings;
- Provenance relationships;
- historical comparisons;
- reproducibility assessments;
- current policy/security annotations.

A deployment MUST NOT assume that because control-plane payloads are small they are non-sensitive.

## Redaction and withholding architecture

### Truthful disclosure states

The architecture preserves the semantic difference among:

```text
ABSENT
UNKNOWN / INDETERMINATE
UNAVAILABLE
WITHHELD
REDACTED / AUTHORIZED SUMMARY
INVALID / INTEGRITY DEFECT
```

A serializer/API MUST NOT flatten these into ordinary `null` when the distinction affects interpretation.

### Withholding preserves existence only when authorized

Where policy allows disclosure that a relationship/resource exists but not its details, an authorized response may expose:

```text
source relationship: present
source identity: WITHHELD
```

However, even relationship existence may itself be sensitive. In those cases the response contract must avoid leaking existence/count information according to policy.

Therefore `WITHHELD` is not universally required to reveal that a secret exists; it is the correct semantic state **when existence itself is authorized to be disclosed**.

### Redaction is an authorized transformation

A redacted summary is not a fabricated replacement value. It must preserve the intended interpretation boundary.

For example:

```text
full diagnostic: 12 protected row examples
redacted view: violation count = 12; examples withheld
```

is legitimate when the summary is authorized and methodologically meaningful.

Replacing protected examples with synthetic invented examples and presenting them as if they were the originals would be false and is prohibited.

### Redaction is view-time, not history mutation

Canonical resource/Provenance history remains unchanged. Actor-specific serialization/query composition produces the permitted view.

A later actor with broader permission may resolve the same historical resource to more detail without creating a new domain revision.

## Historical query and projection security

### Security applies to derived projections too

004-G query indexes, adjacency caches, explain paths, dependency-usage indexes, comparison views and reproducibility caches are subject to the same disclosure rules as canonical state.

Protecting the canonical record while leaving a search index open is insufficient.

### Query authorization occurs before disclosure

A historical query service SHOULD evaluate authorization for:

- starting target;
- requested relationship types;
- candidate neighboring resources/edges;
- field-level details;
- aggregate/count results where existence is sensitive;
- diagnostic/platform drill-down links.

The exact execution strategy may use security-partitioned indexes, authorization-aware query predicates, post-resolution filtering with side-channel protections, or another mechanism. 004-H does not select one database/query technology.

### Derived indexes are not authorization authority

An index MAY cache security-domain/classification metadata for efficient filtering but cannot grant access merely because an entry is present.

Current authorization ultimately comes from the configured security authority and canonical resource/security context.

### Avoid inference through counts and graph shape

Unauthorized actors MUST NOT be able to infer protected resource/relationship existence simply through:

- total counts;
- pagination gaps;
- dependency reverse-lookups;
- timing/status differences where reasonably preventable;
- error message detail;
- comparison result shape;
- reproducibility limitation messages.

Exact side-channel defenses are deployment/implementation concerns, but public API semantics must allow non-disclosing responses.

### Reproducibility assessment under restricted context

The internal assessment service may know that a protected dependency exists while the requesting actor cannot see its identity.

The response may legitimately say, where policy permits:

```text
supported class: statistical
limiting dependency detail: WITHHELD
```

or may return a more opaque authorized summary.

The service MUST NOT reveal secret dependency/provider/source identities merely to explain reproducibility.

## Secrets and credentials

### Secret value is not dependency identity

API keys, passwords, tokens, certificates, private keys and cloud credentials are operational secrets. Their literal values MUST NOT be persisted in:

- commitment snapshots;
- runtime invocation specifications stored durably;
- Provenance;
- Evidence;
- manifests;
- checkpoint metadata;
- public handles;
- ordinary logs/diagnostics.

A durable record may preserve a secret **reference**, provider/credential class, intended service role, or rotation-safe identity where needed, but not the bearer value.

### Secret broker boundary

Runtime adapters requiring credentials SHOULD obtain them through a framework/platform secret-resolution capability scoped to the approved service/action.

Conceptually:

```text
runtime invocation
contains secret_ref = SR7
        ↓
authorized secret broker
        ↓
short-lived credential injected into Attempt
```

The runtime should not query arbitrary secret stores using broad operator credentials.

### Rotation normally does not change semantic identity

Rotating a credential that grants equivalent access to the same dependency/service does not by itself create a new Strategy or domain activity semantic revision.

If the credential change changes the effective provider/resource/behavior or permissions materially, compatibility/authorization must be reassessed.

### Secret leakage is a security incident, not Provenance

Security audit/incident systems may record credential misuse or leakage. Provenance should only retain security facts that materially explain domain derivation/reproducibility/policy review and must never copy the secret value.

## Runtime/plugin containment

### Plugin code is not automatically trusted with host authority

A Strategy/Evaluation implementation may be approved for execution yet should still receive only its declared/bounded runtime capabilities.

The architecture rejects an assumption equivalent to:

```text
plugin installed => plugin may inspect process environment,
all secrets, all sources, all output paths and unrestricted network
```

Where runtime technology makes complete process isolation impractical, the limitation becomes a deployment security consideration under 004-I and may narrow which environments approve the implementation binding.

### Runtime access through ports

Runtime adapters SHOULD use framework-supplied ports for:

- data reads;
- Learned State/dependency resolution;
- candidate/checkpoint/diagnostic writes;
- remote service calls;
- secret retrieval;
- progress reporting.

The architecture does not prohibit libraries from performing local computation directly. It constrains access to protected external/system capabilities.

### Platform-native identity is not authorization authority by itself

A Spark job, Databricks run, Kubernetes service account or cloud workload identity may carry delegated access, but the platform identifier alone does not prove that a SYNGAN action is semantically or organizationally authorized.

The Execution/Attempt and runtime invocation provide the SYNGAN context needed to issue the delegation.

## Retry/recovery security interaction

### Retry must revalidate current security conditions

A retry/resume preserves the committed domain semantics but may occur after:

- source permission revocation;
- dependency approval change;
- network policy change;
- credential rotation;
- Learned State restriction;
- destination/egress policy change.

Therefore automatic/manual recovery SHALL revalidate material current authorization/dependency/security conditions before issuing a new Attempt capability set.

### Security change does not permit semantic substitution

If B3 becomes forbidden during recovery, retry cannot silently use B4.

If remote service R7 becomes prohibited, retry cannot silently switch to local Strategy behavior unless the original committed Strategy/implementation contract explicitly treated that behavior as semantically equivalent and the actual committed binding permits it.

Otherwise the same Execution cannot continue and the domain workflow must decide whether new work is needed.

### Revocation and active Attempts

Where platform/security authority supports revocation, SYNGAN SHOULD revoke/expire delegated capabilities and request cancellation when an active operation is no longer authorized.

Because revocation is not guaranteed to stop physical work immediately, 004-F fencing still protects framework-owned canonical state.

Security revocation and Attempt fencing are complementary:

```text
authorization revocation
    limits future protected access
Attempt fence
    prevents stale canonical writes
```

### Unknown policy state fails closed for protected actions

If a required authorization service is unavailable and no valid cached/leased decision policy applies, sensitive read/write/egress operations remain blocked/indeterminate rather than assuming permission.

Exact safe caching/decision-TTL rules are deployment/security-policy choices.

## Promotion and security

### Semantic completion does not equal export authorization

Learning may establish Learned State, Generation may promote completed output, and Evaluation may establish Evidence when their semantic contracts are met.

Those transitions do not by themselves authorize external release or unrestricted reading.

### Security may gate ability to complete when required operation is protected

If Generation completion requires Evaluation over a candidate but the current service is no longer authorized to read the candidate, Generation remains pending/fails according to existing semantic/operational rules. Security does not manufacture favorable Evidence to allow promotion.

### Promotion itself requires authorized mutation

The service performing owner-side promotion/establishment must be authorized to mutate the canonical owner and related required Provenance under the current execution/security context.

A runtime plugin cannot bypass this through direct storage writes.

## Multi-domain and tenant isolation

### Security-domain context is explicit

Stable logical resource IDs may be namespace-capable under 004-C. Security-sensitive operations additionally require enough context to prevent accidental cross-domain resolution.

An exact reference SHOULD resolve within an explicit authority/security-domain/tenant context when the deployment supports multiple domains.

### Cross-domain access is not implied by globally unique identity

A globally unique ID does not imply that a principal in another tenant/security domain may resolve it.

Similarly, a shared physical object store/database does not collapse isolation boundaries.

### Caches and indexes must preserve isolation

Dependency caches, query indexes, artifact caches, runtime caches and materialized read models MUST avoid serving protected material across security domains merely because the content/locator appears identical.

Deduplication across domains is allowed only when the underlying security/trust/retention contract explicitly supports it.

## Security audit and Provenance boundary

### Security audit is broader than Provenance

Security-relevant audit may include:

- successful/denied sensitive reads;
- dependency approval decisions;
- egress requests/denials;
- privileged administrative actions;
- secret access events;
- security-policy failures;
- cross-domain access attempts.

Most of these are not automatically canonical Provenance.

### Provenance retains material security facts only

Provenance SHOULD preserve/reference a security/dependency fact when materially needed to explain:

- which dependency/service actually affected Learning/Generation/Evaluation;
- that a network/egress path materially participated;
- which security-domain context is required for reproducibility;
- why recovery changed operational outcome;
- historical policy context where auditability requires it.

It does not ingest the entire authorization decision log.

### Audit records do not become semantic authority

An audit log saying `allowed` or `completed` does not override canonical Learning/Generation/Evaluation/Execution state.

## Failure and issue representation

Architecture SHALL preserve enough typed issue semantics to distinguish at least:

- dependency unavailable;
- dependency identity/integrity mismatch;
- dependency untrusted/unapproved;
- dependency use unauthorized;
- required network prohibited;
- egress category/destination prohibited;
- authorization indeterminate/unavailable;
- credential unavailable/expired;
- secret access denied;
- source/reference read denied;
- Learned State use/read/export denied;
- candidate/output/diagnostic access denied;
- query/provenance detail withheld;
- runtime attempted undeclared network/egress;
- cross-security-domain resolution denied;
- policy changed since commitment;
- security enforcement capability insufficient for required profile.

These are architecture-level issue categories, not a new universal domain failure enum.

### Pre-commit versus post-commit treatment

Before commitment, a known incompatible dependency/security condition normally produces readiness blockers rather than fake failed domain activities.

After commitment, an inability to perform an authorized required action is represented through Execution operational facts plus the owning domain lifecycle. The exact semantic terminal result depends on the activity contract and whether safe continuation remains possible.

## Public/API architecture consequences

Future SDK/CLI/service APIs MUST be able to express, without relying on a generic `permission_denied` string:

- dependency requirement and exact resolution state;
- integrity/trust/approval status where authorized;
- acquisition versus runtime network behavior;
- egress categories/destinations;
- committed network/no-egress posture;
- current authorization decision/status and reason code where disclosure permits;
- operation being denied/withheld;
- `absent` versus `unknown` versus `unavailable` versus `withheld`;
- capability/use versus payload-read distinctions;
- security-domain/tenant boundary errors;
- policy change/retry revalidation requirements;
- legitimate next actions without revealing protected information.

Public resource handles remain identity/navigation objects, not transferable bearer-capability tokens by default.

## Persistence architecture consequences

Control-plane persistence must have room for stable references to, as applicable:

- dependency requirement/resolution identity;
- verified concrete dependency identity;
- trust/approval decision reference;
- committed network/egress profile;
- security domain/tenant context;
- relevant authorization/audit decision references;
- disclosure/classification references;
- secret references without values;
- security-related current restrictions;
- material Provenance relationships.

These fields do not require one monolithic security table or database.

Derived security/read models remain non-authoritative and rebuildable where appropriate.

## Deployment architecture obligations handed to 004-I

004-I must choose or constrain deployment/platform mechanisms sufficient to realize this architecture, including where applicable:

- identity/workload-principal integration;
- network isolation and outbound controls;
- secret-manager integration;
- storage/catalog authorization;
- runtime sandbox/process/container boundaries;
- private package/artifact distribution;
- authorization service/policy integration;
- security/audit event transport;
- encryption in transit/at rest expectations;
- tenant/security-domain isolation;
- query/index security enforcement;
- platform-specific credential delegation;
- provider-specific egress/fencing limitations.

004-H specifies the required semantics; 004-I maps them to concrete deployment/platform architecture.

## Enterprise-scale security

Security controls MUST remain compatible with large distributed workloads.

The architecture MUST NOT require:

- collecting all source/generated rows to a driver merely to authorize access;
- copying all Learned State through the coordinator to mediate security;
- evaluating one control-plane authorization request per row when the underlying provider can enforce a stable scoped dataset capability;
- ingesting every runtime event into Provenance;
- materializing all graph/query results before filtering authorization.

Authorization may issue scoped capabilities over stable distributed references, partitions, table snapshots, object prefixes or equivalent provider-native boundaries when their semantics are sufficient.

Fine-grained row/column policies MAY be delegated to the underlying data platform where present; SYNGAN does not invent a universal row-level security concept.

## No-new-concept audit

004-H does **not** introduce standalone domain concepts for:

- Security;
- Policy;
- Authorization;
- Authentication;
- Principal;
- Role;
- Permission;
- Capability;
- Data Classification;
- Trust;
- Approval;
- Artifact;
- Dependency Resolution;
- Egress;
- Network;
- Secret;
- Credential;
- Redaction;
- Tenant;
- Security Domain;
- Audit Event.

These remain external authorities, architecture mechanisms, integration state, or view/security semantics unless future independent state/actions/invariants justify explicit concept discovery.

## Architecture invariants

1. Dependency requirement, dependency availability/integrity, semantic compatibility, trust/approval, authorization and egress permission MUST remain distinguishable.
2. A mutable locator MUST NOT silently substitute for exact dependency identity where historical/reproducibility guarantees require stronger identity.
3. Dependency acquisition MUST NOT occur implicitly during committed runtime execution.
4. Core supported structured/tabular workflows MUST remain operable without outbound network after approved local provisioning.
5. Network connectivity MUST NOT imply permission to transmit source, source-derived, generated or diagnostic data.
6. A later authorization grant MUST NOT broaden a committed no-network/no-egress/dependency semantic profile.
7. A later authorization revocation MUST NOT rewrite historical commitment or Provenance.
8. Sensitive actions MUST be authorized at an action/resource/context boundary appropriate to their risk; a global resource Boolean is insufficient.
9. Public durable resource handles MUST NOT act as bearer credentials merely by possession.
10. Runtime adapters SHOULD receive bounded delegated capabilities rather than ambient broad credentials/network/state access.
11. Delegated runtime capability MUST NOT exceed the intersection of committed semantics, current authorization and deployment capability.
12. Secret bearer values MUST NOT be persisted in canonical semantic state, Provenance, Evidence, manifests, checkpoints, public handles or ordinary logs.
13. Learned State, candidate output, completed output, diagnostics and Provenance MUST NOT be assumed non-sensitive merely because they are source-derived or synthetic.
14. Semantic completion MUST NOT imply export/release authorization.
15. `WITHHELD`/redacted/unknown/unavailable/absent MUST remain distinguishable when disclosure policy permits the distinction.
16. Redaction MUST be a view-time authorized transformation and MUST NOT rewrite canonical history.
17. Derived search/graph/history/reproducibility projections MUST enforce disclosure policy and MUST NOT become information-leak bypasses around canonical resources.
18. Security filters MUST account for relationship/count/existence leakage where those facts are protected.
19. Retry/resume MUST revalidate current security/dependency authorization without changing committed semantics.
20. Revocation and Attempt fencing are complementary; neither replaces the other.
21. Unknown/indeterminate authorization for a protected action MUST NOT be treated optimistically as permission.
22. Security audit MUST remain distinct from Provenance and neither may override canonical semantic state.
23. Multi-tenant/security-domain deployment MUST preserve isolation even when physical storage/index/cache infrastructure is shared.
24. Security architecture MUST remain distributed/enterprise-scale and MUST NOT require ordinary full payload materialization on the driver.
25. No security mechanism may turn a generic Security/Policy/Artifact/Authorization object into new cross-concept semantic ownership by convenience.

## Operational examples

### Local artifact, no-egress Generation

```text
Generation G42 commitment
Strategy S4/R3
Dependency requirement B3/H7
Network posture: no outbound network
Egress: none

Dependency resolver
→ local repository contains B3/H7
→ integrity verified
→ approved for security domain D1

Authorization
→ workload may read B3/H7
→ workload may read Source S8
→ workload may write Candidate C42

Attempt capability set
→ read Source S8
→ read B3/H7
→ write fenced C42
→ no network capability
→ no export capability
```

If B3 disappears before retry, the new Attempt is blocked pending approved local restoration. It does not download B3 or switch to B4.

### Remote Evaluation with bounded egress

```text
Evaluation V9
Remote method R7
Committed egress plan:
  aggregate summary only
  destination service = RS3
  no source records
  no generated records

Current authorization:
  RS3 permitted
  aggregate summary permitted

Runtime receives:
  exact candidate read capability
  bounded summary transformation
  scoped RS3 client
  no arbitrary network capability
```

An attempt by the plugin to upload example rows is outside the committed/authorized plan and must not be accepted as an implicit extension of permission.

### Restricted historical query

```text
Actor asks:
Explain Output O42

Canonical history:
O42 ← G42 ← Source S8 ← protected domain D1
             ↘ Base artifact B3

Authorized view:
O42 ← G42
Source relationship: present
Source identity: WITHHELD
Base dependency: approved local dependency [detail withheld]
```

If even source existence is protected, the query returns a policy-authorized opaque path/summary rather than leaking the hidden edge through graph shape or result counts.

### Revocation during recovery

```text
Attempt A1 fails
Checkpoint CP7 valid

Before A2 resume:
source access was revoked

Result:
checkpoint compatibility: technically valid
current authorization: denied
resume: blocked
Execution: recovery pending or terminal according to allowed continuation
```

SYNGAN does not reinterpret CP7 as invalid and does not rewrite the historical source binding. It simply cannot currently exercise the required authorized source access.

## Representation questions intentionally deferred

004-H does not decide:

- RBAC versus ABAC or policy language;
- identity provider or authentication protocol;
- cloud/platform IAM technology;
- authorization service implementation;
- exact data-classification vocabulary;
- package/artifact signing/scanning technology;
- artifact repository;
- secret manager/KMS;
- token/capability encoding;
- TLS/encryption implementation;
- DLP implementation;
- network firewall/service mesh/sandbox technology;
- exact tenant-isolation deployment topology;
- security audit backend;
- query-security physical strategy;
- cache partitioning implementation;
- incident-management system;
- retention/deletion policy details.

Those implementation/platform choices must preserve the architecture above and are refined primarily by 004-I and later implementation planning.

## Phase outcome

004-H establishes an enterprise security architecture that preserves the accepted semantic model while making dependency trust, offline/no-egress behavior, actor/service authorization, delegated runtime capabilities, sensitive-state access, redaction/withholding, secret handling, query security and revocation explicit implementation-facing boundaries.

No accepted concept or synchronization requires revision.

The next architecture group is **004-I — Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture**.