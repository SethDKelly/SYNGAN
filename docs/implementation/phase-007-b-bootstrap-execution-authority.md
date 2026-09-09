---
type: Implementation Authority
title: Phase 007-B Bootstrap Execution Authority
status: active
---

# Phase 007-B Bootstrap Execution Authority

## Purpose

Define the concrete execution boundary for **007-B — Repository/Toolchain Bootstrap, Reproducible Environment & Verification Harness** beneath the [Phase 007 Implementation Authority Lock](phase-007-implementation-authority-lock.md).

This authority does not widen 007-B into source/package/domain implementation. It resolves one bootstrap mechanics question: how the exact CI-resolved `uv.lock` may be materialized into version control when the connected repository API can read the generated artifact but cannot directly upload the artifact bytes as a repository file.

## Entry baseline

007-B begins from:

```text
repository: SethDKelly/SYNGAN
branch:     main
commit:     f71df8c6f4d9fefdfda7fac5284c261acdc56d25
```

## Existing 007-A boundary remains controlling

007-B remains limited to repository/toolchain/verification bootstrap material.

In particular, 007-B still MUST NOT introduce:

- `src/syngan/` production source;
- domain/application/port/adapter behavior;
- database schema/migrations;
- Spark/model/Strategy runtime behavior;
- security-provider or secret-store integration;
- deployment/publishing automation;
- benchmark implementation;
- production runtime dependencies such as PySpark, PyTorch, Transformers, Databricks, MLflow, cloud SDKs, database drivers, or telemetry exporters.

## Locked toolchain realization

007-B realizes:

```text
Python >= 3.11
uv 0.12.x
Hatchling
pytest
Hypothesis
pytest-socket
Ruff
mypy
Import Linter
coverage.py / pytest-cov
GitHub Actions verification
```

Current CI pins may use exact contemporary action/tool releases while the repository compatibility contract remains the bounded family declared in `pyproject.toml`.

## One-time lock materialization exception

The normal Phase 007 CI posture is read-only verification.

For **one temporary bootstrap workflow only**, 007-B MAY grant `contents: write` to GitHub Actions solely to commit the exact `uv.lock` generated from the committed `pyproject.toml` after verification succeeds.

This is an implementation bootstrap mechanism, not ongoing CI authority.

The temporary workflow MUST satisfy all of the following:

1. resolve `uv.lock` from committed metadata using the locked uv tool family;
2. provision the environment from that lock;
3. run the repository-owned verification gate successfully before any repository write;
4. verify that the working tree contains **no generated change other than `uv.lock`**;
5. stage and commit only `uv.lock`;
6. use a bounded, explicit bootstrap commit message;
7. avoid an infinite workflow loop by excluding a lock-only push from retriggering the temporary workflow;
8. perform no release, publication, deployment, package upload, tag, branch-protection, or source generation action;
9. be removed before 007-B is declared complete;
10. be replaced by a permanent verification workflow with `contents: read` only.

If any other file is modified/generated, the write step MUST fail closed and commit nothing.

## Why this does not broaden authority

`uv.lock` is already an explicitly authorized 007-B repository surface and Phase 005-C requires reproducible development/CI resolution from committed lock state.

The exception changes only the transport mechanism used to materialize an already-authorized, already-verified generated configuration file. It does not authorize a new product capability or semantic/architecture change.

## Portable-core network boundary

Explicit dependency provisioning may access declared package infrastructure.

After provisioning, the portable-core pytest profile runs with Python sockets disabled by default. Tests may not normalize hidden package installation, public model-hub lookup, hosted inference, or undeclared remote fallback.

## Exit condition

This authority is satisfied only when:

- a full hash-bearing `uv.lock` is committed;
- `uv lock --check` succeeds against committed metadata;
- the permanent read-only verification workflow provisions with `--locked` and passes all repository-owned gates;
- the temporary writable lock-materialization workflow no longer exists;
- no `src/syngan/` tree or unauthorized runtime dependency has been introduced.

## Next-authorization boundary

This document does **not** authorize 007-C.

007-C may be authorized only after 007-B produces its completion evidence and an explicit proceed decision is recorded.
