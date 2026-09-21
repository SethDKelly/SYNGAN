---
type: Phase Record
title: 002-A — Data Meaning & Constraint Specification
status: complete
---

# 002-A — Data Meaning & Constraint Specification

## Objective

Deepen the accepted [Data Meaning](../../concepts/data-meaning.md) and [Constraint](../../concepts/constraint.md) concepts into sufficiently precise state, revision, authority, applicability, uncertainty, and invariant semantics for later experience and representation design.

The phase preserves the Phase 001 descriptive-versus-prescriptive boundary while making explicit how inferred meaning, steward declarations, rule revisions, contextual applicability, unsupported rules, conflict, and enterprise-scale control-plane behavior must work.

## Governing authority

002-A is governed by:

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Terminology Policy](../../authority/terminology-policy.md)
- [Problem Knowledge](../../problem/index.md)
- [Accepted Concepts](../../concepts/index.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Phase 001 Exit](../001/001-H-phase-001-consolidation-initial-concept-catalog.md)

The canonical concept specifications remain under `docs/concepts/`; this phase record preserves the refinement history and conclusions.

## Scope

002-A specifies:

- Data Meaning logical scope and semantic assertion model;
- explicit unknown/unresolved semantic state;
- declared versus inferred meaning;
- semantic authority/source and override/correction rules;
- Data Meaning revision lifecycle and historical binding;
- relationship between structural observations/source characterization and semantic authority;
- Constraint rule/scope/revision semantics;
- Constraint applicability and semantic prerequisites;
- Constraint handling disposition versus satisfaction;
- conflicting constraints and satisfiability uncertainty;
- authority/source and supersession semantics;
- Data Meaning ↔ Constraint interaction;
- control-plane scale expectations;
- synchronization refinements to SYNC-01, SYNC-02, SYNC-03, SYNC-06, SYNC-12, SYNC-14, and SYNC-15 where necessary.

## Non-goals

002-A does not select:

- Python classes or module layout;
- Spark SQL/Spark metadata representation;
- YAML/JSON metadata schemas;
- semantic type enums;
- inference algorithms;
- constraint expression language;
- distributed rule-enforcement implementation;
- public API names;
- storage/persistence formats;
- enterprise identity/authorization integration;
- exact Generation completion semantics for constraint verification;
- exact Evaluation evidence taxonomy for constraint satisfaction;
- relational/multi-table implementation;
- formal privacy mechanisms.

Those remain later concept specification or representation work.

## Canonical authority refined

002-A directly deepens:

1. [Data Meaning](../../concepts/data-meaning.md)
2. [Constraint](../../concepts/constraint.md)
3. [Core Synchronizations](../../synchronizations/core-synchronizations.md)

No new standalone concept is introduced.

## Data Meaning specification decisions

### 1. Data Meaning is semantic authority, not physical schema

Physical data type and structure can inform semantic interpretation but cannot determine it automatically.

Examples:

- integer does not imply continuous numeric meaning;
- string does not imply categorical meaning;
- observed uniqueness does not establish identifier semantics;
- date-like formatting does not establish date semantics.

This preserves Data Meaning as descriptive domain interpretation rather than an alias for Spark schema.

### 2. Meaning can apply at multiple logical scopes

Data Meaning is not restricted to individual fields.

It can describe:

- fields;
- groups of fields;
- record-level semantics;
- dataset-level semantics;
- future relational/cross-scope semantics.

Therefore Phase 002-A preserves the Phase 001 rule that no permanent field-local or single-table invariant may enter the conceptual model.

### 3. Semantic assertions are attributable

A material semantic assertion needs enough conceptual state to identify:

- subject/scope;
- semantic property;
- interpretation;
- declared versus inferred origin;
- authority/source;
- confidence/uncertainty for inference;
- material supporting basis/reference;
- status in the effective revision.

The representation remains deferred.

### 4. Unknown and unresolved are first-class semantic states

Absence of meaning does not authorize an implementation default.

Data Meaning may explicitly retain:

- unknown meaning;
- unresolved alternatives;
- unsupported inference;
- conflicting declarations.

A partially resolved revision is valid as a semantic artifact. Whether an activity can proceed depends on which semantics that activity actually requires.

### 5. Material inference must be visible before commitment

Inference may use profiles, distributed statistics, heuristics, or models.

However, if inferred meaning materially changes how committed Learning, Generation, or Evaluation treats data, that interpretation must be surfaced as attributable Data Meaning before commitment.

A model implementation cannot create hidden semantic authority merely by embedding an inference into preprocessing.

### 6. Explicit declarations outrank silent inference

For the same semantic proposition/scope:

- inference cannot silently replace an authoritative declaration;
- explicit authorized correction may supersede inferred meaning;
- conflicts among authoritative declarations remain unresolved until explicitly reconciled;
- inference confidence alone does not grant authority over declaration.

SYNGAN records authority/source but does not become a general enterprise organizational policy engine.

