---
type: Concept
title: Evidence
status: accepted
---

# Evidence

## Purpose

Preserve an inspectable observation or result with enough question, method, scope, strength, uncertainty, input, and limitation context that actors can understand what was actually established without rerunning the producing Evaluation.

Evidence exists because a metric value alone is rarely self-explanatory. The same number can support very different claims depending on the Criterion, population examined, sampling design, reference data, method assumptions, uncertainty, and whether the result was exhaustive, bounded, statistical, approximate, or merely diagnostic.

## Concept boundary

Evidence is **durable finding authority**.

It owns the observation that an Evaluation validly established and the context required to interpret that observation later.

It does not own:

- the Criterion question;
- the Evaluation method/lifecycle;
- Constraint or Generation Condition authority;
- Generation completion authority;
- Provenance as a universal history store;
- privacy guarantees merely because the finding concerns disclosure risk;
- external release/use approval;
- a generic enterprise evidence warehouse.

## Evidence state model

An Evidence record represents one independently interpretable finding.

A single Evaluation may produce multiple Evidence records when several findings have distinct interpretation, scope, or applicability.

### Required interpretive content

Evidence conceptually preserves or stably references enough information to identify:

- Evidence identity/version;
- exact Criterion revision answered;
- producing Evaluation;
- evaluated subject/input identity;
- reference/baseline identity where applicable;
- observed result/finding;
- logical scope/population/cohort;
- method identity/configuration sufficient for interpretation;
- coverage model;
- sampling/approximation semantics;
- uncertainty/confidence/error bounds where applicable;
- assumptions and limitations;
- claim-strength/applicability boundary;
- material Data Meaning/Constraint/Condition context where the finding depends on it;
- provenance linkage.

Evidence SHOULD reference canonical upstream state rather than copy entire concept payloads.

## Finding semantics

Evidence must distinguish the substantive answer from the success/failure of the Evaluation that produced it.

An Evidence finding may conceptually indicate states such as:

- property established/satisfied under the stated scope;
- property violated/not satisfied;
- estimated value with uncertainty;
- comparative improvement/degradation/no meaningful difference;
- risk estimate under a stated threat model;
- indeterminate/inconclusive;
- bounded result;
- diagnostic observation not sufficient for a stronger conclusion.

This is not a required universal enum. The finding form is Criterion/method dependent.

## Claim strength

Evidence MUST carry enough semantics to prevent a reviewer from making a stronger claim than the producing Evaluation supports.

Conceptually relevant evidence-strength forms include:

### Exhaustive / universal evidence

Supports a claim over the complete committed logical scope when the method truly examined or established the property over that scope.

Example: a distributed scan checks every relevant record and establishes zero violations for a deterministic row-level Constraint.

### Deterministic bounded / certificate evidence

Supports a property through a proof, construction guarantee, certificate, deterministic bound, or equivalent method whose scope is explicit.

### Statistical evidence

Supports an estimate or population-level statement with stated sampling design, uncertainty/confidence, assumptions, and scope.

It does not become universal evidence merely because no failure was observed in the sample.

### Approximate / sketch evidence

Supports a claim within explicit approximation/error semantics.

### Diagnostic / partial evidence

Supports investigation within an intentionally limited subset/scope and MUST remain clearly insufficient for population-wide claims unless the Criterion says otherwise.

These distinctions may later be represented differently, but claim strength must remain inspectable.

## Evidence and Generation completion

Evidence may be consumed by [Generation](generation.md) when post-production validation is required for completion.

For completion use, Evidence must be tied to:

- the exact candidate output identity;
- the exact mandatory Condition or Constraint semantics being tested;
- the Criterion revision defining the required question;
- method/coverage/uncertainty sufficient for the committed completion contract.

A Generation may rely on Evidence only to the strength the Evidence actually supports.

Examples:

- a universal Constraint cannot ordinarily be satisfied for completion by sample-only Evidence;
- a tolerance-based mandatory Condition may be satisfied by statistical Evidence when its confidence/error semantics are strong enough to determine the committed tolerance;
- an indeterminate result blocks completion when determination is mandatory;
- negative Evidence establishing violation blocks successful completion under the current committed Generation;
- diagnostic Evidence may explain failure without satisfying completion.

Evidence itself does not flip the Generation state. Generation owns the completion decision under its accepted contract.

## Evidence and Constraint authority

Constraint-satisfaction Evidence records what was observed about a specific output under a specific method and rule revision.

It does not:

