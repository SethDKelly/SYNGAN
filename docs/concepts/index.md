---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and refined through later explicit design authority.

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

The accepted catalog remains **eleven concepts**.

[006-G — Structured-Data Topology: Single-Table, Time-Series & Multi-Table Relationship Concept/Extensibility Audit](../phases/006/006-G-structured-data-topology-single-table-time-series-multi-table-relationship-concept-extensibility-audit.md) resolved the previously reopened `Relationship` candidate.

**Relationship is not a standalone accepted concept.** Material structural relationship semantics are subordinate descriptive state owned by Data Meaning under the canonical [Structured-Data Topology & Relationship Semantics Contract](../authority/structured-data-topology-relationship-semantics-contract.md).

This means synthesis-relevant semantics such as shared-key correspondence, series/entity membership and temporal/order roles remain explicit, inspectable and historically bound without duplicating Data Meaning's declaration/revision/authority lifecycle in a twelfth concept.

## Phase 002 consolidation

[002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](../phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md) confirmed that the eleven-concept model was coherent at the Phase 002 exit.

Phase 006 later revalidated that catalog against implementation-planning, recovery, runtime-distribution, scale, privacy and structured-topology evidence. 006-G retained the same concept count after deliberate Relationship rediscovery.

## Authority rule

These specifications plus active cross-cutting authority under `docs/authority/` supersede provisional concept statements under `docs/discovery/` unless later explicit design authority accepts a revision.

No Python class, Spark API, PyTorch object, storage format, job type, package module, database, function parameter, or UI element is implied by one concept document.

## Deferred/non-concept responsibilities

The following remain intentionally outside the accepted standalone concept catalog unless later authority changes them:

- Generation Request and Condition — subordinate to Generation;
- Attempt, Checkpoint, Retry, and cancellation realization — subordinate to Execution/domain lifecycle semantics;
- stable dataset/artifact identity — representation/integration obligation;
- reproducibility — cross-cutting [Reproducibility Contract](../authority/reproducibility-contract.md);
- lineage — derivational subset of Provenance;
- privacy objectives/guarantees — mechanism-specific future discovery; formal composable DP is deferred and requires concept rediscovery before implementation;
- **Relationship — resolved by 006-G as Data Meaning-owned structural relationship semantics, not a standalone concept**;
- Use / Release Decision — external authority boundary;
- Source Characterization/Profile — supporting observation/method;
- `GenerationMode`, `DataTopologyMode`, `Series`, `Sequence`, `TimeSeries`, `Table`, and generic `Dataset` — not accepted concepts merely because an API may select single-table/time-series/multi-table behavior;
- Resource, Backpressure, Approximation, DegradedMode, Cost and Quota — cross-cutting/operational policy or owner-specific semantics rather than standalone concepts under current evidence;
- Validation, Metric, Quality, Model, Metadata, Run, Artifact, and Synthesizer — umbrella/compatibility terms that MUST NOT silently become god-concepts.
