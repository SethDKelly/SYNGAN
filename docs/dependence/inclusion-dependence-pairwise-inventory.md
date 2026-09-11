---
type: Concept Dependence Authority
title: Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory
status: active
---

# Inclusion-Dependence Semantics, Evidence Rules & Pairwise Relation Inventory

## Purpose

Provide the current Phase 009-A authority for identifying **Jackson application inclusion dependence** among SYNGAN's eleven accepted concepts without confusing it with ordinary reference, validation, production, operational, provenance, import, storage, or runtime dependency.

This authority is a precursor to the canonical graph. It determines which directed concept pairs have sufficient evidence for universal inclusion dependence and which relations are non-dependent or only conditional/disjunctive.

It does **not** yet decide:

- direct versus transitive graph edges;
- cycle acceptance/rejection;
- graph roots/leaves;
- dependence-derived explanation ordering;
- valid application-family subsets;
- synchronization closure.

Those remain 009-B onward.

## Governing authority

- [Concept Design Methodology](../authority/design-methodology.md)
- [Jackson Methodology Completion Matrix](../authority/jackson-methodology-completion-matrix.md)
- [Phase 008 Individual-Concept Design Consolidation](../concepts/phase-008-individual-concept-consolidation.md)
- [Concept-Justification Traceability](../problem/concept-justification-traceability.md)
- the eleven accepted concept specifications
- [Phase 009 Entry / Decomposition](../phases/009/009-entry-decomposition.md)

Historical dependency/composition documents are evidence only and do not pre-decide this inventory.

---

# 1. Inclusion-dependence semantics

## 1.1 Governing question

For concepts `C1` and `C2` in an application variant `A`:

> **If `C1` is included, does including `C1` make sense only if `C2` is also included?**

The question concerns **application functionality** and purpose, not object references or implementation structure.

## 1.2 Direction

`C1 -> C2` means:

> an application that includes `C1` cannot remain conceptually coherent with `C2` absent.

The arrow therefore points from the dependent concept to the concept required for its purpose to make sense.

## 1.3 Inclusion versus occurrence

A concept can be included in an application even when no occurrence of it exists in one particular workflow.

Therefore:

- direct Generation without Learning is evidence that Generation does not universally depend on Learning;
- the fact that one Generation uses Learned State does not create universal `Generation -> Learned State` dependence;
- the fact that one Evaluation concerns a Constraint does not create universal `Evaluation -> Constraint` dependence;
- the fact that one activity happens to use durable Execution does not prove every application including that activity must include Execution.

Phase 009 reasons about **which concept capabilities the application includes**, not whether every concept has an instance in every workflow.

## 1.4 Full-product justification is not inclusion dependence

Phase 008-B established why the complete current SYNGAN design benefits from all eleven concepts.

That does not mean every reduced application variant must contain all eleven.

A concept may be fully justified in the complete product and still be omittable from a coherent contraction.

---

# 2. Classification vocabulary

009-A uses four classifications.

### `D` — DEPENDS

Current evidence supports universal pairwise inclusion dependence.

No coherent current application witness has been found in which the row concept remains meaningfully included while the column concept is absent.

### `N` — DOES NOT DEPEND

Current evidence supplies at least one coherent witness or purpose argument showing that the row concept can remain meaningfully included while the column concept is absent.

`N` does not mean the concepts never interact.

### `C` — CONDITIONAL / DISJUNCTIVE

There is no universal pairwise edge, but the column concept becomes required under a specific supported capability/configuration, or the row concept has a one-of/disjunctive requirement in which the column is one valid member.

`C` MUST NOT be turned into an unconditional graph edge in 009-B.

### `I` — INSUFFICIENT

Current evidence is insufficient to classify the pair safely.

009-A exits with **no unresolved `I` classifications**. Graph directness and cycle treatment remain open, but the pairwise inclusion question itself is sufficiently classified.

---

# 3. Evidence rules

A universal `D` classification requires all of the following:

1. the row concept's current purpose cannot be fulfilled coherently without the column concept being included;
2. the requirement follows from current concept semantics rather than architecture convenience;
3. no accepted current counterexample variant preserves the row concept while omitting the column;
4. the relation is not merely a stable reference, validation, production, runtime, provenance, or synchronization relation;
5. the requirement survives the Phase 008 no-occurrence cases and catalog boundaries.

A single counterexample application variant is sufficient to reject a universal `D` claim, provided the counterexample preserves the row concept's purpose rather than silently weakening or redefining it.

## 3.1 Evidence that is not enough

The following do not establish `D` by themselves:

- one concept stores another concept's ID;
- one concept queries or validates another;
- one concept is usually created before another;
- a synchronization exists between the pair;
- one concept produces another in one workflow;
- a database foreign key, package import, service call, or API parameter connects them;
- the complete product normally deploys both;
- implementation would be simpler if both were always present.

## 3.2 Conditional requirement discipline

A conditional capability must remain visible as `C` when removing the target concept would remove only a particular supported variant rather than invalidate the row concept as a whole.

For example:

```text
Generation -> Learned State   C
```

because learned-state-assisted Generation requires Learned State, while direct-generation Strategies are explicitly valid.

---

# 4. Pairwise inventory

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

The matrix is intentionally asymmetric.

---

# 5. Universal dependence candidates

009-A finds twelve directed universal inclusion-dependence candidates.

## 5.1 Learning -> Data Meaning

**Verdict: `D`.**

Learning's purpose is to derive reusable source-informed state according to accepted source meaning and explicitly binds a Data Meaning revision at semantic commitment.

Removing Data Meaning would force Learning either to rely on hidden source interpretation or to weaken its current purpose.

No valid current Learning variant has been identified that can preserve Learning's accepted semantics while omitting Data Meaning entirely.

## 5.2 Learning -> Synthesis Strategy

**Verdict: `D`.**

Learning derives state according to selected synthesis behavior and binds an exact Strategy/configuration revision.

Without Synthesis Strategy, algorithm behavior and requirements would become implicit inside Learning, contradicting the accepted Strategy/Learning boundary.

## 5.3 Learning -> Learned State

**Verdict: `D`.**

Learning exists to derive **reusable source-informed state**. Learned State is the accepted durable result concept that fulfills that purpose after Learning completes.

An application that included Learning but had no Learned State concept would either make successful Learning purposeless or elevate checkpoints/model files into accidental result authority.

The fact that failed/cancelled Learning establishes no Learned State does not defeat application inclusion dependence; occurrence cardinality and concept inclusion are different questions.

## 5.4 Learned State -> Learning

**Verdict: `D`.**

Learned State is explicitly the durable logical result of successful Learning and preserves producing-Learning identity.

Current scope does not permit externally imported reusable state to masquerade as Learned State with no Learning history.

Therefore Learned State inclusion currently requires Learning inclusion.

## 5.5 Learned State -> Data Meaning

**Verdict: `D` at pairwise inclusion level; directness deferred to 009-B.**

A valid Learned State inherits historically bound source/Data Meaning context from its producing Learning and must remain interpretable against that context.

Because current Learned State cannot exist without Learning, and current Learning cannot preserve its purpose without Data Meaning, an application containing Learned State cannot coherently omit Data Meaning.

009-B must determine whether this is represented as a direct edge or only as transitive closure through Learning.

## 5.6 Learned State -> Synthesis Strategy

**Verdict: `D` at pairwise inclusion level; directness deferred to 009-B.**

Learned State preserves the Strategy/configuration identity under which it was derived and exposes Strategy-dependent reuse requirements/limitations.

An application with Learned State but no Strategy authority would make the reusable state semantically uninterpretable as synthesis knowledge.

009-B will determine direct versus transitive representation through Learning.

## 5.7 Generation -> Data Meaning

**Verdict: `D`.**

Generation's accepted purpose is to fulfill a synthetic-data request under explicit semantic expectations. Its committed scope is represented through Data Meaning rather than hidden model/type assumptions.

A Generation capability with no Data Meaning concept would contradict the current explicit-semantics product boundary.

## 5.8 Generation -> Synthesis Strategy

**Verdict: `D`.**

Generation must use some synthesis behavior and binds a Strategy/configuration revision.

