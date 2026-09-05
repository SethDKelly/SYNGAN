---
type: Architecture Authority
title: Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture
status: active
---

# Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture

## Purpose

Define how SYNGAN's accepted semantic, control-plane, distributed-data, runtime, recovery, Evidence/Provenance and security architecture can be deployed across local development, generic/self-managed Spark environments, managed Spark platforms, and enterprise private/offline environments without allowing any one platform to become semantic authority.

This document establishes the canonical Phase 004-I architecture for:

- deployable logical roles and failure domains;
- control-plane and data/runtime-plane placement;
- platform capability discovery and negotiation;
- distributed scaling and admission/resource boundaries;
- observability, telemetry, audit and correlation;
- portability and platform-specialization rules;
- compatibility/version matrices and migration boundaries;
- managed-platform integration, including Databricks-oriented adapter roles;
- private/offline package, dependency and runtime distribution;
- deployment enforcement of 004-H identity, secret, network and egress constraints;
- degraded operation and platform capability loss.

It does **not** select a cloud, container orchestrator, database engine, Spark distribution, scheduler, object/table storage provider, query engine, observability vendor, IAM provider, Databricks deployment topology, CI/CD product, package repository, or exact Python package/module layout.

## Governing authority

This architecture remains downstream of:

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md);
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](public-api-resource-handle-workflow-semantic-mapping.md);
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md);
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md);
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](strategy-extension-learning-generation-evaluation-runtime-adapter.md);
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md);
- [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](evaluation-evidence-provenance-reproducibility-historical-query.md);
- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md);
- [Enterprise Scale Envelope](../problem/enterprise-scale-envelope.md).

## Primary decision

SYNGAN SHALL use a **portable contract core with capability-negotiated platform adapters**.

Conceptually:

```text
SYNGAN semantic / application / control contracts
                    ↓
          required capability contract
                    ↓
       deployment capability negotiation
          ┌─────────┼─────────┐
          ↓         ↓         ↓
   generic Spark  managed    local/private
      adapters     platform    adapters
                    adapters
          ↓         ↓         ↓
 storage / runtime / identity / network / observability
```

A platform adapter may optimize realization, expose native references, or add optional capabilities. It MUST NOT redefine Learning, Generation, Evaluation, Evidence, Execution, Provenance, promotion, dependency, authorization, or reproducibility semantics.

The architecture therefore adopts the rule:

> **Platform identity is not a semantic capability. SYNGAN binds to explicit guarantees; when a required guarantee is unavailable it must use a semantics-preserving fallback or report incompatibility rather than silently weaken the contract.**

## Logical deployment roles

The architecture defines logical roles rather than mandatory processes/services. Several roles may run in one process for development or be separated/horizontally scaled in enterprise deployments.

### Client / public API role

Provides user/programmatic interaction through typed handles/specifications from 004-B.

It may run in:

- a notebook;
- a Python application;
- a service/API process;
- a CLI;
- another authorized client.

The client is not canonical durable state. Losing the client MUST NOT lose committed activity/resource identity.

### Application/control coordinator role

Owns application-level orchestration of:

- readiness/commitment;
- control-plane transitions;
- dependency/security checks;
- Execution/Attempt creation;
- runtime invocation composition;
- result validation/promotion;
- Evidence establishment;
- required Provenance recording;
- reconciliation.

This role may be stateless or restartable with respect to durable owner repositories. In-memory coordinator state MUST NOT be required to reconstruct committed authority after process loss.

### Canonical control persistence role

Persists the bounded owner state accepted in 004-C, including exact revisions/commitment snapshots, lifecycle state, Execution/Attempt records, Evidence, Provenance assertions and other bounded reference/state records.

One physical database may serve multiple logical owners, but shared technology does not merge semantic ownership.

### Projection/query role

Builds and serves derived indexes/read models used for search, explain, comparison and other efficient queries.

These projections may scale independently and may be eventually consistent under 004-G. They are rebuildable and non-authoritative.

### Distributed data/state storage role

