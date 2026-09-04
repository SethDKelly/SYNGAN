---
type: Phase Record
title: 002-F — Execution, Attempt History, Failure & Recovery Semantics
status: complete
---

# 002-F — Execution, Attempt History, Failure & Recovery Semantics

## Objective

Deepen the accepted [Execution](../../concepts/execution.md) concept into precise logical-execution, Attempt-history, retry, resume, checkpoint, idempotency, cancellation, failure, unknown-state, platform-mapping, and enterprise-scale semantics shared by Learning, Generation, and Evaluation.

The phase preserves the Phase 001 rule that Execution is operational realization authority rather than semantic authority for the domain activity it realizes.

## Governing authority

002-F is governed by:

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Terminology Policy](../../authority/terminology-policy.md)
- [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md)
- [Accepted Concepts](../../concepts/index.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Phase 001 Exit](../001/001-H-phase-001-consolidation-initial-concept-catalog.md)
- [002-C — Learning & Learned State Specification](002-C-learning-learned-state-specification.md)
- [002-D — Generation Specification, Request/Condition Semantics & Output Completion](002-D-generation-request-condition-output-completion.md)
- [002-E — Evaluation Criterion, Evaluation & Evidence Specification](002-E-evaluation-criterion-evaluation-evidence-specification.md)

Canonical concept authority remains under `docs/concepts/`; this phase record preserves refinement history and handoff.

## Scope

002-F specifies:

- stable logical Execution identity independent of physical platform jobs;
- Execution lifecycle and terminal/indeterminate operational states;
- Attempt as subordinate Execution history;
- Attempt outcome and retryability semantics;
- retry versus new domain activity;
- resume/checkpoint/recovery compatibility;
- partial operational success;
- single semantic promotion versus exactly-once physical execution;
- duplicate-effect and idempotency expectations;
- operational failure classification boundary;
- terminal failure versus recoverable Attempt failure;
- cancellation request, terminal cancellation, and cancellation races;
- unknown/lost operational state and reconciliation;
- mapping to Spark/Databricks/PyTorch/Kubernetes/etc. without platform identity takeover;
- progress/health/resource context boundaries;
- enterprise-scale operational history without task/log explosion;
- synchronization refinements to SYNC-04, SYNC-05, SYNC-07, SYNC-08, SYNC-11, SYNC-12, SYNC-14, and SYNC-15.

## Non-goals

002-F does not select:

- Spark/Databricks/Kubernetes job model;
- scheduler/orchestration technology;
- queueing system;
- retry/backoff values;
- checkpoint storage/serialization format;
- transactional/fencing technology;
- idempotency-key representation;
- distributed lock/lease mechanism;
- logging/telemetry backend;
- exact error-code taxonomy;
- cloud-provider failure model;
- public retry/cancel/resume API shape;
- cost-accounting implementation.

## Canonical authority refined

002-F directly deepens:

1. [Execution](../../concepts/execution.md)
2. [Core Synchronizations](../../synchronizations/core-synchronizations.md)

No new standalone `Attempt`, `Checkpoint`, `Retry`, `Run`, or `Workflow` concept is introduced.

## Execution specification decisions

### 1. Execution is logical operational identity

Execution represents the operational realization of one committed domain activity occurrence under the current model.

It can survive worker/process loss, physical job retries, cluster replacement, checkpoint resume, and multiple Attempts while preserving one logical operational history.

A material change to committed Learning, Generation, or Evaluation semantics is not an Execution retry.

### 2. Attempt remains subordinate history

Attempt is one distinguishable operational try within an Execution.

Attempt is not defined as one Spark job, Databricks run, Kubernetes job, process, or scheduler execution.

One Attempt may involve several such objects, and a simple runtime may map one Attempt one-to-one when appropriate.

### 3. Operational unknown state is first-class

Distributed platforms can lose certainty about whether work or side effects completed.

Execution therefore supports an indeterminate/unknown operational state rather than coercing uncertainty to success or failure.

Reconciliation/fencing is required before a retry can safely proceed when duplicate external/canonical side effects are possible.

### 4. Retry preserves semantic commitment

Retry creates another Attempt under the same logical Execution only when committed domain semantics remain unchanged.

Operational substitutions such as replacing a failed worker or changing executor count may be acceptable when they preserve behavior under the activity/reproducibility contract.

Changing Strategy configuration, Data Meaning, Constraints, Generation Conditions, Evaluation method/coverage, source identity, or other material semantic state requires a new domain activity rather than disguised retry.

