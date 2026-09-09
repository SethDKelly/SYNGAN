# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Current authority state

**Phase 007 is ACTIVE and incrementally authorized.**

Current state:

```text
007-A  COMPLETE
007-B  COMPLETE
007-C  COMPLETE
007-D  NOT AUTHORIZED — next eligible subgroup
007-E..007-K  NOT AUTHORIZED
```

Canonical implementation authority currently includes:

- `docs/implementation/phase-007-implementation-authority-lock.md`
- `docs/implementation/phase-007-b-bootstrap-execution-authority.md`
- `docs/implementation/phase-007-c-source-package-topology-execution-authority.md`
- `docs/phases/007/index.md`

No agent may begin 007-D identity/revision/serialization/public-resource behavior until the user explicitly authorizes that subgroup.

## Executable substrate through 007-C

The production package structure now exists:

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

These are responsibility boundaries, not concepts.

Import Linter enforces:

```text
api -> application -> ports -> domain -> foundation

core packages !-> adapters/bootstrap
adapters !-> application/api/bootstrap
```

Do not bypass these contracts through dynamic import tricks, broad re-export modules, shared generic packages, or test-only path manipulation.

## Toolchain / verification

Current repository-owned stack:

```text
Python >=3.11
uv >=0.12,<0.13
Hatchling
editables
pytest
Hypothesis
pytest-socket
Ruff
mypy
Import Linter
coverage.py / pytest-cov
GitHub Actions Verify
```

`[project].dependencies` remains empty at 007-C exit. Hatchling and `editables` are build/development tooling, not runtime capabilities.

After explicit dependency provisioning, use:

```text
uv sync --all-groups --no-install-project --locked
uv sync --all-groups --locked --no-build-isolation
uv run --no-sync python tools/verify.py all
uv run --no-sync python tools/verify.py coverage
```

Normal verification installs the first-party package, runs lint/format/type/unit/architecture/fitness gates, verifies package imports/`py.typed`, and builds/inspects wheel + sdist without publication.

Portable/core pytest denies Python sockets by default. Explicit provisioning may access declared package infrastructure; hidden package/model acquisition, hosted inference or undeclared runtime fallback is prohibited.

## Progressive disclosure

For implementation work:

1. read `docs/index.md`;
2. read the Phase 007 implementation lock;
3. read `docs/phases/007/index.md`;
4. read the enduring 007-C topology authority;
5. read only the implementation/architecture authority relevant to the explicitly authorized current subgroup;
6. use repository-owned verification and preserve exact subgroup evidence.

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

## Source topology guardrails

Preserve at minimum:

- `foundation` imports no other SYNGAN top-level package;
- `domain` depends inward on `foundation` only;
- `ports` depends only on `foundation/domain`;
- `application` depends only on `foundation/domain/ports`;
- `api` depends only on `foundation/domain/ports/application`;
- `adapters` may depend on `foundation/domain/ports`, not `application/api/bootstrap`;
- `bootstrap` is composition-only;
- root `syngan.__init__` stays small and side-effect free;
- root import must not force optional Spark/model/platform dependencies into the base closure;
- do not introduce universal `utils`, `context`, `config`, `manager`, `registry`, `metadata`, `state`, `result`, `relationship` or `data_topology` god-owner packages;
- production source must not import test support;
- use installed-package verification, not `PYTHONPATH=src` as a substitute.

If a later slice needs to change these boundaries, classify it as a potential Class 3 issue before proceeding.

## Change classification

- Class 0 — local/non-contractual: allowed inside active scope.
- Class 1 — implementation realization: allowed only when traced to active authority and verified.
- Class 2 — public/persisted/compatibility: requires explicit implementation authority + compatibility/migration evidence.
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

`main` remains unprotected and Verify is not claimed as a required branch check.

007-C successfully used PR #1 and a green Verify result on the exact reviewed head before merge. Material production-source work SHOULD continue using reviewable branches/PRs when supported and retain exact-head verification evidence.

Do not describe direct-to-main as independent review and do not claim branch-protection enforcement unless repository state confirms it.

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

**007-D — Identity, Revision, Serialization, Typed Public Resource/Handle & Programmatic-View Foundation** is next eligible but **NOT AUTHORIZED**.

Do not begin 007-D until the user explicitly proceeds.
