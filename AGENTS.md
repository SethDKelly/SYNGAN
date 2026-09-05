# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Current program boundary

**Phase 005 is implementation planning only.**

Unless a later phase explicitly authorizes production coding, agents working in Phase 005 MUST NOT create or modify production source code, package scaffolds/tool configuration, database schemas/migrations, Spark/runtime adapters, test suites, CI workflows, deployment infrastructure, or runtime/platform configuration merely because the corresponding plan is detailed enough to implement.

During Phase 005, terms such as `implementation sequence`, `package path`, `class`, `port`, `adapter`, `migration`, and `quality gate` describe **future implementation contracts**.

## Start with authority, not repository-wide scanning

For any material task:

1. read `docs/index.md`;
2. read `docs/architecture/phase-004-consolidated-architecture-contract.md` for implementation-facing architecture;
3. read `docs/implementation/index.md` and the implementation plan relevant to the task;
4. read `docs/implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md` and identify affected verification/fitness obligations;
5. read `docs/implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md` for package/import/dependency/toolchain constraints;
6. for public handles/specs, durable identity, canonical state, persistence, transactions, historical resolution or migrations, read `docs/implementation/public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md`;
7. for Spark selectors/access, exact source state, manifests, candidates, sealed snapshots, output representations or Generation promotion, read `docs/implementation/spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md`;
8. follow only the detailed concept/experience/architecture links needed for the active slice;
9. use ADRs for rationale when necessary, not as a replacement for current canonical authority.

Do not load or copy the entire documentation corpus by default.

## Authority order

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation planning authority
  > future code / deployment
  > examples / generated artifacts / runtime state
```

Existing or future code does not override upstream authority. If implementation later appears incompatible with an accepted contract, identify the conflict explicitly rather than silently redefining it in code.

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

- create this scaffold during Phase 005 merely because it is planned;
- move concept-owned behavior into `foundation` to avoid an import boundary;
- create generic `utils`, `Context`, `Config`, `Metadata`, `State`, `Result`, `Manager`, `Registry`, or Session-like ownership as a shortcut;
- make `domain` depend on ports/application/API/adapters/bootstrap;
- make application/API depend on concrete adapters;
- make optional adapter SDKs import-time requirements of the base package;
- bypass future Import Linter/architecture fitness by adding broad ignored imports without an accepted boundary revision.

`bootstrap` may eventually wire the full graph but does not own canonical state.

## Foundational toolchain plan

When a later phase explicitly begins implementation, use the accepted baseline:

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

Do not instantiate this toolchain during Phase 005 unless the phase program is explicitly changed to authorize coding.

## Durable identity and control-plane rules

005-D establishes one future identity/version substrate for all later slices:

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

Do not plan or later implement competing replacements.

Do not:

- use database auto-increment IDs, paths, table names, Spark/Databricks run IDs, model IDs, timestamps, or Python object identity as canonical ResourceId;
- overload one generic `version` field across semantic revision, state concurrency, schema, Attempt epoch, package version, or migration revision;
- make ORM/database row objects canonical domain/public resources;
- expose SQLAlchemy/Psycopg/Alembic types through foundation/domain/ports/application/API;
- mutate immutable commitment/revision payloads through ordinary update paths;
- use last-writer-wins for material canonical state;
- silently resolve an exact historical ref to current/latest authority;
- collapse absent/unavailable/unknown/invalid/withheld resolution into ordinary `None`;
- put source/generated rows, DataFrames, tensors, checkpoints, large diagnostics, or full Spark logs into bounded control records;
- put bearer secrets into canonical control records.

Future material lifecycle mutation uses owner validation plus expected `StateVersion` CAS. Persistence adapters enforce conditional writes; they do not decide semantic transition legality.

The planned built-in SQL boundary is adapter-only SQLAlchemy Core + Alembic, with PostgreSQL as reference production control backend and SQLite restricted to local/test evidence. Transactional outbox/durable-intent records remain technical coordination state, not Provenance, Execution, or semantic completion.

## Spark/data boundary rules

005-E establishes the future Spark/data contract.

Do not:

- treat DataFrame/table/path/query values as durable source or output identity;
- store a live DataFrame in a committed specification/snapshot;
- assume rerunning an arbitrary query/DataFrame plan recreates the historical source state;
- treat path/file existence as candidate seal or Generation completion;
- make candidate materialization or sealed data snapshot interchangeable with `GenerationOutput`;
- copy full manifest component membership into bounded control SQL or one required driver list;
- make Delta, Iceberg, Hudi, Databricks, or Parquet itself semantic authority;
- require a second full data copy merely to promote a sealed candidate;
- silently materialize/snapshot data into another security domain;
- omit the future writer-fence parameter from candidate write/seal boundaries simply because 005-G has not yet specified Attempt epochs.

The planned source-resolution posture is conservative:

```text
exact SourceStateRef
    -> reuse exact state

provider-native exact snapshot
    -> bind exact native state

arbitrary DataFrame/query/mutable locator
    -> distributed snapshot preparation before commitment
       unless exact stable binding is proved
```

The planned physical chain remains:

```text
candidate materialization
    -> sealed exact data snapshot
    -> required Evaluation/Evidence
    -> one logical GenerationOutput
```

Sealing is not semantic completion.

## Dependencies and optional integrations

The base/core distribution remains model/platform neutral.

Do not place PySpark, PyTorch, Databricks/cloud SDKs, MLflow, remote-model/service clients, CUDA/GPU runtimes, SQLAlchemy/Psycopg, or similar adapter dependencies into base runtime dependencies merely for one planned slice.

005-E reserves Spark as an optional capability. `syngan[spark]` must not implicitly mean Databricks, Delta/Iceberg/Hudi, cloud SDKs, or remote catalog clients.

Any future direct dependency requires explicit purpose/classification and compatibility/offline/network/security review.

Committed runtime execution must never install missing packages or download missing models/artifacts as an undocumented fallback.

## Scope and change discipline

Before material work, identify:

- the active Phase 005 planning slice;
- upstream architecture/implementation-planning authority;
- whether the work is planning/documentation only or later explicitly authorized implementation;
- affected verification layer(s), AF fitness IDs, and quality gates.

Keep changes bounded to the requested slice.

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

005-B defines future verification obligations. During Phase 005, agents plan these tests/gates but do not create production verification suites unless later coding is explicitly authorized.

Future tests must derive their oracle from accepted authority, not merely current implementation output. Do not plan blind snapshot/golden refresh as a contract-change mechanism.

Future portable/core pytest profiles use socket/network denial by default. Networked/platform tests must be explicitly profiled and narrowly allowed.

For 005-E future implementation, V5 and AF-03/04/08/13/17 are direct concerns, with AF-07 completed after 005-G defines Attempt fencing.

## Secrets and sensitive data

Never commit real credentials, tokens, passwords, private keys, bearer secrets, sensitive source rows, Learned State payloads, or protected diagnostics into planning fixtures/examples.

## Documentation synchronization

When a durable planning decision changes, update canonical `docs/implementation/` authority.

If architecture itself changes, update `docs/architecture/` and relevant ADR rationale explicitly.

## Completion

During Phase 005, `complete` means the **implementation plan** for that slice is complete, not that production code exists.

Canonical planning authority currently includes:

- `docs/implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md`
- `docs/implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md`
- `docs/implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md`
- `docs/implementation/public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md`
- `docs/implementation/spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md`
