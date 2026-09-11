---
type: Concept Dependence Authority
title: Application Family, Valid Concept Subsets & Minimal Coherent Variants
status: active
---

# Application Family, Valid Concept Subsets & Minimal Coherent Variants

## Purpose

Define the current SYNGAN **application family** from the canonical Phase 009-B inclusion-dependence graph plus the non-binary and conditional rules that cannot be represented safely as ordinary universal graph edges.

This authority answers:

> **Which subsets of the eleven accepted concepts are coherent applications or capability variants under current concept purposes, and what additional concepts are required when a variant advertises a particular capability?**

It closes the current Jackson methodology obligation to derive meaningful valid concept subsets without assuming that every SYNGAN application must include all eleven concepts.

It does not yet perform the systematic contraction/extension consequence audit owned by 009-D, replay the synchronization inventory owned by 009-E, or decide product packaging/editions.

## Governing authority

- [Concept Design Methodology](../authority/design-methodology.md)
- [Phase 008 Individual-Concept Design Consolidation](../concepts/phase-008-individual-concept-consolidation.md)
- [009-A Pairwise Inclusion-Dependence Inventory](inclusion-dependence-pairwise-inventory.md)
- [009-B Canonical Graph & Explanation Ordering](inclusion-dependence-graph-ordering.md)
- [Phase 009 Entry / Decomposition](../phases/009/009-entry-decomposition.md)

## Vocabulary

009-C distinguishes three questions that must not be collapsed.

### Coherent concept subset

A non-empty set of accepted concepts whose members can preserve their current purposes together while satisfying universal inclusion dependence and all applicable non-binary prerequisites.

A coherent subset is a valid member of the design application family.

### Capability-coherent variant

A coherent subset that additionally contains every concept required by the capabilities the variant explicitly claims to provide.

A subset may be coherent in general yet invalid for a stronger advertised capability.

Example:

```text
{ Data Meaning, Synthesis Strategy, Generation }
```

is coherent for direct Generation but is **not** sufficient for a variant claiming learned-state-assisted Generation.

### Product/package completeness

Whether a coherent subset is a commercially useful edition, deployable SKU, default installation, or supported packaging profile is not decided here.

Concept-design validity does not imply product packaging policy.

---

# 1. Canonical family validity rules

Let `S` be a non-empty subset of the eleven accepted concepts.

`S` is currently coherent only if all applicable rules below hold.

## F1 — Learning / Learned State co-inclusion

Because the two concepts form a legitimate strongly connected inclusion component:

```text
Learning in S      iff Learned State in S
```

If either is present, universal closure also requires:

```text
Data Meaning in S
Synthesis Strategy in S
```

Therefore the minimal closure of either Learning or Learned State is:

```text
L-KERNEL = {
  Data Meaning,
  Synthesis Strategy,
  Learning,
  Learned State
}
```

## F2 — Generation universal closure

If Generation is present:

```text
Generation in S
  => Data Meaning in S
  => Synthesis Strategy in S
```

Therefore the minimal direct-generation closure is:

```text
G-KERNEL = {
  Data Meaning,
  Synthesis Strategy,
  Generation
}
```

This does not require Learning/Learned State because direct-generation Strategies remain valid.

## F3 — Evaluation / Evidence co-inclusion

Because Evaluation and Evidence form a legitimate strongly connected inclusion component:

```text
Evaluation in S iff Evidence in S
```

If either is present:

```text
Evaluation Criterion in S
```

Therefore the minimal evaluation-capability closure is:

```text
E-KERNEL = {
  Evaluation Criterion,
  Evaluation,
  Evidence
}
```

The evaluated subject may be external or may be supplied by another included concept such as Generation or Learned State. Generation is not universally required.

## F4 — Execution one-of prerequisite

Execution is not a standalone scheduler/workflow concept.

If Execution is present, the application must include at least one committed domain activity it can realize:

```text
Execution in S
  => Learning in S
     OR Generation in S
     OR Evaluation in S
```

