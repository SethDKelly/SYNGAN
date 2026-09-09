---
type: Phase Index
title: Phase 007 — Implementation Authority, Controlled Bootstrap & Evidence-Gated Delivery
status: planned
---

# Phase 007 — Implementation Authority, Controlled Bootstrap & Evidence-Gated Delivery

## Purpose

Translate the Phase 006 positive design-readiness decision into a **controlled, evidence-gated implementation entry** without turning readiness into unrestricted coding authority.

Phase 006 concluded:

```text
DESIGN COMPLETE ENOUGH FOR A LATER
EXPLICIT IMPLEMENTATION-AUTHORITY PHASE
```

Phase 007 is that proposed implementation-authority phase, but **this index only defines its logical subgroup structure. Phase 007 is not active and production implementation remains unauthorized until 007-A is explicitly entered and completes the authority lock.**

## Governing authority

When Phase 007 is entered, it will remain downstream of:

1. [Phase 006 Consolidated Design Readiness Contract](../../authority/phase-006-consolidated-design-readiness-contract.md);
2. current cross-cutting authority under `docs/authority/`;
3. accepted [Concepts](../../concepts/index.md) and [Synchronizations](../../synchronizations/index.md);
4. [Phase 006 Experience Contract](../../experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md);
5. [Phase 006 Architecture Reconciliation Contract](../../architecture/phase-006-architecture-reconciliation-contract.md);
6. [Phase 006 Implementation-Planning Reconciliation](../../implementation/phase-006-implementation-planning-reconciliation.md);
7. the Phase 005 detailed implementation plans where not refined by Phase 006;
8. active ADR rationale where material.

The implementation rule remains:

> **Implementation realizes accepted authority. Code, tests, platform behavior, convenience APIs, model libraries, or successful runtime experiments do not silently redefine upstream semantics.**

## Phase 007 scope boundary

Phase 007 is intentionally **not** the entire product implementation program.

Its job is to:

- establish actual implementation authority and change-control gates;
- create the reproducible repository/toolchain/verification substrate;
- establish source/package boundaries and architecture-fitness enforcement;
- implement the shared identity/control/data/runtime/recovery/security/history foundations in dependency-safe order;
- finish with one bounded self-contained single-table reference vertical slice that proves the architecture end-to-end;
- use evidence from that vertical slice to decide what broader delivery phase should follow.

The complete product baseline still requires supported self-contained Strategy paths for:

```text
single-table
time-series
multi-table shared-key
```

Phase 007 may establish semantic/representation support for all three, but it should **not** force time-series and multi-table synthesis algorithms into the bootstrap phase merely to claim breadth. Those capabilities remain required before complete-baseline product support is claimed and should be authorized in later delivery slices after the shared substrate proves sound.

## Authorization ladder

Phase 007 MUST use progressive implementation authority:

```text
Phase 006 readiness
        ↓
007-A authority lock
        ↓ authorizes only bounded bootstrap
007-B verification/toolchain bootstrap
        ↓ evidence gate
007-C source/package topology
        ↓ evidence gate
007-D identity/public contract foundation
        ↓ evidence gate
007-E control persistence/history foundation
        ↓ evidence gate
007-F distributed data/topology foundation
        ↓ evidence gate
007-G runtime/dependency/security closure foundation
        ↓ evidence gate
007-H Execution/recovery foundation
        ↓ evidence gate
007-I Evidence/history/reproducibility foundation
        ↓ evidence gate
007-J bounded vertical proof
        ↓
007-K exit/consolidation
```

No subgroup becomes authorized merely because the previous subgroup exists in this plan. Each transition requires the prior subgroup's acceptance evidence and an explicit proceed decision.

If implementation exposes a Class 3 architecture conflict or Class 4 semantic/experience conflict, ordinary implementation MUST stop at the smallest affected boundary and reopen the appropriate upstream authority rather than coding around it.

## Logical subgroups

