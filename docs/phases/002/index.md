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
| **002-B** | [**Synthesis Strategy Specification & Capability Semantics**](002-B-synthesis-strategy-capability-semantics.md) | **complete** |
| **002-C** | **Learning & Learned State Specification** | **next** |
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

### 002-B

002-B deepened the canonical [Synthesis Strategy](../../concepts/synthesis-strategy.md) specification, refined core synchronization rules, and added the [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md).

Key established semantics include:

- Strategy/configuration identity and historical revision binding;
- scoped capabilities, requirements, and limitations;
- Data Meaning and Constraint capability boundaries;
- Learning-required versus direct-generation Strategies;
- material scale/resource and reproducibility declarations;
- explicit external dependency/network profiles;
- a supported no-outbound-network enterprise operating profile for core structured/tabular synthesis;
- local provision of pretrained artifacts where appropriate;
- no silent artifact download, remote fallback, or network-policy bypass;
- contextual compatibility states including limited, incompatible, and indeterminate outcomes;
- extension-author responsibility to declare material Strategy semantics/dependencies.

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
- [Design Authority](../../authority/index.md)
- [Phase 001 Exit](../001/001-H-phase-001-consolidation-initial-concept-catalog.md)

## Current next phase

**002-C — Learning & Learned State Specification**
