---
type: Implementation Index
title: SYNGAN Implementation Planning & Delivery Authority
status: active
---

# SYNGAN Implementation Planning & Delivery Authority

## Purpose

This directory is the canonical home for **implementation planning** decisions that translate accepted architecture into future source/module boundaries, toolchain expectations, persisted/wire representations, implementation slices, migrations, verification obligations, platform integration plans, delivery sequencing, and acceptance evidence.

**Phase 005 is planning-only.** Documents under this directory may select concrete future implementation technologies/interfaces and define dependency-safe coding sequences, but they do not authorize production source, schema, migration, workflow, infrastructure, or runtime implementation during Phase 005.

Implementation authority is downstream of the [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md) and MUST NOT redefine accepted semantic, experience, or architecture authority for implementation convenience.

## Start here

- [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](implementation-authority-delivery-governance-toolchain-repository-enforcement.md) — 005-A implementation precedence, change/dependency/toolchain governance and repository enforcement.
- [Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md) — 005-B V0-V11 verification, AF-01 through AF-20 and Q0-Q4 quality gates.
- [Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) — 005-C future package/test topology, Python/toolchain baseline, import direction and optional-dependency isolation.
- [Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan](public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md) — 005-D future public reference/handle model, identity/version primitives, SQL control persistence, CAS/transactions/outbox and migration contract.
- [Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan](spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md) — 005-E future Spark selector/access, exact source-state, manifest/candidate/sealed-snapshot and output-promotion plan.
- [Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan](strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md) — 005-F future binding/SPI/discovery/runtime invocation and Learned-State representation/codec plan.
- [Phase 005 navigator](../phases/005/index.md) — current planning sequence.

## Authority relationship

```text
design / cross-cutting authority
        ↓
concepts + synchronizations
        ↓
experience contracts
        ↓
architecture contracts
        ↓
implementation planning authority
        ↓
future source code + deployment configuration
        ↓
runtime/platform realization
```

Code and configuration, once implementation is explicitly authorized in a later phase, are executable realizations of accepted authority. They do not acquire permission to contradict upstream contracts because a dependency/platform makes another implementation easier.

## Progressive disclosure for implementers and agents

For a material planning or later implementation task, begin with:

1. [`docs/index.md`](../index.md);
2. [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md);
3. this index and the relevant implementation-plan authority;
4. [005-B verification authority](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
5. [005-C package/source authority](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md);
6. [005-D control-plane authority](public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md) whenever durable identity, public handles, canonical state, persistence, transactions, historical resolution, or migration are involved;
7. [005-E Spark/data boundary plan](spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md) whenever Spark selectors, exact source state, manifests, candidates, sealed snapshots, output representations or Generation promotion are involved;
8. [005-F runtime/SPI/Learned-State plan](strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md) whenever executable bindings, extension discovery, runtime invocation, Learned-State physical representation/loading or Evaluation-method runtime are involved;
9. only the detailed architecture/concept/experience documents directly linked by the active slice;
10. ADRs only when rationale/supersession history is needed.

Do not load the whole design corpus by default.

## Completed implementation-planning authority

### 005-A — Implementation governance

Established implementation precedence/conflict escalation, change classification, delivery-slice traceability, completion-evidence requirements, toolchain/dependency governance, migration discipline, repository agent instructions and PR review enforcement.

Phase record: [005-A](../phases/005/005-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md).

### 005-B — Verification architecture

Established V0-V11 logical verification layers, AF-01 through AF-20 architecture-fitness identifiers, conformance suites, synthetic fixture classes, deterministic/statistical/failure/security/platform verification, no-network portable-core testing and Q0-Q4 gates.

Phase record: [005-B](../phases/005/005-B-verification-strategy-test-harness-architecture-fitness-evidence-fixtures-quality-gates.md).

### 005-C — Source/package topology and dependency enforcement

Established one future `syngan` distribution/import package using `src/` layout, Python >=3.11, the `foundation/domain/ports/application/api/adapters/bootstrap` dependency direction, uv/Hatchling/pytest/Hypothesis/pytest-socket/Ruff/mypy/Import Linter/GitHub Actions toolchain, optional runtime/platform isolation, test topology and stable Q0-Q4 developer commands.

No package scaffold or production code was created by 005-C.

Phase record: [005-C](../phases/005/005-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md).

### 005-D — Public/control-plane identity, persistence and migration

Established the future shared durable control-plane substrate for all later slices:

- `AuthorityId`, UUIDv4 `ResourceId`, typed `ResourceRef`, scoped `RevisionNumber`/`RevisionRef`, `SnapshotId`, `StateVersion` and `SchemaVersion` as distinct axes;
- frozen standard-library value/domain/public types rather than ORM objects as canonical resources;
- planned `LearningSpec`, `GenerationSpec`, `EvaluationSpec`, typed handles/views and `SynGANClient` facade roles;
- typed historical resolution including absent/unavailable/unknown/invalid/withheld distinctions;
- explicit versioned JSON codecs and no pickle for canonical control/wire state;
- owner-specific persistence ports rather than a universal MetadataStore/CRUD registry;
- SQLAlchemy Core 2.x + Alembic 1.x planned built-in SQL adapter, PostgreSQL reference production backend, SQLite local/test backend and Psycopg 3 driver family;
- optional SQL/PostgreSQL persistence capability isolation from base `syngan`;
- expected-version CAS, bounded transactions/locks, operation-scoped idempotency support and transactional outbox/durable intent;
- migration policy preserving immutable history;
- V1/V2/V4 and AF-03/05/06/16/17 verification mapping.

No SQL schema, migration or persistence implementation was created by 005-D.

Phase record: [005-D](../phases/005/005-D-public-resource-api-control-plane-identity-state-persistence-transactions-migration-implementation.md).

### 005-E — Spark data boundary, manifests and promotion

Established the future distributed-data implementation plan:

- optional `spark` capability isolation from base `syngan`;
- Spark DataFrame/table/path/query selectors remain access instructions rather than durable identity;
- exact committed source state uses 005-D `ResourceRef`-based `SourceStateRef` values;
- arbitrary DataFrame/query/mutable-locator inputs default to distributed snapshot preparation before commitment unless an adapter proves an exact stable native read binding;
- bounded manifest roots with distributed/provider-native component indexes;
- portable manifested-Parquet profile as the first generic file representation plan;
- candidate materialization, sealed data snapshot and logical Generation output remain distinct;
- exact sealed snapshot is the subject for required completion Evaluation;
- future write/seal APIs reserve the writer-fence seam owned by 005-G;
- Generation promotion reuses 005-D CAS/transactions/idempotency/outbox and may be metadata-only;
- V5 and AF-03/04/08/13/17 plus future AF-07 integration are mapped.

No PySpark package, Spark adapter, manifest, migration, test or storage materialization was created by 005-E.

Phase record: [005-E](../phases/005/005-E-spark-data-boundary-source-output-references-manifest-materialization-promotion-implementation-plan.md).

### 005-F — Runtime extension, SPI and Learned-State planning

Established the future runtime implementation plan:

- stable revisioned Strategy/Evaluation-method implementation bindings separate from semantic authority;
- explicit `RuntimeSpiVersion` separate from binding/package/codec/schema versions;
- standard-library structural Protocols with separate Learning, Generation and Evaluation adapter/result contracts;
- explicit deployment composition plus optional lazy Python entry-point discovery through `syngan.runtime_extensions`;
- discovery does not authorize/select/trust code, and no global mutable registry or runtime auto-install/download path is accepted;
- immutable Attempt-scoped activity invocation snapshots using exact commitment, binding, data/state and dependency identities;
- narrow runtime port bundles rather than arbitrary canonical repositories/clients;
- Learned-State candidate and representation resources with explicit state-codec identity/version and distributed component support;
- no universal model/state byte format and no universal driver-local Learned-State deserialization;
- direct Generation without fabricated Learning/Learned State;
- optional `spark`/`torch` runtime families with launcher choice deferred to 005-G/005-J;
- V6 plus AF-02/04/09/12/13/14/20 conformance obligations.

No extension provider, runtime adapter, entry point, StateCodec, PyTorch/Spark runtime implementation or launcher was created by 005-F.

Phase record: [005-F](../phases/005/005-F-strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-implementation-plan.md).

## Current state

**Phase 005 — Implementation Planning & Delivery Decomposition is current and remains planning-only.**

Next:

**005-G — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan**.

005-G must now bind 004-F's at-least-once/fenced operational model to 005-D control persistence, 005-E candidate-writer fence seams and 005-F immutable Attempt invocation/checkpoint/cancellation-facing runtime ports—without beginning production implementation.