Stores or references potentially large source snapshots, candidate/output data, Learned State components, checkpoints, Evaluation diagnostics, manifest/index structures and other data-plane material.

This role may be supplied by platform-native tables, files/object storage, distributed state stores or other compliant providers.

### Execution launcher / runtime integration role

Maps one immutable Attempt invocation to platform/runtime work, such as Spark jobs, managed jobs, distributed ML runtimes or local execution.

It preserves the 004-F distinction between SYNGAN Execution/Attempt identity and platform job/process identity.

### Security/identity integration role

Supplies authenticated principal/workload identity, current authorization decisions, scoped capabilities, secret delegation and relevant network/egress enforcement interfaces under 004-H.

### Observability integration role

Exports or exposes permitted operational telemetry without becoming canonical semantic state.

## Deployment composition profiles

Profiles are architecture compositions, not products or separate semantic modes.

### Development / single-process profile

May colocate client, coordinator, local control persistence, local data references and runtime adapters for convenience.

It MUST preserve the same identity, commitment, promotion and semantic/operational distinctions as distributed deployment. Development convenience must not introduce alternate semantics such as process-local handles as canonical identity.

### Portable Spark profile

Uses a Spark-capable distributed data boundary with platform-neutral control/runtime interfaces.

The profile may rely on generic catalog/table/file/runtime adapters while keeping optional managed-platform features absent.

### Managed-platform profile

Uses platform-native capabilities where they satisfy accepted contracts, for example native versioned data references, job launch, workload identity, secret delivery, catalog integration, observability links or managed storage.

Native capabilities are mapped through adapters and remain subordinate to SYNGAN identity and authority.

### Private/offline/no-egress profile

Uses locally provisioned packages/dependencies and deployment controls that do not require outbound network for supported core workflows.

Remote observability, package resolution, model acquisition, telemetry and hosted services MUST be optional/replaceable or disabled in this profile.

### Hybrid profile

A deployment may combine a durable shared control plane with multiple runtime environments or security domains. Cross-boundary data/dependency movement remains subject to 004-H authorization/egress rules and exact reference compatibility.

## Platform capability model

### Capability descriptors

A platform/environment adapter SHALL be able to describe relevant capabilities and limitations in a machine-inspectable form or equivalent bounded contract.

Capability dimensions may include:

- exact immutable/versioned source read support;
- distributed dataset read/write support;
- candidate/staging isolation;
- atomic/conditional metadata mutation;
- fencing/CAS/lease primitives;
- immutable checkpoint/snapshot representation support;
- workload launch/reconciliation support;
- provider idempotency/correlation support;
- workload/service identity;
- scoped storage/data authorization;
- secret delegation;
- outbound-network and egress enforcement;
- local/offline package/artifact resolution;
- accelerator/GPU/runtime availability;
- distributed model-state loading;
- query/index capability;
- observability/log/metric/trace integration;
- native lineage/catalog references;
- retained historical version resolution;
- retention/cleanup controls.

A capability descriptor describes technical guarantees. It does not grant semantic compatibility or authorization by itself.

### Required versus optional capabilities

The application/runtime binding evaluates required capabilities for the exact activity.

For example:

```text
Generation G42 requires:
- stable source/state references
- distributed candidate writer
- stale-writer fencing
- no runtime network

Environment P7 provides:
- native stable snapshots ✓
- distributed writer ✓
- conditional-write fence ✓
- outbound network disabled ✓

Deployment compatibility: supported
```

Another Strategy may require accelerator or remote-service capability and be incompatible in the same environment.

### Capability negotiation

Negotiation SHALL produce a contextual result equivalent to:

- supported directly;
- supported through an explicit semantics-preserving fallback;
- supported with declared limitations compatible with the commitment;
- incompatible;
- indeterminate because capability cannot be established.

The negotiation result is contextual deployment/readiness state rather than a new domain concept.

### Fallbacks must preserve semantics

Examples of legitimate fallback include:

- platform lacks native immutable source versioning -> materialize an explicit distributed snapshot under 004-D;
- platform lacks a native provenance query graph -> use canonical typed relationship persistence plus derived indexes under 004-G;
- platform lacks native job idempotency -> use durable submission intent/correlation/reconciliation under 004-F.

A fallback is invalid if it weakens the semantic contract silently, for example:

- using a mutable table alias when exact historical binding is required;
- dropping Attempt fencing because the scheduler retries jobs;
- collecting the full enterprise dataset to the driver because a model adapter lacks distributed ingestion;
- enabling remote inference because local acceleration is unavailable;
- exposing unrestricted worker network because scoped egress is difficult.

## Control-plane deployment architecture

### Durable-state-first coordination

Coordinators MUST be restartable from canonical durable state and platform correlations.

A compliant deployment therefore avoids correctness dependence on:

- one immortal notebook kernel;
- one process-local session object;
- one in-memory task map;
- one driver holding all mutable lifecycle state.

### Horizontal coordination

Multiple coordinator/service replicas MAY operate concurrently if material mutations use the owner-specific state-version/idempotency/fencing rules established by 004-C and 004-F.

Horizontal scale MUST NOT rely on last-writer-wins.

### Projection independence

Search/history/query projections MAY scale and fail independently of canonical control persistence.

Projection outage may degrade convenience/history query performance while preserving canonical workflow authority, unless a particular operation explicitly requires a canonical historical verification that cannot currently be performed.

### Control-plane boundedness

Control-plane memory/storage/traffic should scale primarily with resources, revisions, activities, Attempts, Evidence findings, Provenance assertions, dependency/security references and query indexes—not source/generated row count or full model parameter volume.

Large payload movement SHOULD bypass the coordinator when safe and use distributed references/capabilities.

## Distributed scalability architecture

### Scale is strategy- and operation-specific

The platform layer MUST expose material runtime limits rather than advertising a generic row-count capability.

Relevant dimensions include:

- row count/data bytes;
- width;
- categorical cardinality;
- skew/partition imbalance;
- source/output partition count;
- model/Learned State size;
- worker/accelerator memory;
- shuffle/network volume;
- Evaluation coverage cost;
- concurrent workload count;
- external dependency throughput/rate limits.

### No hidden single-node boundary

An implementation binding advertised for enterprise-scale workloads MUST disclose any stage whose state/work requires one process/driver to hold source-size-proportional material.

Ordinary core enterprise paths MUST NOT require full source/output/Learned State/diagnostic payload materialization in driver memory.

### Bounded coordinator exchange

Runtime adapters SHOULD exchange bounded summaries/references with control-plane services while bulk data flows through distributed data/storage/runtime boundaries.

Examples:

```text
runtime -> candidate manifest/reference
runtime -> checkpoint reference
runtime -> bounded progress summary
runtime -> Evaluation aggregate + diagnostic reference
```

rather than full rows/tensors/diagnostic datasets.

### Admission and resource envelope

A deployment MAY provide admission control, quotas, queues, concurrency limits, resource classes and scheduling policies.

The architecture requires that resource/admission failure remain operational/deployment state and not be misreported as semantic incompatibility unless the committed Strategy/runtime truly cannot be realized under available resources.

### Backpressure

Control-plane/event/projection integrations SHOULD tolerate high Attempt/progress/telemetry volume through batching, sampling, rate limiting or bounded queues without dropping canonical material transitions silently.

Low-level telemetry may be lossy where appropriate; canonical Execution/Evidence/Provenance transitions may not be lost merely because telemetry is overloaded.

## Failure-domain architecture

The deployment SHALL distinguish failure domains sufficiently to avoid converting every outage into the same semantic outcome.

Relevant failure domains include:

- client/notebook loss;
- coordinator/service loss;
- canonical control persistence loss/unavailability;
- projection/index lag/outage;
- Spark/runtime cluster loss;
- worker/accelerator failure;
- distributed storage/catalog outage;
- dependency/artifact repository outage;
- policy/identity/secret provider outage;
- remote dependency outage;
- observability backend outage;
- network partition.

