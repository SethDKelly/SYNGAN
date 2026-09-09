---
type: Implementation Authority
title: Phase 007-C Source/Package Topology Execution Authority
status: active
---

# Phase 007-C Source/Package Topology Execution Authority

## Purpose

Authorize the first production Python package structure for SYNGAN after the successful 007-B repository/toolchain bootstrap, while keeping implementation limited to **source/package topology, dependency direction and architecture-fitness enforcement**.

This authority does not authorize concept behavior, public resource contracts, persistence, Spark/runtime execution, synthesis algorithms, security adapters, Evidence/history behavior or deployment infrastructure.

## Entry baseline

007-C is entered against:

```text
repository: SethDKelly/SYNGAN
branch:     main
commit:     c833c5de8ecb0b84481ab6046af6e929b34d01e9
```

007-B acceptance evidence is recorded in:

`docs/phases/007/007-B-repository-toolchain-bootstrap-reproducible-environment-verification-harness.md`

## Governing authority

007-C SHALL implement, in precedence order:

1. current Phase 006 authority/concepts/synchronizations/experience;
2. `docs/architecture/phase-006-architecture-reconciliation-contract.md`;
3. `docs/implementation/phase-006-implementation-planning-reconciliation.md`;
4. `docs/implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md`;
5. `docs/implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md`;
6. `docs/implementation/phase-007-implementation-authority-lock.md`;
7. this 007-C bounded authority.

## Authorized production topology

007-C SHALL establish exactly one initial Python distribution/import package using a `src/` layout:

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

Each top-level responsibility package may contain only minimal package markers/documentation in 007-C. Owner-specific implementations belong to 007-D and later slices.

Empty placeholder module forests are prohibited. Create only the package boundaries required to make the accepted topology importable and enforceable.

## Dependency direction

The executable architecture SHALL preserve:

```text
foundation
    ↑
domain
    ↑
ports
    ↑
application
    ↑
api

foundation/domain/ports
    ↑
adapters

all required outer/inner packages
    ↑
bootstrap
```

Specific rules:

- `foundation` imports no other SYNGAN top-level package;
- `domain` may import `foundation` only;
- `ports` may import `foundation` and `domain`;
- `application` may import `foundation`, `domain`, `ports`;
- `api` may import `foundation`, `domain`, `ports`, `application`;
- `adapters` may import `foundation`, `domain`, `ports` but not `application`, `api`, or `bootstrap`;
- `bootstrap` is composition-only and may import the packages it needs for wiring;
- inner/core packages may not import `adapters` or `bootstrap`.

These are code-responsibility boundaries, not new domain concepts.

## Root package rule

`syngan.__init__` SHALL remain small and side-effect free.

007-C SHALL NOT introduce root-package imports/re-exports that pull in adapters or optional runtimes. Importing `syngan` in the base environment must succeed without PySpark, PyTorch, Hugging Face/Transformers, Databricks, MLflow, database drivers, cloud SDKs or remote-service clients.

A curated public re-export surface is deferred until the owning API/public-contract slices.

## Build/package authority

007-C MAY:

- make Hatchling's `src/syngan` package selection explicit;
- add `py.typed` as package data through the selected package layout;
- make Hatchling a locked development/build dependency so installing/building the first-party package does not depend on an untracked build-backend version;
- update locked dependency state only for that authorized build-tooling change;
- change CI/local provisioning from `--no-install-project` to installed-project verification;
- add a build/package smoke gate that verifies wheel/sdist creation and expected package contents without publishing artifacts.

007-C MUST NOT publish a package or claim that the public `syngan` distribution name has completed ecosystem/trademark review.

## Architecture-fitness enforcement

Import Linter SHALL become an executed verification gate in 007-C.

At minimum its contracts must enforce:

1. inward core layers;
2. no inner/core dependency on adapters/bootstrap;
3. no adapter dependency on application/api/bootstrap.

The permanent repository verification entry point must run this check automatically.

007-C SHALL also retain executable checks that:

- the expected top-level package boundaries exist and import;
- root/base import requires no unauthorized optional runtime dependency;
- `py.typed` is packaged/visible;
- production code does not import from `tests`;
- the 007-C topology does not invent generic `utils`, `context`, `manager`, `registry`, `metadata`, `result`, `relationship` or `data_topology` owner packages.

## Verification/source posture

Once `src/syngan` exists, CI and local verification SHALL install the first-party package before running tests. The repository must not rely on adding `src/` to `PYTHONPATH` as a substitute for package installation.

Portable-core pytest remains socket-denied by default after explicit provisioning.

## Review/check policy refinement

007-B established a green `Verify` workflow but `main` remains unprotected and the current connector does not provide repository-administration writes for branch protection.

007-C therefore adopts the following procedural policy for subsequent material production-source work:

- `Verify` is the canonical repository check;
- material production-source changes SHOULD be made through a reviewable branch/pull request when the execution environment supports that workflow;
- a green `Verify` result against the exact reviewed head is required evidence before merge/acceptance;
- direct-to-main remains possible only when explicitly authorized by the active subgroup/user and must not be described as independent review;
- branch protection/required-check enforcement must not be claimed until GitHub repository state confirms it.

007-C does not silently enable administration settings it cannot verify or manage.

## Prohibited 007-C work

007-C MUST NOT implement:

- accepted concept lifecycle/state behavior;
- `ResourceRef`, revision/snapshot/public handle contracts;
- persistence schemas, CAS/outbox/migrations;
- Spark/DataFrame source/output behavior;
- Strategy, Learning, Generation or Evaluation algorithms;
- runtime/model bindings;
- Execution/Attempt/fencing/recovery behavior;
- authorization/secrets/provider integrations;
- Evidence/Provenance/history/reproducibility behavior;
- API facades beyond importable structural package markers;
- deployment/release/publish workflows.

Those remain owned by 007-D and later subgroups.

## Completion gate

007-C may be marked complete only if:

1. `src/syngan` and the seven accepted top-level responsibility packages exist without substantive premature behavior;
2. Hatchling package selection is explicit and the package installs from the declared locked environment;
3. Import Linter contracts are configured and executed in normal verification;
4. architecture/topology fitness checks pass;
5. root/base import works without unauthorized optional runtime dependencies or side effects;
6. package build smoke evidence succeeds without publication;
7. the committed lock is current after any authorized build-tool dependency change;
8. the permanent read-only `Verify` workflow passes on the completed repository head;
9. no Class 3 architecture or Class 4 semantic/experience conflict is unresolved;
10. 007-C records its evidence and does not authorize 007-D without a later explicit proceed decision.

## Authorization state

**007-C: AUTHORIZED / ACTIVE.**

**007-D through 007-K: NOT AUTHORIZED.**
