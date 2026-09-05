---
type: Phase Index
title: Phase 004 — Representation & Architecture Design
status: active
---

# Phase 004 — Representation & Architecture Design

Phase 004 translates SYNGAN's accepted concept, synchronization, and experience contracts into implementation-facing architecture without allowing representation convenience to redefine semantic ownership.

## Entry authority

- [Design Authority](../../authority/index.md)
- [Accepted Concepts](../../concepts/index.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Experience & Workflow Design](../../experience/index.md)
- [Phase 003 Consolidated Experience Contract](../../experience/phase-003-consolidated-experience-contract.md)
- [Architecture Authority](../../architecture/index.md)
- [004-A Architecture Constitution](../../architecture/architecture-authority-representation-layering.md)
- [004-B Public API/Resource Architecture](../../architecture/public-api-resource-handle-workflow-semantic-mapping.md)
- [004-C Control-Plane Identity/State Architecture](../../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)
- [004-D Spark Data Boundary/Manifest/Promotion Architecture](../../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md)
- [004-E Strategy Extension/Runtime Adapter Architecture](../../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md)
- [004-F Execution/Recovery Architecture](../../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md)
- [004-G Evaluation/Evidence/Provenance/Reproducibility Architecture](../../architecture/evaluation-evidence-provenance-reproducibility-historical-query.md)
- [004-H Dependency/Security Architecture](../../architecture/dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md)
- [004-I Deployment/Platform Architecture](../../architecture/deployment-scalability-observability-portability-compatibility-platform-integration.md)

## Groups

| Group | Scope | Status |
|---|---|---|
| **004-A** | [**Architecture Authority, Representation Principles, Layering & Dependency Direction**](004-A-architecture-authority-representation-layering-dependency-direction.md) | **complete** |
| **004-B** | [**Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping**](004-B-public-api-resource-handle-workflow-semantic-mapping.md) | **complete** |
| **004-C** | [**Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture**](004-C-control-plane-identity-revision-state-persistence-historical-reference-architecture.md) | **complete** |
| **004-D** | [**Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture**](004-D-spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion-architecture.md) | **complete** |
| **004-E** | [**Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture**](004-E-strategy-extension-learning-generation-evaluation-runtime-adapter-architecture.md) | **complete** |
| **004-F** | [**Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture**](004-F-execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-architecture.md) | **complete** |
| **004-G** | [**Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture**](004-G-evaluation-evidence-provenance-reproducibility-historical-query-architecture.md) | **complete** |
| **004-H** | [**Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture**](004-H-dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security-architecture.md) | **complete** |
| **004-I** | [**Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture**](004-I-deployment-scalability-observability-portability-compatibility-platform-integration-architecture.md) | **complete** |
| **004-J** | **Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit** | **next** |

## Completed architecture refinement

### 004-A — Architecture constitution

Established downstream architecture authority, semantic-preserving representation, control/data-plane separation, inward dependencies, platform adapter isolation, Spark-native/model-neutral boundaries, anti-god-module rules, and ADR discipline.

### 004-B — Public resource model

Established editable specifications, contextual readiness, durable committed activity handles, promoted result handles, subordinate non-final material, independent Execution/Attempt inspection, long-running re-resolution, explicit payload access, and convenience façades without canonical state ownership.

Decision: [ADR-0001 — Typed Resource/Handle Public API](../../decisions/ADR-0001-typed-resource-handle-public-api.md).

### 004-C — Control-plane identity/state/persistence

Established stable resource identity, immutable semantic revisions/commitment snapshots, conflict-versioned mutable lifecycle state, representation schema versioning, exact historical reference resolution, logical persistence ownership, and recoverable coupled-transition consistency.

Decision: [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](../../decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md).

### 004-D — Spark data boundary/materialization/promotion

Established exact source-state/read binding, distributed/bounded manifest architecture, open-to-sealed candidate materialization, exact completion-Evaluation subject binding, stale-writer fencing obligations, and one idempotently promoted logical output without mandatory row copying or exactly-once physical execution.

Decision: [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](../../decisions/ADR-0003-sealed-manifest-gated-output-promotion.md).

### 004-E — Strategy extension/runtime adapters

Established semantic Strategy/method authority separate from executable bindings; immutable Attempt-scoped runtime invocation; typed Learning/Generation/Evaluation runtime boundaries; distributed Learned State loading; framework-owned candidate sinks; Evaluation method result envelopes; and no hidden dependency/network fallback.

Decision: [ADR-0004 — Semantic Extension & Runtime Binding Separation](../../decisions/ADR-0004-semantic-extension-runtime-binding-separation.md).

### 004-F — Execution/recovery/fencing

Established one stable logical Execution across valid Attempts; ordered Attempt epochs/fencing generations; lease-versus-fence separation; scoped idempotency; immutable checkpoint snapshots and contextual resume qualification; explicit retry/restart/reconcile decisions; durable unknown-state semantics; safe candidate sealing/promotion preconditions; Evaluation double-count protection; and cancellation as durable intent followed by reconciled outcome.

Decision: [ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution](../../decisions/ADR-0005-attempt-epoch-fencing-recoverable-at-least-once-execution.md).

