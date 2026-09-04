---
type: Experience Index
title: SYNGAN Experience & Workflow Design
status: active
---

# SYNGAN Experience & Workflow Design

This directory contains canonical actor-visible and programmatic workflow/experience design derived from the accepted concept, synchronization, and authority layers.

Experience authority defines how actors discover, prepare, commit, observe, inspect, recover, and understand SYNGAN work. It does **not** redefine concept ownership or select final UI/API/package/storage/runtime architecture.

## Start here

For cross-workflow architecture/design work, read:

- [Phase 003 Consolidated Experience Contract](phase-003-consolidated-experience-contract.md) — compact cross-workflow invariants and Phase 004 architecture obligations.

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

## Authority boundary

For conflicts:

1. `docs/authority/` governs cross-cutting policy/contracts;
2. `docs/concepts/` governs concept purpose, lifecycle, state, actions, and invariants;
3. `docs/synchronizations/` governs cross-concept coordination;
4. `docs/experience/` governs how those semantics are exposed to actors/programmatic users;
5. phase records preserve design history and rationale.

An experience view MAY compose several concepts for comprehension or task flow. Such composition MUST NOT create a new canonical owner for the combined state.

## Consolidated experience guardrails

The full invariant set is canonical in the [Phase 003 Consolidated Experience Contract](phase-003-consolidated-experience-contract.md). The minimum entry guardrails are:

- pre-commit readiness/compatibility remains contextual and derived;
- semantic commitment remains distinguishable from operational execution;
- checkpoint/candidate/diagnostic material remains distinguishable from promoted domain results;
- Learning/Generation/Evaluation semantic completion remains owned by those concepts, not Execution/platform state;
- Evidence strength remains bounded by method/scope/coverage/uncertainty and remains distinct from external approval;
- historical bindings remain distinct from current aliases/status/reproducibility;
- dependency requirement/availability/identity/permission/network/egress remain distinct;
- hidden acquisition, hidden remote fallback, and silent material dependency substitution are prohibited;
- withheld/redacted, unknown, absent, and unavailable remain distinguishable;
- synthetic/source-derived state is not presumed private or release-authorized;
- human and programmatic surfaces preserve equivalent semantic distinctions;
- ordinary enterprise workflows remain understandable without mandatory full driver-local materialization.

## Representation boundary

These documents do not decide whether the experience is implemented through Python resources/builders, notebooks, CLI, REST/SDK, web UI, Spark extensions, managed-platform integrations, or another surface.

Representation and architecture work is now governed under [SYNGAN Representation & Architecture Design](../architecture/index.md) and must preserve this experience authority.