Universal closure of the selected activity still applies.

Thus examples of minimal Execution-bearing closures are:

```text
GX-KERNEL = { Data Meaning, Synthesis Strategy, Generation, Execution }

LX-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State, Execution }

EX-KERNEL = { Evaluation Criterion, Evaluation, Evidence, Execution }
```

Execution alone, or Execution with only reusable authorities, is invalid.

## F5 — Provenance semantic-witness prerequisite

Provenance is not a standalone lineage/metadata database.

If Provenance is present, the variant must support at least one **meaningful provenance-bearing relationship** involving current SYNGAN concept state/result/history and, where relevant, external identities.

Examples of valid witness forms include:

- an activity bound to exact authority revisions;
- Learned State produced by Learning;
- completed synthetic output produced by Generation;
- Evidence produced by Evaluation;
- a domain activity operationally realized by Execution;
- an activity or result using a material external dependency;
- an evaluated subject/reference relationship;
- a material supersession/restriction/invalidation historical relationship.

Membership alone cannot fully prove this rule because the relationship semantics matter.

Therefore:

```text
{ Provenance }
```

is invalid, while Provenance added to a variant with an actual provenance-bearing relation can be coherent.

009-C intentionally does not invent a generic `Provenance -> AnyConcept` graph edge.

## F6 — Constraint is optional unless claimed

Constraint has no universal pairwise prerequisite and no activity universally requires Constraint.

Therefore:

```text
{ Constraint }
```

is a coherent authority-only subset, and Learning/Generation may be coherent without Constraint.

A variant that advertises reusable prescriptive-rule definition/binding must include Constraint.

## F7 — Reusable authority concepts may stand alone

Current purposes permit authority-definition/inspection applications containing any one of:

```text
{ Data Meaning }
{ Synthesis Strategy }
{ Constraint }
{ Evaluation Criterion }
```

These are coherent **authority-only** family members even though they do not generate synthetic data by themselves.

The empty set is excluded from the application family because it provides no SYNGAN concept functionality.

---

# 2. Capability-conditional family rules

Universal closure defines the structural floor. Capability claims may impose additional inclusion requirements.

## C1 — Learned-state-assisted Generation

A variant that claims Generation from reusable Learned State requires:

```text
Generation
+ L-KERNEL
```

which yields the minimal learned-generation capability:

```text
LG-VARIANT = {
  Data Meaning,
  Synthesis Strategy,
  Learning,
  Learned State,
  Generation
}
```

A plain G-KERNEL remains coherent but supports only direct-generation capability unless its Strategy contract says otherwise.

## C2 — Evaluation-gated Generation

A variant whose Generation completion contract requires evaluation-backed Evidence must include:

```text
G-KERNEL
+ E-KERNEL
```

Minimal closure:

```text
GE-VARIANT = {
  Data Meaning,
  Synthesis Strategy,
  Generation,
  Evaluation Criterion,
  Evaluation,
  Evidence
}
```

This rule does not mean all Generation universally depends on Evaluation.

## C3 — Reusable prescriptive-rule support

A variant that claims actors can define/bind reusable prescriptive rules includes:

```text
Constraint
```

Adding Constraint does not automatically require Generation, Learning, or Evaluation; those consumers remain optional.

## C4 — Durable operational lifecycle

A variant that claims durable retry/recovery/cancellation/indeterminate operational history for an activity includes Execution and must satisfy F4.

Examples:

```text
G-KERNEL + Execution
L-KERNEL + Execution
E-KERNEL + Execution
```

## C5 — Provenance inspection/history

A variant that claims typed provenance/history includes Provenance and must satisfy F5 with at least one meaningful relationship witness.

Canonical unambiguous examples include:

```text
G-KERNEL + Provenance
L-KERNEL + Provenance
E-KERNEL + Provenance
```

These examples are not the only possible provenance-bearing family members.

## C6 — Topology breadth does not add a concept

