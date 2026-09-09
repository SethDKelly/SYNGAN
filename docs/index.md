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

Phase 006 concluded that the design is complete enough for a later explicit implementation-authority phase.

## Phase 007 — active, incrementally authorized

Canonical implementation authority begins with:

- [Phase 007 Implementation Authority Lock](implementation/phase-007-implementation-authority-lock.md)
- [Phase 007-B Bootstrap Execution Authority](implementation/phase-007-b-bootstrap-execution-authority.md)

Current subgroup state:

```text
007-A  COMPLETE
007-B  COMPLETE
007-C  NOT AUTHORIZED — next eligible subgroup
007-D..007-K  NOT AUTHORIZED
```

007-B established the repository-owned executable bootstrap without creating production package behavior:

```text
pyproject.toml
uv.lock
.python-version
tools/verify.py
tests/unit + tests/fitness
.github/workflows/verify.yml
```

The base runtime dependency list remains empty. The permanent Verify workflow is read-only and provisions from the committed lock.

Stable bootstrap commands:

```text
uv sync --all-groups --no-install-project --locked
uv run --no-sync python tools/verify.py all
uv run --no-sync python tools/verify.py coverage
```

Portable-core pytest runs with Python sockets disabled by default. Import Linter is installed but production import contracts remain 007-C work because `src/syngan/` does not yet exist.

## Locked design baseline

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
```

Complete structured-data target remains single-table + time-series + multi-table shared-key with source-derived/local free-form-text support in the complete supported baseline.

## Current next boundary

**007-C — Source/Package Topology, Dependency Direction & Architecture-Fitness Enforcement** is next eligible but **not yet authorized**.

An explicit proceed decision is required before production package/source topology may be created.

## Governance note

The repository uses a project-specific OKF-oriented profile. Strict external OKF 0.2 normalization remains non-blocking while authority is unambiguous.
