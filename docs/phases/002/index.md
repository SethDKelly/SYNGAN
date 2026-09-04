---
type: Phase Index
title: Phase 002 — Concept Specification & Invariant Refinement
status: active
---

# Phase 002 — Concept Specification & Invariant Refinement

Phase 002 deepens the accepted Phase 001 concept model before experience/API/representation architecture is selected.

The grouping follows accepted concept responsibilities rather than implementation technology.

## Groups

| Group | Scope | Status |
|---|---|---|
| **002-A** | [**Data Meaning & Constraint Specification**](002-A-data-meaning-constraint-specification.md) | **complete** |
| **002-B** | **Synthesis Strategy Specification & Capability Semantics** | **next** |
| 002-C | Learning & Learned State Specification | planned |
| 002-D | Generation Specification, Request/Condition Semantics & Output Completion | planned |
| 002-E | Evaluation Criterion, Evaluation & Evidence Specification | planned |
| 002-F | Execution, Attempt History, Failure & Recovery Semantics | planned |
| 002-G | Provenance, Reproducibility Contract & Historical Binding Specification | planned |
| 002-H | Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review | planned |

## Completed refinement

### 002-A

002-A deepened the canonical [Data Meaning](../../concepts/data-meaning.md) and [Constraint](../../concepts/constraint.md) specifications and refined the [core synchronization rules](../../synchronizations/core-synchronizations.md).

Key established semantics include:

- explicit semantic assertions and unresolved meaning;
- declared versus inferred authority;
- revisioned historical binding;
- material inference visibility before commitment;
- contextual Constraint applicability;
- activity-owned rule handling disposition;
- separation of handling from actual satisfaction;
- conflict/satisfiability uncertainty;
- control-plane state that does not scale with row count by default.

## Phase 002 boundary

Phase 002 SHOULD specify concept state, actions, invariants, lifecycle semantics, authority, revision/history rules, failure behavior, and accepted synchronization refinements.

It MUST NOT prematurely select:

- Python class/module hierarchy;
- Spark ML Estimator/Model mappings;
- PyTorch/TorchDistributor architecture;
- storage/serialization formats;
- plugin architecture;
- managed-platform requirements;
- final public API ergonomics.

Those remain downstream unless concept feasibility requires an explicit earlier design revision.

## Entry authority

- [Accepted Concepts](../../concepts/index.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Phase 001 Exit](../001/001-H-phase-001-consolidation-initial-concept-catalog.md)

## Current next phase

**002-B — Synthesis Strategy Specification & Capability Semantics**
