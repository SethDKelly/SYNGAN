---
type: Phase Record
title: 005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement
status: complete
---

# 005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement

## Objective

Select the concrete Python source/package/test topology and foundational build/environment/verification tools required to make the Phase 004 architecture and 005-B fitness/quality-gate contract enforceable, without prematurely implementing the domain/control/data/runtime/security/platform slices planned for 005-D through 005-J.

## Entry authority

005-C is downstream of:

- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [005-A Implementation Authority](../../implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md);
- [005-B Verification Strategy](../../implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [Phase 005 navigator](index.md).

## Repository observation at entry

The repository remained intentionally free of production Python source, `pyproject.toml`, test topology and CI workflows at 005-C entry.

This allowed the package/toolchain structure to be selected from accepted architecture and verification obligations rather than inherited from premature scaffolding.

## Canonical authority created

005-C establishes:

[Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](../../implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md).

## Packaging decision

The initial implementation SHALL use:

```text
one repository
one initial Python distribution
one top-level import package: syngan
src/ layout
```

A multi-package workspace is not justified initially. Independently released plugins/distributions may be introduced later only when separate lifecycle/dependency/versioning needs exist.

Public package publication remains gated by a deliberate external distribution-name/ecosystem/trademark review; the import-package choice does not claim external naming rights.

## Python compatibility decision

The portable-core Python floor is:

```text
Python >= 3.11
```

Formatting/lint/type compatibility targets the Python 3.11 floor.

Optional runtime/platform support may later be narrower, but optional adapter limitations do not redefine the portable-core Python contract.

## Foundational toolchain selected

005-C accepts:

| Concern | Selected tool |
|---|---|
| project environment / lock | `uv` + committed `uv.lock` |
| project/build metadata | `pyproject.toml` |
| build backend | Hatchling |
| test runner | pytest |
| property/stateful testing | Hypothesis |
| core socket/network denial | pytest-socket |
| lint/format | Ruff |
| static typing | mypy |
| import/dependency architecture | Import Linter |
| coverage diagnostics | coverage.py / pytest integration |
| repository CI | GitHub Actions |

Tool versions are locked for development/CI but tool upgrades remain ordinary governed dependency changes.

005-C does not create application/runtime code or claim these files/workflows already exist merely because their future contents are now specified.

## Production package topology accepted

The initial top-level topology is:

```text
src/syngan/
├── __init__.py
├── foundation/
├── domain/
├── ports/
├── application/
├── api/
├── adapters/
└── bootstrap/
```

### Foundation

Contains only genuinely shared, technology-neutral primitives. It is not a miscellaneous utility/config/metadata/state/result/context dumping ground.

### Domain

Owns accepted concept semantics and owner-specific lifecycle/invariant logic.

### Ports

Defines technology-neutral capability contracts needed by application/runtime coordination.

### Application

Coordinates accepted use cases/synchronizations through domain contracts and ports without becoming a workflow/session owner.

### API

Provides typed specs/handles/navigation/facades while remaining independent of concrete adapters.

### Adapters

Contain optional concrete persistence/data/runtime/platform/security implementations behind ports.

### Bootstrap

Owns outer composition/wiring only and may see the full graph without owning canonical semantic state.

## Dependency direction accepted

The ordinary allowed graph is:

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

all required components
    ↑
bootstrap
```

Import Linter will enforce forbidden/layer/independence contracts.

Key consequences:

- domain cannot import ports/application/api/adapters/bootstrap;
- ports cannot import application/api/adapters/bootstrap;
- application cannot import concrete adapters/bootstrap;
- API cannot import adapters/bootstrap;
- adapters should not import application/API;
- adapter siblings remain independent by default;
- bootstrap may wire outward dependencies but cannot own canonical state.

## Root import rule

`import syngan` must remain small and side-effect free.

It must not require/import PySpark, PyTorch, Databricks, cloud/remote SDKs, connect to network/database/catalog services, create Spark sessions, inspect cloud credentials, configure telemetry, or instantiate a universal mutable Session/Context.

## Dependency isolation accepted

The base/core dependency set remains model/platform neutral.

The base package does not require:

- PySpark;
- PyTorch;
- Databricks SDKs;
- MLflow;
- cloud-provider SDKs;
- remote model/service clients;
- CUDA/GPU runtimes.

Reserved published capability extras are initially equivalent to:

```text
spark
torch
databricks
```

Their concrete dependencies/version ranges remain owned by 005-E/005-F/005-J.

No broad `all` extra is accepted initially.

Repository-only PEP 735 dependency groups begin logically with:

```text
test
lint
type
fitness
dev = aggregate convenience group
```

Additional integration/runtime groups are added only when their owning slices define them.

## Test topology accepted

```text
tests/
├── unit/
├── contract/
├── fitness/
├── conformance/
├── integration/
│   ├── persistence/
│   ├── spark/
│   ├── runtime/
│   ├── recovery/
│   ├── history/
│   ├── security/
│   └── platform/
├── scale/
├── scenarios/
├── fixtures/
│   └── golden/
└── support/
```

This topology supports V0-V11 without mechanically creating one directory for every verification layer.

Production code must not depend on `tests` support utilities.

## Verification tooling consequences

### pytest

Strict markers/configuration are required.

Markers express cost/environment/capability such as integration, Spark, runtime, recovery, security, platform, network, scale and statistical profiles.

### pytest-socket

Portable/core profiles deny Python socket/network use by default. Network/platform tests opt into explicit profiles and the narrowest allowed connectivity.

Spark local-process communication is handled in its explicit integration profile rather than weakening portable-core network-denial expectations globally.

### Ruff

One formatter/linter protects the Python surface with target-version aligned to Python 3.11.

### mypy

The strongest type discipline starts with foundation/domain/ports/application/API. Adapter exceptions for weak third-party typing are narrow/module-specific rather than global suppression.

### Import Linter

Import contracts are mandatory AF-01/AF-02 fitness enforcement, not advisory style rules.

### Coverage

Coverage is diagnostic evidence and not a replacement for fitness/contract behavior. No global percentage is accepted as semantic correctness.

## Stable developer quality-gate commands

005-C accepts a repository-only cross-platform orchestrator:

```text
tools/verify.py
```

Stable command meanings are:

```text
uv run --locked python tools/verify.py q0
uv run --locked python tools/verify.py q1
uv run --locked python tools/verify.py q2 --profile <profile>
uv run --locked python tools/verify.py q3 [--profile <matrix>]
uv run --locked python tools/verify.py q4 [--profile <release-profile>]
```

The script orchestrates existing tools; it does not reimplement domain/test semantics.

Q0 includes fast static/structure/unit/fitness/no-network checks.

Q1 includes Q0 plus full deterministic contract/fitness coverage, affected migration/serialization tests, package build, installed-wheel smoke and base/offline import checks.

## CI decision

GitHub Actions is selected as the initial repository CI system.

Initial Q1 check responsibilities are equivalent to:

```text
Q1 / static-and-structure
Q1 / unit-contract-fitness
Q1 / package-offline-core
```

Changed-slice bounded Spark/recovery/security checks may be added as separate required Q1 checks where appropriate.

Q2, Q3 and Q4 remain distinct integration/scheduled/release profiles.

Workflow dependencies/actions should use immutable pins or equivalent drift control.

Branch protection should require the stable Q1 checks once the workflows actually exist; 005-C does not falsely claim that this enforcement is already configured.

## `src/` and built-package verification

Q1 package verification must build wheel/sdist and test the installed artifact, not only imports from a repository checkout.

It must prove the base distribution imports without optional Spark/Torch/Databricks SDKs or external network activity and does not unintentionally package repository-only tests/tools.

## Later-slice ownership map

005-C maps later implementation slices onto the top-level packages:

| Slice | Primary refinement |
|---|---|
| 005-D | foundation/domain/application/ports/API + control persistence boundaries |
| 005-E | distributed data/source/output ports and Spark/data adapters |
| 005-F | Strategy/method runtime ports/adapters and Learned-State loading |
| 005-G | Execution/recovery domain/application/ports and scheduler/checkpoint adapters |
| 005-H | Evaluation/Evidence/Provenance/reproducibility + query projections |
| 005-I | dependency/security/authorization/disclosure ports/adapters |
| 005-J | bootstrap, platform/observability adapters, compatibility/scale profiles |

Later slices may refine subpackages without reversing 005-C dependency direction.

## Architecture fitness mapping

005-C directly operationalizes:

- AF-01 through Import Linter dependency contracts;
- AF-02 through base/optional dependency isolation and package smoke;
- AF-12 through socket-denied portable-core verification and no hidden acquisition;
- AF-13 through later Spark static/behavioral full-driver-materialization checks;
- AF-20 through platform-adapter dependency isolation.

The remaining fitness obligations are implemented by their owning later slices under this topology.

## External/current-tool validation

During 005-C, current upstream documentation was checked to avoid selecting stale foundational assumptions:

- current Python Packaging guidance continues to support `pyproject.toml` and the `src/` layout;
- current uv project behavior supports committed locking/synchronization and dependency groups/optional extras;
- current Ruff supplies both formatter and linter;
- current pytest supports explicit fixtures/markers and strict marker/config behavior;
- current Import Linter supports TOML configuration plus layered/forbidden/independence contract types;
- current PySpark 4.2 documentation supports Python 3.10+, so a Python 3.11 portable-core floor does not itself prevent current Spark integration.

These observations inform implementation tooling but do not make those external tools semantic authority.

## No production implementation started

005-C selects the implementation structure/toolchain but does not implement:

- public resource classes/handles;
- persistence schemas/repositories;
- Spark materialization/manifests;
- Strategy/runtime plugins;
- checkpoint/fencing/recovery mechanisms;
- Evidence/Provenance stores;
- authorization/security adapters;
- Databricks/deployment integration.

Those remain planned work in 005-D through 005-J.

## No upstream revision required

005-C found no package/toolchain requirement that requires changing the eleven accepted concepts, fifteen synchronizations, Phase 003 experience contract, Phase 004 architecture contract, or ADR-0001 through ADR-0008.

No new architecture ADR is required because the phase chooses downstream implementation topology/tooling within accepted architecture.

## Exit criteria

- [x] one-distribution/import-package strategy selected;
- [x] `src/` layout selected;
- [x] Python >=3.11 floor accepted;
- [x] production package responsibilities defined;
- [x] foundation admission/anti-bloat rule defined;
- [x] import/dependency direction defined;
- [x] optional runtime/platform dependency isolation defined;
- [x] concrete foundational project/build/test/lint/type/import tools selected;
- [x] test/conformance/fixture topology selected;
- [x] Q0-Q4 stable developer command surface defined;
- [x] GitHub Actions initial Q1 check architecture selected;
- [x] built-package/base-install/no-network verification defined;
- [x] later Phase 005 slices mapped to package areas;
- [x] no production domain/runtime implementation prematurely created.

## Exit decision

**005-C — complete.**

Next:

**005-D — Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan**.
