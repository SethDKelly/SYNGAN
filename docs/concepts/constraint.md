---
type: Concept
title: Constraint
status: accepted
---

# Constraint

## Purpose

Let authorized actors state reusable prescriptive rules that applicable synthetic output is required to satisfy independently of the strategy or activity that attempts to honor them.

Constraint exists so domain validity is not hidden inside a model implementation, preprocessing pipeline, generation algorithm, or evaluation metric. A rule remains authoritative even when different synthesis strategies enforce, defer, validate, or fail to support it differently.

## Concept boundary

Constraint is **prescriptive authority**: it states what applicable synthetic output must obey.

It does not own:

- descriptive semantic interpretation — [Data Meaning](data-meaning.md) owns that;
- request-specific desired characteristics — Generation-owned Condition semantics cover those;
- synthesis strategy capability;
- contextual compatibility state for every dataset or activity;
- measurement method or Evidence of satisfaction;
- organizational release/use approval;
- a general enterprise policy engine.

A rule that merely expresses a preference or target population is not a Constraint unless it carries a genuine prescriptive requirement.

## Conceptual state model

A Constraint is a logical rule lineage with one or more revisions.

### Rule definition

A Constraint revision conceptually contains enough information to identify:

- the prescriptive rule itself;
- the logical scope to which it may apply;
- semantic subjects or roles referenced by the rule;
- applicability prerequisites/conditions intrinsic to interpreting the rule;
- authority/source;
- requirement/severity semantics where materially relevant;
- revision identity and lifecycle state;
- semantic dependencies required to interpret the rule correctly.

The specification does not require one physical predicate language. A future representation may support declarative expressions, typed rule objects, SQL-like predicates, extension-defined rules, or other mechanisms, provided the same conceptual semantics are preserved.

### Scope

A Constraint may apply at different logical scales, including:

- a field/value scope;
- multiple fields within a record;
- record-to-record or dataset-level properties;
- aggregate/distribution-level rules when truly prescriptive;
- future relational or cross-dataset scope.

The concept MUST NOT assume that all Constraints are row-local or single-table.

### Revision

Changing the meaning of a rule creates a new revision.

Conceptually, revisions distinguish at least:

- **draft** — not yet available for committed work;
- **effective** — eligible to be considered/bound by new work;
- **superseded** — replaced for future work while remaining historically authoritative for activities that bound it;
- **retired** — intentionally withdrawn from new use without asserting that the historical rule was wrong;
- **invalidated** — known to be materially erroneous or unsuitable for new reliance.

A representation MAY use different lifecycle labels but MUST preserve these distinctions where they matter.

### Requirement semantics

Constraint is fundamentally prescriptive. Applicable required rules cannot be silently treated as optional.

If requirement/severity metadata is supported, it MUST make clear whether the rule is actually binding for the activity context. A non-binding preference, optimization target, or desired cohort characteristic should instead be represented through Generation intent/Condition or another appropriate concept rather than weakening Constraint semantics.

## Authority semantics

A Constraint records the actor/source under whose authority the rule exists.

SYNGAN does not globally adjudicate enterprise organizational authority. It must preserve enough authority/source information for actors and integrations to understand where a rule came from and to support explicit supersession or reconciliation.

### Conflicting constraints

Two effective Constraints may conflict or be jointly unsatisfiable.

SYNGAN MUST NOT resolve such conflicts by silently discarding one rule based on implementation convenience.

Known conflicts or inability to establish satisfiability must remain visible to the activity that proposes to bind them.

Satisfiability is contextual and may be computationally difficult or impossible to determine completely. Therefore:

- no global `satisfiable=true/false` state belongs to Constraint;
- an activity may perform contextual validation and retain that result locally;
- unknown satisfiability MUST NOT be represented as confirmed compatibility.

## Applicability semantics

Constraint owns the rule's declared scope and prerequisites. The consuming activity owns the **contextual applicability result**.

Applicability may depend on:

- the activity's data/output scope;
- bound Data Meaning;
- requested Generation semantics;
- the operation being performed;
- strategy/method capability;
- other explicit rule prerequisites.

An applicability determination MUST bind or reference the exact Constraint and Data Meaning revisions used when those facts are material.

A Constraint MUST NOT accumulate mutable global state such as `applies_to_dataset_X=true` because applicability can change when context or semantic revisions change.

## Data Meaning dependency

A Constraint may require Data Meaning to interpret its subjects correctly.

Examples:

- Data Meaning: `start_date` and `end_date` represent dates;
- Constraint: `end_date >= start_date`.

If required meaning is unresolved, conflicting, invalidated, or incompatible, the activity cannot silently fabricate the missing semantics in order to claim the Constraint was applied.

A later Data Meaning revision may alter future applicability or interpretation of a Constraint, but MUST NOT rewrite historical activities that bound an earlier meaning/Constraint pair.

## Handling disposition

When an applicable Constraint is bound to Learning, Generation, or Evaluation, the activity records how it will handle the rule where relevant.

Canonical conceptual handling dispositions include:

- **enforced** — the activity/method intends to enforce the rule during its operation;
- **validated later** — the activity does not guarantee enforcement during production but commits to a later validation path where appropriate;
- **unsupported** — the selected strategy/method cannot honor or assess the rule as required;
- **not applicable** — contextual validation establishes that the rule does not apply to this activity scope.

A future specification may refine these states, but it MUST preserve the distinction between rule authority and activity handling.

An unsupported required Constraint MUST remain visible. It MUST NOT disappear from the committed activity specification simply because the selected implementation cannot handle it.

## Handling versus satisfaction

Handling disposition and actual satisfaction are different questions.

Constraint does not own a global satisfaction status.

A particular output may later be assessed as:

- satisfied;
- violated;
- not assessed;
- indeterminate under the available method/evidence.

Those observations belong to the Generation/Evaluation/Evidence context that establishes them, not to the Constraint's canonical rule state.

Likewise, `enforced` is a handling claim and MUST NOT automatically be interpreted as empirical Evidence that every produced record satisfied the rule unless the relevant concept contract establishes that guarantee.

Phase 002-D and 002-E will refine how Constraint handling and satisfaction participate in Generation completion and Evidence.

## Actions

### Declare

Establish a new draft Constraint revision with rule, scope, authority, and requirement semantics.

### Review / Inspect

Examine the rule, scope, authority, dependencies, and revision history independently of any synthesis implementation.

### Revise

Create a materially new rule revision for future use.

A bound historical revision is never edited in place.

### Supersede

Make a newer revision the rule intended for future use while retaining historical validity of prior bindings.

### Retire

Stop selecting the rule for new work without claiming historical error.

### Invalidate

Mark a rule revision as unsuitable for new reliance because it is materially incorrect or unsafe.

### Determine applicability

Evaluate the rule's scope/prerequisites against a specific activity context.

**Result ownership:** the activity owns the contextual result; the Constraint owns the rule/prerequisites used to derive it.

### Associate handling expectations

Declare or bind how an activity is expected to handle an applicable rule without changing the rule's meaning.

## Commitment and historical binding

When Learning, Generation, or Evaluation commits with an applicable Constraint, it MUST bind the exact revision.

The committed activity MUST preserve:

- the bound revision;
- applicability result where material;
- handling disposition where relevant;
- known unsupported or indeterminate conditions.

After commitment:

- a later Constraint revision applies only to future work unless explicitly evaluated against historical output;
- supersession/retirement/invalidation does not rewrite the rule set that governed historical work;
- later Evaluation MAY ask whether historical output satisfies a newer Constraint, but the result MUST be represented as a new evaluation question rather than pretending the newer rule governed original production.

