---
type: Phase Index
title: Phase 005 — Implementation Planning & Delivery Decomposition
status: active
---

# Phase 005 — Implementation Planning & Delivery Decomposition

Phase 005 translates the accepted Phase 004 architecture into dependency-safe **implementation plans**: source/module boundaries, technology choices, persisted/wire representations, verification obligations, migration/deployment sequencing, and acceptance evidence.

## Critical planning-only boundary

**Phase 005 does not authorize production implementation.**

Across 005-A through 005-K:

- production source code is not implemented;
- package scaffolds/tool configuration are not created merely because their future form is planned;
- database schemas/migrations are not executed;
- Spark/runtime/platform adapters are not built;
- CI/deployment infrastructure is not created;
- tests are not implemented as production verification suites.

Where a Phase 005 document says `implementation sequence`, `package path`, `class`, `port`, `adapter`, `table`, `migration`, or `quality gate`, it describes a **future implementation contract/sequence** unless a later phase explicitly authorizes coding.

## Entry authority

Implementation planning is downstream of:

- [Design Authority](../../authority/index.md);
- [Accepted Concepts](../../concepts/index.md);
- [Accepted Synchronizations](../../synchronizations/index.md);
- [Phase 003 Consolidated Experience Contract](../../experience/phase-003-consolidated-experience-contract.md);
- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [Implementation Planning & Delivery Authority](../../implementation/index.md);
- relevant detailed architecture under [`docs/architecture/`](../../architecture/index.md);
- ADR rationale under [`docs/decisions/`](../../decisions/index.md) only when needed.

## Implementation-planning rule

Every material future implementation slice SHOULD remain traceable through:

```text
concept / experience invariant
        ↓
architecture authority
        ↓
implementation plan
        ↓
future module / port / adapter / persisted representation
        ↓
future implementation slice
        ↓
verification / architecture fitness test
        ↓
acceptance evidence
```

Planning MUST NOT begin with a preferred framework/package tree and then reinterpret semantic ownership to fit it.

## Groups

| Group | Scope | Status |
|---|---|---|
| **005-A** | [**Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement**](005-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md) | **complete** |
| **005-B** | [**Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**](005-B-verification-strategy-test-harness-architecture-fitness-evidence-fixtures-quality-gates.md) | **complete** |
| **005-C** | [**Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement**](005-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md) | **complete** |
| **005-D** | [**Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan**](005-D-public-resource-api-control-plane-identity-state-persistence-transactions-migration-implementation.md) | **complete** |
| **005-E** | [**Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan**](005-E-spark-data-boundary-source-output-references-manifest-materialization-promotion-implementation-plan.md) | **complete** |
| **005-F** | [**Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan**](005-F-strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-implementation-plan.md) | **complete** |
| **005-G** | [**Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan**](005-G-execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-implementation-plan.md) | **complete** |
| **005-H** | **Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan** | **next** |
| 005-I | Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan | planned |
| 005-J | Deployment/Platform Adapters, Observability, Compatibility, Scale & Performance Implementation Plan | planned |
| 005-K | Cross-Slice Integration, Delivery Sequencing, Backlog Closure & Implementation-Readiness Exit | planned |

## Completed planning refinement

### 005-A — implementation governance

Established implementation precedence/conflict escalation, change classification, dependency/toolchain/migration governance, agent/PR discipline and acceptance-evidence requirements.

### 005-B — verification architecture

Established V0-V11 verification layers, AF-01 through AF-20 architecture-fitness properties, conformance suites, synthetic fixture policy, failure/security/offline/statistical/platform verification and Q0-Q4 gates.

### 005-C — source/package/toolchain plan

Established the future single `syngan` package using `src/`, Python >=3.11, inward `foundation/domain/ports/application/api/adapters/bootstrap` dependency direction, accepted foundational toolchain, optional-dependency isolation, test topology and stable Q0-Q4 command architecture.

No production scaffold or code was created.

### 005-D — public/control-plane plan

Established future durable identity/version/reference types, public specs/handles/views, typed historical resolution, SQLAlchemy Core/Alembic/PostgreSQL/SQLite/Psycopg persistence plan, CAS/transaction/outbox rules and migration strategy.

No database schema, migration or persistence code was created.

### 005-E — Spark data boundary plan

Established exact `SourceStateRef` binding, distributed snapshot preparation, bounded manifest roots, provider-native or manifested-Parquet physical profiles, candidate/sealed-snapshot/output separation, writer-fence seam and metadata-only idempotent promotion.