- redefine the Constraint;
- make a violated rule optional;
- supersede the rule;
- create global `constraint.satisfied=true` state across all outputs;
- transfer rule authority to Evaluation.

Newer Evaluation may produce different Evidence about another output or a newer method without rewriting the historical finding.

## Evidence and Condition authority

A mandatory or best-effort Generation Condition may be evaluated and produce Evidence.

The Evidence answers whether the exact committed Condition semantics were fulfilled under the Evaluation's scope/method. It does not make the Condition reusable across unrelated Generations or convert it into a Constraint.

## Uncertainty and indeterminacy

Uncertainty is first-class Evidence context, not an implementation detail.

Where applicable Evidence must preserve:

- confidence interval or credible interval;
- deterministic error bound;
- sample variance/standard error;
- approximation tolerance;
- false-positive/false-negative limitations;
- representativeness assumptions;
- tail/rare-event sensitivity limitations;
- unresolved ambiguity that prevents a definitive answer.

If uncertainty prevents the Criterion from being answered at the required strength, Evidence must remain indeterminate/inconclusive rather than selecting the favorable interpretation.

## Negative, unfavorable, and risk Evidence

Evidence is not required to be positive.

Valid durable Evidence may establish:

- a Constraint violation;
- Condition failure;
- poor fidelity;
- weak downstream utility;
- elevated disclosure risk;
- no meaningful improvement over a baseline;
- a methodological limit that makes a prior claim unsupported.

Such Evidence is valuable precisely because the Evaluation succeeded in establishing an unfavorable observation.

## Evidence applicability and lifecycle

Evidence is historically immutable in what it observed and how it was produced.

Its future-use status may change conceptually among states such as:

- **applicable/current** — still relevant to the question/context for which actors are using it;
- **superseded** — newer Evidence is preferred for current use;
- **obsolete/stale** — context changed enough that the Evidence is no longer appropriate for current decisions;
- **inapplicable** — the Evidence does not apply to the requested context;
- **invalidated** — a material methodological/data defect was discovered that undermines reliance on the finding.

These status changes do not rewrite the historical observation.

A newer Criterion, regenerated output, changed threat model, or changed downstream task may make old Evidence inapplicable without making the original Evaluation historically false.

## Evidence comparison and conflict

Multiple Evidence records may disagree.

The framework MUST preserve relevant differences such as:

- Criterion revision;
- method;
- scope;
- reference baseline;
- time/data version;
- uncertainty;
- threat model;
- sampling design.

Evidence MUST NOT be averaged or merged automatically merely because values appear numerically compatible.

An explicit Evaluation Criterion or later decision policy may define combination semantics, but Evidence itself does not invent one.

## Privacy/disclosure-risk Evidence

Evidence concerning privacy/disclosure risk must remain scoped to the method and threat model that produced it.

For example, a favorable membership-inference result does not automatically establish safety against attribute inference, linkage attacks, memorization, or another threat model.

Likewise:

- `low observed disclosure risk` is not automatically `formally private`;
- successful use of synthetic data is not proof of anonymization;
- Evidence does not authorize external release.

A formal mechanism-specific privacy guarantee requires its own explicit authority/state where applicable.

## Learned State as an Evaluation subject

Evidence may concern [Learned State](learned-state.md) when a legitimate Criterion asks about reusable state itself, such as memorization/disclosure risk, compatibility characteristics, or another state-level property.

Learned State sensitivity remains independent of whether generated output appears safe. Evidence must identify which subject was actually evaluated.

## Provenance boundary

Evidence retains or references enough provenance to explain its origin, but Provenance remains the cross-cutting relationship/history concept.

Evidence SHOULD NOT copy:

- full source data;
- full candidate output;
- full model/Learned State payloads;
- complete Execution logs;
- every upstream concept state.

Stable references plus interpretation context are preferred.

## Reproducibility semantics

Evidence must preserve enough producing context that a later actor can state whether the finding can be:

- reproduced exactly;
- reproduced statistically;
- recomputed approximately within a bound;
- compared only qualitatively;
- not meaningfully reproduced because critical context is unavailable.

002-G will define the cross-cutting reproducibility contract; Evidence owns only the finding-specific facts needed for interpretation/recomputation.

## Scale semantics

Evidence is durable control-plane/result state, not an automatic copy of per-record evaluation output.

For enterprise-scale evaluations, Evidence may preserve:

- aggregate counts;
- bounds;
- estimates;
- confidence intervals;
- representative diagnostic examples where policy permits;
- references to separately retained violation/diagnostic datasets;
- stable references to distributed detailed results.