Single-table, time-series, multi-table shared-key, and legitimate composite structured topology vary Data Meaning/Strategy/Generation/Constraint/Evaluation semantics without creating a new current concept.

A topology-capable generation variant therefore starts from G-KERNEL and adds only those optional concepts actually required by its Strategy/capability claims.

## C7 — Text-bearing structured data does not add a concept

Free-form/source-language text fields inside structured data are represented through the existing concepts.

A direct local/self-contained text-capable Strategy can use G-KERNEL.

A source-derived reusable text-capable Strategy may require LG-VARIANT.

Evaluation, Constraint, Execution, and Provenance remain conditional on the advertised text-related capability and workflow, not on the mere presence of text.

No standalone Text, Tokenizer, Vocabulary, or Language Model concept is restored.

---

# 3. Canonical minimal coherent variants

009-C uses **minimal** to mean no concept can be removed from the named capability while preserving that capability's current semantics.

## 3.1 Authority-only minima

```text
A-DM   = { Data Meaning }
A-SS   = { Synthesis Strategy }
A-CON  = { Constraint }
A-CRI  = { Evaluation Criterion }
```

These support authoring/inspection/reuse of one independent authority concept.

## 3.2 Learning capability minimum

```text
L-KERNEL = {
  Data Meaning,
  Synthesis Strategy,
  Learning,
  Learned State
}
```

Removing any member either violates universal closure or removes the reusable-result purpose of Learning.

## 3.3 Direct Generation capability minimum

```text
G-KERNEL = {
  Data Meaning,
  Synthesis Strategy,
  Generation
}
```

This is the smallest current synthesis-output capability because Generation universally requires Data Meaning and Strategy but not Learning/Learned State.

## 3.4 Evaluation capability minimum

```text
E-KERNEL = {
  Evaluation Criterion,
  Evaluation,
  Evidence
}
```

The evaluated subject/reference may be external; Generation is not universal.

## 3.5 Execution-bearing minima

```text
GX-KERNEL = G-KERNEL + Execution
LX-KERNEL = L-KERNEL + Execution
EX-KERNEL = E-KERNEL + Execution
```

These are the smallest unambiguous Execution variants for each supported domain-activity family.

## 3.6 Provenance-bearing minima

No single concept-only provenance minimum is declared because F5 depends on the relationship being explained, not just the names present in `S`.

For later synchronization/application-family testing, three canonical unambiguous provenance-bearing kernels are:

```text
GP-VARIANT = G-KERNEL + Provenance
LP-VARIANT = L-KERNEL + Provenance
EP-VARIANT = E-KERNEL + Provenance
```

Smaller authority-history variants may be coherent when they contain a genuine typed historical relationship; 009-C does not claim otherwise.

---

# 4. Important combined variants

The application family is not limited to the minima. Coherent variants may combine closed kernels and optional capability extensions.

## 4.1 Learned-state-assisted Generation

```text
L-KERNEL + Generation
```

Supports derivation of reusable state followed by Generation using that state.

## 4.2 Generation plus Evaluation

```text
G-KERNEL + E-KERNEL
```

Supports evaluating synthetic output and is the minimum concept set for evaluation-gated Generation when the Evaluation targets that output.

## 4.3 Learned Generation plus Evaluation

```text
L-KERNEL + Generation + E-KERNEL
```

Supports Learning, Learned State reuse, Generation, and Evaluation/Evidence without requiring Constraint, Execution, or Provenance unless those capabilities are claimed.

## 4.4 Constraint-aware variants

Constraint may be added to any coherent kernel whose intended capability needs reusable prescriptive authority.

Examples:

```text
G-KERNEL + Constraint
L-KERNEL + Constraint
G-KERNEL + E-KERNEL + Constraint
```

Constraint presence does not transfer rule ownership to the activity or Evaluation.

## 4.5 Operational variants

Execution may be added to any coherent variant containing Learning, Generation, or Evaluation when durable operational realization is part of the capability contract.

