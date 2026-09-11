---
type: Concept Dependence Authority
title: Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory
status: active
---

# Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory

## Purpose

Provide the current Phase 009-A authority for identifying **Jackson application inclusion dependence** among SYNGAN's eleven accepted concepts without confusing it with reference, validation, production, operational, provenance, import, storage, or runtime dependency.

This document classifies every directed non-self concept pair as:

- `D` — universal inclusion dependence;
- `N` — no universal inclusion dependence;
- `C` — conditional or disjunctive requirement rather than a universal pairwise edge;
- `I` — insufficient evidence.

009-A determines the pairwise relation inventory only. Direct versus transitive edges, cycle treatment, roots/leaves, and explanation ordering remain 009-B work.

## Governing question

For concepts `C1` and `C2` in an application variant `A`:

> **If `C1` is included, does including `C1` make sense only if `C2` is also included?**

`C1 -> C2` means the application cannot preserve `C1`'s current purpose while omitting `C2`.

## Inclusion versus occurrence

Concept inclusion is not the same as concept occurrence.

Examples:

- direct Generation can exist without any Learning/Learned State occurrence;
- a Generation may bind zero reusable Constraints;
- an Evaluation may concern Learned State or another subject rather than Generation output;
- an activity may be realized locally without a durable Execution occurrence;
- a reusable Criterion may be defined before any Evaluation exists.

A relation does not become universal merely because one workflow uses both concepts.

## Evidence rules for `D`

A `D` finding requires all of the following:

1. the row concept's current purpose cannot be fulfilled coherently with the column concept absent;
2. the requirement follows from concept semantics, not architecture or implementation convenience;
3. no accepted current counterexample preserves the row concept's purpose while omitting the column;
4. the relation is more than reference, validation, production, runtime realization, provenance, or synchronization;
5. the conclusion survives Phase 008's no-occurrence and boundary findings.

The following are insufficient by themselves:

- storing another concept's identity;
- querying or validating another concept;
- being produced before/after another concept;
- synchronizing with another concept;
- package imports, service calls, storage references, or API parameters;
- deployment of both concepts in the full product.

## Pairwise matrix

Abbreviations:

```text
DM   Data Meaning
SS   Synthesis Strategy
LRN  Learning
LS   Learned State
GEN  Generation
CON  Constraint
CRI  Evaluation Criterion
EVA  Evaluation
EVD  Evidence
EXE  Execution
PRO  Provenance
```

Legend: `D` depends, `N` does not universally depend, `C` conditional/disjunctive, `—` self.

| From \\ To | DM | SS | LRN | LS | GEN | CON | CRI | EVA | EVD | EXE | PRO |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **DM**  | — | N | N | N | N | N | N | N | N | N | N |
| **SS**  | C | — | C | N | C | C | N | N | N | N | N |
| **LRN** | D | D | — | D | N | C | N | N | N | C | N |
| **LS**  | D | D | D | — | N | C | N | N | N | N | N |
| **GEN** | D | D | C | C | — | C | C | C | C | C | N |
| **CON** | C | N | N | N | C | — | N | N | N | N | N |
| **CRI** | C | N | N | C | C | C | — | N | N | N | N |
| **EVA** | C | N | N | C | C | C | D | — | D | C | N |
| **EVD** | C | N | N | C | C | C | D | D | — | N | C |
| **EXE** | N | N | C | N | C | N | N | C | N | — | N |
| **PRO** | C | C | C | C | C | C | C | C | C | C | — |

Across the 110 directed non-self pairs:

```text
DEPENDS (D)                 12
CONDITIONAL/DISJUNCTIVE     43
DOES NOT DEPEND (N)         55
INSUFFICIENT (I)             0
```

The counts are diagnostic only. The important result is that universal inclusion dependence is substantially sparser than the historical SYNGAN dependency/synchronization graph.

## Universal dependence candidates

### Learning -> Data Meaning — `D`

Learning derives reusable source-informed state according to accepted source meaning and binds Data Meaning at commitment. Removing Data Meaning would force Learning to depend on hidden source interpretation and would weaken its accepted purpose.

### Learning -> Synthesis Strategy — `D`

Learning derives state according to selected synthesis behavior and binds Strategy/configuration. Without Strategy, algorithm semantics would collapse into Learning.

