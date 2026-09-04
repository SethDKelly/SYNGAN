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

## Groups

| Group | Scope | Status |
|---|---|---|
| **004-A** | [**Architecture Authority, Representation Principles, Layering & Dependency Direction**](004-A-architecture-authority-representation-layering-dependency-direction.md) | **complete** |
| **004-B** | [**Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping**](004-B-public-api-resource-handle-workflow-semantic-mapping.md) | **complete** |
| **004-C** | [**Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture**](004-C-control-plane-identity-revision-state-persistence-historical-reference-architecture.md) | **complete** |
| **004-D** | [**Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture**](004-D-spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion-architecture.md) | **complete** |
| **004-E** | [**Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture**](004-E-strategy-extension-learning-generation-evaluation-runtime-adapter-architecture.md) | **complete** |
| **004-F** | [**Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture**](004-F-execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-architecture.md) | **complete** |
| **004-G** | **Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture** | **next** |
| 004-H | Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture | planned |
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

Established [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](../../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md).

Key accepted rules include:

- one stable logical Execution spans many valid Attempts/platform submissions;
- each write-capable Attempt receives a supersedable ordered epoch/fencing generation;
- only the current epoch may mutate framework-owned current candidate/checkpoint/control state;
- leases support liveness but do not replace fencing;
- duplicate physical work and overlapping stale processes may exist while stale canonical writes are rejected/isolated;
- Attempt runtime invocation remains immutable and same-semantics;
- platform submission is correlation/idempotency/reconciliation aware across crash windows;
- idempotency is scoped to Attempt launch, checkpoint commit, candidate mutation/seal, Evaluation aggregation, semantic promotion, cancellation, and other material operations rather than one global key;
- committed checkpoints are immutable recovery snapshots with exact activity/runtime/dependency context;
- resume eligibility is contextual and distinct from checkpoint existence;
- recovery explicitly chooses retry-from-start, resume, reconcile-first, or cannot-continue;
- unknown platform/side-effect state remains durable until safely reconciled/fenced;
- external effects that cannot be fenced/query/deduplicated may block automatic retry;
- candidate sealing requires resolved writer authority and is idempotent for an exact manifest generation;
- semantic promotion remains owner-side and at-most-once in authority;
- Evaluation retries cannot accidentally double-count logical work units;
- cancellation is durable intent followed by reconciled outcome and cannot erase prior authority;
- automatic retry obeys the same semantic/dependency/no-egress/cancellation safety checks as manual retry;
- canonical Execution state remains bounded rather than duplicating all platform telemetry.

Decision: [ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution](../../decisions/ADR-0005-attempt-epoch-fencing-recoverable-at-least-once-execution.md).

## Phase 004 guardrails

Phase 004 MUST NOT:

- redesign accepted concept semantics for package/runtime convenience;
- erase typed semantic/operational distinctions behind generic status/session/plugin/result objects;
- make one runtime/platform mandatory unless semantics require it;
- require ordinary full driver-local source/output/Learned-State/diagnostic materialization;
- make dependency/network/resource acquisition implicit;
- treat runtime success, file existence, manifest sealing, checkpoint durability, or plugin output as semantic promotion;
- equate platform retry/exactly-once claims with SYNGAN semantic authority;
- allow stale Attempts to mutate current framework-owned state after supersession;
- use lease expiry or last-writer-wins as the sole protection for material authority;
- assume unknown external effects failed merely to permit retry;
- permit runtime/platform adapters to rewrite committed semantics or create semantic results directly;
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

**004-G — Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture**
