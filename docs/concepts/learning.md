---
type: Concept
title: Learning
status: accepted
---

# Learning

## Purpose

Derive reusable source-informed state according to accepted source meaning, synthesis behavior, and applicable rules.

## Owns

- learning intent/specification;
- source reference;
- bound Data Meaning, Strategy/configuration, and applicable Constraint revisions;
- semantic lifecycle and outcome;
- resulting Learned State association;
- learning-specific diagnostics.

## Actions

Initiate, validate prerequisites, observe domain status, cancel/withdraw where permitted, complete, fail, and associate a successful result.

## Invariants

1. Learning completion MUST mean reusable source-informed state was validly derived under the selected strategy semantics.
2. Execution completion alone MUST NOT establish Learning completion.
3. Failed/cancelled/incomplete Learning MUST NOT establish usable Learned State.
4. Strategies requiring no reusable source-derived state MUST NOT be forced through no-op Learning.

## Operational principle

A practitioner commits a Learning against stable semantic and strategy revisions. Physical work may fail and retry through Execution; only successful semantic completion establishes Learned State.

## Boundaries

Learning is the domain activity, not generic training infrastructure, Execution, a checkpoint, or the Learned State it produces.

## Synchronization

See [SYNC-03](../synchronizations/core-synchronizations.md#sync-03--constraint-binding-and-handling-disposition), [SYNC-04](../synchronizations/core-synchronizations.md#sync-04--learning-operational-realization), and [SYNC-05](../synchronizations/core-synchronizations.md#sync-05--learning-produces-learned-state).
