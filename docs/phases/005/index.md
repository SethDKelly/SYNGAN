---
type: Phase Index
title: Phase 005 — Implementation Planning & Delivery Decomposition
status: active
---

# Phase 005 — Implementation Planning & Delivery Decomposition

Phase 005 translates the accepted Phase 004 architecture into dependency-safe implementation boundaries, source/package topology, implementation slices, verification obligations, migration/deployment sequencing, and acceptance evidence without reopening upstream semantic authority for convenience.

## Entry authority

Implementation planning is downstream of:

- [Design Authority](../../authority/index.md);
- [Accepted Concepts](../../concepts/index.md);
- [Accepted Synchronizations](../../synchronizations/index.md);
- [Phase 003 Consolidated Experience Contract](../../experience/phase-003-consolidated-experience-contract.md);
- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [Implementation Planning & Delivery Authority](../../implementation/index.md);
- detailed architecture authorities under [`docs/architecture/`](../../architecture/index.md);
- active architecture rationale under [`docs/decisions/`](../../decisions/index.md).

## Groups

| Group | Scope | Status |
|---|---|---|
| **005-A** | [**Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement**](005-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md) | **complete** |
| **005-B** | [**Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**](005-B-verification-strategy-test-harness-architecture-fitness-evidence-fixtures-quality-gates.md) | **complete** |
| **005-C** | [**Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement**](005-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) | **complete** |
| **005-D** | [**Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan**](005-D-public-resource-api-control-plane-identity-state-persistence-transactions-migration-implementation.md) | **complete** |
| **005-E** | **Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan** | **next** |
| 005-F | Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan | planned |
| 005-G | Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan | planned |
| 005-H | Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan | planned |
| 005-I | Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan | planned |
| 005-J | Deployment/Platform Adapters, Observability, Compatibility, Scale & Performance Implementation Plan | planned |
| 005-K | Cross-Slice Integration, Delivery Sequencing, Backlog Closure & Implementation-Readiness Exit | planned |

## Completed implementation-planning refinement

### 005-A — implementation authority and delivery governance

Established [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](../../implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md): implementation precedence/conflict escalation, change classification, dependency/toolchain/migration governance, agent/PR discipline and acceptance-evidence requirements.

### 005-B — verification strategy, fitness functions and quality gates

Established [Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates](../../implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md): V0-V11 verification layers, AF-01 through AF-20 architecture-fitness properties, conformance suites, synthetic fixture policy, failure/security/offline/statistical/platform verification and Q0-Q4 gates.

### 005-C — source topology, package boundaries and dependency enforcement

Established [Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](../../implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md): one `syngan` package using `src/`, Python >=3.11, inward `foundation/domain/ports/application/api/adapters/bootstrap` dependency direction, concrete foundational Python/build/test/static-analysis toolchain, optional dependency isolation, test topology and stable verification command/CI architecture.

### 005-D — public resource/control-plane identity, persistence and migration

Established [Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan](../../implementation/public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md).

Key accepted rules include:

- one durable identity/version model for later slices: AuthorityId, UUIDv4 ResourceId, typed ResourceRef, family-scoped RevisionNumber/RevisionRef, SnapshotId, StateVersion and SchemaVersion;
- immutable standard-library domain/public values, owner-specific lifecycle states and explicit versioned JSON codecs;
- concrete Learning/Generation/Evaluation specs, typed activity/result handles/views and a non-authoritative `SynGANClient` facade;
- typed exact historical resolution preserving absent/unavailable/unknown/invalid/withheld distinctions;
- owner-meaningful persistence ports rather than one generic metadata/CRUD owner;
- SQLAlchemy Core 2.x + Alembic 1.x, PostgreSQL reference production backend, SQLite local/test backend and Psycopg 3 driver family;
- optional SQL/PostgreSQL dependency isolation from the base package;
- technical resource-identity anchor plus owner-specific revision/commitment/current-state records, transition journal, tombstones and derived indexes;
- expected-version CAS, bounded relational transactions/locks, operation-scoped idempotency support and transactional outbox/durable intent;
- migration/autogenerate/offline-SQL/expand-migrate-contract policy preserving immutable historical semantics;
- V1/V2/V4 and AF-03/05/06/16/17 verification mapping;
- dependency-safe D1-D8 coding order from foundation IDs through SQL/PostgreSQL/migrations/Q1 acceptance.

005-D deliberately does not implement Spark materialization, runtime adapters, Attempt recovery/fencing, Evidence/Provenance, security or platform integration.

## Why the remaining order is dependency-safe

### 005-E — distributed data boundary next

005-E can now implement-plan:

- source selectors versus exact source-state references using 005-D ResourceRef/history semantics;
- Spark DataFrame resolution without making DataFrame identity canonical;
- distributed source snapshots/fingerprints/manifests;
- candidate materialization IDs and sealed candidate snapshot/manifest structures;
- Spark/table/file/object-store adapter boundaries;
- exact candidate subject binding for Evaluation;
- Generation output control identity/promotion using 005-D CAS/transaction/outbox mechanisms;
- distributed no-full-driver-collection verification under V5/AF-04/08/13/17.

### 005-F through 005-J — downstream slices

Runtime extension, Execution/recovery, Evidence/history, security, and platform/deployment planning then consume the shared control/data contracts rather than inventing parallel identity/state/persistence conventions.

### 005-K — integration and readiness exit

The final group verifies all slice plans compose into one dependency-safe implementation sequence without circular dependencies, hidden prerequisites, conflicting migrations or unowned acceptance criteria.

## Phase 005 guardrails

Phase 005 MUST NOT:

- redefine accepted concept meaning or ownership;
- weaken Phase 003 experience contracts for API convenience;
- weaken the Phase 004 architecture contract to fit a preferred library/platform;
- reverse the 005-C inward package dependency direction;
- invent parallel ResourceId/StateVersion/schema-version conventions downstream of 005-D;
- turn foundation or persistence into a generic utilities/config/metadata/context/result owner;
- place Spark/PyTorch/Databricks/cloud/remote dependencies into base core merely for one adapter;
- make raw DataFrame/model/platform objects canonical identity;
- design enterprise-scale workflows around mandatory full driver-local materialization;
- introduce hidden package/model downloads, remote fallback, telemetry or egress;
- equate scheduler retry/exactly-once claims with SYNGAN semantic authority;
- skip fencing, idempotency, exact historical binding, Evidence strength, Provenance, authorization or required architecture-fitness checks;
- allow derived indexes/telemetry/security audit to become canonical semantic state;
- treat snapshot refresh, platform success, line coverage or retry-until-green as sufficient correctness evidence;
- claim strict OKF 0.2 normalization is complete unless separately verified against external authority.

## Phase 005 exit target

Each planned implementation slice must identify:

```text
upstream authority
architecture mapping
source/module ownership
interface/persistence representation
implementation tasks and dependency order
verification/fitness tests
migration/deployment consequences
acceptance evidence
```

## Current next phase

**005-E — Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan**
