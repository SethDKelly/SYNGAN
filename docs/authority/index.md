---
type: Authority Index
title: SYNGAN Design Authority
status: active
---

# Design Authority

These documents define how SYNGAN design knowledge is created, interpreted, changed, and eventually implemented.

## Current methodology and governance

- [Concept Design Methodology](design-methodology.md)
- [Jackson Design Completion & Implementation Hold](jackson-design-completion-implementation-hold.md) — current delivery/design posture
- [Jackson Methodology Completion Matrix](jackson-methodology-completion-matrix.md) — current completion ledger
- [Documentation Governance](documentation-governance.md)
- [Terminology Policy](terminology-policy.md)
- [Source & Provenance Policy](source-provenance-policy.md)

Current individual-concept normalization authority:

- [Concept State, Identity, History & Invariant Normalization](../concepts/state-identity-history-invariant-normalization.md)
- [Concept Action, Query, Preconditions/Postconditions & Lifecycle Normalization](../concepts/action-query-lifecycle-normalization.md)
- [Operational Principle, Purpose Fulfillment & Counterexample Normalization](../concepts/operational-principle-purpose-counterexample-normalization.md)
- [Concept Independence, Genericity, Familiarity & Reuse Normalization](../concepts/independence-genericity-familiarity-reuse-normalization.md)

## Current posture

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
current desired outcomes   16
Phase 008                  ACTIVE
008-A                      COMPLETE
008-B                      COMPLETE
008-C                      COMPLETE
008-D                      COMPLETE
008-E                      COMPLETE
008-F                      COMPLETE
008-G                      NEXT ELIGIBLE
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Phase 008 results to date

008-A established the fuller Jackson methodology rubric, completion matrix and design-only guardrails. 008-B closed current problem/purpose justification. 008-C closed conceptual state/history/invariants. 008-D closed command/query/transition behavior. 008-E closed current operational-principle completeness.

008-F now closes accepted-concept independence and appropriate genericity, closes explicit familiarity/reuse review for individual concepts, completes C1 naming when combined with 008-B purpose closure, and closes accepted-concept boundary/non-responsibility review subject to 008-G perimeter rediscovery.

All eleven concepts and all eleven names are retained. No merge, split, addition or removal was justified by 008-F.

The remaining Phase 008 design uncertainty is the catalog perimeter: rejected, subordinated, deferred, externalized and representation-classified candidates must be deliberately rediscovered before individual-concept completeness can be decided.

## Relationship to Phase 007 authority

The [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md) remains downstream design evidence pending Phase 013 reconciliation.

The historical 007-K implementation-reentry result remains superseded. Architecture may expose a concept misfit but cannot become upstream concept authority merely because it is detailed.

## Remaining design sequence

```text
008-G  Deferred/Rejected Candidate Rediscovery, Missing-Concept & Boundary Audit
008-H  Phase 008 Consolidation & Phase 009 Handoff
009    Concept Dependence, Application Family, Composition & Synchronization Closure
010    Concept Mapping, Interaction, Linguistic & Experience Alignment
011    Specificity, Familiarity, Integrity, Synergy, Misfit & Adversarial Validation
012    Jackson Concept-Design Consolidation & Completion Decision
013    Post-Concept Representation & Architecture Reconciliation
014    Whole-Design Consolidation, Residual Debt Audit & Implementation-Readiness Decision
```

Phases 009-014 will be subdivided only immediately before they start.

## Cross-cutting authority retained

Operational-recovery, runtime-distribution, enterprise-scale, privacy/disclosure and structured-topology contracts remain useful design evidence/authority subject to correction when current Phase 008-012 concept work requires it.

## Implementation-readiness transition rule

Phases 008-013 cannot make implementation ready.

Only Phase 014 may set **READY / NOT STARTED / NEXT**, and only after the whole design passes. A positive readiness result still requires a later explicit Phase 015 before implementation begins.

## Current next boundary

**008-G — Deferred/Rejected Candidate Rediscovery, Missing-Concept & Boundary Audit**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