### Canonical persistence outage

If canonical mutation cannot be durably recorded, semantic transitions that require durable authority MUST NOT be optimistically declared complete.

### Projection outage

A projection outage does not by itself invalidate canonical state. Query/read surfaces may report degraded or stale status.

### Observability outage

Loss of optional telemetry does not automatically fail a domain activity when canonical operational state can still be maintained, but audit/security/trace obligations that are mandatory for the activity may make the action incompatible or blocked.

### Control-plane/runtime partition

Runtime work may continue physically during a partition, but canonical authority and subsequent recovery follow 004-F fencing/reconciliation rules. The coordinator must not assume failure merely because it cannot currently observe the platform.

## Observability architecture

### Three distinct observability/history lanes

SYNGAN SHALL keep at least three logically distinct information lanes:

1. **canonical semantic/operational history** — bounded owner state, Execution/Attempts, Evidence, Provenance and material transitions;
2. **platform/runtime observability** — logs, metrics, traces, Spark/runtime events, resource utilization and detailed diagnostics;
3. **security audit** — authentication/authorization/secret/egress/privileged-access events as governed by 004-H.

These systems may correlate with one another but do not replace one another.

### Correlation context

Where permitted, telemetry SHOULD carry stable correlation references such as:

```text
activity_id
execution_id
attempt_id
attempt_epoch
runtime/platform correlation
candidate/checkpoint reference
implementation binding
```

Sensitive resource/dependency/principal identifiers may require hashed/redacted/opaque correlation according to policy.

### Metrics

Operational metrics may include bounded indicators such as:

- activity/Execution/Attempt counts by operational state;
- runtime duration;
- retry/recovery/cancellation counts;
- candidate/checkpoint write volumes;
- platform queue/launch latency;
- resource utilization;
- control-store/projection latency/error rates;
- dependency-resolution failures;
- security/egress denial counts where policy permits.

Metrics do not become Evidence or semantic completion authority.

### Logs

Logs SHOULD be structured enough to correlate material operational events while excluding secrets and avoiding unnecessary source/synthetic/sensitive diagnostic payloads.

A log message is not canonical state merely because it records a transition attempt.

### Traces

Distributed traces MAY connect client -> coordinator -> dependency/security checks -> launcher -> runtime -> storage/query integration.

Trace IDs are diagnostic correlation, not resource identity.

### Progress

Platform/runtime progress remains operational and method-specific. It MUST NOT be automatically converted into semantic completion percentage.

### Offline observability

Core supported offline/no-egress deployments MUST be able to operate with local/in-boundary observability or no optional external telemetry.

External telemetry exporters MUST NOT be a hidden runtime dependency.

## Retention and cleanup architecture

### Retention classes remain distinguishable

Deployment may apply different retention to:

- canonical control history;
- source/output/Learned State payloads;
- checkpoints/candidates/scratch state;
- Evidence diagnostics;
- query projections;
- platform telemetry;
- security audit.

Deleting one category does not imply deletion of every related canonical identity/reference.

### Cleanup is authority-aware

Garbage collection of Attempt scratch, abandoned candidates and obsolete checkpoints MUST respect current Attempt fencing, retained history, investigation needs and security policy.

A cleanup process cannot remove material still needed by a sealed/promoted representation, valid checkpoint, required Evidence diagnostic reference, or retained reproducibility contract without recording resulting unavailability/retention effects appropriately.

### Tombstone/history interaction

If payload retention expires while historical identity remains required, 004-C tombstone/reference semantics apply: history may remain resolvable as `identity known / payload unavailable` rather than being fabricated as absent.

## Portability architecture

### Portable semantic/control core

Core semantic, application and control contracts MUST NOT require importing or directly depending on one managed-platform SDK.

Platform-specific implementations depend inward on stable ports/contracts.

### Portable public identity

SYNGAN resource identity remains portable across clients and runtime teardown. Platform-native identifiers may be retained as external references but are not the sole identity of domain resources.

