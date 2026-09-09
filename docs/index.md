---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design and implementation-planning knowledge bundle for SYNGAN.

## Progressive disclosure

- [Authority](authority/index.md) — methodology/governance/cross-cutting contracts.
- [Problem Knowledge](problem/index.md) — problem, purpose, actors, constraints and enterprise scale envelope.
- [Domain Terminology](terminology/index.md) — canonical vocabulary.
- [Accepted Concepts](concepts/index.md) — current concept authority.
- [Accepted Synchronizations](synchronizations/index.md) — current cross-concept coordination authority.
- [Experience & Workflow Design](experience/index.md) — begin with the [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md).
- [Representation & Architecture Design](architecture/index.md) — begin with the [Phase 004 Consolidated Architecture Contract](architecture/phase-004-consolidated-architecture-contract.md).
- [Implementation Planning & Delivery Authority](implementation/index.md) — Phase 005 planning baseline; implementation is not yet authorized.
- [Architecture Decision Records](decisions/index.md) — rationale/supersession history.
- [Concept Discovery](discovery/index.md) — historical discovery/design evidence.
- [Backlog](backlog/index.md) — blocking/refinement/deferred delivery debt; non-authoritative.
- [Phases](phases/index.md) — current phase program and history.

## Authority rule

A durable fact, definition, requirement, invariant, policy, design decision, or implementation rule has one canonical home. Other documents SHOULD reference that authority rather than restating it as a competing source of truth.

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation planning
  > future code / deployment
  > ADR rationale / phase history / summaries / backlog where applicable
```

Later layers MUST NOT redefine earlier authority for convenience. If later feasibility/planning exposes a genuine upstream problem, the upstream authority is reopened explicitly.

## Completed layers

- **Phase 001 — Design Foundation & Concept Discovery — complete**
- **Phase 002 — Concept Specification & Invariant Refinement — complete** — eleven accepted concepts and fifteen synchronizations.
- **Phase 003 — Experience & Workflow Design — complete** — [consolidated experience contract](experience/phase-003-consolidated-experience-contract.md).
- **Phase 004 — Representation & Architecture Design — complete** — [consolidated architecture contract](architecture/phase-004-consolidated-architecture-contract.md).
- **Phase 005 — Implementation Planning & Delivery Decomposition — complete as planning only** — [005-K exit](phases/005/005-K-cross-slice-integration-delivery-sequencing-backlog-closure-jackson-methodology-completeness-implementation-readiness-exit.md).

Phase 005's accepted planning baseline is consolidated in the [Phase 005 Consolidated Implementation-Planning Contract](implementation/phase-005-consolidated-implementation-planning-contract.md).

## Current phase

**[Phase 006 — Post-Planning Design Validation & Adversarial Refinement](phases/006/index.md) is current and design-only.**

005-K found that the A-J implementation plans are coherent and dependency-safe, but did not approve production implementation readiness.

Blocking design refinement is tracked in the [Backlog](backlog/index.md):

1. regressive restore and temporal-authority closure;
2. post-planning adversarial end-to-end validation;
3. representative Strategy/method design probes;
4. initial-baseline scope and future-extensibility closure.

Phase 006 exists to resolve those issues at the correct concept/synchronization/experience/architecture layer before code hardens downstream assumptions.

## Current invariant baseline

Until Phase 006 explicitly revises upstream authority, the system continues to preserve:

- model-neutral structured/tabular synthesis concepts;
- one stable ResourceRef/revision/state/schema identity substrate in future implementation planning;
- exact source/candidate/sealed-snapshot/result boundaries;
- semantic completion distinct from runtime/platform completion;
- one Execution with multiple fenced Attempts and explicit recovery/cancellation semantics;
- owner-established Evidence and typed canonical Provenance;
- qualified reproducibility rather than Boolean inheritance;
- explicit dependency/trust/authorization/network/egress distinctions;
- no hidden runtime acquisition/remote fallback/required external telemetry in offline/no-egress profiles;
- capability-negotiated platforms rather than provider-name authority;
- enterprise-scale workflows without mandatory full-corpus driver-local materialization;
- no production implementation until a later explicit implementation-authority phase is approved.

## Next

**006-A — Post-Planning Concept Completeness, Mechanism-vs-Concept & Scope-Boundary Revalidation**

## Documentation governance note

The repository continues to use its project-specific OKF-oriented profile. Strict external OKF 0.2 reserved-file/frontmatter normalization has not been declared complete and remains non-blocking governance debt until separately audited against current external authority.