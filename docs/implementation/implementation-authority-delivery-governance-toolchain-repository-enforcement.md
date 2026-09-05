---
type: Implementation Authority
title: Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement
status: active
---

# Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement

## Purpose

Define the governance boundary under which SYNGAN implementation planning, source code, tests, migrations, dependencies, build/test tooling, platform adapters, and delivery changes may be introduced after the Phase 004 architecture exit.

This document is the canonical Phase 005-A implementation authority. It establishes **how implementation decisions are authorized, traced, reviewed, changed, verified, and enforced** before later Phase 005 groups select detailed package/module topology and concrete implementation technologies.

It intentionally does **not** yet select a Python version, build backend, dependency manager, lockfile technology, test runner, formatter/linter, type checker, database, Spark table provider, scheduler, policy engine, CI vendor, or deployment topology.

## Governing authority

Implementation work remains downstream of:

- [Documentation Governance and Anti-Drift Rules](../authority/documentation-governance.md);
- [Accepted Concepts](../concepts/index.md);
- [Accepted Synchronizations](../synchronizations/index.md);
- [Phase 003 Consolidated Experience Contract](../experience/phase-003-consolidated-experience-contract.md);
- [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md);
- the detailed architecture authority relevant to the implementation slice;
- active ADR rationale when a material architecture choice is being implemented.

The governing implementation rule is:

> **Implementation is a realization of accepted authority, not a new authority layer that may silently redefine it. Every material implementation choice must either fit the accepted contracts or explicitly escalate the smallest required upstream revision.**

## Implementation authority hierarchy

For implementation conflicts, use this order:

```text
cross-cutting design/documentation authority
        ↓
accepted concepts + synchronizations
        ↓
accepted experience contracts
        ↓
accepted architecture contracts
        ↓
canonical implementation authority / accepted slice plan
        ↓
source code + migrations + configuration
        ↓
derived/generated artifacts + runtime/platform state
```

Architecture Decision Records explain architectural rationale but do not override newer canonical architecture. Phase records preserve planning/execution history but do not replace promoted canonical implementation authority.

### Code is executable evidence, not a permission source

Existing code does not win a conflict merely because it is implemented.

If code conflicts with upstream authority, one of the following must happen explicitly:

1. the code is corrected to match authority; or
2. a genuine infeasibility is demonstrated and the appropriate upstream authority is revised through its normal governance path before the conflicting behavior becomes accepted.

`It already works this way`, `the library expects it`, or `the platform makes it easier` are not sufficient reasons to redefine SYNGAN semantics.

## Canonical implementation knowledge

Durable implementation-planning decisions belong under `docs/implementation/` once accepted.

A phase record may discover a decision, but a durable implementation rule should be promoted to the smallest canonical implementation document that owns it.

Implementation documents should prefer references to architecture/concepts over copying their full text.

### Implementation decision versus architecture decision

An implementation choice belongs in implementation authority when it chooses **how to realize** an already-accepted architecture without materially changing its contract.

Examples:

- selecting a particular Python serialization library behind an accepted port;
- choosing physical table names or repository classes that preserve accepted ownership;
- selecting a concrete conditional-write mechanism that satisfies the accepted fencing contract;
- choosing one test tool that exercises already-required fitness properties.

An implementation choice requires architecture review/update when it changes **what guarantee exists or where authority lives**, for example:

- removing exact source-state binding;
- replacing fenced Attempt writes with last-writer-wins;
- making a Databricks run the canonical Execution identity;
- changing candidate sealing/promotion semantics;
- making runtime output itself Evidence;
- making a query/index store canonical Provenance;
- weakening no-egress guarantees;
- making one platform/runtime mandatory for semantic reasons not already accepted.

## Change classification

Every material change should be classified before implementation.

### Class 0 — local/non-contractual maintenance

Examples:

- typo or comment correction;
- internal rename with no public/persisted/runtime effect;
- refactor proven behaviorally equivalent by existing tests;
- test fixture cleanup that does not change asserted contract.

Requirements:

- normal review/tests;
- no new implementation authority required unless the change exposes a missing rule.

### Class 1 — implementation realization decision

Examples:

