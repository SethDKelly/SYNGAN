---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and normalized through Phase 008.

Current cross-concept authority is consolidated by Phase 009, Phase 010 mapping, and the completed Phase 011 quality/misfit program.

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

## Current concept/design state

```text
accepted concepts                    11
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
Phase 010                            COMPLETE
Phase 011                            COMPLETE
011-A..011-J                         COMPLETE
G1-G7                                CURRENTLY CLOSED
H1/H2                                OPEN — PHASE 012
Jackson concept design               NOT COMPLETE
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

No Phase 011 finding requires adding, removing, merging, splitting or renaming a current concept.

## Final Phase 011 catalog result

```text
current M2-M5 conceptual defects      0
unresolved MAT-2 findings             0
MAT-3 blockers                        0
concept reopen                        NONE
catalog change                        NONE
accepted conceptual tradeoff          NONE REQUIRED
M6 Phase-013 deferrals                1 — downstream documentation only
M8 future-rediscovery groups          4 — conditional future gates
```

The M6 item does not affect concept authority. M8 findings are not accepted concepts now.

## Future rediscovery boundary

Future scope must reopen concept discovery before implementation when it introduces an independently useful product purpose with durable state/history and independently meaningful actions/lifecycle that cannot be owned cleanly by the current catalog.

Known trigger forms include:

```text
formal composable privacy / guarantee accounting
product-owned governance / release decisions
independent output publication / versioning / retirement
independently reusable request / cohort semantics
independently governed graph / relationship lifecycle
durable streaming / session / feed lifecycle
product-owned economic / resource accounting
product-owned reusable knowledge / memory beyond Strategy/Learned State
```

These remain future design-governance triggers, not accepted concepts, architecture placeholders or implementation backlog items.

## Core boundaries preserved

```text
Data Meaning          != Constraint
Synthesis Strategy    != implementation/plugin/runtime/provider model
Learning              != Learned State
Learning/Generation/
Evaluation             != Execution
Generation Condition  != Constraint
Evaluation Criterion  != Evaluation != Evidence
Evidence               != Provenance
Execution              != Attempt != platform job
```

Generation owns request/Condition and candidate-to-completed logical output semantics under current scope. Learned State owns reusable source-derived synthesis knowledge under current scope. Reproducibility remains cross-cutting. Generic Privacy remains rejected pending mechanism-specific discovery. Use/Release Decision remains external until product scope explicitly changes.

## Application-family result

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Direct Generation remains valid without Learning/Learned State. Evaluation/Evidence are not universal prerequisites for Generation. Constraint, Execution and Provenance remain capability-conditional.

## Phase 012 boundary

Phase 012 must audit this catalog together with problem authority, application-family/dependence, synchronization, mapping and Phase 011 quality results as one current Jackson concept design.

## Current next boundary

**Phase 012 — Jackson Concept-Design Consolidation & Completion Decision** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
