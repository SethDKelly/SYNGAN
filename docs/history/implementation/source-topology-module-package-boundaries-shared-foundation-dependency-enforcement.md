---
type: Implementation Authority
title: Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement
status: active
---

# Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement

## Purpose

Define the concrete repository/package topology and foundational Python/build/test/static-analysis toolchain that later SYNGAN implementation slices MUST use unless explicitly superseded through implementation governance.

This document is the canonical Phase 005-C implementation authority. It translates the [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md), [005-A implementation governance](implementation-authority-delivery-governance-toolchain-repository-enforcement.md), and [005-B verification authority](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md) into enforceable source boundaries without implementing the control-plane, Spark/runtime, recovery, Evidence/history, security, or platform behavior owned by 005-D through 005-J.

## Governing rule

> **Source topology exists to preserve authority and verification boundaries. Package convenience MUST NOT create a new semantic owner, collapse optional integrations into the portable core, or make a concrete runtime/platform a dependency of inner SYNGAN layers.**

The topology is therefore chosen from the architecture inward rather than from preferred framework conventions outward.

## Repository state at entry

At 005-C entry the repository contains design/implementation-planning documentation, `AGENTS.md`, and a pull-request template, but intentionally contains no production Python package, `pyproject.toml`, test tree, or CI workflow.

005-C selects those structures and tools as implementation authority. It does **not** create production domain/runtime implementation merely to make the repository look coded.

## Packaging decisions

### One initial Python distribution and one import package

SYNGAN SHALL begin as one Python distribution containing one top-level import package:

```text
import package: syngan
```

The initial repository SHALL NOT be split into multiple independently versioned Python distributions merely to mirror architecture layers.

Separate distributions remain possible later for independently released plugins/adapters when there is demonstrated lifecycle/dependency value, but a multi-package workspace is not the initial architecture.

The public distribution project name may use `syngan` during local/package implementation, but public package publication remains gated by a deliberate PyPI/ecosystem/name/trademark review. The import-package decision does not assert that an external distribution name is legally or operationally available.

### `src/` layout

Production importable code SHALL use a `src/` layout:

```text
repository/
├── pyproject.toml
├── uv.lock
├── src/
│   └── syngan/
├── tests/
├── tools/
├── docs/
├── .github/
├── AGENTS.md
└── README.md
```

The `src/` layout is selected so tests and developer commands exercise the installed package rather than accidentally importing a repository-root copy.

### Python floor

The initial portable-core Python requirement SHALL be:

```text
Python >= 3.11
```

The code style/type configuration SHALL target Python 3.11 syntax/semantics as the minimum compatibility contract until the support matrix is deliberately revised.

No upper Python version bound is accepted merely because later optional adapters may lag. 005-J owns the tested platform/runtime compatibility matrix; optional runtime limitations MUST remain narrower adapter compatibility facts rather than silently lowering or redefining the portable-core contract.

## Foundational project/toolchain decisions

### Project and lock management — `uv`

SYNGAN SHALL use **uv** as the repository project-environment and lock manager for the initial implementation program.

Required behavior:

- `pyproject.toml` is canonical project/dependency/tool configuration;
- `uv.lock` is committed to version control;
- developer and CI commands use locked resolution (`--locked` or equivalent fail-on-stale behavior);
- dependency upgrades are explicit repository changes rather than implicit latest-version resolution during tests;
- dependency groups distinguish local verification/build concerns from published optional extras;
- private/offline installation profiles can consume pre-provisioned indexes/wheels without runtime code self-installing dependencies.

The lockfile governs reproducible development/CI resolution. Published library dependency constraints remain intentionally distinct from one exact development lock.

### Build backend — Hatchling

The initial build backend SHALL be **Hatchling** behind the standard `[build-system]`/`[project]` `pyproject.toml` contract.

Hatchling is a packaging mechanism only. It MUST NOT acquire runtime/domain authority.

The package SHALL build both wheel and source distribution artifacts as part of package/release verification.

### Test runner — pytest

**pytest** SHALL be the foundational test runner.

