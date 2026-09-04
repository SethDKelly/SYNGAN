---
type: Phase Record
title: 002-E — Evaluation Criterion, Evaluation & Evidence Specification
status: complete
---

# 002-E — Evaluation Criterion, Evaluation & Evidence Specification

## Objective

Deepen the accepted [Evaluation Criterion](../../concepts/evaluation-criterion.md), [Evaluation](../../concepts/evaluation.md), and [Evidence](../../concepts/evidence.md) concepts into precise question, method, coverage, uncertainty, claim-strength, lifecycle, historical, Generation-completion, and enterprise-scale semantics.

The phase preserves the Phase 001 rule that evaluative questions, examinations, durable findings, and downstream decisions are distinct authorities.

## Governing authority

002-E is governed by:

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Terminology Policy](../../authority/terminology-policy.md)
- [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md)
- [Accepted Concepts](../../concepts/index.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Phase 001 Exit](../001/001-H-phase-001-consolidation-initial-concept-catalog.md)
- [002-A — Data Meaning & Constraint Specification](002-A-data-meaning-constraint-specification.md)
- [002-B — Synthesis Strategy Specification & Capability Semantics](002-B-synthesis-strategy-capability-semantics.md)
- [002-C — Learning & Learned State Specification](002-C-learning-learned-state-specification.md)
- [002-D — Generation Specification, Request/Condition Semantics & Output Completion](002-D-generation-request-condition-output-completion.md)

Canonical concept authority remains under `docs/concepts/`; this phase record preserves refinement history and handoff.

## Scope

002-E specifies:

- Evaluation Criterion question/scope/reference/answer-strength semantics;
- fidelity, utility, validity, and privacy/disclosure-risk separation;
- Criterion revision/history and Constraint/Condition-derived Criteria;
- Evaluation commitment and method compatibility;
- coverage models including exhaustive, bounded/certificate, statistical, approximate/sketch, and diagnostic/partial examination;
- sampling, approximation, uncertainty, representativeness, and rare-event limitations;
- distinction between Evaluation success and favorable subject outcome;
- Evidence finding, claim-strength, applicability, uncertainty, supersession, and invalidation semantics;
- Evidence use in Generation completion;
- privacy/disclosure-risk evidence scope and non-guarantee boundary;
- Learned State as a possible Evaluation subject;
- enterprise-scale evaluation without mandatory driver collection;
- refinements to SYNC-09 through SYNC-15 where relevant.

## Non-goals

002-E does not select:

- metric library or plugin architecture;
- built-in statistical algorithms;
- Spark implementation of distributed validators;
- Python class hierarchy or API shape;
- Evidence serialization/database schema;
- report/dashboard format;
- privacy attack implementations;
- external release/approval workflow;
- exact Execution retry/cancellation mechanics;
- cross-cutting reproducibility classification details.

## Canonical authority refined

002-E directly deepens:

1. [Evaluation Criterion](../../concepts/evaluation-criterion.md)
2. [Evaluation](../../concepts/evaluation.md)
3. [Evidence](../../concepts/evidence.md)
4. [Core Synchronizations](../../synchronizations/core-synchronizations.md)

No new standalone concept is introduced.

## Evaluation Criterion decisions

### 1. Criterion owns the question, not the metric

A Criterion states what property matters, for what subject/scope/reference context, and what strength of answer is meaningful.

Available metrics MUST NOT silently determine the question.

### 2. Criterion may define answer-sufficiency semantics

Where required, Criterion may state whether the answer needs to be universal/exhaustive, bounded, statistical, comparative, or diagnostic and may define tolerance/confidence/coverage requirements.

These semantics answer the Criterion; they do not become generic enterprise approval policy.

### 3. Quality remains plural

Fidelity, utility, validity, and privacy/disclosure risk remain separate dimensions.

A score in one dimension cannot imply another.

### 4. Constraint/Condition-derived Criteria preserve source authority

A Constraint may motivate a validity Criterion and a Generation Condition may motivate a fulfillment Criterion, but Criterion does not take ownership of the rule/request.

### 5. Universal requirements cannot be weakened for convenience

A universal required rule cannot become a sample-only question because exhaustive checking is expensive.

If the committed requirement itself permits statistical/bounded assurance, then corresponding evidence may be sufficient.

## Evaluation decisions

### 1. Evaluation owns the examination

Evaluation binds Criterion, subject/reference inputs, method/configuration, logical scope, coverage, sampling/approximation, uncertainty, and material dependency/reproducibility context at semantic commitment.

Material changes after commitment require a new distinguishable Evaluation.

### 2. Claim strength cannot exceed method strength

The central rule is:

> **The strength of Evidence produced by an Evaluation MUST NOT exceed what its method, scope, coverage, assumptions, and uncertainty can support.**

### 3. Coverage is explicit

002-E distinguishes conceptual coverage modes:

- exhaustive/complete-scope;
- deterministic bounded/certificate-backed;
- statistical/sampled;
- approximate/sketch-based;
- diagnostic/partial.

These are semantic distinctions, not a required API enum.

### 4. Sampling and approximation are allowed but not invisible

Sampling design, effective scope, uncertainty, approximation/error bounds, representativeness, rare-event/tail limitations, and material randomness must remain inspectable.

### 5. Evaluation success is not subject success

A valid check that proves a Constraint violation is a successful Evaluation producing negative Evidence.

A computational job that completes with invalid methodology, wrong scope/reference, or broken assumptions may be an Evaluation failure despite producing numbers.

### 6. Evaluation completion requires interpretability

Execution completion alone is insufficient. Evaluation must establish that the committed examination was validly realized and that Evidence can legitimately be produced at the represented claim strength.

## Evidence decisions

### 1. Evidence is a durable finding, not a metric value

Evidence preserves/references Criterion, producing Evaluation, subject/reference, finding, scope, method, coverage, uncertainty, limitations, claim-strength boundary, and provenance.

### 2. Evidence claim strength is first-class

Evidence may be exhaustive/universal, deterministic bounded/certificate, statistical, approximate/sketch, or diagnostic/partial.

A later reader must be able to understand what was established and what was not.

### 3. Indeterminate remains indeterminate

Where uncertainty prevents a definitive answer, Evidence remains inconclusive/indeterminate rather than selecting a favorable interpretation.

### 4. Negative Evidence is valuable Evidence

Constraint violations, failed Conditions, poor fidelity, weak utility, elevated disclosure risk, and similar unfavorable findings remain valid Evidence when produced by a valid Evaluation.

### 5. Evidence has historical applicability lifecycle

Evidence may become superseded, stale/obsolete, inapplicable, or invalidated for current reliance without rewriting what the original Evaluation observed.

### 6. Evidence disagreement remains inspectable

Conflicting Evidence is not automatically averaged or merged. Differences in Criterion, method, reference, scope, uncertainty, or threat model remain visible unless explicit combination semantics exist elsewhere.

## Generation completion integration

002-E completes the evidentiary side of 002-D's promotion barrier.

When candidate output requires validation before Generation completion:

1. Evaluation binds the exact candidate output;
2. Evaluation binds a Criterion that preserves the exact committed Condition/Constraint requirement;
3. the selected method must be strong enough for that requirement;
4. resulting Evidence must preserve coverage, uncertainty, and claim-strength limits;
5. negative Evidence blocks completion where satisfaction is mandatory;
6. indeterminate Evidence blocks completion where determination is mandatory;
7. Evidence does not itself transition Generation — Generation owns the completion decision.

### Example: universal Constraint

For `quantity >= 0 for every record`, a representative sample with zero observed violations is not ordinarily sufficient to claim universal satisfaction.

A distributed exhaustive check can establish the property across all relevant partitions without collecting all rows to the driver.

### Example: tolerance-based Condition

For a mandatory Condition requiring a category proportion within an explicit tolerance, statistical Evidence may be completion-sufficient when its uncertainty/error semantics are tight enough to determine whether the committed tolerance was met.

## Privacy/disclosure-risk boundary

Privacy-related Evaluation/Evidence remains threat-model and method scoped.

A favorable result under one attack model does not establish universal privacy, anonymization, or release safety.

Formal mechanism-specific privacy guarantees remain separate future concept/policy work when independent state/actions warrant it.

## Enterprise-scale conclusions

Evaluation must remain viable at Spark-scale without requiring full subject/output driver collection.

Legitimate scale techniques include:

- distributed exhaustive checks;
- partition-local validation plus global reduction;
- aggregates;
- deterministic certificates/bounds;
- sketches;
- statistically designed samples;
- task-specific distributed model evaluation.

Scale pressure does not authorize claim inflation or Criterion weakening.

Evidence likewise should preserve durable findings, summaries, bounds, estimates, references, and limited diagnostics rather than copying all per-row examination state into canonical Evidence.

## Synchronization refinements

### SYNC-09 — Evaluation Criterion binding

Now includes Criterion subject/scope/reference and answer-strength semantics, plus exact originating Constraint/Condition context where material.

### SYNC-10 — Evaluation method compatibility

Now explicitly requires method claim strength, coverage, sampling/approximation, uncertainty, and Generation-completion adequacy to match the Criterion.

### SYNC-11 — Evaluation operational realization

