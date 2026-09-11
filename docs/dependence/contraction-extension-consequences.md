---
type: Concept Dependence Authority
title: Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences
status: active
---

# Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences

## Purpose

Establish the current Phase 009-D authority for how SYNGAN's application family changes when accepted concepts or strongly connected inclusion components are removed, added, or newly required by an advertised capability.

This authority answers:

> **What functionality, scope, explanation obligations, and family membership change when a current concept is removed or added, and when does an apparent extension stop being ordinary composition of the current catalog and require fresh concept discovery?**

It closes the current Jackson methodology obligation for product-scope consequences of adding/removing concepts.

It does not replay synchronization rules, map interfaces, change architecture, decide packaging/SKUs, or authorize implementation.

## Governing authority

- [Concept Design Methodology](../authority/design-methodology.md)
- [Phase 008 Individual-Concept Design Consolidation](../concepts/phase-008-individual-concept-consolidation.md)
- [Catalog Perimeter Candidate Rediscovery, Missing-Concept & Boundary Audit](../concepts/catalog-perimeter-candidate-rediscovery-boundary-audit.md)
- [009-A Pairwise Inclusion-Dependence Inventory](inclusion-dependence-pairwise-inventory.md)
- [009-B Canonical Graph & Explanation Ordering](inclusion-dependence-graph-ordering.md)
- [009-C Application Family, Valid Concept Subsets & Minimal Coherent Variants](application-family-valid-subsets.md)
- [Phase 009 Entry / Decomposition](../phases/009/009-entry-decomposition.md)

---

# 1. Contraction and extension vocabulary

## 1.1 Contraction

A **contraction** removes one or more accepted concepts or drops one or more advertised capabilities from a current application-family member.

A contraction is valid only after the remaining set is re-evaluated against:

1. universal inclusion-dependence closure;
2. strongly connected component co-inclusion;
3. Execution's one-of prerequisite;
4. Provenance's semantic-witness prerequisite;
5. capability-specific inclusion requirements;
6. current concept purposes/boundaries.

Removing a concept therefore does not mean merely deleting one name from a list.

## 1.2 Forced dependent contraction

When a prerequisite is removed, concepts whose purposes can no longer be preserved must also be removed or the capability must be re-scoped.

Example:

```text
remove Data Meaning
  => Learning/Learned State cannot remain
  => Generation cannot remain
```

This consequence follows from current universal dependence, not implementation coupling.

## 1.3 Capability-only contraction

A concept can be removed without forcing unrelated concepts out of the set while still removing a distinct capability.

Examples:

```text
remove Constraint  => no reusable prescriptive-rule capability
remove Execution   => no durable operational-realization capability
remove Provenance  => no typed provenance/history capability
```

The remaining family member can still be coherent if its claims are narrowed accordingly.

## 1.4 Extension

An **ordinary family extension** adds one or more already accepted concepts and then takes the required closure/side constraints.

An extension is not automatically a new product concept and does not imply implementation modularity.

## 1.5 Scope expansion requiring rediscovery

An apparent extension requires fresh Jackson-style concept discovery when the desired new functionality introduces a **new independently useful purpose with its own state/history/actions** that the accepted concepts cannot own without boundary erosion.

Existing catalog facts, implementation resources, IDs, status values, tables, services, or package boundaries are insufficient by themselves to trigger promotion.

---

# 2. General contraction rule

Given a coherent family member `S` and a proposed removal set `R`:

```text
S' = S - R
```

`S'` is valid only if all remaining advertised capabilities can still be expressed and the family rules hold.

If a remaining concept depends universally on a removed concept, either:

- remove that dependent concept too; or
- reject the contraction.

If Execution remains, at least one of Learning, Generation, or Evaluation must remain.

If Provenance remains, at least one meaningful typed historical/derivation/binding/realization/evaluation/dependency relationship must remain possible in the contracted variant.

Capability claims must be rewritten to match the contracted set. A contraction that preserves the set syntactically while retaining an impossible capability claim is invalid.

---

# 3. Systematic removal consequences

