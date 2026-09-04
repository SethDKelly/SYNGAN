---
type: Concept
title: Provenance
status: accepted
---

# Provenance

## Purpose

Explain how material states and results came to exist by recording and traversing typed derivation and context relationships across SYNGAN concepts.

## Owns

- typed derivation/context relationships;
- stable references to participating concept revisions/results;
- actor/software/runtime context when materially relevant;
- temporal/history links needed for explanation and comparison.

## Actions

Record material relationships/context, inspect, traverse, and compare derivations.

## Invariants

1. Provenance MUST reference canonical concept state rather than duplicate it wholesale.
2. Provenance may have high fan-in but MUST have low authority fan-out.
3. Current domain truth MUST NOT depend on reconstructing canonical state from Provenance.
4. Where traceability requires a provenance fact for a committed transition, the transition and required provenance MUST NOT silently diverge.

## Operational principle

A reviewer traverses from Evidence or synthetic output to the bound meaning, strategy, activity, execution context, learned state, and source references that explain how the result came to exist.

## Boundaries

Provenance is broader than lineage but is not a shadow metadata database, data catalog, or owner of the substantive state it references.

## Synchronization

See [SYNC-14](../synchronizations/core-synchronizations.md#sync-14--provenance-recording-at-material-transitions) and [SYNC-15](../synchronizations/core-synchronizations.md#sync-15--reproducibility-relevant-commitment-snapshot).
