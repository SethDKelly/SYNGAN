---
type: Phase Index
title: SYNGAN Design Phases
status: active
---

# Design Phases

## Phase 001 — Design Foundation & Concept Discovery — complete

See [Phase 001 index](001/index.md).

Phase 001 accepted the initial [concept catalog](../concepts/index.md) and [core synchronization set](../synchronizations/index.md).

## Phase 002 — Concept Specification & Invariant Refinement — complete

See [Phase 002 index](002/index.md).

Phase 002 refined the eleven accepted concepts and fifteen synchronizations without requiring a concept/synchronization redesign.

## Phase 003 — Experience & Workflow Design — complete

See [Phase 003 index](003/index.md).

Phase 003 closed through [003-I — Cross-Workflow Consistency & Phase 003 Consolidation Review](003/003-I-cross-workflow-consistency-phase-003-consolidation-review.md).

Phase 003 exit authority: [Phase 003 Consolidated Experience Contract](../experience/phase-003-consolidated-experience-contract.md).

## Phase 004 — Representation & Architecture Design — current

See [Phase 004 index](004/index.md).

- [004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction](004/004-A-architecture-authority-representation-layering-dependency-direction.md) — complete
- [004-B — Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](004/004-B-public-api-resource-handle-workflow-semantic-mapping.md) — complete
- [004-C — Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](004/004-C-control-plane-identity-revision-state-persistence-historical-reference-architecture.md) — complete
- **004-D — Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture — next**
- 004-E — Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture
- 004-F — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture
- 004-G — Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture
- 004-H — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture
- 004-I — Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture
- 004-J — Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit

Current architecture authority includes:

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](../architecture/architecture-authority-representation-layering.md)
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../architecture/public-api-resource-handle-workflow-semantic-mapping.md)
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)

Active ADR rationale includes:

- [ADR-0001 — Typed Resource/Handle Public API](../decisions/ADR-0001-typed-resource-handle-public-api.md)
- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](../decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md)

Representation/architecture is the active design layer. Implementation task breakdown remains downstream until Phase 004 establishes the necessary boundaries.
