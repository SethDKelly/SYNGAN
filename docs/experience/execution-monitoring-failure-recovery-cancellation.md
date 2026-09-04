---
type: Experience Specification
title: Execution Monitoring, Failure, Recovery & Cancellation Experience
status: active
---

# Execution Monitoring, Failure, Recovery & Cancellation Experience

## Purpose

Define how human and programmatic actors observe, diagnose, retry, resume, reconcile, and cancel [Execution](../concepts/execution.md) while preserving the distinction between operational realization and the semantic authority of Learning, Generation, and Evaluation.

This experience does not introduce standalone `Run`, `Job`, `Attempt`, `Checkpoint`, `Retry`, `Recovery`, `Cancellation`, `Incident`, `Reconciliation`, or `Workflow` concepts.

## Primary experience principle

> **Actors should be able to understand what is happening operationally, what has already happened, what is safe to do next, and what remains uncertain without platform state being mistaken for domain completion or a recovery action silently changing committed semantics.**

The experience must preserve:

```text
Learning / Generation / Evaluation
        owns semantic intent and completion
                    ↕
                Execution
        owns operational realization
                    ↓
                Attempts
        own subordinate operational history
                    ↓
          platform jobs/tasks/processes
```

## Entry modes

Actors may enter the Execution experience from:

- an active Learning, Generation, or Evaluation;
- a queued/pending Execution;
- a failed Attempt with possible retry/resume;
- an Execution in recovery pending;
- a cancellation request awaiting resolution;
- an indeterminate/unknown Execution or Attempt requiring reconciliation;
- a completed Execution whose associated domain activity is still semantically incomplete;
- a historical Execution requiring incident/provenance/reproducibility inspection.

An activity that requires no operational realization need not fabricate an Execution view.

## Default operational orientation

A concise operational view should identify:

- parent domain activity identity and semantic state;
- logical Execution identity;
- Execution lifecycle state;
- active/latest Attempt;
- recoverable versus terminal failure state;
- current cancellation state;
- checkpoint/recovery availability;
- relevant progress/health summary;
- unresolved unknown-state/side-effect concerns;
- selected platform job/run references for drill-down;
- legitimate next actions.

For example:

```text
Generation G42
Semantic state: fulfilling

Execution EX9
Operational state: recovery pending
Latest Attempt: A2 — failed, recoverable
Candidate output: partial, non-final
Checkpoint/recovery basis: available
Retry safety: pending reconciliation
Completed output: none
```

A generic `job failed` message is insufficient when valid recovery may continue the same committed activity.

## Semantic versus operational status

The Execution experience MUST keep domain state visible enough to prevent operational status from being misinterpreted.

Examples:

```text
Execution: completed
Generation: awaiting required validation
Candidate output: physically complete
Completed output: not promoted
```

```text
Execution: completed
Learning: failed semantic completion
Learned State: not established
```

```text
Execution: completed
Evaluation: validating result semantics
Evidence: not established yet
```

Likewise, a failed Attempt does not automatically mean the parent domain activity failed while a same-semantics recovery path remains valid.

## Execution and Attempt history

### One logical Execution

The actor-facing model should present one stable logical Execution for one committed activity occurrence even when operational realization spans:

- several scheduler submissions;
- replacement clusters;
- many Spark jobs/stages/tasks;
- multiple Databricks runs;
- multiple distributed worker groups;
- checkpoint-based continuation.

Platform job identity is supporting operational detail, not the top-level SYNGAN identity.

### Attempts remain visible and ordered

Attempt history should make materially relevant transitions inspectable, for example:

```text
A1 — failed, recoverable
     worker loss after partial materialization

A2 — failed, outcome initially unknown
     coordinator lost after write request

A3 — running
     started only after A2 side-effect reconciliation
```

The experience should preserve failed, cancelled, superseded/abandoned, and unknown Attempts rather than replacing history with only the latest scheduler state.

## Progress and health experience

### Progress must be operationally meaningful

The experience MAY expose:

- Strategy/method-defined stages;
- processed partitions/shards/cohorts where meaningful;
- row/materialization counts when semantically interpretable;
- epochs/iterations where meaningful;
- checkpoint creation;
- worker/resource health;
- current Attempt duration;
- queue/wait time;
- dependency/service availability;
- output/reference/check coverage summaries;
- platform-native links for detailed telemetry.

It MUST NOT invent a universal Execution or domain percentage where none exists.

### Health is not semantic success

`healthy`, `all workers running`, `100% tasks complete`, or equivalent operational status does not establish:

- valid Learned State;
- completed Generation output;
- valid Evidence;
- fulfilled Conditions or Constraints.

The experience should keep these messages operationally scoped.

## Failure experience

### Failure should be classified by effect, not just exception text

Actors should be able to distinguish at least:

- recoverable Attempt failure;
- terminal Execution failure;
- cancellation-related termination;
- indeterminate/unknown outcome;
- domain-semantic failure after operational success.

Operational diagnostics may include categories such as:

- infrastructure/platform failure;
- worker/process loss;
- resource/capacity exhaustion;
- dependency/service unavailability;
- credential/access failure;
- storage/output failure;
- checkpoint/recovery corruption;
- runtime/implementation defect;
- timeout/coordination loss;
- forbidden network/dependency behavior;
- lost/unknown platform state.

The exact error taxonomy is deferred, but the actor must understand whether the failure can legitimately continue under the same committed semantics.

### Root cause versus consequence

The experience SHOULD distinguish causal operational facts from domain consequences.

For example:

```text
Operational cause:
worker group lost during partition production

Execution consequence:
Attempt A1 failed, recoverable

Generation consequence:
still fulfilling; partial candidate retained as non-final
```

This avoids presenting every operational exception as if it directly defined the domain outcome.

## Retry experience

### Retry means same committed semantics

A Retry action should only be offered as a same-Execution continuation when material domain bindings remain unchanged.

The experience should expose retry qualification against material facts such as:

- same parent activity identity;
- same source/input identity;
- same Data Meaning revision;
- same Strategy/configuration;
- same Constraints/handling;
- same Generation Conditions/quantity/scope where applicable;
- same Evaluation Criterion/method/coverage where applicable;
- compatible dependency/base-artifact identity;
- compatible network/no-egress profile;
- randomness/reproducibility continuity where material.

If an operator proposes a materially behavior-changing substitution, the experience must indicate that the change requires a new domain activity rather than presenting it as a retry option.

### Retry safety is contextual

The platform being able to resubmit work is not enough.

Retry safety should distinguish states equivalent to:

- safe to retry from start;
- safe to resume from validated recovery state;
- retry requires reconciliation first;
- retry incompatible with committed semantics;
- retry safety indeterminate.

A future UI may use different labels.

## Resume and checkpoint experience

### Recovery material is evidence for continuation, not authority

Checkpoint/recovery views should show:

- checkpoint/recovery identity;
- producing Attempt;
- parent Execution/activity identity;
- known completeness/scope;
- integrity/compatibility assessment;
- dependency/runtime requirements;
- whether resume is qualified;
- non-final status relative to Learned State, completed output, or Evidence.

For example:

```text
Checkpoint CP7
Produced by: Attempt A1
Parent: Learning L12 / Execution EX4
Integrity: verified
Committed-context compatibility: verified
Resume eligibility: yes
Learned State: no
```

File existence alone must never be rendered as resume eligibility.

### Resume may recompute work

The experience should not imply that safe resume means every previously completed physical unit is preserved exactly once.

Recomputation is acceptable when correctness and canonical-result semantics remain intact.

## Partial side effects and duplicate work

Distributed retries may leave:

- duplicate temporary partitions;
- repeated validation work;
- repeated model steps;
- multiple checkpoint candidates;
- partially written external/internal state.

The experience should classify side effects by their semantic risk where possible:

- transient/recomputable;
- candidate/staged but non-final;
- canonical promotion already established;
- externally visible/irreversible;
- unknown.

