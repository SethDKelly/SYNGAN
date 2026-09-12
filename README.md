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
- [`Phase 010`](docs/phases/010/index.md)

## Status

```text
accepted concepts                    11
current desired outcomes             16
historical synchronization IDs       15
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
009-A..009-H                         COMPLETE
D1-D4                                CURRENTLY CLOSED
E1-E5                                CURRENTLY CLOSED
Phase 010                            ACTIVE
Phase 010 decomposition              COMPLETE
010-A                                NEXT ELIGIBLE
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

Phase 010 now has a dependency-safe mapping sequence:

```text
010-A  mapping authority / coverage / actor-surface taxonomy / evidence baseline
010-B  action -> actor intent / interaction mapping
010-C  state/query/history -> inspection mapping
010-D  linguistic / vocabulary / typed status / disclosure semantics
010-E  physical interaction across candidate surface families
010-F  application-family workflow composition / progressive disclosure
010-G  human-programmatic parity / degraded-recovery-scale mapping misfit
010-H  mapping consolidation / Phase 011 handoff
```

Phase 003/006 experience documents are retained as strong evidence, but Phase 010 must replay them against the normalized Phase 008 concept design and completed Phase 009 application-family/composition authority rather than assuming historical workflows are automatically complete current mappings.

Mapping must preserve multiple coherent application variants rather than presenting one mandatory full-suite workflow. It must also preserve semantic versus operational completion, candidate/non-final versus authoritative results, Criterion/Evaluation/Evidence separation, Evidence versus approval/release authority, Provenance versus source-fact authority, exact historical bindings and occurrence-scoped synchronization.

Phase 010 may identify candidate SDK/API, notebook, CLI, report/history, graphical and operator/admin interaction forms. It does not yet choose concrete endpoints, classes, widgets, packages, storage, services, event topology or runtime mechanisms.

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

**010-A — Mapping Authority, Coverage Model, Actor/Surface Taxonomy & Evidence Baseline** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.