# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**Jackson concept design is complete for the current product scope. Phase 013 architecture reconciliation is ACTIVE; 013-A and 013-B are complete, and 013-C is next. Implementation remains held.**

Start with:

- `docs/index.md`
- `docs/problem/problem-purpose.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-013-architecture-reconciliation-authority.md`
- `docs/phases/013/index.md`
- `docs/phases/013/013-A-reconciliation-authority-retained-corpus-inventory-precedence-reset-discrepancy-taxonomy.md`
- `docs/phases/013/013-B-representation-layering-public-contract-identity-revision-handle-view-reconciliation.md`
- `docs/architecture/phase-013-b-representation-layering-public-contract-identity-view-reconciliation.md`
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
013-C                                NEXT ELIGIBLE
R1 architecture reconciliation       DOWNSTREAM / IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Primary authority rule

> **Completed concept design and completed Phase 013 reconciliation decisions are upstream authority for unreconciled architecture. Retained architecture, code, tests and provider models may expose a genuine defect, but they may not redefine semantics merely to preserve historical choices.**

Only a demonstrated `AR-9` genuine upstream contradiction may justify `UPSTREAM-REOPEN`. Use the smallest-authority reopen rule and revalidate the material blast radius.

## Phase 013 finding discipline

Use the canonical discrepancy classes `AR-0..AR-9`, materiality `AMAT-0..AMAT-3`, and dispositions:

```text
RETAIN
CLARIFY
SUPERSEDE
CORRECT
DEFER
UPSTREAM-REOPEN
```

Do not turn these documentation classifications into runtime enums/resources/issues by implication.

## 013-B current representation invariants

Architecture must preserve:

- architecture as representation of semantic authority, not a second semantic owner;
- logical layering without mandatory package/service/process/API-tier mapping;
- Python package/SDK, notebook and embedded automation as primary interaction roles;
- CLI/report/graphical/service surfaces as optional or integration roles;
- semantic parity for any surfaces that exist, without requiring all optional surfaces;
- stable logical identity distinct from path/table/provider/run/model/artifact identity;
- separate logical identity, semantic revision/commitment, current state version/freshness and representation schema version;
- exact historical bindings alongside refreshable current views;
- handles/views as resolvers/projections rather than detached mutable canonical entities;
- Execution ownership of retry/resume/reconcile/cancel operational state;
- owner-specific Learned State, Generation-output and Evidence establishment rather than a universal Result lifecycle;
- readiness/actionability as contextual derived views rather than global status authority;
- D0-D4 as semantic disclosure depth, not architecture/API/UI/storage tiers;
- bounded/reference-first interaction for Spark-scale payloads.

Historical `007-D` synchronization-count wording and old representation-precedence wording are semantically superseded by current authority but remain explicit 013-I cleanup obligations.

## 013-C next scope

013-C reconciles control persistence, exact historical references, transaction/concurrency boundaries, migration and recovery-state representation.

It must verify at least:

- persistence preserves owner authority rather than creating generic CRUD authority;
- immutable exact bindings remain distinct from mutable current projections;
- CAS/state versions protect observed mutation boundaries but do not validate semantics;
- same-owner coupled facts and cross-boundary durable intent do not create synchronization-owned state;
- transaction/outbox language does not prescribe one universal technology pattern;
- migration changes representation unless upstream semantics explicitly changed;
- restored persistence cannot recreate current mutation authority;
- reconstructed/partial/unknown history remains attributable;
- current 13-sync semantics replace historical synchronization assumptions.

## Durable quality rules

Decision-material disclosure:

> **Do not hide a qualifier whose omission could change the actor's immediate semantic decision or make current state appear stronger than its owner supports.**

Provider evidence:

> **Consume provider facts only at the evidentiary strength they actually establish.**

Future rediscovery:

> **New independent product-facing purpose/state/actions/lifecycle returns to concept discovery before architecture or implementation.**

## M6 / M8 carry-forward

Current synchronization authority is `15 historical IDs / 13 active synchronizations`; `SYNC-08` is retired as Generation-local behavior and `SYNC-15` is reclassified as the Reproducibility contract. Old current-looking architecture wording must be cleaned by 013-I.

M8 areas such as formal composable privacy/accounting, product-owned governance/release, publication lifecycle, durable session/feed lifecycle, independent graph lifecycle, resource economics and reusable knowledge/memory receive no placeholder architecture absent renewed concept discovery.

## Implementation boundary

Phase 013 is design/reconciliation only.

Do not begin production behavior, migrations, persistence schemas, provider adapters, public API stabilization, package refactoring, recovery mechanisms, runtime integration, benchmarks or executable conformance work.

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

**013-C — Control Persistence, Historical Reference, Transaction/Concurrency, Migration & Recovery-State Reconciliation** is next eligible.
