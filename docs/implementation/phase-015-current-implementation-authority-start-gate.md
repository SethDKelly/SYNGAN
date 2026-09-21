
---
type: Implementation Authority
title: Phase 015 Start Gate — Implementation Authority, Current-Baseline Reconciliation & Controlled-Delivery Decomposition
status: complete-current
---

# Phase 015 Start Gate — Implementation Authority, Current-Baseline Reconciliation & Controlled-Delivery Decomposition

## Purpose

Convert Phase 014-H readiness into bounded current implementation authority without letting historical plans, scaffold code, tests, or provider convenience redefine the completed design.

The gate satisfies:

~~~text
P15-01 current authority lock / precedence
P15-02 historical plan + scaffold/test disposition
P15-03 dependency-safe implementation decomposition
P15-04 verification/conformance map
P15-05 implementation change/reopen rules
P15-06 explicit first-slice authorization
~~~

This gate implements no domain behavior.

## P15-01 — authority lock

Implementation authority order is:

~~~text
current problem / actors / outcomes
 -> current concepts
 -> current dependence / application family
 -> current synchronization authority
 -> current mapping / disclosure authority
 -> Phase 013 architecture + cross-cutting contracts
 -> Phase 014 whole-design/readiness closure
 -> Phase 015 implementation authority
 -> explicitly authorized slice authority
 -> code / tests / tooling / provider behavior
~~~

Historical implementation documents and existing code/tests are downstream evidence only.

Current implementation must preserve the Phase 013 architecture invariants, especially singular semantic ownership, exact historical binding, non-regressing recovery, Generation-owned finality, Strategy/runtime separation, Execution/Attempt separation, Evaluation/Evidence/Provenance separation, no-egress closure, external release/use governance, provider-evidence qualification, and application-family optionality.

## P15-02 — historical baseline disposition

### RETAIN

The following choices are reauthorized as implementation/tooling decisions:

~~~text
one initial Python distribution / import package: syngan
src/ layout
py.typed
Python >= 3.11 current floor
pyproject.toml
uv
Hatchling
pytest
Hypothesis availability
Ruff
mypy
Import Linter availability
coverage diagnostics
portable-core external-network-denied test capability
optional/provider dependency isolation
root import avoids eager optional integration loading
general inward-dependency intent
~~~

### REVISE in 015-A

~~~text
exact seven top-level package set as a permanent invariant
exact historical Import Linter graph
exact-package-set fitness test
Phase 007 progression/lock tests
historical phase-state wording in tests/docs
socket-denial assumptions where legitimate local Spark/process communication applies
historical V0-V11 / AF-* wording when it conflicts with current authority
historical Wave 0..N sequencing
~~~

The governing rule is responsibility/authority preservation, not preservation of a historical file tree.

### DEFER to owning slices

~~~text
PostgreSQL
SQLAlchemy Core
Alembic
Psycopg
SQLite production role
concrete persistence schema
transaction/outbox mechanism
UUIDv4 encoding where opaque stable identity is sufficient
literal manifest implementation
checkpoint backend
Databricks-specific integration
OpenTelemetry
container/deployment topology
provider/table-format APIs
Strategy algorithms/model runtimes
benchmark envelopes
~~~

These remain candidates, not current mandates.

### REJECT / SUPERSEDE as current authority

~~~text
fifteen active synchronization assumptions
SYNC-08 as active cross-concept synchronization
SYNC-15 as synchronization-owned canonical state
obsolete Phase 007 subgroup locks
historical tests whose sole purpose is obsolete phase status
exact seven-package topology as permanent architecture
one module/service/table per concept or synchronization
provider/platform success as semantic completion
named provider/tool choices as product semantics
~~~

## Existing scaffold disposition

Retain the syngan package root, py.typed, current toolchain, empty base runtime dependency set until an authorized slice adds dependencies, portable-core network-denied capability, and general inward-dependency intent.

015-A must revise historical exact-package and phase-lock tests plus any Import Linter rules that overconstrain current architecture.