### 7. Data Meaning uses historical revisions

A material semantic change creates a new revision.

The conceptual lifecycle distinguishes:

- draft;
- effective;
- superseded;
- invalidated.

Once committed work binds a revision, its semantic meaning is immutable for history. Later corrections affect future work only.

### 8. Historical error does not rewrite history

If an earlier meaning revision is later discovered to be wrong:

- it can be invalidated for future use;
- new activities may reject or qualify historical Learned State/output because of that discovery;
- the original Learning/Generation/Evaluation history still records the meaning it actually used.

The framework records truth about what happened rather than retrospectively pretending corrected knowledge existed earlier.

## Constraint specification decisions

### 1. Constraint is reusable prescriptive authority

Constraint states a rule applicable synthetic output must obey. It remains independent of the implementation that attempts to enforce or validate it.

Constraint therefore cannot be collapsed into:

- model preprocessing;
- Generation Condition;
- Strategy capability;
- Evaluation metric;
- enterprise release policy.

### 2. Constraints can span different logical scopes

The concept supports rules over:

- individual values;
- multiple fields;
- records;
- cross-record/dataset properties;
- aggregate/distribution properties when genuinely prescriptive;
- future relational scope.

No row-local/single-table invariant is introduced.

### 3. Rule semantics are revisioned

Changing the meaning of a rule creates a new revision.

The conceptual lifecycle distinguishes:

- draft;
- effective;
- superseded;
- retired;
- invalidated.

Retired means intentionally withdrawn from future use; invalidated means known to be unsuitable/incorrect. Both remain historically visible.

### 4. Applicability is contextual

Constraint owns:

- rule;
- scope;
- semantic prerequisites;
- authority/source.

The consuming activity owns whether that exact revision applies in the specific context.

Applicability can depend on Data Meaning, operation scope, requested semantics, and explicit prerequisites.

Therefore no global mutable `constraint.applies_to(dataset)` truth is accepted into the concept model.

### 5. Handling disposition is activity-owned

When an applicable rule is bound, the activity records how it will handle the rule where relevant.

The canonical conceptual dispositions are:

- enforced;
- validated later;
- unsupported;
- not applicable.

These may be refined in later phases, but rule ownership remains with Constraint.

### 6. Unsupported required rules cannot disappear

A selected Strategy or method lacking support for a required Constraint does not weaken or delete the rule.

The unsupported state remains explicit in the committed activity and its provenance.

### 7. Handling is not satisfaction

`enforced`, `validated later`, and `unsupported` describe handling.

They are not the same as observed result states such as:

- satisfied;
- violated;
- not assessed;
- indeterminate.

Constraint itself owns no global satisfaction flag. Satisfaction observations belong to Generation/Evaluation/Evidence context.

This prevents capability promises from silently becoming Evidence.

### 8. Constraint conflict is not silently resolved

Two effective required Constraints can conflict or be unsatisfiable together.

SYNGAN must surface known conflicts or inability to establish satisfiability. It does not discard a rule because an algorithm prefers another.

Because satisfiability can be contextual or computationally difficult, unknown satisfiability remains unknown rather than becoming an implicit compatibility success.

### 9. New rules do not govern old output retroactively

A later Constraint revision can be evaluated against historical output as a new evaluative question.

It cannot be represented as though the newer rule governed the original Generation.

## Data Meaning ↔ Constraint boundary refinement

002-A locks the following distinction:

> **Data Meaning states what the data means. Constraint states what valid applicable output must obey.**

Examples:

- `customer_id is an identifier` → Data Meaning;
- `customer_id values must be unique` → Constraint;
- `start_date and end_date represent dates` → Data Meaning;
- `end_date >= start_date` → Constraint.

A Constraint may depend on Data Meaning to resolve its subjects. That dependency does not transfer ownership.

If the semantic prerequisite is unresolved, the activity must preserve the unresolved dependency rather than silently inventing meaning.

## Condition boundary reaffirmed

Condition remains Generation-owned request direction.

For example:

- `generate records where region = Midwest` is a Condition when it describes the requested population;
- `end_date must not precede start_date` is a Constraint when it describes validity.

A future implementation may use the same predicate/expression machinery for both, but shared machinery cannot collapse their semantics.

## Authority conclusions

Neither Data Meaning nor Constraint makes SYNGAN a universal enterprise governance system.

The framework records sufficient authority/source state to support:

- inspection;
- explicit correction/supersession;
- historical attribution;
- integration with external governance/catalog authority.

It does not invent implicit precedence among organizational actors beyond the accepted semantic rule that inference cannot silently override an authoritative declaration.

## Scale conclusions

Data Meaning and Constraint are both primarily **control-plane concepts**.

Their ordinary canonical state should scale with:

- semantic subjects/assertions/revisions;
- rule count/complexity/scope;

rather than source/synthetic row count.

Distributed scans, profiling, enforcement, and validation may operate over hundreds of millions of records, but their row-level intermediate state does not become canonical Data Meaning or Constraint state merely because those operations support the concepts.