Project configuration SHALL enable strict marker/config behavior. Verification profiles and markers MUST be explicit rather than relying on undocumented filename conventions or hidden environment state.

### Property/stateful verification — Hypothesis

**Hypothesis** SHALL be available in the verification dependency set for property/state-machine tests where it adds value, especially identity/version invariants, lifecycle transition properties, serialization/migration properties, and recovery/state-machine behavior.

Hypothesis is not required for every test and MUST NOT replace explicit architectural scenario tests.

### Network-deny verification — pytest-socket

**pytest-socket** SHALL provide the default Python-socket denial mechanism for portable/core pytest profiles.

Core verification SHOULD run with sockets disabled by default. Tests that genuinely require local/distributed/process or external network access MUST opt into an explicitly named profile/marker and use the narrowest permitted host/network scope.

Spark integration tests are not classified as portable-core no-network tests merely because local PySpark uses process/socket communication; the profile must distinguish loopback/process plumbing from external network/egress.

### Linting and formatting — Ruff

**Ruff** SHALL provide Python linting and formatting.

Required posture:

- formatting and lint configuration live in `pyproject.toml`;
- target version matches the Python 3.11 floor;
- production source, tests, and repository Python tooling are checked;
- lint suppressions are narrow and explained where they protect intentional interoperability rather than convenience.

A second general Python formatter/linter SHOULD NOT be added without a specific uncovered requirement.

### Static typing — mypy

**mypy** SHALL be the initial static type checker.

Typing expectations:

- `foundation`, `domain`, `ports`, `application`, and `api` are held to the strongest baseline;
- public/port contracts should be fully typed;
- adapters may use narrowly scoped module-specific exceptions for weakly typed third-party SDKs;
- global `ignore_missing_imports = true` or equivalent blanket suppression is prohibited;
- typing exceptions must not hide a semantic boundary or turn `Any` into an informal cross-layer API.

### Dependency/import architecture — Import Linter

**Import Linter** SHALL enforce the package dependency rules accepted below.

Its contracts SHALL live in repository configuration, preferably `pyproject.toml`, and SHALL be treated as AF-01/AF-02 architecture-fitness enforcement rather than optional style checks.

### Coverage reporting

`coverage.py`/pytest coverage integration SHALL be available for test diagnostics and changed-slice review.

No universal line-coverage percentage is accepted as a proxy for correctness. Coverage data supports gap detection; V0-V11 and AF-01 through AF-20 remain the actual verification contract.

## Canonical production package topology

The initial top-level production topology SHALL be equivalent to:

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

These are code-responsibility boundaries, not new domain concepts.

### `syngan.foundation`

Purpose: smallest technology-neutral shared primitives required across inner layers.

Suitable responsibilities may include stable typed identity/reference/version primitives, bounded issue/problem representations, small immutable/common value mechanics, and other cross-owner primitives whose meaning is genuinely shared.

Foundation acceptance test:

A type/function belongs here only when all are true:

1. at least two inner responsibilities need it;
2. no accepted concept clearly owns its lifecycle/meaning;
3. it has no dependency on application, ports, adapters, runtime/platform SDKs, Spark, PyTorch, Databricks, database drivers, or network clients;
4. moving it here does not erase an owner-specific distinction;
5. the name is specific enough that the package does not become a utilities/config/metadata dumping ground.

The following generic catch-alls are specifically prohibited as foundation ownership without a later explicit decision:

- `utils` as a broad miscellaneous module;
- universal `Context`;
- universal `Config`;
- universal `Metadata`;
- universal `State`;
- universal `Result`;
- global service locator/registry.

### `syngan.domain`

Purpose: accepted concept-owned semantic/control logic and typed state/value contracts.

This package holds the implementation of concept ownership and owner-specific lifecycle/invariant logic for the eleven accepted concepts. It MAY use multiple modules per concept or combine tightly coupled internal value structures where responsibility/volatility warrants it; 005-C does not impose one class per concept.

`domain` MUST NOT import application, ports, API, adapters, bootstrap, Spark/PyTorch/Databricks SDKs, persistence drivers, network clients, or platform lifecycle types.

