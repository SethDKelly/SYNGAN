---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and refined through current Phase 008 authority.

Cross-concept coordination remains authoritative under [Synchronizations](../synchronizations/index.md), while current inclusion-dependence/application-family work is governed by [Concept Dependence & Application Family](../dependence/index.md) and [Phase 009](../phases/009/index.md).

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

009-A/009-B likewise find no reason to add, remove, merge, split, or rename a concept.

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

## Current inclusion-dependence result

009-A classified pairwise application inclusion. 009-B now establishes the direct universal graph:

```text
Learning      -> Data Meaning
Learning      -> Synthesis Strategy
Learning      -> Learned State
Learned State -> Learning

Generation    -> Data Meaning
Generation    -> Synthesis Strategy

Evaluation    -> Evaluation Criterion
Evaluation    -> Evidence
Evidence      -> Evaluation
```

The pairwise findings `Learned State -> Data Meaning`, `Learned State -> Synthesis Strategy`, and `Evidence -> Evaluation Criterion` are transitive rather than direct.

Two legitimate application-inclusion SCCs remain:

```text
{ Learning, Learned State }
{ Evaluation, Evidence }
```

This does **not** weaken Phase 008 independence. Independence concerns whether each concept is understandable/behaviorally coherent on its own; inclusion dependence concerns whether the current SYNGAN application family has a reason to include one without the other.

The SCCs do not merge state/actions or authorize technical co-location.

Execution and Provenance retain non-binary application-family prerequisites rather than universal pairwise edges.

## Future rediscovery triggers

The catalog is not permanently frozen. Fresh Jackson-style discovery is required before implementing materially expanded scope such as composable formal privacy/accounting, product-owned governance/release decisions, reusable request/cohort definitions, independent output lifecycle, arbitrary graph/recursive topology, or product-owned economic/resource management.

## Authority rule

The individual concept specifications plus current Phase 008 normalization/consolidation authorities remain upstream of Phase 009 dependence/composition and downstream architecture.

No implementation resource or architecture dependency may redefine a concept boundary or dependence relation merely because it exists.

## Current next boundary

**009-C — Application Family, Valid Concept Subsets & Minimal Coherent Variants**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
