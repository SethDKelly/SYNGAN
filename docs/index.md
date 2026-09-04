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
- [002-E — Evaluation Criterion, Evaluation & Evidence Specification](phases/002/002-E-evaluation-criterion-evaluation-evidence-specification.md)
- [002-F — Execution, Attempt History, Failure & Recovery Semantics](phases/002/002-F-execution-attempt-failure-recovery-semantics.md)
- [002-G — Provenance, Reproducibility Contract & Historical Binding Specification](phases/002/002-G-provenance-reproducibility-historical-binding-specification.md)

002-B established the [Network and External Dependency Policy](authority/network-external-dependency-policy.md), including an offline/no-outbound-network design profile for supported core structured/tabular synthesis and explicit declaration of optional external dependencies.

002-F established logical Execution/Attempt identity, retry/resume/checkpoint safety, unknown-state and cancellation semantics, single semantic promotion, and platform-neutral operational history without equating physical job completion with domain completion.

002-G deepened [Provenance](concepts/provenance.md) and established the [Reproducibility Contract](authority/reproducibility-contract.md), including stable historical identity, typed relationship semantics, exact/semantic/statistical/bounded/comparative reproduction classes, explicit insufficient-context outcomes, and materiality-bounded history that avoids copying complete data/model/telemetry payloads.

Next: **002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review**.

See [Phase 002 index](phases/002/index.md).
