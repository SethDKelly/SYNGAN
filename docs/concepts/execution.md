---
type: Concept
title: Execution
status: accepted
---

# Execution

## Purpose

Give operationally significant work a durable logical identity and lifecycle independent of any one platform job, process, task graph, physical retry, or scheduler representation.

Execution exists because long-running distributed Learning, Generation, and Evaluation can fail, retry, resume, cancel, lose worker processes, reuse checkpoints, or span several platform jobs while still realizing one committed domain activity. Those operational facts must remain inspectable without allowing platform state to redefine semantic success.

## Concept boundary

Execution is **operational realization authority**.

It owns how committed domain work is attempted operationally and what happened during that realization.

It does not own:

- Learning, Generation, or Evaluation semantic commitment;
- whether valid Learned State was established;
- whether candidate synthetic output qualifies as completed Generation output;
- whether an Evaluation method was methodologically valid or produced legitimate Evidence;
- Data Meaning, Constraint, Strategy, or Criterion authority;
- a generic scheduler/workflow/orchestration engine;
- one Spark job, Databricks run, Kubernetes job, process, thread, stage, or task;
- a generic artifact/checkpoint concept;
- retry policy as a universal platform policy;
- application-level release/use decisions.

A platform job/run may realize part or all of an Attempt, and one Attempt may itself involve several physical jobs or processes.

## Execution identity

An Execution has one stable logical identity associated with one committed domain activity occurrence under the current model.

The logical identity survives:

- worker/process replacement;
- platform job retries;
- one or more failed Attempts;
- checkpoint-based resume;
- scheduler resubmission;
- physical cluster changes that remain compatible with the committed activity semantics.

Changing the committed Learning, Generation, or Evaluation semantics is not an Execution retry. It requires a new distinguishable domain activity and therefore a new operational realization.

The current model expects one primary Execution for a domain activity that requires operational realization. An activity that is satisfied without operational work need not fabricate an Execution.

## Execution lifecycle

Execution must preserve states equivalent to the following where operationally relevant:

- **prepared** — operational realization has been defined but not yet started;
- **queued/pending** — accepted for execution but not yet actively running;
- **running** — an Attempt is actively realizing work;
- **recovery pending** — no Attempt is currently making progress and recovery/retry may legitimately continue the same Execution;
- **cancellation requested** — cancellation intent has been issued but terminal outcome is not yet resolved;
- **completed** — operational realization reached its committed operational endpoint without unresolved operational defect;
- **failed** — no valid retry/resume path remains under the current Execution contract;
- **cancelled** — cancellation was accepted and operational work terminated before operational completion;
- **indeterminate/unknown** — the platform cannot currently establish the actual operational terminal state strongly enough to classify it safely.

A representation may use different labels but MUST preserve distinctions where they affect recovery, audit, domain synchronization, or actor understanding.

`Execution.completed` is an operational fact only. It MUST NOT automatically establish semantic completion of the associated domain activity.

## Attempt semantics

An **Attempt** is subordinate Execution history representing one distinguishable operational try to realize or continue the same logical Execution.

Attempt is not an accepted standalone concept.

An Attempt conceptually preserves enough information to identify:

- Attempt identity and ordinal/history position;
- parent Execution identity;
- start/end timing where known;
- recovery/checkpoint basis where used;
- material runtime/resource/dependency context;
- physical platform-job/run references where useful;
- operational outcome;
- failure/cancellation/unknown-state facts;
- output/checkpoint/intermediate references needed for recovery or diagnosis.

One Attempt may map to:

- one platform job;
- many Spark jobs/stages/tasks;
- several Kubernetes/Databricks/PyTorch runtime objects;
- a distributed worker set;
- or another physical realization.

Platform identity is evidence about an Attempt, not the Attempt definition.

### Attempt outcome

Attempt outcomes must preserve distinctions equivalent to:

- **operationally succeeded** — the Attempt reached the operational endpoint assigned to it;
- **failed, retryable/recoverable** — the Attempt failed but same Execution can continue safely;
- **failed, non-recoverable for current Execution** — the Attempt exposes a terminal operational defect;
- **cancelled** — the Attempt stopped because cancellation was accepted;
- **superseded/abandoned for recovery** — the Attempt is no longer authoritative for progress because a later valid Attempt took over;
- **indeterminate/unknown** — actual Attempt outcome cannot yet be established safely.

Attempt success does not establish domain success.

## Retry semantics

Retry means another Attempt continues the **same logical Execution** under the **same committed domain semantics**.