### Learning -> Learned State — `D`

Learning exists to derive reusable source-informed state. Learned State is the accepted durable result that fulfills that purpose after Learning completes. Omitting Learned State would make successful Learning purposeless or elevate checkpoints/model files into accidental result authority.

### Learned State -> Learning — `D`

Learned State is explicitly the durable logical result of successful Learning. Current scope does not permit an externally imported object with no Learning history to masquerade as Learned State.

### Learned State -> Data Meaning — `D` at pairwise level

A valid Learned State inherits exact source/Data Meaning context from its producing Learning. Since Learned State requires Learning and Learning requires Data Meaning, an application containing Learned State cannot coherently omit Data Meaning. 009-B decides whether this is a direct edge or transitive closure.

### Learned State -> Synthesis Strategy — `D` at pairwise level

Learned State preserves Strategy/configuration identity and Strategy-dependent reuse requirements. 009-B decides direct versus transitive representation through Learning.

### Generation -> Data Meaning — `D`

Generation's purpose requires explicit semantic expectations rather than hidden type/model assumptions. A Generation capability with no Data Meaning concept contradicts the current semantic boundary.

### Generation -> Synthesis Strategy — `D`

Generation must use some synthesis behavior and bind its Strategy/configuration. Without Strategy, reusable synthesis behavior would collapse into Generation.

### Evaluation -> Evaluation Criterion — `D`

Evaluation exists to examine explicit Criteria. Without Criterion, method availability would define the question and collapse the question/examination distinction.

### Evaluation -> Evidence — `D`

Evaluation exists to produce inspectable Evidence. A completed Evaluation with no durable finding concept would reduce the examination to ephemeral method/runtime output.

### Evidence -> Evaluation Criterion — `D` at pairwise level

Evidence must preserve the exact Criterion answered. Without Criterion, the finding loses the question/standard needed for interpretation. 009-B decides direct versus transitive graph representation.

### Evidence -> Evaluation — `D`

Evidence is what an Evaluation validly established and records its producing Evaluation. Current scope does not define independently authored Evidence disconnected from Evaluation.

## Mutual-dependence candidates requiring 009-B cycle analysis

Two pairs are mutually dependent at the pairwise level:

```text
Learning      <-> Learned State
Evaluation    <-> Evidence
```

This does **not** automatically justify merging either pair. Phase 008 already established distinct purposes and state machines:

```text
Learning      = derivation activity
Learned State = reusable durable result

Evaluation    = committed examination
Evidence      = durable interpretable finding
```

009-B must determine whether each becomes a legitimate strongly connected dependence cluster, a different direct/transitive representation, or evidence of an upstream J2 boundary defect.

## Conditional/disjunctive relations

`C` relations are not universal graph edges.

### Strategy conditions

Synthesis Strategy may conditionally require:

- Data Meaning for Strategies whose behavior depends on explicit semantic roles;
- Learning for Strategies that require reusable learned state;
- Generation when the Strategy is exercised to synthesize output;
- Constraint where Strategy capability/support semantics concern reusable rules.

Other valid Strategy configurations make these non-universal.

### Learning conditions

Learning conditionally requires:

- Constraint when applicable rules govern derivation;
- Execution when operational significance requires a durable operational lifecycle.

Valid Learning can exist with no applicable reusable Constraint and, for trivial/local realization, without durable Execution.

### Learned State conditions

Learned State conditionally references Constraint when its producing Learning bound applicable rules. Constraint is not universal to all Learned State.

### Generation conditions

Generation conditionally requires:

- Learning/Learned State for learned-state-assisted Strategies;
- Constraint when reusable rules apply;
- Criterion/Evaluation/Evidence when completion requires evaluation-backed validation;
- Execution for operationally significant realization.

Direct Generation, unconstrained Generation, no-evaluation completion, and trivial/local realization provide accepted counterexamples to universal dependence.

### Constraint conditions

Constraint may conditionally require Data Meaning where a rule references semantic roles. Constraint may be used with Generation, but reusable rule definition can remain coherent without Generation being included.

### Criterion conditions

A Criterion may conditionally require Data Meaning, Learned State, Generation, or Constraint depending on the question/subject/reference context. Criterion does not universally require Evaluation or Evidence because reusable questions can exist before examination.