The governing rule is:

> **Duplicate physical work is tolerable; ambiguous duplicate authoritative semantic results are not.**

Actors should be warned before retry when prior externally visible or canonical side effects cannot yet be determined/fenced safely.

## Unknown and indeterminate operational state

### Unknown is a first-class state

When platform information is insufficient, the experience must say so explicitly.

Example:

```text
Attempt A2: outcome unknown
Last confirmed state: candidate write requested
Platform coordinator: unreachable
Candidate output commit: not yet reconciled
Retry: blocked pending reconciliation
```

The experience MUST NOT map unknown to `failed` merely to enable retry or to `succeeded` merely because output appears to exist.

### Reconciliation experience

Reconciliation should help answer only the operational questions necessary for safe continuation/terminal classification, such as:

- is the prior Attempt still active?;
- did a checkpoint commit fully?;
- did candidate output materialize and with what scope?;
- did an external operation occur?;
- did canonical promotion already happen?;
- would a retry duplicate an unsafe side effect?;
- can prior material be safely fenced/ignored/reused?

The result may establish:

- safe retry/resume;
- operational completion;
- terminal failure;
- cancellation outcome;
- continued indeterminacy.

Reconciliation is an Execution action/experience, not a new domain concept.

## Cancellation experience

### Cancellation request versus terminal outcome

The experience must preserve:

```text
cancellation requested
        ↓
┌──────────────┬───────────────┬────────────────────┬───────────────┐
│              │               │                    │
cancelled    completed      failed while          unknown /
             before stop     cancelling            reconciling
```

Issuing `cancel` must not immediately render the Execution or parent domain activity as cancelled.

### Cancellation race visibility

Actors should be able to see what was known when cancellation was requested and what later happened.

For example:

```text
Cancellation requested at 14:22
Attempt A3 acknowledged stop at 14:23
Candidate output: partial, non-final
Execution: cancelled
Generation: cancelled
```

or:

```text
Cancellation requested at 14:22
Attempt A3 had already completed operationally
Execution: completed
Generation: awaiting validation
```

The parent domain concept decides its semantic terminal state.

### Post-cancel retained material

Checkpoints, partial output, or diagnostics may remain after cancellation. The experience must label them non-final and subject to later retention/cleanup policy.

## Operator intervention boundary

Platform operators may legitimately:

- replace failed workers/resources;
- retry/resume qualified Attempts;
- reconcile unknown state;
- inspect platform telemetry;
- initiate cancellation;
- resolve infrastructure/dependency incidents;
- select compatible operational resources where policy allows.

They must not silently change:

- Data Meaning;
- Strategy synthesis semantics/configuration;
- applicable Constraints;
- Generation Conditions/quantity/scope;
- Learned State identity;
- Evaluation Criterion/method semantics;
- dependency/network policy;
- other material committed domain state.

If operational recovery requires one of those changes, the experience should hand the actor back to the owning domain workflow to create a new distinguishable commitment.

## Cross-domain recovery orientation

### Learning

Execution may show recoverable checkpoint/intermediate state, but only Learning can later establish Learned State.

### Generation

Execution may show partial/complete candidate material and recovery status, but only Generation can promote completed output.

### Evaluation

Execution may show partial coverage or completed physical checks, but only Evaluation can establish methodologically valid Evidence.

The monitoring experience should use domain-specific labels when helpful rather than flattening all three into generic `output` terminology.

## Platform drill-down

A logical Execution/Attempt should provide links/references to platform-native observability when available, such as Spark, Databricks, Kubernetes, PyTorch/distributed, or cloud-batch job detail.

The canonical SYNGAN experience should summarize only material operational facts and not copy every task/log/metric by default.

Platform identifiers must not replace Execution/Attempt identity.

## Historical execution inspection

Historical inspection should expose:

