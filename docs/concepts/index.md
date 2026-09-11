---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and refined through current Phase 008 authority.

Cross-concept coordination remains authoritative under [Synchronizations](../synchronizations/index.md), while current inclusion-dependence work is governed by [Concept Dependence & Application Family](../dependence/index.md) and [Phase 009](../phases/009/index.md).

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

## Current catalog state

```text
accepted concepts          11
accepted synchronizations  15
missing current concept     NONE FOUND
INDIVIDUAL CONCEPT DESIGN   COMPLETE ENOUGH FOR PHASE 009
```

Phase 008 found no unresolved J1 local concept-specification defect or J2 purpose/boundary/catalog defect.

## Core boundary results

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

Generation owns request/Condition and candidate-to-completed logical output semantics. Relationship remains Data Meaning-owned descriptive structure. Generic Privacy remains rejected pending fresh mechanism-specific discovery if future independent state/actions arise. Use/Release Decision remains external authority.

## 009-A inclusion-dependence result

009-A asks a different question from Phase 008 independence: if one concept is included in an application, must another also be included for the first concept's purpose to make sense?

The current [pairwise inventory](../dependence/inclusion-dependence-pairwise-inventory.md) finds twelve universal pairwise candidates:

```text
Learning      -> Data Meaning / Synthesis Strategy / Learned State
Learned State -> Learning / Data Meaning / Synthesis Strategy
Generation    -> Data Meaning / Synthesis Strategy
Evaluation    -> Evaluation Criterion / Evidence
Evidence      -> Evaluation Criterion / Evaluation
```

This does not merge concepts. `Learning <-> Learned State` and `Evaluation <-> Evidence` remain distinct activity/result concepts and are explicit 009-B cycle questions.

Execution and Provenance have conditional/disjunctive prerequisites rather than one universal pairwise dependency.

009-A makes no catalog change.

## Future rediscovery triggers

The catalog is not permanently frozen. Fresh Jackson-style discovery is required before implementing materially expanded scope such as composable formal privacy/accounting, product-owned governance/release decisions, reusable request/cohort definitions, independent output lifecycle, arbitrary graph/recursive topology, or product-owned economic/resource management.

## Authority rule

The individual concept specifications plus current Phase 008 normalization/consolidation authorities remain upstream of Phase 009 dependence/composition and downstream architecture.

No implementation resource or architecture dependency may redefine a concept boundary or dependence relation merely because it exists.

## Current next boundary

**009-B — Inclusion-Dependence Graph, Roots, Cycles & Explanation Ordering**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
