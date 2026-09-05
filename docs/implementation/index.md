---
type: Implementation Index
title: SYNGAN Implementation Planning & Delivery Authority
status: active
---

# SYNGAN Implementation Planning & Delivery Authority

## Purpose

This directory is the canonical home for implementation-planning and delivery-governance decisions that translate accepted architecture into source/module boundaries, toolchain expectations, persisted/wire representations, implementation slices, migrations, verification obligations, platform integration plans, delivery sequencing, and acceptance evidence.

Implementation authority is downstream of the [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md) and MUST NOT redefine accepted semantic, experience, or architecture authority for implementation convenience.

## Start here

- [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](implementation-authority-delivery-governance-toolchain-repository-enforcement.md) — 005-A implementation precedence, change/dependency/toolchain governance and repository enforcement.
- [Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md) — 005-B V0-V11 verification, AF-01 through AF-20 and Q0-Q4 quality gates.
- [Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) — 005-C package/test topology, Python/toolchain baseline, import direction and optional-dependency isolation.
- [Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan](public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md) — 005-D public reference/handle model, identity/version primitives, SQL control persistence, CAS/transactions/outbox and migration contract.
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
implementation authority / plans
        ↓
source code + deployment configuration
        ↓
runtime/platform realization
```

Code and configuration are executable realizations of accepted authority. They do not acquire permission to contradict upstream contracts because a dependency/platform makes another implementation easier.

## Progressive disclosure for implementers and agents

For a material task, begin with:

1. [`docs/index.md`](../index.md);
2. [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md);
3. this index and the relevant implementation authority;
4. [005-B verification authority](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
5. [005-C package/source authority](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md);
6. [005-D control-plane authority](public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md) whenever durable identity, public handles, canonical state, persistence, transactions, historical resolution, or migration are involved;
7. only the detailed architecture/concept/experience documents directly linked by the active slice;
8. ADRs only when rationale/supersession history is needed.

Do not load the whole design corpus by default.

## Completed implementation-planning authority

### 005-A — Implementation governance

Established implementation precedence/conflict escalation, change classification, delivery-slice traceability, completion-evidence requirements, toolchain/dependency governance, migration discipline, repository agent instructions and PR review enforcement.

Phase record: [005-A](../phases/005/005-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md).

### 005-B — Verification architecture

Established V0-V11 logical verification layers, AF-01 through AF-20 architecture-fitness identifiers, conformance suites, synthetic fixture classes, deterministic/statistical/failure/security/platform verification, no-network portable-core testing and Q0-Q4 gates.

Phase record: [005-B](../phases/005/005-B-verification-strategy-test-harness-architecture-fitness-evidence-fixtures-quality-gates.md).

### 005-C — Source/package topology and dependency enforcement

Established one `syngan` distribution/import package using `src/` layout, Python >=3.11, the `foundation/domain/ports/application/api/adapters/bootstrap` dependency direction, uv/Hatchling/pytest/Hypothesis/pytest-socket/Ruff/mypy/Import Linter/GitHub Actions toolchain, optional runtime/platform isolation, test topology and stable Q0-Q4 developer commands.

Phase record: [005-C](../phases/005/005-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md).

### 005-D — Public/control-plane identity, persistence and migration

Established one shared durable control-plane substrate for all later slices:

- `AuthorityId`, UUIDv4 `ResourceId`, typed `ResourceRef`, scoped `RevisionNumber`/`RevisionRef`, `SnapshotId`, `StateVersion` and `SchemaVersion` as distinct axes;
- frozen standard-library value/domain/public types rather than ORM objects as canonical resources;
- concrete `LearningSpec`, `GenerationSpec`, `EvaluationSpec`, typed handles/views and `SynGANClient` facade roles;
- typed historical resolution including absent/unavailable/unknown/invalid/withheld distinctions;
- explicit versioned JSON codecs and no pickle for canonical control/wire state;
- owner-specific persistence ports rather than a universal MetadataStore/CRUD registry;
- SQLAlchemy Core 2.x + Alembic 1.x built-in SQL adapter, PostgreSQL reference production backend, SQLite local/test backend and Psycopg 3 driver family;
- optional `sql`/`postgres` persistence capability isolation from base `syngan`;
- technical identity anchor plus owner-specific immutable revision/commitment records, mutable state projections, transition journal, tombstones and derived indexes;
- expected-version CAS, bounded transactions/locks, operation-scoped idempotency support and transactional outbox/durable intent;
- migration/autogenerate/offline-SQL/expand-migrate-contract policy preserving immutable history;
- V1/V2/V4 and AF-03/05/06/16/17 verification mapping.

Phase record: [005-D](../phases/005/005-D-public-resource-api-control-plane-identity-state-persistence-transactions-migration-implementation.md).

## Current state

**Phase 005 — Implementation Planning & Delivery Decomposition is current.**

Next:

**005-E — Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan**.

005-E must use 005-D's ResourceRef/history/state/transaction model for exact source-state binding and Generation output control authority while keeping distributed rows/components/manifests in the data plane and preserving the sealed-candidate/evaluation/promotion boundary.