| Group | Scope | Planned authority/result |
|---|---|---|
| **007-A** | **Implementation Authority Lock, Canonical Baseline, Change Control & Slice Authorization** | Governance-only entry. Locks authority/preference order, repository baseline, change classes, allowed file/change surface, evidence gates and explicit slice authorization. **No production feature code in 007-A.** |
| **007-B** | **Repository/Toolchain Bootstrap, Reproducible Environment & Verification Harness** | First executable bootstrap after 007-A approval. Establish repository-owned Python/build/test/static-analysis/dependency tooling, stable verification entry points, hermetic/offline defaults, evidence capture and initial V0/V1/V3 fitness framework. |
| **007-C** | **Source/Package Topology, Dependency Direction & Architecture-Fitness Enforcement** | Create the accepted `syngan` source/test topology, inward import boundaries, optional-integration isolation and executable architecture-fitness checks before substantive domain implementation expands. |
| **007-D** | **Identity, Revision, Serialization, Typed Public Resource/Handle & Programmatic-View Foundation** | Implement stable IDs/refs/revision/snapshot/state/schema axes, explicit serialization, typed handles/resolution and bounded actionability/disclosure/history view contracts without persistence/vendor coupling. |
| **007-E** | **Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline** | Implement the durable control substrate, owner-specific state/revisions/commitments, optimistic concurrency, append-preserved history, tombstone/unavailable semantics, transactional outbox and migration/conformance foundation. |
| **007-F** | **Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation** | Implement exact SourceState/data refs, Data Meaning structural-assertion addressing, logical multi-scope topology, hierarchical/composite manifest contracts, candidate/seal boundaries and one-logical-output promotion without hard-coded single-table assumptions. |
| **007-G** | **Strategy/Method Binding, Dependency Trust, Authorization, Secrets & Distributed Runtime Closure Foundation** | Implement semantic/runtime binding separation, activity-specific SPI contracts, exact multi-component implementation closure, dependency/trust/authorization/capability boundaries, secret brokering interfaces and worker-runtime closure. No hidden model/package acquisition. |
| **007-H** | **Execution/Attempt, Idempotency, Fencing, Non-Regressing Recovery, Checkpoint, Cancellation & Admission Foundation** | Implement one logical Execution across Attempts, writer fencing, fresh recovery-authority frontier, launch intent/reconciliation, checkpoints, retry/resume qualification, cancellation and operational admission/backpressure without semantic weakening. |
| **007-I** | **Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation** | Implement owner-established Evidence, typed canonical Provenance, exact promotion basis, bounded history/query projections, reconstructed/partial/unknown historical semantics, qualified reproducibility and disclosure-safe views. No universal privacy/release flag. |
| **007-J** | **Self-Contained Single-Table Reference Vertical Slice & Spark-Local End-to-End Proof** | Deliver one deliberately bounded end-to-end reference path proving Learning/Generation/Evaluation/Execution/Evidence/history across the real implementation substrate, including source-derived local text and Spark-local distributed-runtime closure. It must not claim enterprise scale or complete topology breadth. |
| **007-K** | **Phase 007 Consolidation, Architecture-Fitness Audit, Evidence Review & Next-Delivery Authorization Decision** | Audit code against authority, review verification/migration/security/offline/recovery evidence, confirm no design drift, classify remaining debt and decide whether a broader capability-delivery phase may be created. |

## 007-A — authority-lock requirements

007-A is the only valid entry point into production implementation.

It must explicitly establish at least:

- the exact canonical authority precedence to be used by humans/agents;
- repository/branch/commit baseline from which implementation begins;
- current accepted concept/synchronization/ADR counts;
- change classification and stop/reopen rules from 005-A, updated for Phase 006;
- which files/tooling/configuration 007-B is allowed to introduce;
- whether direct-to-main changes are permitted or review/PR workflow is required;
- dependency-intake rules and supported offline/no-egress development posture;
- definition of acceptance evidence for every subgroup;
- required architecture-fitness checks from 005-B plus Phase 006 AF-21..AF-28 obligations;
- explicit statement that authorization is incremental, not phase-wide blanket permission.