- new internal module implementing an accepted port;
- dependency addition;
- persistence mapping;
- schema/index implementation;
- adapter implementation;
- developer/build/test tooling change.

Requirements:

- trace to accepted architecture/slice authority;
- document material dependency/compatibility/migration effects;
- update canonical implementation authority when the decision is durable;
- provide verification evidence.

### Class 2 — public/persisted/compatibility contract change

Examples:

- public API shape or behavior;
- persisted schema/wire format;
- identifier encoding exposed across boundaries;
- plugin/SPI contract;
- compatibility/support matrix;
- migration behavior;
- security-sensitive capability boundary.

Requirements:

- explicit implementation-plan update before or in the same change;
- compatibility/migration analysis;
- architecture conformance review;
- new/updated fixtures and contract tests;
- deprecation/migration strategy where existing consumers/data may be affected.

### Class 3 — architecture-affecting change

Any change that would weaken, contradict, relocate, or materially reinterpret an accepted Phase 004 guarantee is Class 3.

Requirements:

- stop ordinary implementation of the conflicting design;
- document the specific conflict/infeasibility;
- update the relevant canonical architecture and ADR if the architecture is intentionally changed;
- re-check downstream implementation plans/tests before proceeding.

### Class 4 — semantic/experience change

Any change to concept ownership, lifecycle meaning, synchronization, or required actor/programmatic experience is outside ordinary implementation authority.

Requirements:

- reopen the appropriate upstream design layer explicitly;
- do not disguise the change as refactoring, API ergonomics, or platform adaptation.

## Delivery-unit contract

Implementation should advance in **reviewable vertical slices** that can demonstrate one bounded set of architecture obligations end to end.

A delivery slice should identify:

```text
upstream concept / experience obligations
        ↓
architecture authority
        ↓
implementation authority / plan
        ↓
owned modules / ports / adapters / schemas
        ↓
implementation change
        ↓
verification / fitness tests
        ↓
acceptance evidence
```

A slice is not complete merely because code compiles, a notebook works once, or a platform job succeeds.

### Scope discipline

A delivery change SHOULD avoid opportunistic unrelated refactors. If adjacent cleanup materially enlarges the review surface, separate it unless the cleanup is required to satisfy the slice.

Agents and humans MUST NOT use `while I am here` changes to introduce unrelated dependencies, rename authority-bearing concepts, move module boundaries, or alter public/persisted contracts without the appropriate change classification.

### Experimental spikes

Exploratory/prototype code MAY be used to test feasibility, but it is non-authoritative until:

- its assumptions are reconciled with accepted architecture;
- its dependencies/security/network behavior are reviewed;
- the relevant implementation slice accepts the approach;
- production-quality verification/migration obligations are defined.

Prototype success does not bypass Phase 005 planning.

## Completion and acceptance evidence

No implementation slice should be marked complete without evidence appropriate to its risk.

At minimum, a completed material slice should be able to point to:

- the upstream authority it implements;
- the accepted implementation boundary/plan;
- implementation files changed;
- automated tests/fitness checks that exercise the material contract;
- test execution result or CI evidence;
- migration/backward-compatibility assessment where persisted/public state changed;
- dependency changes and their rationale;
- network/egress/offline implications where relevant;
- security/disclosure implications where relevant;
- scale/resource assumptions where relevant;
- intentionally deferred work with an owner/phase/backlog reference.

005-B will define the concrete verification harness and evidence-fixture structure. This phase establishes that such evidence is mandatory, not optional documentation added after coding.

## Definition of done hierarchy

A slice may progress through implementation states such as:

```text
planned
  ↓
implemented locally
  ↓
verified against slice tests
  ↓
architecture fitness checks pass
  ↓
integration/security/migration evidence complete where applicable
  ↓
accepted / merge-ready
```

`Implemented locally` is not synonymous with `complete`.

A failing or waived required check must remain explicit. Waivers may be time-bounded exceptions with rationale/owner/follow-up; they must not silently redefine the baseline.

## Toolchain governance

### Toolchain is repository-owned

Development, build, test, migration, documentation, and release behavior must be reproducible from repository-declared configuration rather than undocumented workstation state.

When Python implementation begins:

- `pyproject.toml` SHOULD be the canonical Python project/build/tool metadata entry point unless an accepted tool requires a separate configuration file;
- direct runtime/build/test dependencies MUST be declared in repository-controlled metadata;
- supported Python/Spark/platform/runtime versions MUST eventually be stated in an explicit compatibility/support matrix rather than inferred from one developer machine;
- a reproducible dependency-resolution mechanism (lock/constraints/equivalent) MUST be selected for developer/CI environments where exact resolution matters;
- library dependency ranges and reproducible development/CI resolution MAY be represented differently when packaging semantics require it, but the distinction must be intentional and documented.

005-B/005-C will select the concrete tools and topology after their requirements are known.

### Stable developer commands

Once executable tooling exists, the repository SHOULD provide a small stable set of documented commands or task entry points for common work such as:

- environment/bootstrap validation;
- unit/contract tests;
- architecture fitness checks;
- static/lint/type checks where selected;
- integration tests;
- packaging/build validation;
- migrations/schema validation;
- offline/no-egress checks where applicable.

Developers and CI should invoke the same underlying commands rather than maintain unrelated local and CI workflows.

The exact task runner/command spelling is deferred.

### No hidden global prerequisites

A supported development/test path MUST document material prerequisites and MUST NOT depend silently on:

- globally installed Python packages outside declared tooling;
- a particular notebook state;
- a developer's personal cloud credentials;
- a public model/package download triggered at test/runtime without explicit setup;
- ambient Databricks/Spark configuration that is not represented by the selected test profile;
- untracked local files containing required state.

## Dependency governance

Dependencies are architectural surface area and must be introduced deliberately.

### Dependency classes

Later project metadata should distinguish at least:

1. **core runtime dependencies** — required for the portable supported core;
2. **development/verification dependencies** — needed to build/test/lint/type/check the project;
3. **optional adapter/runtime dependencies** — Spark platform, PyTorch/model runtime, Databricks, external services, or other optional integrations;
4. **build/release dependencies** — package construction/publishing tooling.

A dependency MUST NOT be placed in the core merely because it is convenient for one adapter.

### Dependency intake review

Adding or materially changing a direct dependency should record, where relevant:

- purpose and owning implementation slice;
- whether equivalent functionality already exists in the standard library/current dependency set;
- runtime versus dev/build/optional classification;
- supported version range and compatibility implications;
- transitive dependency/size implications;
- license suitability;
- known security/supply-chain considerations appropriate to project maturity;
- native/system/GPU/JVM requirements;
- network/download behavior;
- offline/private-repository availability expectations;
- data-egress/telemetry behavior if any;
- removal/substitution path if the dependency becomes unavailable.

### Runtime installation/download prohibition

Committed Learning/Generation/Evaluation execution MUST NOT perform package installation or model/artifact acquisition as an undocumented convenience fallback.

Dependencies/artifacts required at runtime must be provisioned explicitly under the 004-H dependency/security contract.

Tests must not normalize hidden network acquisition as expected behavior.

### Optional integration isolation

Optional integration dependencies must remain import/runtime-isolatable so supported offline/core use does not require installing or importing unrelated remote/platform/model-runtime SDKs.

Concrete extras/plugin packaging is deferred to 005-C/005-F/005-J.

## Repository structure governance

### Repository-native authority surfaces

The repository currently contains documentation only. 005-A establishes these immediate governance surfaces:

- `docs/index.md` — canonical knowledge entry;
- `docs/implementation/index.md` — implementation authority entry;
- root `AGENTS.md` — concise repository-wide agent execution rules referencing canonical authority;
- `.github/pull_request_template.md` — review checklist for authority, verification, dependency, migration, security/network, and deferred-work disclosure.

These files are navigation/enforcement aids. They do not outrank canonical design/implementation authority.

### Source/package topology is not selected here

005-A MUST NOT invent placeholder `src/`, package, persistence, adapter, or test module boundaries merely to make the repository look implementation-ready.

005-C owns source/package topology after 005-B has defined executable verification obligations.

### Generated/vendor material

Generated, vendored, cache, build, large fixture, model, and data artifacts must not be committed casually.

Later tooling should define:

- what generated artifacts are reproducible and therefore excluded from source control;
- what small golden fixtures belong in source control for deterministic verification;
- what large fixtures/artifacts use external/local test data providers;
- how third-party notices/licenses are retained if vendoring is ever approved;
- secret scanning and artifact-size limits where CI/platform supports them.

## Main-branch and review governance

Once implementation source/configuration is introduced, material changes SHOULD merge to the default branch through reviewable pull requests and automated required checks.

005-A does not claim GitHub branch protection or CI checks are already enabled. 005-B should define the required checks before enforcement is configured.

A production implementation change should not bypass failed required checks by deleting/weakening the check in the same change without explicit rationale and review.

### Pull-request traceability

A material PR should state:

- implementation slice/phase;
- upstream architecture/implementation authority;
- change classification;
- verification performed;
- dependency/toolchain changes;
- public/persisted compatibility/migration impact;
- network/egress/security impact;
- scale/performance impact where material;
- deferred/follow-up items.

The repository PR template operationalizes this requirement.

## Agent and Codex governance

Automated implementation agents are contributors subject to the same authority and review rules as humans.

The root `AGENTS.md` is the concise machine-facing entry point and SHALL reference canonical authority rather than duplicate the full design corpus.

Agents MUST:

- begin with repository/index guidance and load only the relevant authority needed for the task;
- identify the implementation slice and upstream contract before making material code changes;
- preserve accepted terminology and typed owner boundaries;
- classify architecture-affecting conflicts instead of silently resolving them in code;
- add/update verification alongside material behavior;
- disclose dependency, network, egress, persistence, migration, and security changes;
- keep optional integrations isolated;
- avoid full-driver collection or hidden remote fallback on enterprise paths;
- preserve exact historical identity, promotion, fencing, Evidence, Provenance, and authorization guarantees;
- keep generated scope bounded to the requested slice.

Agents MUST NOT:

- treat README/examples/tests as higher authority than canonical documents;
- invent a new `Manager`, `Session`, `Metadata`, `Registry`, `Context`, or generic `Result` ownership layer to simplify implementation;
- add a dependency merely because it makes code generation easier;
- switch platform/runtime/storage technology silently when an operation fails;
- weaken a test or architectural invariant solely to make a change pass;
- make broad cleanup/refactor changes outside the active slice without an explicit reason;
- claim a slice complete without the required acceptance evidence.

## Architecture fitness enforcement ownership

005-A establishes that architecture fitness properties are enforceable repository obligations.

005-B owns the concrete checks, but later CI should be able to detect or exercise properties such as:

- semantic/control code does not import concrete platform adapters;
- optional network/runtime integrations are absent from supported offline-core dependency closure;
- public/non-final/promoted resource types are not interchangeable accidentally;
- committed historical state is immutable through public mutation paths;
- stale Attempt writers are rejected;
- promotion/Evidence establishment is idempotent;
- query projections do not become canonical write dependencies;
- restricted query/history views cannot bypass authorization;
- enterprise paths do not require full `collect()`/driver materialization;
- platform capability fallback never silently weakens accepted semantics.

An architecture fitness check is not optional style tooling when it protects a Phase 004 invariant.

## Migration and compatibility governance

### Persisted state changes

Once persisted schemas exist, changes must distinguish:

```text
semantic revision
        ≠
persistence schema migration
        ≠
current lifecycle-state update
```

A migration must preserve stable resource identity, immutable commitment/history, correction/supersession semantics, and actor disclosure state unless an explicitly approved compatibility change says otherwise.

Destructive rewrites of historical committed state are not ordinary migrations.

### Public/API/SPI evolution

Public API, persisted representation, wire protocol, plugin SPI, Learned State codec, manifest/checkpoint schema, and platform-adapter protocol may evolve independently.

Compatibility must be assessed on the affected axis rather than hidden behind the package version alone.

### Deprecation

Once external or persisted compatibility exists, breaking changes should normally use an explicit deprecation/migration path unless an approved pre-release compatibility policy states otherwise.

The exact semantic-versioning/release policy is deferred until package/release planning has enough context.

## Security and secret governance for implementation work

Source control MUST NOT contain real credentials, private keys, access tokens, passwords, or equivalent bearer secrets.

Examples/configuration/fixtures must use placeholders or dedicated test credentials supplied through approved test/deployment mechanisms.