Retry MUST NOT silently change any material bound domain state such as:

- source identity;
- Data Meaning revision;
- Strategy/configuration;
- applicable Constraints/handling;
- Learning sampling/approximation semantics;
- Generation Conditions, quantity, or scope;
- Learned State/direct-generation basis;
- Evaluation Criterion, subject/reference, method, coverage, or uncertainty semantics;
- deployment/network/no-egress profile;
- required base/pretrained artifact identity;
- materially behavior-changing randomness/reproducibility policy.

Operational parameters may change when they do not alter domain meaning, for example replacing a failed worker, changing executor count within allowed semantics, or selecting another compatible cluster.

If a proposed recovery change materially changes the committed domain behavior, it is not a retry. The domain concept must decide whether a new activity is required.

## Resume semantics

Resume is a retry that intentionally reuses valid prior operational state rather than restarting all work.

Resume is valid only when the recovery basis can be shown sufficiently compatible with:

- the same Execution;
- the same committed domain activity;
- required Strategy/method/runtime semantics;
- the checkpoint/intermediate's integrity and completion scope;
- any dependency/software/base-artifact requirements that affect correctness.

Unverified recovery state MUST NOT be treated as valid merely because files or checkpoint markers exist.

A resume may legitimately recompute previously performed work. SYNGAN does not require exactly-once physical computation.

## Checkpoint and recovery-state boundary

A checkpoint or recovery artifact is persisted operational state intended to permit continuation, diagnosis, or bounded recomputation.

Checkpoint state does not become:

- Learned State merely because parameters are durable;
- completed Generation output merely because generated partitions exist;
- Evidence merely because evaluation summaries exist;
- proof that an Attempt or Execution completed successfully.

Recovery material must remain associated with enough Execution/Attempt/domain context to prevent cross-use under incompatible semantics.

A checkpoint from one committed activity MUST NOT silently seed a materially different activity unless the relevant domain concept explicitly defines that derivation.

## Idempotency and duplicate-effect semantics

Distributed systems may execute physical work more than once. The conceptual requirement is therefore **single semantic promotion**, not exactly-once physical execution.

Retry/recovery mechanisms MUST prevent repeated physical work from accidentally creating multiple authoritative domain results for the same committed activity.

Under the current model:

- one successful Learning establishes zero or one primary Learned State;
- one successful Generation establishes zero or one completed logical output result;
- one Evaluation may establish its legitimate Evidence set once under its committed semantic result, even if operational work was retried.

This does not prohibit physically duplicated intermediate files, repeated partition computation, redundant validation, or multiple Attempt-specific diagnostics.

Later architecture must provide enough fencing, identity, promotion, manifest, transaction, compare-and-set, or equivalent semantics to prevent ambiguous duplicate canonical results. No specific mechanism is selected here.

An operation is **retry-safe** only when repeated/recovered operational realization cannot silently change the committed domain meaning or produce ambiguous authoritative side effects.

## Partial operational success

Distributed Attempts may partially succeed.

Examples include:

- some partitions generated while others fail;
- some learning shards/checkpoints persisted before a worker failure;
- part of an exhaustive Evaluation completed;
- a remote dependency call succeeded for some units before outage;
- a cancellation reached some workers before others.

Partial operational success is not a terminal semantic result by itself.

Execution records enough status to support recovery/diagnosis while the domain activity determines whether remaining work, validation, or cleanup is required.

Partial outputs/checkpoints may be reused only when the later representation and domain contract can establish that reuse is safe.

## Failure semantics

Execution owns **operational failure facts**, not every semantic reason a domain activity may fail.

Operational failure categories may include, where material:

- infrastructure/platform failure;
- resource/capacity exhaustion;
- worker/process loss;
- dependency/service unavailability;
- credential/access failure;
- forbidden network/dependency requirement detected during realization;
- implementation/runtime defect;
- checkpoint/recovery corruption or incompatibility;
- storage/output write failure;
- timeout/lease/coordination loss;
- explicit cancellation;
- unknown/lost operational state.

The exact future error taxonomy is representation design.

A domain activity may fail semantically even when Execution completes operationally. Examples include:

- Learning produced no valid reusable state;
- Generation output violated mandatory requirements;
- Evaluation assumptions became invalid;
- Evidence claim strength was insufficient.

Conversely, one Attempt may fail operationally without causing terminal domain failure if retry/recovery remains valid.

## Retryability and terminal failure

Retryability is contextual.

