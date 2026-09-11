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
D1 dependence graph         CURRENTLY CLOSED
D2 application family       CURRENTLY CLOSED
D3 explanation ordering     CURRENTLY CLOSED
```

Phase 008 found no unresolved J1 local concept-specification defect or J2 purpose/boundary/catalog defect.

009-A/B/C likewise find no reason to add, remove, merge, split, or rename a concept.

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

## Current inclusion-dependence graph

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

This does **not** weaken Phase 008 independence. Independence concerns whether each concept is understandable/behaviorally coherent on its own; inclusion dependence concerns whether the current application family has a reason to include one without the other.

## Current application-family result

009-C establishes that the accepted catalog composes into multiple coherent application subsets rather than one mandatory eleven-concept application.

Canonical capability kernels are:

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Reusable authority-only family members also include:

```text
{ Data Meaning }
{ Synthesis Strategy }
{ Constraint }
{ Evaluation Criterion }
```

Execution is valid only with at least one of Learning, Generation, or Evaluation. Provenance is valid only when there is a meaningful provenance-bearing relationship/history witness.

Capability claims can require larger subsets without changing universal dependence. Examples include learned-state-assisted Generation, evaluation-gated Generation, reusable Constraint support, durable Execution, and Provenance/history capability.

Topology/time-series/multi-table/text-bearing structured-data variants do not add current concepts merely because their representation differs.

## Future rediscovery triggers

The catalog is not permanently frozen. Fresh Jackson-style discovery is required before implementing materially expanded scope such as:

- composable formal privacy/accounting;
- product-owned governance/release decisions;
- independently reusable request/cohort definitions;
- independent synthetic-output publication/versioning/retirement/transformation lifecycle;
- arbitrary graph/recursive topology beyond current structural semantics;
- product-owned economic/resource allocation/budget management.

009-D must distinguish these rediscovery triggers from ordinary extension by adding existing concepts to a coherent family member.

## Authority rule

The individual concept specifications plus current Phase 008 normalization/consolidation authorities remain upstream of Phase 009 dependence/composition and downstream architecture.

No implementation resource or architecture dependency may redefine a concept boundary, dependence relation, or family member merely because it exists.

A coherent application-family subset does not imply one package/module/service/deployment boundary.

## Current next boundary

**009-D — Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
