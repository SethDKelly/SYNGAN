---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design and implementation-planning knowledge bundle for SYNGAN.

## Progressive disclosure

- [Authority](authority/index.md) — methodology/governance/cross-cutting contracts, including operational-authority continuity, self-contained/runtime-distribution closure and enterprise-scale/resource/degraded-operation rules.
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
- [006-E — Enterprise Scale, Resource/Approximation, Backpressure & Degraded-Mode Design Validation](phases/006/006-E-enterprise-scale-resource-approximation-backpressure-degraded-mode-design-validation.md)

Current Phase 006 cross-cutting authority includes:

- [Operational Authority Continuity & Regressive Recovery Contract](authority/operational-authority-continuity-regressive-recovery-contract.md)
- [Self-Contained Execution & Runtime Distribution Closure Contract](authority/self-contained-execution-runtime-distribution-closure-contract.md)
- [Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract](authority/enterprise-scale-resource-admission-approximation-degraded-operation-contract.md)

## Current invariant baseline

Until Phase 006 explicitly revises further authority, preserve:

- eleven accepted concepts and fifteen synchronizations;
- `Relationship` provisional only, pending 006-G;
- single-table generation as the current baseline topology, with time-series and multi-table shared-key as explicit design targets;
- at least one self-contained source-derived free-form-text synthesis path in the supported baseline;
- optional pretrained/world-knowledge text remains explicit local-artifact or runtime-network capability;
- driver-local availability is not cluster readiness; every material worker must satisfy compatible runtime closure;
- no hidden first-use dependency/model acquisition;
- large state/model distribution cannot universally require driver-memory loading/broadcast;
- enterprise compatibility is multidimensional and workload-specific;
- undisclosed source-size-proportional driver/single-process stages invalidate enterprise-scale claims for that path;
- resource pressure may queue/block/retry work but MUST NOT silently weaken committed semantics;
- approximation is explicit owner-bound semantics, not a hidden runtime fallback;
- backpressure is lossless with respect to mandatory logical scope;
- degraded operation is capability-specific rather than one global state;
- sampled/sketched Evaluation cannot claim stronger Evidence because exhaustive validation is expensive;
- semantic completion remains distinct from runtime/platform/progress completion;
- one Execution may span multiple fenced Attempts with explicit recovery/cancellation semantics;
- potentially regressive recovery enters continuity-unverified/recovery-quarantine semantics before write authority resumes;
- owner-established Evidence and typed canonical Provenance remain distinct from projections/telemetry/security audit;
- no production implementation until a later explicit implementation-authority phase is approved.

## Next

**006-F — Privacy, Disclosure, Release-Governance Boundary & Mechanism-Specific Scope Decision**

006-F must revalidate privacy/disclosure/release authority in light of self-contained text generation, memorization/disclosure risk, enterprise-scale sampling/approximation, optional pretrained/network text, and possible mechanism-specific guarantees such as differential privacy—without implementing any privacy mechanism or release-governance system.

## Documentation governance note

The repository continues to use its project-specific OKF-oriented profile. Strict external OKF 0.2 reserved-file/frontmatter normalization has not been declared complete and remains non-blocking governance debt until separately audited against current external authority.