### Portability levels

Architecture SHOULD permit deployment/runtime bindings to declare portability characteristics such as:

- portable semantic state and representation;
- portable semantics with representation conversion required;
- portable control identity but platform-bound data representation;
- platform-bound runtime capability;
- non-portable because dependency/service behavior cannot be reproduced elsewhere.

These are capability/compatibility descriptors, not a new concept taxonomy.

### Platform migration

Moving a retained SYNGAN resource between environments must preserve or explicitly re-establish:

- logical identity;
- semantic revision/commitment snapshot;
- representation equivalence/integrity where identity is retained;
- Provenance/history;
- security-domain authorization;
- dependency/runtime compatibility;
- current availability and reproducibility limitations.

Copying bytes to another platform does not by itself prove equivalent representation or authorize use.

### Platform-specific enhancement

A managed adapter MAY expose useful native links/references or optimized implementations, but canonical APIs should retain a platform-neutral path to the same semantic information where feasible.

Users should not need to understand native job IDs/table-history internals merely to determine SYNGAN semantic state.

## Compatibility architecture

### No single package `version` is sufficient

Compatibility spans multiple independent axes already established by Phase 004.

A deployment/runtime compatibility matrix may need to consider:

- SYNGAN public API/package version;
- canonical persistence schema version;
- resource/wire serialization schema version;
- Strategy semantic revision/configuration schema;
- implementation-binding revision;
- extension/SPI version;
- Learned State representation/codec version;
- manifest/checkpoint representation version;
- Provenance assertion schema version;
- Spark/runtime version;
- Python/runtime version;
- accelerator/runtime library versions;
- platform adapter version;
- storage/catalog provider version;
- external dependency/service behavior version.

These axes MUST NOT be collapsed into one global `compatible=true` without reasons/limitations.

### Compatibility negotiation

At startup, binding selection, state load, retry/resume, source resolution or migration, the relevant adapter SHOULD evaluate the exact compatibility axes needed for the action.

Outcomes remain explainable:

- compatible;
- compatible with declared limitations;
- migration/conversion required;
- incompatible;
- indeterminate.

### Backward readability and migration

Future implementation SHOULD define supported compatibility windows for persisted canonical state, manifests, checkpoints, Learned State codecs and public wire/resource schemas.

Migration must preserve 004-C identity/history rules and must not silently reinterpret old semantic state under new code.

A storage-schema migration is not a domain revision.

### Rolling upgrades

A distributed deployment may temporarily run mixed service/runtime versions. Material interfaces therefore need explicit protocol/schema compatibility rules rather than assuming every component upgrades atomically.

An old worker/runtime MUST NOT write state it cannot represent safely under the current owner schema/fence.

### Strategy/plugin upgrade

Installing a new implementation version does not retroactively change historical work or current Learned State compatibility. Binding selection remains explicit/contextual under 004-E.

## Databricks-oriented integration boundary

Databricks is an important target managed Spark environment, but it is an adapter/integration target rather than package identity.

A Databricks-oriented implementation may map portable ports to managed capabilities such as:

- Spark DataFrame/session access;
- versioned/catalognative data references where sufficient;
- platform job/task launch and correlation;
- workload/service identity;
- managed secret resolution;
- storage/catalog authorization;
- platform-native logs/metrics/job links;
- optional lineage/ML lifecycle integrations;
- accelerator/runtime selection;
- private networking and enterprise egress controls.

The exact Databricks services/APIs are intentionally not fixed in Phase 004-I.

### Native identity remains external reference

A Databricks job/run/task/table/model/catalog identifier may be stored as a platform correlation/reference. It does not replace SYNGAN Execution, Attempt, source-state, Learned State, output, Evidence or Provenance identity.

### Native retries remain subordinate

Databricks/platform-native retries/speculation/resubmission remain physical realization. SYNGAN Attempt identity/fencing/idempotency rules still govern canonical side effects.

### Native data versioning capability

