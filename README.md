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
- [`Concept Mapping Authority`](docs/mapping/index.md)
- [`010-B Concept Action Mapping`](docs/mapping/concept-action-actor-intent-interaction-mapping.md)
- [`010-C Inspection Mapping`](docs/mapping/concept-state-query-history-explanation-inspection-mapping.md)
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
010-D                                NEXT ELIGIBLE
F1                                   CURRENTLY CLOSED
F2                                   CURRENTLY CLOSED
F3                                   PARTIAL TO STRONG
F4                                   PARTIAL
F5                                   STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

Current semantic mapping coverage is:

```text
normalized command groups               66 / 66 SEMANTICALLY MAPPED
normalized query groups                 52 / 52 SEMANTICALLY MAPPED
lifecycle/history envelopes             11 / 11 SEMANTICALLY MAPPED
cross-concept explanation patterns       5
```

The 010-C inspection rule is: **inspection exposes owned or validly derived truth; it does not create a second owner for that truth**.

Current mapping therefore preserves current versus exact historical state, semantic versus operational state, candidate/intermediate versus authoritative result, Evidence claim-strength versus approval, Provenance relationships versus source facts, typed disclosure/history-quality distinctions, application-family optionality and bounded enterprise-scale inspection.

010-D now owns linguistic alignment. It must choose safe actor/programmatic vocabulary for these mapped semantics without turning mapping categories into universal runtime enums or implementation schemas.

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

**010-D — Linguistic Mapping, Vocabulary, Typed Status & Disclosure Semantics** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
