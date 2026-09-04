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
- [Domain Terminology](terminology/index.md) — canonical domain vocabulary, semantic distinctions, compatibility mappings and term status.
- [Concept Discovery](discovery/index.md) — provisional candidate concepts, operational principles, review decisions, ownership guardrails, boundary/synchronization hypotheses and coverage checks.
- [Phases](phases/index.md) — phase plans, outcomes and exit reviews.
- `concepts/` — canonical concept specifications, created only after Phase 001 has completed the required concept tests and consolidation.
- `synchronizations/` — accepted cross-concept coordination knowledge, created after composition/synchronization review.
- `architecture/` — representation and implementation architecture, intentionally downstream of concept design.
- `decisions/` — architecture and governance decisions that need durable provenance.
- `references/` — external references used by the design.
- `backlog/` — unresolved or deferred work that is not canonical design authority.

## Authority rule

A fact, definition, requirement, invariant, or design decision has one canonical home. Other documents SHOULD link to that authority rather than restating it. Repetition is allowed only when required for local comprehension, independent auditability, or an explicit derived summary; repeated text MUST NOT silently become a competing authority.

## Current phase

Phase 001 — Design Foundation & Concept Discovery.

Completed:

- [001-A — Design Authority, Methodology, OKF 0.2 & Documentation Governance](phases/001/001-A-design-authority-methodology-okf-documentation-governance.md)
- [001-B — Problem, Purpose, Actors, Outcomes & Enterprise Scale Envelope](phases/001/001-B-problem-purpose-actors-outcomes-enterprise-scale-envelope.md)
- [001-C — Domain Terminology & Synthetic-Data Semantic Inventory](phases/001/001-C-domain-terminology-synthetic-data-semantic-inventory.md)
- [001-D — Candidate Concept Discovery & Boundary Hypotheses](phases/001/001-D-candidate-concept-discovery-boundary-hypotheses.md)
- [001-E — Concept Criteria, Independence, Genericity & Completeness Review](phases/001/001-E-concept-criteria-independence-genericity-completeness-review.md)
- [001-F — Operational Principle Development](phases/001/001-F-operational-principle-development.md)

Next: **001-G — Concept Composition, Synchronization & Dependency Analysis**.

The current provisional handoff to 001-G is the [Operational Principle Falsification Review](discovery/operational-principle-review.md) together with the full [Candidate Operational Principles](discovery/operational-principles.md). All eleven candidates remain provisional until composition/synchronization analysis and Phase 001 consolidation are complete.