The same Execution concept can coexist with more than one activity type in larger variants; F4 only requires at least one.

## 4.6 Provenance-bearing variants

Provenance may be added wherever the variant has an actual typed historical/derivation/binding/realization/evaluation/dependency relationship worth preserving.

It remains high-fan-in/low-authority-fan-out and does not become a prerequisite for the domain concepts' own purposes.

## 4.7 Full current concept family member

The complete eleven-concept set is coherent:

```text
{
  Data Meaning,
  Synthesis Strategy,
  Learning,
  Learned State,
  Generation,
  Constraint,
  Evaluation Criterion,
  Evaluation,
  Evidence,
  Execution,
  Provenance
}
```

Full-set coherence does not imply universal inclusion of all concepts in every application.

---

# 5. Invalid subset classes

009-C explicitly records representative invalid subsets so later design does not treat graph closure as optional.

## 5.1 Learning without Learned State

```text
{ Data Meaning, Synthesis Strategy, Learning }
```

**Invalid.** Learning's reusable-result purpose has no accepted result concept.

## 5.2 Learned State without Learning

```text
{ Data Meaning, Synthesis Strategy, Learned State }
```

**Invalid.** Current Learned State is defined as the durable result of successful Learning.

## 5.3 Generation missing semantic authority

```text
{ Synthesis Strategy, Generation }
```

**Invalid.** Generation universally requires Data Meaning.

Likewise `{ Data Meaning, Generation }` is invalid because Synthesis Strategy is missing.

## 5.4 Evaluation without Evidence

```text
{ Evaluation Criterion, Evaluation }
```

**Invalid.** Current Evaluation purpose includes producing durable Evidence.

## 5.5 Evidence without Evaluation

```text
{ Evaluation Criterion, Evidence }
```

**Invalid.** Current Evidence is what an Evaluation validly established.

## 5.6 Evaluation/Evidence missing Criterion

```text
{ Evaluation, Evidence }
```

**Invalid.** The question/standard being answered has no authority.

## 5.7 Standalone Execution

```text
{ Execution }
```

**Invalid.** Execution must realize at least one supported domain activity.

A set such as `{ Data Meaning, Synthesis Strategy, Execution }` is also invalid because it still contains no realizable activity.

## 5.8 Standalone Provenance

```text
{ Provenance }
```

**Invalid.** There is no SYNGAN history/relationship subject to explain.

## 5.9 Capability-claim mismatch

```text
G-KERNEL
```

is a valid direct-generation subset but **invalid as a learned-state-assisted Generation claim** because Learning/Learned State are absent.

Likewise G-KERNEL is coherent generally but **invalid as an evaluation-gated Generation claim** when E-KERNEL is absent.

This distinction is central: subset coherence does not authorize capabilities that require omitted concepts.

---

# 6. Closure and extension properties

## 6.1 Universal graph closure

For any proposed subset `S`, first add every concept required by the canonical universal graph until no new concept is required.

Examples:

```text
closure({ Generation })
  = { Data Meaning, Synthesis Strategy, Generation }

closure({ Learned State })
  = { Data Meaning, Synthesis Strategy, Learning, Learned State }

closure({ Evidence })
  = { Evaluation Criterion, Evaluation, Evidence }
```

The closure operation alone does not satisfy F4/F5 or capability-conditional claims.

## 6.2 Union is usually safe only after side-constraint replay

The union of two graph-closed subsets remains graph-closed.

However the resulting variant must still replay:

- Execution one-of semantics;
- Provenance witness semantics;
- explicit capability claims;
- concept-local invariants and later synchronization rules.

009-C therefore does not equate set union with automatic final product validity.

## 6.3 Removing a concept requires re-closure

Removing a prerequisite from a coherent subset may require removing all dependents that can no longer preserve their purposes or changing the variant's advertised capability.

Systematic contraction/extension consequences are deferred to 009-D, which will use the family rules established here.

---

# 7. Required scenario probes