A failure is retryable only when another Attempt can continue the same Execution without violating committed semantics and without creating ambiguous authoritative effects.

Retryability may depend on:

- availability/integrity of recovery state;
- whether prior side effects can be safely recognized or fenced;
- whether the required source/output/reference identity still resolves equivalently;
- dependency availability;
- permitted resource/runtime substitutions;
- randomness/reproducibility contract;
- domain deadline/cancellation state;
- whether the failure exposed a deterministic defect that retry cannot fix.

Repeated retry MUST NOT be assumed safe simply because the platform can resubmit a job.

When no valid continuation exists, Execution becomes terminally failed and reports that fact to the associated domain activity.

## Cancellation semantics

Cancellation is a request/intent first and a terminal result only after the operational outcome is resolved.

Conceptually:

```text
cancellation requested
        |
        +--> cancelled
        +--> completed before cancellation took effect
        +--> failed while cancelling
        +--> indeterminate until platform state is reconciled
```

Cancellation MUST NOT erase prior Attempts, committed domain state, or already established domain results.

### Race with semantic completion

Execution cannot decide whether a domain activity was semantically complete merely by observing cancellation timing.

For example:

- Generation may have operationally completed production but still await required validation;
- Evaluation may finish computation but not yet establish valid Evidence;
- Learning may have durable checkpoint material without valid Learned State.

The domain concept resolves its own terminal state using Execution facts plus its semantic contract.

### Cancellation propagation

When Learning, Generation, or Evaluation requests cancellation, Execution should attempt to stop further operational work and prevent unauthorized promotion of later Attempt side effects.

The exact scheduler/API cancellation mechanics are deferred.

## Unknown and lost-state semantics

Distributed systems can lose authoritative knowledge of whether a physical job or side effect completed.

Execution MUST be able to preserve an **indeterminate/unknown** operational state rather than falsely choosing success or failure.

Recovery from unknown state requires reconciliation sufficient to answer questions such as:

- is a prior Attempt still running?;
- did candidate output already materialize?;
- did a checkpoint commit fully?;
- did a remote operation happen?;
- would retry duplicate an externally visible side effect?;

Until ambiguity is resolved or safely fenced, Execution MUST NOT promote uncertainty to operational success.

## Platform mapping boundary

Execution and Attempt are intentionally platform-neutral.

A later adapter may map them to Spark, Databricks, Kubernetes, Ray, PyTorch distributed, cloud batch, or another system.

The mapping may be:

```text
1 Execution -> many Attempts
1 Attempt   -> many platform jobs/stages/tasks
```

or a simpler one-to-one mapping where appropriate.

The platform's native retry/run identity MUST NOT overwrite SYNGAN logical history.

Changing platform implementation does not change Execution semantics if the same operational contract is preserved.

## Progress and health semantics

Execution may expose progress/health sufficient for operators and domain activities to understand operational state.

Progress may be exact, estimated, stage-based, partition-based, iteration-based, or Strategy/method-defined.

Progress is not domain completion percentage unless the domain concept explicitly defines that mapping.

Examples:

- `100% partitions written` may still leave Generation awaiting validation;
- `training epoch complete` may not mean Learning has valid Learned State;
- `all validation tasks finished` may not mean Evaluation assumptions held.

Health/progress observations should not require driver-local collection of all per-task telemetry.

## Resource and dependency context

Execution preserves/references runtime facts material to operational diagnosis, recovery, reproducibility, or policy review, such as:

- execution environment/cluster identity where useful;
- software/runtime versions;
- resource class/accelerator availability;
- relevant dependency/service identity;
- network/deployment policy facts;
- worker/partition topology where behaviorally material;
- physical job/run references;
- material timing/duration/cost observations where later design retains them.

Execution does not become a full observability platform or generic billing system.

## Scale semantics

Execution is control-plane operational state.

Its canonical history should scale with logical Attempts, material transitions, summaries, checkpoint references, and operational facts—not with every Spark task, record, tensor, generated row, or log line by default.

Detailed platform telemetry can remain in platform-native systems and be referenced when needed.

SYNGAN MUST NOT require collecting all executor/task telemetry to the driver in order to maintain Execution identity or terminal state.

Long-running enterprise work may last hours or days and survive cluster/process turnover while retaining the same logical Execution identity.

## Actions

### Prepare / submit

Associate operational realization with a committed domain activity and prepare it for scheduling.

### Start Attempt

Create a distinguishable Attempt before or as operational work begins.

