---
type: Authority Index
title: SYNGAN Design Authority
status: active
---

# Design Authority

These documents define how SYNGAN design knowledge is created, interpreted, changed, and eventually implemented.

## Current methodology and governance

- [Concept Design Methodology](design-methodology.md)
- [Jackson Design Completion & Implementation Hold](jackson-design-completion-implementation-hold.md)
- [Jackson Methodology Completion Matrix](jackson-methodology-completion-matrix.md)
- [Documentation Governance](documentation-governance.md)
- [Terminology Policy](terminology-policy.md)
- [Source & Provenance Policy](source-provenance-policy.md)

## Current design authority chain

- [Problem Knowledge](../problem/index.md)
- [Accepted Concept Catalog](../concepts/index.md)
- [Phase 008 Individual-Concept Design Consolidation](../concepts/phase-008-individual-concept-consolidation.md)
- [Accepted Synchronizations](../synchronizations/index.md)
- [Concept Dependence & Application Family](../dependence/index.md)
- [009-A Inclusion-Dependence Pairwise Inventory](../dependence/inclusion-dependence-pairwise-inventory.md)

## Current posture

```text
accepted concepts          11
accepted synchronizations  15
current desired outcomes   16
Phase 008                  COMPLETE
Phase 009                  ACTIVE
009-A                      COMPLETE
009-B                      NEXT ELIGIBLE
D1                         PARTIAL — GRAPH PENDING
D2                         OPEN
D3                         OPEN
D4                         PARTIAL
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## 009-A authority result

009-A distinguishes Jackson inclusion dependence from reference/validation/production/runtime/provenance relationships and classifies all 110 directed non-self concept pairs.

```text
12 universal dependence candidates
43 conditional/disjunctive relations
55 non-dependent relations
0 insufficient relations
```

The two mutual-dependence candidates are `Learning <-> Learned State` and `Evaluation <-> Evidence`. 009-B must decide graph/cycle representation without allowing implementation structure to decide the answer.

Execution has a one-of prerequisite across `{Learning, Generation, Evaluation}` and Provenance has a non-binary subject prerequisite; these are not universal pairwise graph edges.

No concept or synchronization changed in 009-A.

## Architecture boundary

The [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md) remains downstream evidence pending Phase 013 reconciliation.

Architecture may expose a counterexample but cannot define inclusion dependence from imports, services, persistence references, transaction order, deployment topology, or runtime calls.

## Remaining design sequence

```text
009-B  dependence graph / roots / cycles / explanation ordering
009-C  application family / valid subsets
009-D  contraction / extension / add-remove consequences
009-E  synchronization inventory replay
009-F  synchronization ownership / hidden coordinator
009-G  composition economy / synergy / integrity
009-H  Phase 009 consolidation / Phase 010 handoff
010    concept mapping / interaction / language / experience
011    final concept-design quality / misfit
012    Jackson concept-design completion decision
013    representation / architecture reconciliation
014    whole-design completion / implementation-readiness decision
```

## Implementation-readiness rule

Phases 009-013 cannot make implementation ready. Only Phase 014 may set **READY / NOT STARTED / NEXT** after the whole design passes, and Phase 015 is still required before implementation begins.

## Current next boundary

**009-B — Inclusion-Dependence Graph, Roots, Cycles & Explanation Ordering**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