The concept MUST NOT require collecting all evaluated rows or all violations to the driver in order to establish Evidence.

Where detailed row-level diagnostics are retained, their storage/identity is a representation concern and they do not become canonical Evidence state merely by volume.

## External decision handoff

Evidence may inform an external actor/system making:

- release approval;
- use restriction;
- model-training acceptance;
- governance review;
- remediation requirement;
- privacy/risk decision.

Evidence MUST remain an observation, not the authorization itself.

The same Evidence may legitimately lead to different decisions under different external policies.

## Actions

### Record / establish

Create durable Evidence only from a semantically valid Evaluation result.

### Inspect

Review question, finding, scope, method, claim strength, uncertainty, limitations, and provenance.

### Compare

Compare Evidence when Criteria/context are sufficiently aligned, preserving methodological differences.

### Supersede / mark stale / inapplicable

Change current-use applicability without rewriting the original finding.

### Invalidate

Record that a material defect undermines reliance while preserving historical provenance.

### Expose / hand off

Provide Evidence to Generation completion logic or external decision authorities without transferring Evidence ownership or silently creating approval state.

## Invariants

1. Evidence MUST remain interpretable after producing Execution/Evaluation compute is gone.
2. Evidence MUST NOT be treated as approval, privacy guarantee, or release authorization.
3. Evidence answers the exact Criterion revision it references; later Criterion revisions MUST NOT reinterpret it.
4. Evidence claim strength MUST NOT exceed the producing Evaluation's method/scope/coverage/uncertainty support.
5. Sampling and approximation limitations MUST remain visible.
6. Indeterminate/inconclusive Evidence MUST NOT be converted to favorable satisfaction automatically.
7. Negative/unfavorable findings from a valid Evaluation remain valid Evidence.
8. Constraint-satisfaction Evidence MUST NOT become Constraint authority or global satisfaction state.
9. Condition-fulfillment Evidence MUST NOT convert Condition into reusable Constraint authority.
10. Evidence used for Generation completion MUST identify the exact candidate output and committed requirement it supports.
11. Supersession/staleness/invalidation changes future reliance, not historical fact.
12. Conflicting Evidence MUST remain inspectable unless an explicit external/criterion rule defines combination semantics.
13. Privacy/disclosure-risk Evidence MUST remain threat-model/method scoped.
14. Evidence SHOULD NOT scale linearly with evaluated row count by default.
15. Evidence MUST NOT require full-corpus/output driver collection for ordinary enterprise-scale use.
16. No Evidence rule may introduce a permanent single-table assumption.

## Operational principle

A distributed Evaluation checks a 200-million-row candidate output against a universal non-negative-quantity Constraint and records zero violations over the full logical output. Evidence preserves that exhaustive scope, the exact candidate output and Constraint revisions, the method, and any relevant limitations. Generation can consume that Evidence as a completion-sufficient basis for the required rule.

A separate sample-based fidelity Evaluation estimates distribution similarity with a 95% confidence interval. Its Evidence preserves the sample design and uncertainty and supports only that statistical claim. A reviewer months later can distinguish the two findings without rerunning either Evaluation and without confusing either with release approval.

## Synchronization

Primary accepted synchronization rules:

- [SYNC-09 — Evaluation Criterion binding](../synchronizations/core-synchronizations.md#sync-09--evaluation-criterion-binding)
- [SYNC-10 — Evaluation method compatibility](../synchronizations/core-synchronizations.md#sync-10--evaluation-method-compatibility)
- [SYNC-11 — Evaluation operational realization](../synchronizations/core-synchronizations.md#sync-11--evaluation-operational-realization)
- [SYNC-12 — Evaluation produces Evidence](../synchronizations/core-synchronizations.md#sync-12--evaluation-produces-evidence)
- [SYNC-13 — Evidence external handoff](../synchronizations/core-synchronizations.md#sync-13--evidence-external-handoff)
- [SYNC-14 — Provenance recording](../synchronizations/core-synchronizations.md#sync-14--provenance-recording-at-material-transitions)
- [SYNC-15 — Reproducibility-relevant commitment snapshot](../synchronizations/core-synchronizations.md#sync-15--reproducibility-relevant-commitment-snapshot)

## Representation questions intentionally deferred

Phase 002-E does not decide:

- Evidence database/schema;
- report format;
- violation dataset representation;
- metric/result class hierarchy;
- dashboard visualization;
- statistical package choices;
- external decision/approval workflow integration;
- public API names.

Those representations must preserve durable, scoped, non-overstated Evidence semantics.