---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design & Implementation Knowledge
status: active
---

# SYNGAN Design & Implementation Knowledge

This directory is the canonical knowledge bundle for SYNGAN.

## Progressive disclosure

Read only what the active task needs:

1. [Authority](authority/index.md)
2. [Concepts](concepts/index.md) + [Synchronizations](synchronizations/index.md)
3. [Experience](experience/index.md)
4. [Architecture](architecture/index.md)
5. [Implementation Planning & Authority](implementation/index.md)
6. [ADRs](decisions/index.md) for rationale
7. [Backlog](backlog/index.md) for deferred work
8. [Phases](phases/index.md) for current execution history/authorization

## Authority order

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation planning
  > active Phase 007 implementation authority
  > code / deployment
  > ADR rationale / phase history / backlog / examples
```

Implementation feasibility may reopen upstream design explicitly; implementation never silently redefines it.

## Completed design/planning baseline

- Phase 001 — complete
- Phase 002 — complete — 11 concepts / 15 synchronizations
- Phase 003 — complete historical experience baseline
- Phase 004 — complete historical architecture baseline
- Phase 005 — complete implementation planning baseline
- Phase 006 — complete post-planning design validation/readiness

Phase 006 concluded:

```text
DESIGN COMPLETE ENOUGH FOR A LATER
EXPLICIT IMPLEMENTATION-AUTHORITY PHASE
```

## Phase 007 — active, incrementally authorized

Canonical current implementation authority:

[Phase 007 Implementation Authority Lock](implementation/phase-007-implementation-authority-lock.md)

Phase 007 entry baseline:

```text
repository: SethDKelly/SYNGAN
branch:     main
commit:     843a518c12f7482229cfb012da658887cb92dfaa
```

Current subgroup state:

```text
007-A  COMPLETE
007-B  AUTHORIZED / NEXT
007-C..007-K  NOT AUTHORIZED
```

The current production implementation authority extends **only** to 007-B repository/toolchain/verification bootstrap.

007-B may add project metadata, lock state, declared build/test/static-analysis tooling, verification scripts/bootstrap tests and verification-only CI. It may not create `src/syngan/` or substantive domain/runtime/platform behavior.

## Locked design baseline

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
```

No `SYNC-16`.

Complete structured-data target:

```text
single-table
time-series
multi-table shared-key
```

The complete supported baseline also requires source-derived/local free-form-text synthesis with no required public model hub or runtime inference service.

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
Phase 005 detailed planning where not refined
        ↓
Phase 007 Implementation Authority Lock
        ↓
active authorized subgroup
        ↓
implementation
```

## Current next

**007-B — Repository/Toolchain Bootstrap, Reproducible Environment & Verification Harness**

Later Phase 007 groups require explicit authorization after the prior group's evidence gate.

## Governance note

The repository uses a project-specific OKF-oriented profile. Strict external OKF 0.2 normalization remains non-blocking while authority is unambiguous.
