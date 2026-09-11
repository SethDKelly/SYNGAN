---
type: Concept Dependence Authority
title: Inclusion-Dependence Graph, Strong Components & Explanation Ordering
status: active
---

# Inclusion-Dependence Graph, Strong Components & Explanation Ordering

## Purpose

Establish the current canonical Jackson-style application inclusion-dependence graph for SYNGAN from the pairwise evidence accepted in Phase 009-A.

This authority resolves:

- direct versus transitive universal dependence;
- treatment of mutual-dependence cycles;
- graph roots/leaves under the chosen edge direction;
- non-binary/disjunctive prerequisites that must not be flattened into false pairwise edges;
- the dependence-derived explanation/design ordering to be used by later application-family work.

It does **not** yet enumerate or approve all valid concept subsets. Phase 009-C owns systematic application-family derivation.

## Governing authority

- [Concept Design Methodology](../authority/design-methodology.md)
- [Phase 008 Individual-Concept Design Consolidation](../concepts/phase-008-individual-concept-consolidation.md)
- [Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory](inclusion-dependence-pairwise-inventory.md)
- [Phase 009 Entry / Decomposition](../phases/009/009-entry-decomposition.md)

## Edge semantics

The canonical graph preserves the Phase 009-A direction:

```text
C1 -> C2
```

means:

> an application that includes `C1` cannot preserve `C1`'s current SYNGAN purpose coherently if `C2` is absent.

The arrow points from the **dependent concept** toward its **required concept**.

This is application inclusion dependence, not implementation, import, runtime, storage, reference, validation, production, provenance, or synchronization dependence.

## Direct-edge rule

A pairwise `D` relation becomes a **direct canonical edge** only when the required concept is not already forced by another direct universal path from the dependent concept.

A pairwise `D` relation that follows through another universal path is retained as **transitive closure evidence** rather than duplicated as a direct edge.

This keeps the canonical graph minimal enough to expose the application-family structure without losing any accepted pairwise dependence.

---

# 1. Canonical direct universal graph

009-B accepts the following **9 direct universal edges**:

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

No other unconditional direct edge is currently justified.

## 1.1 Transitive pairwise dependencies

The following 009-A universal pairwise findings are real but **transitive** in the canonical graph:

```text
Learned State -> Data Meaning
  via Learned State -> Learning -> Data Meaning

Learned State -> Synthesis Strategy
  via Learned State -> Learning -> Synthesis Strategy

Evidence -> Evaluation Criterion
  via Evidence -> Evaluation -> Evaluation Criterion
```

Therefore the 009-A totals reconcile as:

```text
pairwise universal dependence findings   12
direct universal graph edges              9
transitive universal findings             3
```

## 1.2 Why directness matters

Duplicating transitive edges would make the graph look more tightly coupled than the application semantics actually require and would obscure which concept boundary explains the requirement.

For example, Learned State requires Data Meaning because current Learned State can only exist through Learning, and current Learning requires explicit Data Meaning. That does not require Learned State to acquire a second independent purpose relationship to Data Meaning.

---

# 2. Strongly connected components and cycle treatment

The direct graph contains exactly two non-trivial strongly connected components.

## 2.1 Learning / Learned State component

```text
Learning <-> Learned State
```

Current interpretation: **legitimate mutual application inclusion dependence**.

Reason:

- Learning remains independently specified as the domain activity that derives reusable source-informed state;
- Learned State remains independently specified as the reusable durable result after Learning completes;
- including Learning permanently without a Learned State concept would remove the accepted result authority that fulfills Learning's purpose;
- including Learned State without Learning would remove the accepted producing activity/history that defines what Learned State is under current scope.

The cycle therefore reflects application-family co-inclusion, not merged state ownership.

It does not authorize either concept to own the other's state/actions.

### Reopen trigger

Reopen the Phase 008 boundary only if future scope introduces a legitimate Learned State with no Learning provenance, or a legitimate Learning purpose whose completed reusable result is not Learned State.

Neither condition exists now.

## 2.2 Evaluation / Evidence component

```text
Evaluation <-> Evidence
```

Current interpretation: **legitimate mutual application inclusion dependence**.

Reason:

- Evaluation remains the committed examination activity;
- Evidence remains the durable interpretable finding;
- an application that includes Evaluation but permanently lacks Evidence would reduce valid examination to ephemeral metric/runtime output;
- current Evidence is defined as what an Evaluation validly established, not as an independently authored claim.

Again, mutual application inclusion does not merge behavior or state ownership.

### Reopen trigger

Reopen the Phase 008 boundary only if future scope introduces durable Evidence that is not established through Evaluation, or an Evaluation capability whose purpose no longer includes producing interpretable findings.

