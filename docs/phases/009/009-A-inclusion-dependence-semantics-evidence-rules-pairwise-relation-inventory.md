---
type: Phase Record
title: 009-A — Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory
status: complete
---

# 009-A — Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory

## Objective

Establish the current Jackson application inclusion-dependence test and classify all materially plausible directed concept pairs without mistaking reference, validation, production, operational realization, provenance, synchronization, or implementation dependency for application inclusion dependence.

009-A is design-only. It does not build the final graph, derive the application family, replay synchronizations, map interfaces, reconcile architecture, or authorize implementation.

## Governing authority

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Jackson Methodology Completion Matrix](../../authority/jackson-methodology-completion-matrix.md)
- [Phase 008 Individual-Concept Design Consolidation](../../concepts/phase-008-individual-concept-consolidation.md)
- [Concept-Justification Traceability](../../problem/concept-justification-traceability.md)
- [Accepted Concept Catalog](../../concepts/index.md)
- [Phase 009 Entry / Decomposition](009-entry-decomposition.md)

009-A establishes the current dependence authority:

- [Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory](../../dependence/inclusion-dependence-pairwise-inventory.md)

## Entry baseline

009-A entered from `main` after the Phase 009 decomposition at:

```text
8ed6a64dabf7daf29a0067cc1e23612f30444d8f
```

Entry methodology state:

```text
D1 inclusion-dependence graph     OPEN
D2 application family             OPEN
D3 explanation ordering           OPEN
D4 add/remove consequences        PARTIAL
E1-E3 composition/sync            REVALIDATION REQUIRED
E4 synergy                        PARTIAL
E5 integrity                      PARTIAL TO STRONG
```

## Inclusion-dependence rule

009-A uses the application-purpose question:

> **If concept C1 is included, does including C1 make sense only if concept C2 is also included?**

The relation is not inferred from:

- one concept referencing another;
- validation or compatibility checks;
- production/result relationships;
- runtime realization;
- provenance records;
- synchronization existence;
- package imports, APIs, tables, files, jobs, or services;
- the fact that the full product currently deploys both concepts.

## Classification result

Every directed non-self pair among the eleven accepted concepts is classified as `D`, `N`, or `C`; no pair remains `I`/insufficient at 009-A exit.

```text
DEPENDS (D)                 12
CONDITIONAL/DISJUNCTIVE     43
DOES NOT DEPEND (N)         55
INSUFFICIENT (I)             0
```

The counts are diagnostic only.

## Universal pairwise dependence candidates

009-A identifies:

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

009-A intentionally does not yet decide which are direct versus transitive graph edges.

## Mutual-dependence findings

Two pairings are mutually dependent at the pairwise level:

```text
Learning   <-> Learned State
Evaluation <-> Evidence
```

These do not automatically invalidate Phase 008 boundaries. Phase 008 established independent activity/result purposes for both pairs.

009-B must determine whether each pair forms a legitimate strongly connected inclusion cluster, should be represented differently through direct/transitive edges, or reveals a genuine J2 boundary problem.

## Key conditional/disjunctive findings

### Direct versus learned Generation

Generation does not universally depend on Learning/Learned State because direct-generation Strategies are explicitly valid.

Learned-state-assisted Generation makes those concepts conditionally required.

### Constraint optionality

Learning/Generation may bind applicable Constraints, but valid workflows with no reusable Constraint exist.

### Evaluation-gated Generation

Generation may conditionally require Criterion/Evaluation/Evidence when its completion contract demands validation evidence, but no-evaluation-gate Generation remains valid.

### Execution disjunction

Execution cannot stand as a generic scheduler concept. It realizes one committed domain activity from:

```text
{ Learning, Generation, Evaluation }
```

No one activity is a universal pairwise prerequisite because any supported member may be the realized activity.

### Provenance disjunction

Provenance requires meaningful canonical/external subjects and relationships, but no one accepted concept is universally required. It therefore has a non-binary/disjunctive application-family prerequisite rather than ten unconditional pairwise edges.

### Criteria/Evaluation/Evidence subject conditions

These may conditionally require Data Meaning, Constraint, Learned State, or Generation depending on the committed question/subject/reference context, but none of those subject concepts is universal to all evaluations/findings.

## Counterexample witnesses retained

009-A preserves current counterexamples including:

- direct Generation without Learning/Learned State;
- Generation without reusable Constraint;
- Generation without mandatory evaluation-gated completion;
- Evaluation of Learned State/reference rather than Generation output;
- Criterion definition before any Evaluation;
- trivial/local activity realization without durable Execution;
- Provenance over different concept combinations across variants.

These are pairwise counterexamples only. 009-C will determine which complete subsets constitute valid/minimal application-family variants.

## Important methodological consequence

The inclusion-dependence relation is materially **sparser** than SYNGAN's historical dependency/synchronization relationships.

This confirms the Phase 009 entry correction: reference/validation/production/runtime/provenance structure cannot be reused as the Jackson dependence graph.

## No upstream defect found

009-A finds no J1 local concept-specification defect and no J2 purpose/boundary/catalog defect requiring Phase 008 reopening.

The two mutual-dependence pairs are explicit 009-B graph questions, not hidden defects.

## Methodology disposition

009-A advances D1 to:

```text
D1  PARTIAL — PAIRWISE INCLUSION SEMANTICS / INVENTORY COMPLETE;
              DIRECT/TRANSITIVE GRAPH + CYCLE TREATMENT PENDING 009-B
```

D2 and D3 remain open.

D4 remains partial, now with additional counterexample evidence, but awaits application-family/contraction work in 009-C/D.

No E-row composition obligation is closed by 009-A.

## No catalog or synchronization change

```text
accepted concepts          11
accepted synchronizations  15
concept add/remove          NONE
concept merge/split/rename  NONE
synchronization change      NONE
```

The fifteen synchronization rules remain current composition candidates for later 009-E replay.

## No executable or architecture changes

009-A introduces no production source, tests, dependencies, lockfiles, CI/workflows, package topology, persistence/data-plane schemas, runtime/model/platform/security adapters, APIs, algorithms, privacy mechanisms, or ADR decisions.

Retained architecture remains downstream evidence only.

## Exit assessment

```text
009-A INCLUSION SEMANTICS                  PASS
PAIRWISE DIRECTED RELATIONS                CLASSIFIED 110 / 110
UNIVERSAL DEPENDENCE CANDIDATES            12
CONDITIONAL / DISJUNCTIVE RELATIONS        43
NON-DEPENDENT RELATIONS                    55
INSUFFICIENT RELATIONS                     0
MUTUAL-DEPENDENCE PAIRS                    2
UNRESOLVED J1/J2 BLOCKER                   NONE FOUND
D1                                         PARTIAL — GRAPH PENDING
D2                                         OPEN
D3                                         OPEN
D4                                         PARTIAL
JACKSON CONCEPT DESIGN                     NOT COMPLETE
IMPLEMENTATION READINESS                   NOT READY
IMPLEMENTATION START                       NOT STARTED
IMPLEMENTATION NEXT                        NOT YET
```

## Next subgroup

**009-B — Inclusion-Dependence Graph, Roots, Cycles & Explanation Ordering** is the next eligible subgroup.

009-B must derive graph directness/transitivity and explicitly resolve the two mutual-dependence pairs without using implementation structure as graph authority.
