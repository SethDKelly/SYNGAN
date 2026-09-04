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
- [Experience & Workflow Design](experience/index.md) — canonical actor-visible and programmatic workflow semantics, including the [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md).
- [Representation & Architecture Design](architecture/index.md) — current implementation-facing architecture authority, downstream of concepts/synchronizations/experience.
- [Architecture Decision Records](decisions/index.md) — durable architecture decision rationale, alternatives and supersession history; current normative architecture remains under `docs/architecture/`.
- [Concept Discovery](discovery/index.md) — historical hypotheses, falsification evidence, alternatives and design provenance.
- [Phases](phases/index.md) — phase plans, outcomes and exit reviews.
- `references/` — external references used by the design.
- `backlog/` — unresolved or deferred work that is not canonical design authority.

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

Architecture may choose representation and implementation-facing boundaries but MUST NOT override upstream semantic/experience contracts. An architectural infeasibility must be surfaced explicitly for upstream revision.

## Phase status

**Phase 001 — Design Foundation & Concept Discovery: complete.**

Exit: [001-H — Phase 001 Consolidation & Initial Concept Catalog](phases/001/001-H-phase-001-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification & Invariant Refinement: complete.**

Exit: [002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md).

Phase 002 closed with eleven accepted concepts and fifteen synchronization rules intact after deep specification, an offline/no-outbound-network capable core, explicit commitment/historical binding, single semantic promotion, typed Provenance, and a canonical [Reproducibility Contract](authority/reproducibility-contract.md).

**Phase 003 — Experience & Workflow Design: complete.**

Exit: [003-I — Cross-Workflow Consistency & Phase 003 Consolidation Review](phases/003/003-I-cross-workflow-consistency-phase-003-consolidation-review.md).

Phase 003 closed with eight detailed experience authorities and the [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md), preserving readiness/commitment, semantic/operational, promotion, Evidence, historical/current, reproducibility, offline/no-egress, disclosure, and enterprise-scale distinctions.

**Current phase: [Phase 004 — Representation & Architecture Design](phases/004/index.md).**

Completed in Phase 004:

- [004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction](phases/004/004-A-architecture-authority-representation-layering-dependency-direction.md)
- [004-B — Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](phases/004/004-B-public-api-resource-handle-workflow-semantic-mapping.md)
- [004-C — Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](phases/004/004-C-control-plane-identity-revision-state-persistence-historical-reference-architecture.md)

004-A establishes the [architecture constitution](architecture/architecture-authority-representation-layering.md): semantic-preserving representation, bounded control/data-plane separation, inward dependencies, adapter isolation, Spark-native/model-neutral semantics, anti-god-module rules, and architecture decision discipline.

004-B establishes the [typed public resource/handle architecture](architecture/public-api-resource-handle-workflow-semantic-mapping.md): editable specifications and contextual readiness remain distinct from committed activities; promoted Learned State/output/Evidence resources remain distinct from raw payloads; Execution remains operationally separate; handles are durable re-resolvable identities; and convenience façades cannot own canonical state.

004-C establishes the [control-plane identity/state architecture](architecture/control-plane-identity-revision-state-persistence-historical-reference.md): stable resource identity, immutable semantic revisions/commitment snapshots, mutable conflict-versioned lifecycle state, representation schema versioning, exact historical references, bounded logical persistence ownership, recoverable coupled-transition consistency, and non-authoritative derived indexes.

Decision rationale:

- [ADR-0001 — Typed Resource/Handle Public API](decisions/ADR-0001-typed-resource-handle-public-api.md)
- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md)

Next: **004-D — Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture**.
