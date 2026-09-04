---
type: Concept
title: Generation
status: accepted
---

# Generation

## Purpose

Define and fulfill an actor's intent to produce synthetic data.

## Owns

- requested output intent, amount, scope, and Conditions;
- bound Data Meaning, Strategy, Learned State when required, and applicable Constraint revisions;
- reproducibility-relevant request state;
- semantic lifecycle and result status;
- completed synthetic-output reference;
- generation-specific diagnostics/limitations.

## Actions

Define/request, amend before commitment where permitted, validate compatibility/satisfiability, initiate fulfillment, observe, cancel/withdraw where permitted, complete/fail, and associate output.

## Invariants

1. Generation Request and Condition semantics are subordinate to Generation.
2. Condition MUST remain distinct from Constraint.
3. Direct-generation strategies MAY omit Learning/Learned State when reusable learned information is not required.
4. Partial/incomplete output MUST be distinguishable from successful completed output.
5. Execution completion alone MUST NOT establish Generation completion.

## Operational principle

A practitioner requests large synthetic output with specific conditions and constraints. After validation, distributed execution may retry; only semantic completion associates the final output, while partial materialization remains non-final.

## Boundaries

Generation is not source sampling, Learning, Execution, or a generic batch-workflow concept.

## Synchronization

See [SYNC-06](../synchronizations/core-synchronizations.md#sync-06--generation-commitment-and-compatibility), [SYNC-07](../synchronizations/core-synchronizations.md#sync-07--generation-operational-realization), and [SYNC-08](../synchronizations/core-synchronizations.md#sync-08--generation-produces-synthetic-output-reference).
