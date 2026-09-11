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
- [009-B Inclusion-Dependence Graph & Ordering](../dependence/inclusion-dependence-graph-ordering.md)

## Current posture

```text
accepted concepts          11
accepted synchronizations  15
current desired outcomes   16
Phase 008                  COMPLETE
Phase 009                  ACTIVE
009-A                      COMPLETE
009-B                      COMPLETE
009-C                      NEXT ELIGIBLE
D1                         CURRENTLY CLOSED
D2                         OPEN
D3                         CURRENTLY CLOSED
D4                         PARTIAL
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Dependence result

009-A classified all 110 directed non-self concept pairs. 009-B converts the 12 universal findings into the canonical graph:

```text
9 direct universal edges
3 transitive universal findings
2 non-trivial strongly connected components
0 unresolved graph-cycle defects
```

The two strongly connected inclusion components are:

```text
{ Learning, Learned State }
{ Evaluation, Evidence }
```

They retain distinct purposes/state/action ownership and are not merge candidates merely because they are mutually required in the current application family.

The condensed universal graph is acyclic.

Execution and Provenance retain non-binary prerequisites that belong to 009-C application-family analysis rather than universal pairwise edges.

## Architecture boundary

The [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md) remains downstream evidence pending Phase 013 reconciliation.

Architecture may expose a counterexample but cannot define inclusion dependence from imports, services, persistence references, transaction order, deployment topology, runtime calls, or API nesting.

The canonical concept graph MUST NOT be mirrored mechanically into technical dependency structure.

## Remaining design sequence

```text
009-C  application family / valid subsets / minimal variants
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

**009-C — Application Family, Valid Concept Subsets & Minimal Coherent Variants**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
