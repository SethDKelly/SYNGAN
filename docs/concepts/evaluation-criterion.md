---
type: Concept
title: Evaluation Criterion
status: accepted
---

# Evaluation Criterion

## Purpose

Enable an actor to state, inspect, revise, and reuse the **evaluative question or standard that matters** independently of the method used to examine it.

Evaluation Criterion exists so available metrics do not silently decide what "quality" means. A practitioner may care about fidelity, a model owner may care about downstream utility, a steward may care about validity against a Constraint, and a governance reviewer may care about disclosure risk. Those are different questions even when one Evaluation method can contribute Evidence to more than one of them.

## Concept boundary

Evaluation Criterion is **evaluative-question authority**.

It owns what property/question is being assessed and what semantic scope makes an answer relevant.

It does not own:

- the measurement algorithm, metric, test, estimator, or distributed job — [Evaluation](evaluation.md) owns the examination method;
- the observed result — [Evidence](evidence.md) owns the durable finding;
- [Constraint](constraint.md) rule authority;
- [Generation](generation.md) completion authority;
- privacy guarantees merely because the Criterion concerns disclosure risk;
- external release/use approval;
- a generic enterprise threshold/policy engine.

A Criterion may encode result-interpretation or acceptance semantics needed to answer its own question, but it MUST NOT silently expand into unrelated organizational authorization.

## Criterion state model

A Criterion is a reusable evaluative definition with historical revisions.

### Evaluative question

A Criterion states the property or question whose Evidence an actor wants.

Examples include questions conceptually equivalent to:

- how closely does synthetic output preserve selected statistical relationships from a reference population?;
- how useful is the synthetic dataset for a stated downstream task?;
- does this exact candidate output satisfy Constraint revision C7?;
- did this Generation fulfill mandatory Condition K3 within its committed tolerance?;
- what disclosure risk is observed under a stated threat model and method?;
- how stable is a result under repeated generation or evaluation?;

These examples do not define a closed Criterion taxonomy.

### Subject and scope

A Criterion identifies enough scope to determine what is being evaluated and what population/domain the answer concerns.

Scope may include:

- a complete synthetic output;
- a subset/cohort;
- fields or relationships;
- aggregate/distribution properties;
- a Learned State where the question legitimately concerns reusable state;
- a source/synthetic comparison;
- future relational/cross-dataset scope.

Criterion scope is logical rather than physical. Spark partitions, files, workers, or sample batches do not define the conceptual population unless the Criterion intentionally concerns them.

### Reference context

A Criterion may depend on reference context such as:

- source/reference dataset identity;
- a historical synthetic output;
- a baseline model/result;
- a bound Constraint revision;
- a Generation Condition and tolerance;
- a downstream task/use context;
- a threat model or privacy-risk scenario;
- domain expectations supplied by an authorized actor.

The Criterion owns the meaning of the comparison/question, not copies of referenced concept state.

### Interpretation / sufficiency semantics

Where necessary, a Criterion may state what kind of answer is meaningful for its own question.

This may include:

- exact/universal satisfaction expectation;
- tolerance or acceptable error band;
- statistical confidence/uncertainty expectation;
- comparison direction or baseline;
- required coverage/population scope;
- whether an indeterminate result is acceptable as an answer;
- minimum methodological strength needed for the Criterion to be considered answered.

These are **Criterion-answer semantics**, not automatically organizational approval thresholds.

For example, a Criterion derived from a universal Constraint such as `quantity >= 0 for every record` may require evidence capable of supporting a universal claim. A sample-based method cannot silently redefine that Criterion into "no violations observed in the sample."

### Criterion revision

A material change to the evaluative question, scope, reference context, interpretation, or answer-sufficiency semantics creates a new revision.

Conceptually revisions distinguish at least:

- **draft** — still being defined and not available for committed Evaluation;
- **effective** — available to be bound by new Evaluation;
- **superseded** — replaced for future selection while remaining historical authority;
- **retired** — intentionally no longer selected for new work;
- **invalidated** — known to be materially unsuitable or erroneous for new reliance.

Historical Evidence remains tied to the Criterion revision it actually answered.

## Criterion families remain distinct

SYNGAN intentionally does not collapse the following into one universal `quality` score:

### Fidelity

Asks whether selected reference properties/relationships are preserved to a stated degree.

High fidelity does not imply utility, validity, or privacy.

### Utility

Asks whether synthetic data is fit for a stated downstream purpose or task.

Utility is use-context dependent and cannot be inferred solely from distribution similarity.

### Validity

Asks whether output satisfies structural, semantic, relational, Condition, or Constraint expectations under a stated scope.

Validity may require universal, bounded, or probabilistic evidence depending on the actual rule/question.

### Privacy / disclosure risk

Asks about privacy properties or observed disclosure risk under an explicit mechanism, threat model, attacker knowledge, and method.

A disclosure-risk Criterion does not itself establish a formal privacy guarantee, and synthetic origin is not enough to answer it.

The project may add other Criterion families later without creating one aggregate Quality concept.

## Criterion derived from Constraint or Generation Condition

A Constraint or mandatory Generation Condition may motivate a Criterion without transferring authority.

For a Constraint:

- Constraint owns the prescriptive rule;
- Criterion owns the evaluative question about a specific output/rule context;
- Evaluation owns the method;
- Evidence owns the observation;
- Generation owns whether that Evidence is sufficient for its completion contract.

For a mandatory Condition:

- Generation owns the request-specific Condition and tolerance;
- Criterion may express the question "did candidate output fulfill this Condition sufficiently?";
- Evaluation/Evidence may establish the answer;
- the Condition does not become a reusable Constraint merely because it is evaluated.

## Answer strength and method compatibility

