---
type: Architecture Index
title: SYNGAN Representation & Architecture Design
status: retained-pending-reconciliation
---

# SYNGAN Representation & Architecture Design

## Purpose

Preserve SYNGAN representation/architecture design as downstream evidence while Jackson concept design remains active.

Current governing authority: [Jackson Design Completion & Implementation Hold](../authority/jackson-design-completion-implementation-hold.md).

## Current posture

```text
Jackson concept design       IN PROGRESS
Phase 008                    COMPLETE
Phase 009                    ACTIVE
009-A                        COMPLETE
009-B                        NEXT ELIGIBLE
architecture corpus          RETAINED AS DOWNSTREAM DESIGN EVIDENCE
architecture reconciliation  PLANNED FOR PHASE 013
implementation readiness     NOT READY
implementation start         NOT STARTED
implementation next          NOT YET
```

## Dependence boundary

The current [009-A Inclusion-Dependence Pairwise Inventory](../dependence/inclusion-dependence-pairwise-inventory.md) is upstream of architecture.

Architecture must not reinterpret Jackson inclusion dependence from:

- package/module imports;
- foreign keys or object references;
- dataflow/service-call direction;
- transaction ordering;
- runtime scheduler dependencies;
- deployment topology;
- platform capability requirements;
- existing API nesting.

009-A finds only 12 universal pairwise inclusion candidates across 110 directed non-self pairs, substantially fewer than the historical runtime/reference dependency relationships.

The two pairwise mutual-dependence candidates—`Learning <-> Learned State` and `Evaluation <-> Evidence`—remain 009-B design questions. Architecture cannot resolve those cycles by collapsing concepts or choosing representation convenience.

Execution's one-of prerequisite across `{Learning, Generation, Evaluation}` and Provenance's non-binary subject prerequisite must likewise not be converted into false mandatory architecture edges.

## Phase 007 architecture status

The [Phase 007 Consolidated Architecture Contract](phase-007-consolidated-architecture-contract.md) remains the strongest retained architecture synthesis through 007-J.

It remains subject to Phase 013 reconciliation after Jackson concept design is completed in Phase 012.

## Authority rule during Phases 009-012

Architecture may provide feasibility evidence, representation pressure, counterexamples and misfits. It may not veto upstream corrections, turn implementation roles into concepts, define inclusion dependence from runtime/module structure, or trigger implementation while design is incomplete.

## Phase 013 obligation

After a positive Phase 012 Jackson completion decision, Phase 013 must reconcile retained architecture with final concept/dependence/composition/mapping authority.

## Phase 014 gate

Only after Phase 013 may Phase 014 decide implementation readiness.

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## Current next boundary

**009-B — Inclusion-Dependence Graph, Roots, Cycles & Explanation Ordering**.
