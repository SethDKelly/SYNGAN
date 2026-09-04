---
type: Phase Index
title: Phase 004 — Representation & Architecture Design
status: active
---

# Phase 004 — Representation & Architecture Design

Phase 004 translates SYNGAN's accepted concept, synchronization, and experience contracts into coherent implementation-facing architecture without allowing representation convenience to redefine semantic ownership.

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

## Groups

| Group | Scope | Status |
|---|---|---|
| **004-A** | [**Architecture Authority, Representation Principles, Layering & Dependency Direction**](004-A-architecture-authority-representation-layering-dependency-direction.md) | **complete** |
| **004-B** | [**Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping**](004-B-public-api-resource-handle-workflow-semantic-mapping.md) | **complete** |
| **004-C** | [**Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture**](004-C-control-plane-identity-revision-state-persistence-historical-reference-architecture.md) | **complete** |
| **004-D** | [**Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture**](004-D-spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion-architecture.md) | **complete** |
| **004-E** | [**Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture**](004-E-strategy-extension-learning-generation-evaluation-runtime-adapter-architecture.md) | **complete** |
| **004-F** | **Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture** | **next** |
| 004-G | Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture | planned |
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

Established stable resource identity, immutable semantic revisions/commitment snapshots, conflict-versioned mutable lifecycle state, representation schema versioning, exact historical reference resolution, logical persistence ownership, and recoverable coupled-transition consistency without mandating one storage technology or universal event sourcing.

Decision: [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](../../decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md).

### 004-D — Spark data boundary/materialization/promotion

Established exact source-state/read binding, Spark DataFrame access-versus-identity separation, distributed/bounded manifest architecture, open-to-sealed candidate materialization, exact completion-Evaluation subject binding, stale-writer fencing obligations, and one idempotently promoted logical output without mandatory row copying or exactly-once physical execution.

Decision: [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](../../decisions/ADR-0003-sealed-manifest-gated-output-promotion.md).

### 004-E — Strategy extension/runtime adapters

Established [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md).

Key accepted rules include:

- semantic Strategy/method authority is separate from executable implementation binding and Attempt-scoped runtime realization;
- bindings identify exact supported semantic revisions plus package/runtime/SPI/state-codec/dependency/resource constraints;
- implementation bindings may narrow but cannot silently broaden Strategy capabilities;
- exact material implementation/runtime identity remains historically attributable when behavior/reproducibility depends on it;
- extension discovery/registration remains infrastructure rather than semantic authority and cannot trigger hidden runtime acquisition;
- runtime invocation is a bounded immutable representation of one committed activity/Attempt context;
- runtime adapters report facts and write non-final material through approved ports rather than mutating canonical semantic state directly;
- Learning adapters produce/seal candidate learned-state representation before Learning establishes the logical Learned State;
- Learned State identity remains separate from loaded PyTorch/Spark/statistical runtime objects and may remain distributed;
- direct Generation remains valid without fabricated Learning/Learned State;
- Generation adapters write only through 004-D candidate sinks and cannot promote output directly;
- Evaluation adapters bind exact subject/reference and return measurements/coverage/uncertainty/diagnostic facts rather than Evidence authority or generic pass/fail;
- platform jobs/processes remain subordinate to SYNGAN Execution/Attempt identity;
- Spark-native data semantics remain compatible with non-Spark model runtimes and prohibit ordinary full-corpus driver collection as a generic bridge;
- dependency/network/egress behavior remains explicit and missing resources cannot cause silent fallback/download;
- no Spark ML, PyTorch, CTGAN, Databricks, HuggingFace, LLM, plugin loader, or runtime family is made universal semantics.

Decision: [ADR-0004 — Semantic Extension & Runtime Binding Separation](../../decisions/ADR-0004-semantic-extension-runtime-binding-separation.md).

## Phase 004 guardrails

Phase 004 MUST NOT:

- redesign accepted concept semantics merely to simplify package/runtime structure;
- erase experience distinctions behind generic API/session/result/plugin objects;
- make one runtime/platform mandatory unless the semantic contract requires it;
- force ordinary enterprise source/output/Learned-State materialization to driver-local memory;
- make network/resource/package/model acquisition implicit;
- treat runtime/process success, physical storage existence, manifest sealing, or plugin output as semantic promotion;
- equate platform exactly-once claims with SYNGAN semantic promotion;
- turn Provenance into a shadow copy of all domain/runtime data;
- make security redaction falsify historical existence;
- create package dependency cycles merely because semantic synchronizations are bidirectional;
- make process-local object/Future/DataFrame/model identity the durable identity of work/results;
- collapse semantic revision, implementation version, lifecycle state version, SPI version, state-codec version, and storage schema version into one ambiguous field;
- use silent last-writer-wins for material authority;
- permit runtime adapters to rewrite committed semantics, create Evidence, establish Learned State, or publish completed output directly;
- allow completion Evaluation to bind mutable/open candidate state;
- require exactly-once computation or data copying merely to express finality;
- jump into implementation task breakdown before Phase 004 architecture is complete.

## Phase 004 exit target

Phase 004 should leave SYNGAN with enough accepted representation/architecture authority that Phase 005 can map:

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

**004-F — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture**