Current domain implementation remains NONE across concept behavior, persistence, distributed data, runtime, Execution/recovery, Evidence/history, and provider/security behavior.

## P15-03 — dependency-safe Phase 015 decomposition

### 015-A — Current Implementation Baseline, Repository/Toolchain & Scaffold Reconciliation
Reconcile current authority, tooling, source scaffold and historical fitness rules. Domain behavior remains absent.

### 015-B — Current Verification Harness, Architecture-Fitness & Evidence-Gate Foundation
Translate Phase 013/014 invariants and scenarios into current verification lanes without manufacturing domain behavior for tests.

### 015-C — Identity, References, Representation, Durable Owner-State & Control Persistence
Implement identity/reference/version foundations, durable owner-state boundaries, exact history, concurrency/transactions and migration-neutral persistence. Concrete persistence technology is selected here, not assumed from Phase 005.

### 015-D — Distributed Data-State, Structured Topology, Candidate/Seal & Generation Promotion
Implement exact physical subject boundaries, topology breadth, candidate/seal behavior and Generation-owned promotion without universal driver-local materialization.

### 015-E — Strategy/Method Binding, Dependency Closure, Learning/Learned-State & Generation Runtime
Implement Strategy-to-runtime binding, direct Generation, Learning/Learned State, distributed runtime closure and self-contained/no-egress-compatible prerequisites.

### 015-F — Execution/Attempt, Admission, Fencing, Idempotency, Checkpoint, Cancellation & Recovery
Implement current operational authority, recovery frontier, ambiguous-effect reconciliation, cancellation and adversarial recovery controls.

### 015-G — Evaluation, Evidence, Provenance, Historical Read Composition & Reproducibility
Implement Evaluation validity, durable Evidence, Evidence-gated Generation basis, typed Provenance, historical read composition and qualified reproducibility.

### 015-H — Authorization, Disclosure, Protected Existence, Secrets, Dependency Trust & No-Egress
Implement action authorization, protected existence, disclosure parity, secrets, dependency trust and no-egress enforcement.

### 015-I — Platform Capability, Portability, Observability, Scale/Performance & Support Qualification
Implement provider capability assessment, optional provider adapters, portability/fallbacks, observability and workload/profile qualification.

### 015-J — Cross-Slice Integration, Residual Risk Closure, Implementation Consolidation & Next-Stage Decision
Replay end-to-end scenarios, close residual readiness risks, verify support evidence and decide the next controlled boundary.

Dependency direction:

~~~text
015-A -> 015-B -> 015-C -> 015-D -> 015-E
                                  -> 015-F -> 015-G -> 015-H -> 015-I -> 015-J
~~~

This is delivery dependency guidance, not a universal runtime workflow.

## P15-04 — verification map

~~~text
C0 authority / static architecture                    015-A/B
C1 semantic / unit / state-machine                    015-C/E/G
C2 persistence / concurrency / migration              015-C
C3 distributed data / topology / physical closure     015-D
C4 runtime / dependency / no-egress                   015-E/H
C5 Execution / failure / recovery                     015-F
C6 Evaluation / Evidence / Provenance / history       015-G
C7 security / disclosure / protected existence        015-H
C8 provider / portability / scale                     015-I
C9 end-to-end adversarial replay                      015-J
~~~

Historical verification material may be reused only after normalization to current authority.

## Readiness-risk ownership

| Risk | Primary Phase 015 control |
|---|---|
| RR-01 historical implementation plans | 015-A / 015-J |
| RR-02 scaffold / fitness tests | 015-A / 015-B |
| RR-03 stale-writer / recovery proof | 015-F |
| RR-04 provider/history qualification | 015-I with 015-C/D |
| RR-05 no-egress distributed closure | 015-E / 015-H |
| RR-06 baseline capability / scale | 015-D / 015-E / 015-I |
| RR-07 Execution adversarial conformance | 015-F / 015-J |
| RR-08 disclosure / protected existence | 015-H / 015-J |

Every Phase 014 readiness risk has a downstream implementation control owner.

## P15-05 — change / reopen classification

