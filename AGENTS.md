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
- `docs/dependence/inclusion-dependence-pairwise-inventory.md`
- `docs/phases/009/index.md`

Current state:

```text
accepted concepts          11
accepted synchronizations  15
Phase 008                  COMPLETE
Phase 009                  ACTIVE
009-A                      COMPLETE
009-B                      NEXT ELIGIBLE
D1                         PARTIAL — PAIRWISE INVENTORY COMPLETE; GRAPH PENDING
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or plans may expose misfits, but they may not veto upstream concept-design correction.**

## 009-A authority to preserve

Jackson inclusion dependence asks:

> If concept C1 is included in an application, does C1 make sense only if concept C2 is also included?

It is not equivalent to reference, validation, production, runtime, provenance, synchronization, import, storage or service dependency.

009-A classified all 110 directed non-self pairs:

```text
D  12 universal dependence candidates
C  43 conditional/disjunctive relations
N  55 no universal dependence
I   0 insufficient
```

Universal candidates are:

```text
Learning      -> Data Meaning
Learning      -> Synthesis Strategy
Learning      -> Learned State
Learned State -> Learning
Learned State -> Data Meaning
Learned State -> Synthesis Strategy
Generation    -> Data Meaning
Generation    -> Synthesis Strategy
Evaluation    -> Evaluation Criterion
Evaluation    -> Evidence
Evidence      -> Evaluation Criterion
Evidence      -> Evaluation
```

009-A does **not** decide direct versus transitive edges.

Two mutual-dependence candidates require 009-B analysis:

```text
Learning   <-> Learned State
Evaluation <-> Evidence
```

Do not merge these concepts merely because the pairwise relation is cyclic; Phase 008 independently established their purposes/boundaries.

Execution has a disjunctive one-of prerequisite across `{Learning, Generation, Evaluation}`. Provenance has a non-binary provenance-subject prerequisite. Do not flatten either into false universal graph edges.

## Current 009-B boundary

**009-B — Inclusion-Dependence Graph, Roots, Cycles & Explanation Ordering** is next eligible.

009-B must determine:

- direct versus transitive dependence;
- treatment of the two mutual-dependence candidates;
- representation of conditional/disjunctive prerequisites;
- graph roots/leaves;
- dependence-derived explanation/design ordering;
- whether graph pressure exposes a J2 concept-boundary defect.

Do not infer graph directness from file references, synchronizations, imports, package structure, APIs, persistence, or runtime topology.

## Stop/reopen discipline

Follow J0-J7 in the methodology matrix. Reopen the smallest affected upstream authority for a real defect.

- J1 local concept defect → Phase 008 concept authority;
- J2 purpose/boundary/catalog defect → Phase 008-B/F/G as appropriate;
- J3 dependence/composition defect → repair in Phase 009 unless it proves an upstream cause.

## What agents may do now

For 009-B, agents may use Phase 009-A pairwise evidence to derive the canonical inclusion graph, strongly connected clusters, direct/transitive reduction, roots/leaves and explanation ordering.

Architecture/source/tests may be inspected only as counterexample/feasibility evidence, not graph authority.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies, package-topology changes, or executable architecture restrictions merely to freeze evolving design.

Do not change module/package dependencies to mirror 009-A/009-B concept dependence.

Do not repair stale implementation tests solely to make implementation appear ready.

## Readiness rule

Phases 009-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**009-B — Inclusion-Dependence Graph, Roots, Cycles & Explanation Ordering**.

Do not begin implementation work.
