---
type: Experience Index
title: SYNGAN Experience & Workflow Design
status: active
---

# SYNGAN Experience & Workflow Design

This directory contains canonical actor-visible and programmatic workflow/experience design derived from the accepted concept, synchronization, and authority layers.

Experience authority defines how actors discover, prepare, commit, observe, inspect, recover, and understand SYNGAN work. It does **not** redefine concept ownership or select final UI/API/package/storage/runtime architecture.

## Start here

For current cross-workflow architecture/design work, read:

1. [Phase 003 Consolidated Experience Contract](phase-003-consolidated-experience-contract.md) — the original four-barrier experience model and foundational invariants;
2. [Phase 006 Recovery, Security, Degraded, Historical & Topology Experience Contract](phase-006-recovery-security-degraded-history-topology-experience-contract.md) — current post-planning refinements for recovery continuity, actionability, runtime closure, security/disclosure, history, privacy/release and structured topology.

The Phase 006 contract refines current experience authority without rewriting Phase 003 history.

Then follow only the detailed experience authority relevant to the task.

## Detailed experience authority

- [Workflow Entry, Source Context & Lifecycle Orientation](workflow-entry-source-context-lifecycle-orientation.md) — intent-oriented entry, source/history context, editable-versus-committed state, semantic-versus-operational lifecycle.
- [Data Meaning, Constraint & Strategy Preparation](data-meaning-constraint-strategy-preparation.md) — declared/inferred/unresolved meaning, contextual Constraint applicability/handling, Strategy compatibility, derived readiness, review-before-commit.
- [Learning & Learned State Lifecycle](learning-learned-state-lifecycle.md) — Learning commitment/observation/recovery, checkpoint non-finality, semantic Learned State promotion, reuse/restriction/retirement/invalidation.
- [Generation Request, Condition, Validation & Output Promotion](generation-request-condition-validation-output-promotion.md) — Generation intent, mandatory/best-effort Conditions, candidate output, requirement-specific Evidence, semantic completed-output promotion.
- [Evaluation, Evidence & Review](evaluation-evidence-review.md) — Criterion-first evaluation, method/claim-strength compatibility, Evidence interpretation, multidimensional review, decision-authority boundary.
- [Execution Monitoring, Failure, Recovery & Cancellation](execution-monitoring-failure-recovery-cancellation.md) — one logical Execution across Attempts/platform jobs, retry/resume qualification, unknown-state reconciliation, cancellation races, operator authority boundary.
- [Provenance, Reproducibility & Historical Inspection](provenance-reproducibility-historical-inspection.md) — result explanation, derivation comparison, historical/current-state separation, qualified reproducibility assessment.
- [Enterprise Dependency, Offline/No-Egress & Safety](enterprise-dependency-offline-no-egress-safety.md) — dependency profiles/resolution/permission, provisioning/runtime network, egress disclosure, sensitive derived state, truthful restricted disclosure.

## Current Phase 006 experience refinements

Current surfaces must preserve orthogonal distinctions among:

- owner semantic state;
- Execution/Attempt operational state;
- current actionability (`runnable`, `queued`, `blocked`, `incompatible`, explicit limitations, or indeterminate where materially relevant);
- post-recovery authority continuity;
- disclosure/withholding state;
- historical knowledge quality;
- Strategy/topology compatibility.

Key current rules include:

- potentially regressive recovery must expose that current mutation authority is unverified until a non-regressing boundary is established;
- restored state must not be presented as complete current truth when post-backup history may be missing;
- reconstructed history remains distinguishable from directly retained canonical history;
- `queued` remains distinct from blocked/incompatible/denied/failure;
- degradation is capability-specific rather than one global status;
- driver/package readiness is not proof of distributed worker runtime closure;
- withheld/redacted/unknown/unavailable/absent remain distinguishable where policy permits, while existence-protected resources may use deliberately non-disclosing outward responses;
- synthetic origin, disclosure Evidence, formal privacy guarantee, current export authorization and external release/use approval remain separate;
- topology presets are convenience syntax and must resolve to inspectable single-table/time-series/multi-table/composite semantics;
- constituent progress does not establish whole-result completion;
- human and programmatic surfaces preserve equivalent material semantics;
- ordinary enterprise-scale experience remains bounded.

## Authority boundary

For conflicts:

1. `docs/authority/` governs cross-cutting policy/contracts;
2. `docs/concepts/` governs concept purpose, lifecycle, state, actions, and invariants;
3. `docs/synchronizations/` governs cross-concept coordination;
4. `docs/experience/` governs how those semantics are exposed to actors/programmatic users;
5. phase records preserve design history and rationale.

An experience view MAY compose several concepts for comprehension or task flow. Such composition MUST NOT create a new canonical owner for the combined state.

## Representation boundary

These documents do not decide whether the experience is implemented through Python resources/builders, notebooks, CLI, REST/SDK, web UI, Spark extensions, managed-platform integrations, or another surface.

Representation and architecture work is governed under [SYNGAN Representation & Architecture Design](../architecture/index.md) and must preserve both the Phase 003 and current Phase 006 experience authority.