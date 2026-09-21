---
type: Phase Record
title: 009-C — Application Family, Valid Concept Subsets & Minimal Coherent Variants
status: complete
---

# 009-C — Application Family, Valid Concept Subsets & Minimal Coherent Variants

## Objective

Derive SYNGAN's current Jackson-style application family from the 009-B canonical inclusion-dependence graph and the non-binary/conditional prerequisite layer.

009-C determines which reduced concept subsets are coherent, which capability claims require additional concepts, which minimal kernels are meaningful, and which representative subsets are invalid.

009-C is design-only. It does not perform the full add/remove consequence audit, replay synchronizations, map interfaces, reconcile architecture, or authorize implementation.

## Governing authority

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Jackson Methodology Completion Matrix](../../authority/jackson-methodology-completion-matrix.md)
- [Phase 008 Individual-Concept Design Consolidation](../../concepts/phase-008-individual-concept-consolidation.md)
- [009-A Pairwise Inclusion-Dependence Inventory](../../dependence/inclusion-dependence-pairwise-inventory.md)
- [009-B Canonical Dependence Graph](../../dependence/inclusion-dependence-graph-ordering.md)
- [Phase 009 Entry / Decomposition](009-entry-decomposition.md)

009-C establishes current application-family authority:

- [Application Family, Valid Concept Subsets & Minimal Coherent Variants](../../dependence/application-family-valid-subsets.md)

## Entry baseline

009-C entered from `main` after 009-B at:

```text
6475b5b65200217615040e6e4a70cc81b4fc5d1a
```

Entry methodology state:

```text
D1  CURRENTLY CLOSED
D2  OPEN
D3  CURRENTLY CLOSED
D4  PARTIAL
E1-E5  NOT CLOSED BY DEPENDENCE WORK
```

## Family derivation rule

A non-empty subset is a coherent current application-family member only when it:

1. is closed under the canonical universal graph;
2. satisfies the Execution one-of prerequisite when Execution is present;
3. satisfies the Provenance semantic-witness prerequisite when Provenance is present;
4. includes every concept required by any capability it explicitly claims;
5. preserves current Phase 008 concept purposes and boundaries.

This distinguishes concept-family validity from implementation packaging or commercial product editions.

## Universal closure rules retained

### Learning / Learned State

```text
Learning in S iff Learned State in S
Learning or Learned State => Data Meaning + Synthesis Strategy
```

Minimal learning capability:

```text
L-KERNEL = {
  Data Meaning,
  Synthesis Strategy,
  Learning,
  Learned State
}
```

### Generation

```text
Generation => Data Meaning + Synthesis Strategy
```

Minimal direct-generation capability:

```text
G-KERNEL = {
  Data Meaning,
  Synthesis Strategy,
  Generation
}
```

### Evaluation / Evidence

```text
Evaluation in S iff Evidence in S
Evaluation or Evidence => Evaluation Criterion
```

Minimal evaluation capability:

```text
E-KERNEL = {
  Evaluation Criterion,
  Evaluation,
  Evidence
}
```

## Non-binary rules retained

### Execution

```text
Execution => Learning OR Generation OR Evaluation
```

Execution alone is invalid. Minimal unambiguous Execution-bearing variants are:

```text
GX-KERNEL = G-KERNEL + Execution
LX-KERNEL = L-KERNEL + Execution
EX-KERNEL = E-KERNEL + Execution
```

### Provenance

Provenance requires at least one meaningful provenance-bearing relationship involving SYNGAN state/result/history. No one accepted concept is universally required.

`{ Provenance }` is invalid.

Canonical unambiguous provenance-bearing examples include G-KERNEL, L-KERNEL, or E-KERNEL plus Provenance when the corresponding derivation/binding/evaluation relationship exists.

## Authority-only coherent minima

009-C accepts these standalone authority-definition/inspection family members:

```text
{ Data Meaning }
{ Synthesis Strategy }
{ Constraint }
{ Evaluation Criterion }
```

These are coherent concept subsets even though they do not provide synthetic generation by themselves.

The empty set is not a meaningful SYNGAN application-family member.

## Capability-conditional variants

### Learned-state-assisted Generation

```text
L-KERNEL + Generation
```

is the minimum current learned-generation variant.

### Evaluation-gated Generation

```text
G-KERNEL + E-KERNEL
```

is the minimum concept closure when Generation completion requires evaluation-backed Evidence.

### Reusable Constraint support

Constraint is included when a variant claims reusable prescriptive-rule definition/binding. Constraint remains optional otherwise.

### Durable operational lifecycle

Execution is included when a variant claims durable retry/recovery/cancellation/indeterminate operational history and must satisfy its one-of prerequisite.

### Provenance/history capability

Provenance is included only where a meaningful typed relationship/history witness exists.

### Topology/text capability