007-A SHOULD end by authorizing **007-B only**, unless it explicitly documents why a larger authorization window is necessary.

## 007-B — controlled executable bootstrap

007-B should implement the concrete toolchain already selected by Phase 005 planning unless 007-A identifies a compatibility reason to revise it through the appropriate authority path.

The planned baseline includes repository-owned equivalents of:

- `pyproject.toml` project/tool metadata;
- reproducible dependency resolution/lock state;
- build backend;
- test runner + property-testing support;
- outbound-network-denied portable-core test profile;
- lint/static/type/import-boundary tools;
- coverage/evidence reporting;
- stable `verify`/bootstrap commands shared by humans and CI;
- initial CI/review checks only to the extent explicitly authorized by 007-A.

007-B must not create substantive domain behavior merely to make the toolchain appear complete.

## 007-C — topology before behavior

007-C establishes the actual source/package boundaries before downstream code grows around accidental imports.

The future package remains one `syngan` distribution with dependency direction equivalent to:

```text
bootstrap
   ↓
adapters
   ↓
api / application / ports
   ↓
domain
   ↓
foundation
```

Concrete directories may reflect the 005-C plan, but the important gate is executable enforcement that:

- semantic/control code cannot depend on concrete platform adapters;
- optional Spark/PyTorch/Databricks/remote integrations do not leak into the portable core;
- no `Manager`/`Context`/`Session`/`Metadata`/generic `Result` god-owner is introduced;
- foundation remains intentionally small;
- tests mirror authority/contract boundaries rather than implementation convenience alone.

## 007-D / 007-E — separate value contracts from persistence

007-D deliberately precedes 007-E so stable identity/public contracts are tested without a database becoming their definition.

007-D should realize value/contract semantics such as:

```text
AuthorityId / ResourceId / ResourceKind / ResourceRef
RevisionNumber / RevisionRef
SnapshotId
StateVersion
SchemaVersion
HistoricalRef
bounded resolution/actionability/disclosure/history views
```

007-E then maps those contracts into durable persistence, concurrency and migration mechanisms.

A database primary key, table name, ORM object, transaction ID or timestamp must never become semantic identity merely because persistence is now available.

## 007-F — topology-neutral distributed data substrate

007-F must make the **representation substrate** capable of the complete topology model even though Phase 007-J will prove only a single-table synthesis algorithm.

This prevents the bootstrap implementation from encoding:

```text
one Generation == one table == one manifest == one physical object
```

The implementation must be capable of logical scopes and structural assertions sufficient for later time-series and multi-table slices, while preserving:

```text
structural meaning            → Data Meaning
prescriptive validity         → Constraint
requested topology/horizon    → Generation
method capability             → Strategy
finding                       → Evaluation / Evidence
```

## 007-G — runtime/security closure before material execution

007-G must establish the execution boundary before a real Strategy is permitted to process protected source data.

Required implementation properties include:

- exact semantic Strategy/method revision distinct from implementation binding;
- exact multi-component runtime/artifact closure;
- discovery separate from trust/authorization/selection;
- no runtime installation/model-hub/download fallback;
- current authorization and scoped capability issuance;
- secrets brokered at use and absent from canonical history/logs/fixtures;
- worker/executor readiness distinct from driver readiness;
- dynamic-worker closure support;
- large Learned State/model artifact resolution without universal driver broadcast.

## 007-H — recovery authority before uncontrolled retry

007-H must realize ADR-0005 and ADR-0009 together.

A future effective writer authority may need to bind equivalent state to:

```text
recovery-authority frontier
+ ExecutionRef
+ AttemptRef
+ AttemptEpoch
+ cancellation generation
```

where applicable.

Failure/recovery evidence must include at least:

- stale Attempt writer rejected;
- lost launch acknowledgement reconciled;
- duplicate physical work cannot create duplicate semantic authority;
- interrupted checkpoint not considered resumable until closed;
- cancellation race preserves actual outcome;
- regressive restore with surviving stale worker cannot resurrect authority;
- recovered immutable effects are adopted by fresh authority rather than reviving the old Attempt;
- resource scarcity queues/blocks rather than silently changing semantic scope.

## 007-I — findings/history before the vertical proof claims success

007-I precedes the reference vertical slice so 007-J cannot define success as “generated some rows.”

The implementation must have a real path for:

```text
Criterion
    ↓
Evaluation
    ↓
Evidence
    ↓
Generation completion basis
    ↓
Provenance / historical query / reproducibility
```

and preserve:

- runtime result != Evidence;
- favorable Evidence != privacy guarantee/release approval;
- exact Evaluation subject and claim-strength bounds;
- idempotent finding establishment;
- canonical Provenance separate from derived query projections;
- retained/reconstructed/partial/unavailable/unknown historical distinctions;
- security-filtered query/disclosure views.

## 007-J — intentionally bounded first vertical slice

007-J is the first subgroup intended to prove substantive synthetic generation end-to-end.

The recommended proof shape is a **simple self-contained Learning-based single-table Strategy** rather than CTGAN as the first architecture oracle. It should be deliberately understandable and deterministic/controlled enough to expose framework defects rather than bury them behind model complexity.

The exact algorithm is selected during 007-J under the accepted Strategy boundary, but the slice should exercise:

```text
source / Data Meaning / Constraints
        ↓
Learning
        ↓
Learned State
        ↓
Generation
        ↓
Execution / Attempts
        ↓
sealed candidate
        ↓
Evaluation / Evidence
        ↓
completed logical output
        ↓
Provenance / history / reproducibility view
```

The reference path should include representative numeric, categorical, datetime/identifier and **source-derived free-form-text** behavior without external network/model acquisition.

It should run through a Spark-local/distributed test profile sufficient to exercise executor/runtime closure, but:

- it does not certify enterprise-scale support;
- it does not certify Databricks support;
- it does not fulfill the time-series or multi-table Strategy requirement;
- it does not establish privacy/anonymization;
- it does not make the reference algorithm the package identity.

## 007-K — exit questions

007-K must answer at least:

1. Did production code remain traceable to current authority?
2. Did the toolchain/fitness gates catch architecture violations rather than merely formatting defects?
3. Did stable identity/public contracts survive persistence realization without database leakage?
4. Did distributed data/runtime boundaries avoid driver-local and hidden-acquisition assumptions?
5. Did ADR-0009 recovery authority survive executable failure scenarios?
6. Did programmatic actionability/security/history distinctions remain representable?
7. Did the first vertical slice prove semantic promotion/Evidence/history rather than only row generation?
8. Did implementation expose any genuine Class 3/4 design conflict requiring upstream reopening?
9. Is the codebase clean enough to authorize broader capability delivery without compounding bootstrap debt?
10. What exact scope should the next delivery phase authorize?

A positive 007-K result should authorize creation of a later capability-delivery phase; it should not silently expand Phase 007 into the entire product roadmap.

## Evidence-gate discipline

Every material subgroup after 007-A must produce evidence appropriate to its scope, including where relevant:

- upstream authority implemented;
- implementation files changed;
- dependency additions/removals and rationale;
- deterministic/unit/contract tests;
- architecture-fitness results;
- migration/compatibility evidence;
- offline/no-egress evidence;
- security/disclosure evidence;
- distributed/failure-injection evidence;
- scale/resource assumptions and explicit non-claims;
- intentionally deferred work/backlog references.

A subgroup is not complete because code compiles, a Spark job succeeds once, or tests were weakened until green.

## Current status

**Logical subgroup design: complete.**

**Phase 007 activation: not yet authorized.**

**Production implementation: still prohibited until 007-A is explicitly entered and completes the implementation-authority lock.**

## Proposed first subgroup

**007-A — Implementation Authority Lock, Canonical Baseline, Change Control & Slice Authorization**
