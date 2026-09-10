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
Jackson concept design       IN PROGRESS
architecture corpus          RETAINED AS DOWNSTREAM DESIGN EVIDENCE
architecture reconciliation  PLANNED FOR PHASE 013
implementation readiness     NOT READY
implementation start         NOT STARTED
implementation next          NOT YET
```

## Phase 008-B problem-scope consequence

008-B updated upstream problem authority to make the current structured-data target explicit:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

with legitimate composite topology remaining representable, plus at least one self-contained source-derived/local capability for free-form/source-language text fields inside structured data.

These upstream scope statements do **not** cause immediate architecture changes. Existing Phase 004/006/007 architecture remains retained evidence and will be reconciled as a whole in Phase 013 after Jackson concept design closes.

If Phase 008-012 changes concept boundaries or semantics, affected architecture must follow the upstream design rather than constraining it.

## Phase 007 architecture status

The [Phase 007 Consolidated Architecture Contract](phase-007-consolidated-architecture-contract.md) remains the strongest current architecture synthesis of work through 007-J.

Detailed authorities remain available for identity/revision/reference/view semantics; persistence/concurrency/history; distributed data/topology/manifests/promotion; Strategy/runtime realization; trust/security/network/worker closure; Execution/recovery; Evaluation/Evidence/Provenance/history/reproducibility/disclosure; and proof/claim boundaries.

This architecture does not prove completion of upstream concept design.

## Authority rule during Phases 008-012

Architecture may provide feasibility evidence, representation pressure, counterexamples, and misfits. It may not veto an upstream concept correction because existing code/tests/docs assume an older shape, define concept state/actions from storage/runtime convenience, turn package/service/object boundaries into concepts, or trigger implementation while design is incomplete.

## Phase 013 obligation

After Phase 012 positively closes Jackson concept design, **Phase 013 — Post-Concept Representation & Architecture Reconciliation** must review this architecture against the final concept/dependence/composition/mapping/experience authority.

Phase 013 may retain compatible architecture, revise/supersede incompatible representation choices, close representation alternatives, and update ADR status/rationale where required. It remains design-only and cannot make implementation ready by itself.

## Phase 014 whole-design gate

Only after Phase 013 reconciliation may Phase 014 decide whether the entire design is complete and remaining uncertainty is implementation-specific.

Until that gate passes:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## Current next boundary

**008-C — Concept State Model, Identity, History & Invariant Normalization**.