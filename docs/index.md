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
8. [Phases](phases/index.md) for execution history and planned Phase 007 subgroup authority.

## Authority rule

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation planning
  > future implementation authority
  > code / deployment
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
future explicit implementation-authority phase
        ↓
future code / deployment
```

## Current blocker/debt state

No identified design-readiness blocker remains open after 006-J.

Remaining known debt is primarily implementation/release/governance work: exact algorithms, Spark/runtime distribution mechanism, recovery-frontier mechanism, provider/runtime versions, persistence/API/error spelling, benchmark/SLO evidence, enterprise security products, package-name review and optional strict OKF normalization.

## Planned Phase 007

[Phase 007 — Implementation Authority, Controlled Bootstrap & Evidence-Gated Delivery](phases/007/index.md) now has a completed **logical subgroup design**, but it is **not active**.

Its dependency-safe plan runs from 007-A authority lock through verification/toolchain/source topology and shared implementation foundations to a bounded self-contained single-table Spark-local vertical proof and a 007-K evidence/fitness exit.

The planned first subgroup is:

**007-A — Implementation Authority Lock, Canonical Baseline, Change Control & Slice Authorization**

007-A is governance-only. It must explicitly lock current authority and normally authorize only the next bounded subgroup rather than granting blanket implementation permission across Phase 007.

Until 007-A is explicitly entered and completed, production implementation remains prohibited.

## Documentation governance note

The repository continues to use its project-specific OKF-oriented profile. Strict external OKF 0.2 reserved-file/frontmatter normalization remains non-blocking while authority remains unambiguous.
