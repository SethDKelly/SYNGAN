---
type: Phase Record
title: 009-D — Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences
status: complete
---

# 009-D — Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences

## Objective

Systematically determine how the current SYNGAN application family changes when concepts/components are removed or added, what capabilities must disappear or become available, and when an apparent extension requires fresh concept discovery instead of ordinary composition of the accepted catalog.

009-D is design-only. It does not replay synchronizations, perform concept mapping, reconcile architecture, change packaging, or authorize implementation.

## Governing authority

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Jackson Methodology Completion Matrix](../../authority/jackson-methodology-completion-matrix.md)
- [Phase 008 Individual-Concept Design Consolidation](../../concepts/phase-008-individual-concept-consolidation.md)
- [Catalog Perimeter Candidate Rediscovery Audit](../../concepts/catalog-perimeter-candidate-rediscovery-boundary-audit.md)
- [009-A Pairwise Inclusion-Dependence Inventory](../../dependence/inclusion-dependence-pairwise-inventory.md)
- [009-B Canonical Dependence Graph](../../dependence/inclusion-dependence-graph-ordering.md)
- [009-C Application Family](../../dependence/application-family-valid-subsets.md)
- [Phase 009 Entry / Decomposition](009-entry-decomposition.md)

009-D establishes current consequence authority:

- [Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences](../../dependence/contraction-extension-consequences.md)

## Entry baseline

009-D entered after 009-C from `main` at:

```text
a4dca56414af8040ce84f403ae09111b6be65de4
```

Entry methodology state:

```text
D1  CURRENTLY CLOSED
D2  CURRENTLY CLOSED
D3  CURRENTLY CLOSED
D4  PARTIAL TO STRONG
E1-E5  NOT CLOSED BY DEPENDENCE WORK
```

## Contraction rule

Removing a concept requires replay of:

1. universal dependence closure;
2. SCC co-inclusion;
3. Execution's one-of prerequisite;
4. Provenance's semantic-witness prerequisite;
5. capability-specific inclusion rules;
6. product/documentation claims.

A contraction is not valid merely because the remaining concept names form a set.

## Systematic removal results

### Data Meaning

Removing Data Meaning forces removal/re-scoping of:

```text
Learning
Learned State
Generation
```

A no-Data-Meaning variant cannot retain current Generation semantics by falling back to hidden physical/model interpretation.

### Synthesis Strategy

Removing Strategy likewise forces removal/re-scoping of:

```text
Learning
Learned State
Generation
```

Current Learning/Generation cannot replace Strategy authority with an implicit algorithm implementation.

### Learning or Learned State

They form one SCC:

```text
remove Learning      => remove Learned State
remove Learned State => remove Learning
```

The product loses learned-state derivation/reuse but may retain direct Generation.

### Generation

Generation can be removed without universal forced removal of another concept.

The variant loses synthetic-output production and Generation-owned request/Condition/completion semantics but may retain Learning/Learned State, Evaluation, authorities, appropriate Execution, and Provenance.

### Constraint

Constraint removal forces no universal concept removal but removes reusable prescriptive-rule capability.

Mandatory rules cannot be hidden in Strategy, Data Meaning, Generation Condition, or Evaluation to simulate the removed concept.

### Evaluation Criterion

Removing Criterion forces removal of:

```text
Evaluation
Evidence
```

The product loses evidence-producing evaluation and evaluation-gated Generation.

### Evaluation or Evidence

They form one SCC:

```text
remove Evaluation => remove Evidence
remove Evidence   => remove Evaluation
```

Criterion may remain as an unanswered reusable question/standard.

### Execution

Removing Execution forces no universal concept removal but removes durable operational realization, Attempt/retry/recovery/cancellation/indeterminate-history capability.

Those semantics must not migrate into domain activities merely because Execution is absent.

### Provenance

Removing Provenance forces no universal concept removal but removes typed cross-concept historical relationship traversal.

Concept-local immutable commitments/history remain required.

## Side-constraint contraction findings

### Execution orphaning

If a contraction leaves Execution but removes all of Learning, Generation and Evaluation, the result is invalid. Repair requires removing Execution or restoring a valid activity closure.

### Provenance orphaning

If contraction removes every meaningful relationship/history witness the variant intended to expose, Provenance must also be removed or re-scoped around a surviving legitimate relationship.

### Capability-claim orphaning

A subset may remain structurally coherent while its previous product claim becomes invalid.

Examples:

```text
remove L-CLUSTER
  => direct Generation may remain
  => learned-state-assisted claim must disappear

remove E-CLUSTER
  => Generation may remain
  => evaluation-gated claim must disappear

remove Constraint
  => Generation may remain
  => reusable prescriptive-rule claim must disappear
```