### 004-G — Evaluation/Evidence, Provenance, reproducibility and historical query

Established semantic Evidence only after Evaluation validation; idempotent independently interpretable finding identities; immutable finding/current-applicability separation; exact Generation completion-Evidence basis; canonical typed Provenance over stable references; append/supersede correction; recoverable transition/provenance consistency; rebuildable historical query projections; bounded explain/compare traversal; difference-versus-causality separation; and qualified current reproducibility assessment.

Decision: [ADR-0006 — Typed Canonical Provenance & Derived Historical Projections](../../decisions/ADR-0006-typed-provenance-canonical-derived-history-projections.md).

### 004-H — Dependency resolution, offline/no-egress and enterprise security

Established explicit dependency requirement/resolution/integrity/trust/authorization distinctions; local/offline provisioning without hidden acquisition; typed network/egress behavior; action-oriented current authorization; non-bearing handles; scoped Attempt capabilities; secret isolation; truthful withholding/redaction; protected query projections; retry security revalidation; multi-security-domain isolation; and security-audit separation.

Decision: [ADR-0007 — Explicit Dependency Resolution & Scoped Capability Security](../../decisions/ADR-0007-explicit-dependency-resolution-scoped-capability-security.md).

### 004-I — Deployment, scalability, observability, portability, compatibility and platform integration

Established [Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture](../../architecture/deployment-scalability-observability-portability-compatibility-platform-integration.md).

Key accepted rules include:

- portable semantic/application/control contracts with capability-negotiated platform adapters;
- platform brand does not imply required guarantees and missing capability requires explicit fallback/limitation/incompatibility/indeterminacy;
- logical deployment roles can be colocated for development or separated/scaled in enterprise deployment without semantic changes;
- coordinators recover from durable canonical state and platform correlations rather than process-local sessions;
- canonical control state remains bounded while bulk source/output/Learned-State/checkpoint/diagnostic payloads remain distributed;
- scalability is Strategy/workload and multi-dimensional rather than a generic row-count promise;
- client, coordinator, persistence, projection, runtime, storage, dependency, security and observability failures remain distinguishable;
- canonical semantic/operational history, platform telemetry and security audit are distinct information lanes;
- logs/metrics/traces provide correlation/diagnosis and never become semantic completion authority;
- supported offline/no-egress profiles do not depend on public package/model lookup or optional external telemetry;
- platform-native identities remain external references rather than SYNGAN resource identity;
- Databricks is an important managed target but not package/semantic identity;
- Databricks/native retries, versioning, lineage, ML metadata, jobs, catalog/security and observability map through adapters and remain subordinate to SYNGAN authority;
- generic/self-managed Spark remains a legitimate target where required guarantees are supplied;
- non-Spark model runtimes remain valid behind scale-compatible distributed bridges;
- compatibility is multi-axis across API/schema, semantic revision, implementation binding, SPI, codecs, manifests/checkpoints, Spark/runtime/platform versions and dependencies;
- rolling/mixed component versions require explicit protocol/schema compatibility;
- private/offline package/plugin/dependency provisioning remains supported;
- deployment must be able to enforce required 004-H workload identity, storage, secret, network/egress, tenant and query/index security guarantees or report the limitation;
- retention/cleanup cannot silently destroy still-authoritative or historically required state.

Decision: [ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters](../../decisions/ADR-0008-portable-core-capability-negotiated-platform-adapters.md).

## Phase 004 guardrails

Phase 004 MUST NOT:

- redesign accepted concept semantics for package/runtime/security/platform convenience;
- erase typed semantic/operational/security distinctions behind generic status/session/plugin/result/metadata/security/platform objects;
- make one runtime/platform/database/graph/security/observability technology mandatory unless semantics require it;
- require ordinary full driver-local source/output/Learned-State/diagnostic/telemetry materialization;
- make dependency/network/resource acquisition implicit;
- treat runtime success, file existence, manifest sealing, checkpoint durability, plugin output, authorization grant, platform job state, telemetry or query-index state as semantic promotion;
- equate platform retry/exactly-once claims with SYNGAN semantic authority;
- allow stale Attempts to mutate current framework-owned state after supersession;
- use lease expiry, bearer-handle possession or last-writer-wins as sole protection for material authority;
- assume unknown external effects, authorization or platform capability states are safe merely to permit retry;
- permit runtime/platform/lineage/security/observability adapters to rewrite committed semantics or canonical Provenance/results directly;
- duplicate canonical concept payloads into a master metadata/security/platform graph;
- store reproducibility, security or compatibility as unqualified global Boolean truth;
- infer causal/quality conclusions from historical differences without Evidence;
- expose restricted historical facts through derived query/index paths;
- make managed-platform convenience a requirement for the portable semantic/core contract;
- jump into implementation task breakdown before 004-J completes the cross-architecture exit audit.

## Phase 004 exit target

Phase 004 should leave enough architecture authority that Phase 005 can map:

```text
concept / experience contract
        ↓
architecture boundary / interface
        ↓
module / implementation slice
        ↓
tests / acceptance evidence
```

without reopening core semantics.

## Current next phase

**004-J — Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit**
