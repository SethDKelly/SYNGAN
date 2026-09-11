---
type: Concept Dependence Index
title: SYNGAN Concept Dependence & Application Family
status: active
---

# SYNGAN Concept Dependence & Application Family

## Purpose

This directory contains current Jackson-style **application inclusion-dependence** authority for SYNGAN.

Inclusion dependence is intentionally distinct from reference, validation, production, operational/runtime, authority, provenance, import, persistence, or dataflow dependency.

For concepts `C1` and `C2` in an application variant `A`, the governing question is:

> **If `C1` is included, does including `C1` make sense only if `C2` is also included?**

## Current authority

- [Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory](inclusion-dependence-pairwise-inventory.md) — Phase 009-A current pairwise authority.

## Current phase state

```text
Phase 008                         COMPLETE
Phase 009                         ACTIVE
009-A                             COMPLETE
009-B                             NEXT ELIGIBLE
D1 inclusion-dependence graph     PARTIAL — PAIRWISE INVENTORY COMPLETE; GRAPH PENDING
D2 application family             OPEN
D3 explanation ordering           OPEN
D4 add/remove consequences        PARTIAL
```

009-A establishes the pairwise relation evidence needed by 009-B. It does **not** decide the canonical direct/transitive graph, cycle treatment, roots/leaves, explanation ordering, application-family subsets, or final composition.

## Pairwise result summary

The current universal inclusion-dependence candidates are:

```text
Learning      -> Data Meaning
Learning      -> Synthesis Strategy
Learning      -> Learned State

Learned State -> Learning
Learned State -> Data Meaning
Learned State -> Synthesis Strategy

Generation    -> Data Meaning
Generation    -> Synthesis Strategy

Evaluation    -> Evaluation Criterion
Evaluation    -> Evidence

Evidence      -> Evaluation Criterion
Evidence      -> Evaluation
```

These are pairwise inclusion findings only. 009-B must determine direct versus transitive edges and explicitly analyze the apparent mutual-dependence pairs `Learning <-> Learned State` and `Evaluation <-> Evidence` rather than treating a cycle as automatically valid or invalid.

## Conditional/disjunctive relations

Several relations are intentionally **not** universal graph edges even though particular application variants require them. Examples include:

- learned-state-assisted Generation may require Learning/Learned State;
- applicable prescriptive rules may require Constraint;
- validation-gated Generation may require Criterion/Evaluation/Evidence;
- operationally significant Learning/Generation/Evaluation may require Execution;
- Execution requires one committed domain activity from `{Learning, Generation, Evaluation}`, but no one member of that set is universally required;
- Provenance requires material canonical/external subjects to relate, but no one accepted concept is a universal pairwise prerequisite;
- Criteria/Evaluation/Evidence may require Data Meaning, Constraint, Generation, or Learned State when their committed question/subject context refers to those authorities.

These conditional/disjunctive requirements must remain visible for 009-B/009-C without being flattened into unconditional edges.

## Historical dependency taxonomy

The existing SYNGAN taxonomy remains useful supporting evidence:

```text
reference / binding
contextual validation
production
operational realization
historical / provenance recording
controlled handoff
```

It does not define Jackson inclusion dependence.

## Current next boundary

**009-B — Inclusion-Dependence Graph, Roots, Cycles & Explanation Ordering** is next.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
