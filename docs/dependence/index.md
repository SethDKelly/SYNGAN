---
type: Concept Dependence Index
title: SYNGAN Concept Dependence & Application Family
status: active
---

# SYNGAN Concept Dependence & Application Family

## Purpose

This directory contains current Jackson-style application inclusion-dependence and application-family authority for SYNGAN.

Inclusion dependence is distinct from reference, validation, production, operational/runtime, provenance, import, persistence, synchronization, or dataflow dependency.

For concepts `C1` and `C2`, the governing question remains:

> **If `C1` is included in an application, does including `C1` make sense only if `C2` is also included?**

## Current authority

- [Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory](inclusion-dependence-pairwise-inventory.md) — 009-A.
- [Inclusion-Dependence Graph, Strong Components & Explanation Ordering](inclusion-dependence-graph-ordering.md) — 009-B.
- [Application Family, Valid Concept Subsets & Minimal Coherent Variants](application-family-valid-subsets.md) — 009-C.
- [Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences](contraction-extension-consequences.md) — 009-D.
- [Current Synchronization Authority](../synchronizations/index.md) — downstream Phase 009 composition authority now beginning from the closed D1-D4 result.

## Current phase state

```text
Phase 008                         COMPLETE
Phase 009                         ACTIVE
009-A                             COMPLETE
009-B                             COMPLETE
009-C                             COMPLETE
009-D                             COMPLETE
009-E                             COMPLETE
009-F                             NEXT ELIGIBLE
D1 inclusion-dependence graph     CURRENTLY CLOSED
D2 application family             CURRENTLY CLOSED
D3 explanation/design ordering    CURRENTLY CLOSED
D4 add/remove consequences        CURRENTLY CLOSED
E1 synchronization inventory      CURRENTLY CLOSED
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

## Contraction/extension authority

009-D closes product-scope consequences.

```text
remove Data Meaning or Synthesis Strategy
  => Learning + Learned State + Generation cannot remain

remove Evaluation Criterion
  => Evaluation + Evidence cannot remain

remove one member of L-CLUSTER or E-CLUSTER
  => remove its mutual-inclusion partner
```

Removing Generation, Constraint, Execution or Provenance may be capability-only contraction when remaining family rules remain satisfied.

Ordinary extension uses accepted concepts plus required closure/side constraints. Fresh discovery is reserved for genuinely new independent purpose/state/action lifecycles.

## Handoff into composition

009-E now establishes the current synchronization inventory over this family:

```text
historical synchronization IDs       15
active synchronizations              13
retired concept-local                SYNC-08
reclassified cross-cutting contract  SYNC-15
new synchronization                  NONE
```

This result does not alter D1-D4.

Important consequences for later dependence reasoning:

- a synchronization never creates an inclusion-dependence edge by itself;
- `SYNC-08` retirement does not change Generation's purpose or family closure because output completion was already Generation-owned local result behavior;
- `SYNC-15` reclassification does not create/remove a concept because reproducibility remains a cross-cutting contract;
- active conditional synchronization does not mean the participating concepts are universally co-required across all family members;
- no `SYNC-16` is needed to preserve family coherence.

## Product-scope documentation rule

A family member may be structurally coherent while losing a former advertised capability after contraction. Later mapping/product documentation must track the actual family member and remove stale promises.

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

**009-F — Synchronization Trigger, Preconditions/Postconditions, State Ownership & Hidden-Coordinator Audit** is next.

Dependence/application-family authority remains reopenable only if later composition reveals a genuine J2/J3 misfit.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
