---
type: Phase Record
title: 003-F — Execution Monitoring, Failure, Recovery & Cancellation Experience
status: complete
---

# 003-F — Execution Monitoring, Failure, Recovery & Cancellation Experience

## Objective

Translate the accepted Execution/Attempt/retry/resume/checkpoint/failure/cancellation/unknown-state semantics into a coherent actor-visible and programmatic operational experience shared by Learning, Generation, and Evaluation.

003-F focuses on resilient operation without allowing scheduler/platform state or operator convenience to redefine committed domain semantics.

## Governing authority

- [Execution](../../concepts/execution.md)
- [002-F — Execution, Attempt History, Failure & Recovery Semantics](../002/002-F-execution-attempt-failure-recovery-semantics.md)
- [003-C — Learning & Learned State Lifecycle Experience](003-C-learning-learned-state-lifecycle-experience.md)
- [003-D — Generation Request, Condition, Validation & Output Promotion Experience](003-D-generation-request-condition-validation-output-promotion-experience.md)
- [003-E — Evaluation, Evidence & Review Experience](003-E-evaluation-evidence-review-experience.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md)
- [Reproducibility Contract](../../authority/reproducibility-contract.md)

## Canonical experience authority created

- [Execution Monitoring, Failure, Recovery & Cancellation](../../experience/execution-monitoring-failure-recovery-cancellation.md)

## Main decisions

### 1. Monitoring centers one logical Execution, not one platform job

Actors see the stable SYNGAN Execution identity and parent Learning/Generation/Evaluation first, with platform jobs/runs as drill-down references.

One Execution may span many Attempts, scheduler submissions, clusters, Spark jobs, or distributed worker groups.

### 2. Parent semantic state stays visible

Operational status is always interpretable alongside domain status.

The experience supports states such as:

```text
Execution: completed
Generation: awaiting required validation
Completed output: not promoted
```

and does not map platform success to domain success automatically.

### 3. Attempt history is durable and ordered

Failed, recoverable, cancelled, superseded/abandoned, and unknown Attempts remain inspectable after later Attempts occur.

The current scheduler run does not replace operational history.

### 4. Progress must be meaningful rather than fabricated

Execution may expose stage, partition, row, iteration, checkpoint, worker, timing, or other Strategy/method/platform signals where useful, but cannot imply a universal semantic percentage.

`100% tasks complete` does not by itself establish Learning, Generation, or Evaluation completion.

### 5. Failure is presented by operational effect

The experience distinguishes:

- recoverable Attempt failure;
- terminal Execution failure;
- cancellation-related termination;
- unknown/indeterminate outcome;
- semantic domain failure after operational success.

Operational root cause and domain consequence are shown separately where possible.

### 6. Retry is a semantic claim

A retry is offered as continuation of the same Execution only when the same committed domain semantics are preserved.

Changing material source identity, Data Meaning, Strategy/configuration, Constraints, Generation Conditions, Learned State, Evaluation Criterion/method, or dependency/network policy is not an operational retry.

### 7. Scheduler resubmission capability does not imply retry safety

Retry qualification is contextual and may be:

- safe from start;
- safe via validated resume;
- reconciliation required first;
- incompatible with committed semantics;
- indeterminate.

### 8. Resume requires validated recovery state

Checkpoint existence is insufficient.

The experience exposes producing Attempt, parent Execution/activity, integrity/scope, committed-context compatibility, dependency/runtime requirements, and explicit resume eligibility.

### 9. Recovery material stays non-final

Checkpoint, partial learned parameters, candidate partitions, partial Evaluation results, and other retained state remain non-authoritative until the owning domain concept establishes its result.

### 10. Duplicate physical work is permitted; duplicate semantic results are not

Retries may recompute partitions, model steps, or validation work.

The experience distinguishes transient/candidate/canonical/external/unknown side effects and warns when retry could create ambiguous authoritative or irreversible effects.

### 11. Unknown operational state is first-class

When actual outcome cannot be established safely, the experience shows `unknown/indeterminate` and blocks unsafe optimistic retry or success classification.

### 12. Reconciliation is an Execution action, not a concept

Reconciliation answers only what is necessary to determine safe continuation or terminal classification: whether prior work is active, checkpoints/output committed, external effects occurred, canonical promotion happened, or retries can be fenced safely.

### 13. Cancellation request and terminal cancellation are distinct

A cancellation request may resolve as cancelled, completed before stop, failed during cancellation, or unknown pending reconciliation.

The parent domain concept determines semantic terminal outcome.

### 14. Cancellation does not erase retained material or history

Partial/checkpoint/diagnostic state may remain after cancellation but is clearly non-final and subject to later retention policy.

### 15. Operator intervention has a hard semantic boundary

Operators may repair infrastructure, replace workers, retry/resume qualified Attempts, reconcile state, inspect telemetry, and cancel work.