Neither condition exists now.

## 2.3 Cycle methodology rule

A mutual-dependence cycle is not automatically a design defect.

It is acceptable when:

1. each concept remains independently understandable and behaviorally coherent;
2. each retains a distinct purpose and state/action authority;
3. the cycle expresses that, **in this application family**, including either concept only makes sense when the other is also included;
4. synchronization does not transfer or duplicate state ownership.

The Learning/Learned State and Evaluation/Evidence cycles satisfy these conditions under current Phase 008 authority.

---

# 3. Condensed acyclic dependence graph

For application-family reasoning, each non-trivial strongly connected component can be treated as one inclusion unit without merging the concepts themselves.

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

Constraint        [no universal pairwise edge]
Execution         [no universal pairwise edge; non-binary prerequisite applies]
Provenance        [no universal pairwise edge; non-binary prerequisite applies]
```

The condensed graph is **acyclic**.

No J2 concept merge/split/rename is required to eliminate cycles.

---

# 4. Roots and leaves

Because arrows point from dependent concepts to required concepts, ordinary graph vocabulary can be misleading. 009-B therefore uses explicit definitions.

## 4.1 Inclusion roots

An **inclusion root** is a node/component with no incoming universal edge in the condensed graph. It represents a capability that is not universally required merely because another current concept is present.

Current inclusion roots/components are:

```text
L-CLUSTER       { Learning, Learned State }
Generation
Constraint
E-CLUSTER       { Evaluation, Evidence }
Execution
Provenance
```

This does **not** mean every root is a valid standalone application. Execution and Provenance have non-binary prerequisites recorded below, and Phase 009-C must validate complete subsets.

## 4.2 Dependency leaves / prerequisite foundations

A **dependency leaf** is a node/component with no outgoing universal edge in the condensed graph.

Current dependency leaves are:

```text
Data Meaning
Synthesis Strategy
Constraint
Evaluation Criterion
Execution
Provenance
```

Again, leaf status means only that no single other accepted concept is universally required by pairwise inclusion dependence. It is not a standalone-application verdict.

## 4.3 Isolated universal-graph nodes

The following nodes have neither incoming nor outgoing **universal pairwise** edges:

```text
Constraint
Execution
Provenance
```

They are not semantically equivalent:

- Constraint can be independently authored and becomes relevant only when an application includes prescriptive rules;
- Execution is meaningful only when operationally realizing at least one supported domain activity;
- Provenance is meaningful only when there is material history/relationship content to record or traverse.

009-C must therefore combine the universal graph with the non-binary constraints rather than treating isolated nodes as automatically standalone variants.

---

# 5. Non-binary and conditional prerequisites

A simple directed graph can represent universal pairwise dependence, but not all meaningful inclusion rules.

009-B therefore preserves a separate application-family constraint layer.

## 5.1 Execution one-of prerequisite

Execution is not a generic scheduler/workflow concept.

If Execution is included, the application must include at least one domain activity it can operationally realize:

```text
Execution
  => Learning OR Generation OR Evaluation
```

Because no one member is universally required, this rule MUST NOT be encoded as three unconditional pairwise edges.

If `Learning` is the selected activity, graph closure also includes Learned State, Data Meaning, and Synthesis Strategy.

If `Evaluation` is selected, graph closure also includes Evidence and Evaluation Criterion.

## 5.2 Provenance subject/relationship prerequisite

Provenance is not a generic metadata or lineage database.

If Provenance is included, the application must include enough canonical concept state/result/history to make at least one SYNGAN provenance relationship meaningful, potentially together with external identities.

Conceptually:

```text
Provenance
  => at least one meaningful provenance-bearing relationship
     involving current SYNGAN concept state/result/history
```

No single accepted concept is universally required across every valid Provenance use, so there is no unconditional pairwise edge.

## 5.3 Learned-state-assisted Generation

Direct Generation is valid, so no universal `Generation -> Learned State` edge exists.

For a variant that advertises learned-state-assisted Generation:

```text
learned-state-assisted Generation
  => Learned State
  => Learning
  => Data Meaning + Synthesis Strategy
```

This remains a capability-conditional application-family rule.

## 5.4 Evaluation-gated Generation

Generation does not universally require Evaluation.

If a Generation completion contract requires evaluation evidence before semantic completion:

```text
validation-gated Generation
  => Evaluation Criterion + Evaluation + Evidence
