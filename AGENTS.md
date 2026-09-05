# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Phase 005 is planning-only

Phase 005 does **not** authorize production implementation.

During 005-A through 005-K, agents may update planning/governance/documentation artifacts requested by the active group, but MUST NOT create production source, package scaffolds, database schemas/migrations, runtime/Spark/platform adapters, verification suites, CI workflows, or deployment infrastructure merely because the future implementation plan describes them.

A Phase 005 group marked `complete` means its plan is complete, not that the planned code exists.

## Start with authority, not repository-wide scanning

For any material task:

1. read `docs/index.md`;
2. read `docs/architecture/phase-004-consolidated-architecture-contract.md` for implementation-facing architecture;
3. read `docs/implementation/index.md` and the implementation authority relevant to the task;
4. read `docs/implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md` and identify affected verification/fitness obligations;
5. read `docs/implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md` for package/import/dependency/toolchain constraints;
6. for public handles/specs, durable identity, canonical state, persistence, transactions, historical resolution or migrations, read `docs/implementation/public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md`;
7. for Spark/data references, exact source state, manifests, candidates, sealed snapshots or output promotion, read `docs/implementation/spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md`;
8. for executable bindings, extension discovery, runtime invocation, Learning/Generation/Evaluation adapters or Learned-State physical representation/loading, read `docs/implementation/strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md`;
9. follow only the detailed concept/experience/architecture links needed for the active slice;
10. use ADRs for rationale when necessary, not as a replacement for current canonical authority.

Do not load or copy the entire documentation corpus by default.

## Authority order

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation authority / accepted plan
  > code / deployment
  > examples / generated artifacts / runtime state