### `syngan.ports`

Purpose: technology-neutral capability interfaces required by the application/runtime coordination boundary.

Later slices may define ports for control persistence, distributed data/source/output resolution, runtime execution, scheduler/Execution realization, dependency/artifact resolution, history/Provenance projection, authorization/disclosure, secrets, and observability.

Ports may depend on `foundation` and stable `domain` types. They MUST NOT depend on concrete adapters or composition/bootstrap.

A port MUST describe the guarantee SYNGAN needs rather than mirror a vendor SDK method-for-method.

### `syngan.application`

Purpose: use-case coordination and synchronization realization across accepted owners through domain contracts and ports.

Application coordination may implement prepare/commit/start/promote/recover/history flows, but MUST NOT become a new `Workflow`, `Manager`, `Session`, or metadata owner.

Application may depend on `foundation`, `domain`, and `ports`; it MUST NOT depend on concrete adapters or bootstrap.

### `syngan.api`

Purpose: stable user/programmatic surface such as specifications, typed handles, resource navigation and convenience facades.

API may depend on `foundation`, `domain`, `ports` where required for public protocols, and `application` coordination. It MUST NOT import concrete adapters or platform/runtime SDKs.

The API package cannot define an alternate canonical lifecycle merely to provide ergonomic methods.

### `syngan.adapters`

Purpose: concrete technology/platform/runtime implementations of accepted ports.

Adapters may depend on `foundation`, `domain`, and `ports` plus their own optional third-party dependencies.

Adapters SHOULD NOT import `application` or `api`. If an adapter appears to require an application-layer object, the boundary should first be checked for a missing/incorrect port contract rather than creating an inward dependency inversion.

Adapter siblings are independent by default. A Databricks adapter, for example, should not reach into a Spark adapter's private internals merely because both use Spark; shared capability code must be deliberately promoted to a narrow shared adapter-support boundary or port contract.

### `syngan.bootstrap`

Purpose: composition/wiring only.

Bootstrap may depend on API, application, ports, adapters, domain and foundation in order to build a configured deployment/client profile.

Bootstrap MUST NOT own canonical state or business semantics.

Runtime/profile selection occurs here or in equivalent outer composition—not through hidden imports in `domain`, `application`, or root package initialization.

## Root package behavior

`syngan.__init__` SHALL remain small and side-effect free.

It MAY re-export a deliberately curated stable public surface from `syngan.api`/stable public value types.

Importing `syngan` MUST NOT:

- import PySpark, PyTorch, Databricks or optional remote-service SDKs;
- open network connections;
- discover/download models or packages;
- initialize a SparkSession;
- connect to a database/catalog;
- inspect cloud credentials;
- configure global logging/telemetry;
- build a default mutable Session/Context singleton.

This requirement directly protects AF-02 and AF-12.

## Import dependency rules

The default permitted production dependency directions are:

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

api + application + ports + adapters + domain + foundation
    ↑
