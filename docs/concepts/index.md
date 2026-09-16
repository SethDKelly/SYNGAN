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
010-F                                COMPLETE
010-G                                COMPLETE
010-H                                NEXT ELIGIBLE
F1 semantic action mapping           CURRENTLY CLOSED
F2 semantic inspection mapping       CURRENTLY CLOSED
F3 linguistic mapping                CURRENTLY CLOSED
F4 physical/family mapping           CURRENTLY CLOSED
F5 human/programmatic parity         CURRENTLY CLOSED
```

Phase 009 found no reason to add, remove, merge, split or rename a concept. 010-B through 010-G find no mapping, family-composition or difficult-condition parity reason to reopen that conclusion.

## Current mapping coverage

```text
66 / 66 normalized command groups       SEMANTICALLY MAPPED
52 / 52 normalized query groups         SEMANTICALLY MAPPED
11 / 11 lifecycle/history envelopes     SEMANTICALLY MAPPED
11 / 11 accepted concept names          LINGUISTICALLY ALIGNED
66 / 66 command groups                  PHYSICAL RESPONSIBILITY MAPPED
52 / 52 query groups                    PHYSICAL RESPONSIBILITY MAPPED
10 / 10 family/capability replays       PASS
20 / 20 difficult-condition probes      PASS
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

Concept completeness is provided through the Python/Spark package contract rather than through a required standalone application.

Primary physical interaction is package/SDK, notebook and embedded automation. CLI, reports, rich/graphical presentation and standalone service/API exposure are optional adapters or representations. Host platforms ordinarily own infrastructure administration UI while SYNGAN preserves its own Execution/Attempt and semantic authority through stable package contracts and correlations.

This product-form mapping does not change any concept boundary.

## Application-family result

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Direct Generation remains valid without Learning/Learned State. Evaluation/Evidence are not universal prerequisites for Generation. Constraint, Execution and Provenance remain capability-conditional.

Concept inclusion defines available capability rather than requiring every included concept to be re-executed in every invocation. Existing Learned State and reusable authority may be selected rather than recreated.

## Difficult-condition parity result

010-G confirms that the current catalog remains sufficient under:

- retry/cancellation/unknown operational state;
- recovery/authority-continuity uncertainty;
- capability-specific degraded operation;
- disclosure/withholding/security responses;
- reconstructed/partial history;
- later Evidence staleness/invalidation/current inapplicability;
- time-series/multi-table and text-bearing structured-data cases;
- enterprise-scale bounded interaction;
- operator and extension-author interaction.

No Actionability, Recovery, Degraded Mode, History Quality, Disclosure State, Topology, Text, Platform Job, Workflow, Status, Dashboard, Approval or other aggregate concept is added.

## Authority rule

No implementation resource, architecture dependency, dashboard/report convenience, query schema, mapping vocabulary, recovery mechanism or host-platform representation may redefine concept boundaries merely because it exists.

## Current next boundary

**010-H — Phase 010 Consolidation, F1-F5 Completion Decision & Phase 011 Handoff** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
