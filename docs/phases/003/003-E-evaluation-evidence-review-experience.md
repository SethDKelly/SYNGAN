---
type: Phase Record
title: 003-E — Evaluation, Evidence & Review Experience
status: complete
---

# 003-E — Evaluation, Evidence & Review Experience

## Objective

Translate the accepted Evaluation Criterion, Evaluation, Evidence, Generation-completion handoff, privacy/disclosure-risk, provenance/reproducibility, and scale semantics into a coherent actor-visible and programmatic evaluation/review experience.

003-E focuses on preserving question/method/finding/decision separation while making Evidence strength, uncertainty, comparison, staleness, conflict, and multidimensional fitness review understandable without creating generic Quality, Validation, Scorecard, Metric, Review Result, or Approval concepts.

## Governing authority

- [003-D — Generation Request, Condition, Validation & Output Promotion Experience](003-D-generation-request-condition-validation-output-promotion-experience.md)
- [Evaluation Criterion](../../concepts/evaluation-criterion.md)
- [Evaluation](../../concepts/evaluation.md)
- [Evidence](../../concepts/evidence.md)
- [Generation](../../concepts/generation.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Reproducibility Contract](../../authority/reproducibility-contract.md)
- [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md)

## Canonical experience authority created

- [Evaluation, Evidence & Review Experience](../../experience/evaluation-evidence-review.md)

## Main decisions

### 1. Evaluation experience begins with the question, not the metric

Actors define/select an Evaluation Criterion before or as the governing authority for method selection.

Available metrics/tests cannot silently decide what quality, validity, utility, or privacy means.

### 2. Criterion, Evaluation, Evidence, and external decision remain separate

The experience preserves:

```text
Criterion -> question
Evaluation -> examination
Evidence -> finding
External actor/policy -> decision
```

A favorable Evidence result is not approval, and an unfavorable finding does not mean Evaluation failed.

### 3. Evaluation dimensions remain independent

Fidelity, utility, validity, privacy/disclosure risk, reproducibility/stability, and later actor-defined dimensions can be grouped for navigation but are not collapsed into one universal Quality concept or score.

### 4. Method compatibility is claim-strength specific

Before commitment, the actor can understand whether a method is exhaustive, bounded/certificate-backed, statistical/sampled, approximate/sketch-based, or diagnostic/partial and whether that strength can answer the Criterion.

A method that can execute is not necessarily compatible.

### 5. Scale cannot weaken the question silently

If a universal Criterion requires universal Evidence, a cheap sample is not presented as equivalent merely because exhaustive validation is expensive.

A weaker feasible method produces weaker Evidence or leaves the Criterion unanswered.

### 6. Evaluation commitment freezes examination semantics

The exact Criterion revision, subject, reference/baseline, method/configuration, scope, coverage, sampling/approximation, uncertainty, dependency profile, and other material facts become historical at commitment.

Changing them materially creates a new Evaluation rather than an edited retry.

### 7. Evaluation and Execution states remain distinct

The experience supports:

```text
Execution: completed
Evaluation: validating method/result semantics
Evidence: not established
```

and:

```text
Evaluation: completed
Evidence: unfavorable
```

without flattening those into one success/failure state.

### 8. Progress is method-meaningful rather than universally percentage-based

Evaluation may expose processed scope, cohorts, sampling progress, method stages, Attempts, elapsed/resource state, or other meaningful progress, but cannot invent a universal percentage where the method does not justify one.

### 9. Evidence is richer than a scalar/boolean

Evidence review exposes enough context to understand the Criterion, subject/reference, finding, method, logical scope, coverage, sampling/approximation, uncertainty, assumptions, limitations, claim strength, provenance, reproducibility, and current applicability.

`score=0.93` or `pass=true` alone is insufficient.

### 10. Favorability, validity, and indeterminacy are separate

A successful Evaluation can produce favorable, unfavorable, or indeterminate Evidence.

A failed Evaluation is reserved for cases where a valid interpretable finding cannot be established under the committed method.

### 11. Generation-completion Evidence handoff is explicit

When Evidence is used for Generation completion, the actor can see which exact candidate output and mandatory Condition/Constraint the finding answers and whether claim strength is sufficient.

Generation retains completion/promotion authority.

### 12. General fitness review remains multidimensional

A review can summarize fidelity, utility, validity, disclosure risk, and other findings side by side while preserving gaps and limitations.

Missing Evidence remains missing; it is not implicitly favorable or unfavorable.

### 13. Evidence comparability is checked before comparison

Criterion revision, subject, reference, method, scope, sampling design, uncertainty, threat model, time/source version, and Data Meaning context can all affect whether findings are meaningfully comparable.

### 14. Conflicting Evidence remains visible

Different legitimate methods may disagree. SYNGAN does not automatically average those findings into one truth or score.

Explicit reconciliation/combination semantics require a Criterion or external decision policy.

### 15. Evidence historical fact and current applicability remain separate

Evidence can become superseded, stale, inapplicable, or invalidated for current use without rewriting what it historically observed.

