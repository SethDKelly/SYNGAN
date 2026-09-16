---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and normalized through Phase 008.

Cross-concept dependence/composition is consolidated by [Phase 009 Dependence, Application Family & Composition Consolidation](../authority/phase-009-dependence-composition-consolidation.md). Concept mapping is consolidated by [Phase 010 Concept Mapping Consolidation](../authority/phase-010-concept-mapping-consolidation.md).

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
Phase 010                            COMPLETE
010-A..010-H                         COMPLETE
F1 semantic action mapping           CURRENTLY CLOSED
F2 semantic inspection mapping       CURRENTLY CLOSED
F3 linguistic mapping                CURRENTLY CLOSED
F4 physical/family mapping           CURRENTLY CLOSED
F5 human/programmatic parity         CURRENTLY CLOSED
concept mapping                      COMPLETE ENOUGH FOR PHASE 011
```

Phase 009 found no reason to add, remove, merge, split or rename a concept. Phase 010-A through 010-H find no mapping, family-composition or difficult-condition parity reason to reopen that conclusion.

## Final mapping coverage

```text
66 / 66 normalized command groups       SEMANTICALLY MAPPED
52 / 52 normalized query groups         SEMANTICALLY MAPPED
11 / 11 lifecycle/history envelopes     SEMANTICALLY MAPPED
5 / 5 explanation patterns              SEMANTICALLY MAPPED
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

> **SYNGAN is agnostic across compliant Spark-capable hosting and infrastructure platforms.**

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

The current catalog remains sufficient under retry/cancellation/unknown operational state, recovery/authority-continuity uncertainty, capability-specific degradation, disclosure/withholding/security responses, reconstructed/partial history, later Evidence staleness/invalidation, topology/text-bearing structured-data cases, enterprise-scale bounded interaction, approximation pressure, and operator/extension-author interaction.

No Actionability, Recovery, Degraded Mode, History Quality, Disclosure State, Topology, Text, Platform Job, Workflow, Status, Dashboard, Approval or other aggregate concept is added.

## Phase 011 handoff

Phase 011 must now test the final mapped catalog for specificity, familiarity, integrity, synergy/simplicity, exceptional/adversarial misfit, future-scope/extensibility misfit and residual conceptual debt.

A later genuine misfit may reopen the smallest affected concept authority; Phase 010 completion is not a prohibition on correction.

## Authority rule

No implementation resource, architecture dependency, dashboard/report convenience, query schema, mapping vocabulary, recovery mechanism or host-platform representation may redefine concept boundaries merely because it exists.

## Current next boundary

**Phase 011 — Specificity, Familiarity, Integrity, Synergy, Misfit & Adversarial Design Validation — entry/decomposition** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
