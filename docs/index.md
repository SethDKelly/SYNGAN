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
- [Experience & Workflow Design](experience/index.md) — actor-visible/programmatic workflow semantics; start implementation-facing experience review with the [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md).
- [Representation & Architecture Design](architecture/index.md) — accepted implementation-facing architecture; start with the [Phase 004 Consolidated Architecture Contract](architecture/phase-004-consolidated-architecture-contract.md).
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
  > implementation planning
  > code / deployment
  > ADR rationale / phase history / summaries / backlog where applicable
```

Implementation planning and code MUST NOT override upstream semantic, experience, or architecture contracts for convenience.

## Completed design layers

### Phase 001 — Design Foundation & Concept Discovery — complete

Exit: [001-H — Phase 001 Consolidation & Initial Concept Catalog](phases/001/001-H-phase-001-consolidation-initial-concept-catalog.md).

### Phase 002 — Concept Specification & Invariant Refinement — complete

Exit: [002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md).

Phase 002 closed with eleven accepted concepts and fifteen synchronization rules.

### Phase 003 — Experience & Workflow Design — complete

Exit: [003-I — Cross-Workflow Consistency & Phase 003 Consolidation Review](phases/003/003-I-cross-workflow-consistency-phase-003-consolidation-review.md).

Exit authority: [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md).

### Phase 004 — Representation & Architecture Design — complete

Exit: [004-J — Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit](phases/004/004-J-cross-architecture-invariant-audit-decision-consolidation-phase-004-exit.md).

Exit authority: [Phase 004 Consolidated Architecture Contract](architecture/phase-004-consolidated-architecture-contract.md).

Phase 004 closed with no concept/synchronization redesign, nine detailed architecture authorities, and active ADR-0001 through ADR-0008.

The architecture baseline now preserves:

- typed durable resource identity and immutable commitments;
- bounded control-plane versus distributed data-plane separation;
- exact Spark-scale source-state binding and sealed candidate/output promotion;
- model-neutral Strategy/runtime extension contracts;
- one logical Execution across fenced/reconcilable Attempts;
- strict checkpoint/candidate/runtime-result versus semantic-result boundaries;
- Evaluation validation before Evidence establishment;
- typed canonical Provenance and qualified reproducibility;
- explicit dependency/trust/authorization/network/egress distinctions;
- scoped runtime capabilities, secret isolation, truthful redaction and protected query projections;
- portable core contracts with capability-negotiated platform adapters;
- Databricks specialization without platform semantic ownership;
- generic/self-managed Spark/private-offline viability when required guarantees are supplied;
- multi-axis compatibility, restartable coordination, and enterprise-scale no-full-driver-materialization requirements.

## Current phase

**[Phase 005 — Implementation Planning & Delivery Decomposition](phases/005/index.md) is current.**

Next:

**005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement**

Phase 005 must map upstream authority through architecture into modules/ports/adapters/persisted representations, dependency-safe implementation slices, verification/fitness tests, and acceptance evidence before coding is treated as implementation-complete.

## Documentation governance note

The repository continues to use its project-specific OKF profile. The separate question of strict external OKF 0.2 metadata/frontmatter normalization has not been falsely declared resolved by the Phase 004 exit and remains documentation-governance debt until explicitly audited against current external authority.