### 16. Privacy/disclosure-risk review is threat-model scoped

A favorable result under one attack/threat model does not imply universal privacy, anonymity, or release safety.

The experience identifies what was and was not examined.

### 17. Review remains distinct from decision authority

Evidence may inform release/use/remediation/governance decisions, but the review experience does not make those decisions automatically or create approval authority.

### 18. Enterprise-scale review remains bounded/control-plane oriented

Large Evaluations may use distributed scans, estimates, sketches, aggregates, diagnostic datasets, and platform-native telemetry references without collecting the entire subject, all violations, or all operational logs into driver/UI memory.

## Review example

```text
Synthetic Output O42

Validity
- Constraint C1: satisfied / exhaustive Evidence E101
- Constraint C2: satisfied / deterministic construction guarantee E102

Fidelity
- marginal distributions: strong statistical Evidence E110
- rare category fidelity: limited / diagnostic only E111

Utility
- downstream task FraudModel-v3: comparable to source baseline E120
- downstream task ChurnModel-v2: not evaluated

Disclosure risk
- membership inference under T1: low observed risk E130
- attribute inference: not evaluated

Decision
- no SYNGAN release approval implied
```

This is an experience example, not a required UI/report schema.

## Actor experience conclusions

### Data Practitioner

Needs Criterion intent, method compatibility, Evaluation lifecycle, Evidence strength/uncertainty, comparison, and diagnostic next actions.

### Data Owner / Steward

Needs exact semantic/rule/reference context, historical revisions, conflicting/stale Evidence, and traceability.

### Platform Operator

Needs operational realization without acquiring authority over the evaluative question or subject favorability.

### Privacy / Risk / Governance Reviewer

Needs threat-model-scoped findings, limitations, provenance/reproducibility, dependency/egress posture, and explicit separation from release approval.

### Synthetic Data Consumer

Needs use-relevant Evidence and explicit gaps rather than every available metric or an opaque overall score.

## Enterprise-scale conclusions

Evaluation/review remains distributed-first and claim-strength preserving.

Actors can inspect bounded summaries, estimates, counts, intervals, Evidence records, diagnostic references, and selected platform links rather than loading complete evaluated data or detailed violations into one process.

## No new concept result

003-E does not require standalone concepts for:

- Quality;
- Metric;
- Validation;
- Review;
- Scorecard;
- Quality Score;
- Evidence Package;
- Review Result;
- Approval;
- Pass/Fail Decision;
- Reconciliation.

These remain experience compositions, method vocabulary, derived summaries, external authority, or rejected umbrella concepts.

## Deferred to later Phase 003 groups

### 003-F

Deepen Execution/Attempt monitoring, operational failures, retry/resume, cancellation races, and unknown-state reconciliation for Evaluation as well as Learning/Generation.

### 003-G

Deepen Provenance traversal, Evidence historical relationships, reproducibility assessment, and cross-run historical comparison.

### 003-H

Deepen enterprise access, sensitive Evidence/diagnostics, network/no-egress, dependency trust, and safety presentation.

## Representation questions intentionally deferred

003-E does not select:

- Criterion class hierarchy;
- metric/plugin registry;
- Evaluation SDK/builder shape;
- statistical package/library;
- dashboard/report design;
- Evidence persistence schema;
- aggregate-score formula;
- conflict-resolution algorithm;
- privacy attack implementation;
- approval/release workflow;
- alerting/notification platform.

## Exit criteria

- [x] Criterion-first question experience defined;
- [x] Criterion/Evaluation/Evidence/decision separation preserved;
- [x] fidelity/utility/validity/privacy dimensions remain distinct;
- [x] method compatibility and claim-strength preview defined;
- [x] scale does not weaken Criterion semantics silently;
- [x] Evaluation pre-commit review/commitment consequence defined;
- [x] Evaluation semantic state separated from Execution state;
- [x] method-meaningful progress established;
- [x] Evidence review goes beyond metric scalar/boolean;
- [x] favorable/unfavorable/indeterminate Evidence distinctions preserved;
- [x] Generation completion Evidence handoff defined without transferring authority;
- [x] missing Evidence remains explicit;
- [x] Evidence comparability review defined;
- [x] conflicting Evidence remains visible;
- [x] historical Evidence versus current applicability defined;
- [x] privacy/disclosure-risk review remains threat-model scoped;
- [x] Evidence remains distinct from approval/release decision;
- [x] programmatic/human semantic parity preserved;
- [x] enterprise-scale review avoids mandatory full driver collection;
- [x] no representation architecture selected prematurely.

## Exit assessment

**Status: complete.**

SYNGAN now has a canonical Evaluation/Evidence experience that starts from explicit questions, preserves method and claim-strength limits, makes uncertainty/conflict/current applicability inspectable, and supports multidimensional synthetic-data review without creating a generic Quality or Approval authority.

## Next phase

**003-F — Execution Monitoring, Failure, Recovery & Cancellation Experience**