## 3.1 Remove Data Meaning

### Forced consequences

Current universal dependence requires:

```text
Learning      -> Data Meaning
Learned State -> Data Meaning   [transitively through Learning]
Generation    -> Data Meaning
```

Therefore removing Data Meaning from a variant forces removal or abandonment of:

```text
Learning
Learned State
Generation
```

### Capabilities lost

- explicit synthesis-relevant semantic interpretation;
- Learning under accepted source meaning;
- direct or learned Generation under explicit semantic scope;
- topology/text-bearing Generation capabilities that rely on current Data Meaning semantics.

### Capabilities that may remain

Subject to their own requirements:

- Synthesis Strategy authoring/inspection;
- Constraint authoring where the rule can be stated without Data Meaning-owned semantic roles;
- Evaluation Criterion authoring;
- Evaluation/Evidence where the supported question/subject does not require Data Meaning;
- Execution only if Evaluation remains as the realized activity;
- Provenance only if a meaningful remaining relationship witness exists.

### Product-scope meaning

Removing Data Meaning is not a "raw-mode Generation" option. Under current design it removes Generation capability because hidden physical-type/model interpretation is explicitly outside accepted Generation semantics.

---

## 3.2 Remove Synthesis Strategy

### Forced consequences

Current universal dependence requires:

```text
Learning      -> Synthesis Strategy
Learned State -> Synthesis Strategy   [transitively through Learning]
Generation    -> Synthesis Strategy
```

Therefore removing Strategy forces removal or abandonment of:

```text
Learning
Learned State
Generation
```

### Capabilities lost

- reusable synthesis-behavior authority;
- direct Generation;
- learned-state derivation/use;
- topology/text synthesis capability declaration;
- inspectable synthesis requirements/limitations/dependency profile.

### Capabilities that may remain

Data Meaning, Constraint, Evaluation Criterion, Evaluation/Evidence, appropriate Execution, and appropriate Provenance remain possible where their own rules are satisfied.

### Product-scope meaning

A variant cannot replace Strategy with an implicit implementation algorithm while still claiming current Learning/Generation semantics.

---

## 3.3 Remove Learning

Learning and Learned State form one inclusion SCC.

Therefore:

```text
remove Learning => remove Learned State
```

### Capabilities lost

- derivation of reusable source-informed synthesis state;
- learned-state-assisted Generation;
- reusable Learned State selection/reuse/history.

### Capabilities retained

Generation may remain through direct-generation Strategies so long as Data Meaning + Strategy remain.

Constraint, Evaluation/Evidence, Execution and Provenance remain according to their own conditions.

### Product-scope meaning

Removing Learning does **not** remove Generation universally. The contracted product becomes direct-generation-only unless another future capability is introduced through fresh design.

---

## 3.4 Remove Learned State

Because of the same SCC:

```text
remove Learned State => remove Learning
```

The capability consequences are the same as removing Learning.

A design that keeps Learning but replaces Learned State with a checkpoint/model file would violate the accepted activity/result boundary rather than form a valid contraction.

---

## 3.5 Remove Generation

No accepted concept universally depends on Generation.

Therefore Generation can be removed without universal forced removal of another concept.

### Capabilities lost

- actor-requested synthetic-data result production;
- Generation-owned Condition/request semantics;
- candidate-to-completed synthetic output lifecycle;
- evaluation-gated Generation as a composed capability.

### Capabilities retained

Potentially:

- Data Meaning authority;
- Strategy authority;
- Learning/Learned State capability;
- Constraint authority;
- evaluation-focused capability over supported external/reference/Learned State subjects;
- Execution if Learning or Evaluation remains;
- Provenance where a meaningful remaining relationship exists.

### Product-scope meaning

A no-Generation family member can still be a coherent SYNGAN design contraction, but it is no longer a synthetic-output-producing application variant. Documentation must not continue to advertise Generation outcomes.

---

## 3.6 Remove Constraint

No accepted concept universally depends on Constraint.

### Capabilities lost

