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

Completion of this planning program does not automatically authorize coding. Phase 005-K must explicitly determine whether Jackson-style concept/synchronization/experience/architecture refinement is sufficiently complete or whether another design phase is required.

## Start here

- [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](implementation-authority-delivery-governance-toolchain-repository-enforcement.md) — 005-A implementation precedence, change/dependency/toolchain governance and repository enforcement.
- [Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md) — 005-B V0-V11 verification, AF-01 through AF-20 and Q0-Q4 quality gates.
- [Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) — 005-C future package/test topology, Python/toolchain baseline, import direction and optional-dependency isolation.
- [Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan](public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md) — 005-D future public reference/handle model, identity/version primitives, SQL control persistence, CAS/transactions/outbox and migration contract.
- [Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan](spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md) — 005-E future Spark selector/access, exact source-state, manifest/candidate/sealed-snapshot and output-promotion plan.
- [Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan](strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md) — 005-F future binding/SPI/discovery/runtime invocation and Learned-State representation/codec plan.
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-plan.md) — 005-G future Execution/Attempt epochs, writer fencing, launch reconciliation, checkpoint/recovery, cancellation and operational-completion plan.
- [Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan](evaluation-evidence-provenance-historical-query-reproducibility-plan.md) — 005-H future Evidence establishment, canonical Provenance, bounded history query and qualified reproducibility plan.
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
9. [005-G Execution/recovery plan](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-plan.md) whenever Attempt lifecycle, writer fencing, launch reconciliation, checkpoints, recovery, cancellation or operational completion are involved;
10. [005-H Evidence/history plan](evaluation-evidence-provenance-historical-query-reproducibility-plan.md) whenever Evidence establishment, Generation completion basis, Provenance, explain/compare/history queries or reproducibility assessment are involved;
11. only the detailed architecture/concept/experience documents directly linked by the active slice;
12. ADRs only when rationale/supersession history is needed.

Do not load the whole design corpus by default.

## Completed implementation-planning authority

### 005-A — Implementation governance

Established implementation precedence/conflict escalation, change classification, delivery-slice traceability, completion-evidence requirements, toolchain/dependency governance, migration discipline, repository agent instructions and PR review enforcement.

Phase record: [005-A](../phases/005/005-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md).

### 005-B — Verification architecture

Established V0-V11 logical verification layers, AF-01 through AF-20 architecture-fitness identifiers, conformance suites, synthetic fixture classes, deterministic/statistical/failure/security/platform verification, no-network portable-core testing and Q0-Q4 gates.

Phase record: [005-B](../phases/005/005-B-verification-strategy-test-harness-architecture-fitness-evidence-fixtures-quality-gates.md).

### 005-C — Source/package topology and dependency enforcement

Established one future `syngan` distribution/import package using `src/` layout, Python >=3.11, the `foundation/domain/ports/application/api/adapters/bootstrap` dependency direction, accepted foundational toolchain, optional runtime/platform isolation, test topology and stable Q0-Q4 developer commands.

No package scaffold or production code was created by 005-C.

Phase record: [005-C](../phases/005/005-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md).

### 005-D — Public/control-plane identity, persistence and migration

Established the future shared durable control-plane substrate: distinct AuthorityId/ResourceId/ResourceRef/revision/SnapshotId/StateVersion/SchemaVersion axes, frozen value/public types, typed historical resolution, owner-specific persistence ports, SQLAlchemy Core/Alembic/PostgreSQL/SQLite/Psycopg persistence plan, CAS/transactions/idempotency/outbox, and migration rules preserving immutable history.

No SQL schema, migration or persistence implementation was created by 005-D.

Phase record: [005-D](../phases/005/005-D-public-resource-api-control-plane-identity-state-persistence-transactions-migration-implementation.md).

### 005-E — Spark data boundary, manifests and promotion

Established the future exact-source and distributed-data plan: optional Spark isolation, SourceStateRef binding, snapshot preparation for mutable selectors, bounded manifests/distributed indexes, manifested-Parquet generic profile, candidate/sealed-snapshot/output separation, writer-fence seam, and metadata-only idempotent Generation promotion.

No PySpark package, Spark adapter, manifest, migration, test or storage materialization was created by 005-E.