### 5. Resume is validated recovery

Resume is a retry that intentionally reuses prior operational state.

A checkpoint cannot be reused merely because it exists. Recovery must establish sufficient identity, integrity, scope, compatibility, and committed-context continuity.

### 6. Checkpoint durability does not imply domain result

A durable checkpoint, partial model, generated partition set, evaluation summary, or recovery manifest is not automatically:

- Learned State;
- completed Generation output;
- Evidence;
- proof of domain completion.

Only the owning domain concept can promote valid semantic results.

### 7. Single semantic promotion replaces exactly-once physical execution

SYNGAN does not require exactly-once physical computation.

A distributed system may recompute partitions, repeat model steps, rerun validation, or execute tasks more than once.

The critical invariant is that repeated operational work must not create ambiguous duplicate **authoritative domain results**.

Later architecture must provide fencing/promotion/identity semantics sufficient to ensure:

- at most one primary Learned State per successful Learning;
- at most one completed logical output per successful Generation;
- coherent durable Evidence identity per semantic finding.

### 8. Partial operational success is not semantic success

An Attempt may complete some partitions/shards/checks before failure.

Execution preserves that operational history and may enable safe reuse, but the domain activity remains responsible for completeness and semantic validity.

### 9. Operational failure and semantic failure remain distinct

Execution owns operational facts such as infrastructure failure, capacity/resource exhaustion, worker loss, service dependency failure, checkpoint corruption, storage failure, runtime defect, cancellation, or lost state.

Domain concepts own semantic failure such as:

- invalid Learned State;
- mandatory Generation Condition/Constraint failure;
- invalid Evaluation methodology;
- insufficient Evidence strength.

### 10. Retryability is contextual

A platform's ability to resubmit a job does not establish retry safety.

A failure is retryable only when another Attempt can continue the same Execution without changing committed semantics and without creating ambiguous authoritative side effects.

### 11. Cancellation request is not terminal cancellation

Cancellation is first an intent/request.

The eventual outcome may be:

- cancelled;
- operationally completed before cancellation took effect;
- failed during cancellation;
- indeterminate until reconciled.

The domain activity determines its own terminal semantic state.

### 12. Platform identities remain references

Spark job IDs, Databricks run IDs, Kubernetes job IDs, cloud task IDs, or PyTorch worker groups may be preserved for diagnosis/provenance but do not become SYNGAN logical Execution/Attempt identity by definition.

## Domain synchronization conclusions

### Learning

A failed Attempt does not automatically fail Learning while valid retry remains possible.

Checkpoint/intermediate state cannot become Learned State without successful Learning completion.

Repeated physical Learning work must not establish ambiguous duplicate primary Learned States.

### Generation

Partial/candidate output may survive failed Attempts for recovery, but remains non-final.

Repeated partition generation is allowed when later fencing/promotion ensures one completed logical output.

Unknown Attempt/output state blocks safe promotion until reconciled.

### Evaluation

Partial validation work can be resumed/reused only when coverage/identity/assumptions remain valid.

Repeated partition checks must not accidentally double-count observations unless method semantics explicitly require it.

Operational completion does not establish method validity or Evidence.

## Cancellation race conclusions

002-F resolves the ownership of cancellation races without prescribing scheduler mechanics.

Execution records:

- cancellation request;
- physical cancellation realization;
- Attempt outcomes;
- operational terminal/unknown state.

Learning/Generation/Evaluation determine whether their semantic state is completed, failed, or cancelled based on those facts plus their own contracts.

A cancellation request cannot erase a semantically completed result.

## Idempotency conclusion

The design uses **retry-safe semantic effects** rather than promising universal physical idempotence.

A repeated Attempt may legally recompute work. What is prohibited is silently producing conflicting canonical results or applying non-repeatable external effects without reconciliation/fencing.

This creates a later architectural obligation to distinguish:

- repeatable internal computation;
- staged/candidate side effects;
- canonical promotion;
- external irreversible side effects;
- unknown prior side-effect state.

## Enterprise-scale conclusions

Execution canonical state remains control-plane state.

It should scale with:

- logical Executions;
- Attempts;
- material transitions;
- summarized failure/recovery facts;
- checkpoint references;
- selected runtime/provenance facts;

not every executor task, log line, row, tensor, or partition event by default.

Detailed telemetry remains in platform-native observability systems and can be referenced when needed.