Now separates successful examination from favorable finding and requires retry invariance of committed Evaluation semantics.

### SYNC-12 — Evaluation produces Evidence

Now defines durable Evidence content, claim-strength limits, negative/indeterminate findings, and exact candidate-output binding for Generation completion.

### SYNC-13 — Evidence handoff

Now covers both Generation completion consumption and external governance/decision handoff while preserving Evidence as observation rather than authorization.

### SYNC-14 / SYNC-15

Evaluation/Evidence provenance and reproducibility facts now include Criterion, subject/reference, method/configuration, scope/coverage, sampling/approximation, uncertainty, dependency/runtime context, and Evidence applicability history where material.

## Refined invariant set

### Evaluation Criterion invariants

1. question remains distinct from metric/method/Evidence/decision;
2. exact Criterion revision is historically bound;
3. method availability cannot silently weaken the question;
4. answer-strength semantics may constrain valid methods;
5. universal requirements are not converted into samples for convenience;
6. quality dimensions remain distinct;
7. Constraint/Condition authority is not absorbed.

### Evaluation invariants

1. method and Criterion remain separately owned;
2. exact inputs/reference/scope are bound;
3. coverage/sampling/approximation/uncertainty remain visible;
4. claim strength does not exceed method support;
5. Execution completion is not Evaluation completion;
6. negative finding is not Evaluation failure;
7. inconclusive Evidence is not favorable satisfaction;
8. scale does not silently lower evidentiary strength;
9. ordinary enterprise evaluation does not require full driver collection.

### Evidence invariants

1. durable and interpretable after compute teardown;
2. claim strength is bounded by producing method;
3. sample/approximation limits remain visible;
4. indeterminate remains indeterminate;
5. negative findings remain Evidence;
6. exact Criterion and candidate/output context is retained;
7. Constraint/Condition authority is not absorbed;
8. Evidence is not approval or privacy guarantee;
9. supersession/staleness/invalidation does not rewrite historical fact;
10. canonical Evidence does not grow linearly with evaluated rows by default.

## Deferred questions handed forward

### To 002-F — Execution

- detailed Evaluation retry/resume/cancellation semantics;
- cancellation races between Evaluation and dependent Generation;
- progress and Attempt identity for long-running distributed validation;
- operational handling when validation partially succeeds across partitions.

### To 002-G — Provenance / Reproducibility

- exact stable identity requirements for evaluated subjects/references;
- exact reproduction classes for statistical/approximate Evidence;
- software/runtime/method version requirements;
- Evidence supersession/invalidation lineage;
- identity for separately retained violation/diagnostic datasets.

### To 002-H — Consolidation

- cross-check Generation completion against Criterion/Evaluation/Evidence invariants;
- verify no `Quality`, `Validation`, `Metric`, or `Decision` god-concept has re-emerged;
- verify synchronization and authority economy after all Phase 002 refinements.

## Exit criteria

002-E is complete when:

- [x] Criterion question/scope/reference semantics are explicit;
- [x] Criterion answer-strength semantics are explicit;
- [x] quality dimensions remain distinct;
- [x] Constraint/Condition-derived Criteria preserve authority boundaries;
- [x] Evaluation commitment/method compatibility is explicit;
- [x] coverage modes are distinguished;
- [x] sampling/approximation/uncertainty are first-class;
- [x] Evaluation success is separated from favorable subject outcome;
- [x] Evidence durable finding semantics are explicit;
- [x] Evidence claim-strength/applicability boundaries are explicit;
- [x] negative and indeterminate Evidence are preserved correctly;
- [x] Evidence lifecycle/supersession/invalidation is explicit;
- [x] Generation completion consumes only sufficiently strong Evidence;
- [x] universal requirements cannot be proven by inadequate sampling;
- [x] privacy/disclosure-risk Evidence remains scoped and non-authorizing;
- [x] Learned State can be an Evaluation subject where appropriate;
- [x] enterprise-scale evaluation avoids mandatory driver collection;
- [x] synchronization authority is refined without new concepts;
- [x] no representation architecture is selected prematurely.

## Exit assessment

**Status: complete.**

Evaluation Criterion, Evaluation, and Evidence are now sufficiently specified to support Generation's completion barrier without conflating metrics, computational completion, sampling, favorable results, privacy guarantees, or organizational authorization.

## Next phase

**002-F — Execution, Attempt History, Failure & Recovery Semantics**

002-F should now refine the operational lifecycle shared by Learning, Generation, and Evaluation: logical Execution identity, Attempt boundaries, retry/resume/checkpoint semantics, cancellation races, failure classification, partial operational success, idempotency/recovery expectations, and separation of platform job/run identity from SYNGAN semantic activities.