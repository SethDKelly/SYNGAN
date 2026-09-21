---
type: Phase Record
title: 007-B — Repository/Toolchain Bootstrap, Reproducible Environment & Verification Harness
status: complete
---

# 007-B — Repository/Toolchain Bootstrap, Reproducible Environment & Verification Harness

## Objective

Realize the bounded executable bootstrap authorized by 007-A: repository-owned Python/build/test/static-analysis metadata, reproducible dependency resolution, stable verification commands, portable-core socket denial, bootstrap fitness checks, and read-only verification CI — without creating production `syngan` source or substantive domain/runtime/platform behavior.

## Result

**PASS — REPRODUCIBLE BOOTSTRAP AND VERIFICATION SUBSTRATE ESTABLISHED.**

007-B is complete. 007-C is the next eligible subgroup but is **not authorized by this record**; explicit proceed authority is still required.

## Entry baseline

```text
repository: SethDKelly/SYNGAN
branch:     main
commit:     f71df8c6f4d9fefdfda7fac5284c261acdc56d25
```

At entry, the repository was still documentation-only and `main` was unprotected with no required status checks.

## Governing implementation authority

- [Phase 007 Implementation Authority Lock](../../implementation/phase-007-implementation-authority-lock.md)
- [Phase 007-B Bootstrap Execution Authority](../../implementation/phase-007-b-bootstrap-execution-authority.md)
- Phase 006-reconciled architecture/planning and the Phase 005-C/005-B tooling/verification authorities.

## Change classification

007-B changes were Class 1 implementation-realization/bootstrap work plus Class 0 documentation/navigation maintenance.

No Class 2 public/persisted product contract, Class 3 architecture conflict, or Class 4 semantic/experience conflict was introduced.

## Files/surfaces introduced

Executable bootstrap material includes:

```text
pyproject.toml
uv.lock
.python-version
.gitignore
tools/verify.py
tests/unit/test_bootstrap_metadata.py
tests/fitness/test_phase_007_authority_boundary.py
tests/fitness/test_portable_core_network_default.py
.github/workflows/verify.yml
```

Supporting authority/navigation/review documentation was also updated.

No `src/syngan/` tree exists.

## Toolchain realization

The repository now declares:

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
```

The generated lock was resolved using uv 0.12.11.

Current GitHub Actions bootstrap/verification actions were checked during the subgroup and the permanent workflow uses exact current releases for checkout/setup-python/setup-uv.

## Dependency boundary

`[project].dependencies` remains empty.

Only build/development/verification dependencies were added.

No production runtime dependency was added for Spark, PyTorch, Transformers/Hugging Face, Databricks, MLflow, cloud SDKs, databases/ORMs, remote-model services, or telemetry exporters.

## Reproducible lock evidence

The initial CI bootstrap resolved a universal hash-bearing `uv.lock` successfully.

Because the connected repository API could read the generated workflow artifact but could not directly materialize those artifact bytes into a repository file, 007-B recorded an explicit one-time bootstrap authority for a temporary writable workflow.

That workflow:

1. generated `uv.lock` from committed metadata;
2. provisioned the locked environment;
3. ran all repository verification gates successfully;
4. verified `uv.lock` was the only generated repository change;
5. committed only `uv.lock` as `e278dc04a8bdd6a8f4da8f417f0720745c67194f`;
6. was removed immediately afterward.

The permanent workflow has read-only repository permission.

## Verification evidence and corrective history

### Initial useful failure

The first complete bootstrap run resolved and provisioned dependencies successfully but failed Ruff on `UP036` because the verification script intentionally retained an explicit Python-version guard even though Ruff targeted Python 3.11.

The guard was kept for direct invocation outside the managed uv environment and received a narrow documented suppression rather than weakening the lint rules.

### Toolchain freshness correction

The first workflow also exposed deprecated GitHub Action runtime warnings. Current releases were checked and the bootstrap was updated to contemporary action majors/releases and current uv 0.12.11 rather than inheriting an older locally available uv family.

### Green lock-generation verification

GitHub Actions run `34375980227` successfully completed:

```text
resolve lockfile                     PASS
provision locked environment         PASS
repository verification gates        PASS
retain generated lockfile            PASS
```

### Green controlled lock materialization

GitHub Actions run `34376719123` successfully completed verification, confirmed `uv.lock` was the sole generated repository change, and materialized only that lockfile.

### Green permanent read-only verification

GitHub Actions run `34376826414` successfully completed:

```text
uv lock --check                      PASS
uv sync --all-groups --no-install-project --locked
                                      PASS
tools/verify.py all                  PASS
```

A final green run on the completed 007-B documentation/test state is required before this record is treated as the final repository-head evidence; subsequent documentation commits do not weaken the gate.

## Repository-owned verification interface

Stable profiles are exposed through:

```text
uv run --no-sync python tools/verify.py bootstrap
uv run --no-sync python tools/verify.py lint
uv run --no-sync python tools/verify.py format
uv run --no-sync python tools/verify.py type
uv run --no-sync python tools/verify.py unit
uv run --no-sync python tools/verify.py fitness
uv run --no-sync python tools/verify.py coverage
uv run --no-sync python tools/verify.py all
```

After explicit provisioning, the normal bootstrap is:

```text
uv sync --all-groups --no-install-project --locked
uv run --no-sync python tools/verify.py all
```

## Portable-core network boundary

Pytest is configured with `--disable-socket` by default.

An executable fitness test asserts that ordinary socket creation raises `pytest_socket.SocketBlockedError`.

This does not prohibit explicit dependency provisioning. It prohibits undeclared network/model/package acquisition during the portable-core verification profile.

Future local Spark tests may require narrowly scoped loopback/process allowances, but those are not authorized or implemented in 007-B.

## Architecture-fitness bootstrap

007-B creates a real `tests/fitness/` authority surface and verifies that:

- Phase 007 authority remains incremental;
- no production source tree appears before 007-C authority;
- portable-core sockets are denied by default.

AF-21 through AF-28 remain future behavior/architecture fitness obligations. They are not fabricated before the domain/runtime structures they test exist.

Import Linter is installed as the selected package-dependency fitness mechanism, but import contracts are intentionally deferred to 007-C because production package topology does not yet exist.

## Coverage posture

pytest-cov/coverage.py is installed and `tools/verify.py coverage` supplies a stable diagnostic profile.

No universal coverage threshold is treated as a correctness oracle; architecture/contract verification remains the governing gate.

## Branch/review status

The permanent `.github/workflows/verify.yml` runs on push, pull request and manual dispatch with `contents: read`.

`main` remains unprotected and the Verify workflow is not currently a required branch check. 007-B therefore does not claim branch-protection enforcement.

007-C must revisit PR/review and required-check policy now that executable verification infrastructure exists.

## Explicit non-claims

007-B does not establish or claim:

- production `syngan` source/package behavior;
- final import-linter production dependency rules in executable form;
- Spark/distributed-runtime correctness;
- synthesis Strategy/model behavior;
- persistence/migration behavior;
- runtime dependency closure across Spark executors;
- enterprise-scale performance/support thresholds;
- privacy/anonymization guarantees;
- release/publishing readiness.

## Conflict review

No Class 3 architecture or Class 4 semantic/experience conflict was discovered.

The encountered issues were ordinary toolchain/configuration realization defects and were corrected inside 007-B authority.

## Exit decision

**007-B: COMPLETE.**

**007-C: NOT YET AUTHORIZED.**

007-C is now eligible to be entered after an explicit proceed decision.

Until then, `src/syngan/` and substantive production package topology/behavior remain outside current implementation authority.
