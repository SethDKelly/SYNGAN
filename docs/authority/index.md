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
- [Documentation governance](documentation-governance.md)
- [Terminology policy](terminology-policy.md)
- [Source and provenance policy](source-provenance-policy.md)
- [Network and external dependency policy](network-external-dependency-policy.md)
- [Reproducibility contract](reproducibility-contract.md)

## Current posture

```text
concept / synchronization baseline   11 / 15
active ADRs                          10
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

The repository is back in deliberate design completion. Implementation is not an eligible next activity.

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

Each later phase must be subdivided only when it becomes next, using the latest upstream design evidence.

## Relationship to Phase 007 authority

The [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md) remains current downstream architecture evidence unless later design supersedes part of it.

The [Phase 007 Consolidated Architecture & Implementation-Reentry Readiness Contract](phase-007-consolidated-architecture-implementation-reentry-readiness-contract.md) remains historically useful for its architecture/scaffold audit, but its **implementation-reentry readiness conclusion is superseded** by the Jackson Design Completion & Implementation Hold.

The supersession is methodological: 007-K showed that the then-current architecture was coherent enough for engineering re-entry, but it did not prove completion of the fuller Jackson design program.

## Cross-cutting authority retained

- [Operational Authority Continuity & Regressive Recovery Contract](operational-authority-continuity-regressive-recovery-contract.md)
- [Self-Contained Execution & Runtime Distribution Closure Contract](self-contained-execution-runtime-distribution-closure-contract.md)
- [Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract](enterprise-scale-resource-admission-approximation-degraded-operation-contract.md)
- [Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract](privacy-disclosure-formal-guarantee-release-boundary-contract.md)
- [Structured-Data Topology & Relationship Semantics Contract](structured-data-topology-relationship-semantics-contract.md)

These are subject to upstream correction if Phase 008-012 changes the concept design they depend upon.

## Implementation-readiness transition rule

Phases 008-013 cannot make implementation ready.

Only Phase 014 may decide that the entire design is complete. If it passes, it may set:

```text
READY / NOT STARTED / NEXT
```

A positive readiness decision still does not authorize code; it only makes a future explicit implementation-authority phase eligible.

## Current next boundary

**008-A — Methodology Authority Reset, Completion Matrix & Design-Only Guardrails**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.