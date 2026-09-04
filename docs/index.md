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
- [Phases](phases/index.md) — phase plans, outcomes and exit reviews.
- `concepts/` — canonical concept specifications, created after concept discovery.
- `synchronizations/` — cross-concept coordination knowledge.
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

Next: **001-C — Domain Terminology & Synthetic-Data Semantic Inventory**.
