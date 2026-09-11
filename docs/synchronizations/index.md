---
type: Synchronization Index
title: SYNGAN Accepted Synchronizations
status: active
---

# SYNGAN Accepted Synchronizations

This directory contains current cross-concept composition authority for SYNGAN.

Concept specifications own their own purpose, state, actions, lifecycle and invariants. Synchronization exists only where already-owned behavior/state effects must coordinate across accepted concept boundaries.

## Current authority

- [Synchronization Inventory Revalidation Across the Application Family](application-family-revalidation.md) — **current Phase 009-E inventory/scope authority**.
- [Core Synchronizations](core-synchronizations.md) — historical detailed SYNC-01 through SYNC-15 rule text and supporting source evidence; inventory membership/scope is superseded where 009-E says otherwise.

## Current synchronization inventory

```text
accepted concepts                    11
historical synchronization IDs       15
active cross-concept synchronizations 13
retired concept-local IDs             1  (SYNC-08)
reclassified contract IDs             1  (SYNC-15)
new synchronization IDs               0
SYNC-16                               NOT JUSTIFIED
E1                                    CURRENTLY CLOSED
```

Historical IDs remain reserved and are never reused.

## Active — required relational

These are required whenever the named semantic relation occurs:

```text
SYNC-01  Data Meaning revision binding
SYNC-02  Strategy selection and compatibility
SYNC-05  Learning produces Learned State
SYNC-06  Generation commitment and compatibility
SYNC-09  Evaluation Criterion binding
SYNC-10  Evaluation method compatibility
SYNC-12  Evaluation produces Evidence
```

## Active — capability / occurrence conditional

These are genuine cross-concept synchronizations, but mere co-presence of concepts does not activate them:

```text
SYNC-03  Constraint binding and handling disposition
SYNC-04  Learning operational realization
SYNC-07  Generation operational realization
SYNC-11  Evaluation operational realization
SYNC-13  Generation/Evidence handoff for evidence-gated completion
SYNC-14  Provenance recording at material transitions
```

Examples:

- Constraint-light variants do not activate `SYNC-03`;
- Execution may realize Learning, Generation, Evaluation, or several at different times; only the actual parent/Execution relation activates the corresponding `SYNC-04/07/11`;
- direct/non-gated Generation does not activate `SYNC-13`;
- Provenance membership does not create arbitrary all-to-all `SYNC-14` relationships.

## SYNC-08 — retired from active synchronization inventory

`SYNC-08 — Generation produces synthetic output reference` remains a reserved historical ID, but output candidate/completion/promotion behavior is now explicitly recognized as **Generation-owned local lifecycle/result behavior**.

Synthetic Output is not a standalone accepted concept. There is no independent `Output.Establish` action to synchronize with `Generation.Complete`.

The substantive semantics remain required under Generation behavior, including:

- candidate versus completed distinction;
- whole-logical-scope completion;
- zero-or-one authoritative completed result;
- no promotion from physical completion alone;
- required validation/Evidence completion barriers;
- single semantic promotion across retry/recovery;
- stable result identity.

Applicable Evidence and Provenance composition remains governed by `SYNC-13` and `SYNC-14`.

## SYNC-15 — reclassified as cross-cutting contract

`SYNC-15 — Reproducibility-relevant commitment snapshot` remains a reserved historical ID but is no longer counted as one active concept synchronization.

Reproducibility remains governed by the [Reproducibility Contract](../authority/reproducibility-contract.md).

Its required facts are assembled from exact concept bindings, immutable commitments/history, production relations, optional Execution history and optional Provenance relations. No standalone Reproducibility concept/state owner is introduced.

## SYNC-13 current scope

009-E narrows the active internal synchronization scope of `SYNC-13` to the conditional Generation/Evidence relation used when Generation completion is evidence-gated.

Evidence exposure to external actors/systems remains important but is not itself cross-concept synchronization inside the accepted catalog. It remains an Evidence/mapping/integration boundary for Phase 010.

## Application-family replay result

Canonical kernels now have these core active synchronization relations:

```text
L-KERNEL
  SYNC-01  Data Meaning binding
  SYNC-02  Strategy compatibility/binding
  SYNC-05  Learning -> Learned State

G-KERNEL
  SYNC-01  Data Meaning binding
  SYNC-02  Strategy compatibility
  SYNC-06  Generation commitment/binding

E-KERNEL
  SYNC-09  Criterion binding
  SYNC-10  method/Criterion compatibility
  SYNC-12  Evaluation -> Evidence
```

Optional Constraint, Execution, evidence-gated completion and Provenance capabilities activate their corresponding conditional synchronization rules only when the actual relation occurs.

## Contraction safety

A synchronization disappears with the relation/capability whose owner is contracted.

No synchronization may recreate semantics belonging to a removed concept:

```text
no Data Meaning   => no hidden semantic default
no Strategy       => no implicit synthesis algorithm authority
no L-CLUSTER      => no fake Learned State production/reuse
no Constraint     => no hidden reusable rule authority
no E-CLUSTER      => no fake Evidence or evaluation-gated completion
no Execution      => no retry/recovery/Attempt migration into domain activities
no Provenance     => no shadow provenance concept/store
```

## Missing-synchronization verdict

009-E finds no missing coordination rule for direct Generation, learned-state-assisted Generation, evaluation-gated Generation, Constraint-light variants, Execution-bearing variants, Provenance-bearing variants, topology breadth, text-bearing structured data, or reproducibility.

```text
new synchronization required  NONE FOUND
SYNC-16                      NOT JUSTIFIED
```

## Current methodology state

```text
D1-D4  CURRENTLY CLOSED
E1     CURRENTLY CLOSED
E2     STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
E3     STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
E4     PARTIAL
E5     PARTIAL TO STRONG
```

009-F must now audit trigger, participating actions/queries, preconditions/postconditions, failure/indeterminate behavior, historical binding, singular state ownership and hidden-coordinator risk for the **13 active rules**.

## Composition guardrails

- one canonical state owner per material fact;
- reusable authorities are queried/bound, not mutated by consumers;
- contextual compatibility belongs to the consuming activity;
- activity/result SCCs do not merge state ownership;
- Execution completion does not establish domain semantic completion;
- Evidence does not own Generation completion or external approval;
- Provenance records established relationships but cannot fabricate upstream facts;
- cross-cutting contracts do not become unnamed shadow concepts;
- historical ID stability does not override synchronization economy.

## Phase 009 sequence

```text
009-A  COMPLETE — pairwise inclusion inventory
009-B  COMPLETE — canonical graph / SCCs / ordering
009-C  COMPLETE — application family / valid subsets
009-D  COMPLETE — contraction / extension / add-remove consequences
009-E  COMPLETE — synchronization inventory replay
009-F  NEXT — trigger / pre-post / state ownership / hidden coordinator
009-G  economy / synergy / integrity
009-H  consolidation
```

## Current next boundary

**009-F — Synchronization Trigger, Preconditions/Postconditions, State Ownership & Hidden-Coordinator Audit** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.