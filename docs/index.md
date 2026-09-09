---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design and implementation-planning knowledge bundle for SYNGAN.

## Progressive disclosure

- [Authority](authority/index.md) — methodology/governance/cross-cutting contracts, including operational-authority continuity and self-contained/runtime-distribution closure.
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
- [006-C — End-to-End Scenario, Exception, Failure & Adversarial Synchronization Validation](phases/006/006-C-end-to-end-scenario-exception-failure-adversarial-synchronization-validation.md)
- [006-D — Reference Strategy/Method and Topology Design Probes & Algorithm-Neutrality Stress Test](phases/006/006-D-reference-strategy-method-topology-design-probes-algorithm-neutrality-stress-test.md)

006-A kept the accepted concept/synchronization counts unchanged, made time-series an explicit design target, and reopened `Relationship` only as a candidate for multi-table/shared-key and possible temporal sequence semantics.

006-B established the active [Operational Authority Continuity & Regressive Recovery Contract](authority/operational-authority-continuity-regressive-recovery-contract.md).

006-C adversarially replayed the design across twenty-four scenarios. The synchronization count remains fifteen and no `SYNC-16` is currently justified.

006-D stress-tested Learning-based/direct/text/time-series/multi-table/Evaluation/large-state/Spark-distribution shapes and established the active [Self-Contained Execution & Runtime Distribution Closure Contract](authority/self-contained-execution-runtime-distribution-closure-contract.md).

## Current invariant baseline

Until Phase 006 explicitly revises further authority, preserve:

- eleven accepted concepts and fifteen synchronizations;
- `Relationship` provisional only, pending 006-G;
- single-table generation as the current baseline capability, with time-series and multi-table shared-key as explicit Phase 006 design targets;
- the supported baseline includes at least one source-derived/local free-form-text synthesis path requiring no pretrained artifact or runtime network service;
- externally pretrained/world-knowledge text remains explicit optional local-artifact or runtime-network capability;
- model-neutral structured/tabular synthesis;
- semantic completion distinct from runtime/platform completion;
- one Execution with multiple fenced Attempts and explicit recovery/cancellation semantics;
- same-Execution continuation may be blocked by current authorization/dependency/platform capability without rewriting the commitment;
- coordinated logical-output completion applies to the whole committed scope rather than one constituent;
- potentially regressive recovery enters continuity-unverified/recovery-quarantine semantics before write authority resumes;
- rollback cannot resurrect stale writer/cancellation/security authority;
- missing post-restore-point history is not proof of non-occurrence, and surviving physical effects are not proof of semantic transition;
- driver-local package/model availability is not distributed executor readiness;
- every material runtime worker must satisfy exact compatible runtime distribution closure, including dynamically allocated workers;
- missing runtime dependencies cannot trigger undeclared first-use package/model acquisition;
- large model/Learned-State distribution cannot universally require full driver-memory loading/broadcast;
- owner-established Evidence and typed canonical Provenance;
- unresolved continuity/history gaps may weaken current reproducibility without rewriting historical commitments;
- explicit dependency/trust/authorization/network/egress distinctions;
- capability-negotiated platforms rather than provider-name authority;
- enterprise-scale workflows without mandatory full-corpus driver-local materialization;
- no production implementation until a later explicit implementation-authority phase is approved.

## Next

**006-E — Enterprise Scale, Resource/Approximation, Backpressure & Degraded-Mode Design Validation**

006-E must stress the refined design under enterprise-scale resource pressure, large/sharded state, text/runtime-distribution pressure, dynamic workers, topology-specific scaling, statistical approximation, backpressure and partial/degraded platform capability—without implementing benchmarks.

## Documentation governance note

The repository continues to use its project-specific OKF-oriented profile. Strict external OKF 0.2 reserved-file/frontmatter normalization has not been declared complete and remains non-blocking governance debt until separately audited against current external authority.
