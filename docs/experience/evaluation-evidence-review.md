---
type: Experience Specification
title: Evaluation, Evidence & Review Experience
status: active
---

# Evaluation, Evidence & Review Experience

## Purpose

Define how human and programmatic actors formulate evaluative questions, choose and review examination methods, commit and observe [Evaluation](../concepts/evaluation.md), interpret [Evidence](../concepts/evidence.md), compare multiple findings, and review synthetic-data fitness without collapsing [Evaluation Criterion](../concepts/evaluation-criterion.md), Evaluation, Evidence, or external decision authority into a generic `Quality`, `Validation`, `Scorecard`, or `Approval` concept.

## Primary experience principle

> **An actor should always be able to tell what question was asked, what method examined it, what subject/reference/scope were bound, what Evidence was actually established, how strong that Evidence is, what remains uncertain or limited, and which downstream decision—if any—remains outside SYNGAN's evidentiary authority.**

The experience MUST preserve:

```text
Criterion -> question
Evaluation -> examination
Evidence -> durable finding
External policy/actor -> decision
```

## Entry modes

Actors may enter evaluation/review from:

- a candidate Generation awaiting required completion validation;
- a completed synthetic output needing fidelity, utility, validity, disclosure-risk, or comparison review;
- a Learned State needing state-level Evaluation;
- an existing Criterion that should be reused against a new subject;
- an existing Evidence record requiring interpretation, comparison, staleness review, or historical inspection;
- a source/reference/baseline comparison question;
- an investigation triggered by surprising or conflicting Evidence.

The experience MUST NOT require every Evaluation to be attached to Generation completion.

## Criterion-first experience

### Start from the question, not the metric

The actor should be able to define or select the evaluative question before choosing the method.

A Criterion review should expose, where material:

- question/property being assessed;
- subject type and logical scope;
- reference/baseline/threat-model context;
- answer-strength requirement;
- tolerance or interpretation semantics;
- uncertainty/confidence expectations;
- authority/source;
- lifecycle/revision status;
- whether the Criterion is intended for Generation completion, diagnostic review, comparative analysis, or another use.

The experience MUST NOT present a list of available metrics as if those metrics define what should matter.

### Criterion families remain distinct

Review surfaces may group Criteria for orientation, but should preserve distinct dimensions such as:

- fidelity;
- utility;
- validity;
- privacy/disclosure risk;
- reproducibility/stability;
- other explicit actor-defined questions.

A review MUST NOT imply that high performance in one dimension compensates automatically for weakness in another.

### Reuse and revision

A reusable Criterion may be selected across multiple Evaluations where the question remains semantically equivalent.

If the material question, scope, reference, tolerance, threat model, or answer-strength semantics change, the experience should show a new Criterion revision rather than silently reinterpret historical Evidence.

## Method selection experience

### Method compatibility is question-specific

After the Criterion is known, actors should be able to inspect one or more candidate Evaluation methods and understand whether each can answer the Criterion at the required strength.

Method review may expose:

- property measured;
- method/version/configuration;
- required subject/reference inputs;
- coverage model;
- sampling design;
- approximation/bounding semantics;
- uncertainty/confidence semantics;
- scale/resource characteristics;
- rare-event/tail limitations;
- network/dependency requirements;
- reproducibility characteristics;
- known assumptions/limitations.

A method that can execute is not automatically compatible.

### Coverage/claim-strength preview

Before commitment, the experience should distinguish method outcomes equivalent to:

- exhaustive/complete-scope;
- deterministic bounded/certificate-backed;
- statistical/sampled;
- approximate/sketch-based;
- diagnostic/partial.

The selected method's attainable claim strength should be compared with the Criterion's required answer strength.

For example:

```text
Criterion: every quantity >= 0
Required answer: universal
Method: 50K-row sample
Compatibility: insufficient for universal completion claim
```

versus:

```text
Criterion: category A proportion is 40% ± 2%
Required answer: statistical determination at stated uncertainty
Method: stratified estimator with sufficiently tight interval
Compatibility: potentially sufficient
```

Scale pressure MUST NOT be presented as permission to silently weaken the Criterion.

### Multiple candidate methods

The experience MAY compare methods without inventing a universal `best metric` score.

Relevant comparison dimensions can include:

- claim strength;
- computational cost;
- coverage;
- uncertainty;
- interpretability;
- scale behavior;
- dependency/network posture;
- diagnostic richness;
- reproducibility.

## Pre-commit Evaluation review

Before semantic commitment, actors should be able to review the material facts that will define the examination historically:

- exact Criterion revision(s);
- exact subject identity;
- reference/baseline identity;
- relevant Data Meaning/Constraint/Condition context;
- method/version/configuration;
- logical scope/population/cohort;
- coverage/sampling/approximation semantics;
- uncertainty/confidence semantics;
- dependency/network/no-egress posture;
- randomness/reproducibility intent;
- expected Evidence forms;
- known limitations.

A material change after commitment requires a new distinguishable Evaluation rather than an edited retry.

## Evaluation lifecycle orientation

The experience should preserve states equivalent to:

```text
draft / proposed
      ↓
validated / ready
      ↓
committed
      ↓
evaluating
      ↓
┌─────────────────────┐
│                     │
completed /           failed / cancelled
completed with limits
      ↓
zero or more durable Evidence findings
```

A completed Evaluation may produce unfavorable or indeterminate Evidence.

### Semantic versus operational state

The experience MUST preserve distinctions such as:

```text
Evaluation: evaluating
Execution: running
Latest Attempt: active
```

```text
Evaluation: validating method/result semantics
Execution: completed
Evidence: not established yet
```

```text
Evaluation: completed
Evidence: Constraint violated
```

Execution success is not Evaluation success, and Evaluation success is not subject success.

## Progress experience

Evaluation progress should be method-meaningful rather than universally normalized.

Useful signals MAY include:

- logical scope processed where meaningful;
- partitions/cohorts completed;
- sampling acquisition status;
- reference preparation status;
- method stages;
- uncertainty/estimation stage;
- current Attempt;
- elapsed/resource information;
- outstanding semantic checks before Evidence establishment.

The experience MUST NOT imply `80% evaluated` has universal meaning when the method cannot support such interpretation.

## Evidence establishment experience

### Evidence is more than a score

Once Evaluation completes semantically, each independently interpretable Evidence record should make available, progressively:

- Evidence identity;
- Criterion revision;
- evaluated subject;
- reference/baseline;
- observed finding/result;
- method/configuration;
- logical scope/population;
- coverage basis;
- sampling/approximation semantics;
- uncertainty/error/confidence information;
- assumptions/limitations;
- claim-strength/applicability boundary;
- provenance/reproducibility references;
- current applicability status.

A bare `score = 0.93` or `pass = true` is not an adequate Evidence experience.

### Favorability is separate from validity

The experience should distinguish:

```text
Evaluation valid/completed
Evidence favorable
```

from:

```text
Evaluation valid/completed
Evidence unfavorable
```

and from:

```text
Evaluation failed
No valid Evidence established
```

For example, a valid exhaustive Evaluation that finds a Constraint violation is successful Evaluation producing negative Evidence.

### Indeterminate/inconclusive Evidence

When uncertainty, coverage, conflicting assumptions, or method limits prevent a decisive answer, Evidence should remain explicitly indeterminate/inconclusive.

The experience MUST NOT select the favorable side of an uncertain interval or turn `unknown` into `pass`.

## Evidence strength presentation

### Claim strength must be visible enough to prevent overstatement

Evidence review should communicate whether a finding is supported as:

- exhaustive/universal;
- deterministic bounded/certificate-backed;
- statistical;
- approximate;
- diagnostic/partial;
- indeterminate.

The presentation may use human-readable summaries, but the underlying semantics must remain inspectable.

### Scope matters as much as numeric result

Two Evidence records with the same numeric value may support different conclusions because their subject, population, reference, threat model, or coverage differ.

The experience should therefore make scope mismatch visible before comparison or aggregation.

## Generation-completion review

When Evidence participates in the 003-D Generation completion barrier, the review should make the exact handoff visible:

```text
Criterion
  ↓
Evaluation
  ↓
Evidence finding/strength
  ↓
Generation requirement-specific completion decision
```

Evidence itself does not mark Generation complete.

The actor should be able to inspect:

- which exact mandatory Condition/Constraint the Evidence answers;
- whether the Evidence applies to the exact candidate output;
- whether claim strength satisfies the committed requirement;
- whether the finding is satisfied/violated/indeterminate;
- why Generation can or cannot promote.

