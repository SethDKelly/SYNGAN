---
type: Synchronization Authority
title: Current Cross-Concept Synchronization Contract
status: complete-current
---

# Current Cross-Concept Synchronization Contract

## Purpose

Provide one unambiguous current inventory for SYNGAN cross-concept synchronization after Phase 009 normalization and Phase 013 architecture reconciliation.

This document supersedes any conflicting current-looking count, identifier role, or ownership statement in pre-Phase-009 material, including the historical fifteen-rule presentation in `core-synchronizations.md`.

Detailed historical synchronization prose remains useful where it does not conflict with this contract. Concept-owned state remains authoritative; synchronization owns no independent canonical state.

## Current inventory

```text
accepted concepts                       11
historical synchronization IDs          15
active cross-concept synchronizations   13
required-relational                      6
capability/occurrence conditional        7
retired concept-local IDs                1  (SYNC-08)
reclassified contract IDs                1  (SYNC-15)
synchronization-owned canonical state    NONE
```

Historical IDs are never renumbered or reused.

## Required-relational synchronizations

### SYNC-01 — Data Meaning revision binding

When Data Meaning participates in a Learning, Generation or Evaluation commitment, the consuming activity binds the exact relevant Data Meaning revision. Learning and Generation universally include Data Meaning under the current family; an Evaluation-only variant may omit Data Meaning when its supported subject/question does not require SYNGAN Data Meaning authority. Later meaning changes do not reinterpret historical work.

### SYNC-02 — Strategy selection and compatibility

Learning or Generation binds a Strategy and owns its contextual compatibility result. Strategy owns reusable capabilities, limitations and requirements; compatibility is not global Strategy state.

### SYNC-05 — Learning produces Learned State

Successful Learning may establish zero or one primary logical Learned State under the current model. Repeated physical work cannot create ambiguous duplicate authoritative Learned State.

### SYNC-09 — Evaluation Criterion binding

Evaluation binds the exact Criterion revision and material question/scope/reference semantics it answers.

### SYNC-10 — Evaluation method compatibility

Evaluation owns contextual method compatibility. Evidence claim strength cannot exceed the actual method, scope, coverage, assumptions and uncertainty.

### SYNC-12 — Evaluation produces Evidence

A semantically valid Evaluation establishes zero or more independently interpretable Evidence findings when such findings exist. Retry/recovery cannot duplicate or conflict the same authoritative semantic finding.

## Capability / occurrence-conditional synchronizations

### SYNC-03 — Constraint binding and handling

Activities bind applicable Constraint revisions and own contextual applicability/handling. Constraint owns the rule; handling is not satisfaction.

### SYNC-04 — Learning operational realization

When Learning requires operational work, Execution realizes it. Learning owns semantic completion; Execution owns operational realization and Attempt history.

### SYNC-06 — Generation / Learned State reuse compatibility and exact basis binding

When Generation selects reusable Learned State, Generation owns contextual reuse compatibility and the exact Learned State binding. Learned State owns its intrinsic state and producing-Learning identity. Direct Generation does not activate SYNC-06; its request, Strategy, Data Meaning, Conditions and other commitments remain Generation-owned or are covered by their own applicable synchronization rules.

### SYNC-07 — Generation operational realization

When Generation requires operational work, Execution realizes it. Generation owns candidate/finality/completed-output semantics; Execution owns operational realization.

### SYNC-11 — Evaluation operational realization

When Evaluation requires operational work, Execution realizes it. Evaluation owns methodological validity and semantic completion; Execution owns operational realization.

### SYNC-13 — Generation / Evidence completion handoff

When a committed Generation is evidence-gated, Generation may consume exact Evidence to evaluate its own completion basis. Evidence retains finding/claim-strength authority; Generation owns applicability/sufficiency assessment, exact Evidence binding and its completion transition. External release/use/governance handoff remains an interaction/external-authority boundary, not an active accepted-concept synchronization.

### SYNC-14 — Provenance recording at material transitions

Where traceability requires it, material transitions establish typed Provenance relationships over exact stable references. Provenance owns relationships, not the referenced concept state or transition.

## Retired historical ID: SYNC-08

```text
SYNC-08  RETIRED AS CROSS-CONCEPT SYNCHRONIZATION
```

The historical `Generation produces synthetic output reference` rule is now Generation-local behavior.

Generation itself owns:

- partial/candidate state;
- whole committed logical-output scope;
- completion/finality;
- zero-or-one successful logical completed-output result under the current model;
- the immutable completion basis, including required Evidence where applicable.

No synchronization owns this state.

References to `SYNC-08` in older documents are historical labels unless explicitly describing this retirement.

## Reclassified historical ID: SYNC-15

```text
SYNC-15  HISTORICAL / RECLASSIFIED
```

Reproducibility is governed by the cross-cutting [Reproducibility Contract](../authority/reproducibility-contract.md), not by active synchronization-owned state.

Reproducibility is a derived assessment over exact owner/integration facts, including where material:

- historical supportability;
- current feasibility;
- actor-visible assessability/disclosure;
- exact bindings and preserved identities;
- Strategy/method reproducibility characteristics;
- randomness/approximation semantics;
- material Execution/recovery/runtime facts;
- dependency availability/identity limitations.

There is no standalone Reproducibility concept or canonical `SYNC-15` lifecycle/resource.

References to `SYNC-15` in older documents are historical compatibility labels unless explicitly describing this reclassification.

## Ownership invariants

```text
consumer exact bindings / contextual assessments -> owning activity
producing Learning identity                       -> Learned State
producing Evaluation identity                     -> Evidence
Execution / Attempt operational history            -> Execution
Generation candidate / finality / completed output -> Generation
Provenance typed relationships                      -> Provenance
synchronization-owned canonical state               -> NONE
```

A transaction, event, queue, outbox, workflow engine, service call or provider callback may realize coordination without becoming synchronization-owned semantic state.

## Historical document interpretation

`core-synchronizations.md` and pre-Phase-009 phase/architecture documents remain retained historical design evidence and stable anchor targets. Where they describe `15 accepted synchronizations`, active `SYNC-08`, or active `SYNC-15`, this current contract controls instead.

Accepted concept documents may retain historical synchronization-link appendices for traceability. Those appendices do not override this inventory or assign active status to retired/reclassified IDs.

## Phase 014-C whole-design clarification

Phase 014-C replayed the synchronization contract against the current application family and corrected three scope regressions without changing the active-rule inventory:

```text
SYNC-01  explicit "when Data Meaning participates" scope for Evaluation
SYNC-06  Generation / Learned State reuse only; direct Generation does not activate it
SYNC-13  Generation / Evidence evidence-gated completion only; external governance handoff is not accepted-concept synchronization
```

The corrections restore the Phase 009-F normalized semantics and require no concept, family, count, identifier or architecture change.

## Phase 013-I disposition

```text
M6 synchronization count / ID drift        CLOSED BY CURRENT AUTHORITY NORMALIZATION
active rules                                13
historical IDs                              15
SYNC-08                                     retired / Generation-local
SYNC-15                                     reclassified / Reproducibility contract
new synchronization                         NONE
upstream reopen                             NONE
```

Phase 013 is complete and R1 is CURRENTLY CLOSED. Phase 014 whole-design consolidation is active.