Without Strategy, the synthesis algorithm/capability contract would become implicit inside Generation and collapse the accepted boundary between requested outcome and reusable synthesis behavior.

## 5.9 Evaluation -> Evaluation Criterion

**Verdict: `D`.**

Evaluation exists to examine explicit Criteria. Without a Criterion concept, method availability would once again define the question being answered, directly violating Evaluation's accepted purpose and the question/examination boundary.

## 5.10 Evaluation -> Evidence

**Verdict: `D`.**

Evaluation exists to produce inspectable Evidence. A completed Evaluation with no durable finding concept would reduce the examination to ephemeral metric/runtime output and fail its current purpose.

Failure/cancellation producing no Evidence does not remove the application-level dependence.

## 5.11 Evidence -> Evaluation Criterion

**Verdict: `D` at pairwise inclusion level.**

Evidence must preserve the exact Criterion revision answered. Without Criterion, the finding loses the question/standard needed to interpret what was established.

009-B will determine whether this edge is direct in the canonical graph or partly represented through Evaluation.

## 5.12 Evidence -> Evaluation

**Verdict: `D`.**

Evidence is the durable finding authority for what an Evaluation validly established and records its producing Evaluation.

Current scope does not define Evidence as an independently authored claim disconnected from Evaluation.

---

# 6. Mutual-dependence findings requiring 009-B cycle analysis

Two pairings are mutually dependent under current pairwise semantics.

## 6.1 Learning <-> Learned State

```text
Learning      -> Learned State   D
Learned State -> Learning        D
```

This does **not** automatically imply that the concepts should be merged.

Phase 008 independently established their separate purposes, state, behavior, lifecycle, and reuse boundaries:

```text
Learning      = derivation activity
Learned State = reusable durable result
```

009-B must determine whether the canonical inclusion model represents them as:

- a legitimate strongly connected concept cluster;
- a direct mutual-dependence pair;
- a cluster with one direct edge plus an application-family invariant;
- or evidence of an upstream boundary issue requiring J2 reopening.

009-A does not pre-decide that graph representation.

## 6.2 Evaluation <-> Evidence

```text
Evaluation -> Evidence    D
Evidence   -> Evaluation  D
```

Again, Phase 008 already established independent purposes:

```text
Evaluation = committed examination
Evidence   = durable interpretable finding
```

009-B owns direct-cycle treatment. 009-A records only that neither concept's current purpose can be preserved in an application that permanently omits the other.

Evaluation Criterion is additionally required by both.

---

# 7. Conditional and disjunctive relation register

`C` relations are material to the application family but are **not** universal pairwise dependencies.

## 7.1 Synthesis Strategy conditional relations

### Strategy -> Data Meaning — conditional

Some Strategy revisions require explicit semantic roles/properties while other Strategies may operate with minimal meaning requirements.

Strategy authority can therefore exist without Data Meaning as a universal prerequisite, but particular Strategy capabilities may be unusable when Data Meaning is absent.

### Strategy -> Learning — conditional

Strategies may require Learning, support it optionally, or support direct Generation with no reusable Learned State.

The Strategy concept therefore does not universally depend on Learning.

### Strategy -> Generation — conditional

Strategy exists as reusable synthesis-behavior authority and can be defined/inspected independently, while actual synthesis use normally occurs through Generation.

A Strategy-authoring/capability application can remain coherent without Generation; an application intending to exercise synthesis output cannot.

### Strategy -> Constraint — conditional

A Strategy may declare Constraint support/limitations even when an application has no reusable Constraint authority in scope.

Constraint is therefore capability-conditional rather than universally required by Strategy.

## 7.2 Learning conditional relations

### Learning -> Constraint — conditional

Learning binds applicable Constraints where such rules govern derivation, but valid Learning may have no applicable reusable Constraint.

### Learning -> Execution — conditional

Operationally significant Learning may require durable Execution. A trivial/local Learning realization need not fabricate an Execution merely to satisfy catalog symmetry.

Therefore no universal `Learning -> Execution` edge exists.

## 7.3 Learned State -> Constraint — conditional

Learned State preserves Constraint context where its producing Learning bound applicable rules. A valid Learned State can also originate from Learning with no applicable reusable Constraint.

