---
type: Authority Index
title: SYNGAN Design Authority
status: active
---

# Design Authority

These documents define how SYNGAN design knowledge is created, interpreted, changed, and eventually implemented.

## Methodology and governance

- [Design methodology](design-methodology.md)
- [Jackson Design Completion & Implementation Hold](jackson-design-completion-implementation-hold.md) — **current delivery/design posture authority**
- [Jackson Methodology Completion Matrix](jackson-methodology-completion-matrix.md) — **current methodology completion ledger**
- [Documentation governance](documentation-governance.md)
- [Terminology policy](terminology-policy.md)
- [Source and provenance policy](source-provenance-policy.md)
- [Network and external dependency policy](network-external-dependency-policy.md)
- [Reproducibility contract](reproducibility-contract.md)

Current upstream problem authority is under [Problem Knowledge](../problem/index.md), including the Phase 008-B [Concept-Justification Traceability](../problem/concept-justification-traceability.md).

## Current posture

```text
concept / synchronization baseline   11 / 15
current desired outcomes             16
active ADRs                          10
Phase 008                            ACTIVE
008-A                                COMPLETE
008-B                                COMPLETE
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

Implementation is not an eligible next activity.

## Phase 008 methodology progress

008-A established the fuller Jackson methodology rubric, completion matrix, artifact-authority classes, J0-J7 stop/reopen rules, and design-only implementation hold.

008-B revalidated the problem/purpose/actor/outcome foundation against all eleven accepted concepts. It:

- reconciled stale topology/text scope in the problem authority;
- made single-table, time-series and multi-table shared-key generation explicit current structured-data targets;
- clarified that text-bearing structured fields are in scope through at least one self-contained source-derived/local baseline path while general unstructured/free-standing text generation remains out of scope;
- extended the desired outcome set with O15 structured-topology breadth and O16 self-contained text-bearing structured-data capability;
- established current problem/actor/outcome → concept purpose and absence-consequence traceability;
- found all eleven concepts positively justified at the purpose level without changing the catalog.

This closes methodology rows A1-A3 only. State/action/OP completeness, independence/familiarity, rejected-candidate rediscovery, inclusion dependence, mapping, integrity and final completion remain open in their assigned phases.

## Remaining design sequence

```text
008  Individual Concept Design Normalization & Completeness
009  Concept Dependence, Application Family, Composition & Synchronization Closure
010  Concept Mapping, Interaction, Linguistic & Experience Alignment
011  Specificity, Familiarity, Integrity, Synergy, Misfit & Adversarial Design Validation
012  Jackson Concept-Design Consolidation & Completion Decision
013  Post-Concept Representation & Architecture Reconciliation
014  Whole-Design Consolidation, Residual Debt Audit & Implementation-Readiness Decision
```

Each later phase is subdivided only immediately before it starts using the latest upstream evidence.

## Relationship to Phase 007 authority

The [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md) remains downstream architecture evidence unless later design supersedes part of it.

The [Phase 007 Consolidated Architecture & Implementation-Reentry Readiness Contract](phase-007-consolidated-architecture-implementation-reentry-readiness-contract.md) remains historically useful for its architecture/scaffold audit, but its implementation-reentry readiness conclusion is superseded.

## Cross-cutting authority retained

- [Operational Authority Continuity & Regressive Recovery Contract](operational-authority-continuity-regressive-recovery-contract.md)
- [Self-Contained Execution & Runtime Distribution Closure Contract](self-contained-execution-runtime-distribution-closure-contract.md)
- [Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract](enterprise-scale-resource-admission-approximation-degraded-operation-contract.md)
- [Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract](privacy-disclosure-formal-guarantee-release-boundary-contract.md)
- [Structured-Data Topology & Relationship Semantics Contract](structured-data-topology-relationship-semantics-contract.md)

These may supply design evidence but remain subject to upstream correction if Phase 008-012 changes the concept design.

## Implementation-readiness transition rule

Phases 008-013 cannot make implementation ready.

Only Phase 014 may decide the entire design complete enough to set:

```text
IMPLEMENTATION READINESS   READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NEXT
```

Even then, implementation begins only under a later explicit Phase 015 authority.

## Current next boundary

**008-C — Concept State Model, Identity, History & Invariant Normalization**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.