Phase record: [005-E](../phases/005/005-E-spark-data-boundary-source-output-references-manifest-materialization-promotion-implementation-plan.md).

### 005-F — Runtime extension, SPI and Learned-State planning

Established revisioned Strategy/Evaluation-method implementation bindings, RuntimeSpiVersion, Protocol-based activity-specific adapters, explicit composition plus optional lazy entry-point discovery, immutable Attempt invocation, narrow runtime ports, Learned-State candidate/representation/codec separation, distributed loading, direct Generation and optional Spark/PyTorch runtime families.

No extension provider, runtime adapter, StateCodec, PyTorch/Spark runtime implementation or launcher was created by 005-F.

Phase record: [005-F](../phases/005/005-F-strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-implementation-plan.md).

### 005-G — Execution, recovery, fencing and cancellation planning

Established the future durable operational substrate:

- one stable Execution with many durable Attempts and positive monotonic AttemptEpoch values;
- observed Attempt/runtime state separated from current framework mutation authority;
- Execution current-authority projection plus WriterFence and cancellation-generation barrier;
- isolation-first fence enforcement at registration/adoption/seal/completion boundaries, with real provider fencing required for shared mutable targets;
- leases/heartbeats retained as liveness evidence rather than mutation authority;
- immutable Attempt-owned RuntimeInvocationRef;
- durable launch intent, provider correlation and reconciliation for ambiguous submission outcomes;
- operation-scoped idempotency using exact target/request fingerprint rather than one global key;
- immutable CheckpointRef commitment, resume qualification and explicit restart/resume/reconcile/cannot-continue modes;
- current-authority adoption of verified immutable prior effects without automatic acceptance of fenced late writes;
- Evaluation logical-work-unit deduplication/restart requirement for retry safety;
- durable unknown/indeterminate operational state and coordinator restart from persisted state;
- cancellation/completion linearization where cancellation revokes old writer/promotion authority before physical termination is proven;
- one authoritative operational-completion basis distinct from Learning/Generation/Evaluation semantic completion;
- V7 and AF-04/06/07/08/09/18/19/20 failure-injection obligations.

No Execution classes, SQL schema, migration, scheduler adapter, checkpoint implementation, test suite or runtime infrastructure was created by 005-G.

Phase record: [005-G](../phases/005/005-G-execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-implementation-plan.md).

### 005-H — Evidence, Provenance, history and reproducibility planning

Established the future Evidence/history substrate:

- Evidence remains owner-established semantic authority downstream of exact Evaluation validation, never a runtime result;
- one Evaluation may establish multiple stable Evidence resources using idempotent finding-slot identity;
- immutable Evidence finding content remains separate from StateVersion-guarded applicability/current-use state;
- claim support remains bounded by method, scope, achieved coverage, uncertainty and assumptions;
- diagnostic support remains exact distributed references rather than copied control payloads;
- Generation promotion retains one immutable exact Evidence completion basis;
- canonical Provenance is initially planned as typed indexed relational assertions in the existing bounded SQL control-store family;
- Provenance stores exact historical references/relationship meaning, not duplicated canonical resource payloads;
- assertion retry is idempotent and correction is append/supersede rather than destructive rewrite;
- same-store owner transitions and required Evidence/Provenance may share one transaction while external projections use outbox/reconciliation;
- history APIs return bounded/paginated typed provenance/explain/compare views and preserve canonical-vs-projection freshness distinctions;
- historical comparison never turns difference into causality/superiority without Evidence;
- ReproducibilityAssessment remains derived and reports strongest historically supportable class separately from current feasibility;
- history/query contracts reserve security-aware withheld/redacted behavior for 005-I;
- V8 plus AF-08/09/10/11/16/17/18/19 obligations are mapped.

No Evidence store, Provenance graph/table, query projection, reproducibility engine, migration, test suite or external lineage integration was created by 005-H.

Phase record: [005-H](../phases/005/005-H-evaluation-evidence-provenance-historical-query-reproducibility-implementation-plan.md).

## Current state

**Phase 005 — Implementation Planning & Delivery Decomposition is current and remains planning-only.**

Next:

**005-I — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan**.

005-I must now apply the accepted enterprise-security architecture to the exact resource/runtime/Execution/Evidence/Provenance/query surfaces defined in 005-D through 005-H without beginning production implementation.
