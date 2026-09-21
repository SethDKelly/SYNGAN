---
type: Architecture Authority
title: Phase 007-G Strategy/Method Binding, Dependency Trust, Authorization, Secrets & Distributed Runtime Closure Foundation
status: active
---

# Phase 007-G — Strategy/Method Binding, Dependency Trust, Authorization, Secrets & Distributed Runtime Closure Foundation

## Purpose

Refine SYNGAN's executable-realization architecture for semantic Strategy/method binding, exact implementation closure, dependency resolution and trust, authorization, secret handling, network/egress control, distributed worker closure, and runtime invocation **without selecting a plugin framework, dependency registry, package-distribution mechanism, IAM/policy engine, secret manager, model hub, Spark launcher, container system, concrete Python SPI, or executable verification implementation**.

007-G continues the architecture/design track governed by the [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md). It is design authority, not permission to implement runtime/security behavior.

## Governing authority

007-G is downstream of:

- [Concept Design Methodology](../authority/design-methodology.md);
- [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md);
- [Synthesis Strategy](../concepts/synthesis-strategy.md);
- [Network and External Dependency Policy](../authority/network-external-dependency-policy.md);
- [Self-Contained Execution & Runtime Distribution Closure Contract](../authority/self-contained-execution-runtime-distribution-closure-contract.md);
- [007-D Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation](phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md);
- [007-E Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline](phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md);
- [007-F Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation](phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md);
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](strategy-extension-learning-generation-evaluation-runtime-adapter.md);
- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md);
- [ADR-0004 — Semantic Extension & Runtime Binding Separation](../decisions/ADR-0004-semantic-extension-runtime-binding-separation.md);
- [ADR-0007 — Explicit Dependency Resolution & Scoped Capability Security](../decisions/ADR-0007-explicit-dependency-resolution-scoped-capability-security.md);
- [ADR-0010 — Self-Contained Distributed Runtime Closure](../decisions/ADR-0010-self-contained-distributed-runtime-closure.md);
- accepted concepts, synchronizations and experience authority.

Earlier Phase 005-F/005-I concrete implementation choices remain planning evidence. They do not become binding architecture merely because they were once selected as future implementation defaults.

## Design result

007-G accepts this executable-realization foundation:

> **Semantic Strategy/method authority, executable implementation binding, resolved dependency closure, current authorization, runtime capability delegation, and physical runtime realization are separate axes that may be composed for one Attempt but must not be collapsed into one plugin/configuration object.**

> **An Attempt may execute only after its material executable/artifact closure is exact enough for the required claim, trusted/authorized for the current security context, compatible with the committed semantics, and distributable to every material runtime role. Driver-local readiness is never sufficient.**

> **Runtime capabilities are current delegated authority, not durable semantic state. Secret values are operational material, not canonical resources or provenance payload.**

> **A missing component, revoked permission, incompatible worker, or unavailable secret must block/fail explicitly; runtime may not repair the situation by undeclared installation, dependency substitution, network expansion, or remote fallback.**

## 1. Architecture roles and non-concepts

007-G uses architecture/integration roles equivalent to:

- implementation binding;
- method binding;
- implementation component;
- implementation closure;
- dependency requirement;
- dependency resolution;
- artifact identity;
- acquisition/provisioning;
- integrity/authenticity assessment;
- trust/approval decision;
- authorization decision;
- runtime capability;
- secret reference/resolution;
- network/egress plan;
- runtime role/profile;
- runtime closure assessment;
- immutable Attempt invocation.

None is a new accepted domain concept.

In particular, 007-G does not create generic `Plugin`, `Model`, `Artifact`, `Dependency`, `Security`, `Authorization`, `Capability`, `Secret`, `Runtime`, `Environment`, `Cluster`, `Registry`, `Context`, or `Session` concepts.

## 2. Core separation

Architecture preserves at least these boundaries:

```text
semantic Strategy / method / activity commitment
        ↓
implementation binding selection
        ↓
exact dependency + implementation closure resolution
        ↓
identity / integrity / trust / compatibility assessment
        ↓
current authorization + network/egress qualification
        ↓
runtime-role distribution closure
        ↓
Attempt-scoped immutable invocation
        +
current scoped runtime capabilities / secret access
        ↓
physical runtime realization
        ↓
non-final runtime/material results
        ↓
owner semantic validation / promotion / Evidence establishment
```

One implementation may optimize several steps together, but their authority semantics remain distinguishable.

## 3. Semantic Strategy/method authority versus implementation binding

### 3.1 Strategy remains semantic synthesis authority

Synthesis Strategy owns reusable declarations about synthesis behavior, requirements, capabilities, limitations, topology support, Learning/Learned-State needs, reproducibility characteristics, scale/resource expectations, and external dependency/network profile.

An executable package/class/model/service cannot broaden those semantics by being installed or registered.

### 3.2 Evaluation method binding remains architectural

An Evaluation may commit a method/configuration appropriate to its Criterion without introducing a standalone Evaluation Method concept.

Executable method binding states which concrete implementation can realize that committed method under what dependency/runtime conditions.

It cannot redefine the Criterion question or inflate Evidence claim strength.

### 3.3 Binding identity is distinct from package/model identity

An implementation binding is a revisioned integration statement connecting semantic authority to executable realization.

It may resolve one or many implementation components and dependencies.

Therefore:

```text
Strategy revision
!= implementation-binding revision
!= implementation component/package build
!= runtime/SPI contract version
!= state codec/representation version
!= platform/runtime version
```

No generic `plugin_version` may carry all of these meanings.

### 3.4 Bindings may narrow, not silently broaden

A binding may support less than the Strategy declares—for example only one topology, smaller scale envelope, CPU-only execution, or a narrower dependency profile.

Readiness then reports the binding limitation.

A binding may not claim broader semantic support than its Strategy/method authority without an upstream semantic revision.

## 4. Binding selection and retry semantics

### 4.1 Semantic commitment need not always freeze one implementation

The committed Learning/Generation/Evaluation semantics may either:

- require an exact implementation binding when compliance/reproducibility/user intent makes the implementation itself a committed requirement; or
- permit later operational selection from a declared compatible set/profile when the semantic commitment intentionally remains implementation-neutral.

The architecture must preserve which case applies.

### 4.2 Attempt freezes exact realization

Every Attempt binds one exact implementation closure/invocation before material execution.

Within that Attempt, runtime must not silently substitute:

- another implementation binding;
- another model/base artifact;
- another tokenizer/vocabulary;
- another dependency version;
- a remote service for a local component;
- another remote service/provider;
- another state codec;
- another source/Learned-State binding.

If substitution is necessary, the Attempt cannot continue as though nothing changed.

### 4.3 Later Attempt may use another compatible realization only when permitted

A later Attempt for the same semantic activity/Execution may use a different executable binding/closure only when all of the following hold:

- the semantic commitment did not require the exact prior implementation;
- the new binding is compatible with the exact unchanged semantic commitment;
- no material Strategy/configuration meaning changes;
- current dependency/security/platform/recovery qualification passes;
- the new Attempt receives a distinct immutable invocation identity/snapshot;
- historical/provenance facts preserve which realization each Attempt used.

This is operational re-realization of the same semantic occurrence, not mutation of the prior Attempt.

If changing the implementation would change the committed semantics, dependency/network posture, required limitations, or an implementation identity that the actor explicitly committed, a new semantic commitment/activity is required instead.

## 5. Implementation closure

### 5.1 Closure may be composite

One top-level binding may require a graph/set of components, for example:

```text
structured synthesis binding
  ├── tabular implementation component
  ├── source-derived text component
  ├── state codec
  ├── native/runtime library
  └── immutable learned/base artifact
```

One package or model is not a universal closure unit.

### 5.2 Closure identity