They may not silently change committed domain semantics. If recovery requires such changes, a new domain activity/commitment is required.

### 16. Cross-domain recovery remains typed

Learning recovery material is not Learned State; Generation recovery material is not completed output; Evaluation recovery material is not Evidence.

The monitoring experience uses domain-specific context rather than generic `output` language where ambiguity would matter.

### 17. Platform observability is referenced, not copied wholesale

SYNGAN canonical monitoring stores/displays bounded Attempt and material operational summaries while detailed Spark/Databricks/Kubernetes/PyTorch/cloud telemetry remains platform-native and linkable.

### 18. Historical Execution inspection supports future provenance/reproducibility

Actors can inspect the Attempt timeline, material recovery/cancellation decisions, runtime/dependency changes, reconciliation outcomes, final operational outcome, and parent semantic outcome without treating every task event as canonical state.

## Operational example

```text
Generation G42
Semantic state: fulfilling

Execution EX9
State: recovery pending

Attempt A1
- failed, recoverable
- 72M / 100M rows candidate-materialized
- recovery manifest R1

Attempt A2
- outcome unknown
- coordinator lost during candidate write

Reconciliation
- A2 confirmed terminated
- no canonical promotion occurred
- candidate scope reconciled
- retry safe from R1

Attempt A3
- running
- same committed Generation semantics

Completed output
- none until Generation later satisfies promotion requirements
```

This is an experience example, not a required UI or persistence schema.

## Actor experience conclusions

### Data Practitioner

Needs parent semantic status, operational progress, recoverable/terminal distinctions, safe next actions, and clear non-final candidate/checkpoint status.

### Platform Operator

Needs detailed Attempt/resource/platform/recovery information and authority to repair operational realization without authority to mutate committed domain semantics.

### Data Owner / Steward

Needs enough incident/recovery history to understand whether source/rule/semantic bindings stayed intact.

### Privacy / Risk / Governance Reviewer

Needs visibility into material dependency/network incidents, unknown external side effects, recovery choices, and provenance without operational logs becoming the sole evidence source.

## Enterprise-scale conclusions

Operational experience remains bounded/control-plane oriented even when platform telemetry contains millions of task/log/metric events.

SYNGAN may summarize logical Attempts, material failures, recovery state, side effects, and selected platform references without ingesting or collecting all telemetry into one driver/UI process.

## No new concept result

003-F does not require standalone concepts for:

- Run;
- Job;
- Attempt;
- Checkpoint;
- Retry;
- Resume;
- Recovery;
- Cancellation;
- Reconciliation;
- Incident;
- Workflow;
- Progress;
- Health.

These remain Execution-owned subordinate history/actions, experience views, platform concepts, or rejected umbrella terms.

## Deferred to later Phase 003 groups

### 003-G

Deepen historical Execution/Attempt provenance traversal, materially relevant retry/recovery facts, reproducibility assessment, and historical comparison.

### 003-H

Deepen sensitive operational telemetry, external dependency trust, access boundaries, offline/no-egress enforcement visibility, and enterprise safety experience.

## Representation questions intentionally deferred

003-F does not select:

- scheduler/orchestrator;
- retry/backoff values;
- checkpoint/manifest format;
- fencing/transaction/lease technology;
- log/metric backend;
- platform adapter shape;
- cancellation API;
- incident integration;
- exact error taxonomy;
- operator authorization model;
- automated remediation engine;
- retention/cleanup policy.

## Exit criteria

- [x] logical Execution versus platform-job orientation defined;
- [x] parent semantic versus operational status kept visible;
- [x] durable Attempt history experience defined;
- [x] meaningful progress without universal fake percentage defined;
- [x] recoverable/terminal/unknown/semantic-failure distinctions defined;
- [x] retry preserves committed semantics;
- [x] retry safety is contextual rather than scheduler-derived;
- [x] resume/checkpoint qualification defined;
- [x] recovery material remains non-final;
- [x] duplicate physical work versus single semantic promotion preserved;
- [x] unknown state and reconciliation experience defined;
- [x] cancellation request/race/terminal outcome distinctions defined;
- [x] operator semantic-authority boundary defined;
- [x] Learning/Generation/Evaluation recovery remains typed;
- [x] platform telemetry remains drill-down rather than shadow canonical state;
- [x] programmatic/human semantic parity preserved;
- [x] enterprise-scale monitoring avoids mandatory telemetry collection to driver;
- [x] no representation architecture selected prematurely.

## Exit assessment

**Status: complete.**

SYNGAN now has a canonical operational experience that supports resilient monitoring, retry, resume, reconciliation, and cancellation across long-running distributed work while preserving one logical Execution, explicit uncertainty, single semantic promotion, and the semantic authority of Learning, Generation, and Evaluation.

## Next phase

**003-G — Provenance, Reproducibility & Historical Inspection Experience**