- reusable prescriptive-rule definition, revision and binding;
- claims that Learning/Generation honor reusable Constraint authority;
- Constraint-based evaluative questions unless redefined to a different legitimate Criterion subject.

### Capabilities retained

Learning, Generation, Evaluation/Evidence and other concepts remain valid when no reusable prescriptive rule is part of the advertised capability.

### Product-scope meaning

Constraint removal is a capability contraction, not semantic permission to hide equivalent mandatory rules inside Strategy, Generation Condition, Data Meaning, or Evaluation.

If the product still claims reusable prescriptive rules, Constraint must be restored.

---

## 3.7 Remove Evaluation Criterion

Evaluation/Evidence universally require Criterion.

Therefore:

```text
remove Evaluation Criterion
  => remove Evaluation
  => remove Evidence
```

### Capabilities lost

- reusable evaluative-question/standard authority;
- Evaluation and durable Evidence;
- evaluation-gated Generation completion;
- empirical disclosure/fidelity/utility/validity findings represented through the accepted evaluation chain.

### Capabilities retained

Learning/Learned State, Generation, Constraint, appropriate Execution, and appropriate Provenance may remain.

### Product-scope meaning

A product cannot retain metrics/tests and call them Evaluation after removing Criterion; doing so would reintroduce the rejected "available metric defines quality" behavior.

---

## 3.8 Remove Evaluation

Evaluation and Evidence form one SCC.

Therefore:

```text
remove Evaluation => remove Evidence
```

Evaluation Criterion may remain independently as reusable question/standard authority.

### Capabilities lost

- committed examination lifecycle;
- durable findings established through Evaluation;
- evaluation-gated Generation;
- supported evidence-producing privacy/disclosure/fidelity/utility/validity examination.

### Product-scope meaning

A Criterion-only contraction remains coherent, but no claim may imply that the question has been answered merely because it is defined.

---

## 3.9 Remove Evidence

Because of the same SCC:

```text
remove Evidence => remove Evaluation
```

Evaluation Criterion may remain.

A design that keeps Evaluation but treats transient metric output as the result is not a valid contraction; it breaks Evaluation's accepted purpose.

---

## 3.10 Remove Execution

No accepted concept universally depends on Execution.

### Capabilities lost

- durable operational identity across attempts/platform jobs;
- retry/recovery/cancellation/indeterminate operational history as a product capability;
- Execution-owned Attempt history and operational realization semantics.

### Capabilities retained

Learning, Generation and Evaluation may remain when their realization does not require the durable operational capability advertised by Execution.

### Product-scope meaning

Removing Execution does not transfer retry/attempt/platform-job authority into domain activities. A contracted variant must narrow its operational claims rather than hide Execution semantics elsewhere.

---

## 3.11 Remove Provenance

No accepted concept universally depends on Provenance for its own purpose.

### Capabilities lost

- typed traversal of derivation/binding/realization/evaluation/dependency/historical relationships;
- product-level provenance/history inspection and reconstruction capability.

### Capabilities retained

All other concepts can preserve their local historical bindings/references required by their own semantics.

### Product-scope meaning

Removing Provenance does not permit erasing concept-owned history or exact commitments. It removes the separate cross-concept typed relationship capability, not the historical integrity of each concept.

---

# 4. Strongly connected component contraction rules

## 4.1 L-CLUSTER

```text
L-CLUSTER = { Learning, Learned State }
```

The application family cannot contract only one member while preserving the other under current scope.

Valid contraction removes both together.

Consequences:

- learned-state-assisted Generation is lost;
- direct Generation may remain;
- Data Meaning/Strategy may remain as authorities or support direct Generation;
- Execution may remain only if Generation or Evaluation still supplies its one-of activity prerequisite;
- Provenance may remain only if another meaningful relationship witness survives.

## 4.2 E-CLUSTER

```text
E-CLUSTER = { Evaluation, Evidence }
```

Valid contraction removes both together. Evaluation Criterion may remain independently.

Consequences:

- evidence-producing examination is lost;
- evaluation-gated Generation is lost;
- Generation may remain with a completion basis that does not require Evaluation/Evidence;
- Execution may remain only if Learning or Generation still supplies its one-of prerequisite;
- Provenance may remain only if another meaningful relationship witness survives.

