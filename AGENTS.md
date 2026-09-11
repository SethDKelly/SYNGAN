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
- `docs/dependence/inclusion-dependence-graph-ordering.md`
- `docs/phases/009/index.md`

Current state:

```text
accepted concepts          11
accepted synchronizations  15
Phase 008                  COMPLETE
Phase 009                  ACTIVE
009-A                      COMPLETE
009-B                      COMPLETE
009-C                      NEXT ELIGIBLE
D1                         CURRENTLY CLOSED
D2                         OPEN
D3                         CURRENTLY CLOSED
D4                         PARTIAL
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or plans may expose misfits, but they may not veto upstream concept-design correction.**

## Current dependence authority

Jackson inclusion dependence asks:

> If concept C1 is included in an application, does C1 make sense only if concept C2 is also included?

It is not equivalent to reference, validation, production, runtime, provenance, synchronization, import, storage or service dependency.

009-A classified all 110 directed non-self pairs. 009-B establishes the direct graph:

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

Three accepted pairwise findings are transitive rather than direct:

```text
Learned State -> Data Meaning
Learned State -> Synthesis Strategy
Evidence      -> Evaluation Criterion
```

## Strongly connected components

Two legitimate mutual inclusion components are current authority:

```text
L-CLUSTER = { Learning, Learned State }
E-CLUSTER = { Evaluation, Evidence }
```

Do not merge these concepts. Mutual application inclusion does not transfer state/action ownership and does not imply one module, class, table, service, aggregate, or transaction.

The condensed universal graph is acyclic.

## Non-binary constraints

Do not flatten these into unconditional edges:

```text
Execution => Learning OR Generation OR Evaluation

Provenance => at least one meaningful provenance-bearing relationship
              involving current SYNGAN concept state/result/history
```

Additional conditional rules include learned-state-assisted Generation, evaluation-gated Generation, optional Constraint support, and durable Execution for operationally significant activities.

## Current 009-C boundary

**009-C — Application Family, Valid Concept Subsets & Minimal Coherent Variants** is next eligible.

009-C must derive valid and invalid subsets from both:

1. universal graph closure; and
2. non-binary/conditional prerequisite rules.

At minimum test:

- direct-generation-only capability;
- learned-state-assisted Generation;
- Evaluation/Evidence capability;
- variants with/without reusable Constraint;
- variants with durable Execution;
- Provenance-bearing variants;
- topology/text-bearing current-scope variants;
- invalid subsets that violate SCC, universal closure, or side constraints.

Graph closure by itself is not enough to validate Execution or Provenance subsets.

## Explanation/design order

Use prerequisite-first explanation where required:

```text
Data Meaning / Synthesis Strategy before Learning / Learned State
Data Meaning / Synthesis Strategy before Generation
Evaluation Criterion before Evaluation / Evidence
```

Within mutual components use narrative order:

```text
Learning before Learned State
Evaluation before Evidence
```

Execution and Provenance are best explained after domain activities/results, but this is not an implementation ordering rule.

## Stop/reopen discipline

Follow J0-J7 in the methodology matrix. Reopen the smallest affected upstream authority for a real defect.

- J1 local concept defect → Phase 008 concept authority;
- J2 purpose/boundary/catalog defect → Phase 008-B/F/G as appropriate;
- J3 dependence/composition defect → repair in Phase 009 unless it proves an upstream cause.

## What agents may do now

For 009-C, agents may enumerate and test application-family subsets using the current graph and side constraints, identify minimal coherent variants, and classify invalid subsets.

Architecture/source/tests may be inspected only as counterexample/feasibility evidence, not application-family authority.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies, package-topology changes, or executable architecture restrictions merely to freeze evolving design.

Do not change module/package dependencies to mirror concept dependence or strongly connected components.

Do not repair stale implementation tests solely to make implementation appear ready.

## Readiness rule

Phases 009-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**009-C — Application Family, Valid Concept Subsets & Minimal Coherent Variants**.

Do not begin implementation work.