Architecture must permit one Attempt to retain or resolve a bounded exact closure identity sufficient to explain the material components that executed.

The concrete representation may later use a root descriptor plus component references, digest/manifests, environment identity, provider image identity, or equivalent.

007-G does not select one closure serialization or hashing scheme.

### 5.3 Closure identity is claim-strength scoped

A package version string, image tag, path, environment name, registry alias, or model filename is not automatically exact immutable identity.

The closure representation must state enough actual identity/integrity basis for the claims being made.

For example:

```text
image:latest
model/current
package >= 2
```

may be valid *requirements/selectors* but are not sufficient historical identities once an exact instance actually ran.

### 5.4 Role-specific closure is allowed

Distributed closure does not require every heterogeneous runtime role to contain identical bytes.

It requires every role to satisfy the exact **role-specific** closure required by the top-level Attempt.

For example:

```text
coordinator role -> control/runtime client closure
Spark executor    -> generation worker closure
GPU trainer       -> accelerator/training closure
remote service    -> exact/qualified external service contract
```

The aggregate Attempt remains closed only if every material role satisfies its declared role-specific requirement.

## 6. Dependency requirement versus resolved dependency

### 6.1 Requirement declares what is acceptable

A dependency requirement may state exact identity or an explicitly allowed compatibility range/class, plus material representation/runtime/network/security constraints.

A requirement is not the actual dependency that ran.

### 6.2 Resolution chooses the concrete instance

Resolution identifies the exact current dependency instance offered by the environment and evaluates whether it satisfies the requirement.

Architecture must preserve independent outcomes equivalent to:

```text
availability
identity match
integrity/authenticity
trust/approval
runtime compatibility
semantic/activity compatibility
current authorization
network/egress compatibility
```

A single `dependency_ok=true` is insufficient when these axes can disagree.

### 6.3 Mutable locator never replaces exact identity

Package names, registry tags, URLs, cache keys, aliases and file paths are locators/selectors unless their provider contract establishes immutable identity strongly enough.

Historical work records the exact resolved identity needed for explanation/reproducibility, not merely the mutable selector.

## 7. Acquisition / provisioning boundary

### 7.1 Acquisition is explicit and outside material runtime execution

Provisioning may acquire packages/models/artifacts before committed execution when the selected profile allows it.

Acquisition is distinct from Learning/Generation/Evaluation runtime.

### 7.2 Acquisition success proves little by itself

Successful download/install/provisioning does not automatically establish:

- expected identity;
- integrity/authenticity;
- organization trust/approval;
- runtime compatibility;
- semantic compatibility;
- current permission to use the dependency.

These remain independently qualified.

### 7.3 No hidden runtime acquisition

During an Attempt, missing material must not trigger undeclared:

- package installation;
- public registry/model-hub lookup;
- artifact download;
- remote inference fallback;
- telemetry/network activation;
- dependency replacement.

The correct outcome is explicit blocked/incompatible/failure/indeterminate state according to lifecycle context.

## 8. Trust and supply-chain boundary

### 8.1 Presence is not trust

A component may be installed and identity-verified but still be disallowed for the current environment/security domain.

### 8.2 Trust dimensions remain separable

Architecture should be able to distinguish evidence/decisions equivalent to:

- bytes/content identity established;
- source/provenance/authenticity established or unknown;
- integrity verified/failed/unknown;
- code/artifact scan or organization approval where policy requires it;
- license/policy eligibility where external governance provides it;
- permission for the current use/security domain.

007-G does not prescribe signatures, SBOMs, attestations, malware scanners, artifact repositories, or approval systems.

### 8.3 Third-party code loading is itself a protected action

Discovering metadata about an installed extension is different from importing/executing its code.

Where loading third-party code can execute arbitrary initialization logic, trust/authorization should be established before that code is invoked whenever the platform allows it.

An extension discovery mechanism must not turn enumeration into automatic execution.

### 8.4 Unsafe deserialization is code-execution trust

