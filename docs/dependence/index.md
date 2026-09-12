---
type: Concept Dependence Index
title: SYNGAN Concept Dependence & Application Family
status: complete-current
---

# SYNGAN Concept Dependence & Application Family

## Purpose

This directory contains current Daniel Jackson-style application inclusion-dependence and application-family authority for SYNGAN.

Inclusion dependence remains distinct from reference, validation, production, operational/runtime, provenance, persistence, synchronization, import, or dataflow dependency.

For concepts `C1` and `C2`, the governing question is:

> **If `C1` is included in an application, does including `C1` make sense only if `C2` is also included?**

## Current authority

- [Inclusion-Dependence Pairwise Inventory](inclusion-dependence-pairwise-inventory.md) — 009-A.
- [Inclusion-Dependence Graph & Ordering](inclusion-dependence-graph-ordering.md) — 009-B.
- [Application Family & Valid Subsets](application-family-valid-subsets.md) — 009-C.
- [Contraction / Extension Consequences](contraction-extension-consequences.md) — 009-D.
- [Phase 009 Consolidation](../authority/phase-009-dependence-composition-consolidation.md) — current cross-layer handoff authority.

## Current phase state

```text
Phase 008                         COMPLETE
Phase 009                         COMPLETE
009-A..009-H                      COMPLETE
D1 inclusion-dependence graph     CURRENTLY CLOSED
D2 application family             CURRENTLY CLOSED
D3 explanation/design ordering    CURRENTLY CLOSED
D4 add/remove consequences        CURRENTLY CLOSED
E1-E5 composition                 CURRENTLY CLOSED
Phase 010                         NEXT ELIGIBLE
```

## Canonical graph result

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

Transitive findings:

```text
Learned State -> Data Meaning
Learned State -> Synthesis Strategy
Evidence      -> Evaluation Criterion
```

Legitimate SCCs:

```text
L-CLUSTER = { Learning, Learned State }
E-CLUSTER = { Evaluation, Evidence }
```

The condensed graph is acyclic.

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

Authority-only coherent members include Data Meaning, Synthesis Strategy, Constraint and Evaluation Criterion independently.

## Contraction / extension authority

```text
remove Data Meaning or Synthesis Strategy
  => Learning + Learned State + Generation cannot remain

remove Evaluation Criterion
  => Evaluation + Evidence cannot remain

remove one member of L-CLUSTER or E-CLUSTER
  => remove its mutual-inclusion partner
```

Removing Generation, Constraint, Execution or Provenance may be capability-only contraction where remaining rules hold.

Ordinary extension uses accepted concepts plus required closure/side conditions. Fresh discovery is reserved for genuinely new independent purpose/state/action lifecycles.

## Composition consistency

Phase 009-E through 009-H confirm that synchronization does not alter the D1-D4 family semantics.

In particular:

- direct Generation remains valid without Learning/Learned State;
- non-gated Generation remains valid without Evaluation/Evidence;
- Constraint remains optional unless reusable rule capability is claimed;
- Execution remains optional unless durable operational realization is claimed;
- Provenance remains optional unless typed relationship/history capability is claimed;
- similarity of synchronization pattern does not imply concept merger or inclusion dependence;
- exact historical binding is occurrence-scoped and does not create permanent inclusion/reactive dependence on future revisions.

## Product-scope documentation rule

A family member may remain coherent while losing a former advertised capability after contraction. Phase 010 mapping must therefore describe the actual included concepts/capabilities and remove stale promises.

Application-family validity remains distinct from product packaging or implementation modularity.

## Dependence-derived explanation ordering

```text
Data Meaning / Synthesis Strategy before Learning / Learned State
Data Meaning / Synthesis Strategy before Generation
Evaluation Criterion before Evaluation / Evidence
```

Within SCCs:

```text
Learning before Learned State
Evaluation before Evidence
```

This is explanation/design order, not implementation order.

## Phase 010 handoff

Concept mapping must preserve valid reduced family members rather than exposing the full eleven-concept design as one mandatory workflow.

Mapping may expose a genuine dependence/family misfit. If so, reopen the smallest affected Phase 009 authority rather than deriving dependence from interface or implementation structure.

## Current next boundary

**Phase 010 — Concept Mapping, Interaction, Linguistic & Experience Alignment** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
