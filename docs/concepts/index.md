---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and normalized through Phase 008.

Cross-concept dependence/composition is consolidated by [Phase 009 Dependence, Application Family & Composition Consolidation](../authority/phase-009-dependence-composition-consolidation.md). Concept mapping is consolidated by [Phase 010 Concept Mapping Consolidation](../authority/phase-010-concept-mapping-consolidation.md). Current composed specificity is governed by [Composed Specificity, Purpose Alignment & Boundary Sharpness Audit](../authority/composed-specificity-purpose-boundary-audit.md).

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
011-C                                NEXT ELIGIBLE
G1 composed specificity              CURRENTLY CLOSED
G2 familiarity                       PARTIAL TO STRONG
```

Phase 009 found no reason to add, remove, merge, split or rename a concept. Phase 010 found no mapping/composition reason to reopen that conclusion. 011-B now re-tests the catalog as one composed mapped design and again finds no catalog change justified.

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

Specificity remains distinct from mere independence. 011-B verifies that each concept's purpose survives composition, has an intelligible absence consequence, retains a proportionate state/action boundary, and does not become infrastructure or a restatement of the whole product.

Key results:

- Data Meaning remains descriptive authority rather than Constraint/schema/metadata/Relationship;
- Synthesis Strategy remains reusable synthesis-behavior authority rather than plugin/runtime infrastructure;
- Learning and Learned State remain a legitimate activity/result split;
- Generation remains independently coherent in direct `G-KERNEL` composition;
- Constraint remains reusable prescriptive authority distinct from Generation Condition and Evaluation Criterion;
- Evaluation Criterion → Evaluation → Evidence remains question → examination → finding;
- Execution remains operational realization rather than scheduler/workflow authority;
- Provenance remains typed historical relationship authority with high fan-in and low authority fan-out.

No Workflow, global Status, Quality, Run, Artifact, Relationship/Topology, Recovery, Degraded Mode, Actionability, History Quality, Disclosure State or similar aggregate concept becomes necessary under composed specificity.

Two bounded `MAT-1` watch points remain for later Phase 011 audits:

- Synthesis Strategy's broad capability declaration surface must not absorb plugin/runtime/configuration infrastructure;
- Provenance's high reference fan-in must not become owner-state authority.

Neither is an unresolved G1 defect.

## Final Phase 010 mapping coverage

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

## Authority rule

No implementation resource, architecture dependency, dashboard/report convenience, query schema, mapping vocabulary, recovery mechanism or host-platform representation may redefine concept boundaries merely because it exists.

Later Phase 011 evidence may reopen the smallest affected concept authority only when a concrete semantic consequence demonstrates a genuine defect.

## Current next boundary

**011-C — Familiarity, Reuse, Vocabulary & External-Model Comparison Audit** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
