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
- `docs/synchronizations/index.md`
- `docs/synchronizations/trigger-ownership-normalization.md`
- `docs/synchronizations/composition-economy-synergy-integrity.md`
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
009-F                                COMPLETE
009-G                                COMPLETE
009-H                                NEXT ELIGIBLE
D1-D4                                CURRENTLY CLOSED
E1-E5                                CURRENTLY CLOSED
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or plans may expose misfits, but they may not veto upstream concept-design correction.**

## Current synchronization inventory

### Required relational

```text
SYNC-01  Data Meaning revision binding
SYNC-02  Strategy selection and compatibility
SYNC-05  Learning produces Learned State
SYNC-09  Evaluation Criterion binding
SYNC-10  Evaluation method compatibility
SYNC-12  Evaluation produces Evidence
```

### Capability / occurrence conditional

```text
SYNC-03  Constraint binding and handling disposition
SYNC-04  Learning operational realization
SYNC-06  Generation / Learned State reuse compatibility and exact basis binding
SYNC-07  Generation operational realization
SYNC-11  Evaluation operational realization
SYNC-13  Generation / Evidence evidence-gated completion handoff
SYNC-14  Provenance recording at material transitions
```

Historical IDs:

```text
SYNC-08  RETIRED — Generation-local output candidate/completion/promotion
SYNC-15  RECLASSIFIED — cross-cutting Reproducibility Contract
SYNC-16  NOT JUSTIFIED
```

Do not reuse or resurrect reserved IDs for symmetry.

## Canonical cross-sync ownership

```text
consumer exact binding / contextual assessment
  -> Learning / Generation / Evaluation

Learned State producer identity
  -> Learned State

Evidence producer identity
  -> Evidence

Execution parent binding + Attempts/retry/recovery
  -> Execution

Provenance typed relationship assertions
  -> Provenance

synchronization-owned canonical state
  -> NONE
```

## Current whole-composition rule

009-G closes economy, coupling, synergy and combined integrity for the current Phase 009 composition.

### Relation-local activation

Mere co-presence of concepts does not activate a conditional synchronization. The actual semantic relation must occur.

Core variant burden remains:

```text
L-KERNEL        SYNC-01, SYNC-02, SYNC-05
Direct G-KERNEL SYNC-01, SYNC-02
E-KERNEL        SYNC-09, SYNC-10, SYNC-12
```

Learned-state-assisted Generation adds `SYNC-06`; evidence-gated Generation adds `SYNC-13`; Constraint/Execution/Provenance add only occurrence-specific relations.

### Synchronization is occurrence-scoped, not a live subscription

Do **not** infer automatic retroactive propagation from an exact historical binding.

Examples:

```text
new Data Meaning revision  != rewrite committed activity
Strategy retirement        != rewrite historical activity
Constraint revision        != rewrite prior binding
Learned State retirement   != mutate prior Generation history
Criterion revision         != reinterpret historical Evidence
Evidence invalidation      != silently rewrite historical Generation completion
Provenance correction      != rewrite source concept history
```

Future/current-use decisions may respond under their own owner rules, but synchronization does not maintain hidden shared state across all later changes.

### Staged evidence feedback

Evaluation-gated Generation is valid staged composition:

```text
Generation candidate
  -> Evaluation
  -> Evidence
  -> Generation-owned completion decision
```

Evaluation requires identifiable candidate state, not an already completed Generation. Evidence never owns `Generation.Complete`.

## Positive synergies to preserve

- `Learning -> Learned State -> Generation` enables reusable learned synthesis without hidden Learned State mutation.
- Evidence-gated Generation lets independent Evaluation/Evidence strengthen Generation completion without collapsing their authorities.
- Constraint + Evaluation/Evidence + Generation makes reusable rule validation explicit without treating enforcement as proof.
- Execution supplies durable operational lifecycle across Learning/Generation/Evaluation while preserving semantic completion ownership.
- exact bindings + Provenance provide cross-concept historical explanation without shadow copies.
- direct and learned Generation coexist without fabricated Learning occurrences.

Do not force every synchronization to be synergistic; basic bindings may be intentionally additive/integrity-preserving.

## Economy rules

Do not merge concept synchronizations merely to reduce the numeric rule count.

In particular:

- keep `SYNC-09` and `SYNC-10` distinct: method sufficiency and exact Criterion commitment are different actions;
- keep `SYNC-04`, `SYNC-07`, `SYNC-11` distinct: a generic Activity umbrella is not an accepted concept and parent semantic contracts differ;
- keep `SYNC-05` and `SYNC-12` distinct: Learned State and Evidence have different result semantics/cardinalities;
- keep one generic typed `SYNC-14` rather than inventing pair-specific Provenance synchronizations.

No new `SYNC-16` is currently justified.

## Critical interpretation

A concept synchronization is not automatically:

- a service call;
- an event or message;
- a transaction or saga;
- a queue/topic;
- an API endpoint;
- a package/module dependency;
- a schema foreign key;
- a runtime workflow edge;
- a deployment unit;
- a permanent observer/subscription mechanism.

Do not translate synchronization authority into implementation topology while design remains incomplete.

## Current 009-H boundary

**009-H — Phase 009 Consolidation, Dependence/Composition Completion Decision & Phase 010 Handoff** is next eligible.

009-H must consolidate, not redesign by default.

It must verify:

- D1-D4 and E1-E5 authority is internally consistent;
- concept count remains 11;
- historical SYNC IDs remain 15 with 13 active rules;
- `SYNC-08`/`SYNC-15` dispositions and `SYNC-06` narrowing are propagated consistently;
- no stale candidate/next-state wording remains in active Phase 009 authority;
- no residual J1/J2/J3 blocker exists;
- Phase 010 receives a clear dependence/application-family/composition handoff;
- implementation remains **NOT READY / NOT STARTED / NOT YET**.

009-H may declare Phase 009 dependence/composition **complete enough for Phase 010**. It may not declare Jackson concept design complete.

## Stop/reopen discipline

Follow J0-J7 in the methodology matrix. Reopen the smallest affected upstream authority for a real defect.

- J1 local concept defect → Phase 008 concept authority;
- J2 purpose/boundary/catalog defect → Phase 008-B/F/G as appropriate;
- J3 dependence/composition defect → Phase 009 authority.

Do not reopen completed authority merely to align with existing implementation structure.

## What agents may do now

For 009-H, agents may consolidate and reconcile current Phase 009 design documents, verify counts/status/authority consistency, identify any residual D/E contradiction, and prepare the Phase 010 handoff.

Architecture/source/tests may be inspected only as counterexample/feasibility evidence, not composition authority.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies, package-topology changes, event/service decomposition, or executable architecture restrictions merely to freeze evolving design.

Do not repair stale implementation tests solely to make implementation appear ready.

## Readiness rule

Phases 009-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**009-H — Phase 009 Consolidation, Dependence/Composition Completion Decision & Phase 010 Handoff**.

Do not begin implementation work.
