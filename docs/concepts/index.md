---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: complete-current
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and normalized/revalidated through the completed Jackson concept-design program.

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
Phase 008-012                        COMPLETE
A1-H2                                CURRENTLY CLOSED
Jackson concept design               COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013                            COMPLETE
R1 architecture reconciliation       CURRENTLY CLOSED
representation / architecture       RECONCILED / CURRENT
Phase 014                            ACTIVE
014-A                                NEXT ELIGIBLE
R2                                   OPEN
R3                                   OPEN
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

Phase 012 found no reason to add, remove, merge, split or rename a current concept. Phase 013 reconciled architecture without requiring a concept reopen.

## Current catalog result

```text
current missing concept              NONE FOUND
current M2-M5 conceptual defects     0
unresolved MAT-2 findings            0
MAT-3 blockers                       0
concept reopen                       NONE
catalog change                       NONE
accepted conceptual tradeoff         NONE REQUIRED
```

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

These are future design-governance triggers, not accepted concepts, architecture placeholders or implementation backlog items.

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

Generation owns request/Condition and candidate-to-completed logical output semantics under current scope. Learned State owns reusable source-derived synthesis knowledge. Reproducibility remains cross-cutting. Generic Privacy remains rejected pending mechanism-specific discovery. Use/Release Decision remains external until product scope explicitly changes.

## Application-family result

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Direct Generation remains valid without Learning/Learned State. Evaluation/Evidence are not universal prerequisites for Generation. Constraint, Execution and Provenance remain capability-conditional.

## Phase 014 boundary

Phase 014 re-audits the catalog only as part of the **whole-design chain**. It may reopen a concept only if cross-layer evidence demonstrates a genuine contradiction or missing independently owned purpose/state/actions/lifecycle.

Existing code, provider convenience, architecture roles, or implementation difficulty cannot create a concept by pressure alone.

## Current next boundary

**014-A — Whole-Design Audit Authority, Evidence Baseline, Traceability & Reopen Rules** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