---

# 5. Side-constraint consequences during contraction

## 5.1 Execution orphaning

After any contraction, if Execution remains but all three realizable activity concepts are absent:

```text
Learning not in S
Generation not in S
Evaluation not in S
Execution in S
```

then the resulting subset is invalid.

Repair options are only:

- remove Execution; or
- restore at least one valid activity closure.

Do not invent generic Work merely to preserve Execution.

## 5.2 Provenance orphaning

After contraction, Provenance must still have at least one meaningful relationship/history witness.

If contraction removes every relationship the variant intends to expose, Provenance must also be removed or the intended provenance capability must be redefined around a surviving legitimate relationship.

Do not retain Provenance as an empty metadata catalog.

## 5.3 Capability-claim orphaning

A contracted subset may be structurally coherent yet semantically invalid for its old product description.

Examples:

```text
remove L-CLUSTER from learned-generation variant
  => direct Generation may remain
  => "learned-state-assisted Generation" claim must be removed

remove E-CLUSTER from evaluation-gated Generation
  => Generation may remain
  => evaluation-gated completion claim must be removed

remove Constraint
  => Generation may remain
  => reusable prescriptive-rule support claim must be removed
```

Product documentation and later mappings must track the actual family member rather than the former larger variant.

---

# 6. Systematic addition/extension consequences

## 6.1 Add Data Meaning

Data Meaning can be added without requiring another concept.

It adds explicit descriptive semantic authority but does not by itself add Generation, Learning, Constraint, Evaluation, or other behavior.

## 6.2 Add Synthesis Strategy

Strategy can be added independently.

It adds reusable synthesis-behavior authority but does not by itself imply that Learning or Generation capability is present.

## 6.3 Add Learning or Learned State

Adding either requires full L-CLUSTER closure:

```text
add Learning OR Learned State
  => add Learning + Learned State
  => add Data Meaning + Synthesis Strategy
```

The extension adds reusable source-informed derivation capability.

It does not add Generation automatically.

## 6.4 Add Generation

Adding Generation requires:

```text
add Generation
  => add Data Meaning
  => add Synthesis Strategy
```

unless those authorities already exist.

This adds direct-generation capability at minimum.

Learned-state-assisted Generation additionally requires L-CLUSTER.

## 6.5 Add Constraint

Constraint can be added independently and adds reusable prescriptive-rule authority.

Consumers may then bind it where their current semantics allow. Adding Constraint does not force a consumer to exist.

## 6.6 Add Evaluation Criterion

Criterion can be added independently and adds reusable evaluative-question/standard authority.

It does not imply an Evaluation has occurred.

## 6.7 Add Evaluation or Evidence

Adding either requires E-KERNEL closure:

```text
add Evaluation OR Evidence
  => add Evaluation + Evidence
  => add Evaluation Criterion
```

The extension adds evidence-producing examination capability.

The evaluated subject may be external or another included concept according to the Criterion/method contract.

## 6.8 Add Execution

Execution may be added only when the resulting variant includes at least one valid Learning, Generation, or Evaluation capability.

If no such activity exists, adding Execution alone is invalid.

Adding Execution adds durable operational realization semantics; it does not change domain semantic completion authority.

## 6.9 Add Provenance

Provenance may be added only where the resulting variant has at least one meaningful provenance relationship/history witness.

Adding Provenance adds typed historical relationship capability but does not copy or take ownership of source concept state.

---

# 7. Capability-oriented extension patterns

## 7.1 Direct Generation -> learned-state-assisted Generation

Starting from:

```text
G-KERNEL
```

add:

```text
Learning + Learned State
```

Data Meaning/Strategy are already present, yielding:

```text
LG-VARIANT
```

This is ordinary current-family extension, not new concept discovery.

## 7.2 Generation -> evaluation-gated Generation

Starting from G-KERNEL, add E-KERNEL.

This is ordinary family extension when the evaluation chain is sufficient for the required completion question.

