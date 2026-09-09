---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design and implementation-planning knowledge bundle for SYNGAN.

## Progressive disclosure

- [Authority](authority/index.md) — methodology/governance/cross-cutting contracts, including operational-authority continuity after regressive recovery.
- [Problem Knowledge](problem/index.md) — problem, purpose, actors, constraints and enterprise scale envelope.
- [Domain Terminology](terminology/index.md) — canonical vocabulary.
- [Accepted Concepts](concepts/index.md) — current concept authority.
- [Accepted Synchronizations](synchronizations/index.md) — current cross-concept coordination authority.
- [Experience & Workflow Design](experience/index.md) — begin with the Phase 003 consolidated experience contract.
- [Representation & Architecture Design](architecture/index.md) — begin with the Phase 004 consolidated architecture contract.
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
- **Phase 003 — Experience & Workflow Design — complete** — consolidated experience contract.
- **Phase 004 — Representation & Architecture Design — complete** — consolidated architecture contract.
- **Phase 005 — Implementation Planning & Delivery Decomposition — complete as planning only** — implementation readiness was not approved.

The accepted Phase 005 planning baseline is consolidated in the [Phase 005 Consolidated Implementation-Planning Contract](implementation/phase-005-consolidated-implementation-planning-contract.md).

## Current phase

**[Phase 006 — Post-Planning Design Validation & Adversarial Refinement](phases/006/index.md) is current and design-only.**

Completed Phase 006 groups:

- [006-A — Concept Completeness, Mechanism-vs-Concept & Scope-Boundary Revalidation](phases/006/006-A-post-planning-concept-completeness-mechanism-vs-concept-scope-boundary-revalidation.md)
- [006-B — Temporal Authority, Disaster Recovery, Rollback, Fork & Historical-Truth Refinement](phases/006/006-B-temporal-authority-disaster-recovery-rollback-fork-historical-truth-refinement.md)

006-A kept the accepted concept/synchronization counts unchanged, made time-series an explicit design target, and reopened `Relationship` only as a candidate for multi-table/shared-key and possible temporal sequence semantics.

006-B established the active [Operational Authority Continuity & Regressive Recovery Contract](authority/operational-authority-continuity-regressive-recovery-contract.md): a restored historical persistence view cannot by itself re-establish current mutation authority, resurrect superseded Attempts/cancellations/capabilities, or erase later historical reality.

## Current invariant baseline

Until Phase 006 explicitly revises further authority, preserve:

- eleven accepted concepts and fifteen synchronizations;
- `Relationship` provisional only, pending 006-G;
- single-table generation as the current baseline capability, with time-series and multi-table shared-key as explicit Phase 006 design targets;
- model-neutral structured/tabular synthesis;
- semantic completion distinct from runtime/platform completion;
- one Execution with multiple fenced Attempts and explicit recovery/cancellation semantics;
- potentially regressive recovery enters continuity-unverified/recovery-quarantine semantics before write authority resumes;
- rollback cannot resurrect stale writer/cancellation/security authority;
- missing post-restore-point history remains recoverable/unknown/unavailable according to evidence rather than silently becoming absence;
- owner-established Evidence and typed canonical Provenance;
- qualified reproducibility rather than Boolean inheritance;
- explicit dependency/trust/authorization/network/egress distinctions;
- no hidden runtime acquisition/remote fallback/required external telemetry in offline/no-egress profiles;
- capability-negotiated platforms rather than provider-name authority;
- enterprise-scale workflows without mandatory full-corpus driver-local materialization;
- no production implementation until a later explicit implementation-authority phase is approved.

## Next

**006-C — End-to-End Scenario, Exception, Failure & Adversarial Synchronization Validation**

006-C must try to falsify SYNC-01 through SYNC-15 against complete happy-path, failure, restore, topology and security scenarios before the synchronization set is considered closed after Phase 005 planning.

## Documentation governance note

The repository continues to use its project-specific OKF-oriented profile. Strict external OKF 0.2 reserved-file/frontmatter normalization has not been declared complete and remains non-blocking governance debt until separately audited against current external authority.
