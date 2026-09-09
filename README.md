# SYNGAN

SYNGAN is a design-first synthetic-data generation framework intended for Spark-scale workloads.

Daniel Jackson concept design and the repository's canonical design/planning work were completed through Phase 006 before production implementation authority was granted.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current implementation authority:

- [`Phase 007 Implementation Authority Lock`](docs/implementation/phase-007-implementation-authority-lock.md)
- [`Phase 007-B Bootstrap Execution Authority`](docs/implementation/phase-007-b-bootstrap-execution-authority.md)
- [`Phase 007 index`](docs/phases/007/index.md)

Repository-wide automated-agent rules are in [`AGENTS.md`](AGENTS.md).

## Status

- Phases 001–006 — complete design/planning/readiness baseline
- **007-A — complete: implementation authority lock**
- **007-B — complete: reproducible repository/toolchain/verification bootstrap**
- **007-C — next eligible, not yet authorized**

No `src/syngan/` production package or substantive domain/runtime/platform behavior has been authorized yet.

## 007-B executable bootstrap

The repository now declares:

```text
Python >= 3.11
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

`[project].dependencies` is still empty. The bootstrap adds development/build/verification tooling only; it does not add PySpark, PyTorch, Transformers/Hugging Face, Databricks, MLflow, cloud SDKs, database drivers/ORMs, remote-model clients, or telemetry exporters.

### Reproduce the development verification environment

```bash
uv sync --all-groups --no-install-project --locked
```

### Run the normal verification gate

```bash
uv run --no-sync python tools/verify.py all
```

This checks the committed lock, Ruff lint/format, strict mypy, bootstrap/unit tests, authority/architecture fitness checks, and the default socket-denied portable-core pytest profile.

### Coverage diagnostics

```bash
uv run --no-sync python tools/verify.py coverage
```

Coverage is diagnostic evidence, not a replacement for contract/architecture fitness.

The permanent GitHub Actions [`Verify`](.github/workflows/verify.yml) workflow runs from the committed lock with read-only repository permissions on pushes and pull requests. `main` is still unprotected and Verify is not yet a required branch check.

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

**007-C — Source/Package Topology, Dependency Direction & Architecture-Fitness Enforcement** is next eligible but **not yet authorized**.

An explicit proceed decision is required before production package/source topology may be created.
