---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and refined through current Phase 008 authority.

Cross-concept coordination remains authoritative under [Synchronizations](../synchronizations/index.md), with current dependence/composition work governed by [Phase 009](../phases/009/index.md).

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

## Phase 008 completion result

```text
accepted concepts          11
accepted synchronizations  15
restored concepts           0
new concepts                0
removed concepts            0
renamed concepts            0
merged concepts             0
split concepts              0
missing current concept     NONE FOUND
INDIVIDUAL CONCEPT DESIGN   COMPLETE ENOUGH FOR PHASE 009
```

No unresolved J1 local concept-specification defect or J2 purpose/boundary/catalog defect remained at the Phase 008 exit.

This is not a claim that Jackson concept design is complete. Phase 009 is now active and must derive inclusion dependence/application-family structure and close composition/synchronization against that structure.

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

Generation currently owns request/Condition and candidate-to-completed logical output semantics. A separate Output concept is not justified under current scope.

Relationship remains Data Meaning-owned descriptive structural semantics; prescriptive referential/cardinality/temporal validity remains Constraint; request-specific topology scope/horizon/quantity remains Generation.

## Current non-concept dispositions

The following remain intentionally outside the standalone catalog under current evidence:

- Generation Request and Condition — Generation-owned;
- Attempt and Checkpoint — Execution-owned/subordinate;
- Artifact/Dataset identity — representation/integration;
- reproducibility — cross-cutting contract;
- generic Privacy — rejected; future mechanism-specific discovery required where independent state/actions arise;
- Relationship — Data Meaning-owned descriptive semantics;
- Use / Release Decision — external authority;
- Source Characterization/Profile — supporting observation/method;
- Resource/Admission/Backpressure/Approximation/DegradedMode/Cost — owner-specific, cross-cutting, operational or deployment policy;
- Source/Dependency/Authorization/Secret/Platform Capability — referenced context, security authority or architecture;
- TimeSeries/Series/Sequence/Table/Text/Tokenizer/Language Model/GenerationMode/DataTopologyMode — vocabulary or representation, not current concepts;
- Metadata/Model/Run/Quality/Validation/Synthesizer/Artifact/Policy — umbrella terms that must not erase accepted boundaries.

## Future rediscovery triggers

The catalog is not permanently frozen. Fresh Jackson-style discovery is required before implementing materially expanded scope such as composable formal privacy/accounting, product-owned governance/release decisions, reusable request/cohort definitions, independent output lifecycle, arbitrary graph/recursive topology, or product-owned economic/resource management.

## Phase 009 handoff rule

Phase 009 must preserve the Phase 008 individual-concept boundaries while asking a different question: which accepted concepts require which others to be included for their **application purpose** to make sense?

Reference, validation, production, runtime and provenance relations do not answer that question automatically.

The current fifteen synchronization IDs are starting composition evidence, not a final Phase 009 result.

## Authority rule

The individual concept specifications plus the current Phase 008 normalization/consolidation authorities supersede provisional statements under `docs/discovery/` unless later explicit design authority accepts a revision.

No Python class, Spark API, storage format, package module, database, UI element, UUID scheme, manifest, fence, dependency record, credential, report or persistence layout becomes concept authority merely because a concept needs representation later.

## Current next boundary

**009-A — Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
