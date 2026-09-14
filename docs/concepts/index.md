---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and normalized through Phase 008.

Cross-concept dependence/composition is consolidated by [Phase 009 Dependence, Application Family & Composition Consolidation](../authority/phase-009-dependence-composition-consolidation.md). Current mapping work is governed by [Concept Mapping Authority](../mapping/index.md) and the [010-A Mapping Control Authority](../mapping/mapping-authority-coverage-actor-surface-evidence-baseline.md).

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
Phase 010                            ACTIVE
010-A                                COMPLETE
010-B                                NEXT ELIGIBLE
```

Phase 009 found no reason to add, remove, merge, split, or rename a concept. 010-A likewise finds no mapping-foundation evidence requiring catalog change.

## Core boundaries mapping must preserve

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

## Current mapping source status

010-A identifies action/query/state sources for all eleven concepts without claiming they are already mapped.

Current status:

```text
Data Meaning          SOURCE IDENTIFIED
Synthesis Strategy    SOURCE IDENTIFIED
Learning              SOURCE IDENTIFIED
Learned State         SOURCE IDENTIFIED
Generation            SOURCE IDENTIFIED
Constraint            SOURCE IDENTIFIED
Evaluation Criterion  SOURCE IDENTIFIED
Evaluation            SOURCE IDENTIFIED
Evidence              SOURCE IDENTIFIED
Execution             SOURCE IDENTIFIED
Provenance            SOURCE IDENTIFIED
```

010-B must advance normalized **state-changing actions** to `SEMANTICALLY MAPPED` only after actor intent, family applicability, semantic preconditions/results and relevant history/disclosure/scale constraints are explicit.

010-C separately owns query/state/history inspection mapping.

## Application-family result

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Direct Generation remains valid without Learning/Learned State. Evaluation/Evidence are not universal prerequisites for Generation. Constraint, Execution and Provenance remain capability-conditional.

010-A preserves that optionality through explicit mapping applicability tags rather than one mandatory workflow.

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

## Mapping misfit rule

If an action/query/state cannot be mapped intelligibly without violating purpose/boundaries, Phase 010 must record a concrete misfit and reopen the smallest affected authority when warranted.

Do not create a new concept merely because:

- several actions share a UI/API interaction pattern;
- several views share a status label;
- several concepts appear on one dashboard/report;
- one physical resource contains state from several concepts;
- one actor wants a cross-concept workflow summary.

## Future rediscovery triggers

Fresh discovery remains required before materially expanded scope such as:

- composable formal privacy/accounting;
- product-owned governance/release decisions;
- independently reusable/negotiable request or cohort definitions;
- independent synthetic-output publication/versioning/retirement/transformation/current-use lifecycle;
- arbitrary graph/recursive topology with independent relationship behavior;
- product-owned economic/resource allocation/budget/quota management.

Implementation objects, IDs, tables, services, manifests or status enums do not themselves justify a concept.

## Current next boundary

**010-B — Concept Action → Actor Intent & Interaction Mapping** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