## 7.3 Add reusable prescriptive rules

Add Constraint.

This remains ordinary extension so long as the desired functionality is reusable prescriptive rule definition/binding already owned by Constraint.

## 7.4 Add durable operational lifecycle

Add Execution to a variant that already has at least one supported domain activity.

This remains ordinary extension for retry/recovery/cancellation/indeterminate operational history already owned by Execution.

## 7.5 Add typed provenance/history

Add Provenance where at least one meaningful relationship witness exists.

This remains ordinary extension while the purpose is traversal/explanation of typed history already owned by Provenance.

## 7.6 Add topology breadth

Single-table -> time-series -> shared-key multi-table -> legitimate composite structured topology is ordinary extension **within existing concepts** when the additional semantics can be represented through Data Meaning, Strategy, Generation, optional Constraint, and Evaluation/Evidence.

No current `Relationship`, `TimeSeries`, `Table`, or topology-mode concept is required.

## 7.7 Add text-bearing structured-data capability

Adding source-language/free-form text fields inside structured data remains ordinary extension through current Data Meaning/Strategy/Generation and optional Learning/Evaluation semantics.

No current Text/Tokenizer/Vocabulary/Language Model concept is required.

---

# 8. Ordinary extension versus concept rediscovery

The following current additions are ordinary application-family extension when their accepted semantics are sufficient:

```text
add Constraint
add E-KERNEL
add L-CLUSTER
add Execution
add Provenance
add topology/text capability through existing concepts
combine existing kernels
```

Fresh discovery is required when the desired extension creates an independent purpose/lifecycle not owned cleanly by the current catalog.

## 8.1 Current explicit rediscovery triggers

The following triggers remain current from Phase 008-G.

### Formal composable privacy/accounting

If SYNGAN adds mechanism-specific privacy state such as reusable privacy-unit/adjacency definitions, budget allocation/consumption/composition/exhaustion, fresh discovery is required.

Do not turn generic `Privacy` into an umbrella concept and do not store such state casually on Evidence or Generation.

### Product-owned governance / release decisions

If SYNGAN becomes responsible for organizational use/release approval rather than merely supplying Evidence/Provenance/security integration, discovery must reopen.

Do not add `approved` to Generation or Evidence.

### Independently reusable request/cohort definitions

If Generation requests, cohorts, segments, or similar definitions acquire a reusable/negotiable/approval lifecycle independent of one Generation, rediscover rather than stretching subordinate Generation Request/Condition semantics.

### Independent synthetic-output lifecycle

If synthetic output acquires product-owned publication, versioning, retirement, transformation, release governance, or lifecycle management independent of Generation, rediscover `Output` or the appropriate candidate.

### Arbitrary graph/recursive topology

If topology requirements exceed the current structured topology boundary and introduce independently meaningful graph relationship state/actions, fresh discovery is required rather than automatically promoting the existing descriptive Relationship vocabulary.

### Product-owned economic/resource management

If SYNGAN gains independent allocation/trading/governance of capacity, budget, quota, spend, or similar resources, discovery must reopen.

## 8.2 Additional boundary rule

A new capability should trigger rediscovery if satisfying it would otherwise require any accepted concept to:

- own another concept's state;
- gain a second unrelated purpose;
- absorb an external organizational authority;
- become a generic infrastructure umbrella;
- treat a representation resource as product functionality;
- create persistent cross-concept shadow state merely for convenience.

---

# 9. Product-scope consequence matrix

