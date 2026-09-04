---
type: Concept
title: Constraint
status: accepted
---

# Constraint

## Purpose

Let authorized actors state reusable prescriptive rules that applicable synthetic output is required to satisfy independently of the strategy or activity that attempts to honor them.

## Owns

- rule definition;
- scope/applicability;
- authority/source;
- revision/supersession state;
- severity or requirement semantics where domain-relevant.

## Actions

Declare, inspect/review, revise/supersede, determine applicability, and associate enforcement/validation expectations.

## Invariants

1. Constraint is prescriptive; Data Meaning is descriptive.
2. Activities MUST bind the applicable Constraint revisions they commit to.
3. Unsupported required Constraints MUST remain visible rather than be silently dropped.
4. Strategy or Evaluation handling of a rule MUST NOT redefine the rule itself.
5. New Constraint revisions MUST NOT be presented as though they governed historical work.

## Operational principle

A steward declares reusable validity rules. Different synthesis strategies may enforce, defer, or not support those rules; later Evaluation can assess compliance without becoming rule authority.

## Boundaries

Constraint is not Condition, Data Meaning, strategy capability, or a general enterprise policy engine.

## Synchronization

See [SYNC-03](../synchronizations/core-synchronizations.md#sync-03--constraint-binding-and-handling-disposition).
