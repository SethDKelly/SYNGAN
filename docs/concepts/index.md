---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and normalized through Phase 008.

Cross-concept dependence/composition is consolidated by [Phase 009 Dependence, Application Family & Composition Consolidation](../authority/phase-009-dependence-composition-consolidation.md). Concept mapping is consolidated by [Phase 010 Concept Mapping Consolidation](../authority/phase-010-concept-mapping-consolidation.md). Current composed specificity is governed by [Composed Specificity, Purpose Alignment & Boundary Sharpness Audit](../authority/composed-specificity-purpose-boundary-audit.md), and composed familiarity/reuse by [Familiarity, Reuse, Vocabulary & External-Model Comparison Audit](../authority/composed-familiarity-reuse-vocabulary-external-model-audit.md).

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
F1-F5 mapping                        CURRENTLY CLOSED
Phase 011                            ACTIVE
011-A                                COMPLETE
011-B                                COMPLETE
011-C                                COMPLETE
011-D                                NEXT ELIGIBLE
G1 composed specificity              CURRENTLY CLOSED
G2 composed familiarity              CURRENTLY CLOSED
```

Phase 009 found no reason to add, remove, merge, split or rename a concept. Phase 010 found no mapping/composition reason to reopen that conclusion. 011-B re-tests the catalog as one composed mapped design and finds no specificity-driven catalog change. 011-C compares the final vocabulary against familiar external conceptual jobs and again retains all eleven canonical names.

## 011-B composed specificity result

```text
11 / 11 concepts                       PASS
high-risk neighboring boundaries      PASS
reduced application-family replay     PASS
full-composition anti-umbrella replay PASS
MAT-2 specificity findings            0
MAT-3 specificity blockers            0
catalog changes                       0
upstream reopens                      0
R010-01 composed specificity drift    NO DEFECT
G1 specificity                        CURRENTLY CLOSED
```

Two bounded `MAT-1` watch points remain for later Phase 011 audits:

- Synthesis Strategy's broad capability declaration surface must not absorb plugin/runtime/configuration infrastructure;
- Provenance's high reference fan-in must not become owner-state authority.

## 011-C composed familiarity result

```text
11 / 11 canonical names retained
application-family vocabulary reuse     PASS
external-model comparison               PASS
MAT-2 familiarity findings              0
MAT-3 familiarity blockers              0
catalog rename / merge / split          NONE
upstream reopens                        NONE
R010-02 familiarity/precision           NO DEFECT — COMPATIBILITY GUIDANCE STRENGTHENED
B4 familiarity / reuse                  CURRENTLY CLOSED
G2 familiarity                          CURRENTLY CLOSED
```

Compatibility terms remain subordinate to canonical ownership:

```text
fit / train         -> qualified Learning verbs
model               -> qualified Learned State analogue when model-shaped
sample              -> Generation verb only when clearly synthetic production
validation result   -> qualified Evidence analogue
lineage             -> derivational subset of Provenance
run / job           -> external operational vocabulary; qualify owner
artifact / metadata -> physical or umbrella vocabulary, not concepts
metric              -> method/observation vocabulary, not Criterion/Evidence by itself
synthesizer         -> external/implementation aggregate, not a canonical concept
```

`Data Meaning`, `Learned State` and `Evaluation Criterion` retain bounded first-use familiarity cost but remain more semantically accurate than their common alternatives.

## Core boundaries preserved

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

## Application-family result

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Direct Generation remains valid without Learning/Learned State. Evaluation/Evidence are not universal prerequisites for Generation. Constraint, Execution and Provenance remain capability-conditional.

Concept inclusion defines available capability rather than requiring every included concept to be re-executed in every invocation.

## Authority rule

No external noun, implementation resource, architecture dependency, dashboard/report convenience, query schema, recovery mechanism or host-platform representation may redefine concept boundaries merely because it exists or is familiar.

Later Phase 011 evidence may reopen the smallest affected concept authority only when a concrete semantic consequence demonstrates a genuine defect.

## Current next boundary

**011-D — Integrity Under Synchronization, Correction, Invalidation & Historical Composition** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
