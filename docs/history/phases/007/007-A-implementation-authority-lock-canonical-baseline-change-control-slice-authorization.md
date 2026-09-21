---
type: Phase Record
title: 007-A — Implementation Authority Lock, Canonical Baseline, Change Control & Slice Authorization
status: complete
---

# 007-A — Implementation Authority Lock, Canonical Baseline, Change Control & Slice Authorization

## Objective

Enter Phase 007 by converting the positive Phase 006 design-readiness decision into a bounded implementation authority, while preventing that readiness decision from becoming unrestricted coding permission.

## Result

**PASS — IMPLEMENTATION AUTHORITY LOCKED; 007-B ONLY AUTHORIZED.**

Canonical implementation authority:

[Phase 007 Implementation Authority Lock](../../implementation/phase-007-implementation-authority-lock.md)

## Entry repository baseline

```text
repository: SethDKelly/SYNGAN
branch:     main
commit:     843a518c12f7482229cfb012da658887cb92dfaa
```

At entry, GitHub reported `main` as unprotected with no required status checks.

007-A therefore does not claim review/branch-protection enforcement that does not yet exist.

## Locked authority chain

Implementation precedence is now explicitly:

```text
design/cross-cutting authority
        ↓
concepts + synchronizations
        ↓
experience
        ↓
Phase 006-reconciled architecture
        ↓
Phase 006-reconciled implementation planning
        ↓
Phase 007 implementation authority + active subgroup
        ↓
code/config/tests/migrations
        ↓
runtime/platform/generated state
```

Implementation may supply feasibility evidence but cannot silently redefine upstream meaning.

## Locked design baseline

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
```

No `SYNC-16`.

The complete structured-data target remains:

```text
single-table
time-series
multi-table shared-key
```

with source-derived/local free-form-text support in the complete supported baseline.

## Change-control decision

005-A change classes remain active and are now explicitly bound to Phase 006 authority:

- Class 0 — local/non-contractual;
- Class 1 — implementation realization;
- Class 2 — public/persisted/compatibility contract;
- Class 3 — architecture-affecting;
- Class 4 — semantic/experience.

Class 3 and Class 4 conflicts are **stop/reopen conditions**. They may not be normalized as implementation convenience.

## Authorization decision

Phase 007 uses incremental subgroup authority.

007-A authorizes **007-B only**.

```text
007-A  complete
007-B  AUTHORIZED
007-C  not authorized
007-D  not authorized
007-E  not authorized
007-F  not authorized
007-G  not authorized
007-H  not authorized
007-I  not authorized
007-J  not authorized
007-K  not authorized
```

Each later subgroup requires prior evidence plus an explicit proceed decision.

## Authorized 007-B surface

007-B may introduce repository/toolchain/verification bootstrap material such as:

- `pyproject.toml`;
- `uv.lock`;
- optional `.python-version`;
- bounded `.gitignore` updates;
- `tools/verify.py` and narrowly scoped verification/bootstrap scripts;
- bootstrap/toolchain-only `tests/unit/`, `tests/fitness/`, `tests/support/` material;
- verification-only `.github/workflows/`;
- PR template, README, AGENTS and documentation updates.

007-B may **not** create `src/syngan/` or substantive domain/application/adapter behavior. That remains 007-C+ work.

## Authorized 007-B toolchain

The accepted initial tooling remains:

```text
Python >=3.11
uv
Hatchling
pytest
Hypothesis
pytest-socket
Ruff
mypy
Import Linter
coverage.py / pytest-compatible coverage integration
GitHub Actions verification-only workflow if introduced
```

No base/runtime PySpark, PyTorch, Hugging Face, Databricks, MLflow, cloud SDK, ORM/database driver, remote-model client or telemetry-export dependency is authorized in 007-B.

## Network/offline decision

Explicit environment/dependency provisioning may use network access.

The portable/core verification profile itself must deny undeclared outbound Python sockets by default and must not normalize model/package download, hosted inference or hidden remote fallback as expected behavior.

## Branch/review decision

Because `main` is currently unprotected and has no required checks:

- explicit subgroup-scoped direct-to-main work is permitted for 007-B;
- direct-to-main is not evidence of independent review or CI enforcement;
- 007-B must establish repository-owned verification entry points and should establish verification CI;
- 007-C must revisit review/PR policy once executable checks exist;
- documentation must not falsely claim branch protection/required checks.

## Evidence gate

Every later material subgroup must record:

- entry commit;
- authority implemented;
- files/change classes;
- dependencies;
- commands/tests/fitness results;
- compatibility/migration effects;
- network/security/disclosure effects;
- recovery/distributed/scale implications where relevant;
- explicit non-claims;
- waivers/debt;
- Class 3/4 conflicts;
- next-subgroup authorization decision.

## Implementation work performed in 007-A

None.

007-A changed documentation/governance authority only. It did not create:

- production package/source code;
- test harness/toolchain configuration;
- dependency lockfiles;
- database schema/migrations;
- runtime/platform/security adapters;
- CI workflows;
- benchmark implementation.

## Exit assessment

**007-A: COMPLETE.**

**Phase 007: ACTIVE.**

**007-B: AUTHORIZED.**

The current production implementation authority is intentionally limited to the 007-B repository/toolchain/verification bootstrap.

## Next subgroup

**007-B — Repository/Toolchain Bootstrap, Reproducible Environment & Verification Harness**
