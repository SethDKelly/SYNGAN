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

The purpose is to make later coding dependency-safe and implementation-ready without letting code/framework convenience reopen Jackson-style conceptual, experience, or architecture decisions.

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
| **005-G** | **Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan** | **next** |
| 005-H | Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan | planned |
| 005-I | Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan | planned |
| 005-J | Deployment/Platform Adapters, Observability, Compatibility, Scale & Performance Implementation Plan | planned |
| 005-K | Cross-Slice Integration, Delivery Sequencing, Backlog Closure & Implementation-Readiness Exit | planned |

## Completed planning refinement

### 005-A — implementation governance

Established implementation precedence/conflict escalation, change classification, dependency/toolchain/migration governance, agent/PR discipline and acceptance-evidence requirements.

### 005-B — verification architecture

Established V0-V11 verification layers, AF-01 through AF-20 architecture-fitness properties, conformance suites, synthetic fixture policy, failure/security/offline/statistical/platform verification and Q0-Q4 gates.

### 005-C — source/package/toolchain plan

Established the future single `syngan` package using `src/`, Python >=3.11, inward `foundation/domain/ports/application/api/adapters/bootstrap` dependency direction, uv/Hatchling/pytest/Hypothesis/pytest-socket/Ruff/mypy/Import Linter/GitHub Actions toolchain plan, optional-dependency isolation, test topology and stable Q0-Q4 command architecture.

No production scaffold or code was created.

### 005-D — public/control-plane plan

Established future durable identity/version/reference types, public specs/handles/views, typed historical resolution, SQLAlchemy Core/Alembic/PostgreSQL/SQLite/Psycopg persistence plan, CAS/transaction/outbox rules and migration strategy.

No database schema, migration or persistence code was created.

### 005-E — Spark data boundary plan

Established [Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan](../../implementation/spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md): exact `SourceStateRef` binding, distributed snapshot preparation, bounded manifest roots, provider-native or manifested-Parquet physical profiles, candidate/sealed-snapshot/output separation, writer-fence seam and metadata-only idempotent promotion.

No Spark/runtime/storage implementation was created.

### 005-F — runtime extension and Learned-State plan

Established [Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan](../../implementation/strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md).

Key future implementation rules include:

- executable implementation binding remains separate from Strategy/method semantic authority;
- binding identity/revision, `RuntimeSpiVersion`, package/build version and state-codec version remain separate axes;
- standard-library `typing.Protocol` is the preferred structural SPI mechanism;
- Learning/Generation/Evaluation keep separate typed runtime adapter/result contracts;
- explicit deployment composition is primary, with optional lazy Python entry-point discovery through `syngan.runtime_extensions`;
- discovery does not authorize/select/trust an implementation and never auto-installs/downloads missing code/artifacts;
- no global mutable plugin registry becomes authority;
- every Attempt consumes an immutable activity-specific invocation snapshot;
- runtime ports expose bounded data/state/diagnostic/dependency/progress capabilities rather than arbitrary canonical repositories;
- Learning runtime produces candidate Learned-State representation, Generation runtime produces candidate data, Evaluation runtime produces method-result facts—none directly establish semantic results;
- Learned-State physical representation uses explicit codec/manifest identity and supports distributed loading without a universal full-driver deserialization requirement;
- direct Generation remains first-class;
- Spark/PyTorch remain optional capability families and concrete launchers are deferred to 005-G/005-J;
- V6 and AF-02/04/09/12/13/14/20 obligations are mapped.

No runtime plugin, entry point, state codec, PyTorch/Spark adapter, test or launcher was implemented.

## Why the remaining order is dependency-safe

### 005-G — Execution/recovery planning next

005-G can now bind the 004-F operational architecture to concrete future representations using:

- 005-D durable ResourceRef/StateVersion/CAS/transaction/outbox primitives;
- 005-E candidate-write/seal fence seam;
- 005-F immutable Attempt-scoped runtime invocation and checkpoint/cancellation-facing runtime ports.

It can therefore define stable Execution/Attempt records, monotonic Attempt epochs/fence tokens, checkpoint identity/eligibility, recovery modes, launch-intent reconciliation, idempotent commands and cancellation/completion linearization without changing runtime or semantic ownership.

### 005-H through 005-J

Evidence/history, enterprise security, and deployment/platform planning follow in architecture dependency order.

### 005-K

The final group audits that all plans compose into one implementation-ready program without circular dependencies, hidden prerequisites, conflicting migrations, or unowned acceptance criteria.

## Phase 005 guardrails

Phase 005 MUST NOT:

- begin production implementation;
- redefine accepted concept meaning or ownership;
- weaken Phase 003 experience contracts for API convenience;
- weaken Phase 004 architecture to fit a preferred library/platform;
- reverse the 005-C inward dependency direction;
- invent parallel ResourceId/StateVersion/schema-version conventions downstream of 005-D;
- turn foundation/persistence/data/runtime infrastructure into generic utilities/config/metadata/context/result owners;
- place Spark/PyTorch/Databricks/cloud/remote dependencies into base core merely for one adapter;
- make raw DataFrame/model/platform objects canonical identity;
- design enterprise workflows around mandatory full driver-local materialization;
- introduce hidden package/model downloads, remote fallback, telemetry or egress;
- skip fencing, idempotency, exact historical binding, Evidence strength, Provenance, authorization or required architecture-fitness checks;
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

**005-G — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan**
