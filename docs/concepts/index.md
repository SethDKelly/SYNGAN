---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and normalized through Phase 008.

Cross-concept dependence/composition is now consolidated by [Phase 009 Dependence, Application Family & Composition Consolidation](../authority/phase-009-dependence-composition-consolidation.md).

## Current individual-concept authority

- [Concept State, Identity, History & Invariant Normalization](state-identity-history-invariant-normalization.md)
- [Concept Action, Query, Preconditions/Postconditions & Lifecycle Normalization](action-query-lifecycle-normalization.md)
- [Operational Principle, Purpose Fulfillment & Counterexample Normalization](operational-principle-purpose-counterexample-normalization.md)
- [Concept Independence, Genericity, Familiarity & Reuse Normalization](independence-genericity-familiarity-reuse-normalization.md)
- [Catalog Perimeter Candidate Rediscovery, Missing-Concept & Boundary Audit](catalog-perimeter-candidate-rediscovery-boundary-audit.md)
- [Phase 008 Individual-Concept Design Consolidation](phase-008-individual-concept-consolidation.md)

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

## Current catalog/composition state

```text
accepted concepts                    11
historical synchronization IDs       15
active synchronizations              13
missing current concept              NONE FOUND
Phase 008                            COMPLETE
Phase 009                            COMPLETE
D1-D4                                CURRENTLY CLOSED
E1-E5                                CURRENTLY CLOSED
Phase 010                            NEXT ELIGIBLE
```

Phase 009 found no reason to add, remove, merge, split, or rename a concept.

## Core boundaries handed to Phase 010

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

Generation owns request/Condition and candidate-to-completed logical output semantics. Synthetic Output is not a separate accepted concept. Reproducibility remains a cross-cutting contract. Generic Privacy remains deferred pending mechanism-specific discovery. Use/Release Decision remains external authority.

## Application-family result

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Direct Generation remains valid without Learning/Learned State. Evaluation/Evidence are not universal prerequisites for Generation. Constraint, Execution, and Provenance remain capability-conditional.

## Synchronization result

```text
required-relational active rules      6
conditional active rules              7
retired concept-local                 SYNC-08
reclassified cross-cutting contract   SYNC-15
new synchronization                   NONE
SYNC-16                               NOT JUSTIFIED
```

`SYNC-06` remains conditional Generation/Learned State reuse.

No hidden Compatibility, Workflow/Run, Artifact/Promotion, Approval/Quality, Reproducibility, or Composition concept is required.

## Phase 010 mapping implications

Phase 010 must map accepted concepts without collapsing their distinct purposes merely for interface convenience.

In particular it must preserve:

- Learning/Generation/Evaluation distinction;
- Learned State/Generation output/Evidence distinction;
- Data Meaning/Constraint/Condition distinction;
- Criterion/Evaluation/Evidence distinction;
- Execution operational state versus domain semantic state;
- Evidence observation versus approval/release authority;
- Provenance relationships versus source facts;
- application-family optionality;
- exact historical bindings and current-versus-historical status.

If a concept cannot be mapped intelligibly without violating its purpose/boundaries, Phase 010 should record a genuine upstream misfit rather than erase the distinction.

## Future rediscovery triggers

Fresh discovery remains required before materially expanded scope such as:

- composable formal privacy/accounting;
- product-owned governance/release decisions;
- independently reusable/negotiable request or cohort definitions;
- independent synthetic-output publication/versioning/retirement/transformation/current-use lifecycle;
- arbitrary graph/recursive topology with independent relationship behavior;
- product-owned economic/resource allocation/budget/quota management.

Implementation objects, IDs, tables, services, manifests or status enums do not themselves justify a concept.

## Authority rule

No implementation resource, architecture dependency, or future mapping convenience may redefine concept boundaries merely because it exists.

Similarity of implementation mechanics does not justify concept merger.

## Current next boundary

**Phase 010 — Concept Mapping, Interaction, Linguistic & Experience Alignment** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
