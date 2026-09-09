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
- [Concept Discovery](discovery/index.md) — historical and active provisional discovery evidence.
- [Backlog](backlog/index.md) — blocking/refinement/deferred delivery debt; non-authoritative.
- [Phases](phases/index.md) — current phase program and history.

## Authority rule

A durable fact, definition, requirement, invariant, policy, design decision, or implementation rule has one canonical home. Later layers MUST NOT redefine earlier authority for convenience. If later feasibility evidence exposes a genuine upstream problem, the upstream authority is reopened explicitly.

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation planning
  > future code / deployment
  > ADR rationale / phase history / discovery / backlog where applicable
```

## Completed layers

- **Phase 001 — Design Foundation & Concept Discovery — complete**
- **Phase 002 — Concept Specification & Invariant Refinement — complete** — eleven accepted concepts and fifteen synchronizations.
- **Phase 003 — Experience & Workflow Design — complete**
- **Phase 004 — Representation & Architecture Design — complete**
- **Phase 005 — Implementation Planning & Delivery Decomposition — complete as planning only**

Phase 005's preserved future implementation baseline is the [Phase 005 Consolidated Implementation-Planning Contract](implementation/phase-005-consolidated-implementation-planning-contract.md).

## Current phase

**[Phase 006 — Post-Planning Design Validation & Adversarial Refinement](phases/006/index.md) is current and design-only.**

### 006-A complete

[006-A — Post-Planning Concept Completeness, Mechanism-vs-Concept & Scope-Boundary Revalidation](phases/006/006-A-post-planning-concept-completeness-mechanism-vs-concept-scope-boundary-revalidation.md) is complete.

006-A found no reason to promote Phase 005 mechanisms into concepts. The accepted catalog remains **eleven concepts / fifteen synchronizations**.

New structured-data capability evidence is now explicit:

```text
single-table generation           current baseline capability
time-series table generation      Phase 006 design target; initial inclusion TBD
multi-table shared-key generation Phase 006 design target; initial inclusion TBD
```

`GenerationMode` / `DataTopologyMode` is not an accepted concept; a future parameter may select a capability profile but cannot own relationship, temporal-order, Constraint, completion or Evidence semantics.

Multi-table shared-key synthesis supplies enough evidence to reopen the previously deferred **Relationship** candidate. It remains provisional discovery only until 006-G determines whether existing concepts suffice, one generic Relationship concept is required, temporal sequence semantics require a distinct boundary, or another narrower model is more defensible.

Discovery evidence: [Post-Planning Concept Revalidation & Structured-Data Topology Candidates](discovery/post-planning-concept-revalidation-structured-topology-candidates.md).

## Current invariant baseline

Until Phase 006 explicitly revises accepted authority, preserve:

- eleven accepted concepts and fifteen synchronizations;
- model-neutral structured/tabular synthesis;
- semantic completion distinct from runtime/platform completion;
- stable Execution with fenced Attempts and explicit recovery/cancellation;
- owner-established Evidence and typed Provenance;
- qualified reproducibility;
- explicit dependency/trust/authorization/network/egress distinctions;
- no hidden acquisition/remote fallback/required external telemetry in offline/no-egress profiles;
- capability-negotiated platforms rather than provider-name authority;
- enterprise-scale workflows without mandatory full-corpus driver-local materialization;
- no production implementation until a later explicit implementation-authority phase is approved.

## Next

**006-B — Temporal Authority, Disaster Recovery, Rollback, Fork & Historical-Truth Refinement**

This use of `temporal` concerns operational authority across rollback/restore and is distinct from time-series data semantics.

## Documentation governance note

The repository continues to use its project-specific OKF-oriented profile. Strict external OKF 0.2 reserved-file/frontmatter normalization has not been declared complete and remains non-blocking governance debt until separately audited.