No Spark/runtime/storage implementation was created.

### 005-F — runtime extension and Learned-State plan

Established executable binding/SPI/version separation, Protocol-based activity-specific runtime adapters, explicit extension composition plus optional lazy entry-point discovery, immutable Attempt invocation, narrow runtime ports, Learned-State candidate/representation/codec boundaries, direct Generation and optional Spark/PyTorch runtime families.

No runtime plugin, entry point, state codec, PyTorch/Spark adapter, test or launcher was implemented.

### 005-G — Execution/recovery/fencing/cancellation plan

Established [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan](../../implementation/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-plan.md).

Key future implementation rules include:

- one stable Execution with many durable Attempts;
- monotonic AttemptEpoch values allocated under Execution CAS;
- Attempt observed state separate from mutation authority;
- WriterFence using exact Execution/Attempt/epoch plus cancellation-generation barrier;
- isolation-first stale-writer containment with provider fencing required for shared mutable targets;
- leases/heartbeats as liveness evidence only;
- immutable Attempt-owned runtime invocation;
- durable launch intent/correlation and reconciliation after ambiguous provider outcomes;
- operation-scoped idempotency keyed to exact target/request fingerprint;
- immutable checkpoint commitment and contextual resume qualification;
- explicit restart/resume/reconcile/cannot-continue recovery modes;
- current-authority verification before adopting immutable prior effects;
- Evaluation logical-work-unit deduplication or clean restart;
- durable unknown/indeterminate operational state and coordinator restart from persisted state;
- cancellation/completion linearization that revokes stale authority before physical termination is proven;
- operational completion kept separate from semantic completion;
- V7 and AF-04/06/07/08/09/18/19/20 obligations mapped.

No Execution classes, SQL tables, scheduler/checkpoint adapter, migration, test suite or runtime infrastructure was created.

## Why the remaining order is dependency-safe

### 005-H — Evidence/history planning next

005-H can now bind the 004-G Evidence/Provenance/history architecture to exact persisted facts from 005-D through 005-G:

- immutable commitments and result identities;
- exact sealed Evaluation subjects;
- runtime binding/invocation identities;
- Execution/Attempt/checkpoint/recovery history;
- operation/promotion basis and historical resolution.

It can therefore plan idempotent Evidence establishment, typed Provenance assertions, derived historical projections and qualified reproducibility assessments without inventing a competing metadata/history store.

### 005-I through 005-J

Enterprise security and deployment/platform planning follow after Evidence/history representation is fixed, so authorization/redaction can apply to canonical history and derived query paths consistently.

### 005-K

The final group audits that all plans compose into one implementation-ready program without circular dependencies, hidden prerequisites, conflicting migrations or unowned acceptance criteria.

## Phase 005 guardrails

Phase 005 MUST NOT:

- begin production implementation;
- redefine accepted concept meaning or ownership;
- weaken Phase 003 experience contracts for API convenience;
- weaken Phase 004 architecture to fit a preferred library/platform;
- reverse the 005-C inward dependency direction;
- invent parallel ResourceId/StateVersion/schema-version conventions downstream of 005-D;
- turn foundation/persistence/data/runtime/execution infrastructure into generic utilities/config/metadata/context/result owners;
- place Spark/PyTorch/Databricks/cloud/remote dependencies into base core merely for one adapter;
- make raw DataFrame/model/platform objects canonical identity;
- design enterprise workflows around mandatory full driver-local materialization;
- introduce hidden package/model downloads, remote fallback, telemetry or egress;
- replace fencing with lease expiry, scheduler retries or last-writer-wins;
- coerce unknown operational state into success/failure merely to retry;
- treat checkpoint existence as resume proof;
- skip exact historical binding, Evidence strength, Provenance, authorization or required architecture-fitness checks;
- allow derived indexes/telemetry/security audit to become canonical semantic state;
- claim strict OKF 0.2 normalization is complete unless separately verified.

## Phase 005 exit target

Phase 005 should leave an implementation-ready program where each planned slice has:

```text
upstream authority
architecture mapping
future source/module ownership
interface/persistence representation
future implementation tasks and dependency order
verification/fitness obligations
migration/deployment consequences
acceptance evidence requirements
```

Only after this planning program exits should a later phase authorize actual coding.

## Current next phase

**005-H — Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan**