## 7.4 Generation conditional relations

### Generation -> Learning / Learned State — conditional

Learned-state-assisted Generation may require both, while direct-generation Strategies explicitly provide a valid counterexample.

Therefore neither relation is universal.

### Generation -> Constraint — conditional

A Generation may bind zero or more applicable reusable Constraints. Unconstrained Generation remains a valid current variant.

### Generation -> Criterion / Evaluation / Evidence — conditional

A Generation whose completion contract requires post-production validation may require the evaluation chain before semantic completion.

Generation that has no mandatory evaluation-based completion condition remains valid, so these are not universal edges.

### Generation -> Execution — conditional

Large/distributed/operationally significant Generation may require durable Execution. Trivial/local Generation need not.

## 7.5 Constraint conditional relations

### Constraint -> Data Meaning — conditional

Many rules require semantic subjects/roles supplied by Data Meaning, but a Constraint may be coherent for an explicitly identified logical scope/property without requiring broader semantic interpretation.

### Constraint -> Generation — conditional

Constraint's primary product use is to govern synthetic output, but reusable rule authoring can exist independently and Constraints can also be referenced by Learning/Evaluation contexts.

Constraint therefore does not universally depend on Generation.

## 7.6 Evaluation Criterion conditional relations

Criterion may conditionally require the authority needed to state its particular question:

- Data Meaning when the question depends on semantic interpretation;
- Learned State when reusable learned state is the subject;
- Generation when a Generation output/Condition is the subject;
- Constraint when the question asks whether an exact rule is satisfied.

No one of those concepts is universal to every Criterion.

Criterion does **not** depend universally on Evaluation or Evidence; an application may support defining/reviewing reusable questions before any examination has occurred.

## 7.7 Evaluation conditional relations

Evaluation universally requires Criterion and Evidence, but its **subject/context** may conditionally require:

- Data Meaning;
- Learned State;
- Generation;
- Constraint.

Evaluation may also require Execution when the examination is operationally significant.

None of these subject/operational concepts is universal to all Evaluations.

## 7.8 Evidence conditional relations

Evidence universally requires Criterion and Evaluation.

Its interpretive subject/context may additionally require Data Meaning, Learned State, Generation, or Constraint depending on what was evaluated.

Evidence may link to Provenance for historical explanation/traceability, but its finding purpose can remain intelligible from its own stable Criterion/Evaluation/input references in a reduced application. Provenance is therefore conditional rather than universal.

## 7.9 Execution has a disjunctive domain-activity prerequisite

Execution cannot coherently exist as a generic scheduler/workflow concept.

Under the current model it realizes one committed domain activity from:

```text
{ Learning, Generation, Evaluation }
```

Therefore:

```text
Execution -> Learning    C
Execution -> Generation  C
Execution -> Evaluation  C
```

No individual member is universal because Execution may realize either of the other supported activities.

009-B/009-C must preserve this **one-of application-family condition** rather than inventing three unconditional edges or a new generic Work concept.

## 7.10 Provenance has a disjunctive subject prerequisite

Provenance records typed relationships among material canonical states/results and external identities.

A Provenance-only application with no provenance-bearing SYNGAN concept would have no product purpose. However, no one accepted concept is universally required: Provenance can explain Data Meaning/Strategy bindings, Learning/Learned State derivation, Generation output, Evaluation/Evidence, Execution realization, and other supported histories.

Therefore every pairwise `Provenance -> Cx` relation is classified `C`, not `D`.

009-B/009-C must represent the stronger non-binary rule:

> Provenance inclusion requires at least one meaningful provenance-bearing SYNGAN subject/context and at least one relationship worth recording; it does not require any one specific accepted concept universally.

---

# 8. Counterexample witness set

The following witness variants reject several tempting but incorrect universal-dependence claims.

## W1 — direct-generation variant

Contains at least:

```text
Data Meaning
Synthesis Strategy
Generation
```

May omit:

```text
Learning
Learned State
Constraint
Evaluation Criterion
Evaluation
Evidence
Execution
Provenance
```