This protects the enterprise-scale design from accidentally putting corpus-growing semantic/rule state into driver-local objects.

## Synchronization refinements

002-A refines the accepted synchronization authority without changing synchronization IDs.

### SYNC-01

Now explicitly requires:

- material inferred meaning be inspectable before commitment;
- unresolved/invalidated required meaning remain visible;
- later revision compatibility be a future-use question rather than historical mutation.

### SYNC-02

Now distinguishes Strategy capability from actual Constraint satisfaction and prohibits reuse of compatibility claims across materially different contexts without equivalence justification.

### SYNC-03

Now explicitly defines:

- contextual applicability ownership;
- handling disposition semantics;
- handling versus satisfaction;
- unresolved Data Meaning dependency;
- conflict/satisfiability uncertainty.

### SYNC-06

Generation commitment must retain unsupported/unresolved applicable Constraint state rather than dropping it. Phase 002-D will determine its effect on semantic completion.

### SYNC-12

Constraint-satisfaction Evidence answers a specific rule/output/method question without becoming authority for the Constraint definition.

### SYNC-14 / SYNC-15

Inference, rule binding, handling disposition, and semantic/rule revisions remain attributable through stable references without copying row-level data into Provenance or a generic reproducibility object.

## Invariant set added/refined

### Data Meaning invariants

1. Bound semantic revisions are immutable in meaning.
2. Historical work retains the revision actually used.
3. Material inference is attributable and inspectable.
4. Inference cannot silently replace authoritative declaration.
5. Unknown/unresolved semantics remain explicit.
6. Structural observation does not equal semantic authority.
7. ordinary state does not scale linearly with row count by default.
8. no permanent field-local/single-table assumption.

### Constraint invariants

1. Bound rule revisions are immutable in meaning.
2. rule authority remains separate from activity handling.
3. unsupported required rules stay visible.
4. applicability/compatibility is contextual, not global mutable state.
5. handling disposition is distinct from satisfaction Evidence.
6. unknown satisfiability/applicability cannot be treated as success.
7. rule conflicts are not silently resolved by implementation preference.
8. new revisions do not retroactively govern old work.
9. ordinary rule state does not scale linearly with row count by default.
10. no permanent row-local/single-table assumption.

## Deferred questions handed forward

### To 002-B — Synthesis Strategy

- capability vocabulary for Data Meaning features and Constraint classes;
- how Strategy declares requirements/limitations without becoming implementation registry metadata;
- how contextual compatibility is expressed consistently.

### To 002-C — Learning / Learned State

- exact semantic commitment point for Learning;
- how meaning/rule revisions become Learned State compatibility history;
- when changed Data Meaning/Constraints should prohibit or qualify Learned State reuse.

### To 002-D — Generation

- how applicable required Constraint handling participates in Generation completion;
- semantics for post-generation validation;
- partial output when required Constraints are unresolved or violated;
- how Conditions are represented within Generation state without becoming a separate concept.

### To 002-E — Evaluation / Evidence

- canonical Evidence semantics for Constraint satisfaction;
- treatment of indeterminate/approximate validation;
- when validation method limitations prevent a satisfaction claim.

### To 002-G — Provenance / Reproducibility

- exact historical facts required for inferred semantic basis, authority, revisions, applicability, and handling;
- reproducibility requirements when semantic inference methods are stochastic or data-dependent.

## Exit criteria

002-A is complete when:

- [x] Data Meaning semantic scope is defined without field-local bias;
- [x] semantic assertions and explicit unresolved states are specified;
- [x] declared/inferred authority rules are explicit;
- [x] material inference cannot remain hidden in model preprocessing;
- [x] Data Meaning revision lifecycle/history semantics are explicit;
- [x] structural characterization remains distinct from semantic authority;
- [x] Constraint rule/scope/revision semantics are explicit;
- [x] Constraint applicability ownership is contextual and non-global;
- [x] handling disposition is distinct from satisfaction;
- [x] unsupported required rules remain visible;
- [x] conflict/satisfiability uncertainty is explicit;
- [x] Data Meaning and Constraint boundaries remain distinct;
- [x] Condition remains distinct from Constraint;
- [x] scale/control-plane semantics are explicit;
- [x] accepted synchronization authority is refined without new god-concepts;
- [x] no representation architecture is selected prematurely.

## Exit assessment

**Status: complete.**

Data Meaning and Constraint are now sufficiently specified for Synthesis Strategy capability semantics to depend on precise semantic/rule authority without treating metadata, schema, predicates, or model configuration as the concept model.

## Next phase

**002-B — Synthesis Strategy Specification & Capability Semantics**

002-B should define reusable synthesis-behavior identity/configuration, capability/requirement/limitation semantics, versioning, compatibility obligations, extension-author responsibilities, and how materially different synthesis approaches declare support without forcing all strategies into Learning or one execution model.