A Criterion constrains what kind of Evaluation can legitimately answer it.

The required answer may be conceptually:

- **universal/exhaustive** — property asserted across the full committed logical scope;
- **bounded** — property asserted within explicit deterministic bounds/tolerance;
- **statistical** — population property estimated with stated uncertainty/confidence;
- **comparative** — relative result against a baseline/reference under defined semantics;
- **diagnostic/exploratory** — observation intended to inform investigation rather than establish a completion-level claim.

These are semantic categories, not a required API enum.

An Evaluation method whose attainable claim strength is weaker than the Criterion requires is incompatible or can only produce explicitly insufficient/limited Evidence. The method MUST NOT silently weaken the Criterion.

## Generation-completion Criteria

When Evaluation exists to satisfy a mandatory Generation completion requirement, the Criterion MUST preserve the exact committed requirement being tested.

Examples:

- a universal required Constraint requires evidence capable of supporting universal satisfaction unless the committed rule itself permits bounded/statistical assurance;
- an exact quantity requirement requires evidence that can establish the requested cardinality semantics;
- a mandatory Condition with `±2%` tolerance may be answerable through a method whose uncertainty is tight enough to determine whether that tolerance was met;
- a best-effort Condition may legitimately produce limited Evidence that supports `completed with limitations` if that behavior was committed explicitly.

The Criterion does not itself mark the Generation complete; it defines the question whose Evidence Generation consumes.

## Authority semantics

A Criterion records sufficient actor/source authority to explain why the question matters and how it is intended to be interpreted.

SYNGAN does not globally decide organizational policy precedence. External governance systems may define or select Criteria and consume Evidence without becoming part of the Criterion concept.

## Actions

### Define

Establish a draft Criterion with question, scope, reference context, authority, and answer semantics.

### Inspect

Review exactly what is being asked and what would constitute a meaningful answer before selecting a method.

### Select / reuse

Use an effective Criterion across multiple Evaluations where the question remains semantically equivalent.

### Revise / supersede

Create a new revision when the material question, scope, reference, tolerance, or answer semantics change.

### Retire / invalidate

Stop new use without rewriting historical Evidence.

## Scale semantics

Evaluation Criterion is control-plane state. Its ordinary state SHOULD scale with evaluative questions, scopes, revisions, and reference definitions rather than source/synthetic row count.

A Criterion may require examination of hundreds of millions of records, but those records and per-row results are not canonical Criterion state.

No Criterion rule may require full-output collection to the driver merely to express the question.

## Failure / ambiguity semantics

A Criterion may be unsuitable for committed Evaluation when:

- subject/scope cannot be stably identified;
- required reference context is unavailable or ambiguous;
- the question is internally contradictory;
- answer-sufficiency semantics are missing where they are required to determine completion;
- the Criterion depends on unresolved Data Meaning in a material way;
- the revision is retired/invalidated for new use.

Ambiguity in the question MUST NOT be repaired silently by whatever metric happens to be available.

## Invariants

1. Criterion MUST remain distinct from metric, method, score, Evidence, and approval authority.
2. Evaluation MUST bind the exact Criterion revision it answers.
3. Later Criterion revisions MUST NOT reinterpret historical Evidence.
4. Multiple Evaluation methods MAY address the same Criterion.
5. Available metrics MUST NOT silently define or weaken the Criterion question.
6. Criterion answer-sufficiency semantics MAY constrain method strength without becoming external authorization policy.
7. A method weaker than the Criterion requires MUST NOT produce an overstated claim.
8. Universal required rules MUST NOT be converted into sample-only claims merely for scale convenience.
9. Fidelity, utility, validity, and privacy/disclosure risk MUST remain semantically distinct evaluation dimensions.
10. A Criterion derived from Constraint or Condition MUST NOT take ownership of that source authority.
11. Criterion state SHOULD NOT scale linearly with evaluated row count.
12. No Criterion rule may introduce a permanent single-table assumption.

## Operational principle

A steward requires every generated `quantity` value to be non-negative. The corresponding Evaluation Criterion asks whether candidate output satisfies that exact Constraint revision over the complete logical output. Because the required rule is universal, a small sample is methodologically insufficient even if it finds no violations. A distributed exhaustive Evaluation can examine all partitions without collecting the dataset to the driver and produce Evidence capable of answering the Criterion.

Separately, a data scientist defines a fidelity Criterion asking whether a population distribution is preserved within a stated statistical tolerance. That Criterion may legitimately be answered using a bounded or sampled estimator with explicit uncertainty. The two Criteria therefore demand different kinds of Evidence even when both evaluate the same synthetic output.

## Synchronization

Primary accepted synchronization rules:

- [SYNC-09 — Evaluation Criterion binding](../synchronizations/core-synchronizations.md#sync-09--evaluation-criterion-binding)
- [SYNC-10 — Evaluation method compatibility](../synchronizations/core-synchronizations.md#sync-10--evaluation-method-compatibility)
- [SYNC-12 — Evaluation produces Evidence](../synchronizations/core-synchronizations.md#sync-12--evaluation-produces-evidence)
- [SYNC-13 — Evidence external handoff](../synchronizations/core-synchronizations.md#sync-13--evidence-external-handoff)
- [SYNC-14 — Provenance recording](../synchronizations/core-synchronizations.md#sync-14--provenance-recording-at-material-transitions)

## Representation questions intentionally deferred

Phase 002-E does not decide:

- built-in Criterion class hierarchy;
- metric registry or plugin shape;
- threshold-expression representation;
- SQL/Python/YAML configuration;
- dashboard/report presentation;
- privacy-risk method implementation;
- statistical library choices;
- external governance integration.

Those representations must preserve the question/method/evidence separation defined here.