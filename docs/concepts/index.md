---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and refined through later explicit design authority.

The catalog remains authoritative for concept purpose, owned state/actions, lifecycle semantics, invariants and boundaries. Cross-concept coordination is authoritative under [Synchronizations](../synchronizations/index.md).

Current cross-concept normalization is governed by:

- [Concept State, Identity, History & Invariant Normalization](state-identity-history-invariant-normalization.md);
- [Concept Action, Query, Preconditions/Postconditions & Lifecycle Normalization](action-query-lifecycle-normalization.md);
- [Operational Principle, Purpose Fulfillment & Counterexample Normalization](operational-principle-purpose-counterexample-normalization.md);
- [Concept Independence, Genericity, Familiarity & Reuse Normalization](independence-genericity-familiarity-reuse-normalization.md).

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

Phase 008-B revalidated a distinct current problem-facing purpose for every accepted concept. Phase 008-C normalized state/identity/history/invariants. Phase 008-D normalized actions, queries, contextual-assessment ownership and lifecycle transitions. Phase 008-E revalidated each operational principle. Phase 008-F now revalidates independence, bounded genericity, familiarity/naming and conceptual reuse for every accepted concept.

No concept has been added, removed, merged, split or renamed through 008-F.

Catalog finality is **not** yet claimed: 008-G still owns deliberate deferred/rejected candidate rediscovery and missing-concept/perimeter-boundary review; 008-H owns Phase 008 consolidation.

## Current individual-concept closure

The current catalog now has dedicated present-state authority for:

```text
purpose / justification               008-B
state / identity / history / invariants 008-C
actions / queries / transitions       008-D
operational principles / counterexamples 008-E
independence / genericity / familiarity / reuse 008-F
```

These are individual-concept results only. Jackson inclusion dependence, application family, final composition/synchronization, mapping and final whole-concept quality remain later work.

## Phase 008-F independence and familiarity result

008-F explicitly distinguishes:

```text
independence != isolation
reuse        != universal presence
familiarity  != copying a neighboring object model
genericity   != generic infrastructure
```

All eleven concepts pass current independence review. Creation or synchronization relationships do not collapse purpose/state ownership: Learning and Learned State remain activity/result; Evaluation and Evidence remain examination/finding; Execution remains operational realization rather than domain completion; Provenance remains typed historical-relationship authority despite high fan-in.

All eleven concepts are generic enough for the current product variation while remaining bounded to synthetic-data purposes. They do not become enterprise-wide metadata, workflow, policy, artifact, model-registry, evidence, observability or lineage systems.

All eleven names are retained after explicit familiarity review. Several familiar alternatives remain intentionally non-canonical because they would import misleading assumptions:

- `Schema` / `Metadata` for Data Meaning;
- `Synthesizer` / `Algorithm` for Synthesis Strategy;
- `Training` / `Fit` for Learning;
- `Model` / `Artifact` for Learned State;
- `Sampling` for Generation;
- `Metric` for Evaluation Criterion;
- `Validation` for Evaluation;
- `Result` for Evidence;
- `Run` / `Job` for Execution;
- `Lineage` for Provenance.

Those terms may still appear in future concept mappings or compatibility surfaces where their local meaning is clear, but they cannot silently redefine the accepted concepts.

## Current topology/text interpretation

The present structured-data target includes single-table, time-series and multi-table shared-key generation with legitimate composite structured topology representable, plus source-derived/local text-bearing structured fields under the current capability boundary.

008-C through 008-F show that this variation fits the current state, behavior, operational-principle and genericity model without a new concept at those stages. This remains subject to the deliberate 008-G candidate rediscovery audit.

## High-risk boundary results

The following distinctions continue to pass current individual-concept review:

```text
Data Meaning          != Constraint
Synthesis Strategy    != Learning / Generation / implementation plugin
Learning              != Learned State
Learning/Generation/
Evaluation             != Execution
Generation Condition  != Constraint
Evaluation Criterion  != Evaluation != Evidence
Evidence               != Provenance
Execution              != Attempt != platform job
```

008-F also continues to reject umbrella collapse through `Synthesizer`, `Model`, `Run`, `Quality`, `Metadata`, `Validation`, `Artifact`, or generic `Privacy` as replacements for the accepted concept boundaries.

## Relationship candidate disposition

[006-G — Structured-Data Topology: Single-Table, Time-Series & Multi-Table Relationship Concept/Extensibility Audit](../phases/006/006-G-structured-data-topology-single-table-time-series-multi-table-relationship-concept-extensibility-audit.md) resolved the previously reopened `Relationship` candidate.

**Relationship is not a standalone accepted concept under the current catalog.** Material structural relationship semantics are currently subordinate descriptive state owned by Data Meaning under the canonical [Structured-Data Topology & Relationship Semantics Contract](../authority/structured-data-topology-relationship-semantics-contract.md).

This disposition is not considered final until 008-G deliberately replays the candidate against all current evidence.

## Historical consolidation

[002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](../phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md) confirmed that the eleven-concept model was coherent at the Phase 002 exit.

Phase 006 later revalidated the catalog against recovery, runtime-distribution, scale, privacy and structured-topology evidence. Phase 008 now replaces reliance on those historical completion labels with current normalized concept authority.

## Authority rule

The individual concept specifications plus current Phase 008 cross-concept normalization authorities and active cross-cutting authority under `docs/authority/` supersede provisional concept statements under `docs/discovery/` unless later explicit design authority accepts a revision.

No Python class, Spark API, PyTorch object, storage format, job type, package module, database, function parameter, UI element, UUID scheme, manifest, event-store representation or persistence layout is implied by one concept document or normalization authority.

## Deferred/non-concept responsibilities

The following remain intentionally outside the accepted standalone concept catalog **pending 008-G rediscovery**:

- Generation Request and Condition — subordinate to Generation;
- Attempt, Checkpoint, Retry, and cancellation realization — subordinate to Execution/domain lifecycle semantics;
- stable dataset/artifact identity — representation/integration obligation under the current model;
- reproducibility — cross-cutting [Reproducibility Contract](../authority/reproducibility-contract.md);
- lineage — derivational subset of Provenance;
- privacy objectives/guarantees — mechanism-specific future discovery; formal composable DP remains deferred and requires concept rediscovery before implementation;
- Relationship — currently Data Meaning-owned structural relationship semantics;
- Use / Release Decision — external authority boundary;
- Source Characterization/Profile — supporting observation/method;
- `GenerationMode`, `DataTopologyMode`, `Series`, `Sequence`, `TimeSeries`, `Table`, and generic `Dataset` — not accepted concepts merely because a later API may represent those variations;
- Resource, Backpressure, Approximation, DegradedMode, Cost and Quota — cross-cutting/operational policy or owner-specific semantics under current evidence;
- Validation, Metric, Quality, Model, Metadata, Run, Artifact, and Synthesizer — umbrella/compatibility terms that must not silently become god-concepts.

008-G must retest these dispositions from first principles rather than merely reaffirming Phase 001 decisions.
