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

Application-family validity asks whether a non-empty concept subset satisfies universal closure, non-binary prerequisites, and every capability-specific inclusion requirement it claims. Contraction/extension authority then determines what capability and family consequences follow when that subset changes.

## Current authority

- [Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory](inclusion-dependence-pairwise-inventory.md) — 009-A pairwise authority.
- [Inclusion-Dependence Graph, Strong Components & Explanation Ordering](inclusion-dependence-graph-ordering.md) — 009-B canonical graph/order authority.
- [Application Family, Valid Concept Subsets & Minimal Coherent Variants](application-family-valid-subsets.md) — 009-C application-family authority.
- [Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences](contraction-extension-consequences.md) — 009-D add/remove consequence authority.

## Current phase state

```text
Phase 008                         COMPLETE
Phase 009                         ACTIVE
009-A                             COMPLETE
009-B                             COMPLETE
009-C                             COMPLETE
009-D                             COMPLETE
009-E                             NEXT ELIGIBLE
D1 inclusion-dependence graph     CURRENTLY CLOSED
D2 application family             CURRENTLY CLOSED
D3 explanation/design ordering    CURRENTLY CLOSED
D4 add/remove consequences        CURRENTLY CLOSED
```

## Canonical graph result

The 12 universal pairwise findings reduce to 9 direct universal edges:

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

Three accepted pairwise findings are transitive:

```text
Learned State -> Data Meaning
Learned State -> Synthesis Strategy
Evidence      -> Evaluation Criterion
```

Two legitimate SCCs remain:

```text
L-CLUSTER = { Learning, Learned State }
E-CLUSTER = { Evaluation, Evidence }
```

The condensed universal graph is acyclic.

## Application-family rule

A non-empty subset `S` is coherent only if it:

1. is closed under the universal graph;
2. satisfies `Execution => Learning OR Generation OR Evaluation` when Execution is present;
3. gives Provenance at least one meaningful typed relationship/history witness when Provenance is present;
4. contains all concepts required by every advertised capability;
5. preserves accepted concept purposes/boundaries.

Canonical capability kernels remain:

```text
L-KERNEL = Data Meaning + Synthesis Strategy + Learning + Learned State
G-KERNEL = Data Meaning + Synthesis Strategy + Generation
E-KERNEL = Evaluation Criterion + Evaluation + Evidence
```

Authority-only minima remain Data Meaning, Synthesis Strategy, Constraint and Evaluation Criterion.

## Contraction authority

009-D establishes systematic removal consequences.

### Closure-breaking removals

```text
remove Data Meaning
  => remove/re-scope Learning + Learned State + Generation

remove Synthesis Strategy
  => remove/re-scope Learning + Learned State + Generation

remove Evaluation Criterion
  => remove Evaluation + Evidence
```

### SCC removals

```text
remove Learning      => remove Learned State
remove Learned State => remove Learning

remove Evaluation => remove Evidence
remove Evidence   => remove Evaluation
```

### Capability-only contractions

```text
remove Generation  => synthetic-output capability disappears
remove Constraint  => reusable prescriptive-rule capability disappears
remove Execution   => durable operational-realization capability disappears
remove Provenance  => typed provenance/history capability disappears
```

These do not create permission to hide the removed concept's semantics inside another concept.

## Extension authority

Ordinary extension uses accepted concepts plus required closure:

```text
add Learning or Learned State
  => add full L-KERNEL closure

add Generation
  => add Data Meaning + Synthesis Strategy

add Evaluation or Evidence
  => add full E-KERNEL closure

add Execution
  => require at least one Learning / Generation / Evaluation activity

add Provenance
  => require a meaningful typed relationship/history witness
```

Adding Constraint, Data Meaning, Strategy or Criterion may be independent.

Learned-state-assisted Generation, evaluation-gated Generation, reusable rule support, durable operational lifecycle, typed provenance, current topology breadth and text-bearing structured-data capability are ordinary family extensions when current concepts remain sufficient.

## Rediscovery boundary

Fresh concept discovery is required rather than ordinary extension when new scope creates an independent purpose/state/action lifecycle that the current catalog cannot own cleanly.

Current explicit rediscovery triggers include:

- composable formal privacy/accounting;
- product-owned governance/use/release decisions;
- independently reusable/negotiable request or cohort definitions;
- independent synthetic-output publication/versioning/retirement/transformation lifecycle;
- arbitrary recursive/graph topology with independent relationship behavior;
- product-owned resource/budget/quota/economic governance.

Implementation resources, IDs, tables, services or status values do not themselves create concepts.

## Product-scope documentation rule

A family member may be structurally coherent while losing a former advertised capability after contraction.

Therefore later mapping/product documentation must track the actual family member and remove stale promises. Examples:

```text
no L-CLUSTER  => no learned-state-assisted claim
no E-KERNEL   => no evaluation-backed/evaluation-gated claim
no Constraint => no reusable prescriptive-rule claim
no Execution  => no durable retry/recovery/cancellation claim
no Provenance => no typed provenance traversal claim
```

Application-family validity remains distinct from product packaging or implementation modularity.

## Dependence-derived explanation ordering

Prerequisite-first explanation remains authoritative:

```text
Data Meaning / Synthesis Strategy before Learning / Learned State
Data Meaning / Synthesis Strategy before Generation
Evaluation Criterion before Evaluation / Evidence
```

Within SCCs use narrative order:

```text
Learning before Learned State
Evaluation before Evidence
```

This is not implementation order.

## Current next boundary

**009-E — Synchronization Inventory Revalidation Across the Application Family** is next.

009-E must replay SYNC-01 through SYNC-15 against the completed D1-D4 authority and decide which rules remain universal when participants are present, capability-conditional, over-broad, redundant, or incomplete.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
