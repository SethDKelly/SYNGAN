---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design knowledge bundle for SYNGAN.

## Progressive disclosure

- [Authority](authority/index.md) — methodology, documentation governance, terminology, provenance, and network/external-dependency rules.
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
- [002-B — Synthesis Strategy Specification & Capability Semantics](phases/002/002-B-synthesis-strategy-capability-semantics.md)
- [002-C — Learning & Learned State Specification](phases/002/002-C-learning-learned-state-specification.md)
- [002-D — Generation Specification, Request/Condition Semantics & Output Completion](phases/002/002-D-generation-request-condition-output-completion.md)

002-B established the [Network and External Dependency Policy](authority/network-external-dependency-policy.md), including an offline/no-outbound-network design profile for supported core structured/tabular synthesis and explicit declaration of optional external dependencies.

002-C established stable Learning commitment/source history, checkpoint-versus-Learned-State separation, distributed reusable Learned State semantics, non-mutating reuse, and explicit sensitivity/dependency boundaries.

002-D established Generation commitment/request semantics, mandatory versus best-effort Conditions, direct-generation and Learned-State paths, required-Constraint completion rules, candidate-versus-completed output, and a semantic completion barrier distinct from physical materialization and Execution completion.

Next: **002-E — Evaluation Criterion, Evaluation & Evidence Specification**.

See [Phase 002 index](phases/002/index.md).