### Observe

Inspect logical Execution state, active/history Attempts, progress, health, failure, recovery, and cancellation status.

### Request cancellation

Record cancellation intent and initiate platform-specific cancellation without assuming immediate terminal outcome.

### Retry

Create a new Attempt under the same committed semantics after establishing retry safety.

### Resume

Create a new Attempt using validated compatible checkpoint/recovery state.

### Reconcile

Resolve indeterminate prior Attempt/side-effect state sufficiently to permit safe continuation or terminal classification.

### Complete operationally

Mark Execution operationally complete only when no unresolved operational work/defect remains under its operational contract.

### Fail terminally

Mark Execution failed when no valid same-semantics retry/recovery path remains.

### Cancel terminally

Mark Execution cancelled when cancellation is accepted and operational work is stopped sufficiently for terminal classification.

## Invariants

1. Execution operational completion MUST NOT automatically establish semantic completion of Learning, Generation, or Evaluation.
2. Attempt is subordinate Execution history and MUST NOT be equated with a platform job/run by definition.
3. Failed/cancelled/unknown Attempts MUST remain historically distinguishable when later Attempts occur.
4. Retry/resume MUST preserve the committed domain semantics of the associated activity.
5. A material domain-semantic change MUST NOT be disguised as an Execution retry.
6. Checkpoint/intermediate durability MUST NOT imply Learned State, completed Generation output, or Evidence.
7. Recovery material MUST be validated against the same Execution/domain context before reuse.
8. Exactly-once physical computation is not required; duplicate physical work MUST NOT create ambiguous duplicate authoritative domain results.
9. Unknown operational state MUST remain explicit until safely reconciled/fenced.
10. Retryability MUST be established contextually rather than inferred from platform resubmission capability.
11. Cancellation request and terminal cancellation are distinct states.
12. Cancellation MUST NOT erase committed history or previously established domain results.
13. Partial operational success MUST remain distinguishable from terminal operational or semantic success.
14. Platform job/run identity MUST remain a mapping/reference rather than SYNGAN Execution authority.
15. Execution MUST remain operational lifecycle state rather than a generic workflow/orchestration engine.
16. Canonical Execution state SHOULD NOT grow with every task/log/record by default.
17. Ordinary enterprise Execution MUST NOT require full worker/task telemetry collection to the driver.
18. Execution MUST preserve enough Attempt/failure/recovery history for provenance and reproducibility without becoming a shadow copy of platform logs.

## Operational principle

A committed Generation begins one logical Execution. Attempt A starts distributed output production but loses workers after several partitions are written and a recovery manifest/checkpoint is persisted. Execution records A as failed but recoverable rather than failing the Generation automatically.

Before retry, recovery logic verifies that the checkpoint belongs to the same committed Generation, Strategy, Learned State, Conditions, Constraints, output scope, and dependency context. Attempt B resumes, recomputing some partitions where necessary. Duplicate physical work is tolerated, but fencing/promotion semantics ensure only one logical candidate output can later become the completed Generation result.

The platform reports Attempt B complete. Execution becomes operationally completed. Generation still remains awaiting required validation until its mandatory Constraint Evidence is sufficient; only Generation can promote the candidate output.

## Synchronization

Primary accepted synchronization rules:

- [SYNC-04 — Learning operational realization](../synchronizations/core-synchronizations.md#sync-04--learning-operational-realization)
- [SYNC-07 — Generation operational realization](../synchronizations/core-synchronizations.md#sync-07--generation-operational-realization)
- [SYNC-11 — Evaluation operational realization](../synchronizations/core-synchronizations.md#sync-11--evaluation-operational-realization)
- [SYNC-14 — Provenance recording](../synchronizations/core-synchronizations.md#sync-14--provenance-recording-at-material-transitions)
- [SYNC-15 — Reproducibility-relevant commitment snapshot](../synchronizations/core-synchronizations.md#sync-15--reproducibility-relevant-commitment-snapshot)

## Representation questions intentionally deferred

Phase 002-F does not decide:

- Spark/Databricks/Kubernetes job mapping;
- scheduler/orchestration technology;
- state-machine storage;
- retry count/backoff defaults;
- checkpoint file/manifest format;
- transaction/fencing mechanism;
- idempotency-key representation;
- distributed lock/lease mechanism;
- progress metric implementation;
- log/telemetry backend;
- exact error-code taxonomy;
- public cancellation/retry/resume API names.

Those implementations must preserve this operational contract rather than redefine it.