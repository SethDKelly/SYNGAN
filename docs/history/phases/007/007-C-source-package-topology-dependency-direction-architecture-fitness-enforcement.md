---
type: Phase Record
title: 007-C — Source/Package Topology, Dependency Direction & Architecture-Fitness Enforcement
status: complete
---

# 007-C — Source/Package Topology, Dependency Direction & Architecture-Fitness Enforcement

## Objective

Establish the first production Python package structure and make its dependency direction executable and continuously verifiable, without introducing owner-specific domain behavior or later-slice runtime/persistence/API semantics.

## Result

**PASS — SOURCE/PACKAGE TOPOLOGY ESTABLISHED AND ARCHITECTURE FITNESS ENFORCED.**

007-C is complete. 007-D is the next eligible subgroup but is **not authorized by this record**; explicit proceed authority remains required.

## Entry baseline

```text
repository: SethDKelly/SYNGAN
branch:     main
commit:     c833c5de8ecb0b84481ab6046af6e929b34d01e9
```

007-C authority was activated on `main` before source implementation began.

## Reviewable implementation branch

Material source work was performed on:

```text
phase-007-c-source-topology
```

Pull request:

```text
PR #1 — 007-C: establish source package topology and architecture fitness
reviewed head: 9f93b6eff7f8d8a1b19950745530dc273d462d6d
merge commit: 063f847953f69a525ee04315fa92bc0e9fa36a1c
```

The branch/PR path was used deliberately because 007-B had established executable CI. This provides reviewable diff and exact-head CI evidence without falsely claiming GitHub branch-protection enforcement.

## Implemented package topology

007-C established one `syngan` distribution/import package using `src/`:

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

The package initializers contain only bounded responsibility documentation. No concept state/lifecycle, persistence, runtime or synthesis behavior was introduced.

No generic `utils`, `context`, `config`, `manager`, `registry`, `metadata`, `state`, `result`, `relationship` or `data_topology` owner package was created.

## Executable dependency architecture

Import Linter is now part of the normal repository verification gate.

Three contracts enforce:

1. **core layers point inward**
   `api -> application -> ports -> domain -> foundation`;
2. **core packages do not depend on outer technology/composition**
   `foundation/domain/ports/application/api` may not depend on `adapters` or `bootstrap`;
3. **adapters stay outside coordination/composition**
   `adapters` may not depend on `application`, `api` or `bootstrap`.

Additional fitness checks enforce:

- exact top-level responsibility package set;
- no generic god-owner package introduction;
- import-free root `syngan.__init__` during this structural slice;
- no production-source imports from `tests`.

These package rules are implementation architecture, not new domain concepts.

## Package/build realization

Hatchling package selection is explicit:

```text
src/syngan
```

`py.typed` is retained in the installed/built package.

The repository verification flow now uses two-stage locked provisioning:

```text
uv sync --all-groups --no-install-project --locked
uv sync --all-groups --locked --no-build-isolation
uv run --no-sync python tools/verify.py all
```

The first stage provisions declared build/test/static-analysis tools. The second installs the first-party project using the already provisioned build backend, avoiding undeclared build-isolation acquisition.

## Dependency result

`[project].dependencies` remains empty.

The build/development group now explicitly contains:

- Hatchling;
- `editables` for Hatchling editable-wheel support under the no-build-isolation verification path.

The resolved lock selected:

```text
hatchling 1.32.0
editables 0.6
```

These are build/development dependencies, not SYNGAN runtime capabilities.

No PySpark, PyTorch, Transformers/Hugging Face, Databricks, MLflow, cloud-provider SDK, database/ORM, remote-model/inference client or telemetry exporter was introduced into the runtime dependency closure.

## Package verification

The repository-owned `package` gate now verifies:

- installed `syngan` import succeeds;
- every accepted top-level responsibility package imports;
- `py.typed` is present through installed package resources;
- `uv build --no-build-isolation` creates exactly one wheel and one source distribution;
- the wheel contains the expected root, typed marker and seven responsibility package initializers;
- build artifacts are removed after verification;
- no publishing occurs.

## Corrective implementation evidence

007-C retained implementation failures as evidence rather than weakening gates.

### Build backend ordering

Initial no-build-isolation install failed because Hatchling had not yet been installed before first-party project build.

Resolution: two-stage locked provisioning, with declared tools installed first.

### Editable build support

The two-stage flow then exposed Hatchling's editable build requirement for `editables`.

Resolution: add `editables` to the locked build/development group. Runtime dependencies remained empty.

### Quality-gate formatting

Ruff lint/format found ordinary line-length/canonical formatting defects in the new verification/test code.

Resolution: correct formatting; no gate was disabled or weakened.

No encountered failure required a Class 3 architecture or Class 4 semantic/experience change.

## Controlled lock materialization

Because `pyproject.toml` changed the locked build-tool graph, a temporary branch-scoped writable workflow was used.

It was constrained to:

1. resolve `uv.lock`;
2. provision the locked environment;
3. install SYNGAN;
4. run the complete repository gate;
5. prove `uv.lock` was the only generated repository change;
6. commit only `uv.lock`.

Successful controlled run:

```text
GitHub Actions run 34388938928
lock/provision/install/verify      PASS
uv.lock-only change check          PASS
lock materialization               PASS
```

Generated lock commit:

```text
5b96a78bdb5aaa88a0089629bb0a452d5b2d8e18
```

The temporary writable workflow was deleted before PR #1 opened.

## Pull-request verification evidence

The permanent read-only `Verify` workflow ran against exact PR head:

```text
head: 9f93b6eff7f8d8a1b19950745530dc273d462d6d
run:  34389127442
result: PASS
```

The PR diff was also inspected for scope/authority drift before merge. It contained the expected source topology, package/build configuration, lock, verification changes and Phase 007-C navigation only. No hidden temporary workflow or later-slice implementation was present.

## Network/offline posture

Explicit dependency provisioning may use declared package infrastructure.

Portable-core pytest continues to deny Python sockets by default after provisioning. 007-C introduced no runtime network acquisition, model-hub access, hosted inference or remote fallback behavior.

## Review/check posture

`Verify` is now the canonical check for material source work and has successfully run on a reviewable pull-request head.

`main` is still not documented as protected and `Verify` is not claimed as a repository-enforced required check. Subsequent material production-source slices should continue using reviewable branches/PRs when supported and retain exact-head green verification evidence.

## Explicit non-claims

007-C does not establish or claim:

- concept lifecycle/state implementation;
- ResourceRef/revision/snapshot/public-handle contracts;
- persistence schemas, CAS/outbox or migrations;
- Spark/DataFrame source/output behavior;
- Strategy/Learning/Generation/Evaluation algorithms;
- runtime/model bindings;
- Execution/Attempt/fencing/recovery behavior;
- authorization/secrets/provider integration;
- Evidence/Provenance/history/reproducibility behavior;
- public API facades beyond an importable structural package;
- package publication or name/trademark clearance;
- enterprise-scale or distributed-runtime correctness.

## Conflict review

No Class 3 architecture conflict or Class 4 semantic/experience conflict was discovered.

The implementation architecture remains compatible with the Phase 006 design baseline and leaves later time-series/multi-table/runtime capabilities structurally open.

## Exit decision

**007-C: COMPLETE.**

**007-D: NOT YET AUTHORIZED.**

007-D — Identity, Revision, Serialization, Typed Public Resource/Handle & Programmatic-View Foundation is now the next eligible subgroup and requires a later explicit proceed decision.
