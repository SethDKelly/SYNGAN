---
type: Architecture Index
title: SYNGAN Representation & Architecture Design
status: retained-pending-reconciliation
---

# SYNGAN Representation & Architecture Design

## Purpose

This directory preserves SYNGAN representation/architecture design downstream of concept design.

The architecture is substantial and remains valuable, but it is **not the current next work** and is not implementation authority while the Jackson design-completion program is active.

Current governing authority: [Jackson Design Completion & Implementation Hold](../authority/jackson-design-completion-implementation-hold.md).

## Current posture

```text
Jackson concept design     IN PROGRESS
architecture corpus        RETAINED AS DOWNSTREAM DESIGN EVIDENCE
architecture reconciliation PLANNED FOR PHASE 013
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Phase 007 architecture status

The [Phase 007 Consolidated Architecture Contract](phase-007-consolidated-architecture-contract.md) remains the strongest current architecture synthesis of the work completed through 007-J.

Detailed authorities remain available for:

- identity/revision/reference/view semantics;
- persistence/concurrency/durable coordination/history;
- distributed data state, topology, manifests and candidate/seal/promotion;
- Strategy/method versus executable/dependency/runtime realization;
- trust, authorization, secrets, network/egress and worker closure;
- Execution/Attempt, idempotency, fencing, recovery, checkpoint, cancellation and admission;
- Evaluation/Evidence, Provenance, historical query, reproducibility and disclosure;
- implementation-proof/claim boundaries.

This architecture does not prove completion of the upstream concept design.

## Authority rule during Phases 008-012

Architecture may provide:

- feasibility evidence;
- examples of representation pressure;
- counterexamples and misfits;
- evidence that a conceptual distinction needs stronger specification;
- evidence that an earlier representation assumption is too narrow.

Architecture may not:

- veto a concept correction because code/tests/docs already assume the old shape;
- turn implementation roles into concepts by convenience;
- define concept state/actions merely because a storage/runtime model needs them;
- make a package/service/object boundary into conceptual authority;
- trigger implementation work while design is incomplete.

If Phase 008-012 changes upstream design, affected architecture becomes pending reconciliation rather than forcing the concept model backward.

## Phase 013 obligation

After Phase 012 positively closes Jackson concept design, **Phase 013 — Post-Concept Representation & Architecture Reconciliation** must review the architecture against the final concept/dependence/composition/mapping/experience authority.

Phase 013 may:

- retain architecture unchanged where it still fits;
- revise or supersede representation choices that conflict with completed concept design;
- close representation-level alternatives and residual design debt;
- update ADR status/rationale where required.

Phase 013 remains design-only and cannot make implementation ready by itself.

## Phase 014 whole-design gate

Only after Phase 013 reconciliation may Phase 014 decide whether the entire design is complete and remaining uncertainty is implementation-specific.

Until that gate passes:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## Current next boundary

**008-A — Methodology Authority Reset, Completion Matrix & Design-Only Guardrails**.