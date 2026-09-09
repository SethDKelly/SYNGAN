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
8. [Phases](phases/index.md) for execution evidence/current authorization

## Authority order

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation planning
  > Phase 007 implementation authority + explicitly authorized subgroup
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

Phase 006 concluded that design was complete enough for an explicit implementation-authority phase.

## Phase 007 — active, incrementally authorized

Current implementation authority includes:

- [Phase 007 Implementation Authority Lock](implementation/phase-007-implementation-authority-lock.md)
- [Phase 007-B Bootstrap Execution Authority](implementation/phase-007-b-bootstrap-execution-authority.md)
- [Phase 007-C Source/Package Topology Execution Authority](implementation/phase-007-c-source-package-topology-execution-authority.md)

Current subgroup state:

```text
007-A  COMPLETE
007-B  COMPLETE
007-C  COMPLETE
007-D  NOT AUTHORIZED — next eligible subgroup
007-E..007-K  NOT AUTHORIZED
```

007-B established the reproducible Python/tool/test/CI substrate. 007-C then established and enforced the first production package architecture:

```text
src/syngan/
├── __init__.py
├── py.typed
├── foundation/
├── domain/
├── ports/
├── application/
├── api/
├── adapters/
└── bootstrap/
```

Import Linter now enforces inward core layering and outer adapter/composition boundaries. Normal verification installs the first-party package, runs architecture fitness, and builds/inspects wheel + sdist without publication.

`[project].dependencies` remains empty. Hatchling and `editables` are locked build/development tooling for installed-project verification, not runtime capabilities.

Current reproducible verification sequence:

```text
uv sync --all-groups --no-install-project --locked
uv sync --all-groups --locked --no-build-isolation
uv run --no-sync python tools/verify.py all
```

Portable-core pytest remains Python-socket denied after explicit provisioning.

007-C was implemented through PR #1, verified on exact PR head `9f93b6eff7f8d8a1b19950745530dc273d462d6d`, and merged as `063f847953f69a525ee04315fa92bc0e9fa36a1c`.

## Locked design baseline

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
```

Complete structured-data target remains single-table + time-series + multi-table shared-key with source-derived/local free-form-text support in the complete supported baseline.

## Current next boundary

**007-D — Identity, Revision, Serialization, Typed Public Resource/Handle & Programmatic-View Foundation** is next eligible but **not yet authorized**.

An explicit proceed decision is required before 007-D implementation begins.

## Governance note

The repository uses a project-specific OKF-oriented profile. Strict external OKF 0.2 normalization remains non-blocking while authority is unambiguous.