bootstrap
```

Equivalent explicit rules:

| Importer | May import | Must not import |
|---|---|---|
| `foundation` | stdlib + explicitly approved foundation dependency only | any outer SYNGAN package/adapters |
| `domain` | `foundation` | `ports`, `application`, `api`, `adapters`, `bootstrap` |
| `ports` | `foundation`, `domain` | `application`, `api`, `adapters`, `bootstrap` |
| `application` | `foundation`, `domain`, `ports` | `api`, `adapters`, `bootstrap` |
| `api` | `foundation`, `domain`, `ports`, `application` | `adapters`, `bootstrap` |
| `adapters` | `foundation`, `domain`, `ports`, adapter-local third-party SDKs | `application`, `api`, `bootstrap` by default |
| `bootstrap` | all production packages needed for wiring | canonical-state ownership |

Import Linter SHALL encode these constraints through layered/forbidden/independence contracts rather than relying only on reviewer memory.

Type-check-only imports MAY be excluded from runtime import-graph enforcement only when they do not create hidden runtime ownership/dependency and the exception is intentional.

## Optional dependency and extra isolation

### Base install

The base/core published dependency set MUST remain platform/model neutral.

The base install MUST NOT require by default:

- `pyspark`;
- `torch`;
- Databricks SDKs/connectors;
- MLflow;
- cloud-provider SDKs;
- remote model/service clients;
- GPU/CUDA libraries.

A third-party dependency may enter the base only when its capability is genuinely required by the portable core and cannot be isolated behind a port/adapter without unreasonable duplication or weakened correctness.

### Reserved adapter/runtime extras

The initial packaging design reserves capability extras equivalent to:

```text
spark
torch
databricks
```

Exact dependency/version contents are selected by the owning later slices (005-E/005-F/005-J).

Additional remote/provider extras may be introduced only with an explicit owner and network/egress contract.

There SHALL NOT initially be a broad `all` extra that silently installs every runtime/platform SDK. Users/deployments should opt into the capabilities they actually need.

### Development dependency groups

PEP 735-style dependency groups in `pyproject.toml` SHALL separate repository-only tooling from published extras. The initial logical groups are:

```text
test
lint
type
fitness
```

A convenience `dev` group MAY include these groups.

Later slices may add bounded groups such as `spark-test`, `torch-test`, `databricks-test`, `security-test`, `integration`, or `release` when their concrete requirements are accepted.

Test/runtime adapter groups MUST NOT be confused with published user extras.

## Test source topology

The physical test tree SHALL be equivalent to:

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

The tree maps to verification concerns without forcing one directory per V-layer.

### `tests/unit`

Fast deterministic V1 tests for bounded semantic/control behavior.

### `tests/contract`

Port/public contract tests and bounded component behavior, including implementation-neutral reusable contracts.

### `tests/fitness`

Explicit AF-01 through AF-20 architecture-fitness checks that are best represented as dedicated tests rather than import configuration.

### `tests/conformance`

Reusable conformance suites that every production adapter/runtime implementation of a shared port must satisfy.

Provider-specific suites may extend but MUST NOT weaken these common expectations.

### `tests/integration`

Real provider/runtime/storage/security integration profiles, split by concern so optional dependencies and credentials can remain isolated.

### `tests/scale`

V11 scale/performance/support evidence. These tests are not ordinary Q1 PR requirements.

### `tests/scenarios`

Reusable synthetic scenario builders expressing historical identities, activities, candidates, Attempts/checkpoints, Evidence/Provenance, security and capability conditions.

Scenario IDs should be stable and human-readable; they do not depend on production ID encoding.

### `tests/fixtures/golden`

Small versioned compatibility fixtures only for persisted/public/wire representations where exact shape/bytes matter.

Large generated data, model artifacts, checkpoints, Spark warehouse state and scale fixtures MUST NOT be committed here.

### `tests/support`

Test-only helpers/fakes/fault injectors. Production code MUST NOT import `tests.support`.

## Test-marker/profile policy

pytest markers SHALL represent execution requirements/cost/capability, not redefine semantic correctness.

Initial markers should cover concerns equivalent to:

```text
integration
spark
runtime
recovery
security
platform
network
scale
statistical
slow
```

Q0/Q1 selectors remain centrally defined; contributors SHOULD NOT invent ad hoc marker expressions in CI workflows that drift from local commands.

Core portable tests run with socket access disabled by default. Tests marked for network/platform integration must not be pulled into Q0/Q1 portable-core profiles accidentally.

## Stable developer command surface

The repository SHALL expose one small cross-platform verification command surface through:

```text
tools/verify.py
```

This script is repository tooling, not part of the published `syngan` package.

It SHOULD use the Python standard library for orchestration and invoke repository-declared tools rather than reimplement them.

Stable commands SHALL be equivalent to:

```text
uv run --locked python tools/verify.py q0
uv run --locked python tools/verify.py q1
uv run --locked python tools/verify.py q2 --profile <profile>
uv run --locked python tools/verify.py q3 [--profile <matrix>]
uv run --locked python tools/verify.py q4 [--profile <release-profile>]
```

The exact internal subprocess composition may evolve while these quality-gate meanings remain stable.

### Q0 planned composition

Q0 should contain at least:

- lock/config sanity;
- Ruff format check;
- Ruff lint check;
- mypy on the changed/inner package baseline as configured;
- Import Linter architecture contracts;
- fastest V0/V1/fitness subset;
- portable-core import/network-deny smoke.

### Q1 planned composition

Q1 should contain Q0 plus:

- complete deterministic V1 suite;
- relevant V2 contracts;
- required AF checks;
- migration/serialization contracts affected by the change;
- wheel/sdist build validation;
- clean built-wheel import smoke rather than source-tree-only import;
- base-install smoke proving optional Spark/Torch/Databricks SDKs are not required;
- bounded changed-slice integration suites when required by 005-B.

Q1 SHOULD exercise the declared minimum Python version in CI so syntax/tooling does not drift above Python 3.11 accidentally.

## CI selection and check mapping

GitHub Actions SHALL be the initial repository CI system because the source repository and pull-request governance are hosted on GitHub.

This is repository delivery tooling only and does not make GitHub part of SYNGAN runtime/platform semantics.

### Initial workflow/check architecture

The initial implementation should provide workflow/check responsibilities equivalent to:

```text
Q1 / static-and-structure
Q1 / unit-contract-fitness
Q1 / package-offline-core
```

Additional bounded checks may be activated based on changed slices, for example:

```text
Q1 / spark-contract
Q1 / recovery-contract
Q1 / security-contract
```

Q2 integration profiles may be workflow-dispatch, label/path-gated, environment-protected, or otherwise explicitly invoked where credentials/resources are required.

Q3 scheduled compatibility/resilience and Q4 release/support workflows remain separate from ordinary PR gating.

GitHub Actions and other workflow dependencies SHOULD be pinned to immutable revisions or otherwise governed against mutable action drift.

Branch protection SHOULD eventually require the stable Q1 checks defined by the implemented workflow; 005-C still does not claim protection exists until those workflows/checks actually exist and are functioning.

## Static typing policy

The Python 3.11 floor is also the static-type semantic floor.

The strictest mypy policy applies first to:

```text
foundation
domain
ports
application
api
```

because these packages define the most stable boundaries.

Adapter exceptions for weak third-party types must be module-scoped and documented. `Any` must not leak through public/port contracts merely to silence SDK typing problems.

## Import-time and packaging fitness

Q1 must test both repository and built-package behavior.

At minimum:

1. build wheel/sdist;
2. create/use a clean environment from the built artifact;
3. import `syngan` without optional extras;
4. verify no optional Spark/Torch/Databricks modules are imported as side effects;
5. verify no external network attempt occurs during import;
6. verify the installed package does not expose repository-only `tests` or `tools` unintentionally;
7. run a minimal API/foundation smoke from the installed package when implementation exists.

This directly protects the `src/` layout and AF-02/AF-12 assumptions.

## Source boundary ownership by later Phase 005 slices

005-C establishes the top-level topology. Later slices own concrete content:

| Slice | Primary package areas it refines |
|---|---|
| 005-D | `foundation`, `domain`, `application`, `ports`, `api`; control-persistence adapter boundaries |
| 005-E | distributed data/source/output ports + Spark/data adapters |
| 005-F | Strategy/method runtime ports + runtime adapters + Learned-State representation loading |
| 005-G | Execution/recovery application/domain/ports + scheduler/checkpoint adapters |
| 005-H | Evaluation/Evidence/Provenance/reproducibility domain/application/ports + query projections |
| 005-I | dependency/security/authorization/disclosure ports + adapters |
| 005-J | bootstrap/deployment/platform/observability adapters, support matrix and scale profiles |

Later slices MAY refine subpackages/modules but MUST preserve the accepted dependency direction or explicitly revise 005-C through normal governance.

## Dependency-introduction enforcement

Every new direct dependency MUST identify:

- its package area/owner;
- base versus published optional extra versus development group;
- why standard-library/current dependencies are insufficient;
- offline/private-provisioning behavior;
- network/telemetry/egress behavior;
- compatibility/system/native requirements;
- relevant test/conformance profile;
- removal/substitution consequence.

A PR that adds `pyspark`, `torch`, Databricks/cloud SDKs or external-service clients to base `project.dependencies` is presumptively invalid unless accompanied by an explicit accepted revision proving the portable core truly requires it.

## No hidden dynamic dependency acquisition

The package may use Python entry points or another later-approved plugin discovery mechanism, but plugin discovery MUST discover **already installed/provisioned** implementations.

Import-time/runtime code MUST NOT call package managers, PyPI, model hubs, public registries, Git checkout, or remote installers to satisfy missing implementation dependencies.

Dependency provisioning remains explicit and outside committed Learning/Generation/Evaluation runtime work.

## Build/release boundary

005-C establishes package-build mechanics but does not define public release/version policy.

Before any public distribution release, later planning MUST settle:

- public project/distribution name availability;
- license metadata/files;
- versioning/release policy;
- supported Python/platform matrix;
- signed/trusted publication workflow if adopted;
- SBOM/provenance/security release evidence;
- artifact retention.

The absence of those release choices does not block source implementation planning.

## Tool selection basis and upgrade policy

The selected foundational tools were chosen because they align with the accepted requirements:

- current Python packaging guidance supports `pyproject.toml` and `src/` layout;
- uv supports repository lock/sync and dependency groups while keeping published optional dependencies distinct;
- Ruff provides one lint/format tool;
- pytest provides fixture/marker/profile mechanics;
- Import Linter provides explicit forbidden/layer/independence contracts;
- current PySpark supports Python 3.10+, so the SYNGAN Python 3.11 floor does not itself prevent current Spark integration.

Tool versions SHALL be locked in `uv.lock` for development/CI and upgraded through ordinary dependency governance. Tool upgrades do not authorize changes to V0-V11, AF-01 through AF-20, package dependency direction, or semantic behavior.

## Explicitly deferred decisions

005-C does not yet choose:

- concrete domain class/file names inside the top-level packages;
- persistence/database technology;
- ID encoding;
- public API class/method spelling;
- exact Spark table/catalog/manifest technology;
- concrete PyTorch/distributed runtime implementation;
- scheduler/orchestrator/fencing backend;
- Provenance/query storage technology;
- IAM/policy/secret/network enforcement technology;
- observability backend;
- exact Databricks integration APIs;
- release versioning/license/publication details;
- final support/scale matrix.

Those remain owned by 005-D through 005-J or the release-readiness exit.

## Fitness obligations created/refined by 005-C

The source topology specifically operationalizes:

- **AF-01** — inward dependency direction through Import Linter;
- **AF-02** — optional/offline dependency closure through extras/groups + base-install smoke;
- **AF-12** — no hidden acquisition/network fallback through pytest-socket/core import tests;
- **AF-13** — no driver-materialization regressions through later Spark behavioral/static checks;
- **AF-20** — managed-platform implementation remains adapter-only by dependency rules.

Later slices implement the remaining behavioral fitness checks under this topology.

## Exit criteria

005-C is complete when:

- [x] initial distribution/import-package strategy is selected;
- [x] `src/` topology is selected;
- [x] Python compatibility floor is selected;
- [x] top-level production packages and ownership boundaries are defined;
- [x] shared foundation admission rules prevent a catch-all layer;
- [x] import direction/adapter isolation rules are explicit;
- [x] base versus optional/runtime versus development dependencies are separated;
- [x] concrete foundational build/environment/test/lint/type/import tools are selected;
- [x] test/conformance/fixture topology is defined;
- [x] stable Q0-Q4 command surface is defined;
- [x] initial GitHub Actions/Q1 check architecture is selected;
- [x] public/package import side-effect rules are defined;
- [x] later 005-D through 005-J package ownership is mapped;
- [x] no domain/runtime implementation is prematurely invented.

## Exit decision

**005-C — complete.**

Next:

**005-D — Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan**.