## 7.1 Direct-generation variant

```text
{ Data Meaning, Synthesis Strategy, Generation }
```

**VALID.**

Confirms that Learning/Learned State are not universal Generation dependencies.

## 7.2 Learned-state-assisted variant

```text
{ Data Meaning, Synthesis Strategy, Learning, Learned State, Generation }
```

**VALID.**

Confirms that the L-CLUSTER composes with Generation without changing concept boundaries.

## 7.3 Constraint-light variant

G-KERNEL or L-KERNEL without Constraint is **VALID** when no reusable prescriptive rule capability is claimed.

## 7.4 Evaluation-focused variant

```text
{ Evaluation Criterion, Evaluation, Evidence }
```

**VALID** for evaluation of a supported external/reference subject or one supplied through integration. Generation is not universally required.

## 7.5 Execution-bearing variants

GX-KERNEL, LX-KERNEL, and EX-KERNEL are **VALID**.

`{ Execution }` and `{ Data Meaning, Synthesis Strategy, Execution }` are **INVALID**.

## 7.6 Provenance-bearing variants

G-KERNEL + Provenance, L-KERNEL + Provenance, and E-KERNEL + Provenance are **VALID when the stated provenance relation exists**.

`{ Provenance }` is **INVALID**.

## 7.7 Topology-bearing variant

G-KERNEL remains the conceptual minimum for a Strategy that directly supports current structured-topology targets.

Adding time-series or multi-table shared-key semantics does not force a Relationship/TimeSeries/Table concept.

## 7.8 Text-bearing structured-data variant

G-KERNEL remains valid for a direct self-contained text-capable Strategy.

L-KERNEL + Generation is valid for a source-derived reusable text-capable Strategy.

No Text/Tokenizer/Language Model concept is required by the application-family structure.

---

# 8. Application-family result

The current application family is **not one mandatory eleven-concept product**.

It is the set of non-empty concept subsets that:

1. are closed under the 009-B universal inclusion-dependence graph;
2. satisfy the Execution one-of prerequisite when Execution is present;
3. satisfy the Provenance semantic-witness prerequisite when Provenance is present;
4. include all concepts required by any capability the variant claims;
5. preserve the individual concept purposes/boundaries established in Phase 008.

This rule-based definition covers both minimal kernels and larger composed variants without enumerating every mathematically possible combination.

No current family member requires a new concept, concept merge/split, or change to the canonical graph.

---

# 9. Methodology disposition

009-C closes the current D2 obligation:

```text
D2  CURRENTLY CLOSED — meaningful valid concept subsets/application family established
```

D1 and D3 remain currently closed from 009-B.

D4 advances but remains open for 009-D:

```text
D4  PARTIAL TO STRONG — family closure/removal rules and representative consequences established;
                        systematic contraction/extension/add-remove audit pending 009-D
```

No E-row synchronization/composition obligation is closed by 009-C.

## Current counts

```text
accepted concepts             11
accepted synchronizations     15
universal direct graph edges   9
strong inclusion components    2
canonical minimal authority variants  4
canonical activity/result kernels     3
catalog changes                0
synchronization changes        0
```

Counts are descriptive, not completion criteria.

## Reopen discipline

If 009-D/E later finds a subset that passes the family rules yet cannot preserve a concept's accepted purpose, reopen the smallest affected D1-D2 or Phase 008 authority rather than patching the contradiction in architecture or implementation.

---

# 10. 009-D handoff

009-D must use this family to analyze contraction and extension explicitly:

- what capability disappears when each concept/component is removed;
- which dependents must also be removed or re-scoped;
- which additions are ordinary family extension versus triggers for fresh concept discovery;
- how strong-component removal behaves;
- how side constraints change under addition/removal;
- whether any family contraction produces misleading product claims;
- how the application family affects explanation/documentation scope.

009-D must not change implementation.

## Implementation hold

```text
JACKSON CONCEPT DESIGN     NOT COMPLETE
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```
