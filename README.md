# SYNGAN

SYNGAN is a design-first synthetic-data generation framework intended for Spark-scale workloads.

SYNGAN is designed as a **deployable Python/Spark package** whose platform promise is:

> **Agnostic across compliant Spark-capable hosting and infrastructure platforms.**

It is not defined as a standalone UI application. Package, notebook and automated job/pipeline use are primary; CLI, reports, graphical presentation and standalone service/API exposure are optional adapters or integrations.

SYNGAN follows Daniel Jackson-style concept design and explicitly requires the full design program to complete before implementation can become ready.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current authority includes:

- [`Problem & Purpose`](docs/problem/problem-purpose.md)
- [`Concept Design Methodology`](docs/authority/design-methodology.md)
- [`Jackson Methodology Completion Matrix`](docs/authority/jackson-methodology-completion-matrix.md)
- [`Accepted Concept Catalog`](docs/concepts/index.md)
- [`Concept Dependence & Application Family`](docs/dependence/index.md)
- [`Synchronization Authority`](docs/synchronizations/index.md)
- [`Concept Mapping Authority`](docs/mapping/index.md)
- [`010-D Linguistic Mapping`](docs/mapping/linguistic-mapping-vocabulary-typed-status-disclosure-semantics.md)
- [`010-E Package/Host Physical Interaction Mapping`](docs/mapping/package-notebook-automation-host-platform-interaction-mapping.md)
- [`Phase 010`](docs/phases/010/index.md)

## Status

```text
accepted concepts                    11
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
Phase 010                            ACTIVE
010-A                                COMPLETE
010-B                                COMPLETE
010-C                                COMPLETE
010-D                                COMPLETE
010-E                                COMPLETE
010-F                                NEXT ELIGIBLE
F1                                   CURRENTLY CLOSED
F2                                   CURRENTLY CLOSED
F3                                   CURRENTLY CLOSED
F4                                   PARTIAL TO STRONG
F5                                   STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

Current mapping coverage is:

```text
66 / 66 command groups                    SEMANTICALLY MAPPED
52 / 52 query groups                      SEMANTICALLY MAPPED
11 / 11 lifecycle/history envelopes       SEMANTICALLY MAPPED
11 / 11 concept names                     LINGUISTICALLY ALIGNED
66 / 66 command groups                    PHYSICAL RESPONSIBILITY MAPPED
52 / 52 query groups                      PHYSICAL RESPONSIBILITY MAPPED
```

010-E establishes package/notebook/automation as primary interaction surfaces and treats CLI/report/UI/operator presentation as optional or host-owned where appropriate. A standalone network service, graphical application or dedicated admin console is not required for semantic completeness.

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

**010-F — Application-Family Workflow Composition, Optional-Capability Experience & Progressive Disclosure** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