~~~text
ICLASS-0 local non-contractual maintenance
ICLASS-1 bounded realization of accepted architecture
ICLASS-2 public/persisted/compatibility contract choice
ICLASS-3 architecture-affecting evidence -> stop and reopen smallest architecture authority
ICLASS-4 semantic/mapping/scope change -> stop and reopen smallest upstream design authority
~~~

Historical convenience, provider preference, cost, or existing code shape never justifies ICLASS-3/4 by itself.

Every slice must state before code: upstream authority, inclusions/exclusions, historical dispositions, dependencies, compatibility impact, verification lanes, readiness-risk controls, acceptance evidence, stop/reopen triggers, and next-slice eligibility.

## P15-06 — first-slice authorization

The start gate authorizes 015-A only.

~~~text
015-A  AUTHORIZED — NEXT ELIGIBLE

allowed:
  authority/documentation reconciliation
  repository/toolchain reconciliation
  scaffold/test retain-revise-remove decisions
  obsolete phase-state fitness removal/rewrite
  architecture-fitness normalization
  no-domain bootstrap corrections

not authorized:
  concept/domain behavior
  durable domain schemas/migrations
  distributed data implementation
  Strategy/Learning/Generation runtime behavior
  Execution/recovery behavior
  Evaluation/Evidence/Provenance behavior
  security/provider adapters
  scale/performance claims

015-B..015-J  NOT AUTHORIZED
~~~

## Start-gate decision

~~~text
Phase 015 Start Gate                 COMPLETE
P15-01                               COMPLETE
P15-02                               COMPLETE
P15-03                               COMPLETE
P15-04                               COMPLETE
P15-05                               COMPLETE
P15-06                               COMPLETE

Phase 015                            ACTIVE
IMPLEMENTATION READINESS            READY
IMPLEMENTATION START                NOT STARTED
IMPLEMENTATION NEXT                 015-A — AUTHORIZED
015-A                                NEXT ELIGIBLE / AUTHORIZED
015-B..015-J                         NOT AUTHORIZED
~~~

## Post-015-A consumption

015-A has consumed the start-gate authorization and completed its repository/toolchain/scaffold reconciliation.

~~~text
015-A                         COMPLETE
015-B                         NEXT ELIGIBLE / NOT AUTHORIZED
015-C..015-J                  NOT AUTHORIZED
IMPLEMENTATION START          NOT STARTED
~~~

Current completion authority: [015-A Current Implementation Baseline / Scaffold Reconciliation](phase-015-a-current-implementation-baseline-scaffold-reconciliation.md).

The original P15-06 block above remains the historical start-gate authorization decision.

## Start-gate post-015-A boundary

At 015-A completion, 015-B was next eligible but not authorized. That boundary has since been consumed by completed 015-B; see the post-015-B state below.


## Post-015-B consumption

015-B has completed the current verification-harness, architecture-fitness and evidence-gate foundation.

~~~text
015-A                         COMPLETE
015-B                         COMPLETE
015-C                         NEXT ELIGIBLE / NOT AUTHORIZED
015-D..015-J                  NOT AUTHORIZED
IMPLEMENTATION START          NOT STARTED
~~~

Current verification authority: [015-B Current Verification Harness / Architecture Fitness / Evidence Gates](phase-015-b-current-verification-harness-architecture-fitness-evidence-gates.md).

The repository next boundary is **015-C — Identity, References, Representation, Durable Owner-State & Control Persistence**, still gated pending explicit proceed.


## Post-015-C consumption

015-C has completed the first production-source implementation foundation.

~~~text
015-A                         COMPLETE
015-B                         COMPLETE
015-C                         COMPLETE
015-D                         NEXT ELIGIBLE / NOT AUTHORIZED
015-E..015-J                  NOT AUTHORIZED
IMPLEMENTATION START          STARTED
~~~

Current authority: [015-C Identity / References / Control Persistence](phase-015-c-identity-reference-control-persistence-authority.md).

The repository next boundary is **015-D — Distributed Data-State, Structured Topology, Candidate/Seal & Generation Promotion**, still gated pending explicit proceed.
