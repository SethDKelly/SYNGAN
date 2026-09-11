# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry.**

Start with:

- `docs/index.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/problem/index.md`
- `docs/concepts/index.md`
- `docs/concepts/phase-008-individual-concept-consolidation.md`
- `docs/synchronizations/index.md`
- `docs/phases/009/009-entry-decomposition.md`
- `docs/phases/009/index.md`

Phase 007 architecture is downstream evidence only until Phase 013 reconciliation.

Current state:

```text
accepted concepts          11
accepted synchronizations  15
current desired outcomes   16
Phase 008                  COMPLETE
individual concept design  COMPLETE ENOUGH FOR PHASE 009
Phase 009                  ACTIVE
009-A                      NEXT ELIGIBLE
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or implementation plans may expose misfits, but they may not veto upstream concept-design correction.**

## Phase 008 authority to preserve

Phase 008-A through 008-H provide current individual-concept authority for problem/purpose, state/history/invariants, actions/queries/transitions, operational principles, independence/genericity/familiarity/reuse, catalog perimeter and consolidation.

The catalog remains eleven concepts. The fifteen synchronization IDs are the current Phase 009 starting set, not a final composition result.

Core distinctions include:

```text
Data Meaning          != Constraint
Synthesis Strategy    != implementation/plugin/runtime
Learning              != Learned State
Learning/Generation/
Evaluation             != Execution
Generation Condition  != Constraint
Evaluation Criterion  != Evaluation != Evidence
Evidence               != Provenance
Execution              != Attempt != platform job
```

Generation currently owns completed logical synthetic-output result semantics. Relationship remains Data Meaning-owned descriptive structural semantics. Generic Privacy remains rejected; future mechanism-specific capabilities such as composable DP require fresh concept discovery before implementation. Use/Release Decision remains external authority.

## Phase 009 active boundary

Phase 009 is decomposed as:

```text
009-A  Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory
009-B  Inclusion-Dependence Graph, Roots, Cycles & Explanation Ordering
009-C  Application Family, Valid Concept Subsets & Minimal Coherent Variants
009-D  Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences
009-E  Synchronization Inventory Revalidation Across the Application Family
009-F  Synchronization Trigger, Preconditions/Postconditions, State Ownership & Hidden-Coordinator Audit
009-G  Composition Economy, Coupling, Synergy & Integrity Closure
009-H  Phase 009 Consolidation, Dependence/Composition Completion Decision & Phase 010 Handoff
```

009-A is the only next eligible subgroup.

## Inclusion-dependence rule

For concepts `C1` and `C2` in an application variant:

> **Does including C1 make sense only if C2 is also included?**

Do not substitute any of the following for that question:

- reference/binding;
- contextual validation;
- production/result establishment;
- operational/runtime realization;
- authority or authorization relation;
- provenance/history relation;
- import/package dependency;
- service call/dataflow/storage relation.

Historical Phase 001-G dependency taxonomy is supporting evidence only.

## Phase 009 sequencing rule

Do not replay synchronization closure before application-family structure exists.

The required sequence is:

```text
pairwise inclusion dependence
  ↓
canonical graph / explanation order
  ↓
valid application-family subsets
  ↓
add/remove / contraction-extension consequences
  ↓
synchronization inventory replay
  ↓
trigger / ownership / pre-post audit
  ↓
composition economy / synergy / integrity
  ↓
consolidation
```

The existing fifteen synchronizations may remain, become conditional/narrower, be removed as redundant, or expose a genuine missing coordination rule. Do not retain a synchronization solely for historical ID stability and do not invent `SYNC-16` for symmetry.

## Stop/reopen classes

Follow J0-J7 in the completion matrix. Reopen the smallest affected upstream authority for a real defect.

For Phase 009:

- J1 — reopen the smallest Phase 008 concept-specification authority;
- J2 — reopen purpose/boundary/catalog authority as appropriate;
- J3 — repair dependence/composition/synchronization within Phase 009 unless it proves a J1/J2 cause;
- J4 — defer true mapping defects to Phase 010;
- J5 — record final-quality issues for Phase 011 unless severe enough to invalidate Phase 009.

## What agents may do now

For 009-A, agents may perform design-only pairwise inclusion-dependence analysis using current concept purposes, absence consequences, operational principles and no-occurrence counterexamples.

Architecture/source/tests may be inspected only as feasibility or misfit evidence, not as authority over the dependence graph.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies for future capability, package-topology changes, or executable architecture/fitness restrictions merely to freeze evolving design.

Do not repair stale implementation tests solely to make implementation appear ready.

## Readiness rule

Phases 009-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision. Even then, implementation itself requires a later explicit Phase 015.

## Current next boundary

**009-A — Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory**.

Do not begin implementation work.
