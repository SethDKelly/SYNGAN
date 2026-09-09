---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design and implementation-planning knowledge bundle for SYNGAN.

## Progressive disclosure

- [Authority](authority/index.md) — methodology/governance and current cross-cutting recovery, runtime-distribution, enterprise-scale/degraded-operation, privacy/disclosure/release and structured-topology contracts.
- [Problem Knowledge](problem/index.md) — problem, purpose, actors, constraints and enterprise scale envelope.
- [Domain Terminology](terminology/index.md) — canonical vocabulary.
- [Accepted Concepts](concepts/index.md) — current concept authority.
- [Accepted Synchronizations](synchronizations/index.md) — current cross-concept coordination authority.
- [Experience & Workflow Design](experience/index.md) — read the Phase 003 consolidated contract plus the current Phase 006 experience overlay.
- [Representation & Architecture Design](architecture/index.md) — begin with the Phase 004 consolidated architecture contract; 006-I is the current reconciliation phase.
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
- [006-F — Privacy, Disclosure, Release-Governance Boundary & Mechanism-Specific Scope Decision](phases/006/006-F-privacy-disclosure-release-governance-boundary-mechanism-specific-scope-decision.md)
- [006-G — Structured-Data Topology: Single-Table, Time-Series & Multi-Table Relationship Concept/Extensibility Audit](phases/006/006-G-structured-data-topology-single-table-time-series-multi-table-relationship-concept-extensibility-audit.md)
- [006-H — Human/Programmatic Experience Closure for Recovery, Security, Degraded & Historical Workflows](phases/006/006-H-human-programmatic-experience-closure-recovery-security-degraded-historical-workflows.md)

## Current invariant baseline

Until Phase 006 explicitly revises further authority, preserve:

- eleven accepted concepts and fifteen synchronizations;
- structural relationship semantics are Data Meaning-owned, not a standalone Relationship concept;
- the first complete structured-data capability baseline includes single-table, time-series and multi-table shared-key generation;
- implementation may be staged and Strategies may support subsets, but the complete baseline claim requires at least one supported self-contained Strategy path for each family;
- topology convenience presets are not semantic authority and must not prevent composite topology;
- self-contained source-derived free-form-text capability is required in the supported baseline;
- externally pretrained/world-knowledge text remains explicit optional local-artifact or runtime-network capability;
- driver-local package/model availability is not distributed executor readiness;
- every material worker must satisfy exact compatible runtime distribution closure;
- enterprise-scale compatibility is multidimensional and cannot hide source-size-proportional driver stages;
- resource pressure may queue/block/retry but cannot silently weaken committed semantics;
- approximation remains explicit owner-bound semantics;
- degraded operation is capability-specific;
- synthetic origin, offline execution and favorable privacy-related Evidence do not imply formal privacy/anonymization;
- differential privacy is deferred from the initial baseline and future composable DP requires concept discovery before implementation;
- Use/Release Decision remains external to current SYNGAN concept authority;
- semantic completion remains distinct from runtime/platform completion;
- regressive recovery cannot resurrect stale writer/cancellation/security authority;
- actor/programmatic experience preserves orthogonal semantic, operational, actionability, continuity, disclosure and historical-knowledge dimensions rather than one universal status;
- queued/blocked/incompatible/limited/indeterminate remain distinguishable;
- reconstructed/partial/unknown history remains explicit;
- existence-protected resources may use non-disclosing outward responses without rewriting internal/canonical truth;
- owner-established Evidence and typed canonical Provenance remain distinct from projections/telemetry/security audit;
- no production implementation until a later explicit implementation-authority phase is approved.

## Current next

**006-I — Architecture/ADR Reconciliation, Canonical Authority Promotion & Planning Back-Propagation**

006-I must reconcile the accepted Phase 006 contracts and experience into Phase 004 architecture/ADRs and then back-propagate the resulting current authority into the frozen Phase 005 implementation-planning baseline without rewriting phase history.

## Documentation governance note

The repository continues to use its project-specific OKF-oriented profile. Strict external OKF 0.2 reserved-file/frontmatter normalization has not been declared complete and remains non-blocking governance debt until separately audited against current external authority.