A Learned-State/dependency codec that can execute arbitrary code during load must declare that characteristic.

Being able to deserialize it technically does not make it approved. Security policy may block or isolate the load.

## 9. Network and egress composition

### 9.1 Network dependency profile remains semantic declaration

Strategy/method authority declares whether its behavior is self-contained, local-artifact dependent, acquisition-network dependent, or runtime-network dependent where material.

Implementation binding may narrow or add implementation-specific requirements but cannot silently convert a self-contained semantic profile into runtime-network behavior.

### 9.2 Connectivity and data egress are distinct

Architecture preserves separately:

```text
network capability
approved destination/service
protocol/action role
egress category
source/security domain
payload/derivation category
current authorization
```

`network_enabled=true` is not an adequate egress model.

### 9.3 Runtime-network implementations need an explicit service boundary

If material synthesis/evaluation depends on a remote service, the Attempt must bind enough exact/qualified service identity and contract context to explain what service was used and what was allowed to leave the execution boundary.

Where the remote provider cannot offer byte-level software identity, the architecture records the strongest available service/model/API/version/endpoint/account/deployment identity and must not overstate reproducibility.

### 9.4 Remote service drift cannot be hidden

A mutable endpoint whose underlying model/service changes may weaken exact reproducibility even when its URL is stable.

If the service identity cannot be pinned strongly enough, that limitation is a declared compatibility/reproducibility fact.

## 10. Authorization model

### 10.1 Authorization is action-specific and current

Authorization evaluates a principal/service action against the relevant resource, dependency, security domain, data/egress context and current policy.

Permission to inspect a Generation summary does not imply permission to read its source rows, Learned State, candidate output, diagnostics, dependencies, secrets, Provenance, or exported payload.

### 10.2 Commitment-time authorization and use-time authorization differ

An actor may have permission to commit work at T1 and lose permission to perform a sensitive read/retry/egress at T2.

Historical commitment remains true; current action becomes blocked.

A later permission grant cannot broaden the immutable semantic/network posture that was committed.

### 10.3 Authorization decision does not become semantic state

Authorization decisions may be retained/audited where material, but they do not own Strategy, Learning, Generation, Evaluation, Evidence, Execution or Provenance lifecycle meaning.

## 11. Runtime capability delegation

### 11.1 Capabilities are bounded operational authority

Runtime receives only the authority needed for its exact role, conceptually:

```text
runtime capability
    = committed requirement
      ∩ current authorization
      ∩ deployment/platform capability
      ∩ current recovery/fencing authority where material
```

A broad permission cannot create a semantic requirement, and a semantic requirement cannot manufacture a permission.

### 11.2 No ambient canonical-store authority

Third-party/model/runtime code should not receive unrestricted canonical database/repository access merely because it runs inside the same process or cluster.

Runtime interacts through bounded data/dependency/output/progress/secret/network capabilities or equivalent platform-enforced seams.

### 11.3 Capability lifetime may differ from Attempt lifetime

An Attempt invocation is immutable historical realization context, while live authorization/capabilities may expire, rotate or be revoked.

Therefore persisted invocation state must not embed reusable bearer capability/credential values.

The Attempt may reference requirement/decision/audit identities while live grants are refreshed/reissued only under current authority.

### 11.4 Revocation blocks; it does not rewrite

Revoking a capability may stop future operations or continuation. It does not rewrite the semantic commitment or erase prior authorized actions.

## 12. Secret architecture

### 12.1 Secret value versus secret reference

Architecture distinguishes a durable/non-secret reference or requirement for a secret from the sensitive secret value/credential itself.

Where persistence is required, canonical/invocation state stores only bounded non-secret reference/context—not the secret value.

### 12.2 Secret values are excluded from semantic/history payloads

Secret/credential values must not appear in:

- semantic Strategy configuration unless the value itself is genuinely domain behavior rather than a credential;
- committed activity snapshots;
- durable public handles;
- manifests;
- Evidence;
- Provenance payloads;
- checkpoints;
- ordinary logs/telemetry;
- reproducibility exports.

