# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**Jackson concept design is complete for the current product scope. Phase 013 architecture reconciliation is ACTIVE; 013-A through 013-C are complete, and 013-D is next. Implementation remains held.**

Start with:

- `docs/index.md`
- `docs/problem/problem-purpose.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-013-architecture-reconciliation-authority.md`
- `docs/authority/operational-authority-continuity-regressive-recovery-contract.md`
- `docs/phases/013/index.md`
- `docs/phases/013/013-A-reconciliation-authority-retained-corpus-inventory-precedence-reset-discrepancy-taxonomy.md`
- `docs/phases/013/013-B-representation-layering-public-contract-identity-revision-handle-view-reconciliation.md`
- `docs/phases/013/013-C-control-persistence-historical-reference-transaction-concurrency-migration-recovery-state-reconciliation.md`
- `docs/architecture/phase-013-b-representation-layering-public-contract-identity-view-reconciliation.md`
- `docs/architecture/phase-013-c-control-persistence-history-concurrency-migration-recovery-reconciliation.md`
- `docs/architecture/index.md`

## Current state

```text
accepted concepts                    11
active synchronizations              13
Phase 012                            COMPLETE
A1-H2                                CURRENTLY CLOSED
Jackson concept design               COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013                            ACTIVE
013-A                                COMPLETE
013-B                                COMPLETE
013-C                                COMPLETE
013-D                                NEXT ELIGIBLE
R1 architecture reconciliation       DOWNSTREAM / IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Primary authority rule

> **Completed concept design and completed Phase 013 reconciliation decisions are upstream authority for unreconciled architecture. Retained architecture, code, tests and provider models may expose a genuine defect, but they may not redefine semantics merely to preserve historical choices.**

Only a demonstrated `AR-9` genuine upstream contradiction may justify `UPSTREAM-REOPEN`. Use the smallest-authority reopen rule and revalidate the material blast radius.

## Phase 013 finding discipline

Use `AR-0..AR-9`, `AMAT-0..AMAT-3`, and:

```text
RETAIN
CLARIFY
SUPERSEDE
CORRECT
DEFER
UPSTREAM-REOPEN
```

These are documentation/design classifications, not runtime enums/resources/issues.

## Reconciled representation invariants — 013-B

Preserve:

- architecture as representation of semantic authority, not a second semantic owner;
- logical layering without mandatory package/service/process/API-tier mapping;
- package/SDK, notebook and embedded automation as primary interaction roles;
- optional/integration surfaces remaining optional;
- stable logical identity distinct from locator/provider identity;
- separate logical identity, semantic revision/commitment, current state version/freshness and representation schema version;
- exact historical bindings alongside refreshable current views;
- handles/views as resolvers/projections rather than detached canonical entities;
- Execution ownership of retry/resume/reconcile/cancel operational state;
- owner-specific result establishment rather than a universal Result lifecycle;
- D0-D4 as semantic disclosure depth rather than architecture tiers;
- bounded/reference-first interaction for Spark-scale payloads.

## Reconciled persistence invariants — 013-C

Preserve:

- persistence makes owner-established authority durable but does not create semantic authority by storing physical state;
- shared store/transaction technology does not merge owner boundaries;
- cross-owner facts may co-commit atomically without transferring ownership;
- durable outbox/transition-intent state is technical coordination state, not `Synchronization.status` or target success;
- synchronization-owned canonical state remains **NONE**;
- CAS/state-version success means the protected observation was current at that boundary, not that the semantic action was legal/authorized/completed;
- restored state versions do not establish non-regressing write authority after rollback;
- exact historical references do not silently resolve to `latest`;
- reconstruction/projection rebuild claims only what retained owner evidence establishes;
- migration changes representation by default and does not rewrite semantic history;
- schema rollback does not reverse domain history;
- regressive restore requires a fresh recovery-authority frontier before ordinary writes resume;
- clone/fork copies do not inherit original authority scope automatically;
- control persistence stays bounded and does not absorb row-scale source/output data by default.

The active recovery contract now uses current Phase 009 semantics: historical `SYNC-15` is reserved/reclassified and is not active.

Historical `007-D/007-E` `15`-synchronization count wording remains a 013-I cleanup obligation.

## 013-D next scope

013-D reconciles distributed data boundary, structured topology, manifests, candidate/seal/promotion, and large Learned-State/diagnostic representation.

It must verify at least:

- Data Meaning owns structural/temporal interpretation while physical layout only represents it;
- no independent Dataset/Output/Relationship/Topology/Manifest/Artifact concept is smuggled into architecture;
- logical source/output identity remains distinct from DataFrame/table/path/provider identity;
- single-table, time-series and shared-key multi-table baseline remains representable without mandatory flattening;
- candidate physical material, sealed exact subject and Generation semantic completion remain distinct;
- manifest/seal integrity never proves Constraint satisfaction, Evidence strength, privacy, approval or semantic completion;
- whole-result completion works over all mandatory scopes/components;
- large Learned State and diagnostics remain distributable/referenceable without universal driver collection;
- persistence facts and durable bytes do not become result authority merely by survival.

## Durable quality rules

Decision-material disclosure:

> **Do not hide a qualifier whose omission could change the actor's immediate semantic decision or make current state appear stronger than its owner supports.**

Provider evidence:

> **Consume provider facts only at the evidentiary strength they actually establish.**

Future rediscovery:

> **New independent product-facing purpose/state/actions/lifecycle returns to concept discovery before architecture or implementation.**

## M6 / M8 carry-forward

Current synchronization authority is `15 historical IDs / 13 active synchronizations`; `SYNC-08` is retired and historical `SYNC-15` is reclassified into the cross-cutting Reproducibility contract. Old current-looking architecture wording must be cleaned by 013-I.

M8 areas such as formal composable privacy/accounting, product-owned governance/release, publication lifecycle, durable session/feed lifecycle, independent graph lifecycle, resource economics and reusable knowledge/memory receive no placeholder architecture absent renewed concept discovery.

## Implementation boundary

Phase 013 is design/reconciliation only.

Do not begin production behavior, migrations, persistence schemas, distributed-data implementation, provider adapters, public API stabilization, package refactoring, recovery mechanisms, runtime integration, benchmarks or executable conformance work.

```text
Phase 013  architecture reconciliation — ACTIVE
Phase 014  whole-design / implementation-readiness decision
Phase 015  implementation authority — FUTURE ONLY
```

Until Phase 014 positively passes:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## Current next boundary

**013-D — Distributed Data Boundary, Structured Topology, Manifest, Candidate/Seal/Promotion & Large-State Reconciliation** is next eligible.
