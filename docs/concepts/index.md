---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and refined through Phase 002.

The catalog remains authoritative for concept purpose, owned state/actions, lifecycle semantics, invariants and boundaries. Cross-concept coordination is authoritative under [Synchronizations](../synchronizations/index.md).

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

## Current concept count

The accepted catalog currently remains **eleven concepts**.

[006-A — Post-Planning Concept Completeness, Mechanism-vs-Concept & Scope-Boundary Revalidation](../phases/006/006-A-post-planning-concept-completeness-mechanism-vs-concept-scope-boundary-revalidation.md) did not accept a new concept. It did, however, reopen the previously deferred **Relationship** candidate for deliberate Phase 006-G discovery because multi-table shared-key generation supplies new evidence of reusable descriptive linkage, while time-series generation supplies a test of whether the same boundary can express sequence membership/order generically.

Until a later Phase 006 authority explicitly accepts a change, `Relationship` remains provisional discovery evidence and MUST NOT be treated as part of the accepted catalog.

## Phase 002 consolidation

[002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](../phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md) confirmed that all eleven concepts were coherent as one system at the Phase 002 exit.

Phase 006 does not invalidate that historical exit. It reopens candidate discovery only where later implementation-planning and capability evidence justifies revalidation under the project's methodology.

## Authority rule

These specifications supersede provisional concept statements under `docs/discovery/` unless later explicit design authority accepts a revision.

No Python class, Spark API, PyTorch object, storage format, job type, package module, database, function parameter, or UI element is implied by one concept document.

## Deferred/non-concept responsibilities

The following remain intentionally outside the accepted standalone concept catalog unless later authority changes them:

- Generation Request and Condition — subordinate to Generation;
- Attempt, Checkpoint, Retry, and cancellation realization — subordinate to Execution/domain lifecycle semantics;
- stable dataset/artifact identity — representation/integration obligation;
- reproducibility — cross-cutting [Reproducibility Contract](../authority/reproducibility-contract.md);
- lineage — derivational subset of Provenance;
- privacy objectives/guarantees — mechanism-specific future discovery;
- **Relationship — reopened Phase 006 candidate, not yet accepted**;
- Use / Release Decision — external authority boundary;
- Source Characterization/Profile — supporting observation/method;
- `GenerationMode`, `DataTopologyMode`, `Series`, `Table`, and generic `Dataset` — not accepted concepts merely because an API may select single-table/time-series/multi-table behavior;
- Validation, Metric, Quality, Model, Metadata, Run, Artifact, and Synthesizer — umbrella/compatibility terms that MUST NOT silently become god-concepts.
