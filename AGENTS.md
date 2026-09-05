# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Start with authority, not repository-wide scanning

For any material task:

1. read `docs/index.md`;
2. read `docs/architecture/phase-004-consolidated-architecture-contract.md` for implementation-facing architecture;
3. read `docs/implementation/index.md` and the implementation authority relevant to the task;
4. read `docs/implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md` and identify affected verification/fitness obligations;
5. read `docs/implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md` for package/import/dependency/toolchain constraints;
6. follow only the detailed concept/experience/architecture links needed for the active slice;
7. use ADRs for rationale when necessary, not as a replacement for current canonical authority.

Do not load or copy the entire documentation corpus by default.

## Authority order

Treat conflicts using this direction:

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation authority / accepted plan
  > code / deployment
  > examples / generated artifacts / runtime state
```

Existing code does not override upstream authority.

If implementation appears incompatible with an accepted contract, identify the conflict explicitly. Do not silently redefine the contract in code.

## Current source topology contract

The accepted production topology is rooted at `src/syngan/` with top-level responsibilities:

```text
foundation
domain
ports
application
api
adapters
bootstrap
```

Dependency direction is inward.

Agents MUST NOT:

- move concept-owned behavior into `foundation` merely to avoid an import boundary;
- create generic `utils`, `Context`, `Config`, `Metadata`, `State`, `Result`, `Manager`, `Registry`, or Session-like ownership as a shortcut;
- make `domain` depend on ports/application/API/adapters/bootstrap;
- make application/API depend on concrete adapters;
- make optional adapter SDKs import-time requirements of the base package;
- bypass Import Linter/architecture fitness by adding broad ignored imports without an accepted boundary revision.

`bootstrap` may wire the full graph but does not own canonical state.

## Foundational toolchain

When implementation scaffolding begins, use the accepted baseline rather than introducing competing tools casually:

- Python >=3.11 portable-core floor;
- `pyproject.toml` project/tool configuration;
- uv + committed `uv.lock` for repository environment/resolution;
- Hatchling build backend;
- pytest + Hypothesis + pytest-socket;
- Ruff;
- mypy;
- Import Linter;
- coverage reporting;
- GitHub Actions repository CI.

Tool changes are governed implementation decisions. Do not add a second formatter/linter/type system/task environment merely because generated code prefers it.

## Dependencies and optional integrations

The base/core distribution remains model/platform neutral.

Do not add PySpark, PyTorch, Databricks/cloud SDKs, MLflow, remote-model/service clients, CUDA/GPU runtimes, or similar platform dependencies to base runtime dependencies merely for one implementation slice.

Optional capability families such as Spark, Torch and Databricks belong behind adapter/runtime extras defined by their owning later Phase 005 slices.

Any new direct dependency must have an explicit purpose and correct classification (core, development/verification, optional adapter/runtime, or build/release) and must be reviewed for compatibility, offline/private provisioning, network/telemetry behavior, and material security/supply-chain implications.

Committed runtime execution must never install missing packages or download missing models/artifacts as an undocumented fallback.

## Scope and change discipline

Before material implementation work, identify:

- the Phase 005 implementation slice;
- upstream architecture/implementation authority;
- whether the change is local, implementation-realization, public/persisted-contract, architecture-affecting, or semantic/experience-affecting;
- affected verification layer(s), architecture-fitness IDs, and quality gate(s).

Keep changes bounded to the requested slice. Avoid opportunistic refactors, dependency additions, package moves, terminology changes, or API/schema changes outside scope.

## Non-negotiable architecture guardrails

Do not:

- make Spark DataFrames, PyTorch/Spark model objects, platform runs, paths, aliases, or process-local objects canonical SYNGAN identity;
- collapse typed semantic/operational/security/history state into one generic status/result/context owner;
- equate checkpoint/candidate/runtime material with Learned State/completed output/Evidence;
- let runtime/platform adapters establish semantic completion directly;
- replace Attempt fencing with lease expiry, scheduler retry, or last-writer-wins;
- hide dependency/model/package downloads, remote fallback, telemetry, or egress;
- require full source/output/Learned-State/diagnostic collection to the driver on enterprise paths;
- make Databricks, PyTorch, Spark ML, CTGAN, or another runtime/platform universal semantics;
- let derived query indexes, telemetry, or security audit become canonical domain state;
- treat resource-handle possession as authorization;
- weaken Evidence claim strength, Provenance history, exact historical binding, or disclosure distinctions for convenience.

## Verification

Material behavior changes require verification appropriate to the implementation slice.

Canonical verification authority: `docs/implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md`.

Tests must derive their oracle from accepted authority rather than merely capture current implementation behavior. Do not refresh snapshots/goldens blindly to bless a contract change.

Do not mock away the distributed, concurrency, security, persistence, or recovery property actually under test. Production adapters must ultimately satisfy their reusable conformance contract.

Portable/core pytest profiles use socket/network denial by default. Networked/platform tests must be explicitly profiled and narrowly allowed.

Never use unbounded retry-until-pass for stochastic/statistical tests. A passing retry does not erase a prior assertion failure.

Never weaken, delete, quarantine, waive, or bypass a required architecture-fitness check merely to make a change pass without the explicit governance required by 005-B.

The accepted stable quality-gate command surface is planned around `tools/verify.py` under `uv run --locked`; do not create unrelated local/CI command stacks that drift from those meanings.

A successful local run is not sufficient completion evidence for a material slice.

## Package/import behavior

The root `syngan` import must remain side-effect free and must not automatically import optional Spark/Torch/Databricks SDKs, open network connections, create Spark sessions, inspect cloud credentials, initialize telemetry, or create a mutable global Session/Context.

Q1 package verification must ultimately exercise a built/installed artifact, not only imports from the repository checkout.

Production source must never import from `tests` or repository-only `tools`.

## Secrets and sensitive data

Never commit real credentials, tokens, passwords, private keys, or bearer secrets.

Do not place sensitive source rows, Learned State payloads, protected diagnostics, or secret-bearing configuration in ordinary fixtures/logs/examples. Use synthetic/non-sensitive fixtures and explicit test/integration profiles.

## Documentation synchronization

When a durable implementation decision changes, update its canonical `docs/implementation/` authority in the same change where practical.

If the architecture itself changes, update `docs/architecture/` and relevant ADR rationale explicitly. Do not leave the new rule only in code, a PR description, or phase notes.

## Completion

Do not claim an implementation slice complete unless its required authority mapping, source-boundary compliance, verification layers/fitness checks, dependency/migration/security/network implications, and acceptance evidence are accounted for.

Canonical governance:

- `docs/implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md`
- `docs/implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md`
- `docs/implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md`
