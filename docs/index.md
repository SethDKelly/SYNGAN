---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design knowledge bundle for SYNGAN.

## Progressive disclosure

- [Authority](authority/index.md) — methodology, documentation governance, terminology, source/provenance, network/external-dependency, and reproducibility rules.
- [Problem Knowledge](problem/index.md) — problem, purpose, actors, outcomes and enterprise scale envelope.
- [Domain Terminology](terminology/index.md) — canonical vocabulary and compatibility mappings.
- [Accepted Concepts](concepts/index.md) — canonical concept purpose, ownership, actions, lifecycle, invariants and boundaries.
- [Accepted Synchronizations](synchronizations/index.md) — canonical cross-concept coordination rules.
- [Experience & Workflow Design](experience/index.md) — actor-visible/programmatic workflow semantics and the [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md).
- [Representation & Architecture Design](architecture/index.md) — current implementation-facing architecture authority.
- [Architecture Decision Records](decisions/index.md) — architecture rationale/alternatives/supersession; current normative architecture remains under `docs/architecture/`.
- [Concept Discovery](discovery/index.md) — historical hypotheses, alternatives and design provenance.
- [Phases](phases/index.md) — phase plans, outcomes and exit reviews.
- `references/` — external references used by the design.
- `backlog/` — unresolved/deferred work that is not canonical authority.

## Authority rule

A durable fact, definition, requirement, invariant, policy, or design decision has one canonical home. Other documents SHOULD reference that authority rather than restating it as a competing source of truth.

The active downstream order is:

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > ADR rationale / phase records
  > summaries / examples / backlog
```

Architecture may choose representation and implementation-facing boundaries but MUST NOT override upstream semantic/experience contracts.

## Phase status

**Phase 001 — Design Foundation & Concept Discovery: complete.**

Exit: [001-H — Phase 001 Consolidation & Initial Concept Catalog](phases/001/001-H-phase-001-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification & Invariant Refinement: complete.**

Exit: [002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md).

Phase 002 closed with eleven accepted concepts and fifteen synchronization rules, offline/no-outbound-network capable core semantics, explicit commitment/historical binding, single semantic promotion, typed Provenance, and qualified reproducibility.

**Phase 003 — Experience & Workflow Design: complete.**

Exit: [003-I — Cross-Workflow Consistency & Phase 003 Consolidation Review](phases/003/003-I-cross-workflow-consistency-phase-003-consolidation-review.md).

Phase 003 closed with eight detailed experience authorities and the [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md).

**Current phase: [Phase 004 — Representation & Architecture Design](phases/004/index.md).**

Completed in Phase 004:

- [004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction](phases/004/004-A-architecture-authority-representation-layering-dependency-direction.md)
- [004-B — Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](phases/004/004-B-public-api-resource-handle-workflow-semantic-mapping.md)
- [004-C — Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](phases/004/004-C-control-plane-identity-revision-state-persistence-historical-reference-architecture.md)
- [004-D — Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](phases/004/004-D-spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion-architecture.md)
- [004-E — Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](phases/004/004-E-strategy-extension-learning-generation-evaluation-runtime-adapter-architecture.md)
- [004-F — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](phases/004/004-F-execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-architecture.md)

Canonical architecture now includes:

- the [architecture constitution](architecture/architecture-authority-representation-layering.md);
- the [typed public resource/handle architecture](architecture/public-api-resource-handle-workflow-semantic-mapping.md);
- the [control-plane identity/state architecture](architecture/control-plane-identity-revision-state-persistence-historical-reference.md);
- the [Spark data boundary/materialization architecture](architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md);
- the [Strategy extension/runtime adapter architecture](architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md);
- the [Execution/recovery/fencing architecture](architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md).

004-F establishes one stable Execution across many Attempts; ordered Attempt epochs/fencing generations; lease-versus-fence separation; operation-scoped idempotency; immutable checkpoint snapshots and contextual resume qualification; explicit retry/restart/reconcile decisions; durable unknown-state semantics; safe candidate sealing and semantic-promotion preconditions; Evaluation double-count protection; and cancellation as durable intent followed by reconciled outcome. Duplicate physical work is allowed while stale or duplicate canonical authority is not.

Decision rationale:

- [ADR-0001 — Typed Resource/Handle Public API](decisions/ADR-0001-typed-resource-handle-public-api.md)
- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md)
- [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](decisions/ADR-0003-sealed-manifest-gated-output-promotion.md)
- [ADR-0004 — Semantic Extension & Runtime Binding Separation](decisions/ADR-0004-semantic-extension-runtime-binding-separation.md)
- [ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution](decisions/ADR-0005-attempt-epoch-fencing-recoverable-at-least-once-execution.md)

Next: **004-G — Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture**.