If a managed platform supplies a historical immutable/versioned data reference strong enough for 004-D exact binding, the adapter may use it directly. Otherwise SYNGAN must create a stronger snapshot/manifest representation or declare the workflow unsupported at the required strength.

### Native lineage/ML metadata

Platform lineage or ML metadata can enrich navigation and observability, but canonical SYNGAN Provenance/Evidence remains governed by 004-G.

### Managed access controls

Platform catalog/storage/identity controls may enforce 004-H capabilities. Their presence does not remove the need for action-specific SYNGAN authorization and scoped runtime invocation.

## Generic Spark integration boundary

SYNGAN SHALL remain deployable in Spark environments that do not provide managed-platform-specific services, provided required capabilities can be supplied through portable adapters.

Generic integration may need explicit implementations for:

- exact source-state snapshot/reference;
- distributed candidate/output storage;
- manifest/index persistence;
- platform submission/correlation;
- fencing/idempotency primitives;
- secret/security integration;
- local/offline dependency resolution;
- observability links.

A missing managed service is not inherently incompatibility if a portable semantics-preserving implementation exists.

## Optional non-Spark runtime integration

Spark remains the structured-data boundary/design center, but model runtimes may be non-Spark under 004-E.

Platform integration must therefore support patterns where:

```text
Spark/distributed source reference
        ↓ bounded/distributed bridge
PyTorch/distributed or other runtime
        ↓
Learned State / candidate sink
        ↓
Spark-readable distributed output/reference
```

The bridge must not collapse enterprise data into ordinary single-driver pandas/local memory unless the Strategy explicitly declares a bounded/local mode compatible with the requested workload.

## Offline/private distribution architecture

Supported private deployments SHOULD be able to provision:

- SYNGAN package distributions;
- extension/plugin packages;
- Strategy/runtime artifacts;
- pretrained/base dependencies;
- schema/migration assets;

through approved local/private repositories or prebuilt images/environments.

Runtime dependency discovery MUST work without public registry access when the deployment profile requires it.

Package/version metadata needed for reproducibility should remain inspectable without contacting a public service.

## Security deployment obligations

004-H security contracts require deployment enforcement beyond application checks where practical.

A compliant enterprise deployment SHOULD be capable of enforcing:

- workload/service identity boundaries;
- least-broad storage/catalog access;
- scoped secret retrieval;
- network/egress restriction;
- tenant/security-domain isolation;
- private dependency resolution;
- protected query/index access;
- encryption and credential protection appropriate to the environment;
- audit collection required by enterprise policy.

If a platform cannot enforce a required security property strongly enough—for example unrestricted worker internet when committed no-egress requires enforceable isolation—the adapter must surface the limitation/incompatibility rather than claiming the guarantee.

## Observability versus canonical history mapping

Adapters may expose native deep links such as platform job URLs, Spark UI/history references or trace/log correlation references.

These remain drill-down tools.

A future public inspection view should conceptually support:

```text
Generation G42
semantic state: awaiting validation
Execution EX9: operationally complete
Attempt A3: succeeded
platform reference: <native link>
```

without requiring the platform UI to determine the first two lines.

## Conformance and compatibility testing obligations

Later implementation planning SHALL include adapter/deployment conformance tests for material guarantees, including at least:

- exact source-reference binding or explicit fallback;
- candidate isolation/sealing/promotion behavior;
- stale Attempt fencing;
- duplicate launch/reconciliation behavior;
- checkpoint integrity/resume compatibility;
- bounded driver memory on declared enterprise-scale paths;
- dependency resolution without hidden network acquisition;
- offline/no-egress enforcement;
- scoped runtime identity/secret/data access;
- query/index authorization isolation;
- telemetry failure without canonical-state corruption;
- restart of clients/coordinators without losing durable activity identity;
- projection rebuild without changing canonical history;
- compatibility/version negotiation and migration;
- platform-native retry/lineage/metadata not overriding SYNGAN authority.

