---
type: Architecture Index
title: SYNGAN Representation & Architecture Design
status: retained-pending-reconciliation
---

# SYNGAN Representation & Architecture Design

## Purpose

This directory preserves SYNGAN representation/architecture design downstream of concept design.

The architecture is substantial and valuable, but it is not current implementation authority and is not the next design work while the Jackson completion program remains active.

Current governing authority: [Jackson Design Completion & Implementation Hold](../authority/jackson-design-completion-implementation-hold.md).

## Current posture

```text
Jackson concept design       IN PROGRESS
Phase 008-A                  COMPLETE
Phase 008-B                  COMPLETE
Phase 008-C                  COMPLETE
Phase 008-D                  NEXT ELIGIBLE
architecture corpus          RETAINED AS DOWNSTREAM DESIGN EVIDENCE
architecture reconciliation  PLANNED FOR PHASE 013
implementation readiness     NOT READY
implementation start         NOT STARTED
implementation next          NOT YET
```

## Relationship to current concept-state authority

Phase 008-C established [Concept State, Identity, History & Invariant Normalization](../concepts/state-identity-history-invariant-normalization.md).

Where retained Phase 004/006/007 architecture uses more specific identity, revision, persistence, fencing, manifest, runtime or recovery mechanisms, those mechanisms are downstream realization hypotheses/evidence. They do not replace the normalized conceptual distinctions.

Architecture may expose a real misfit in the concept model, but it must not force concept state to mirror a preferred storage/runtime representation.

## Phase 007 architecture status

The [Phase 007 Consolidated Architecture Contract](phase-007-consolidated-architecture-contract.md) remains the strongest retained architecture synthesis through 007-J.

It remains subject to Phase 013 reconciliation after Jackson concept design is completed in Phase 012.

## Authority rule during Phases 008-012

Architecture may provide feasibility evidence, representation pressure, counterexamples and misfits. It may not veto upstream corrections; turn implementation roles into concepts; define state/actions merely because a storage/runtime model needs them; or trigger implementation while design is incomplete.

## Phase 013 obligation

After a positive Phase 012 Jackson completion decision, Phase 013 must reconcile all retained architecture with the final concept/dependence/composition/mapping/experience authority. It may retain, revise or supersede architecture, but remains design-only.

## Phase 014 gate

Only after Phase 013 may Phase 014 decide whether the whole design is complete enough for implementation readiness.

Until then:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## Current next boundary

**008-D — Concept Action, Query, Preconditions/Postconditions & Lifecycle Closure**.