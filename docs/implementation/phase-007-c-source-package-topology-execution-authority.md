---
type: Implementation Authority
title: Phase 007-C Source/Package Topology Execution Authority
status: active
---

# Phase 007-C Source/Package Topology Execution Authority

## Purpose

Preserve the implementation architecture established by completed 007-C: the first production Python package structure, dependency direction, package-build boundary and architecture-fitness enforcement for SYNGAN.

Execution evidence/history is recorded in [007-C — Source/Package Topology, Dependency Direction & Architecture-Fitness Enforcement](../phases/007/007-C-source-package-topology-dependency-direction-architecture-fitness-enforcement.md).

007-C is complete. This contract remains active because later implementation must continue to obey the topology it established.

## Governing precedence

Implementation SHALL continue to follow, in order:

1. current Phase 006 authority/concepts/synchronizations/experience;
2. `docs/architecture/phase-006-architecture-reconciliation-contract.md`;
3. `docs/implementation/phase-006-implementation-planning-reconciliation.md`;
4. `docs/implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md`;
5. `docs/implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md`;
6. `docs/implementation/phase-007-implementation-authority-lock.md`;
7. this topology contract;
8. any later explicitly authorized Phase 007 subgroup.

## Canonical production topology

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

These are implementation responsibility boundaries, not new concepts.

Later owner-specific modules may be created inside the appropriate responsibility package only when their subgroup is authorized. Do not create empty package forests or generic convenience owners merely to anticipate future work.

## Dependency direction

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

required outer/inner packages
    ↑
bootstrap
```

Rules:

- `foundation` imports no other SYNGAN top-level package;
- `domain` may import `foundation` only;
- `ports` may import `foundation` and `domain`;
- `application` may import `foundation`, `domain`, `ports`;
- `api` may import `foundation`, `domain`, `ports`, `application`;
- `adapters` may import `foundation`, `domain`, `ports`, but not `application`, `api`, or `bootstrap`;
- `bootstrap` is composition-only and may import packages required for wiring;
- inner/core packages may not import `adapters` or `bootstrap`.

Import Linter is the executable architecture-fitness mechanism for these boundaries and is part of normal repository verification.

## Root package contract

`syngan.__init__` remains small and side-effect free.

Do not introduce root imports/re-exports that force adapters or optional runtimes into the base import closure. Importing `syngan` must remain possible without PySpark, PyTorch, Hugging Face/Transformers, Databricks, MLflow, database drivers, cloud SDKs or remote-service clients unless later explicit authority changes the base dependency contract.

Curated public re-exports belong to the subgroup that owns the public API contract.

## Build/package contract

Current package/build rules:

- one `syngan` distribution/import package;
- `src/` layout;
- Hatchling package selection explicitly targets `src/syngan`;
- `py.typed` is included in the package;
- `[project].dependencies` remains the runtime dependency authority and was empty at 007-C exit;
- Hatchling and `editables` are locked build/development tooling, not runtime capabilities;
- first-party verification provisions locked tooling before installing SYNGAN with build isolation disabled;
- normal verification builds and inspects wheel + sdist without publishing.

No package-publication or public-name/trademark clearance was established by 007-C.

## Architecture-fitness contract

Normal verification must preserve at least:

1. inward core layers;
2. no core dependency on adapters/bootstrap;
3. no adapter dependency on application/api/bootstrap;
4. exact accepted top-level responsibility boundaries unless later architecture authority changes them;
5. no production dependency on test support;
6. base/root import without unauthorized optional runtime dependencies;
7. packaged `py.typed` visibility;
8. no generic `utils`, `context`, `config`, `manager`, `registry`, `metadata`, `state`, `result`, `relationship` or `data_topology` god-owner introduced as a substitute for explicit responsibility.

## Verification/install contract

Repository verification installs the first-party package; it must not rely on an ad hoc `PYTHONPATH=src` as a substitute for package installation.

Current reproducible sequence is conceptually:

```text
provision locked build/test tooling
        ↓
install first-party SYNGAN with provisioned backend
        ↓
run lint / format / type / unit
        ↓
run Import Linter + architecture fitness
        ↓
run package build/content smoke
```

Portable-core pytest remains socket-denied by default after explicit dependency provisioning.

## Review/check contract

`Verify` is the canonical repository check for material source work.

Material production-source changes SHOULD use a reviewable branch/pull request when supported, with a green `Verify` result against the exact reviewed head retained as evidence.

Direct-to-main does not count as independent review. Do not claim branch protection or required-check enforcement unless repository state confirms it.

## Anti-drift boundary

This contract does not itself authorize later behavior.

It does not grant authority for:

- concept lifecycle/state behavior;
- ResourceRef/revision/snapshot/public-handle contracts;
- persistence/CAS/outbox/migrations;
- Spark/DataFrame behavior;
- Strategy/Learning/Generation/Evaluation algorithms;
- runtime/model bindings;
- Execution/Attempt/fencing/recovery;
- authorization/secrets/provider integrations;
- Evidence/Provenance/history/reproducibility behavior;
- deployment/release/publish workflows.

Those require their owning later subgroup.

## Stop/reopen rule

If implementation requires weakening or relocating these package boundaries, treat that as a Class 3 architecture issue and stop ordinary implementation until the smallest affected architecture authority is explicitly reopened.

If the pressure changes concept ownership, synchronization responsibility or required actor/programmatic meaning, treat it as Class 4 and reopen upstream design authority.

## Current authorization state

**007-C: COMPLETE — TOPOLOGY CONTRACT REMAINS ACTIVE.**

**007-D: NOT YET AUTHORIZED — NEXT ELIGIBLE.**

007-E through 007-K remain not authorized.