A platform adapter that cannot demonstrate a required guarantee MUST declare its limitation instead of being assumed conformant.

## No new domain-concept audit

004-I does not introduce standalone concepts for:

- Deployment;
- Platform;
- Environment;
- Capability;
- Compatibility Matrix;
- Runtime Profile;
- Cluster;
- Scheduler;
- Service;
- Telemetry;
- Metric;
- Trace;
- Log;
- Adapter;
- Migration;
- Portability;
- Resource Class;
- Admission Control.

These remain architecture/deployment/integration mechanisms downstream of accepted concept ownership.

## Architecture invariants established by 004-I

1. Platform adapters depend on SYNGAN contracts; semantic/core authority does not depend on one platform SDK.
2. Platform-native identities remain external references and do not replace SYNGAN resource identities.
3. Platform capability must be explicit enough to determine whether required guarantees can be met.
4. Missing capability causes explicit fallback, limitation, incompatibility or indeterminacy—not silent semantic weakening.
5. Development/single-process deployment preserves the same semantic distinctions as distributed deployment.
6. Client/coordinator loss does not erase committed activity identity or canonical state.
7. Canonical control state remains bounded relative to bulk source/output/model/diagnostic payloads.
8. Enterprise-scale paths do not require ordinary full source/output/Learned-State materialization to driver memory.
9. Resource/scale limits are Strategy/runtime/workload specific rather than a generic row-count promise.
10. Projection/index/observability failure does not rewrite canonical state.
11. Canonical semantic/operational history, platform telemetry and security audit remain distinct authorities.
12. Telemetry IDs are correlation, not domain identity.
13. Optional external telemetry cannot be required by supported offline/no-egress core workflows.
14. Security guarantees required by commitment must be enforceable by deployment capability or reported as unsupported.
15. Managed-platform specialization may optimize or enrich but cannot weaken shared semantic/recovery/security guarantees.
16. Generic/self-managed Spark remains a legitimate deployment target when required capabilities are supplied.
17. Non-Spark model runtimes remain valid behind scale-compatible distributed data/state bridges.
18. Compatibility remains multi-axis and explainable; one generic package `version` cannot stand for all compatibility.
19. Schema/representation migration does not create or rewrite domain history unless semantic state actually changes.
20. Mixed/rolling component versions require explicit protocol/schema compatibility and cannot rely on atomic whole-system upgrade.
21. Native scheduler retries, lineage, model registries and catalogs remain subordinate integrations rather than canonical authority.
22. Private/offline dependency/package provisioning remains possible without public-network lookup during supported runtime work.
23. Cleanup/retention cannot silently destroy still-authoritative result/history/reproducibility state.
24. No platform integration may introduce a permanent single-table, Databricks-only, Spark-ML-only, PyTorch-only or cloud-only assumption into SYNGAN semantics.

## Representation and technology decisions intentionally deferred

004-I does not decide:

- exact service/process topology;
- Kubernetes or another orchestrator;
- serverless versus long-lived services;
- Postgres/Delta/graph/document/control-store choice;
- Delta/Iceberg/Hudi/file-provider choice;
- Databricks Jobs/Workflows/Connect/Asset Bundles or another exact API;
- Unity Catalog or another authorization/catalog technology;
- MLflow/OpenLineage/OpenTelemetry integration details;
- Prometheus/vendor observability stack;
- cloud/on-prem IAM technology;
- container/image/package build/distribution system;
- CI/CD topology;
- autoscaling algorithm;
- SLO/SLA values;
- benchmark methodology or supported row-count claims;
- supported Spark/Python/platform version matrix values.

Those choices belong to implementation planning and explicit later decisions while remaining constrained by this architecture.

## Phase 004-I exit conclusion

The deployment/platform architecture is sufficiently defined for cross-architecture consolidation.

004-J should now verify that 004-A through 004-I compose without contradiction, consolidate the accepted architecture baseline and ADR set, identify any unresolved implementation-decision register, and determine whether Phase 004 can exit into implementation planning without reopening concept or experience authority.
