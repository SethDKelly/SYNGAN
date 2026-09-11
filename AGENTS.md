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
- `docs/dependence/contraction-extension-consequences.md`
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
009-D                      COMPLETE
009-E                      NEXT ELIGIBLE
D1                         CURRENTLY CLOSED
D2                         CURRENTLY CLOSED
D3                         CURRENTLY CLOSED
D4                         CURRENTLY CLOSED
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
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

## Current contraction/extension authority

009-D closes systematic add/remove consequences.

### Removing prerequisites

```text
remove Data Meaning or Strategy
  => current Learning + Learned State + Generation cannot remain

remove Evaluation Criterion
  => Evaluation + Evidence cannot remain
```

### SCC contraction

```text
remove Learning      => remove Learned State
remove Learned State => remove Learning

remove Evaluation => remove Evidence
remove Evidence   => remove Evaluation
```

### Capability-only contraction

```text
remove Generation => no synthetic-output production
remove Constraint => no reusable prescriptive-rule capability
remove Execution  => no durable operational-realization capability
remove Provenance => no typed provenance/history capability
```

Do not move the removed concept's semantics into another concept to preserve a stale feature claim.

### Ordinary extension

Adding accepted concepts requires their current closure/side constraints. Examples:

```text
add Learning or Learned State => full L-KERNEL
add Generation                => Data Meaning + Strategy + Generation
add Evaluation or Evidence    => full E-KERNEL
add Execution                 => at least one valid domain activity
add Provenance                => meaningful relationship/history witness
```

Topology breadth and text-bearing structured data remain variations of existing concepts.

### Rediscovery boundary

Fresh concept discovery is required when new scope introduces a genuinely independent purpose/state/action lifecycle that current concepts cannot own cleanly. Current triggers include formal composable privacy/accounting, product-owned release governance, reusable request/cohort lifecycle, independent synthetic-output lifecycle, arbitrary graph relationship behavior, and product-owned resource/economic governance.

An implementation object, table, service, ID or status value is not enough to create a concept.

## Critical interpretation

A coherent concept subset or contraction/extension rule is not automatically:

- a package/module boundary;
- an installable edition;
- a deployable service set;
- a feature-flag bundle;
- a database/schema partition;
- a transaction boundary;
- a commercial SKU.

Do not create implementation topology from the application-family model while design remains incomplete.

## Current 009-E boundary

**009-E — Synchronization Inventory Revalidation Across the Application Family** is next eligible.

009-E must replay SYNC-01 through SYNC-15 against the now-closed D1-D4 authority and classify each rule as universal-when-applicable, family-conditional, over-broad, redundant, under-specified, unjustified, or evidence for a genuinely missing synchronization.

A synchronization must not recreate semantics belonging to a concept absent from a valid contraction.

Do not perform 009-F's detailed trigger/precondition/postcondition/state-owner audit early except where necessary to classify the inventory; 009-F owns that normalization after the inventory is settled.

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

This is not implementation ordering.

## Stop/reopen discipline

Follow J0-J7 in the methodology matrix. Reopen the smallest affected upstream authority for a real defect.

- J1 local concept defect → Phase 008 concept authority;
- J2 purpose/boundary/catalog defect → Phase 008-B/F/G as appropriate;
- J3 dependence/composition defect → repair in Phase 009 unless it proves an upstream cause.

## What agents may do now

For 009-E, agents may replay and classify the current synchronization inventory across valid family variants and contractions, identify over-broad/redundant/missing coordination, and record whether synchronization IDs survive unchanged, narrow, or are removed/replaced.

Architecture/source/tests may be inspected only as counterexample/feasibility evidence, not composition authority.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies, package-topology changes, or executable architecture restrictions merely to freeze evolving design.

Do not translate application-family subsets into package dependencies, product editions, deployment profiles, or feature flags.

Do not repair stale implementation tests solely to make implementation appear ready.

## Readiness rule

Phases 009-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**009-E — Synchronization Inventory Revalidation Across the Application Family**.

Do not begin implementation work.
