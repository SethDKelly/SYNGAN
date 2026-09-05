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

[004-J — Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit](../004/004-J-cross-architecture-invariant-audit-decision-consolidation-phase-004-exit.md) is the formal Phase 004 handoff.

## Implementation-planning rule

Every material implementation slice SHOULD remain traceable through:

```text
concept / experience invariant
        ↓
architecture authority
        ↓
implementation authority / plan
        ↓
module / port / adapter / persisted representation
        ↓
implementation slice
        ↓
verification / architecture fitness test
        ↓
acceptance evidence
```

Implementation planning MUST NOT begin with a preferred framework/package tree and then reinterpret semantic ownership to fit it.

## Groups

| Group | Scope | Status |
|---|---|---|
| **005-A** | [**Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement**](005-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md) | **complete** |
| **005-B** | [**Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**](005-B-verification-strategy-test-harness-architecture-fitness-evidence-fixtures-quality-gates.md) | **complete** |
| **005-C** | **Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement** | **next** |
| 005-D | Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan | planned |
| 005-E | Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan | planned |
| 005-F | Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan | planned |
| 005-G | Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan | planned |
| 005-H | Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan | planned |
| 005-I | Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan | planned |
| 005-J | Deployment/Platform Adapters, Observability, Compatibility, Scale & Performance Implementation Plan | planned |
| 005-K | Cross-Slice Integration, Delivery Sequencing, Backlog Closure & Implementation-Readiness Exit | planned |

## Completed implementation-planning refinement

### 005-A — implementation authority and delivery governance

Established [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](../../implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md).

Key accepted rules include:

- implementation is downstream realization rather than permission to override architecture;
- existing code does not outrank canonical authority;
- material changes are classified from local maintenance through semantic/experience-affecting changes so conflicts escalate to the correct layer;
- delivery slices remain traceable from upstream authority through modules/ports/adapters to verification and acceptance evidence;
- build/test/development behavior must be repository-declared and reproducible rather than workstation-defined;
- direct dependencies require explicit purpose/classification and compatibility/offline/network/security consideration;
- runtime package/model acquisition and hidden fallback remain prohibited;
- optional integrations remain isolatable from the portable/offline core;
- persisted/public/SPI changes require compatibility/migration analysis on their actual version axis;
- humans and agents follow the same authority/change/evidence rules.

Immediate repository governance created:

- root [`AGENTS.md`](../../../AGENTS.md);
- [`.github/pull_request_template.md`](../../../.github/pull_request_template.md).

### 005-B — verification strategy, fitness functions and quality gates

Established [Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates](../../implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md).

Key accepted rules include:

- test oracles derive from accepted authority rather than current code/platform output;
- logical verification layers V0-V11 separate repository, deterministic, component, fitness, persistence, distributed, runtime, recovery, Evidence/history, security/offline, platform and scale/compatibility concerns;
- architecture-fitness catalog AF-01 through AF-20 gives stable identifiers to cross-cutting Phase 004 properties;
- core deterministic rules should remain hermetic and fast enough for continuous gating;
- production adapters inherit reusable common conformance suites rather than provider-specific weaker contracts;
- failure/recovery tests deliberately inject faults around durable mutation, provider submission, checkpoint closure, candidate seal, Evidence establishment and promotion;
- portable/core verification defaults to no outbound network and treats unexpected network access as failure;
- fixtures are synthetic/non-sensitive and split into micro, reproducibly generated medium, ephemeral scale and fault/control classes;
- golden snapshots are compatibility evidence, not self-authorizing truth;
- stochastic/statistical tests predeclare acceptance/confidence behavior and never use retry-until-green;
- Q0-Q4 distinguish local, PR, integration, scheduled and release/support certification gates by cadence/cost rather than semantic importance;
- flaky/quarantined tests and gate waivers remain explicit, owned and time-bounded;
- acceptance evidence records verification profiles, fitness results, fixture versions and material compatibility/security/scale context without confusing delivery evidence with the domain `Evidence` concept.

005-B deliberately leaves concrete test/build/static-analysis tools and physical source/test topology to 005-C.

## Why the remaining order is dependency-safe

### 005-C — source/package topology after governance and verification

005-C can now select:

- Python package/source/test topology;
- shared primitives and application/port/adapter boundaries;
- import/dependency rules;
- optional dependency/extras isolation;
- foundational concrete Python/build/test/static-analysis tooling;
- architecture fitness enforcement mechanism;
- stable Q0/Q1 developer/CI commands and entry points for Q2-Q4 profiles;
- fixture/conformance-suite physical organization;
- initial CI workflow/check mapping.

The topology must make V0-V11, AF-01 through AF-20, and Q0-Q4 enforceable rather than weaken them for package convenience.

### 005-D through 005-J — implementation slices follow architectural dependency order

The implementation plans then proceed from durable control/public foundations into distributed data, runtime extension, execution/recovery, Evidence/history, security, and deployment/platform integration.

Each slice identifies ownership, persisted/wire representation, interfaces, dependencies, tests/fixtures, migration/failure behavior, integration points, and explicit deferred work.

### 005-K — integration and readiness exit

The final group verifies that slice plans compose into one implementable delivery sequence without circular dependencies, hidden prerequisites, conflicting migrations, or unowned acceptance criteria.

## Phase 005 guardrails

Phase 005 MUST NOT:

- redefine accepted concept meaning or ownership;
- weaken Phase 003 experience contracts for API convenience;
- weaken the Phase 004 architecture contract to fit a preferred library/platform;
- make CTGAN, GAN, PyTorch, Spark ML, Databricks, a specific database, scheduler, graph store, IAM system, or observability vendor universal unless a later explicit implementation decision with accepted rationale requires it;
- collapse typed semantic/operational/security/history state into generic status/session/result/metadata objects;
- make raw DataFrame/model/platform objects canonical identity;
- design enterprise-scale workflows around mandatory full driver-local materialization;
- introduce hidden package/model downloads, remote fallback, telemetry, or egress;
- equate scheduler retry/exactly-once claims with SYNGAN semantic authority;
- treat implementation planning as permission to skip fencing, idempotency, exact historical binding, Evidence strength, Provenance, authorization, or required architecture-fitness checks;
- allow derived indexes/telemetry/security audit to become canonical semantic state;
- treat snapshot refresh, platform success, line coverage, or retry-until-green as sufficient correctness evidence;
- claim strict OKF 0.2 normalization is complete unless separately verified against external authority.

## Phase 005 exit target

Phase 005 should leave an implementation-ready program where each planned slice has:

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

The exit should be strong enough that subsequent coding phases can execute the plan without rediscovering architecture decisions or introducing agent-driven scope/authority drift.

## Current next phase

**005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement**