Long-running work may survive hours/days and process/cluster turnover without losing logical Execution identity.

## Synchronization refinements

### SYNC-04

Now defines Learning Attempt/retry/resume/checkpoint/cancellation/unknown-state semantics and preserves Learning completion authority.

### SYNC-05

Now explicitly requires single semantic promotion of the primary Learned State despite repeated physical Attempts.

### SYNC-07

Now defines Generation partial-output recovery, duplicate partition/retry handling, cancellation/unknown state, and single completed-output promotion.

### SYNC-08

Now explicitly prevents retry/recovery from promoting multiple ambiguous completed outputs.

### SYNC-11

Now defines Evaluation partial coverage recovery, repeated-work counting safety, cancellation/unknown-state handling, and preservation of Evaluation methodological authority.

### SYNC-12

Now prevents repeated operational work from creating ambiguous duplicate authoritative Evidence for the same semantic finding.

### SYNC-14

Now defines the Execution/Attempt facts appropriate for provenance without copying complete platform telemetry/logs.

### SYNC-15

Now recognizes retry/resume/checkpoint/topology/failure timing as reproducibility-relevant only when those facts materially affect behavior or comparison claims.

## Refined invariant set

1. Execution completion is operational, not domain-semantic completion.
2. Attempt is subordinate history, not a platform-job synonym.
3. retries preserve domain commitment.
4. material semantic change is not retry.
5. checkpoints/intermediates are not domain results by durability alone.
6. retry/resume requires recovery compatibility/integrity.
7. unknown operational state remains explicit until reconciled/fenced.
8. exactly-once physical computation is not required.
9. duplicate physical work cannot create ambiguous duplicate authoritative domain results.
10. retryability is contextual rather than assumed from scheduler capability.
11. cancellation request and terminal cancellation are distinct.
12. cancellation does not erase committed history or completed results.
13. partial operational success remains distinct from terminal/domain success.
14. platform job/run identity remains a reference.
15. Execution remains operational rather than generic workflow authority.
16. canonical operational history does not expand to every task/log by default.
17. ordinary enterprise Execution does not require full telemetry collection to driver-local memory.

## Deferred questions handed forward

### To 002-G — Provenance / Reproducibility

- exact minimum Attempt history needed for material provenance;
- source/output/model/checkpoint identity requirements;
- reproducibility classifications when retry/resume changes physical execution;
- whether/how nondeterministic Attempt ordering or recovery affects statistical reproducibility;
- treatment of platform/software/runtime migration;
- stable identity for external side effects and recovered candidate material.

### To 002-H — Consolidation

- verify no Execution semantics have absorbed domain completion;
- verify Attempt/Checkpoint/Retry remain subordinate rather than new concepts;
- verify single semantic promotion aligns Learning/Generation/Evidence cardinalities;
- verify synchronization economy after the full Phase 002 refinement.

## Exit criteria

002-F is complete when:

- [x] stable logical Execution identity is specified;
- [x] Execution lifecycle includes explicit unknown/indeterminate state;
- [x] Attempt boundary/history/outcome semantics are explicit;
- [x] platform job/run identity remains separate;
- [x] retry preserves committed semantics;
- [x] resume/checkpoint compatibility is explicit;
- [x] checkpoint durability is separated from domain result authority;
- [x] partial operational success is explicit;
- [x] operational and semantic failures are separated;
- [x] retryability is contextual;
- [x] single semantic promotion replaces exactly-once computation assumptions;
- [x] duplicate physical work is allowed only with unambiguous canonical effects;
- [x] cancellation request/races/terminal outcomes are explicit;
- [x] unknown side-effect/platform state requires reconciliation/fencing;
- [x] enterprise-scale operational history avoids task/log explosion;
- [x] synchronizations are refined without creating new concepts;
- [x] no representation architecture is selected prematurely.

## Exit assessment

**Status: complete.**

Execution is now sufficiently specified to support resilient enterprise-scale Learning, Generation, and Evaluation without conflating retryable physical work with semantic identity or completion.

## Next phase

**002-G — Provenance, Reproducibility Contract & Historical Binding Specification**

002-G should define which stable identities and historical facts must survive across Data Meaning, Strategy, Learning, Learned State, Generation, Evaluation, Evidence, Execution/Attempts, dependencies, and outputs; distinguish exact/statistical/approximate/comparative reproducibility; and ensure traceability is sufficient without turning Provenance into a shadow database or storing complete platform telemetry.