Time-series, multi-table shared-key, composite structured topology, and text-bearing structured data do not force new concepts. They vary current Data Meaning/Strategy/Generation and optional Learning/Constraint/Evaluation semantics.

## Required scenario results

### Direct Generation

```text
{ Data Meaning, Synthesis Strategy, Generation }
```

**VALID.**

Confirms no universal Generation -> Learning/Learned State dependence.

### Learned-state-assisted Generation

```text
{ Data Meaning, Synthesis Strategy, Learning, Learned State, Generation }
```

**VALID.**

### Constraint-light Generation/Learning

G-KERNEL and L-KERNEL without Constraint are **VALID** when no reusable prescriptive-rule capability is claimed.

### Evaluation-focused application

```text
{ Evaluation Criterion, Evaluation, Evidence }
```

**VALID** for supported external/reference or integration-provided subjects. Generation is not universal.

### Execution-bearing variants

GX-KERNEL, LX-KERNEL, and EX-KERNEL are **VALID**.

`{ Execution }` and `{ Data Meaning, Synthesis Strategy, Execution }` are **INVALID**.

### Provenance-bearing variants

G/L/E kernels plus Provenance are **VALID when a corresponding typed relationship exists**.

`{ Provenance }` is **INVALID**.

### Topology-bearing direct generation

G-KERNEL remains conceptually sufficient where the selected Strategy itself supports the requested topology.

No standalone Relationship/TimeSeries/Table concept is required.

### Text-bearing structured data

G-KERNEL is valid for direct self-contained text-capable synthesis. L-KERNEL + Generation is valid for source-derived reusable text-capable synthesis.

No Text/Tokenizer/Language Model concept is restored.

## Representative invalid closures

009-C records the following invalid classes:

```text
{ Data Meaning, Synthesis Strategy, Learning }
  invalid — missing Learned State

{ Data Meaning, Synthesis Strategy, Learned State }
  invalid — missing Learning

{ Synthesis Strategy, Generation }
  invalid — missing Data Meaning

{ Data Meaning, Generation }
  invalid — missing Synthesis Strategy

{ Evaluation Criterion, Evaluation }
  invalid — missing Evidence

{ Evaluation Criterion, Evidence }
  invalid — missing Evaluation

{ Evaluation, Evidence }
  invalid — missing Evaluation Criterion

{ Execution }
  invalid — no realizable domain activity

{ Provenance }
  invalid — no meaningful provenance-bearing relationship
```

A subset may also be generally coherent but invalid for a stronger capability claim. G-KERNEL, for example, is valid direct Generation but invalid when advertised as learned-state-assisted or evaluation-gated Generation without the corresponding closures.

## Important design conclusion

The current application family is **not one mandatory eleven-concept application**.

It is a rule-defined family of coherent non-empty subsets. Universal graph closure establishes the structural floor; side constraints and capability claims determine whether a particular family member is semantically valid for its advertised functionality.

This preserves concept independence while making legitimate co-inclusion explicit.

## No upstream defect found

009-C finds no J1/J2/J3 defect requiring Phase 008 or 009-A/B reopening.

The current graph supports meaningful reduced variants without forcing concept merger, synthetic dependencies, or a hidden generic Work/Artifact/Relationship concept.

## Methodology disposition

009-C closes D2:

```text
D2  CURRENTLY CLOSED — meaningful valid concept subsets/application family established
```

D1 and D3 remain currently closed from 009-B.

D4 advances to:

```text
D4  PARTIAL TO STRONG — family closure, minimum variants, invalid subsets,
                        and representative add/remove implications established;
                        systematic contraction/extension audit pending 009-D
```

No E-row is closed by 009-C.

## No catalog or synchronization change

```text
accepted concepts          11
accepted synchronizations  15
concept add/remove          NONE
concept merge/split/rename  NONE
synchronization change      NONE
```

## No executable or architecture change

009-C introduces no production source, tests, CI/workflows, dependencies, lockfiles, package topology, persistence/data-plane schemas, runtime/model/platform/security adapters, APIs, algorithms, privacy mechanisms, or architecture ADR decisions.

The application-family rules MUST NOT be copied mechanically into package/module editions while design remains incomplete.

## Exit assessment

```text
009-C APPLICATION FAMILY                    PASS
D1                                          CURRENTLY CLOSED
D2                                          CURRENTLY CLOSED
D3                                          CURRENTLY CLOSED
D4                                          PARTIAL TO STRONG
UNRESOLVED J1/J2/J3 BLOCKER                 NONE FOUND
JACKSON CONCEPT DESIGN                      NOT COMPLETE
IMPLEMENTATION READINESS                    NOT READY
IMPLEMENTATION START                        NOT STARTED
IMPLEMENTATION NEXT                         NOT YET
```

## Next subgroup

**009-D — Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences** is the next eligible subgroup.

009-D must systematically analyze how removing/adding each concept or strongly connected component changes the supported application family and distinguish ordinary family extension from future scope that requires fresh concept discovery.
