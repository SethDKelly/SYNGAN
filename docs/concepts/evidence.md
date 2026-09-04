---
type: Concept
title: Evidence
status: accepted
---

# Evidence

## Purpose

Preserve an inspectable observation or result with enough question, method, scope, context, and limitation information that actors can understand what was established without rerunning the Evaluation.

## Owns

- evidence identity/revision;
- Criterion reference;
- observed result/finding;
- method/scope context sufficient for interpretation;
- relevant input references;
- limitations/uncertainty;
- applicability/supersession state;
- provenance linkage.

## Actions

Record, inspect, compare, mark superseded/obsolete/inapplicable without rewriting history, and expose for external decision use.

## Invariants

1. Evidence MUST remain interpretable after the producing Execution is gone.
2. Evidence MUST NOT be treated as approval, privacy guarantee, or release authorization.
3. Evidence answers the Criterion revision it references; later Criterion revisions MUST NOT reinterpret it.
4. Supersession changes current applicability, not historical fact.

## Operational principle

Months after Evaluation completes, a reviewer can inspect utility and disclosure-risk findings, see their methods/scopes/limitations, and use them in governance without confusing those observations with authorization.

## Boundaries

Evidence is not Evaluation, Provenance, claim/decision authority, or a generic evidence warehouse.

## Synchronization

See [SYNC-12](../synchronizations/core-synchronizations.md#sync-12--evaluation-produces-evidence) and [SYNC-13](../synchronizations/core-synchronizations.md#sync-13--evidence-external-handoff).
