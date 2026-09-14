---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and normalized through Phase 008.

Cross-concept dependence/composition is consolidated by [Phase 009 Dependence, Application Family & Composition Consolidation](../authority/phase-009-dependence-composition-consolidation.md). Current mapping work is governed by [Concept Mapping Authority](../mapping/index.md).

## Accepted concepts

1. [Data Meaning](data-meaning.md)
2. [Synthesis Strategy](synthesis-strategy.md)
3. [Learning](learning.md)
4. [Learned State](learned-state.md)
5. [Generation](generation.md)
6. [Constraint](constraint.md)
7. [Evaluation Criterion](evaluation-criterion.md)
8. [Evaluation](evaluation.md)
9. [Evidence](evidence.md)
10. [Execution](execution.md)
11. [Provenance](provenance.md)

## Current concept/mapping state

```text
accepted concepts                    11
historical synchronization IDs       15
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
Phase 010                            ACTIVE
010-A                                COMPLETE
010-B                                COMPLETE
010-C                                NEXT ELIGIBLE
F1 semantic action mapping           CURRENTLY CLOSED
```

Phase 009 found no reason to add, remove, merge, split or rename a concept. 010-B finds no mapping reason to reopen that conclusion.

## Normalized action-mapping coverage

Current 010-B authority maps every normalized command group from [Concept Action, Query, Preconditions/Postconditions & Lifecycle Normalization](action-query-lifecycle-normalization.md):

```text
Data Meaning             7 / 7
Synthesis Strategy       4 / 4
Learning                 8 / 8
Learned State            4 / 4
Generation              11 / 11
Constraint               4 / 4
Evaluation Criterion     4 / 4
Evaluation               8 / 8
Evidence                 3 / 3
Execution                11 / 11
Provenance               2 / 2
                         ------
TOTAL                    66 / 66  SEMANTICALLY MAPPED
```

The canonical mapping is [Concept Action → Actor Intent & Interaction Mapping](../mapping/concept-action-actor-intent-interaction-mapping.md).

## Core boundaries mapping preserves

```text
Data Meaning          != Constraint
Synthesis Strategy    != implementation/plugin/runtime
Learning              != Learned State
Learning/Generation/
Evaluation             != Execution
Generation Condition  != Constraint
Evaluation Criterion  != Evaluation != Evidence
Evidence               != Provenance
Execution              != Attempt != platform job
```

Generation owns request/Condition and candidate-to-completed logical output semantics. Synthetic Output is not a separate concept. Reproducibility remains cross-cutting. Generic Privacy remains deferred pending mechanism-specific discovery. Use/Release Decision remains external authority.

## Important 010-B findings

- a conceptual command is not automatically one physical control;
- system-established actions remain semantically visible without requiring dedicated user gestures;
- Learning/Generation/Evaluation own contextual validation/readiness;
- Learned State/Evidence result establishment remains distinct from producer completion;
- Execution owns Attempt/retry/recovery/cancellation operations, not parent semantic completion;
- Generation candidate state remains Generation-local and does not resurrect `SYNC-08`;
- Evidence remains a finding, not approval/release/privacy authority;
- Provenance remains relation authority, not source-state authority;
- current/future-use status changes do not rewrite exact historical bindings.

## Application-family result

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Direct Generation remains valid without Learning/Learned State. Evaluation/Evidence are not universal prerequisites for Generation. Constraint, Execution and Provenance remain capability-conditional.

## 010-C handoff

010-C must map current concept state, queries, history and explanation obligations to actor/programmatic inspection.

It must preserve exact historical bindings, semantic-versus-operational state, candidate-versus-authoritative results, Evidence scope/strength/limitations/applicability, Provenance relations versus source facts, typed disclosure/history quality and bounded enterprise-scale inspection.

## Authority rule

No implementation resource, architecture dependency or mapping convenience may redefine concept boundaries merely because it exists. Similarity of implementation mechanics does not justify concept merger.

## Current next boundary

**010-C — Concept State, Query, History & Explanation → Inspection Mapping** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
