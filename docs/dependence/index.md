---
type: Concept Dependence Index
title: SYNGAN Concept Dependence & Application Family
status: active
---

# SYNGAN Concept Dependence & Application Family

## Purpose

This directory contains current Jackson-style **application inclusion-dependence** authority for SYNGAN.

Inclusion dependence is distinct from reference, validation, production, operational/runtime, authority, provenance, import, persistence, or dataflow dependency.

For concepts `C1` and `C2`, the governing question remains:

> **If `C1` is included in an application, does including `C1` make sense only if `C2` is also included?**

## Current authority

- [Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory](inclusion-dependence-pairwise-inventory.md) — 009-A pairwise authority.
- [Inclusion-Dependence Graph, Strong Components & Explanation Ordering](inclusion-dependence-graph-ordering.md) — 009-B canonical graph/order authority.

## Current phase state

```text
Phase 008                         COMPLETE
Phase 009                         ACTIVE
009-A                             COMPLETE
009-B                             COMPLETE
009-C                             NEXT ELIGIBLE
D1 inclusion-dependence graph     CURRENTLY CLOSED
D2 application family             OPEN
D3 explanation/design ordering    CURRENTLY CLOSED
D4 add/remove consequences        PARTIAL
```

## Canonical graph result

The 12 universal pairwise findings from 009-A reduce to 9 direct universal edges:

```text
Learning      -> Data Meaning
Learning      -> Synthesis Strategy
Learning      -> Learned State
Learned State -> Learning

Generation    -> Data Meaning
Generation    -> Synthesis Strategy

Evaluation    -> Evaluation Criterion
Evaluation    -> Evidence
Evidence      -> Evaluation
```

Three pairwise findings are transitive rather than direct:

```text
Learned State -> Data Meaning
Learned State -> Synthesis Strategy
Evidence      -> Evaluation Criterion
```

## Strongly connected components

Two legitimate mutual inclusion components remain:

```text
L-CLUSTER = { Learning, Learned State }
E-CLUSTER = { Evaluation, Evidence }
```

They do not merge the concepts. Phase 008 already established distinct activity/result purposes and singular state/action ownership.

The condensed universal graph is acyclic.

## Non-binary constraints retained for 009-C

Universal pairwise edges are not sufficient to derive valid application subsets.

At minimum:

```text
Execution => Learning OR Generation OR Evaluation

Provenance => at least one meaningful provenance-bearing relationship
              involving current SYNGAN concept state/result/history
```

Additional conditional application-family rules include learned-state-assisted Generation, evaluation-gated Generation, optional Constraint support, and conditional durable Execution for operationally significant activities.

These are side constraints, not false unconditional graph edges.

## Dependence-derived explanation ordering

Strict prerequisite constraints are:

```text
Data Meaning before Learning / Learned State
Synthesis Strategy before Learning / Learned State
Data Meaning before Generation
Synthesis Strategy before Generation
Evaluation Criterion before Evaluation / Evidence
```

Recommended explanatory layers are:

```text
Layer 0  Data Meaning / Synthesis Strategy / Constraint / Evaluation Criterion
Layer 1  Learning / Learned State / Generation / Evaluation / Evidence
Layer 2  Execution / Provenance
```

Within the mutual components, use narrative activity-before-result order:

```text
Learning before Learned State
Evaluation before Evidence
```

This is an explanation/design order, not package/runtime/implementation order.

## Current next boundary

**009-C — Application Family, Valid Concept Subsets & Minimal Coherent Variants** is next.

009-C must derive valid and invalid subsets from both universal graph closure and the non-binary/conditional constraint layer.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
