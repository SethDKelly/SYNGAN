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

## Groups

| Group | Scope | Status |
|---|---|---|
| **004-A** | [**Architecture Authority, Representation Principles, Layering & Dependency Direction**](004-A-architecture-authority-representation-layering-dependency-direction.md) | **complete** |
| **004-B** | [**Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping**](004-B-public-api-resource-handle-workflow-semantic-mapping.md) | **complete** |
| **004-C** | [**Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture**](004-C-control-plane-identity-revision-state-persistence-historical-reference-architecture.md) | **complete** |
| **004-D** | **Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture** | **next** |
| 004-E | Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture | planned |
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

Key accepted architecture rules include:

- resource identity, semantic revision/commitment snapshot, lifecycle state version, and representation schema version remain separate;
- stable logical IDs are typed, durable, namespace-capable where required, independent of mutable locators/platform IDs, and never reused for materially different resources;
- bindable Data Meaning/Constraint/Strategy/Criterion revisions become immutable in material meaning;
- persisted draft/specification identity remains distinct from committed Learning/Generation/Evaluation occurrence identity;
- each committed activity has an immutable commitment snapshot and mutable owner-specific current lifecycle state;
- Learned State/output/Evidence historical identity remains stable while future-use/applicability lifecycle changes separately;
- material lifecycle writes require conflict/stale-write detection rather than silent last-writer-wins;
- material transition history is retained without requiring universal event sourcing;
- logical persistence ownership remains separated among semantic authorities, committed activities, promoted results, Execution/Attempts, Provenance, and derived indexes even when one physical database is shared;
- derived read/search indexes do not gain canonical write authority;
- coupled semantic transitions require detectable/recoverable consistency across crashes/retries without mandating one global distributed transaction technology;
- exact historical reference resolution never silently substitutes current/latest state;
- withheld/redacted, unavailable, unknown/indeterminate, invalid-reference and absent states remain distinguishable;
- retained identity/tombstone semantics prevent payload expiration from erasing historical existence or enabling ID reuse;
- correction/supersession preserves authority boundaries and auditability;
- representation schema migration remains separate from semantic revision;
- canonical control-plane state remains bounded by resources/revisions/material transitions rather than row/task/log/tensor volume.

004-C intentionally does not choose ID encoding, database technology, physical schemas, event-sourcing strategy, transaction/outbox implementation, retention periods, source fingerprints, output manifests, provenance store, authorization implementation, or serialized handle format.

## Phase 004 guardrails

Phase 004 MUST NOT:

- redesign accepted concept semantics merely to simplify package structure;
- erase experience distinctions behind generic API status/metadata/session objects;
- make one runtime/platform mandatory unless the semantic contract requires it;
- force ordinary enterprise source/output materialization to driver-local memory;
- make network/resource acquisition implicit;
- treat physical storage existence as semantic promotion;
- equate platform exactly-once claims with SYNGAN semantic promotion;
- turn Provenance into a shadow copy of all domain/runtime data;
- make security redaction falsify historical existence;
- create package dependency cycles merely because semantic synchronizations are bidirectional;
- make process-local object/Future identity the durable identity of distributed work;
- collapse semantic revision, lifecycle state version, and storage schema version into one ambiguous field;
- allow derived indexes or mutable aliases to become canonical historical truth;
- use silent last-writer-wins for material semantic/lifecycle authority;
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

**004-D — Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture**
