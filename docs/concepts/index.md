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
F1 semantic action mapping           CURRENTLY CLOSED
F2 semantic inspection mapping       CURRENTLY CLOSED
F3 linguistic mapping                CURRENTLY CLOSED
F4 physical mapping                  PARTIAL TO STRONG
```

Phase 009 found no reason to add, remove, merge, split or rename a concept. 010-B through 010-E find no mapping reason to reopen that conclusion.

## Current mapping coverage

```text
66 / 66 normalized command groups       SEMANTICALLY MAPPED
52 / 52 normalized query groups         SEMANTICALLY MAPPED
11 / 11 lifecycle/history envelopes     SEMANTICALLY MAPPED
11 / 11 accepted concept names          LINGUISTICALLY ALIGNED
66 / 66 command groups                  PHYSICAL RESPONSIBILITY MAPPED
52 / 52 query groups                    PHYSICAL RESPONSIBILITY MAPPED
```

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

## Package product-form implications

010-E confirms that concept completeness is provided through the Python/Spark package contract rather than through a required standalone application.

Primary physical interaction is:

```text
Python package / SDK
notebook / interactive package use
embedded job / pipeline / automation
```

CLI, reports, rich/graphical presentation and standalone service/API exposure are optional adapters or representations. Host platforms ordinarily own infrastructure administration UI while SYNGAN preserves its own Execution/Attempt and semantic authority through stable package contracts and correlations.

This product-form mapping does not change any concept boundary.

## Application-family result

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Direct Generation remains valid without Learning/Learned State. Evaluation/Evidence are not universal prerequisites for Generation. Constraint, Execution and Provenance remain capability-conditional.

010-F must now compose package/notebook/automation interaction through these valid family members without making optional concepts or optional presentation surfaces mandatory.

## Authority rule

No implementation resource, architecture dependency, dashboard/report convenience, query schema or mapping vocabulary may redefine concept boundaries merely because it exists. Similarity of implementation mechanics or labels does not justify concept merger.

## Current next boundary

**010-F — Application-Family Workflow Composition, Optional-Capability Experience & Progressive Disclosure** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