Audit may record a safe secret-reference/version/credential-class decision where needed, not the value.

### 12.3 Resolve at use time

Runtime should obtain secrets through a scoped secret capability/broker/platform mechanism at the material use boundary.

The exact secret-manager technology is deferred.

### 12.4 Rotation is normally operational

Rotating a credential that grants equivalent authorized access does not require a new Strategy revision or semantic activity merely because the secret bytes changed.

If changing credentials also changes destination/account/security domain/service identity or otherwise materially changes the committed execution meaning, then the relevant semantic/invocation/dependency authority must be reconsidered.

### 12.5 Secret unavailability does not justify fallback

If a required secret cannot be resolved, runtime blocks/fails according to lifecycle context. It must not substitute ambient credentials, a developer token, another account, or a less protected endpoint.

## 13. Runtime invocation foundation

### 13.1 Attempt-scoped immutable invocation

Before material execution, the application/control layer creates or binds an immutable invocation specification for one Attempt.

It contains or references the exact material facts required to execute that Attempt, including where applicable:

- semantic activity + immutable commitment identity;
- Strategy/configuration or Evaluation method identity;
- exact implementation binding revision;
- exact implementation/dependency closure identity;
- exact source/sealed subject/Learned-State references;
- activity-owned randomness/coverage/approximation semantics;
- declared network/egress posture;
- runtime-role requirements;
- approved output/candidate/diagnostic sinks;
- writer/recovery authority references required for safe mutation;
- representation/SPI versions needed for interpretation;
- security-domain and non-secret capability requirements.

It must remain bounded and must not copy unrelated canonical state.

### 13.2 Live capabilities are not serialized into the invocation

The invocation may reference capability requirements and material authorization/audit decisions, but bearer tokens, secrets, live sessions and refreshable credentials remain outside its durable representation.

### 13.3 Runtime reads exact references

Runtime may not re-resolve semantic/current aliases such as `latest`, `current`, or mutable provider tags in place of the exact bound dependency/source/Learned-State/subject when exact identity is required.

## 14. Distributed runtime closure

### 14.1 Every material role must close

A distributed Attempt is ready only if each material runtime role can execute its role-specific exact compatible closure.

Coordinator/driver readiness alone never proves distributed readiness.

### 14.2 Dynamic workers

Where autoscaling/replacement is supported, a deployment must guarantee that any newly eligible worker inherits/proves the required closure before receiving material work.

A worker that does not satisfy closure is ineligible for the Attempt rather than allowed to self-repair over public network.

### 14.3 Closure may be established by profile rather than enumerating workers

Architecture need not persist one control record per worker.

A deployment may prove closure through an immutable worker image/template/environment/profile whose guarantees apply to every eligible worker.

This preserves bounded control state.

### 14.4 Mixed runtime roles

Learning/Generation/Evaluation may use mixed coordinator, Spark, accelerator, native and optional remote-service roles.

Each role has its own requirements; the whole Attempt is closed only when their composition is compatible with the exact binding and committed semantics.

### 14.5 Large state/artifact locality

Large Learned State, model, tokenizer or other artifacts may be sharded, shared, cached by exact identity, or loaded provider-natively.

No universal driver-memory materialization/broadcast requirement is accepted.

A cache hit is not sufficient if identity/integrity/trust/authorization cannot be established for the cached content.

## 15. Topology capability interaction

Implementation binding/runtime closure must be able to express support/limitations for the logical structured-data topology refined by 007-F.

A binding may support single-table but not time-series, multi-table but only certain fan-out/cardinality ranges, or composite topology only under specific runtime profiles.

These are implementation/runtime limitations.

They do not own or redefine the underlying Data Meaning structural assertions, Generation scope, or Constraint semantics.

If the selected binding cannot realize the committed topology, readiness reports incompatibility/limitation; it must not flatten the subject to a simpler topology.