```

Existing code does not override upstream authority. If implementation appears incompatible with an accepted contract, identify the conflict explicitly rather than silently redefining it in code.

## Current source topology contract

The accepted future production topology is rooted at `src/syngan/` with top-level responsibilities:

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

## Foundational toolchain plan

When a later phase explicitly authorizes implementation, use the accepted baseline:

- Python >=3.11 portable-core floor;
- `pyproject.toml`;
- uv + committed `uv.lock`;
- Hatchling;
- pytest + Hypothesis + pytest-socket;
- Ruff;
- mypy;
- Import Linter;
- coverage diagnostics;
- GitHub Actions.

Tool changes are governed implementation decisions.

## Durable identity and control-plane rules

005-D establishes one identity/version substrate for all later slices:

```text
AuthorityId
ResourceId
ResourceKind
ResourceRef
RevisionNumber / RevisionRef
SnapshotId
StateVersion
SchemaVersion
```

Do not:

- use database auto-increment IDs, paths, table names, Spark/Databricks run IDs, model IDs, timestamps, or Python object identity as canonical ResourceId;
- overload one generic `version` field across semantic revision, state concurrency, schema, Attempt epoch, package version, SPI version, codec version, or migration revision;
- make ORM/database row objects canonical domain/public resources;
- expose SQLAlchemy/Psycopg/Alembic types through foundation/domain/ports/application/API;
- mutate immutable commitment/revision payloads through ordinary update paths;
- use last-writer-wins for material canonical state;
- silently resolve an exact historical ref to current/latest authority;
- collapse absent/unavailable/unknown/invalid/withheld resolution into ordinary `None`;
- put source/generated rows, DataFrames, tensors, checkpoints, large diagnostics, or full Spark logs into bounded control records;
- put bearer secrets into canonical control records.

Material lifecycle mutation uses owner validation plus expected `StateVersion` CAS. Transactional outbox/durable-intent records are technical coordination state, not Provenance, Execution, or semantic completion.

## Spark/data-boundary rules

005-E establishes the future data-boundary plan.

Do not:

- treat a Spark DataFrame, query, table/path alias or path listing as durable committed source/output identity;
- bind committed work to a mutable selector when exact source-state preparation is required;
- confuse Spark/storage structural schema with Data Meaning;
- store one mandatory SQL/control row per physical file/component;
- treat a candidate materialization or sealed snapshot as a completed Generation output;
- let Evaluation Evidence for one sealed snapshot silently validate another snapshot;
- require a second full distributed copy merely to promote an already sealed candidate;
- design candidate write/seal ports without a future writer-fence/authority seam;
- make Delta/Iceberg/Hudi/Databricks or Parquet itself semantic authority.

Enterprise paths must not require complete source/output/component collection on the driver merely to establish identity, sealing, promotion or payload access.

## Runtime extension and Learned-State rules

005-F establishes the future executable extension boundary.

Keep these axes separate:

```text
Strategy / method semantic revision
ImplementationBindingRef revision
RuntimeSpiVersion
implementation package/build version
Learned-State codec/version
representation SchemaVersion
runtime/platform version
```

Agents MUST NOT:

- treat an installed/discovered Python entry point as a selected, trusted, compatible or semantically effective implementation;
- create a global mutable plugin registry as canonical runtime availability/authority;
- make `import syngan` scan/load plugins or import PyTorch/Spark optional runtimes;
- use one generic `run(context) -> Result` interface as the only Learning/Generation/Evaluation SPI;
- let runtime adapters receive unrestricted `SynGANClient`, SQL repositories/sessions, or arbitrary canonical mutation authority;
- let runtime success directly establish Learned State, completed Generation output, or Evidence;
- equate a checkpoint, candidate Learned-State representation, loaded PyTorch/Spark model, or state file with the logical Learned State identity;
- fabricate Learning/Learned State for direct-generation Strategies;
- make pickle/`.pt`/Spark model directories/ONNX/model registries the universal state format;
- require universal full-driver Learned-State loading/deserialization;
- silently change committed source, Strategy/configuration, Learned State, Conditions, Evaluation method/scope, dependency identity, or network posture inside a runtime Attempt;
- automatically install/download missing extension code/models/artifacts or switch to remote fallback;
- choose a concrete distributed launcher inside the SPI when 005-G/005-J own Execution/platform realization.

Future extension composition is explicit; optional Python entry-point discovery through the planned `syngan.runtime_extensions` group is lazy infrastructure only. Learned-State codecs must expose exact identity/version and material deserialization safety characteristics.

## Dependencies and optional integrations

The base/core distribution remains model/platform neutral.

Do not add PySpark, PyTorch, Databricks/cloud SDKs, MLflow, remote-model/service clients, CUDA/GPU runtimes, SQLAlchemy/Psycopg, or similar adapter dependencies to base runtime dependencies merely for one implementation slice.

Optional capability families belong behind their owning extras/adapters. Any new direct dependency requires explicit purpose/classification and compatibility/offline/network/security review.

Committed runtime execution must never install missing packages or download missing models/artifacts as an undocumented fallback.

## Scope and change discipline

Before material work, identify:

- the Phase 005 planning slice or later implementation slice;
- upstream architecture/implementation authority;
- change classification;
- affected verification layer(s), AF fitness IDs, and quality gates.

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
- let derived query indexes, telemetry, security audit, or SQL outbox become canonical domain state;
- treat resource-handle possession as authorization;
- weaken Evidence claim strength, Provenance history, exact historical binding, or disclosure distinctions for convenience.

## Verification

Material behavior changes, once coding is authorized, require verification appropriate to the implementation slice.

Tests derive their oracle from accepted authority, not merely current implementation output. Do not refresh snapshots/goldens blindly to bless a contract change.

Do not mock away the distributed, concurrency, security, persistence, runtime, or recovery property under test. Production adapters must satisfy reusable conformance contracts.

Portable/core pytest profiles use socket/network denial by default. Networked/platform tests must be explicitly profiled and narrowly allowed.

Never use retry-until-pass for stochastic/statistical tests, or weaken/quarantine/waive required architecture-fitness checks merely to make a change pass without 005-B governance.

005-F future runtime work directly contributes to V6 and AF-02/04/09/12/13/14/20. Extension conformance must prove runtime-result/semantic-result separation, immutable invocation, no hidden acquisition, optional dependency isolation, exact subject/state binding, state-codec safety and non-driver-local scale behavior.

The accepted quality-gate command surface remains planned around `tools/verify.py` under `uv run --locked`.

## Package/import behavior

The root `syngan` import remains side-effect free and must not automatically import optional Spark/Torch/Databricks/SQL persistence SDKs, scan plugin entry points, open network connections, create Spark sessions, inspect credentials, initialize telemetry, or create a mutable global Session/Context.

Future Q1 package verification must exercise a built/installed artifact. Production source must never import from `tests` or repository-only `tools`.

## Secrets and sensitive data

Never commit real credentials, tokens, passwords, private keys, or bearer secrets.

Do not place sensitive source rows, Learned-State payloads, protected diagnostics, or secret-bearing configuration in ordinary fixtures/logs/examples. Use synthetic/non-sensitive fixtures and explicit integration profiles.

## Documentation synchronization

When a durable implementation decision changes, update canonical `docs/implementation/` authority in the same change where practical.

If architecture itself changes, update `docs/architecture/` and relevant ADR rationale explicitly. Do not leave the new rule only in code, a PR description, or phase notes.

## Completion

Do not claim an implementation-planning slice complete unless its authority mapping, future source-boundary compliance, verification/fitness obligations, dependency/migration/security/network implications, and acceptance evidence requirements are accounted for.

Do not claim production implementation exists merely because a Phase 005 plan is complete.