### Evaluation conditions

Evaluation universally requires Criterion/Evidence, but may conditionally require Data Meaning, Learned State, Generation, Constraint, or Execution depending on its subject and operational scale.

### Evidence conditions

Evidence universally requires Criterion/Evaluation, but may conditionally require Data Meaning, Learned State, Generation, Constraint, or Provenance depending on the finding's subject and traceability context.

### Execution is disjunctive

Execution is not a generic scheduler concept. It realizes one committed domain activity from:

```text
{ Learning, Generation, Evaluation }
```

Therefore each pairwise relation is `C`, not `D`:

```text
Execution -> Learning
Execution -> Generation
Execution -> Evaluation
```

The stronger rule is a one-of inclusion requirement. 009-B/009-C must preserve that disjunction instead of inventing three unconditional edges or a generic Work concept.

### Provenance is disjunctive

Provenance requires meaningful canonical/external subjects and a typed relationship worth recording, but no one accepted concept is universally required. It may explain different concepts in different application variants.

Therefore every pairwise `Provenance -> Cx` cell is `C`, not `D`.

009-B/009-C must preserve the non-binary rule rather than flattening it into ten graph edges.

## Counterexample witnesses

The following accepted witnesses reject several tempting universal edges:

### Direct-generation witness

```text
Data Meaning
Synthesis Strategy
Generation
```

can be coherent without Learning/Learned State when a direct Strategy is selected.

### No-Constraint witness

Generation and Learning may have no applicable reusable Constraint.

### No-evaluation-gate witness

Generation may complete without mandatory Criterion/Evaluation/Evidence handoff.

### Non-Generation Evaluation witness

Evaluation may examine Learned State or another supported subject/reference context, rejecting universal `Evaluation -> Generation`.

### Criterion-before-Evaluation witness

A reusable Criterion may be authored/reviewed before any Evaluation exists.

### Local/trivial realization witness

A semantically valid activity may be fulfilled without durable Execution when operational significance does not warrant it.

### Provenance-subject variation witness

Provenance may explain different concept combinations in different variants, rejecting a universal pairwise dependency on any one concept.

## Interpretation of `N`

`N` means only that no universal pairwise inclusion dependence exists.

Several reusable authority concepts can remain meaningfully included independently of a specific consumer:

```text
Data Meaning
Synthesis Strategy
Constraint
Evaluation Criterion
```

Likewise:

- Learning does not universally require Generation;
- Learned State does not universally require Generation;
- Evaluation/Evidence do not universally require Generation as their subject;
- domain activities do not universally require Provenance to preserve their own purpose;
- Provenance does not become current-state authority for the concepts it describes.

## 009-B handoff

009-B must now derive the canonical inclusion-dependence graph from this inventory and decide:

1. which `D` relations are direct versus transitive;
2. treatment of `Learning <-> Learned State`;
3. treatment of `Evaluation <-> Evidence`;
4. whether Learned State's Data Meaning/Strategy dependence is direct or transitive through Learning;
5. whether Evidence's Criterion dependence is direct or transitive through Evaluation;
6. how conditional/disjunctive requirements are represented without becoming universal edges;
7. roots/leaves and dependence-derived explanation ordering;
8. whether any cycle pressure requires J2 reopening.

## Methodology disposition

```text
D1 JACKSON APPLICATION INCLUSION-DEPENDENCE GRAPH
   PARTIAL — PAIRWISE SEMANTICS / INVENTORY COMPLETE; GRAPH PENDING 009-B

D2 APPLICATION FAMILY
   OPEN

D3 EXPLANATION ORDERING
   OPEN

D4 ADD/REMOVE CONSEQUENCES
   PARTIAL — FULL-PRODUCT ABSENCE + 009-A COUNTEREXAMPLES; 009-C/D PENDING
```

No J1/J2 defect is found by 009-A.

No concept or synchronization is added, removed, merged, split, renamed, or revised by this subgroup.

## Implementation hold

009-A is design authority only.

```text
JACKSON CONCEPT DESIGN     NOT COMPLETE
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## Current next boundary

**009-B — Inclusion-Dependence Graph, Roots, Cycles & Explanation Ordering** is next eligible.