| Change | Forced concept consequence | Capability consequence | Classification |
|---|---|---|---|
| Remove Data Meaning | remove Learning, Learned State, Generation | loses semantic synthesis/Learning/Generation | closure-breaking contraction |
| Remove Strategy | remove Learning, Learned State, Generation | loses synthesis behavior/Learning/Generation | closure-breaking contraction |
| Remove Learning | remove Learned State | loses learned-state capability; direct Generation may remain | SCC contraction |
| Remove Learned State | remove Learning | same as above | SCC contraction |
| Remove Generation | none universally | loses synthetic output production | capability contraction |
| Remove Constraint | none universally | loses reusable prescriptive-rule capability | capability contraction |
| Remove Criterion | remove Evaluation + Evidence | loses evidence-producing evaluation | closure-breaking contraction |
| Remove Evaluation | remove Evidence | Criterion may remain unanswered | SCC contraction |
| Remove Evidence | remove Evaluation | Criterion may remain unanswered | SCC contraction |
| Remove Execution | none universally | loses durable operational-realization capability | capability contraction |
| Remove Provenance | none universally | loses typed cross-concept provenance/history | capability contraction |
| Add Learning/LS | add full L-KERNEL closure | adds reusable learned-state derivation | ordinary extension |
| Add Generation | add DM + Strategy | adds direct synthesis-output capability | ordinary extension |
| Add Evaluation/Evidence | add E-KERNEL closure | adds evidence-producing evaluation | ordinary extension |
| Add Constraint | none forced | adds reusable rule authority | ordinary extension |
| Add Execution | must have Learning or Generation or Evaluation | adds durable operational lifecycle | conditional extension |
| Add Provenance | must have meaningful relationship witness | adds typed provenance/history | conditional extension |

---

# 10. Documentation and explanation consequences

A contracted or extended family member must be documented according to the concepts/capabilities it actually includes.

## 10.1 Do not preserve stale promises

When a concept is removed, later mapping/product documentation must remove claims that require it.

Examples:

- no Learning/Learned State -> do not advertise learned-state-assisted generation;
- no E-KERNEL -> do not advertise evaluation-backed findings or evaluation-gated completion;
- no Constraint -> do not advertise reusable prescriptive-rule support;
- no Execution -> do not advertise durable retry/recovery/cancellation history;
- no Provenance -> do not advertise typed provenance traversal.

## 10.2 Preserve prerequisite-first explanation

Extensions should be explained by introducing required concepts before dependent capabilities.

Contractions should explain both:

1. the removed concept/capability; and
2. any dependent concepts/capabilities that must also disappear or be re-scoped.

## 10.3 Application-family validity is not packaging policy

Nothing in this authority establishes package/module boundaries, install extras, commercial editions, deployment profiles, service splits, persistence partitions, or API namespaces.

Those are later representation/product decisions and must not be inferred mechanically from concept subsets.

---

# 11. Synchronization handoff implications

009-D does not change the synchronization catalog.

It does, however, establish the variant consequences that 009-E must use when replaying SYNC-01 through SYNC-15.

For each synchronization, 009-E must ask:

- are all participants present in the current family member?;
- does contraction remove the reason for the synchronization entirely?;
- is the synchronization universal whenever participants are present, or only when a narrower capability claim is active?;
- does an extension activate a previously irrelevant synchronization without changing concept ownership?;
- does any synchronization accidentally recreate a capability whose owning concept has been contracted away?

No synchronization may be retained merely to simulate missing concepts.

---

# 12. Current methodology disposition

009-D closes the current add/remove consequence obligation:

```text
D1  CURRENTLY CLOSED — canonical inclusion-dependence graph
D2  CURRENTLY CLOSED — application family / valid subsets
D3  CURRENTLY CLOSED — dependence-derived explanation ordering
D4  CURRENTLY CLOSED — systematic contraction/extension and add/remove consequences
```

No E-row is closed by 009-D.

## Current catalog result

```text
accepted concepts          11
accepted synchronizations  15
concept add/remove          NONE
concept merge/split/rename  NONE
new concept promoted        NONE
synchronization change      NONE
```

No J1/J2/J3 defect is exposed by the contraction/extension audit.

The current eleven-concept catalog supports the required contractions/extensions without hidden replacement concepts or boundary erosion.

## Implementation hold

009-D is design authority only.

```text
JACKSON CONCEPT DESIGN     NOT COMPLETE
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## Current next boundary

**009-E — Synchronization Inventory Revalidation Across the Application Family** is next eligible.

009-E must replay the current fifteen synchronization candidates against the family and consequence rules now closed by 009-A through 009-D.