## Systematic extension results

### Independent additions

These may be added without universal prerequisite closure:

```text
Data Meaning
Synthesis Strategy
Constraint
Evaluation Criterion
```

They add their own authority capability only.

### Add Learning or Learned State

Either addition requires full L-KERNEL closure:

```text
Data Meaning
Synthesis Strategy
Learning
Learned State
```

### Add Generation

Requires:

```text
Data Meaning
Synthesis Strategy
Generation
```

at minimum.

### Add Evaluation or Evidence

Either requires E-KERNEL closure:

```text
Evaluation Criterion
Evaluation
Evidence
```

### Add Execution

Requires at least one valid Learning, Generation or Evaluation activity in the resulting family member.

### Add Provenance

Requires a meaningful typed relationship/history witness.

## Ordinary family extension findings

The following are current-family extensions, not new concept discovery:

- direct Generation -> learned-state-assisted Generation by adding L-CLUSTER;
- Generation -> evaluation-gated Generation by adding E-KERNEL;
- adding reusable rules by adding Constraint;
- adding durable operational lifecycle by adding Execution;
- adding typed history by adding Provenance with a valid witness;
- expanding current structured topology within Data Meaning/Strategy/Generation/Constraint/Evaluation semantics;
- adding text-bearing structured-data capability through current concepts.

## Rediscovery boundary

Fresh concept discovery remains mandatory when new scope introduces an independent purpose/state/action lifecycle that current concepts cannot own without erosion.

Current explicit triggers retained from 008-G include:

- composable formal privacy/accounting state;
- product-owned governance/use/release decisions;
- independently reusable/negotiable request or cohort definitions;
- independent synthetic-output publication/versioning/retirement/transformation lifecycle;
- arbitrary recursive/graph topology that creates independent relationship behavior beyond current structured-topology semantics;
- product-owned resource/budget/quota/economic allocation/governance.

A new ID/table/service/status or implementation resource is not enough to trigger a concept.

## Product-scope consequence principle

The application family is capability-sensitive.

A concept may be optional across the family while mandatory for one advertised capability.

Therefore product/mapping documentation must track the actual contracted/extended family member and must not preserve stale claims after concepts are removed.

009-D does not decide commercial editions or implementation packages.

## Synchronization handoff

009-D leaves the synchronization set unchanged but supplies the family consequences 009-E must use.

For every SYNC-01..15, 009-E must determine whether the rule:

- applies whenever all participants are present;
- applies only in a narrower capability variant;
- disappears entirely when contraction removes its purpose;
- becomes relevant when extension adds its participants/capability;
- accidentally recreates state/capability owned by a concept contracted away.

## No upstream defect found

009-D finds no J1/J2/J3 defect requiring Phase 008, 009-A, 009-B, or 009-C reopening.

The current eleven concepts support systematic contraction and extension without requiring a hidden replacement concept or boundary erosion.

## Methodology disposition

009-D closes D4:

```text
D1  CURRENTLY CLOSED
D2  CURRENTLY CLOSED
D3  CURRENTLY CLOSED
D4  CURRENTLY CLOSED
```

No E-row is advanced by this subgroup.

## No catalog or synchronization change

```text
accepted concepts          11
accepted synchronizations  15
concept add/remove          NONE
concept merge/split/rename  NONE
new concept promoted        NONE
synchronization change      NONE
```

## No executable or architecture change

009-D introduces no production source, tests, CI/workflows, dependencies, lockfiles, package topology, persistence/data-plane schemas, runtime/model/platform/security adapters, APIs, algorithms, privacy mechanisms, packaging decisions, or architecture ADR decisions.

The consequence matrix is not implementation/package authority.

## Exit assessment

```text
009-D CONTRACTION / EXTENSION AUDIT         PASS
D1                                          CURRENTLY CLOSED
D2                                          CURRENTLY CLOSED
D3                                          CURRENTLY CLOSED
D4                                          CURRENTLY CLOSED
UNRESOLVED J1/J2/J3 BLOCKER                 NONE FOUND
JACKSON CONCEPT DESIGN                      NOT COMPLETE
IMPLEMENTATION READINESS                    NOT READY
IMPLEMENTATION START                        NOT STARTED
IMPLEMENTATION NEXT                         NOT YET
```

## Next subgroup

**009-E — Synchronization Inventory Revalidation Across the Application Family** is the next eligible subgroup.

009-E must now replay the current fifteen synchronization candidates against the completed dependence/application-family/contraction authority before any trigger/ownership deep audit in 009-F.
