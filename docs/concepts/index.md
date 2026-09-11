---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and refined through current Phase 008 authority.

Cross-concept coordination is governed by [Synchronizations](../synchronizations/index.md), while inclusion-dependence/application-family work is governed by [Concept Dependence & Application Family](../dependence/index.md) and [Phase 009](../phases/009/index.md).

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
INDIVIDUAL CONCEPT DESIGN            COMPLETE ENOUGH FOR PHASE 009
D1-D4                                CURRENTLY CLOSED
E1                                   CURRENTLY CLOSED
```

Phase 008 found no unresolved J1 local concept-specification defect or J2 purpose/boundary/catalog defect.

009-A through 009-E likewise find no reason to add, remove, merge, split, or rename a concept.

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

## Current application-family result

The accepted catalog composes into multiple coherent application subsets rather than one mandatory eleven-concept application.

Canonical capability kernels are:

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Reusable authority-only family members include Data Meaning, Synthesis Strategy, Constraint and Evaluation Criterion independently.

Execution is valid only with at least one Learning/Generation/Evaluation activity. Provenance is valid only with a meaningful provenance-bearing relationship/history witness.

## Current synchronization result

009-E confirms that concept independence and composition are cleaner with **13 active synchronizations**, not fifteen.

### Active required-relational

```text
SYNC-01  Data Meaning revision binding
SYNC-02  Strategy selection and compatibility
SYNC-05  Learning produces Learned State
SYNC-06  Generation commitment and compatibility
SYNC-09  Evaluation Criterion binding
SYNC-10  Evaluation method compatibility
SYNC-12  Evaluation produces Evidence
```

### Active conditional

```text
SYNC-03  Constraint binding/handling
SYNC-04  Learning operational realization
SYNC-07  Generation operational realization
SYNC-11  Evaluation operational realization
SYNC-13  evidence-gated Generation/Evidence handoff
SYNC-14  Provenance recording
```

`SYNC-08` is retired from active composition because synthetic output is Generation-owned result state. This reinforces rather than changes the existing catalog boundary: no standalone Output concept is introduced.

`SYNC-15` is reclassified as the cross-cutting Reproducibility Contract. No standalone Reproducibility concept is introduced.

No `SYNC-16` or missing concept is justified by the replay.

## Current contraction/extension result

009-D confirms that concept optionality across the family does not weaken concept boundaries.

Removing a prerequisite forces dependent contraction; removing Generation, Constraint, Execution, or Provenance can instead be capability-only contraction when remaining family rules are satisfied.

Ordinary extension uses current concepts plus closure/side constraints. Fresh discovery remains required when new scope introduces a genuinely independent purpose/state/action lifecycle.

## Future rediscovery triggers

The catalog is not permanently frozen. Fresh Jackson-style discovery remains required before materially expanded scope such as:

- composable formal privacy/accounting;
- product-owned governance/release decisions;
- independently reusable/negotiable request or cohort definitions;
- independent synthetic-output publication/versioning/retirement/transformation lifecycle;
- arbitrary graph/recursive topology that creates independent relationship behavior beyond current structural semantics;
- product-owned economic/resource allocation/budget/quota management.

Implementation objects, IDs, tables, services, manifests or status enums do not themselves justify a concept.

## Authority rule

The individual concept specifications plus current Phase 008 normalization/consolidation authorities remain upstream of Phase 009 composition and downstream architecture.

No implementation resource or architecture dependency may redefine a concept boundary or synchronization merely because it exists.

A synchronization does not imply one package/module/service/event/transaction boundary.

## Current next boundary

**009-F — Synchronization Trigger, Preconditions/Postconditions, State Ownership & Hidden-Coordinator Audit**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
