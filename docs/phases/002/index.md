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
| **002-D** | [**Generation Specification, Request/Condition Semantics & Output Completion**](002-D-generation-request-condition-output-completion.md) | **complete** |
| **002-E** | [**Evaluation Criterion, Evaluation & Evidence Specification**](002-E-evaluation-criterion-evaluation-evidence-specification.md) | **complete** |
| **002-F** | [**Execution, Attempt History, Failure & Recovery Semantics**](002-F-execution-attempt-failure-recovery-semantics.md) | **complete** |
| **002-G** | [**Provenance, Reproducibility Contract & Historical Binding Specification**](002-G-provenance-reproducibility-historical-binding-specification.md) | **complete** |
| **002-H** | **Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review** | **next** |

## Completed refinement

### 002-A

002-A deepened [Data Meaning](../../concepts/data-meaning.md) and [Constraint](../../concepts/constraint.md), establishing revisioned semantic/rule authority, explicit unresolved state, contextual applicability, handling-versus-satisfaction, and control-plane scale semantics.

### 002-B

002-B deepened [Synthesis Strategy](../../concepts/synthesis-strategy.md) and established the [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md), including explicit capability/requirement/limitation semantics and an offline/no-egress core operating profile.

### 002-C

002-C deepened [Learning](../../concepts/learning.md) and [Learned State](../../concepts/learned-state.md), establishing semantic commitment/source-history binding, retry invariance, checkpoint-versus-Learned-State separation, distributed/composite learned-state semantics, non-mutating reuse, and sensitivity/dependency boundaries.

### 002-D

002-D deepened [Generation](../../concepts/generation.md), establishing request/Condition commitment, direct and Learned-State paths, required Constraint completion rules, candidate-versus-completed output, and a semantic completion barrier distinct from physical materialization or Execution completion.

### 002-E

002-E deepened [Evaluation Criterion](../../concepts/evaluation-criterion.md), [Evaluation](../../concepts/evaluation.md), and [Evidence](../../concepts/evidence.md), establishing question/method/finding separation, explicit evidence strength, uncertainty-aware evaluation, and Generation-completion validation semantics.

### 002-F

002-F deepened [Execution](../../concepts/execution.md), establishing logical Execution/Attempt identity, retry/resume/checkpoint safety, partial/unknown operational state, cancellation races, contextual retryability, and single semantic promotion rather than exactly-once physical computation.

### 002-G

002-G deepened [Provenance](../../concepts/provenance.md), refined the [core synchronizations](../../synchronizations/core-synchronizations.md), clarified documentation-source provenance, and established the canonical [Reproducibility Contract](../../authority/reproducibility-contract.md).

Key established semantics include:

- Provenance owns typed historical relationships and stable references rather than duplicate concept payloads;
- mutable aliases such as table names, model aliases, URLs, service names, or platform run IDs are insufficient identity by themselves when underlying state can change materially;
- committed historical bindings remain tied to the exact source/meaning/Strategy/Constraint/Learned State/Condition/Criterion/method/dependency state actually used;
- lineage remains the derivational subset of broader Provenance;
- canonical Provenance remains materiality-bounded and does not become a copy of rows, model state, task telemetry, or complete logs;
- provenance correction preserves auditability and cannot silently rewrite another concept's authority;
- reproducibility remains a cross-cutting contract rather than a standalone concept;
- substantive reproducibility claims must identify target, preserved conditions, and acceptable equivalence;
- exact deterministic, semantic, statistical, bounded/approximate, comparative, and explicitly insufficient/not-reproducible outcomes remain distinguishable;
- seeds alone do not imply deterministic reproduction;
- retry/recovery facts enter the reproduction context only when materially behavior-affecting;
- external artifact/service mutability constrains claim strength and must remain explicit;
- loss of historical dependencies may weaken present reproducibility without rewriting historical provenance;
- enterprise-scale provenance/reproduction does not require full corpus/output/model/log collection to driver-local memory.

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
- [Reproducibility Contract](../../authority/reproducibility-contract.md)
- [Phase 001 Exit](../001/001-H-phase-001-consolidation-initial-concept-catalog.md)

## Current next phase

**002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review**
