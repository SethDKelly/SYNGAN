---
type: Concept Dependence Index
title: SYNGAN Concept Dependence & Application Family
status: active
---

# SYNGAN Concept Dependence & Application Family

## Purpose

This directory contains current Jackson-style application inclusion-dependence and application-family authority for SYNGAN.

Inclusion dependence remains distinct from reference, validation, production, operational/runtime, provenance, persistence, synchronization, import, or dataflow dependency.

For concepts `C1` and `C2`, the governing question is:

> **If `C1` is included in an application, does including `C1` make sense only if `C2` is also included?**

## Current authority

- [Inclusion-Dependence Pairwise Inventory](inclusion-dependence-pairwise-inventory.md) — 009-A.
- [Inclusion-Dependence Graph & Ordering](inclusion-dependence-graph-ordering.md) — 009-B.
- [Application Family & Valid Subsets](application-family-valid-subsets.md) — 009-C.
- [Contraction / Extension Consequences](contraction-extension-consequences.md) — 009-D.
- [Current Synchronization Authority](../synchronizations/index.md) — downstream Phase 009 composition authority.

## Current phase state

```text
Phase 008                         COMPLETE
Phase 009                         ACTIVE
009-A                             COMPLETE
009-B                             COMPLETE
009-C                             COMPLETE
009-D                             COMPLETE
009-E                             COMPLETE
009-F                             COMPLETE
009-G                             COMPLETE
009-H                             NEXT ELIGIBLE
D1 inclusion-dependence graph     CURRENTLY CLOSED
D2 application family             CURRENTLY CLOSED
D3 explanation/design ordering    CURRENTLY CLOSED
D4 add/remove consequences        CURRENTLY CLOSED
E1-E5 composition                 CURRENTLY CLOSED
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

Three pairwise findings are transitive:

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

A non-empty subset is coherent only if it:

1. is closed under the universal graph;
2. satisfies `Execution => Learning OR Generation OR Evaluation` when Execution is present;
3. gives Provenance a meaningful typed relationship/history witness when Provenance is present;
4. includes all concepts required by every advertised capability;
5. preserves accepted concept purposes/boundaries.

Canonical kernels:

```text
L-KERNEL = Data Meaning + Synthesis Strategy + Learning + Learned State
G-KERNEL = Data Meaning + Synthesis Strategy + Generation
E-KERNEL = Evaluation Criterion + Evaluation + Evidence
```

## Contraction / extension authority

```text
remove Data Meaning or Synthesis Strategy
  => Learning + Learned State + Generation cannot remain

remove Evaluation Criterion
  => Evaluation + Evidence cannot remain

remove one member of L-CLUSTER or E-CLUSTER
  => remove its mutual-inclusion partner
```

Removing Generation, Constraint, Execution or Provenance may instead be capability-only contraction where remaining family rules hold.

Ordinary extension uses accepted concepts plus required closure/side constraints. Fresh discovery is reserved for genuinely new independent purpose/state/action lifecycles.

## Composition handoff after 009-G

The current family composes through thirteen active synchronization rules with D1-D4 unchanged.

009-G confirms that synchronization does not accidentally turn conditional concept relations into new inclusion dependencies:

- direct Generation remains valid without Learning/Learned State;
- direct/non-gated Generation remains valid without Evaluation/Evidence;
- Execution remains optional for trivial/local activity;
- Constraint remains optional across the family;
- Provenance remains optional where its capability is not claimed;
- similarity of synchronization patterns does not imply concept merger or new application dependence.

The occurrence-scoped synchronization rule also preserves dependence semantics: an exact historical binding does not create permanent inclusion/reactive dependence on all future revisions/status changes.

## Product-scope documentation rule

A family member may remain structurally coherent while losing a former advertised capability after contraction. Later mapping/product documentation must therefore describe the actual included concepts/capabilities and remove stale promises.

Application-family validity remains distinct from product packaging or implementation modularity.

## Dependence-derived explanation ordering

Prerequisite-first explanation remains:

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

**009-H — Phase 009 Consolidation, Dependence/Composition Completion Decision & Phase 010 Handoff** is next.

009-H must consolidate this dependence/application-family authority with the completed synchronization/composition authority before Phase 010 begins.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