- parent committed activity;
- logical Execution identity;
- Attempt timeline;
- material failure/recovery/cancellation events;
- checkpoints/recovery basis used;
- relevant resource/runtime/dependency changes;
- unknown-state reconciliation outcomes;
- final operational outcome;
- parent semantic outcome;
- provenance/reproducibility references.

Historical inspection should explain physical history without implying that every physical event is canonical business/domain state.

003-G will deepen Provenance and reproducibility traversal.

## Programmatic parity

A future SDK/CLI/API should allow programmatic users to determine:

- logical Execution identity/state;
- parent activity identity/semantic state;
- current/latest Attempt and Attempt history;
- progress/health summaries with interpretation;
- recoverable versus terminal failure;
- retry/resume qualification and reasons;
- checkpoint/recovery identity and compatibility;
- unknown/indeterminate state and reconciliation requirement;
- cancellation requested versus resolved outcome;
- partial/candidate/canonical side-effect status where material;
- selected platform references;
- legitimate next actions.

A thrown exception, platform run ID, or scheduler state alone is not an adequate Execution lifecycle interface.

## Enterprise-scale monitoring

The monitoring experience must remain bounded when workloads contain hundreds of millions of rows and millions of platform task events.

Canonical orientation should rely on:

- logical Execution and Attempt records;
- bounded progress/health summaries;
- checkpoint/recovery references;
- selected failure incidents;
- material side-effect state;
- platform links;
- provenance references.

It MUST NOT require ingestion of all platform logs/tasks/metrics into SYNGAN or collection of that telemetry into driver/UI memory.

## Experience invariants

1. Execution operational status MUST remain distinct from Learning/Generation/Evaluation semantic status.
2. One logical Execution MUST remain stable across valid retries/resumes/platform resubmissions.
3. Attempt MUST remain subordinate history and not a platform-job synonym.
4. Failed, cancelled, superseded, and unknown Attempts MUST remain historically inspectable.
5. Progress/health presentation MUST NOT imply domain completion unless the domain contract explicitly establishes that relation.
6. Retry MUST preserve committed domain semantics; material semantic change requires a new domain activity.
7. Platform resubmission capability MUST NOT be presented as proof of retry safety.
8. Checkpoint existence MUST NOT imply resume compatibility or domain-result authority.
9. Recovery state MUST be validated against the same committed Execution/domain context before reuse.
10. Unknown operational state MUST remain explicit until reconciled or safely fenced.
11. Duplicate physical work MAY occur; it MUST NOT create ambiguous duplicate authoritative domain results.
12. Partial side effects MUST remain distinguishable from canonical promotion.
13. Cancellation request and terminal cancellation MUST remain distinct.
14. Cancellation races MUST preserve the actual operational and domain outcomes rather than rewriting history.
15. Operator intervention MUST NOT silently mutate committed Data Meaning, Strategy, Constraint, Condition, Learned State, Criterion, method, or dependency semantics.
16. Platform job/run identity MUST remain a reference rather than SYNGAN Execution authority.
17. Canonical monitoring MUST NOT become a shadow observability platform by copying all task/log telemetry.
18. Programmatic and human-facing surfaces MUST preserve equivalent recovery/cancellation/unknown-state distinctions.
19. Ordinary enterprise monitoring MUST NOT require full task/log/row collection to driver-local memory.
20. Experience convenience MUST NOT create generic Run, Job, Attempt, Checkpoint, Retry, Recovery, Cancellation, Reconciliation, Incident, or Workflow god-concepts.

## Representation questions intentionally deferred

003-F does not decide:

- scheduler/orchestrator technology;
- retry/backoff policy values;
- exact error-code taxonomy;
- checkpoint/manifest format;
- transactional/fencing/lease mechanism;
- platform adapter API;
- log/metrics backend;
- incident-management integration;
- cancel API implementation;
- UI timeline design;
- retention/cleanup mechanics;
- operator authorization model;
- automated remediation policy.

Later architecture must preserve the logical Execution, Attempt-history, retry-safety, unknown-state, single-semantic-promotion, cancellation, and bounded-observability semantics defined here.
