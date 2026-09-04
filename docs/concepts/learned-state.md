---
type: Concept
title: Learned State
status: accepted
---

# Learned State

## Purpose

Preserve reusable source-derived information independently of the Learning occurrence and runtime object that produced it.

## Owns

- stable logical identity/version;
- usability/compatibility/retirement status;
- producing Learning reference;
- Strategy/configuration identity;
- compatibility requirements and limitations;
- durable-representation references;
- provenance linkage.

## Actions

Establish on successful Learning, inspect, validate for intended use, select/reuse, compare, retire, and invalidate for future use.

## Invariants

1. Learned State MUST be independently identifiable after producing compute is gone.
2. It MUST NOT be defined as one file, checkpoint, Python object, Spark ML Model, or PyTorch module.
3. Retirement/invalidation affects future use and MUST NOT rewrite historical Generations.
4. A Learned State MUST trace to the Learning and Strategy/configuration that produced it.

## Operational principle

A successful Learning establishes state that can be reused for multiple Generations weeks later, compared with newer state, and eventually retired without altering prior history.

## Boundaries

Learned State is not Learning, checkpoint recovery state, or a generic Artifact concept.

## Synchronization

See [SYNC-05](../synchronizations/core-synchronizations.md#sync-05--learning-produces-learned-state) and [SYNC-06](../synchronizations/core-synchronizations.md#sync-06--generation-commitment-and-compatibility).
