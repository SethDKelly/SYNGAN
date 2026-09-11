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
- `docs/dependence/application-family-valid-subsets.md`
- `docs/phases/009/index.md`

Current state:

```text
accepted concepts          11
accepted synchronizations  15
Phase 008                  COMPLETE
Phase 009                  ACTIVE
009-A                      COMPLETE
009-B                      COMPLETE
009-C                      COMPLETE
009-D                      NEXT ELIGIBLE
D1                         CURRENTLY CLOSED
D2                         CURRENTLY CLOSED
D3                         CURRENTLY CLOSED
D4                         PARTIAL TO STRONG
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or plans may expose misfits, but they may not veto upstream concept-design correction.**

## Current dependence graph

Jackson inclusion dependence asks whether concept C1 can remain meaningfully included when concept C2 is absent. It is not ordinary reference, validation, production, runtime, provenance, import, storage, or service dependency.

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

Do not merge concepts or technical modules merely because they share an inclusion component.

## Current application-family rule

A non-empty concept subset is a coherent current family member only if it:

1. is closed under the universal graph;
2. satisfies `Execution => Learning OR Generation OR Evaluation` when Execution is included;
3. gives Provenance an actual meaningful typed relationship/history witness when Provenance is included;
4. includes every concept required by the capabilities the variant explicitly claims;
5. preserves the Phase 008 concept purposes and boundaries.

Canonical kernels:

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Authority-only subsets `{Data Meaning}`, `{Synthesis Strategy}`, `{Constraint}`, and `{Evaluation Criterion}` are coherent design-family members.

## Capability conditions to preserve

```text
learned-state-assisted Generation
  => L-KERNEL + Generation

evaluation-gated Generation
  => G-KERNEL + E-KERNEL

reusable prescriptive-rule capability
  => Constraint

durable operational lifecycle
  => Execution + at least one domain activity

provenance/history capability
  => Provenance + meaningful relationship witness
```

Topology breadth and text-bearing structured data remain variations of existing concepts; do not restore Relationship, TimeSeries, Table, Text, Tokenizer, Vocabulary, or Language Model merely because an implementation may expose such objects.

## Critical interpretation

A **coherent concept subset is not automatically**:

- a package/module boundary;
- an installable edition;
- a deployable service set;
- a feature-flag bundle;
- a database/schema partition;
- a transaction boundary;
- a commercial SKU.

Do not create implementation topology from the application-family model while design remains incomplete.

## Current 009-D boundary

**009-D — Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences** is next eligible.

009-D must use the current family rules to analyze systematically:

- what functionality is lost when each concept/component is removed;
- which dependents must be removed/re-scoped as a consequence;
- how L-CLUSTER/E-CLUSTER contract as units;
- what happens to Execution/Provenance side constraints;
- which additions are ordinary composition of existing concepts;
- which future additions trigger fresh concept discovery under 008-G;
- which capability claims become misleading after contraction.

Do not perform synchronization replay early; 009-E owns that work after D4 closes.

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

For 009-D, agents may analyze concept/component contraction and extension against the current application family, record capability consequences, and distinguish ordinary family composition from future-scope rediscovery triggers.

Architecture/source/tests may be inspected only as counterexample/feasibility evidence, not family authority.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies, package-topology changes, or executable architecture restrictions merely to freeze evolving design.

Do not translate application-family subsets into package dependencies, product editions, deployment profiles, or feature flags yet.

Do not repair stale implementation tests solely to make implementation appear ready.

## Readiness rule

Phases 009-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**009-D — Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences**.

Do not begin implementation work.