```

The Evaluation/Evidence mutual component remains intact.

## 5.5 Constraint-conditioned use

Constraint has no universal pairwise dependency and is not universally required by Learning or Generation.

A variant that advertises reusable prescriptive-rule support must include Constraint, and any activity claiming to bind such rules must preserve current Constraint ownership.

## 5.6 Operationally significant activities

Learning, Generation, and Evaluation do not universally depend on Execution because trivial/local realization is explicitly valid.

A variant that advertises durable retry/recovery/cancellation/indeterminate operational history for one of those activities conditionally includes Execution.

---

# 6. Dependence-derived explanation ordering

The dependence graph determines a **partial order**, not one mandatory linear sequence.

Because arrows point from dependent to prerequisite, intelligible explanation normally introduces prerequisites before dependents.

## 6.1 Strict universal ordering constraints

The canonical graph requires:

```text
Data Meaning        before Learning / Learned State
Synthesis Strategy  before Learning / Learned State

Data Meaning        before Generation
Synthesis Strategy  before Generation

Evaluation Criterion before Evaluation / Evidence
```

Within each strongly connected component, the graph cannot supply an internal topological order.

009-B therefore uses operational-purpose narrative order:

```text
Learning before Learned State
Evaluation before Evidence
```

This is an **explanation convention**, not an additional dependence edge and not state-ownership transfer.

## 6.2 Recommended layered explanation order

A current intelligible design explanation is:

### Layer 0 — reusable authorities / questions

1. Data Meaning
2. Synthesis Strategy
3. Constraint
4. Evaluation Criterion

These concepts can be explained independently and provide vocabulary used by later activities.

### Layer 1 — domain activities and durable results

5. Learning
6. Learned State
7. Generation
8. Evaluation
9. Evidence

Learning/Learned State and Evaluation/Evidence are explained adjacent because they form mutual inclusion components while retaining activity/result separation.

Generation follows Data Meaning/Strategy and can then be explained with both direct and learned-state-assisted variants.

### Layer 2 — cross-cutting operational/historical functionality

10. Execution
11. Provenance

Execution is best explained after at least one domain activity because of its one-of prerequisite.

Provenance is best explained after canonical states/results/activities exist to participate in typed historical relationships.

This layered order is recommended for design documentation and later concept mapping. It is not a package order, API order, persistence order, runtime startup order, or authorization to implement.

## 6.3 Alternative valid explanation sequences

Any explanation sequence is valid if it respects the strict universal prerequisite constraints and introduces enough context before Execution/Provenance to make their purpose intelligible.

For example, Evaluation Criterion/Evaluation/Evidence may be introduced before Generation in an evaluation-focused narrative, and Constraint may be introduced later in a direct-generation narrative where reusable prescriptive rules are not initially in scope.

---

# 7. Design/development-order interpretation

Jackson-style dependence can suggest an intelligible future development order, but SYNGAN is still in design and implementation remains suspended.

The only current design conclusion is:

- establish prerequisite concept semantics before reasoning about dependent application variants;
- treat mutual components as co-inclusion units for application-family analysis;
- do not force code/package dependencies to mirror this graph;
- do not start implementation from this ordering.

Any later implementation decomposition must be derived only after Phases 012-014 complete and may use different technical dependency directions while preserving conceptual behavior.

---

# 8. 009-C handoff rules

Phase 009-C must derive the application family using **both**:

1. closure under the canonical universal graph; and
2. the non-binary/conditional prerequisite layer.

At minimum 009-C must test:

- standalone/reduced authority-definition variants such as Data Meaning, Strategy, Constraint, and Criterion where meaningful;
- the minimal Learning/Learned State capability closure;
- minimal direct Generation capability closure;
- learned-state-assisted Generation;
- Evaluation/Evidence capability closure;
- Execution-bearing variants satisfying the one-of rule;
- Provenance-bearing variants with meaningful relationship subjects;
- optional Constraint and evaluation-gated Generation extensions;
- invalid subsets that violate graph closure or side constraints.

009-C must not infer validity solely from graph closure where a non-binary prerequisite applies.

---

# 9. Current methodology disposition

009-B closes the current graph/order obligations:

```text
D1  CURRENTLY CLOSED — canonical universal inclusion-dependence graph established
D3  CURRENTLY CLOSED — dependence-derived explanation/design ordering established
```

D2 remains open for systematic application-family derivation in 009-C.

D4 remains partial pending contraction/extension consequences in 009-C/009-D.

No E-row composition obligation is closed by 009-B.

## Current counts

```text
accepted concepts                         11
pairwise universal dependence findings   12
direct universal graph edges              9
transitive universal findings             3
non-trivial strongly connected components 2
unresolved graph cycle defects             0
concept catalog changes                    0
synchronization changes                    0
```

## Exit boundary

The canonical graph is current design authority but remains reopenable if 009-C/D application-family analysis exposes a genuine J2/J3 misfit.

Implementation remains:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```
