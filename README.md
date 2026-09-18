# SYNGAN

SYNGAN is a design-first synthetic-data generation framework intended for Spark-scale workloads.

SYNGAN is designed as a **deployable Python/Spark package** whose platform promise is:

> **Agnostic across compliant Spark-capable hosting and infrastructure platforms.**

It is not defined as a standalone UI application. Package, notebook and automated job/pipeline use are primary; CLI, reports, graphical presentation and standalone service/API exposure are optional adapters or integrations.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current governing architecture-reconciliation authority includes:

- [`Phase 013 Architecture Reconciliation Authority`](docs/authority/phase-013-architecture-reconciliation-authority.md)
- [`Phase 013`](docs/phases/013/index.md)
- [`013-D Distributed Data Reconciliation`](docs/architecture/phase-013-d-distributed-data-topology-manifest-candidate-promotion-reconciliation.md)
- [`013-E Runtime / Dependency / Security Reconciliation`](docs/architecture/phase-013-e-strategy-runtime-dependency-authorization-secrets-distribution-reconciliation.md)
- [`013-F Execution / Recovery / Admission Reconciliation`](docs/architecture/phase-013-f-execution-attempt-fencing-idempotency-checkpoint-cancellation-recovery-admission-reconciliation.md)
- [`Jackson Methodology Completion Matrix`](docs/authority/jackson-methodology-completion-matrix.md)
- [`Jackson Design Completion & Implementation Hold`](docs/authority/jackson-design-completion-implementation-hold.md)

## Status

```text
accepted concepts                    11
active synchronizations              13
Jackson concept design               COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013                            ACTIVE
013-A                                COMPLETE
013-B                                COMPLETE
013-C                                COMPLETE
013-D                                COMPLETE
013-E                                COMPLETE
013-F                                COMPLETE
013-G                                NEXT ELIGIBLE
R1 architecture reconciliation       DOWNSTREAM / IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Phase 013 results through 013-F

Representation, persistence/history/recovery, distributed-data/topology, runtime/dependency/security, and Execution/recovery/admission architecture have been reconciled against the completed concept design.

```text
013-B AMAT-2 / AMAT-3 / AR-9   0 / 0 / 0
013-C AMAT-2 / AMAT-3 / AR-9   0 / 0 / 0
013-D AMAT-2 / AMAT-3 / AR-9   0 / 0 / 0
013-E AMAT-2 / AMAT-3 / AR-9   0 / 0 / 0
013-F AMAT-2 / AMAT-3 / AR-9   0 / 0 / 0
upstream reopen                NONE
```

The current operational baseline preserves:

- one stable logical Execution distinct from subordinate Attempts/provider jobs;
- Attempt observed state separate from current framework mutation authority;
- non-regressing recovery-frontier authority above ordinary Attempt fencing after rollback;
- lease/heartbeat as liveness coordination rather than stale-writer proof;
- scoped idempotency plus fencing rather than exactly-once physical computation;
- immutable checkpoints distinct from current resume eligibility and semantic results;
- cancellation intent distinct from terminal operational outcome;
- late provider success unable to restore owner/result authority;
- admission as current operational eligibility distinct from semantic readiness, authorization, runtime closure, queue/capacity and mutation authority;
- resource pressure unable to silently weaken committed scope, validation, approximation, dependency or security semantics;
- bounded operational history at Spark scale.

Current synchronization authority remains:

```text
historical sync IDs   15
active syncs          13
SYNC-08               retired — Generation-local output lifecycle
SYNC-15               reclassified — Reproducibility contract
```

Remaining current-looking historical references in retained operational/scale documents are explicit 013-I corpus-cleanup obligations and do not control current semantics.

## Remaining Phase 013 sequence

```text
013-G  Evaluation / Evidence / Provenance / Historical Query /
       Reproducibility / Disclosure / External-Governance Boundary — NEXT
013-H  Deployment / Scale / Observability / Portability / Platform Integration
013-I  Cross-Architecture / ADR / Legacy / M6 / Residual Register
013-J  R1 Completion Decision / Phase 014 Handoff
```

## Implementation boundary

Phase 013 remains design-only.

```text
013    Post-Concept Representation & Architecture Reconciliation — ACTIVE
014    Whole-Design Consolidation & Implementation-Readiness Decision
015    Implementation Authority & Controlled Delivery — FUTURE ONLY
```

Only a positive Phase 014 may change implementation to **READY / NOT STARTED / NEXT**. A later explicit Phase 015 is still required to begin implementation.

## Current next boundary

**013-G — Evaluation, Evidence, Provenance, Historical Query, Reproducibility, Disclosure & External-Governance Boundary Reconciliation** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
