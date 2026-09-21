---
type: Phase Record
title: 009-B — Inclusion-Dependence Graph, Roots, Cycles & Explanation Ordering
status: complete
---

# 009-B — Inclusion-Dependence Graph, Roots, Cycles & Explanation Ordering

## Objective

Convert the complete 009-A pairwise inclusion-dependence inventory into the canonical direct/transitive graph, resolve mutual-dependence cycles, identify roots/leaves without ambiguity about edge direction, preserve non-binary prerequisites that cannot be expressed as ordinary pairwise edges, and establish an intelligible dependence-derived explanation/design ordering.

009-B is design-only. It does not derive the full application family, replay synchronizations, perform concept mapping, reconcile architecture, or authorize implementation.

## Governing authority

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Jackson Methodology Completion Matrix](../../authority/jackson-methodology-completion-matrix.md)
- [Phase 008 Individual-Concept Design Consolidation](../../concepts/phase-008-individual-concept-consolidation.md)
- [009-A Pairwise Inclusion-Dependence Inventory](../../dependence/inclusion-dependence-pairwise-inventory.md)
- [Phase 009 Entry / Decomposition](009-entry-decomposition.md)

009-B establishes current graph authority:

- [Inclusion-Dependence Graph, Strong Components & Explanation Ordering](../../dependence/inclusion-dependence-graph-ordering.md)

## Entry baseline

009-B entered after 009-A from `main` at:

```text
cef36d81786ffa65a847852c87dff10087eea32d
```

Entry state:

```text
009-A                              COMPLETE
D1                                 PARTIAL — pairwise inventory complete; graph pending
D2                                 OPEN
D3                                 OPEN
D4                                 PARTIAL
pairwise universal findings        12
mutual-dependence candidates        2
accepted concepts                  11
accepted synchronizations          15
implementation readiness           NOT READY
implementation start               NOT STARTED
implementation next                NOT YET
```

## Methodology cross-check

009-B retains the Jackson distinction that concept dependence is contextual to an application family rather than intrinsic software coupling.

A cycle is therefore not automatically a modularity failure. Mutual inclusion can be legitimate when each concept remains independently specified yet, in the current application family, including either only makes sense if the other is also included.

This interpretation is consistent with Daniel Jackson's published dependency tutorial, which uses a mutual concept-dependence example to derive valid subsets while maintaining concept independence.

## Direct/transitive reduction result

The twelve 009-A pairwise universal findings reduce to nine direct universal edges:

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

Three pairwise universal findings are retained as transitive closure rather than duplicated direct edges:

```text
Learned State -> Data Meaning
  via Learned State -> Learning -> Data Meaning

Learned State -> Synthesis Strategy
  via Learned State -> Learning -> Synthesis Strategy

Evidence -> Evaluation Criterion
  via Evidence -> Evaluation -> Evaluation Criterion
```

The reduction therefore preserves all 009-A semantics while making the graph's actual direct structure visible.

## Mutual-dependence resolution

### Learning / Learned State

```text
Learning <-> Learned State
```

**Disposition: legitimate strongly connected inclusion component.**

The cycle does not merge the concepts:

- Learning owns derivation activity;
- Learned State owns the reusable durable result;
- their state/actions remain singular and separate;
- current application inclusion of either requires the other.

No J2 reopening is justified.

### Evaluation / Evidence

```text
Evaluation <-> Evidence
```

**Disposition: legitimate strongly connected inclusion component.**

The cycle does not merge the concepts:

- Evaluation owns the examination activity/method/lifecycle;
- Evidence owns the durable finding;
- their state/actions remain singular and separate;
- current application inclusion of either requires the other.

No J2 reopening is justified.

## Condensed graph

Define:

```text
L-CLUSTER = { Learning, Learned State }
E-CLUSTER = { Evaluation, Evidence }
```

The condensed universal graph is:

```text
L-CLUSTER  -> Data Meaning
L-CLUSTER  -> Synthesis Strategy

Generation -> Data Meaning
Generation -> Synthesis Strategy

E-CLUSTER  -> Evaluation Criterion

Constraint  [no universal pairwise edge]
Execution   [no universal pairwise edge; side constraint]
Provenance  [no universal pairwise edge; side constraint]
```

The condensed graph is acyclic.

## Roots/leaves disposition

Because the graph points dependent -> required, 009-B uses explicit terms.

### Inclusion roots

No incoming universal edge in the condensed graph:

```text
L-CLUSTER
Generation
Constraint
E-CLUSTER
Execution
Provenance
```

These are not automatically standalone applications.

### Dependency leaves / prerequisite foundations

No outgoing universal edge:

```text
Data Meaning
Synthesis Strategy
Constraint
Evaluation Criterion
Execution
Provenance
```

Constraint, Execution, and Provenance are isolated only in the **universal pairwise graph** and therefore require application-family interpretation rather than naive standalone treatment.

## Non-binary prerequisite layer

009-B explicitly refuses to flatten these requirements into unconditional edges.

### Execution

```text
Execution => Learning OR Generation OR Evaluation
```

Execution is meaningful only as operational realization of committed domain work, but no one activity is universally required.

### Provenance

```text
Provenance => at least one meaningful provenance-bearing relationship
              involving current SYNGAN concept state/result/history
```

No one accepted concept is universally required across every valid provenance use.

### Conditional capability constraints retained

- learned-state-assisted Generation requires Learned State and therefore the L-CLUSTER closure;
- evaluation-gated Generation requires Evaluation Criterion plus the E-CLUSTER;
- variants advertising reusable prescriptive-rule functionality include Constraint;
- variants advertising durable operational retry/recovery/cancellation for activities include Execution;
- subject-specific Criteria/Evaluations/Evidence may conditionally require Data Meaning, Constraint, Generation, or Learned State.

These constraints belong to 009-C application-family derivation and are not graph edges.

## Explanation/design ordering

The graph establishes a partial order rather than one mandatory sequence.

Strict universal prerequisite constraints are:

```text
Data Meaning before Learning / Learned State
Synthesis Strategy before Learning / Learned State
Data Meaning before Generation
Synthesis Strategy before Generation
Evaluation Criterion before Evaluation / Evidence
```

Within strongly connected components, 009-B adopts narrative order rather than inventing a new edge:

```text
Learning before Learned State
Evaluation before Evidence
```

Recommended layered explanation:

```text
Layer 0
  Data Meaning
  Synthesis Strategy
  Constraint
  Evaluation Criterion

Layer 1
  Learning
  Learned State
  Generation
  Evaluation
  Evidence

Layer 2
  Execution
  Provenance
```

This order is for intelligible design explanation/mapping. It is not a package, runtime, persistence, API, or implementation order.

## D1/D3 methodology closure

009-B closes:

```text
D1  CURRENTLY CLOSED — canonical application inclusion-dependence graph established
D3  CURRENTLY CLOSED — dependence-derived explanation/design ordering established
```

D2 remains open for 009-C application-family derivation.

D4 remains partial for 009-C/009-D contraction/extension consequences.

No E-row is advanced.

## No catalog or synchronization change

```text
accepted concepts          11
accepted synchronizations  15
concept add/remove          NONE
concept merge/split/rename  NONE
synchronization change      NONE
```

The two strongly connected components do not justify concept merger.

## No executable or architecture change

009-B introduces no production source, tests, dependencies, lockfiles, CI/workflows, package topology, persistence/data-plane schemas, runtime/model/platform/security adapters, APIs, algorithms, privacy mechanisms, or architecture ADR decisions.

The dependence graph MUST NOT be copied mechanically into package/module dependencies.

## Exit assessment

```text
009-B DIRECT/TRANSITIVE REDUCTION          PASS
PAIRWISE UNIVERSAL FINDINGS                12
DIRECT UNIVERSAL EDGES                      9
TRANSITIVE UNIVERSAL FINDINGS               3
NON-TRIVIAL STRONGLY CONNECTED COMPONENTS   2
UNRESOLVED GRAPH CYCLE DEFECTS              0
D1                                          CURRENTLY CLOSED
D2                                          OPEN
D3                                          CURRENTLY CLOSED
D4                                          PARTIAL
UNRESOLVED J1/J2/J3 BLOCKER                 NONE FOUND
JACKSON CONCEPT DESIGN                      NOT COMPLETE
IMPLEMENTATION READINESS                    NOT READY
IMPLEMENTATION START                        NOT STARTED
IMPLEMENTATION NEXT                         NOT YET
```

## Next subgroup

**009-C — Application Family, Valid Concept Subsets & Minimal Coherent Variants** is the next eligible subgroup.

009-C must derive valid/invalid subsets from both the universal graph closure and the non-binary/conditional prerequisite layer rather than treating graph closure alone as sufficient.