See [SYNC-03](../synchronizations/core-synchronizations.md#sync-03--constraint-binding-and-handling-disposition).

## Constraint and Condition distinction

The same expression shape can represent different semantics depending on purpose.

Examples:

- Generation Condition: `region = "Midwest"` because the requester wants a Midwest-focused synthetic population;
- Constraint: `end_date >= start_date` because any valid applicable output must obey the rule.

A Condition is request-specific direction owned by Generation. A Constraint is reusable prescriptive authority.

Implementation may use shared predicate machinery, but shared representation MUST NOT collapse the concepts.

## Strategy interaction

Synthesis Strategy owns declared capability and limitations. Constraint owns rule meaning. A Learning or Generation activity owns the contextual decision about whether the selected Strategy can handle the bound Constraint revisions.

Therefore:

- Strategy capability MAY state supported classes/forms of Constraints;
- an activity MAY validate specific rule compatibility;
- neither Strategy nor Constraint owns global pairwise compatibility state;
- unsupported rules remain explicit.

See [SYNC-02](../synchronizations/core-synchronizations.md#sync-02--strategy-selection-and-compatibility).

## Evaluation interaction

Evaluation may assess whether output satisfies a Constraint, but it does not become the authority for the rule itself.

Constraint validity can therefore become an Evaluation Criterion or directly inform one, while Evidence records what was actually observed under a method/scope.

A metric result MUST NOT rewrite, weaken, or supersede the Constraint.

## Scale semantics

Constraint is primarily **control-plane rule state**.

Ordinary Constraint state SHOULD scale with the number/complexity of rules and semantic scope, not with the number of source or synthetic records.

Large-scale enforcement or validation may require distributed computation, but row-level violations, samples, diagnostic records, and evidence are outputs of Generation/Evaluation/Execution rather than canonical Constraint state.

A Constraint representation MUST NOT require collecting the full source or synthetic corpus to the driver merely to preserve the rule definition.

## Failure and uncertainty semantics

Constraint-related failure/uncertainty includes at least:

- rule cannot be interpreted because required Data Meaning is unresolved;
- rule is known to conflict with another bound required rule;
- satisfiability cannot be established when required before commitment;
- selected Strategy/method reports the required rule unsupported;
- contextual applicability is indeterminate;
- required post-generation validation cannot be completed;
- rule revision is invalidated or retired for new use.

The response to these conditions depends on the consuming activity's contract. However, no condition may be converted silently into `satisfied` or omitted from traceability.

## Invariants

1. Constraint is prescriptive; Data Meaning is descriptive.
2. A material rule change creates a new revision rather than mutating historical authority.
3. Activities MUST bind the exact applicable Constraint revisions they commit to.
4. Unsupported required Constraints MUST remain visible rather than be silently dropped.
5. Strategy, Learning, Generation, or Evaluation handling of a rule MUST NOT redefine the rule itself.
6. New Constraint revisions MUST NOT be presented as though they governed historical work.
7. Contextual applicability and compatibility results belong to the activity context, not globally mutable Constraint state.
8. Unknown/indeterminate applicability or satisfiability MUST NOT be represented as confirmed satisfaction.
9. Handling disposition MUST remain distinct from actual satisfaction Evidence.
10. Conflicting required Constraints MUST NOT be silently resolved by implementation preference.
11. Constraint MUST NOT absorb Generation Conditions, Evaluation methods, or external use/release policy.
12. Constraint state SHOULD NOT grow linearly with record count merely because enforcement/validation occurs at scale.
13. Constraint semantics MUST allow future cross-record and relational scope; no permanent row-local/single-table invariant may be introduced.
14. Constraint or constraint-satisfaction claims MUST NOT by themselves constitute a formal privacy guarantee or release authorization.

## Operational principle

A steward declares that `end_date >= start_date`, quantity must never be negative, and a pair of domain fields must remain mutually consistent. The rules are effective independently of any selected synthesis algorithm.

A practitioner proposes a Strategy. Contextual validation using the bound Data Meaning shows that two rules can be enforced during Generation while one must be validated after generation. The activity binds the exact Constraint revisions and handling dispositions. If a required rule is unsupported, that fact remains visible rather than disappearing from configuration.

Later, a steward corrects one rule. A new revision governs future work. Historical Generations continue to show the exact rule revision they originally bound.

## Synchronization

Primary accepted synchronization rules:

- [SYNC-01 — Data Meaning revision binding](../synchronizations/core-synchronizations.md#sync-01--data-meaning-revision-binding)
- [SYNC-02 — Strategy selection and compatibility](../synchronizations/core-synchronizations.md#sync-02--strategy-selection-and-compatibility)
- [SYNC-03 — Constraint binding and handling disposition](../synchronizations/core-synchronizations.md#sync-03--constraint-binding-and-handling-disposition)
- [SYNC-06 — Generation commitment and compatibility](../synchronizations/core-synchronizations.md#sync-06--generation-commitment-and-compatibility)
- [SYNC-14 — Provenance recording](../synchronizations/core-synchronizations.md#sync-14--provenance-recording-at-material-transitions)
- [SYNC-15 — Reproducibility-relevant commitment snapshot](../synchronizations/core-synchronizations.md#sync-15--reproducibility-relevant-commitment-snapshot)

## Representation questions intentionally deferred

Phase 002-A does not decide:

- the constraint expression language;
- whether constraints are represented as Python objects, SQL expressions, schemas, YAML, catalog rules, or extension-defined types;
- exact built-in constraint taxonomy;
- distributed enforcement implementation;
- violation-output format;
- persistence/storage representation;
- public API naming;
- enterprise authorization integration.

Those decisions must preserve this concept specification rather than redefine it.