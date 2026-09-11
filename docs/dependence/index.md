---
type: Concept Dependence Index
title: SYNGAN Concept Dependence & Application Family
status: active
---

# SYNGAN Concept Dependence & Application Family

## Purpose

This directory contains current Jackson-style **application inclusion-dependence and application-family** authority for SYNGAN.

Inclusion dependence is distinct from reference, validation, production, operational/runtime, authority, provenance, import, persistence, or dataflow dependency.

For concepts `C1` and `C2`, the governing question remains:

> **If `C1` is included in an application, does including `C1` make sense only if `C2` is also included?**

Application-family validity then asks whether a non-empty concept subset satisfies universal closure, non-binary prerequisites, and every capability-specific inclusion requirement it claims.

## Current authority

- [Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory](inclusion-dependence-pairwise-inventory.md) — 009-A pairwise authority.
- [Inclusion-Dependence Graph, Strong Components & Explanation Ordering](inclusion-dependence-graph-ordering.md) — 009-B canonical graph/order authority.
- [Application Family, Valid Concept Subsets & Minimal Coherent Variants](application-family-valid-subsets.md) — 009-C current application-family authority.

## Current phase state

```text
Phase 008                         COMPLETE
Phase 009                         ACTIVE
009-A                             COMPLETE
009-B                             COMPLETE
009-C                             COMPLETE
009-D                             NEXT ELIGIBLE
D1 inclusion-dependence graph     CURRENTLY CLOSED
D2 application family             CURRENTLY CLOSED
D3 explanation/design ordering    CURRENTLY CLOSED
D4 add/remove consequences        PARTIAL TO STRONG
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

Two legitimate mutual inclusion components remain:

```text
L-CLUSTER = { Learning, Learned State }
E-CLUSTER = { Evaluation, Evidence }
```

The condensed universal graph is acyclic.

## Current application-family rule

A non-empty subset `S` is a coherent current family member only if it:

1. is closed under the universal graph;
2. satisfies `Execution => Learning OR Generation OR Evaluation` when Execution is present;
3. gives Provenance at least one meaningful typed relationship/history witness when Provenance is present;
4. contains all concepts required by every capability the variant advertises;
5. preserves the accepted concept purposes and boundaries.

Concept-family validity is not the same as product packaging or implementation modularity.

## Canonical minimal variants

### Authority-only

```text
{ Data Meaning }
{ Synthesis Strategy }
{ Constraint }
{ Evaluation Criterion }
```

### Learning capability

```text
L-KERNEL = {
  Data Meaning,
  Synthesis Strategy,
  Learning,
  Learned State
}
```

### Direct Generation capability

```text
G-KERNEL = {
  Data Meaning,
  Synthesis Strategy,
  Generation
}
```

### Evaluation capability

```text
E-KERNEL = {
  Evaluation Criterion,
  Evaluation,
  Evidence
}
```

### Execution-bearing minima

```text
GX-KERNEL = G-KERNEL + Execution
LX-KERNEL = L-KERNEL + Execution
EX-KERNEL = E-KERNEL + Execution
```

Provenance has no single membership-only minimum because a valid Provenance variant depends on the relationship semantics being preserved.

## Capability-conditioned extensions

Current family rules additionally preserve:

```text
learned-state-assisted Generation
  => L-KERNEL + Generation

evaluation-gated Generation
  => G-KERNEL + E-KERNEL

reusable prescriptive-rule capability
  => Constraint

durable operational lifecycle
  => Execution + at least one domain activity

provenance/history capability
  => Provenance + meaningful relationship witness
```

Topology breadth and text-bearing structured-data capability do not introduce new current concepts. They remain variations of Data Meaning/Strategy/Generation plus optional Learning/Constraint/Evaluation/Execution/Provenance as the capability requires.

## Invalid subset examples

```text
{ Data Meaning, Synthesis Strategy, Learning }
  invalid — missing Learned State

{ Data Meaning, Synthesis Strategy, Learned State }
  invalid — missing Learning

{ Synthesis Strategy, Generation }
  invalid — missing Data Meaning

{ Evaluation Criterion, Evaluation }
  invalid — missing Evidence

{ Evaluation, Evidence }
  invalid — missing Evaluation Criterion

{ Execution }
  invalid — no realizable activity

{ Provenance }
  invalid — no provenance-bearing relationship
```

A coherent subset can still be invalid for a stronger advertised capability; for example G-KERNEL is valid direct Generation but not learned-state-assisted Generation without L-KERNEL.

## Dependence-derived explanation ordering

Strict prerequisite constraints remain:

```text
Data Meaning before Learning / Learned State
Synthesis Strategy before Learning / Learned State
Data Meaning before Generation
Synthesis Strategy before Generation
Evaluation Criterion before Evaluation / Evidence
```

Recommended explanatory layers remain:

```text
Layer 0  Data Meaning / Synthesis Strategy / Constraint / Evaluation Criterion
Layer 1  Learning / Learned State / Generation / Evaluation / Evidence
Layer 2  Execution / Provenance
```

Within the mutual components:

```text
Learning before Learned State
Evaluation before Evidence
```

This is an explanation/design order, not package/runtime/implementation order.

## Current next boundary

**009-D — Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences** is next.

009-D must systematically use the family rules above to determine what is lost, forced out, or newly required when concepts/components are removed or added, and distinguish ordinary family extension from future scope that requires fresh concept discovery.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
