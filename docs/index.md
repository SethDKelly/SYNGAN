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

1. [Authority](authority/index.md) — methodology/governance plus current readiness authority.
2. [Accepted Concepts](concepts/index.md) and [Synchronizations](synchronizations/index.md).
3. [Experience](experience/index.md) — Phase 003 baseline plus Phase 006 experience overlay.
4. [Architecture](architecture/index.md) — begin with the Phase 006 Architecture Reconciliation Contract.
5. [Implementation Planning](implementation/index.md) — begin with the Phase 006 Implementation-Planning Reconciliation.
6. [ADRs](decisions/index.md) for rationale/history.
7. [Backlog](backlog/index.md) for non-authoritative deferred implementation/release work.
8. [Phases](phases/index.md) for execution history.

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

## Completed design/planning phases

- **Phase 001 — Design Foundation & Concept Discovery — complete**
- **Phase 002 — Concept Specification & Invariant Refinement — complete**
- **Phase 003 — Experience & Workflow Design — complete historical baseline**
- **Phase 004 — Representation & Architecture Design — complete historical baseline**
- **Phase 005 — Implementation Planning & Delivery Decomposition — complete as planning only**
- **Phase 006 — Post-Planning Design Validation & Adversarial Refinement — complete**

No production implementation has begun or been authorized.

## Current readiness authority

[Phase 006 Consolidated Design Readiness Contract](authority/phase-006-consolidated-design-readiness-contract.md)

Phase 006-J concluded:

```text
DESIGN COMPLETE ENOUGH FOR A LATER
EXPLICIT IMPLEMENTATION-AUTHORITY PHASE
```

This permits creation/entry of a later explicit implementation-authority phase. It does **not** authorize coding on its own.

## Current baseline

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
```

No `SYNC-16` and no provisional concept remains.

The complete structured-data baseline target is:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

with composable topology and self-contained supported Strategy paths. The supported baseline also requires source-derived/local free-form-text synthesis with no mandatory pretrained model hub or runtime inference service.

## Current implementation-facing precedence

```text
Phase 006 design authority / experience
        ↓
Phase 006 Architecture Reconciliation
        ↓
Phase 004 baseline where not refined
        ↓
Phase 006 Implementation-Planning Reconciliation
        ↓
Phase 005 planning where not refined
        ↓
future implementation-authority phase
```

## Current blocker/debt state

No identified design-readiness blocker remains open after 006-J.

Remaining known debt is primarily implementation/release/governance work: exact algorithms, Spark/runtime distribution mechanism, recovery-frontier mechanism, provider/runtime versions, persistence/API/error spelling, benchmark/SLO evidence, enterprise security products, package-name review and optional strict OKF normalization.

## Recommended next phase

**Phase 007 — Implementation Authority, Controlled Bootstrap & Evidence-Gated Delivery** is the recommended next phase.

It is not active until explicitly entered. Its first subgroup must lock current authority, repository/toolchain/change-control boundaries, verification gates and which implementation slices are authorized.

## Documentation governance note

The repository continues to use its project-specific OKF-oriented profile. Strict external OKF 0.2 reserved-file/frontmatter normalization remains non-blocking while authority remains unambiguous.