## 16. Learned State interaction

### 16.1 Logical state versus executable load closure

A Learned State identity remains semantic result authority.

To use it, runtime must resolve an executable load closure including its exact representation/codec/components/base artifacts and compatible implementation/runtime requirements.

### 16.2 Base artifacts remain exact dependencies

If Learned State depends on a pretrained base model/tokenizer/dictionary/reference artifact, that dependency remains part of the material load/invocation closure and is historically attributable where relevant.

The logical Learned State does not absorb those artifact bytes into its identity merely because they are required for loading.

### 16.3 Large state remains distributed

Worker-local/shared/sharded state loading remains valid. Driver-only deserialization is not a universal prerequisite.

## 17. Failure/readiness semantics

Architecture must preserve distinguishable dimensions/outcomes equivalent to:

```text
semantic incompatibility
binding limitation/incompatibility
dependency missing/unavailable
wrong dependency identity
integrity/authenticity failure or unknown
untrusted/unapproved
current authorization denied/indeterminate
secret unavailable
network/egress incompatible or denied
runtime/SPI/platform incompatible
distribution closure incomplete
worker role incompatible
remote-service identity/reproducibility limitation
closure indeterminate
```

These may be orthogonal fields rather than one flat enum.

`indeterminate` is never promoted to ready merely because the driver can import code.

## 18. History / Provenance / reproducibility

Where materially behavior-affecting, history must retain enough exact facts to explain:

- semantic Strategy/method identity;
- exact implementation binding used by each Attempt;
- implementation/dependency closure identities;
- state codec/base artifact identities;
- runtime/platform profile/version facts;
- remote service/model/API identity to the strongest available basis;
- declared network/egress posture;
- material limitation/indeterminacy;
- authorization/security audit references when required for explanation without embedding secrets.

This does not make Provenance a package inventory or security access log.

If the exact executable/dependency closure cannot later be reconstructed, the strongest reproducibility claim must weaken rather than guessing.

## 19. Self-contained baseline consequence

The complete supported baseline still requires at least one source-derived/local free-form-text-capable Strategy path with no externally acquired pretrained model or runtime service required for normal execution after supported provisioning.

The architecture therefore cannot make a model hub, remote embedding service, hosted LLM, or pretrained world-knowledge artifact mandatory to ordinary baseline structured-data synthesis.

Optional local-artifact and runtime-network Strategies remain compatible when explicit.

## 20. Phase 005-F / 005-I implementation-planning disposition

Earlier implementation planning proposed concrete choices such as:

- standard-library `typing.Protocol` for runtime SPIs;
- specific runtime adapter/protocol names;
- Python entry-point group `syngan.runtime_extensions`;
- a process-local extension catalog;
- specific `ResourceKind` values;
- explicit `RuntimeSpiVersion` spelling;
- `spark` / `torch` optional extras;
- concrete `DependencyRequirementRef`, `DependencyResolution`, `AuthorizationDecision`, `CapabilityGrant`, `SecretRef`, and related type names;
- concrete package/module ownership for security/runtime ports;
- particular discovery and provisioning workflows.

007-G preserves the **responsibilities and boundaries** those choices were intended to satisfy but does not treat their Python spelling, package topology, entry-point mechanism, protocol mechanism, or resource representation as settled architecture.

They remain candidates for implementation re-entry after the architecture track is explicitly consolidated.

## 21. Falsification scenarios

007-G tests the architecture against at least these cases.

### Scenario A — installed but untrusted extension

The package is installed and discoverable, but current policy has not approved it for the security domain.

Result: discovery/availability may be true; runtime eligibility is false/blocked. Presence does not become trust.

### Scenario B — driver ready, one executor missing native dependency

The coordinator resolves the Strategy, while one dynamically allocated worker lacks a required native library.

Result: distributed closure is not satisfied; the worker is ineligible or the Attempt blocks/fails. No worker-side public installation occurs.

