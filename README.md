# SYNGAN

SYNGAN is a design-first synthetic-data generation framework intended for Spark-scale workloads.

Daniel Jackson concept design and the repository's canonical design/planning work were completed through Phase 006 before production implementation authority was granted.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current implementation authority:

- [`Phase 007 Implementation Authority Lock`](docs/implementation/phase-007-implementation-authority-lock.md)
- [`Phase 007-B Bootstrap Execution Authority`](docs/implementation/phase-007-b-bootstrap-execution-authority.md)
- [`Phase 007-C Source/Package Topology Execution Authority`](docs/implementation/phase-007-c-source-package-topology-execution-authority.md)
- [`Phase 007 index`](docs/phases/007/index.md)

Repository-wide automated-agent rules are in [`AGENTS.md`](AGENTS.md).

## Status

- Phases 001–006 — complete design/planning/readiness baseline
- **007-A — complete: implementation authority lock**
- **007-B — complete: reproducible repository/toolchain/verification bootstrap**
- **007-C — complete: source/package topology + architecture-fitness enforcement**
- **007-D — next eligible, not yet authorized**

## Executable substrate through 007-C

The first production package architecture now exists:

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

These packages currently establish responsibility boundaries only. Owner-specific concept/public-contract/persistence/runtime behavior belongs to later explicitly authorized subgroups.

Import Linter is part of normal verification and enforces inward core layering plus adapter/composition boundaries.

The repository declares:

```text
Python >= 3.11
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
```

`[project].dependencies` remains empty. Hatchling and `editables` are build/development tooling; no PySpark, PyTorch, Transformers/Hugging Face, Databricks, MLflow, cloud SDK, database driver/ORM, remote-model client, or telemetry exporter is in the runtime dependency closure.

### Reproduce and install the verification environment

```bash
uv sync --all-groups --no-install-project --locked
uv sync --all-groups --locked --no-build-isolation
```

The two-stage sequence explicitly provisions locked build/test tooling before installing the first-party package without hidden build-isolation acquisition.

### Run the normal verification gate

```bash
uv run --no-sync python tools/verify.py all
```

The gate checks the committed lock, Ruff lint/format, strict mypy, unit tests, Import Linter contracts, architecture/topology fitness, installed-package imports, `py.typed`, and non-publishing wheel/sdist construction/content.

### Coverage diagnostics

```bash
uv run --no-sync python tools/verify.py coverage
```

Coverage is diagnostic evidence, not a replacement for contract/architecture fitness.

The permanent GitHub Actions [`Verify`](.github/workflows/verify.yml) workflow has read-only repository permissions and runs on pushes and pull requests. 007-C exercised that review path through PR #1; exact PR head `9f93b6eff7f8d8a1b19950745530dc273d462d6d` passed Verify before merge as `063f847953f69a525ee04315fa92bc0e9fa36a1c`.

`main` is still not claimed as protected and Verify is not claimed as a repository-required check.

## Locked design baseline

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
```

Complete structured-data target:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

The complete supported baseline also requires source-derived/local free-form-text synthesis without mandatory public model-hub or runtime inference-service dependency.

## Current implementation rules

```text
restored stale control state
    != current mutation authority

driver import success
    != cluster worker readiness
resource pressure
    != permission to weaken semantics
topology preset
    != durable semantic topology
privacy Evidence
    != formal privacy guarantee
    != release approval
```

Implementation is evidence-gated and incremental. A Class 3 architecture conflict or Class 4 semantic/experience conflict stops ordinary implementation and reopens upstream authority.

## Current next boundary

**007-D — Identity, Revision, Serialization, Typed Public Resource/Handle & Programmatic-View Foundation** is next eligible but **not yet authorized**.

An explicit proceed decision is required before 007-D implementation begins.
