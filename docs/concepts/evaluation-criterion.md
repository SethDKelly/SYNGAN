---
type: Concept
title: Evaluation Criterion
status: accepted
---

# Evaluation Criterion

## Purpose

Enable an actor to state and reuse the evaluative question or standard that matters independently of the method used to measure it.

## Owns

- criterion identity/revision;
- question/property being assessed;
- relevant scope, reference population, or use context;
- actor/authority provenance;
- interpretation requirements or acceptance semantics where domain-relevant.

## Actions

Define, select/reuse, inspect, refine/supersede, and associate scope/use context.

## Invariants

1. Criterion MUST remain distinct from metric, method, score, Evidence, and approval authority.
2. Evaluation MUST bind the exact Criterion revision it answers.
3. Later Criterion revisions MUST NOT reinterpret historical Evidence.
4. Multiple Evaluation methods MAY address the same Criterion.

## Operational principle

A model owner defines a utility question and a governance reviewer separately defines a disclosure-risk question before measurement methods are selected; each criterion is reusable across evaluations and datasets.

## Boundaries

Evaluation Criterion is synthetic-data evaluative authority, not a generic policy engine or threshold store.

## Synchronization

See [SYNC-09](../synchronizations/core-synchronizations.md#sync-09--evaluation-criterion-binding) and [SYNC-10](../synchronizations/core-synchronizations.md#sync-10--evaluation-method-compatibility).
