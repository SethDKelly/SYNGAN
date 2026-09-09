---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design and implementation-planning knowledge bundle for SYNGAN.

## Progressive disclosure

Read only the layers needed for the task:

1. [Authority](authority/index.md) — methodology/governance plus Phase 006 cross-cutting contracts.
2. [Accepted Concepts](concepts/index.md) and [Synchronizations](synchronizations/index.md).
3. [Experience](experience/index.md) — Phase 003 baseline plus the Phase 006 experience overlay.
4. [Architecture](architecture/index.md) — **begin with the Phase 006 Architecture Reconciliation Contract**.
5. [Implementation Planning](implementation/index.md) — **begin with the Phase 006 Implementation-Planning Reconciliation**.
6. [ADRs](decisions/index.md) for rationale/history.
7. [Backlog](backlog/index.md) for non-authoritative blocker/deferred classification.
8. [Phases](phases/index.md) for execution history/current group.

## Authority rule

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation planning
  > future code / deployment
  > ADR rationale / phase history / backlog / examples
```

Later feasibility may reopen upstream authority explicitly; later layers never silently redefine earlier semantics.

## Completed layers

- **Phase 001 — Design Foundation & Concept Discovery — complete**
- **Phase 002 — Concept Specification & Invariant Refinement — complete** — 11 concepts / 15 synchronizations.
- **Phase 003 — Experience & Workflow Design — complete historical baseline**
- **Phase 004 — Representation & Architecture Design — complete historical baseline**
- **Phase 005 — Implementation Planning & Delivery Decomposition — complete as planning only**
- **Phase 006 — Post-Planning Design Validation & Adversarial Refinement — current**

No production implementation has begun or been authorized.

## Current Phase 006 authority

Phase 006 has completed 006-A through **006-I**.

Current cross-cutting authority includes:

- [Operational Authority Continuity & Regressive Recovery](authority/operational-authority-continuity-regressive-recovery-contract.md)
- [Self-Contained Execution & Runtime Distribution Closure](authority/self-contained-execution-runtime-distribution-closure-contract.md)
- [Enterprise Scale, Resource Admission, Approximation & Degraded Operation](authority/enterprise-scale-resource-admission-approximation-degraded-operation-contract.md)
- [Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary](authority/privacy-disclosure-formal-guarantee-release-boundary-contract.md)
- [Structured-Data Topology & Relationship Semantics](authority/structured-data-topology-relationship-semantics-contract.md)
- [Phase 006 Recovery, Security, Degraded, Historical & Topology Experience Contract](experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md)
- [Phase 006 Architecture Reconciliation Contract](architecture/phase-006-architecture-reconciliation-contract.md)
- [Phase 006 Implementation-Planning Reconciliation](implementation/phase-006-implementation-planning-reconciliation.md)

## Current invariant baseline

Preserve at least:

- 11 accepted concepts / 15 synchronizations; no `SYNC-16`;
- `Relationship` remains Data Meaning-owned structural semantics, not a standalone concept;
- complete structured-data baseline target = single-table + time-series + multi-table shared-key;
- at least one supported self-contained Strategy path required for each baseline topology family before claiming complete baseline support;
- source-derived/local free-form text support in the baseline, with pretrained/network text optional and explicit;
- driver import/runtime availability != cluster worker readiness;
- every material worker must satisfy exact compatible runtime closure;
- no hidden dependency/model acquisition or remote fallback;
- large state/model distribution cannot universally require driver broadcast;
- resource pressure may queue/block/retry but cannot weaken quantity/horizon/topology/Evaluation/Constraint/security semantics;
- synthetic/offline/favorable privacy Evidence != formal privacy/anonymization/release approval;
- formal DP is deferred and future composable DP requires concept discovery before implementation;
- potentially regressive restore cannot resurrect stale writer/cancellation/security authority;
- fresh non-regressing recovery authority is required before mutation resumes;
- historical fact, reconstructed fact, partial history, unavailable material and unknown occurrence remain distinct;
- public/programmatic state preserves actionability/recovery/disclosure/history dimensions instead of one universal status;
- canonical history, telemetry and security audit remain distinct;
- production implementation requires a later explicit implementation-authority phase.

## Current architecture/ADR state

Current architecture precedence:

```text
Phase 006 authority + experience
        ↓
Phase 006 Architecture Reconciliation
        ↓
Phase 004 baseline
        ↓
Phase 006 Implementation-Planning Reconciliation
        ↓
Phase 005 planning details
```

The active ADR set is **ADR-0001 through ADR-0010**. ADR-0009 adds non-regressing recovery authority; ADR-0010 adds self-contained distributed runtime closure. No prior ADR is superseded.

## Current blocker state

BDR-001 through BDR-004 have accepted closure through 006-I. No identified Phase 006 design blocker remains open, but 006-J must still perform a residual design-debt/readiness audit and may discover new blocking evidence.

## Current next

**006-J — Phase 006 Consolidation, Residual Design-Debt Audit & Implementation-Authority Readiness Decision**

006-J may either approve creation of a later explicit implementation-authority phase or require further design refinement. It does not itself authorize coding.

## Documentation governance note

The repository continues to use its project-specific OKF-oriented profile. Strict external OKF 0.2 reserved-file/frontmatter normalization has not been declared complete and remains non-blocking governance debt unless it creates authority ambiguity.
