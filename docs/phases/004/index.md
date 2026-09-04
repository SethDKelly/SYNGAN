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
| **004-H** | **Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture** | **next** |
| 004-I | Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture | planned |
| 004-J | Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit | planned |

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

Established [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](../../architecture/evaluation-evidence-provenance-reproducibility-historical-query.md).

Key accepted rules include:

- Evaluation runtime results remain non-final until owner-side semantic validation establishes interpretable Evidence;
- one Evaluation may establish multiple independently interpretable Evidence resources through idempotent logical finding slots;
- Evidence finding semantics are immutable while current applicability is separately conflict-versioned;
- Evidence preserves typed findings, claim support, uncertainty/limitations, and stable diagnostic references rather than a universal scalar Quality/Pass value;
- Generation promotion retains the exact candidate/requirement/Criterion/Evidence completion basis used historically;
- canonical Provenance is a typed stable-reference assertion layer and does not duplicate canonical concept/result payloads;
- Provenance recording is idempotent and recoverably coupled to material transitions that require traceability;
- Provenance corrections are append/supersede and cannot mutate another concept's historical authority;
- historical explain/traverse/compare capabilities are read-composition services over canonical resources/Provenance plus rebuildable derived indexes;
- derived query projections may be eventually consistent but remain non-authoritative;
- historical comparison reports structural differences without inventing causality, quality, or superiority;
- reproducibility is assembled as a current qualified assessment over exact historical facts, dependencies, implementation/runtime identities, randomness/approximation, representation equivalence, and material recovery facts;
- the strongest supportable reproduction class cannot exceed the weakest unresolved material boundary;
- reproduction readiness remains distinct from actual reproduction success through new domain work;
- historical facts, current lifecycle/applicability, current availability, disclosure state, and current reproducibility remain distinct;
- `absent`, `unknown`, `unavailable`, `withheld`, `invalid`, and corrected/superseded states remain distinguishable;
- external lineage/catalog systems remain integrations rather than canonical semantic authority;
- Evidence/Provenance/history/query state remains bounded and does not require full row/model/diagnostic/task/log collection.

Decision: [ADR-0006 — Typed Canonical Provenance & Derived Historical Projections](../../decisions/ADR-0006-typed-provenance-canonical-derived-history-projections.md).

## Phase 004 guardrails

Phase 004 MUST NOT:

- redesign accepted concept semantics for package/runtime convenience;
- erase typed semantic/operational distinctions behind generic status/session/plugin/result/metadata objects;
- make one runtime/platform/database/graph technology mandatory unless semantics require it;
- require ordinary full driver-local source/output/Learned-State/diagnostic/telemetry materialization;
- make dependency/network/resource acquisition implicit;
- treat runtime success, file existence, manifest sealing, checkpoint durability, plugin output, or query-index state as semantic promotion;
- equate platform retry/exactly-once claims with SYNGAN semantic authority;
- allow stale Attempts to mutate current framework-owned state after supersession;
- use lease expiry or last-writer-wins as sole protection for material authority;
- assume unknown external effects failed merely to permit retry;
- permit runtime/platform/lineage adapters to rewrite committed semantics or canonical Provenance/results directly;
- duplicate canonical concept payloads into a master metadata graph;
- store reproducibility as unqualified global Boolean truth;
- infer causal/quality conclusions from historical differences without Evidence;
- jump into implementation task breakdown before Phase 004 architecture is complete.

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

**004-H — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture**
