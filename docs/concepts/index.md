---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and normalized through Phase 008.

Cross-concept coordination is governed by [Synchronizations](../synchronizations/index.md); inclusion dependence/application-family authority is governed by [Concept Dependence & Application Family](../dependence/index.md).

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
E1-E5                                CURRENTLY CLOSED
```

No Phase 009 subgroup through 009-G finds a reason to add, remove, merge, split, or rename a concept.

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

Generation owns request/Condition and candidate-to-completed logical output semantics. Relationship remains Data Meaning-owned descriptive structure. Generic Privacy remains rejected pending fresh mechanism-specific discovery. Use/Release Decision remains external authority.

## Application-family result

Canonical kernels remain:

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Reusable authority-only family members include Data Meaning, Synthesis Strategy, Constraint and Evaluation Criterion independently.

Execution is valid only with at least one Learning/Generation/Evaluation activity. Provenance is valid only with a meaningful provenance-bearing relationship/history witness.

## Current synchronization result

```text
required-relational active rules      6
conditional active rules              7
retired concept-local                 SYNC-08
reclassified cross-cutting contract   SYNC-15
new synchronization                   NONE
SYNC-16                               NOT JUSTIFIED
```

`SYNC-08` retirement reinforces the existing boundary that synthetic output is Generation-owned result state, not an independent Output concept.

`SYNC-15` reclassification reinforces the existing boundary that Reproducibility is a cross-cutting contract, not an independent concept.

`SYNC-06` is conditional Generation/Learned State reuse, not a general Generation umbrella.

## Composition economy and integrity result

009-G finds no reason to merge concepts merely because synchronizations share patterns.

Examples:

- `SYNC-04/07/11` remain distinct because Learning, Generation and Evaluation have different semantic completion contracts; their common Execution pattern does not justify a generic Activity concept.
- `SYNC-05/12` remain distinct because Learned State and Evidence have different purposes/cardinalities/lifecycles; their common activity/result shape does not justify a generic Artifact concept.
- `SYNC-09/10` remain distinct because Criterion binding and method sufficiency are different Evaluation actions.

Synchronization is occurrence-scoped, not a permanent reactive subscription. Later changes to a bound concept do not silently rewrite historical activity state.

The current composition also demonstrates positive synergy without purpose collapse:

```text
Learning -> Learned State -> Generation
evidence-gated Generation
Constraint + Evaluation/Evidence + Generation
shared Execution operational lifecycle
exact bindings + Provenance
direct + learned Generation variants
```

No hidden Compatibility, Workflow/Run, Artifact/Promotion, Approval/Quality, Reproducibility, or Composition concept is required.

## Future rediscovery triggers

The catalog is not permanently frozen. Fresh Jackson-style discovery remains required before materially expanded scope such as:

- composable formal privacy/accounting;
- product-owned governance/release decisions;
- independently reusable/negotiable request or cohort definitions;
- independent synthetic-output publication/versioning/retirement/transformation/current-use lifecycle;
- arbitrary graph/recursive topology that creates independent relationship behavior beyond current structural semantics;
- product-owned economic/resource allocation/budget/quota management.

009-G specifically preserves the independent-output-lifecycle trigger rather than inventing retroactive `Evidence -> completed Generation` mutation when later Evidence becomes stale/invalidated.

Implementation objects, IDs, tables, services, manifests or status enums do not themselves justify a concept.

## Authority rule

No implementation resource or architecture dependency may redefine concept boundaries or synchronization merely because it exists.

Similarity of implementation mechanics does not justify concept merger; similarity of synchronization pattern does not justify an umbrella concept.

## Current next boundary

**009-H — Phase 009 Consolidation, Dependence/Composition Completion Decision & Phase 010 Handoff**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
