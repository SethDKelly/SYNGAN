---
type: Authority Index
title: SYNGAN Design Authority
status: active
---

# SYNGAN Design Authority

These documents define how SYNGAN design knowledge is created, interpreted, changed, and eventually implemented.

## Current methodology and governance

- [Concept Design Methodology](design-methodology.md)
- [Jackson Design Completion & Implementation Hold](jackson-design-completion-implementation-hold.md)
- [Jackson Methodology Completion Matrix](jackson-methodology-completion-matrix.md)
- [Phase 009 Dependence, Application Family & Composition Consolidation](phase-009-dependence-composition-consolidation.md)
- [Documentation Governance](documentation-governance.md)
- [Terminology Policy](terminology-policy.md)
- [Source & Provenance Policy](source-provenance-policy.md)

## Current design authority chain

- [Problem Knowledge](../problem/index.md)
- [Accepted Concept Catalog](../concepts/index.md)
- [Phase 008 Individual-Concept Design Consolidation](../concepts/phase-008-individual-concept-consolidation.md)
- [Concept Dependence & Application Family](../dependence/index.md)
- [Synchronization Authority](../synchronizations/index.md)
- [Phase 009 Consolidation](phase-009-dependence-composition-consolidation.md)
- [Concept Mapping Authority](../mapping/index.md)
- [010-A Mapping Control Authority](../mapping/mapping-authority-coverage-actor-surface-evidence-baseline.md)
- [010-B Concept Action Mapping](../mapping/concept-action-actor-intent-interaction-mapping.md)
- [Phase 010](../phases/010/index.md)

## Current posture

```text
accepted concepts                    11
historical synchronization IDs       15
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
D1-D4                                CURRENTLY CLOSED
E1-E5                                CURRENTLY CLOSED
Phase 010                            ACTIVE
010-A                                COMPLETE
010-B                                COMPLETE
010-C                                NEXT ELIGIBLE
F1                                   CURRENTLY CLOSED
F2                                   PARTIAL
F3                                   PARTIAL TO STRONG
F4                                   PARTIAL
F5                                   STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Current mapping authority

010-A defines the record schema, coverage ledgers, actor/surface taxonomy, application-family tags and evidence baseline.

010-B now supplies complete current semantic action mapping:

```text
normalized command groups       66
semantically mapped             66
mapping blockers                 0
new concept                      0
new synchronization              0
```

F1 is therefore currently closed at the surface-neutral semantic interaction layer. F4 remains separate: later physical mapping may realize one conceptual command through multiple gestures or combine several read-only facts without changing ownership.

## Action-mapping authority rules

- conceptual command does not imply direct user control;
- synchronized/system-established result actions remain observable rather than hidden;
- Validation/Readiness remains contextual to the consuming activity;
- semantic commitment remains distinct from operational start;
- cancellation request remains distinct from terminal cancellation;
- Execution/Attempt outcomes remain separate from parent domain outcomes;
- Generation candidate state remains distinct from completed output;
- Evaluation completion remains distinct from favorable Evidence;
- Evidence remains distinct from approval/release/privacy authority;
- Provenance remains relation authority rather than source-fact owner;
- status changes for future use do not rewrite historical bindings;
- optional capabilities remain optional across the application family.

## Architecture boundary

The [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md) remains downstream evidence pending Phase 013 reconciliation.

Neither 010-A's mapping schema nor 010-B's 66 action records prescribe concrete APIs, classes, widgets, schema types, events, transactions, services, packages, queues or deployment topology.

## Remaining design sequence

```text
010-C  state/query/history/explanation inspection mapping — NEXT
010-D  linguistic/vocabulary mapping
010-E  physical interaction mapping
010-F  application-family workflow replay
010-G  parity/degraded/recovery/scale misfit audit
010-H  Phase 010 consolidation
011    final concept-design quality / misfit
012    Jackson concept-design completion decision
013    representation / architecture reconciliation
014    whole-design completion / implementation-readiness decision
```

## Implementation-readiness rule

Only Phase 014 may set **READY / NOT STARTED / NEXT** after the whole design passes. Phase 015 is still required before implementation begins.

## Current next boundary

**010-C — Concept State, Query, History & Explanation → Inspection Mapping** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
