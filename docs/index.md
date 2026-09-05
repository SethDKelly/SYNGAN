---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design and implementation-planning knowledge bundle for SYNGAN.

## Progressive disclosure

- [Authority](authority/index.md) — methodology, documentation governance, terminology, source/provenance, network/external-dependency, and reproducibility rules.
- [Problem Knowledge](problem/index.md) — problem, purpose, actors, outcomes and enterprise scale envelope.
- [Domain Terminology](terminology/index.md) — canonical vocabulary and compatibility mappings.
- [Accepted Concepts](concepts/index.md) — canonical concept purpose, ownership, actions, lifecycle, invariants and boundaries.
- [Accepted Synchronizations](synchronizations/index.md) — canonical cross-concept coordination rules.
- [Experience & Workflow Design](experience/index.md) — actor-visible/programmatic workflow semantics; start implementation-facing experience review with the [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md).
- [Representation & Architecture Design](architecture/index.md) — accepted implementation-facing architecture; start with the [Phase 004 Consolidated Architecture Contract](architecture/phase-004-consolidated-architecture-contract.md).
- [Implementation Planning & Delivery Authority](implementation/index.md) — current implementation governance and accepted Phase 005 implementation plans.
- [Architecture Decision Records](decisions/index.md) — architecture rationale/alternatives/supersession; current normative architecture remains under `docs/architecture/`.
- [Concept Discovery](discovery/index.md) — historical hypotheses, alternatives and design provenance.
- [Phases](phases/index.md) — phase plans, outcomes and exit reviews.
- `references/` — external references used by the design.
- `backlog/` — unresolved/deferred work that is not canonical authority.

## Authority rule

A durable fact, definition, requirement, invariant, policy, design decision, or implementation rule has one canonical home. Other documents SHOULD reference that authority rather than restating it as a competing source of truth.

The active downstream order is:

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation authority / planning
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

## Current phase

**[Phase 005 — Implementation Planning & Delivery Decomposition](phases/005/index.md) is current.**

Completed:

- [005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](phases/005/005-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md)

Canonical implementation authority now begins at [Implementation Planning & Delivery Authority](implementation/index.md).

005-A establishes implementation precedence/conflict escalation, delivery/change classification, acceptance evidence requirements, reproducible toolchain/dependency governance, migration/compatibility discipline, repository-wide [`AGENTS.md`](../AGENTS.md), and a GitHub PR review checklist without prematurely selecting source topology or concrete verification tooling.

Next:

**005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**

005-B must convert the accepted Phase 004 invariants and 005-A completion-evidence contract into executable verification layers and repository quality gates before 005-C selects detailed source/package topology.

## Documentation governance note

The repository continues to use its project-specific OKF profile. The separate question of strict external OKF 0.2 reserved-file/frontmatter normalization has not been falsely declared resolved and remains documentation-governance debt until explicitly audited against current external authority.
