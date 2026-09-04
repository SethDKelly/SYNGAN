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
- [Experience & Workflow Design](experience/index.md) — canonical actor-visible and programmatic workflow/experience semantics derived from the accepted model.
- [Concept Discovery](discovery/index.md) — historical hypotheses, falsification evidence, alternatives and design provenance.
- [Phases](phases/index.md) — phase plans, outcomes and exit reviews.
- `architecture/` — representation and implementation architecture, intentionally downstream of experience/workflow design.
- `decisions/` — architecture and governance decisions requiring durable provenance.
- `references/` — external references used by the design.
- `backlog/` — unresolved or deferred work that is not canonical design authority.

## Authority rule

A durable fact, definition, requirement, invariant, policy, or design decision has one canonical home. Other documents SHOULD reference that authority rather than restating it as a competing source of truth.

For accepted concept meaning, `docs/concepts/` supersedes provisional discovery statements. For accepted cross-concept coordination, `docs/synchronizations/` supersedes provisional synchronization hypotheses/specifications under discovery. `docs/experience/` defines how actors encounter those semantics and MUST NOT override the concept/synchronization/authority layers.

## Phase status

**Phase 001 — Design Foundation & Concept Discovery: complete.**

Exit record: [001-H — Phase 001 Consolidation & Initial Concept Catalog](phases/001/001-H-phase-001-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification & Invariant Refinement: complete.**

Exit record: [002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md).

Phase 002 exits with eleven accepted concepts and fifteen synchronization rules intact after deep specification, an offline/no-outbound-network capable core, explicit semantic commitment/historical binding, single semantic promotion, typed Provenance, and a canonical [Reproducibility Contract](authority/reproducibility-contract.md).

**Current phase: [Phase 003 — Experience & Workflow Design](phases/003/index.md).**

Completed in Phase 003:

- [003-A — Workflow Entry, Source Context & Lifecycle Orientation](phases/003/003-A-workflow-entry-source-context-lifecycle-orientation.md)
- [003-B — Data Meaning, Constraint & Strategy Preparation Experience](phases/003/003-B-data-meaning-constraint-strategy-preparation-experience.md)
- [003-C — Learning & Learned State Lifecycle Experience](phases/003/003-C-learning-learned-state-lifecycle-experience.md)

003-A established the canonical experience layer and defined intent-oriented workflow entry, source/history orientation, semantic commitment visibility, semantic-versus-operational status separation, candidate-versus-authoritative-result distinction, and programmatic/human parity.

003-B defines preparation as a composition over Data Meaning, Constraint, and Synthesis Strategy; preserves declared/inferred/unresolved semantic distinctions, contextual rule applicability/handling, explainable Strategy compatibility, derived readiness, review-before-commit, and explicit offline/dependency posture without creating Metadata/Validation/Readiness god-concepts.

003-C defines Learning/Learned State lifecycle experience: direct-generation Strategies bypass fake Learning, commitment freezes semantic context, progress remains Strategy-meaningful, Execution/Attempts remain operational, checkpoints stay non-final, semantic completion explicitly promotes one logical Learned State, reuse is non-mutating/contextual, restricted/retired/invalidated statuses remain distinct, and source-derived sensitivity/dependency posture stays visible.

Next: **003-D — Generation Request, Condition, Validation & Output Promotion Experience**.
