---
type: Implementation Index
title: SYNGAN Implementation Planning & Delivery Authority
status: active
---

# SYNGAN Implementation Planning & Delivery Authority

## Current authority

Phase 007 remains active under:

- [Phase 007 Implementation Authority Lock](phase-007-implementation-authority-lock.md)
- [Phase 007-B Bootstrap Execution Authority](phase-007-b-bootstrap-execution-authority.md)

Current subgroup state:

```text
007-A  complete
007-B  complete
007-C  NOT AUTHORIZED — next eligible
007-D..007-K  NOT AUTHORIZED
```

No production package/source topology beyond the completed bootstrap is currently authorized.

## Governing order

For implementation work, read current design/experience/architecture/planning authority first, then the Phase 007 implementation lock and only the explicitly authorized subgroup.

Code does not outrank this chain. Class 3 architecture or Class 4 semantic/experience conflicts stop implementation and reopen upstream authority.

## 007-B executable bootstrap

The repository now has:

```text
pyproject.toml
uv.lock
.python-version
.gitignore
tools/verify.py
tests/unit/
tests/fitness/
.github/workflows/verify.yml
```

Locked bootstrap stack:

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

The base runtime dependency list remains empty. No PySpark/PyTorch/Transformers/Databricks/MLflow/cloud/database/runtime-service dependency was introduced.

Stable commands after explicit provisioning:

```text
uv sync --all-groups --no-install-project --locked
uv run --no-sync python tools/verify.py all
uv run --no-sync python tools/verify.py coverage
```

Portable-core pytest denies Python sockets by default. The permanent GitHub Actions Verify workflow has read-only repository permissions and runs from the committed lock.

Import Linter is installed but its production import contracts remain 007-C work because `src/syngan/` is intentionally absent.

## Evidence status

[007-B phase record](../phases/007/007-B-repository-toolchain-bootstrap-reproducible-environment-verification-harness.md) records entry baseline, dependency/tool choices, useful CI failures/corrections, green verification runs, lock materialization, network/offline posture and explicit non-claims.

`main` remains unprotected and Verify is not currently a required branch check. 007-C must revisit PR/review enforcement now that executable checks exist.

## Historical planning

Phase 005 and Phase 006 planning remain active beneath Phase 007 where not refined. The broader future wave sequence remains planning authority, but only an explicitly authorized Phase 007 subgroup may execute.

## Current next boundary

**007-C — Source/Package Topology, Dependency Direction & Architecture-Fitness Enforcement** is next eligible but **not yet authorized**.

An explicit proceed decision is required before `src/syngan/` or production package topology may be created.
