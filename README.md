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
- [`013-A Reconciliation Authority / Corpus Inventory / Taxonomy`](docs/phases/013/013-A-reconciliation-authority-retained-corpus-inventory-precedence-reset-discrepancy-taxonomy.md)
- [`013-B Representation Phase Record`](docs/phases/013/013-B-representation-layering-public-contract-identity-revision-handle-view-reconciliation.md)
- [`013-B Representation Reconciliation Authority`](docs/architecture/phase-013-b-representation-layering-public-contract-identity-view-reconciliation.md)
- [`Representation & Architecture`](docs/architecture/index.md)
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
013-C                                NEXT ELIGIBLE
R1 architecture reconciliation       DOWNSTREAM / IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## 013-B result

The representation/layering/public-contract/identity/view architecture is retained with bounded clarification.

```text
AMAT-2 representation defects   0
AMAT-3 blockers                 0
AR-9 contradictions             0
upstream reopen                 NONE
```

Current representation rules preserve semantic ownership upstream of architecture, stable logical identity independent of provider/location identity, distinct revision/current-state/schema axes, owner-qualified handles/views, Execution ownership of operational cancellation/retry/recovery, optional surface semantics, owner-specific result establishment, and D0-D4 as presentation depth rather than technical tiers.

Historical `007-D` synchronization-count wording and old representation-precedence wording remain tracked for 013-I cleanup.

## Remaining Phase 013 sequence

```text
013-C  Control Persistence / Historical Reference / Transactions / Concurrency / Migration / Recovery State — NEXT
013-D  Distributed Data / Topology / Manifest / Candidate-Seal-Promotion
013-E  Strategy/Runtime / Dependency / Security / Offline-No-Egress
013-F  Execution / Attempt / Recovery / Fencing / Admission
013-G  Evaluation / Evidence / Provenance / History / Disclosure
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

**013-C — Control Persistence, Historical Reference, Transaction/Concurrency, Migration & Recovery-State Reconciliation** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
