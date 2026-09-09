# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Current authority state

**Phase 007 is ACTIVE and incrementally authorized.**

Current state:

```text
007-A  COMPLETE
007-B  COMPLETE
007-C  NOT AUTHORIZED — next eligible subgroup
007-D..007-K  NOT AUTHORIZED
```

Canonical implementation authority:

- `docs/implementation/phase-007-implementation-authority-lock.md`
- `docs/implementation/phase-007-b-bootstrap-execution-authority.md`
- `docs/phases/007/index.md`

No agent may create `src/syngan/` or substantive production package/domain/runtime/platform behavior until 007-C is explicitly authorized.

## Current executable bootstrap

Repository-owned toolchain/verification now exists:

```text
Python >=3.11
uv >=0.12,<0.13
Hatchling
pytest
Hypothesis
pytest-socket
Ruff
mypy
Import Linter
coverage.py / pytest-cov
GitHub Actions Verify workflow
```

The base runtime dependency list is empty.

After explicit dependency provisioning, use:

```text
uv sync --all-groups --no-install-project --locked
uv run --no-sync python tools/verify.py all
uv run --no-sync python tools/verify.py coverage
```

The permanent Verify workflow is read-only and runs from the committed `uv.lock`.

Portable/core pytest denies Python sockets by default. Explicit provisioning may access declared package infrastructure; hidden package/model acquisition, hosted inference, or undeclared runtime fallback is prohibited.

Import Linter is installed but production import contracts are intentionally deferred until 007-C creates the package topology.

## Progressive disclosure

For future implementation work:

1. read `docs/index.md`;
2. read the Phase 007 implementation lock;
3. read `docs/phases/007/index.md`;
4. read only the implementation/architecture authority relevant to the explicitly authorized subgroup;
5. use the repository-owned verification commands and preserve subgroup evidence.

Do not load/copy the full design corpus by default.

## Authority order

```text
docs/authority/
  > concepts / synchronizations
  > experience
  > Phase 006-reconciled architecture
  > Phase 006-reconciled implementation planning
  > Phase 007 implementation authority + explicitly authorized subgroup
  > code / config / tests / migrations
  > runtime/platform/generated state
```

Code does not become authority because it exists or passes tests.

## Locked counts

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
```

No `SYNC-16`.

## Change classification

- Class 0 — local/non-contractual: allowed inside active scope.
- Class 1 — implementation realization: allowed only when traced to active authority and verified.
- Class 2 — public/persisted/compatibility: requires explicit implementation-authority + compatibility/migration evidence.
- Class 3 — architecture-affecting: **STOP** and reopen the smallest architecture/ADR authority.
- Class 4 — semantic/experience: **STOP** and reopen the appropriate upstream design authority.

Do not code around Class 3/4 conflicts.

## Evidence gate

Every material subgroup must retain:

- entry repository/branch/commit;
- authority implemented;
- bounded files and change classes;
- dependencies and rationale;
- commands/tests/fitness results;
- migration/compatibility impact;
- network/offline/security/disclosure impact;
- distributed/recovery/scale implications where relevant;
- explicit non-claims;
- waivers/debt;
- Class 3/4 conflicts;
- explicit next-subgroup authorization decision.

A subgroup is not complete because a command exits zero once.

## Branch/review posture

`main` remains unprotected and the Verify workflow is not currently a required branch check.

007-C must revisit PR/review/required-check policy now that executable verification exists. Do not claim branch protection or required checks until repository state confirms them.

## Non-negotiable design rules

Preserve at minimum:

- restored stale control state != current mutation authority;
- driver import success != distributed worker readiness;
- no hidden dependency/model acquisition or remote fallback;
- topology presets != durable semantic topology;
- production topology must not preclude time-series/multi-table shared-key support;
- resource pressure cannot silently weaken committed semantics;
- synthetic/offline/favorable Evidence != formal privacy guarantee/release approval;
- directly retained/reconstructed/partial/unavailable/unknown history remain distinct;
- semantic completion != runtime/platform success;
- no universal Session/Context/Manager/Metadata/Result/Relationship/DataTopology god-owner.

## Current next boundary

**007-C — Source/Package Topology, Dependency Direction & Architecture-Fitness Enforcement** is next eligible but **NOT AUTHORIZED**.

Do not create `src/syngan/` until the user explicitly proceeds to 007-C.