## General quality/fitness review

### No universal quality score by default

A review surface may summarize several Criteria/Evidence findings, but SHOULD preserve separate dimensions instead of collapsing them automatically.

For example:

```text
Fidelity
- distribution preservation: strong statistical Evidence
- rare-category fidelity: limited Evidence

Utility
- downstream task A: comparable to source baseline
- task B: not evaluated

Validity
- required Constraints: satisfied exhaustively

Disclosure risk
- membership inference: low observed risk under threat model T1
- attribute inference: not evaluated
```

The experience MUST NOT imply an overall `92/100 quality` unless an explicit actor-defined decision rule/policy defines how those dimensions are combined.

### Missing Evidence remains missing

`not evaluated` is not a negative score and not a positive score.

The experience should distinguish:

- favorable Evidence;
- unfavorable Evidence;
- indeterminate Evidence;
- no applicable Evidence;
- stale/superseded Evidence;
- Evidence not yet produced.

## Evidence comparison experience

### Comparability must be checked before visual comparison

Before two Evidence records are compared directly, actors should be able to understand differences in:

- Criterion revision;
- subject identity;
- reference/baseline;
- method/configuration;
- scope/population;
- sampling design;
- uncertainty;
- time/source version;
- threat model;
- Data Meaning context.

The experience MAY provide side-by-side comparison but MUST NOT silently treat incomparable findings as equivalent observations.

### Conflicting Evidence remains visible

Different legitimate methods may disagree.

For example:

```text
Criterion: downstream utility for task X
Evidence E1: comparable to source baseline
Evidence E2: moderately degraded
```

The review should show the methodological/contextual reasons available for the disagreement rather than average the findings automatically.

An explicit Criterion or external decision policy may later define combination semantics; the Evidence layer itself does not.

## Evidence lifecycle and current applicability

Historical Evidence remains immutable in what it observed, while current reliance may change.

The review experience should distinguish states equivalent to:

- applicable/current;
- superseded;
- stale/obsolete;
- inapplicable;
- invalidated.

Opening old Evidence should show both:

- what it established historically; and
- whether it is still appropriate for the actor's current question.

A newer Criterion, regenerated output, changed downstream task, new threat model, or discovered methodological defect may alter current applicability without rewriting history.

## Privacy/disclosure-risk review

Privacy-oriented review must preserve the exact threat model and method scope.

Actors should be able to see, where material:

- evaluated subject: output or Learned State;
- threat model;
- attacker assumptions/knowledge;
- attack/test method;
- finding;
- uncertainty;
- limitations;
- threats not examined;
- whether a formal privacy mechanism/guarantee exists separately.

The experience MUST NOT translate:

```text
low observed membership-inference risk
```

into:

```text
anonymous / private / safe to release
```

without separate authority supporting that claim.

## Review versus decision boundary

Evidence may be reviewed by a practitioner, steward, consumer, or governance actor and may inform external decisions such as release, remediation, use restriction, or acceptance.

The experience MUST preserve:

```text
Evidence says what was observed.
Decision authority says what action is allowed.
```

A favorable Evidence package is not automatically approval, and an unfavorable finding may legitimately trigger different actions under different organizational policies.

003-E does not introduce a Release Decision or Approval concept.

## Actor-specific review

### Data Practitioner

Emphasize Criterion intent, method suitability, lifecycle, Evidence interpretation, uncertainty, comparison, and next diagnostic/evaluation action.

### Data Owner / Steward

Emphasize validity/semantic Criteria, exact source/Constraint/Data Meaning context, conflicting/stale Evidence, and historical traceability.

### Platform Operator

Emphasize Execution/resource/method realization while preserving whether Evidence has actually been established. Operational health does not decide favorability.

### Privacy / Risk / Governance Reviewer

Emphasize threat model, claim strength, limitations, dependency/egress posture, current applicability, provenance, and the explicit boundary between Evidence and approval.

### Synthetic Data Consumer

Emphasize Criteria/Evidence relevant to the intended use rather than requiring review of all available metrics. Missing fitness Evidence for the consumer's use should remain visible.

## Programmatic parity

A future SDK/CLI/notebook/API should allow programmatic users to inspect:

- Criterion question/revision/answer-strength semantics;
- selected Evaluation method and compatibility findings;
- Evaluation semantic state and associated Execution summary;
- coverage/sampling/approximation/uncertainty;
- Evidence identity/finding/claim strength/limitations;
- Evidence applicability lifecycle;
- comparability/conflict information;
- relationship to Generation completion where relevant;
- distinction between Evidence and external decisions.

Returning only metric scalars or booleans is insufficient.

## Enterprise-scale evaluation/review

The experience MUST remain practical when Evaluations operate over hundreds of millions of records.

Actors should be able to understand large-scale Evaluation through bounded control-plane state such as:

- subject/reference identities;
- distributed coverage summaries;
- aggregate counts;
- estimates/confidence intervals;
- bounded/sketch results;
- representative diagnostics where permitted;
- references to distributed detailed-result datasets;
- selected platform links.

The experience MUST NOT require full subject, all violations, or all telemetry to be collected into driver/UI memory merely to establish or review Evidence.

If scale permits only a weaker method, the Evidence remains weaker; the user experience may not silently strengthen the claim.

## Next-action guidance

Derived next actions may include:

```text
Criterion defined
  → compare/select compatible method
  → review and commit Evaluation

Evaluation completed with negative Evidence
  → inspect finding/diagnostics
  → remediate/regenerate/re-evaluate as appropriate

Evidence indeterminate
  → strengthen method / increase coverage / revise question only if actor intent truly changes

Conflicting Evidence
  → inspect method/context differences
  → define an explicit comparison/reconciliation Criterion if needed

Evidence stale/inapplicable
  → run new Evaluation against current subject/context
```

Guidance is derived from canonical state and does not create a generic Quality workflow authority.

## Experience invariants

1. Criterion, Evaluation, Evidence, and external decision authority MUST remain distinct.
2. Criterion selection SHOULD precede or explicitly govern method selection; available metrics MUST NOT silently define the question.
3. Fidelity, utility, validity, privacy/disclosure risk, and other Criteria MUST remain distinct dimensions unless an explicit decision rule combines them.
4. Method compatibility MUST be evaluated against the Criterion's required answer strength.
5. Scale pressure MUST NOT silently weaken Criterion semantics.
6. Sampling/approximation/coverage/uncertainty MUST remain visible where material.
7. Evaluation semantic state MUST remain distinct from Execution/Attempt state.
8. Evaluation success MUST remain distinct from favorable subject Evidence.
9. Unfavorable Evidence from a valid Evaluation MUST remain valid Evidence.
10. Indeterminate Evidence MUST NOT be converted into favorable satisfaction automatically.
11. Evidence MUST expose claim-strength/applicability boundaries sufficiently to prevent overstatement.
12. A bare metric scalar or boolean MUST NOT be the only Evidence interface.
13. Evidence used for Generation completion MUST identify the exact candidate output and exact committed requirement it supports.
14. Generation retains completion authority; Evidence does not promote output itself.
15. Missing Evidence MUST remain distinguishable from negative or favorable Evidence.
16. Conflicting Evidence MUST remain inspectable unless explicit combination/reconciliation semantics exist.
17. Historical Evidence and current applicability MUST remain distinguishable.
18. Privacy/disclosure-risk Evidence MUST remain threat-model/method scoped and MUST NOT imply release approval or universal privacy.
19. Programmatic and human-facing review surfaces MUST preserve equivalent semantic distinctions.
20. Ordinary enterprise review MUST NOT require full subject/violation/telemetry collection to driver-local memory.
21. No Evaluation experience rule may impose a permanent single-table assumption.
22. Experience convenience MUST NOT create a generic Quality, Metric, Validation, Scorecard, Review Result, or Approval god-concept.

## Representation questions intentionally deferred

003-E does not decide:

- built-in Criterion taxonomy/class hierarchy;
- metrics/plugin registry;
- statistical library choices;
- Evaluation builder/API shape;
- dashboard/report visualization;
- charting library;
- Evidence database/schema;
- automated aggregate quality score;
- conflict-resolution algorithm;
- privacy-attack implementation;
- external approval/release workflow;
- alert/notification implementation.

Later architecture must preserve the question, method, Evidence-strength, comparison, lifecycle, and decision-boundary semantics defined here.
