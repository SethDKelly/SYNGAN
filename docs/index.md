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
- [Representation & Architecture Design](architecture/index.md) — current representation/module/interface/runtime/persistence architecture authority, downstream of concepts and experience.
- [Concept Discovery](discovery/index.md) — historical hypotheses, falsification evidence, alternatives and design provenance.
- [Phases](phases/index.md) — phase plans, outcomes and exit reviews.
- `decisions/` — architecture and governance decisions requiring durable provenance.
- `references/` — external references used by the design.
- `backlog/` — unresolved or deferred work that is not canonical design authority.

## Authority rule

A durable fact, definition, requirement, invariant, policy, or design decision has one canonical home. Other documents SHOULD reference that authority rather than restating it as a competing source of truth.

For accepted concept meaning, `docs/concepts/` supersedes provisional discovery statements. For accepted cross-concept coordination, `docs/synchronizations/` supersedes discovery hypotheses. `docs/experience/` defines how actors encounter those semantics. `docs/architecture/` may choose representation and implementation-facing boundaries but MUST NOT override authority/concept/synchronization/experience contracts.

## Phase status

**Phase 001 — Design Foundation & Concept Discovery: complete.**

Exit: [001-H — Phase 001 Consolidation & Initial Concept Catalog](phases/001/001-H-phase-001-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification & Invariant Refinement: complete.**

Exit: [002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md).

Phase 002 closed with eleven accepted concepts and fifteen synchronization rules intact after deep specification, an offline/no-outbound-network capable core, explicit commitment/historical binding, single semantic promotion, typed Provenance, and a canonical [Reproducibility Contract](authority/reproducibility-contract.md).

**Phase 003 — Experience & Workflow Design: complete.**

Exit: [003-I — Cross-Workflow Consistency & Phase 003 Consolidation Review](phases/003/003-I-cross-workflow-consistency-phase-003-consolidation-review.md).

Phase 003 closed with eight detailed experience authorities and the [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md). The exit audit found no concept/synchronization redesign required and preserved readiness/commitment, semantic/operational, promotion, Evidence, historical/current, reproducibility, offline/no-egress, disclosure, and enterprise-scale consistency.

**Current phase: [Phase 004 — Representation & Architecture Design](phases/004/index.md).**

Phase 004 translates the frozen semantic/experience model into public API/resource boundaries, control-plane identity/persistence, Spark-scale data/reference architecture, strategy/runtime adapters, Execution/recovery mechanics, Evidence/Provenance/reproducibility representation, enterprise dependency/security controls, and deployment/platform integration.

Next: **004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction**.