### Scenario C — source-derived baseline text

The selected Strategy synthesizes a free-form text field using source-derived local behavior.

Result: no pretrained model-hub/API dependency is introduced merely because the field is text.

### Scenario D — optional pretrained local text

A Strategy requires an exact locally provisioned model/tokenizer.

Result: the artifacts are explicit dependency closure components; a missing artifact blocks rather than downloading automatically.

### Scenario E — runtime-network Strategy under no-egress commitment

Implementation can technically call a remote service.

Result: semantic/network incompatibility remains; a permission or available API key cannot make the committed no-egress activity compatible.

### Scenario F — secret rotates during long Attempt

A credential expires and a replacement credential grants equivalent scoped access to the same approved destination.

Result: live capability/secret may be reissued under current authority without rewriting semantic commitment or immutable invocation meaning; secret bytes are not persisted.

### Scenario G — permission revoked after commitment

Generation remains historically committed, but source-read permission is revoked before retry.

Result: retry/read becomes blocked; the historical commitment is unchanged and runtime cannot substitute a different source.

### Scenario H — implementation crashes and fallback binding exists

A compatible alternative implementation is available.

Result: the running Attempt cannot hot-swap. A later Attempt may select the alternative only if the unchanged semantic commitment permits implementation-neutral re-realization and the new exact invocation is recorded.

### Scenario I — user committed exact implementation for compliance

A later compatible implementation is technically available.

Result: the exact implementation requirement is part of the activity contract; changing it requires a new semantic commitment rather than silent retry substitution.

### Scenario J — third-party entry-point metadata exists

Extension metadata can be enumerated, but importing the provider executes arbitrary package initialization.

Result: discovery does not imply authorization to import/execute. Trust/authorization precedes code execution where technically possible.

### Scenario K — unsafe Learned-State codec

State representation requires code-executing deserialization.

Result: technical compatibility does not imply policy approval; load may be denied or isolated.

### Scenario L — cache contains artifact under mutable alias

A worker cache has `model/current`, but the Attempt requires artifact A17.

Result: cache presence is insufficient until exact identity/integrity match A17 is established.

### Scenario M — remote API silently changes underlying model

Endpoint URL remains constant but provider model changes.

Result: historical service identity/reproducibility claim is limited to what the provider can actually identify/pin; stable URL does not manufacture exact reproduction.

### Scenario N — composite topology uses mixed runtimes

A multi-table subject includes a time-series scope, and the selected Strategy uses Spark for distributed structured work plus a separate local text component.

Result: semantic topology remains Data Meaning/Generation authority; implementation closure composes role-specific components without creating a `CompositeStrategy` concept.

The scenarios remain coherent under existing concept/synchronization/ADR authority.

## 22. Future verification obligations — non-executable during design freeze

At later implementation re-entry, verification should eventually prove, where applicable:

- semantic Strategy identity remains separate from binding/package/runtime identity;
- a binding cannot broaden Strategy semantic claims;
- runtime cannot hot-swap undeclared dependencies/components inside one Attempt;
- a permitted later Attempt can use a distinct compatible binding without rewriting prior Attempt history;
- driver readiness does not imply worker readiness;
- dynamic workers cannot receive material work without required closure;
- missing artifacts do not cause hidden acquisition;
- no-egress commitments cannot be broadened by authorization or available credentials;
- extension discovery does not automatically execute untrusted code;
- unsafe state loading is policy-visible;
- secret values do not enter durable semantic/history representations;
- capability revocation blocks current action without rewriting historical commitment;
- topology limitations are reported rather than silently simplified;
- large state/model loading does not universally require the driver;
- exact material implementation/dependency identities are attributable for reproducibility.

These are design obligations only. 007-G adds no executable checks.

## 23. Explicitly deferred

007-G intentionally does not select:

