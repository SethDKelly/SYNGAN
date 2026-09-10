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

Current concept-state authority:

- [Concept State, Identity, History & Invariant Normalization](../concepts/state-identity-history-invariant-normalization.md)

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
008-D                      NEXT ELIGIBLE
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Phase 008 results to date

008-A established the fuller Jackson methodology rubric, conservative completion matrix and design-only guardrails.

008-B reconciled current problem scope and established current problem/outcome → concept justification traceability.

008-C normalized all eleven concepts' state shapes, logical identity distinctions, historical immutability, current-use/applicability state, uncertainty and invariant spine without changing the catalog or selecting representation mechanisms.

The methodology matrix now marks C3 conceptual state modeling closed for this stage while C7 remains partial until 008-D closes transition/action semantics.

## Relationship to Phase 007 authority

The [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md) remains downstream design evidence pending Phase 013 reconciliation.

The historical 007-K implementation-reentry result remains superseded. Architecture may expose a concept misfit but cannot become upstream concept authority merely because it is detailed.

## Remaining design sequence

```text
008-D  Concept Action, Query, Preconditions/Postconditions & Lifecycle Closure
008-E  Operational Principle Completeness, Purpose Fulfillment & Counterexample Review
008-F  Independence, Genericity, Familiarity & Reuse Revalidation
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

**008-D — Concept Action, Query, Preconditions/Postconditions & Lifecycle Closure**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.