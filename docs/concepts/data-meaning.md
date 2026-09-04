---
type: Concept
title: Data Meaning
status: accepted
---

# Data Meaning

## Purpose

Enable practitioners and data stewards to establish, inspect, and revise the semantic interpretation SYNGAN relies upon for structured data.

## Owns

- semantic interpretations by relevant data scope;
- declared, inferred, overridden, unresolved, superseded, or invalidated status;
- authority/source of an interpretation;
- confidence or uncertainty for inferred meaning;
- revision identity for materially distinct interpretations.

## Actions

Declare, infer, review, override/correct, mark unknown/unsupported, supersede, and invalidate.

## Invariants

1. Material meaning used by committed work MUST be bound to a stable revision.
2. Later revisions MUST NOT retroactively reinterpret historical Learning, Generation, Learned State, Evaluation, or Evidence.
3. Structural observations MAY inform meaning but MUST NOT silently become semantic authority.
4. Data Meaning MUST NOT absorb Constraints, Provenance, execution metadata, or generic artifact metadata.

## Operational principle

A steward reviews ambiguous fields, declares or corrects their semantic roles, and leaves unresolved fields explicit. Subsequent synthesis binds the accepted revision; later corrections affect future work only.

## Boundaries

Data Meaning is descriptive, not prescriptive. [Constraint](constraint.md) owns required rules. Physical Spark schema and storage representation are not this concept.

## Synchronization

See [SYNC-01](../synchronizations/core-synchronizations.md#sync-01--data-meaning-revision-binding) and related validation rules.
