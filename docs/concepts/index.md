---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and refined through Phase 002.

The concept catalog is authoritative for concept purpose, owned state/actions, lifecycle semantics, invariants, and boundaries. Cross-concept coordination is authoritative under [Synchronizations](../synchronizations/index.md). Cross-cutting policy/contract authority remains under [Design Authority](../authority/index.md).

## Accepted concepts

1. [Data Meaning](data-meaning.md)
2. [Synthesis Strategy](synthesis-strategy.md)
3. [Learning](learning.md)
4. [Learned State](learned-state.md)
5. [Generation](generation.md)
6. [Constraint](constraint.md)
7. [Evaluation Criterion](evaluation-criterion.md)
8. [Evaluation](evaluation.md)
9. [Evidence](evidence.md)
10. [Execution](execution.md)
11. [Provenance](provenance.md)

## Phase 002 consolidation

[002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](../phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md) confirms that all eleven concepts remain coherent as one system after deep specification.

No concept merge, split, or additional standalone concept is required at the Phase 002 exit.

## Authority rule

These specifications supersede provisional concept statements under `docs/discovery/`. Discovery remains design history and rationale.

No Python class, Spark API, PyTorch object, storage format, job type, package module, database, or UI element is implied by one concept document.

## Deferred/non-concept responsibilities

The following remain intentionally outside the accepted standalone concept catalog:

- Generation Request and Condition — subordinate to Generation;
- Attempt, Checkpoint, Retry, and cancellation realization — subordinate to Execution/domain lifecycle semantics;
- stable dataset/artifact identity — representation/integration obligation;
- reproducibility — cross-cutting [Reproducibility Contract](../authority/reproducibility-contract.md);
- lineage — derivational subset of Provenance;
- privacy objectives/guarantees — mechanism-specific future discovery;
- Relationship — deferred relational-synthesis edge;
- Use / Release Decision — external authority boundary;
- Source Characterization/Profile — supporting observation/method;
- Validation, Metric, Quality, Model, Metadata, Run, Artifact, and Synthesizer — umbrella/compatibility terms that MUST NOT silently become god-concepts.
