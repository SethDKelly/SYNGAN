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

## Groups

| Group | Scope | Status |
|---|---|---|
| **004-A** | [**Architecture Authority, Representation Principles, Layering & Dependency Direction**](004-A-architecture-authority-representation-layering-dependency-direction.md) | **complete** |
| **004-B** | [**Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping**](004-B-public-api-resource-handle-workflow-semantic-mapping.md) | **complete** |
| **004-C** | [**Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture**](004-C-control-plane-identity-revision-state-persistence-historical-reference-architecture.md) | **complete** |
| **004-D** | [**Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture**](004-D-spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion-architecture.md) | **complete** |
| **004-E** | **Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture** | **next** |
| 004-F | Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture | planned |
| 004-G | Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture | planned |
| 004-H | Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture | planned |
| 004-I | Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture | planned |
| 004-J | Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit | planned |

## Completed architecture refinement

### 004-A

004-A established the canonical [Architecture Authority, Representation Principles, Layering & Dependency Direction](../../architecture/architecture-authority-representation-layering.md), including downstream architecture authority, bounded control/data-plane separation, inward dependencies, adapter isolation, Spark-native/model-neutral boundaries, anti-god-module rules, and ADR discipline.

### 004-B

004-B established [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../../architecture/public-api-resource-handle-workflow-semantic-mapping.md) and [ADR-0001 — Typed Resource/Handle Public API](../../decisions/ADR-0001-typed-resource-handle-public-api.md).

It accepts typed editable specifications, contextual readiness results, durable committed activity handles, promoted result handles, subordinate non-final descriptors, logical Execution/Attempt inspection, long-running re-resolution, explicit payload access, and convenience façades that do not own canonical state.

### 004-C

004-C established [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../../architecture/control-plane-identity-revision-state-persistence-historical-reference.md) and [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](../../decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md).

It separates resource identity, immutable semantic revisions/commitment snapshots, mutable conflict-versioned lifecycle state, and representation schema versions; establishes logical persistence ownership; requires exact historical resolution and stale-write detection; and preserves bounded control-plane history without mandating one persistence technology or universal event sourcing.

### 004-D

004-D established [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md) and [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](../../decisions/ADR-0003-sealed-manifest-gated-output-promotion.md).

Key accepted architecture rules include:

- Spark DataFrames are distributed access objects, not durable source/output identity;
- mutable source selectors such as table names, paths, queries, aliases, or DataFrames must resolve to stable source-state identity/read boundaries before committed work relies on them;
- provider-native immutable snapshots, materialized snapshots, immutable manifests, fingerprints with explicit strength, or external authoritative snapshot identities may satisfy source identity without requiring one universal full-corpus hash;
- stable source identity must also provide a read binding sufficient to prevent execution from silently reading a later/mixed mutable source state;
- source snapshotting/manifesting remains distributed preparation rather than fabricated Learning;
- physical Spark/storage schema stays distinct from Data Meaning;
- typed source/candidate/completed-output reference roles remain distinguishable even if resolver infrastructure is shared;
- manifests are representation mechanisms and use bounded control-plane roots with distributed component indexes/provider snapshots where scale requires;
- candidate materialization is mutable/open while writers are active, then establishes an immutable sealed candidate snapshot before required Evaluation or promotion relies on it;
- sealing establishes physical extent/integrity/immutability to a declared strength but does not establish Generation completion;
- Evidence used for Generation completion must bind the exact sealed candidate evaluated;
- open, sealed-unpromoted, failed, abandoned, and quarantined candidates remain outside ordinary completed-output discovery;
- stale writers must be fenceable, while duplicate physical computation remains permissible when candidate membership and semantic authority remain unambiguous;
- Generation promotion is a separate idempotent/fenced control-plane transition that may create at most one completed logical output;
- promotion may reuse the sealed candidate bytes in place and does not universally require copying distributed rows to a new final location;
- completed-output identity remains distinct from its Spark DataFrame/table/file/component representation;
- arbitrary downstream Spark transformations do not inherit completed-output identity or canonical Provenance automatically;
- relocation/replication/compaction/reserialization may preserve output identity only under explicit equivalence/integrity semantics;
- physical row/partition/file order does not define logical identity unless ordering is semantically material;
- reference resolution and snapshot/promotion data movement remain authorization/no-egress aware;
- no concrete Spark table/file provider, manifest serialization, hash algorithm, or fencing technology is selected yet.

## Phase 004 guardrails

Phase 004 MUST NOT:

- redesign accepted concept semantics merely to simplify package structure;
- erase experience distinctions behind generic API status/metadata/session objects;
- make one runtime/platform mandatory unless the semantic contract requires it;
- force ordinary enterprise source/output materialization to driver-local memory;
- make network/resource acquisition implicit;
- treat physical storage existence or manifest sealing as semantic promotion;
- equate platform exactly-once claims with SYNGAN semantic promotion;
- turn Provenance into a shadow copy of all domain/runtime data;
- make security redaction falsify historical existence;
- create package dependency cycles merely because semantic synchronizations are bidirectional;
- make process-local object/Future/DataFrame identity the durable identity of distributed work or output;
- collapse semantic revision, lifecycle state version, and storage schema version into one ambiguous field;
- allow derived indexes or mutable aliases to become canonical historical truth;
- use silent last-writer-wins for material semantic/lifecycle authority;
- allow Evaluation completion Evidence to bind an open/mutable candidate when exact candidate identity is required;
- require row-copying or exactly-once physical writes merely to express semantic finality;
- jump prematurely into implementation task breakdown before architecture boundaries are accepted.

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

**004-E — Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture**
