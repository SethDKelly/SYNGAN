---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design knowledge bundle for SYNGAN.

## Progressive disclosure

- [Authority](authority/index.md) — methodology, documentation governance, terminology and source rules.
- [Problem Knowledge](problem/index.md) — problem, purpose, actors, outcomes and enterprise scale envelope.
- [Domain Terminology](terminology/index.md) — canonical vocabulary and compatibility mappings.
- [Accepted Concepts](concepts/index.md) — canonical concept purpose, ownership, actions, invariants and boundaries.
- [Accepted Synchronizations](synchronizations/index.md) — canonical cross-concept coordination rules.
- [Concept Discovery](discovery/index.md) — historical hypotheses, falsification evidence, alternatives and design provenance.
- [Phases](phases/index.md) — phase plans, outcomes and exit reviews.
- `architecture/` — representation and implementation architecture, intentionally downstream of concept specification.
- `decisions/` — architecture and governance decisions requiring durable provenance.
- `references/` — external references used by the design.
- `backlog/` — unresolved or deferred work that is not canonical design authority.

## Authority rule

A durable fact, definition, requirement, invariant, policy, or design decision has one canonical home. Other documents SHOULD reference that authority rather than restating it as a competing source of truth.

For accepted concept meaning, `docs/concepts/` supersedes earlier provisional discovery statements. For accepted cross-concept coordination, `docs/synchronizations/` supersedes provisional synchronization hypotheses/specifications under discovery.

## Phase status

**Phase 001 — Design Foundation & Concept Discovery: complete.**

Exit record: [001-H — Phase 001 Consolidation & Initial Concept Catalog](phases/001/001-H-phase-001-consolidation-initial-concept-catalog.md).

**Current phase: Phase 002 — Concept Specification & Invariant Refinement.**

Completed in Phase 002:

- [002-A — Data Meaning & Constraint Specification](phases/002/002-A-data-meaning-constraint-specification.md)

Next: **002-B — Synthesis Strategy Specification & Capability Semantics**.

See [Phase 002 index](phases/002/index.md).
