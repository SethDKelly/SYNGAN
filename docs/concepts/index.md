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
010-D                                NEXT ELIGIBLE
F1 semantic action mapping           CURRENTLY CLOSED
F2 semantic inspection mapping       CURRENTLY CLOSED
```

Phase 009 found no reason to add, remove, merge, split or rename a concept. 010-B/010-C find no mapping reason to reopen that conclusion.

## Current semantic mapping coverage

[010-B Action Mapping](../mapping/concept-action-actor-intent-interaction-mapping.md):

```text
66 / 66 normalized command groups  SEMANTICALLY MAPPED
```

[010-C Inspection Mapping](../mapping/concept-state-query-history-explanation-inspection-mapping.md):

```text
52 / 52 normalized query groups        SEMANTICALLY MAPPED
11 / 11 lifecycle/history envelopes    SEMANTICALLY MAPPED
5 explanation patterns                 SEMANTICALLY MAPPED
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

## 010-C inspection implications

Inspection does not create duplicate state ownership.

Current mappings preserve:

- current status versus exact historical bound truth;
- revisioned authority history without retroactive rewrite;
- proposed/committed/terminal activity state;
- durable result current-use status versus immutable historical result content;
- Generation partial/candidate/awaiting-validation/completed distinctions;
- Execution/Attempt operational history versus parent semantic state;
- Evidence finding/context/strength/limitations/current applicability;
- Provenance assertions/corrections versus referenced source facts;
- disclosure and historical-knowledge quality distinctions;
- bounded enterprise-scale inspection.

No standalone Dashboard, Status, History, Explanation, Lineage, Artifact, Result, Approval or Inspection concept is justified.

## Application-family result

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Direct Generation remains valid without Learning/Learned State. Evaluation/Evidence are not universal prerequisites for Generation. Constraint, Execution and Provenance remain capability-conditional.

Inspection follows the same optionality: absent capabilities do not produce fabricated relationships or empty mandatory panels/workflow steps.

## 010-D handoff

010-D must establish actor/programmatic linguistic mapping over the now-complete surface-neutral action and inspection semantics.

It must preserve concept-owner-specific lifecycle language and qualify overloaded ecosystem terms rather than flattening all state into a generic status vocabulary.

## Authority rule

No implementation resource, architecture dependency, dashboard/report convenience, query schema or mapping vocabulary may redefine concept boundaries merely because it exists. Similarity of implementation mechanics does not justify concept merger.

## Current next boundary

**010-D — Linguistic Mapping, Vocabulary, Typed Status & Disclosure Semantics** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
