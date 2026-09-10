---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and refined through later explicit design authority.

The catalog remains authoritative for concept purpose, owned state/actions, lifecycle semantics, invariants and boundaries. Cross-concept coordination is authoritative under [Synchronizations](../synchronizations/index.md).

Current cross-concept state normalization is additionally governed by [Concept State, Identity, History & Invariant Normalization](state-identity-history-invariant-normalization.md).

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

Phase 008-B revalidated a distinct current problem-facing purpose for every accepted concept. Phase 008-C then normalized the state/identity/history/invariant model of all eleven without adding, removing, merging or renaming a concept.

Catalog finality is **not** yet claimed: 008-F still owns independence/genericity/familiarity and 008-G still owns deliberate deferred/rejected candidate rediscovery.

## Phase 008-C state normalization

The eleven concepts intentionally do not share one generic lifecycle. Current state-shape families are:

- reusable revisioned authorities — Data Meaning, Synthesis Strategy, Constraint, Evaluation Criterion;
- committed domain activities — Learning, Generation, Evaluation;
- durable established results — Learned State, Evidence;
- operational realization — Execution;
- typed historical relationships — Provenance.

The cross-concept normalization distinguishes lineage identity, semantic revision, activity occurrence identity, result identity and current-use/applicability status without selecting any identifier/storage technology.

It also establishes that material historical state is non-destructive, contextual compatibility/applicability remains contextual, physical durability does not establish semantic completion, and unresolved/indeterminate state remains explicit where false certainty would change behavior or historical interpretation.

Older concept wording that describes relational/time-series semantics only as future is superseded as a scope qualifier by Phase 008-B's current problem authority. The present structured-data target includes single-table, time-series and multi-table shared-key generation with legitimate composite structured topology representable. This does not create a standalone Relationship/Table/Series/Dataset/DataTopology concept or select a physical representation.

## Relationship candidate disposition

[006-G — Structured-Data Topology: Single-Table, Time-Series & Multi-Table Relationship Concept/Extensibility Audit](../phases/006/006-G-structured-data-topology-single-table-time-series-multi-table-relationship-concept-extensibility-audit.md) resolved the previously reopened `Relationship` candidate.

**Relationship is not a standalone accepted concept under the current catalog.** Material structural relationship semantics are subordinate descriptive state owned by Data Meaning under the canonical [Structured-Data Topology & Relationship Semantics Contract](../authority/structured-data-topology-relationship-semantics-contract.md).

Phase 008-C confirms only that the current state model can express those semantics. Phase 008-G must still deliberately rediscover the candidate before Phase 008 can claim individual-concept completeness.

## Historical consolidation

[002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](../phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md) confirmed that the eleven-concept model was coherent at the Phase 002 exit.

Phase 006 later revalidated that catalog against implementation-planning, recovery, runtime-distribution, scale, privacy and structured-topology evidence. Phase 008 now replays the catalog against the fuller Jackson methodology rather than treating those historical completions as final proof.

## Authority rule

These specifications, the active Phase 008-C cross-concept normalization, and active cross-cutting authority under `docs/authority/` supersede provisional concept statements under `docs/discovery/` unless later explicit design authority accepts a revision.

No Python class, Spark API, PyTorch object, storage format, job type, package module, database, function parameter, UI element, UUID scheme, manifest, event-store representation or persistence layout is implied by one concept document.

## Deferred/non-concept responsibilities

The following remain intentionally outside the accepted standalone concept catalog unless later authority changes them:

- Generation Request and Condition — subordinate to Generation;
- Attempt, Checkpoint, Retry, and cancellation realization — subordinate to Execution/domain lifecycle semantics;
- stable dataset/artifact identity — representation/integration obligation under the current model;
- reproducibility — cross-cutting [Reproducibility Contract](../authority/reproducibility-contract.md);
- lineage — derivational subset of Provenance;
- privacy objectives/guarantees — mechanism-specific future discovery; formal composable DP remains deferred and requires concept rediscovery before implementation;
- Relationship — currently Data Meaning-owned structural relationship semantics, not a standalone concept;
- Use / Release Decision — external authority boundary;
- Source Characterization/Profile — supporting observation/method;
- `GenerationMode`, `DataTopologyMode`, `Series`, `Sequence`, `TimeSeries`, `Table`, and generic `Dataset` — not accepted concepts merely because an API may select or represent single-table/time-series/multi-table behavior;
- Resource, Backpressure, Approximation, DegradedMode, Cost and Quota — cross-cutting/operational policy or owner-specific semantics rather than standalone concepts under current evidence;
- Validation, Metric, Quality, Model, Metadata, Run, Artifact, and Synthesizer — umbrella/compatibility terms that MUST NOT silently become god-concepts.

These dispositions remain subject to the explicit Phase 008-G rediscovery audit.