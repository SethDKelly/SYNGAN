# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry.**

Start with:

- `docs/index.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/concepts/phase-008-individual-concept-consolidation.md`
- `docs/dependence/index.md`
- `docs/dependence/application-family-valid-subsets.md`
- `docs/dependence/contraction-extension-consequences.md`
- `docs/synchronizations/index.md`
- `docs/synchronizations/application-family-revalidation.md`
- `docs/phases/009/index.md`

Current state:

```text
accepted concepts                    11
historical synchronization IDs       15
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            ACTIVE
009-A                                COMPLETE
009-B                                COMPLETE
009-C                                COMPLETE
009-D                                COMPLETE
009-E                                COMPLETE
009-F                                NEXT ELIGIBLE
D1-D4                                CURRENTLY CLOSED
E1                                   CURRENTLY CLOSED
E2-E3                                REVALIDATION REQUIRED
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or plans may expose misfits, but they may not veto upstream concept-design correction.**

## Current dependence/application-family authority

Current direct universal graph:

```text
Learning      -> Data Meaning
Learning      -> Synthesis Strategy
Learning      -> Learned State
Learned State -> Learning

Generation    -> Data Meaning
Generation    -> Synthesis Strategy

Evaluation    -> Evaluation Criterion
Evaluation    -> Evidence
Evidence      -> Evaluation
```

Current mutual inclusion components:

```text
L-CLUSTER = { Learning, Learned State }
E-CLUSTER = { Evaluation, Evidence }
```

Canonical kernels:

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Execution is valid only with at least one Learning, Generation or Evaluation activity. Provenance is valid only where a meaningful typed relationship/history witness exists.

## Current synchronization inventory

009-E supersedes the historical assumption that all fifteen `SYNC-*` IDs remain active composition rules.

### Active required-relational

```text
SYNC-01  Data Meaning revision binding
SYNC-02  Strategy selection and compatibility
SYNC-05  Learning produces Learned State
SYNC-06  Generation commitment and compatibility
SYNC-09  Evaluation Criterion binding
SYNC-10  Evaluation method compatibility
SYNC-12  Evaluation produces Evidence
```

### Active capability/occurrence conditional

```text
SYNC-03  Constraint binding and handling disposition
SYNC-04  Learning operational realization
SYNC-07  Generation operational realization
SYNC-11  Evaluation operational realization
SYNC-13  Generation/Evidence handoff for evidence-gated completion
SYNC-14  Provenance recording at material transitions
```

Mere co-presence of concepts does not activate a conditional synchronization. The actual semantic relation must occur.

### Historical IDs not active synchronization authority

```text
SYNC-08  RETIRED — Generation-local output candidate/completion/promotion behavior
SYNC-15  RECLASSIFIED — cross-cutting Reproducibility Contract
```

Do not reuse, renumber, or resurrect these IDs merely for symmetry.

`SYNC-08` semantics remain required inside Generation behavior. `SYNC-15` semantics remain required under the Reproducibility Contract.

`SYNC-13` active internal scope is Generation consuming exact Evidence for evidence-gated completion. External Evidence handoff is a later concept-mapping/integration concern, not an internal concept synchronization.

No `SYNC-16` is justified.

## Contraction safety

Synchronization disappears with the relation/capability whose concept owner is contracted.

Do not use synchronization to recreate removed concept semantics:

```text
no Data Meaning => no hidden semantic default
no Strategy     => no implicit synthesis algorithm authority
no L-CLUSTER    => no fake Learned State production/reuse
no Constraint   => no hidden reusable rule authority
no E-CLUSTER    => no fake Evidence/evaluation-gated completion
no Execution    => no retry/recovery/Attempt migration into domain activities
no Provenance   => no shadow provenance concept/store
```

## Critical interpretation

A concept synchronization is not automatically:

- a service call;
- an event or message;
- a transaction;
- a queue/topic;
- an API endpoint;
- a package/module dependency;
- a schema foreign key;
- a runtime workflow edge.

Do not translate synchronization authority into implementation topology while design remains incomplete.

## Current 009-F boundary

**009-F — Synchronization Trigger, Preconditions/Postconditions, State Ownership & Hidden-Coordinator Audit** is next eligible.

009-F must audit only the thirteen active rules from 009-E and normalize for each:

- trigger / initiating conceptual action;
- participating concept actions and queries;
- preconditions;
- effects/postconditions;
- failure and indeterminate behavior;
- exact historical binding where material;
- canonical owner for each fact/state transition;
- shadow-state or hidden-coordinator risk;
- application-family conditionality.

Do not perform 009-G economy/synergy/integrity closure early except where a finding is necessary to identify a 009-F defect.

## Stop/reopen discipline

Follow J0-J7 in the methodology matrix. Reopen the smallest affected upstream authority for a real defect.

- J1 local concept defect → Phase 008 concept authority;
- J2 purpose/boundary/catalog defect → Phase 008-B/F/G as appropriate;
- J3 dependence/composition defect → repair in Phase 009 unless it proves an upstream cause.

## What agents may do now

For 009-F, agents may normalize and adversarially audit the thirteen active synchronization rules for trigger, preconditions/postconditions, failure/indeterminate behavior, historical binding, singular state ownership, conditionality and hidden coordinator/shadow authority.

Historical `core-synchronizations.md` is supporting source evidence. `application-family-revalidation.md` is the current inventory/scope authority.

Architecture/source/tests may be inspected only as counterexample/feasibility evidence, not composition authority.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies, package-topology changes, or executable architecture restrictions merely to freeze evolving design.

Do not implement synchronization as services/events/transactions or repair stale implementation tests solely to make implementation appear ready.

## Readiness rule

Phases 009-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**009-F — Synchronization Trigger, Preconditions/Postconditions, State Ownership & Hidden-Coordinator Audit**.

Do not begin implementation work.
