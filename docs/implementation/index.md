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
- [Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan](public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md) — 005-D durable reference/state/persistence/transaction/migration plan.
- [Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan](spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md) — 005-E exact distributed source/candidate/snapshot/output plan.
- [Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan](strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md) — 005-F binding/SPI/runtime/Learned-State plan.
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-plan.md) — 005-G Execution/recovery/fencing plan.
- [Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan](evaluation-evidence-provenance-historical-query-reproducibility-plan.md) — 005-H Evidence/history/reproducibility plan.
- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan](dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security-plan.md) — 005-I dependency/security/offline/disclosure plan.
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

Code/configuration, once implementation is explicitly authorized in a later phase, are executable realizations of accepted authority. They do not gain permission to contradict upstream contracts because a dependency/platform makes another implementation easier.

## Progressive disclosure for implementers and agents

For a material planning or later implementation task, begin with:

1. [`docs/index.md`](../index.md);
2. [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md);
3. this index and the relevant implementation-plan authority;
4. [005-B verification authority](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
5. [005-C package/source authority](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md);
6. [005-D control-plane authority](public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md) for durable identity/state/persistence/migration;
7. [005-E data plan](spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md) for Spark/data refs/manifests/candidates/output promotion;
8. [005-F runtime plan](strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md) for executable bindings/runtime invocation/Learned-State representation;
9. [005-G execution plan](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-plan.md) for Attempt/fencing/recovery/checkpoints/cancellation;
10. [005-H history plan](evaluation-evidence-provenance-historical-query-reproducibility-plan.md) for Evidence/Provenance/query/reproducibility;
11. [005-I security plan](dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security-plan.md) for dependency resolution, authorization, runtime capabilities, secrets, offline/no-egress, disclosure, audit and tenant isolation;
12. only the detailed architecture/concept/experience documents directly linked by the active slice;
13. ADRs only when rationale/supersession history is needed.

Do not load the whole design corpus by default.

## Completed implementation-planning authority

### 005-A through 005-C — governance, verification and package/toolchain topology

Established implementation precedence/governance; V0-V11, AF-01 through AF-20 and Q0-Q4; and one future `src/syngan` package with inward dependency direction, optional adapter/runtime isolation and a concrete foundational toolchain plan.

No production scaffold, test suite or CI implementation was created.

### 005-D — public/control-plane identity, persistence and migration

Established the shared ResourceRef/revision/SnapshotId/StateVersion/SchemaVersion substrate, public handles/views, typed historical resolution, owner-specific persistence ports, SQLAlchemy Core/Alembic/PostgreSQL/SQLite/Psycopg plan, CAS/transactions/idempotency/outbox and migration rules preserving immutable history.

No SQL schema/migration or persistence implementation was created.

### 005-E — distributed data boundary

Established SourceStateRef exact binding, distributed snapshot preparation, bounded manifest roots, portable manifested-Parquet profile, candidate/sealed-snapshot/output separation, writer-fence seam and metadata-only idempotent Generation promotion.

No Spark/storage implementation was created.

### 005-F — runtime extension and Learned-State

Established revisioned Strategy/Evaluation-method implementation bindings, RuntimeSpiVersion, Protocol-based activity-specific adapters, explicit extension composition, immutable Attempt invocation, narrow runtime ports, Learned-State candidate/representation/codec separation, distributed loading, direct Generation and optional Spark/PyTorch runtime families.

No runtime implementation was created.

### 005-G — Execution, recovery, fencing and cancellation

Established one stable Execution with many Attempts, monotonic AttemptEpoch, observed-state versus mutation-authority separation, WriterFence/cancellation generation, isolation-first stale-writer containment, launch reconciliation, immutable checkpoints/resume qualification, scoped idempotency, recovery modes, cancellation/completion linearization and operational-completion handoff.

No execution/scheduler/checkpoint implementation was created.

### 005-H — Evidence, Provenance, history and reproducibility

Established owner-side idempotent Evidence establishment, immutable Evidence finding versus applicability state, exact Generation completion basis, typed relational canonical Provenance, append/supersede correction, bounded explain/compare/history views, non-authoritative projections and derived reproducibility support/feasibility assessment.

No Evidence/Provenance/query implementation was created.

### 005-I — dependency resolution, offline/no-egress and enterprise security

Established the future enterprise-security/dependency contract:

- exact dependency requirements/resolutions remain separate from mutable locators;
- availability, identity, integrity/authenticity, trust/approval, compatibility and current authorization remain inspectable separately;
- explicit provisioning/acquisition remains outside committed runtime and never implies trust/authorization;
- no hidden runtime download/install/public-registry lookup/remote fallback/telemetry;
- supported core workflows preserve an offline/no-egress profile after approved local/private provisioning;
- network connectivity, destination, egress category, security domain and authorization remain separate;
- EgressPlan declares requirements but does not authorize transfer;
- action-oriented AuthorizationRequest/Decision replaces global `can_access` state;
- sensitive use/retry/resume/export/history operations re-authorize under current policy;
- Attempt runtime capabilities are bounded by semantic requirement ∩ current authorization ∩ deployment capability;
- handles remain identifiers rather than credentials;
- SecretRef is non-secret and bearer credentials remain ephemeral/non-canonical;
- extension loading and unsafe Learned-State deserialization participate in trust/authorization;
- source/Learned-State/candidate/output/diagnostic permissions remain distinct;
- canonical history and derived indexes/counts/reverse traversal/reproducibility reasons all enforce disclosure policy;
- redaction/withholding is view-time and preserves truthful absence/unknown/unavailable/withheld distinctions;
- revocation and 005-G fencing remain complementary;
- security audit remains separate from Provenance and telemetry;
- tenant/security-domain isolation applies across control/data/history/cache/runtime boundaries;
- V9 and AF-02/11/12/14/15/16/17/18 obligations are mapped.

No authorization code, dependency resolver, secret manager integration, network enforcement, security schema/migration, test suite or platform security configuration was created.

Phase record: [005-I](../phases/005/005-I-dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security-implementation-plan.md).

## Current state

**Phase 005 — Implementation Planning & Delivery Decomposition is current and remains planning-only.**

Next:

**005-J — Deployment/Platform Adapters, Observability, Compatibility, Scale & Performance Implementation Plan**.

005-J must now map all accepted portability, execution, storage, security, observability and scale contracts onto concrete deployment/platform capability profiles while preserving the platform-neutral semantic/control authority and without beginning production implementation.