Logs, snapshots, golden fixtures, test failures, and generated evidence must avoid including sensitive source rows, Learned State payloads, or diagnostic material unless the fixture is explicitly synthetic/non-sensitive and suitable for source control.

A convenience test that requires broad personal cloud credentials is not a substitute for an explicit integration-test profile.

## Documentation synchronization during implementation

Code and documentation changes should remain synchronized at the smallest authoritative layer.

When implementation reveals a durable choice:

- update `docs/implementation/` if it is an implementation realization decision;
- update `docs/architecture/` and ADR rationale if the architecture itself changes;
- reopen upstream semantic/experience authority only when that layer truly changes;
- update phase records as planning/execution evidence, not as the sole source of current truth.

README and examples remain orientation/usage surfaces and should link to current authority rather than restating large rules.

## Release and completion claims

No release or implementation-ready claim should imply guarantees that have not been verified for the declared environment/profile.

In particular, claims such as:

- `enterprise scale`;
- `offline/no-egress`;
- `Databricks compatible`;
- `reproducible`;
- `secure`;
- `supports N rows`;

require explicit scope, environment, Strategy/runtime, and verification basis rather than being inferred from architecture intent alone.

Benchmark/support claims remain downstream of 005-J and later implementation evidence.

## Exceptions and waivers

A temporary waiver to an implementation governance rule must be explicit and bounded.

A waiver should identify:

- the rule/check being waived;
- reason;
- affected scope;
- risk;
- owner/follow-up;
- expiration or removal condition where practical.

A waiver MUST NOT be used to authorize contradiction of concept/experience authority. Architecture-level exceptions require architecture review rather than an implementation waiver.

## 005-A accepted implementation-governance invariants

1. Implementation is downstream realization, not authority override.
2. Durable implementation decisions have one canonical home under `docs/implementation/` once accepted.
3. Existing code does not outrank architecture.
4. Architecture-affecting implementation conflicts are escalated explicitly rather than hidden in code.
5. Material implementation work remains traceable from upstream authority through verification evidence.
6. A slice is not complete merely because code runs once or compiles.
7. Toolchain/build/test behavior is repository-declared and reproducible rather than workstation-defined.
8. Concrete tool selection waits until its requirements are known; governance does not invent tools prematurely.
9. Direct dependencies are classified and reviewed as architecture/security/offline surface area.
10. Runtime package/model acquisition is never a hidden fallback.
11. Optional integrations remain isolatable from the supported portable/offline core.
12. Source/package topology is selected only after verification obligations are defined.
13. Material implementation changes should flow through review and automated checks once those checks exist.
14. Agents and humans follow the same authority/change/evidence rules.
15. Agents use progressive disclosure and do not load/copy the entire corpus by default.
16. Architecture fitness checks are product correctness controls, not optional style preferences.
17. Public/persisted/SPI changes require compatibility and migration analysis.
18. Persistence migrations do not rewrite immutable historical meaning.
19. Real secrets never belong in source, fixtures, logs, or canonical history.
20. README/examples/telemetry/generated artifacts remain below canonical implementation authority.
21. Required check waivers are explicit, bounded, and cannot override upstream semantic authority.
22. Product/scale/security/offline claims require scoped verification evidence.

## Decisions deliberately deferred

005-A intentionally does not yet choose:

- supported Python version(s);
- `uv`, `pip-tools`, Poetry, PDM, Hatch, or another dependency/environment manager;
- build backend;
- test runner/plugins;
- formatter/linter/type checker;
- source layout or package names;
- CI workflow/vendor/check names;
- database/migration framework;
- Spark/table/catalog implementation;
- scheduler/fencing mechanism;
- plugin discovery mechanism;
- PyTorch/distributed runtime technology;
- IAM/policy/secret/network tooling;
- observability vendor;
- release/versioning policy;
- benchmark/support thresholds.

005-B defines verification requirements/tooling. 005-C then defines source/package boundaries and the concrete foundational toolchain needed to enforce them. Later slices choose technologies only where their architecture-specific requirements are available.

## Phase handoff

005-A establishes implementation authority and repository governance without introducing production source topology prematurely.

Next:

**005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**.
