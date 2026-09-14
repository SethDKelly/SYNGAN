# SYNGAN

SYNGAN is a design-first synthetic-data generation framework intended for Spark-scale workloads.

SYNGAN follows Daniel Jackson-style concept design and explicitly requires the full design program to complete before implementation can become ready.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current authority includes:

- [`Concept Design Methodology`](docs/authority/design-methodology.md)
- [`Jackson Design Completion & Implementation Hold`](docs/authority/jackson-design-completion-implementation-hold.md)
- [`Jackson Methodology Completion Matrix`](docs/authority/jackson-methodology-completion-matrix.md)
- [`Accepted Concept Catalog`](docs/concepts/index.md)
- [`Concept Dependence & Application Family`](docs/dependence/index.md)
- [`Synchronization Authority`](docs/synchronizations/index.md)
- [`Phase 009 Consolidation`](docs/authority/phase-009-dependence-composition-consolidation.md)
- [`Concept Mapping Authority`](docs/mapping/index.md)
- [`010-A Mapping Control Authority`](docs/mapping/mapping-authority-coverage-actor-surface-evidence-baseline.md)
- [`Phase 010`](docs/phases/010/index.md)

## Status

```text
accepted concepts                    11
current desired outcomes             16
historical synchronization IDs       15
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
D1-D4                                CURRENTLY CLOSED
E1-E5                                CURRENTLY CLOSED
Phase 010                            ACTIVE
Phase 010 decomposition              COMPLETE
010-A                                COMPLETE
010-B                                NEXT ELIGIBLE
F1                                   PARTIAL
F2                                   PARTIAL
F3                                   PARTIAL TO STRONG
F4                                   PARTIAL
F5                                   STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

010-A establishes the current mapping-control model:

```text
actor roles                             7
surface families                        7
application-family applicability tags  10
mapping coverage dimensions            12
canonical mapping fields               19
```

Every later mapping must identify a canonical concept owner, actor intent, surface-neutral interaction/inspection obligation, family applicability, temporal orientation, disclosure/history-quality constraints, scale/boundedness, evidence source, and explicit mapping status.

Current coverage progression:

```text
SOURCE IDENTIFIED
  -> SEMANTICALLY MAPPED
  -> LINGUISTICALLY ALIGNED
  -> SURFACE-MAPPED
  -> FAMILY-REPLAYED
  -> PARITY-VALIDATED
```

`BLOCKED BY MISFIT` remains explicit when a concept cannot be mapped honestly without reopening upstream authority.

Phase 003/006 experience documents remain strong evidence, but 010-A normalizes stale assumptions: there are 15 historical synchronization IDs but 13 active rules; `SYNC-08` is retired; `SYNC-15` is reclassified; and Learning, Evaluation/Evidence, Execution and Provenance are conditional rather than universal workflow requirements.

Phase 010 may identify candidate SDK/API, notebook, CLI, report/history, graphical and operator/admin interaction forms. It does not choose concrete endpoints, classes, widgets, packages, storage, services, event topology or runtime mechanisms.

## Remaining design roadmap

```text
010    Concept Mapping, Interaction, Linguistic & Experience Alignment — ACTIVE
011    Specificity, Familiarity, Integrity, Synergy, Misfit & Adversarial Design Validation
012    Jackson Concept-Design Consolidation & Completion Decision
013    Post-Concept Representation & Architecture Reconciliation
014    Whole-Design Consolidation, Residual Debt Audit & Implementation-Readiness Decision
---
015    Implementation Authority & Controlled Delivery — FUTURE ONLY
```

Only a positive Phase 014 may change implementation to **READY / NOT STARTED / NEXT**. A later explicit Phase 015 would still be required to begin implementation.

## Current next boundary

**010-B — Concept Action → Actor Intent & Interaction Mapping** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