- Python ABC versus Protocol versus another SPI mechanism;
- exact runtime adapter interfaces/classes;
- Python entry points or any other plugin discovery mechanism;
- `syngan.runtime_extensions` or another entry-point group;
- implementation-binding persistence schema;
- closure-manifest schema/digest algorithm;
- package/image/environment identity technology;
- artifact repository/model registry;
- SBOM/signing/attestation/scanning technology;
- PySpark/PyTorch/ML library version;
- Spark package-distribution mechanism;
- PEX/Conda/venv/container/Databricks environment mechanism;
- runtime launcher/orchestrator;
- IAM/RBAC/ABAC/policy engine;
- identity provider;
- secret manager/KMS;
- network firewall/service mesh/DLP product;
- secret-reference/token format;
- concrete egress categories beyond current semantic distinctions;
- capability token format/lifetime;
- remote-service client/protocol;
- exact history/provenance schema for executable closure;
- implementation/security/runtime tests or enforcement.

## 24. Phase boundary

007-G completes when architecture can explain how one exact semantic commitment becomes one exact, trusted, authorized, distributed executable Attempt without selecting concrete implementation technology.

It does not authorize runtime/security implementation.

## Invariants

1. Strategy/method semantics MUST remain separate from executable implementation identity.
2. Installed/discovered code MUST NOT create or broaden semantic capability authority.
3. Every material Attempt MUST bind an exact executable/dependency closure sufficient for the required historical/reproducibility claim.
4. Runtime MUST NOT silently substitute a component/dependency/binding inside an Attempt.
5. A later Attempt MAY use another compatible binding only when the unchanged semantic commitment permits it and the new realization is independently attributable.
6. Dependency requirement, concrete resolution, integrity/authenticity, trust, semantic/runtime compatibility and authorization MUST remain distinguishable.
7. Acquisition MUST remain explicit and MUST NOT occur as hidden runtime repair.
8. Runtime-network and egress behavior MUST remain explicit before material execution.
9. Current authorization MUST NOT broaden immutable committed semantics.
10. Durable handles/references MUST NOT become bearer credentials by possession alone.
11. Runtime capabilities MUST remain bounded by committed need, current permission, deployment capability and current operational/recovery authority.
12. Secret values MUST NOT become canonical semantic/history/provenance material.
13. Secret rotation normally remains operational when it preserves the same authorized meaning.
14. Driver/coordinator readiness MUST NOT establish distributed runtime closure.
15. Every material worker/runtime role MUST satisfy its exact role-specific compatible closure or remain ineligible.
16. Dynamic worker admission MUST preserve closure.
17. Large state/model/artifact distribution MUST NOT universally require driver-memory materialization/broadcast.
18. Cache/discovery presence MUST NOT substitute for exact identity/integrity/trust/authorization.
19. Strategy implementation topology capability MUST NOT redefine Data Meaning/Generation/Constraint topology semantics.
20. Missing/untrusted/unauthorized/incompatible/indeterminate closure MUST NOT be represented as ready merely because code can technically run.
21. Optional remote/pretrained capabilities MUST NOT become mandatory baseline dependencies.
22. No rule here makes PyTorch, Spark ML, Hugging Face, Python entry points, containers, Databricks, any IAM/policy engine, or any secret manager universal SYNGAN semantics.
23. 007-G adds no production implementation or new executable design gate.

## Operational principle

A practitioner commits a Generation against exact semantic topology and a Strategy that permits implementation-neutral realization. The control plane selects a compatible implementation binding, resolves its exact multi-component closure, verifies artifact identities and trust, checks the current security/no-egress posture, establishes that every eligible Spark executor inherits the required role-specific closure, and creates one immutable Attempt invocation. Runtime receives only the exact data/state/dependency/write capabilities it needs; credentials are resolved at use time and are not persisted in the invocation. If a worker lacks a native dependency, the Attempt does not let that worker download it from the Internet. If the Attempt later fails and another compatible binding is selected for retry, the new Attempt receives a new exact invocation and historical realization record while the original semantic Generation commitment remains unchanged.