subject to the selected direct Strategy and deliberately reduced product outcomes.

This witnesses:

- `Generation !-> Learning` universally;
- `Generation !-> Learned State` universally;
- no fabricated train-then-generate pipeline.

Application-family validity of the complete subset is formally tested in 009-C; 009-A uses it only as accepted counterexample evidence from Phase 008.

## W2 — generation without reusable Constraint

A direct or learned Generation may have no applicable reusable prescriptive rule.

This witnesses `Generation !-> Constraint` universally.

## W3 — generation without evaluation-gated completion

A Generation may complete from its committed semantic/request conditions without requiring a Criterion/Evaluation/Evidence handoff.

This witnesses that those relations are conditional rather than universal.

## W4 — evaluation of Learned State/reference rather than Generation output

Evaluation can legitimately examine a Learned State or other supported subject/reference context.

This rejects universal `Evaluation -> Generation` dependence.

## W5 — reusable Criterion definition before examination

An application may define/review reusable Criteria before any Evaluation occurs.

This rejects `Evaluation Criterion -> Evaluation` as universal.

## W6 — local/trivial operational realization

A semantically valid activity may be fulfilled without a durable long-running Execution identity when operational significance does not warrant one.

This rejects universal activity -> Execution dependence.

## W7 — Provenance with different subjects

A provenance capability may explain Learning/Learned State in one application and Generation/Evidence in another.

This rejects every proposed universal pairwise `Provenance -> specific concept` edge while preserving the disjunctive subject prerequisite.

---

# 9. Negative-dependence interpretation

Most `N` cells are intentional, not omissions.

The current catalog contains several reusable authority concepts that are independently definable:

```text
Data Meaning
Synthesis Strategy
Constraint
Evaluation Criterion
```

Their usefulness may increase when consumer activities are included, but consumer presence is not universally required merely to define, inspect, revise, compare, or reuse the authority.

Likewise:

- Learning does not require Generation to be present;
- Learned State does not require Generation to be present;
- Evaluation/Evidence do not require Generation specifically because other subjects are valid;
- domain activities do not require Provenance merely to preserve their own purpose;
- Provenance does not become canonical state authority for the concepts it describes.

---

# 10. Pairwise result counts

Across the 110 directed non-self pairs:

```text
DEPENDS (D)                12
CONDITIONAL/DISJUNCTIVE    38
DOES NOT DEPEND (N)        60
INSUFFICIENT (I)            0
```

These counts are diagnostic only; they are not a design-quality target.

The important result is that universal inclusion dependence is substantially **sparser** than the historical reference/validation/production/runtime relationship graph.

---

# 11. 009-B graph handoff

009-B must now convert this pairwise inventory into the canonical inclusion-dependence model.

It must explicitly determine:

1. which `D` relations are direct versus transitive;
2. whether `Learning <-> Learned State` is a legitimate strongly connected cluster or exposes a boundary problem;
3. whether `Evaluation <-> Evidence` is a legitimate strongly connected cluster or exposes a boundary problem;
4. whether `Learned State -> Data Meaning/Strategy` and `Evidence -> Criterion` should appear as direct edges or only through transitive closure;
5. how conditional/disjunctive relations are represented without being promoted to universal edges;
6. graph roots/leaves;
7. dependence-derived explanation ordering;
8. whether any cycle or graph pressure triggers J2 reopening.

009-B MUST NOT derive directness from file references, synchronization arrows, or implementation architecture.

---

# 12. Methodology disposition

009-A advances D1 but does not close it:

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

No current J1/J2 defect is found by the pairwise audit.

No concept is added, removed, merged, split, or renamed.

No synchronization is added, removed, or revised by 009-A.

---

# 13. Implementation hold

009-A is concept-design authority only.

It introduces no production source, tests, dependencies, lockfiles, CI/workflows, package topology, persistence/data-plane schemas, runtime/model/platform/security adapters, public APIs, algorithms, privacy mechanisms, or architecture decisions.

```text
JACKSON CONCEPT DESIGN     NOT COMPLETE
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## Current next boundary

**009-B — Inclusion-Dependence Graph, Roots, Cycles & Explanation Ordering** is next eligible.
