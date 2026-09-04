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
| **002-C** | [**Learning & Learned State Specification**](002-C-learning-learned-state-specification.md) | **complete** |
| **002-D** | **Generation Specification, Request/Condition Semantics & Output Completion** | **next** |
| 002-E | Evaluation Criterion, Evaluation & Evidence Specification | planned |
| 002-F | Execution, Attempt History, Failure & Recovery Semantics | planned |
| 002-G | Provenance, Reproducibility Contract & Historical Binding Specification | planned |
| 002-H | Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review | planned |

## Completed refinement

### 002-A

002-A deepened [Data Meaning](../../concepts/data-meaning.md) and [Constraint](../../concepts/constraint.md), establishing revisioned semantic/rule authority, explicit unresolved state, contextual applicability, handling-versus-satisfaction, and control-plane scale semantics.

### 002-B

002-B deepened [Synthesis Strategy](../../concepts/synthesis-strategy.md) and established the [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md), including explicit capability/requirement/limitation semantics and an offline/no-egress core operating profile.

### 002-C

002-C deepened [Learning](../../concepts/learning.md) and [Learned State](../../concepts/learned-state.md) and refined the [core synchronizations](../../synchronizations/core-synchronizations.md).

Key established semantics include:

- Learning exists only when reusable source-derived state is actually part of Strategy intent;
- explicit Learning semantic commitment and stable source-history binding;
- retries/Attempts preserve committed Learning semantics;
- Execution completion is not Learning completion;
- checkpoints/intermediates are not Learned State by durability alone;
- one Learning produces zero or one primary logical Learned State under the current model;
- Learned State is a logical durable result that may be physically composite/distributed;
- Learned State compatibility is contextual to Generation rather than global mutable state;
- ordinary reuse is non-mutating;
- base/pretrained artifact dependencies remain explicit;
- Learned State is potentially sensitive and is not presumed private or release-safe.

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

**002-D — Generation Specification, Request/Condition Semantics & Output Completion**
