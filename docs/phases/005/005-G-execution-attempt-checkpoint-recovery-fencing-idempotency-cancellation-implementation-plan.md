---
type: Phase Record
title: 005-G — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan
status: complete
---

# 005-G — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan

## Objective

Translate the accepted 004-F operational architecture plus the 005-D/005-E/005-F control/data/runtime seams into a concrete **future implementation plan** for stable Execution/Attempt identity, Attempt epochs, writer fencing, launch intent/correlation, checkpoints, resume/restart/reconciliation, idempotency, unknown state, cancellation and operational completion.

**No production implementation is authorized or performed by this phase.** Phase 005 remains planning-only.

## Entry authority

005-G is downstream of:

- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](../../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md);
- [005-B Verification Strategy](../../implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [005-D Public Resource/Control-Plane Plan](../../implementation/public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md);
- [005-E Spark Data Boundary Plan](../../implementation/spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md);
- [005-F Runtime/SPI/Learned-State Plan](../../implementation/strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md).

## Canonical authority created

005-G establishes:

[Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan](../../implementation/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-plan.md).

## Planning-only clarification

005-G creates no Execution/Attempt classes, SQL tables, migrations, scheduler adapter, checkpoint store, fencing backend, tests, CI workflow, or runtime infrastructure.

All resource roles, ports, persistence responsibilities and G1-G10 steps are future implementation contracts only.

## Core operational decisions

Accepted future rules include:

- one committed Learning/Generation/Evaluation occurrence has at most one primary logical Execution under the current architecture;
- one Execution may have many durable Attempts;
- each write-capable Attempt receives a positive monotonic `AttemptEpoch` scoped to its Execution;
- `AttemptEpoch` is distinct from `StateVersion`, semantic/schema versions, candidate generations and provider retry/job numbers;
- Attempt observed/runtime state is separate from current framework mutation authority;
- leases/heartbeats are liveness evidence only and cannot replace fencing;
- the preferred scale-safe fencing model uses Attempt-isolated physical namespaces and validates authority at registration/adoption/seal/completion boundaries rather than per row/file;
- shared mutable targets require actual provider fencing/version/CAS guarantees or are incompatible with overlapping recovery;
- platform launch uses durable intent plus provider correlation/reconciliation; lost acknowledgement yields unknown rather than assumed failure;
- operation idempotency is scoped to exact command/effect targets and request fingerprints;
- committed checkpoints are immutable recovery snapshots and do not become Learned State/output/Evidence;
- checkpoint existence does not imply resume eligibility;
- recovery explicitly distinguishes restart, resume, reconcile-first and cannot-continue-same-Execution;
- immutable prior effects may be adopted only after current-authority verification; late fenced mutable effects are not automatically authoritative;
- Evaluation partial retries require logical work-unit deduplication or clean restart;
- unknown/indeterminate external state remains durable and may block automatic retry;
- cancellation is a durable linearized intent that invalidates old writer/promotion authority even if provider termination is delayed or fails;
- operational completion remains separate from semantic completion;
- platform/native scheduler identity, retries, leases and success signals remain subordinate observations;
- no concrete scheduler, lock/lease service, checkpoint provider or launcher is selected in 005-G.

## Future resource roles

005-G reserves future resource/reference roles equivalent to:

```text
execution
execution_attempt
runtime_invocation
checkpoint
```

and accepts future public/internal values equivalent to:

```text
ExecutionHandle
ExecutionView
AttemptRef
AttemptEpoch
AttemptView
RuntimeInvocationRef
WriterFence
CheckpointRef
ResumeAssessment
RecoveryDecision
CancellationResult
```

Attempt/checkpoint/runtime invocation remain subordinate operational/representation state rather than new domain concepts.

## State/authority plan

Future `ExecutionState` preserves distinctions equivalent to:

```text
prepared
pending
running
recovery_pending
cancellation_requested
completed_operationally
failed
cancelled
indeterminate
```

Attempt observations remain a separate dimension equivalent to:

```text
prepared
submission_pending
submitted
running
succeeded
failed
cancelled
unknown
```

while mutation authority is tracked separately as current/fenced/read-only-equivalent.

This allows an old Attempt to remain physically `running` while already fenced from canonical writes.

## Writer-fence plan

Execution current authority retains the current Attempt/epoch plus a monotonic cancellation-generation barrier.

A future `WriterFence` carries:

```text
ExecutionRef
AttemptRef
AttemptEpoch
cancellation_generation
```

and must be validated at material framework-owned mutation boundaries.

The fence is an operational authority discriminator, not a secret. 005-I later provides actual authorization/capability security.

## Launch/reconciliation plan

A narrow future launcher port can submit, query/reconcile and request provider cancellation using one exact Attempt invocation.

Before external submission, SYNGAN persists a bounded `LaunchIntent`/outbox-backed operation identity and correlation information.

If the provider accepted a launch but the acknowledgement is lost, reconciliation must search/query by the durable correlation before repeating the effect.

If an external effect cannot be queried, fenced or deduplicated safely, automatic retry may remain blocked while Execution is indeterminate.

## Idempotency plan

Future operation idempotency uses exact operation family + target refs + request fingerprint + key.

Rules include:

```text
same key + same request -> same logical effect/result
same key + different request -> conflict
stale WriterFence -> rejected even if key previously succeeded
```

No universal one-key-per-Execution scheme is accepted.

## Checkpoint plan

A committed `CheckpointRef` identifies one immutable recovery snapshot tied to exact:

- Execution/producing Attempt/epoch;
- runtime invocation;
- domain commitment snapshot;
- checkpoint/state codec;
- exact material source/input/state identities;
- dependency/base-artifact identities;
- represented progress and RNG continuity where material;
- component/manifest root and integrity basis.

Incomplete staged checkpoint bytes are not resumable merely because they exist.

A checkpoint head may aid discovery but cannot establish resume eligibility by itself.

## Resume/recovery plan

Future `ResumeAssessment` preserves:

```text
eligible
eligible_with_limitations
restart_required
incompatible
indeterminate
```

and checks same-Execution semantic continuity, implementation/codec/runtime compatibility, exact data/state/dependency identities, integrity, represented progress, randomness continuity and later current security conditions.

Future `RecoveryMode` preserves:

```text
restart
resume
reconcile_first
cannot_continue_same_execution
```

A bounded immutable `RecoveryDecision` records the chosen continuation basis and prior effects that were retained, fenced, ignored, quarantined or adopted.

## Safe reuse plan

To avoid throwing away very large distributed work unnecessarily, current authority may explicitly adopt immutable prior effects after proving exact same commitment, identity/integrity, work-unit/membership safety and absence of stale mutable contamination.

A fenced Attempt finishing late does not gain authority by itself.

Mutable or weakly identified post-fence effects remain ineligible for automatic adoption.

## Evaluation retry protection

Evaluation recovery that reprocesses the same logical shard/work unit must deduplicate that contribution before aggregation unless duplicate observations are explicitly part of the committed method.

If the method/runtime cannot provide safe contribution identity, it must restart from clean aggregate state instead of risking double-counted Evidence inputs.

## Cancellation/completion plan

Accepting cancellation under Execution CAS:

1. transitions Execution to `cancellation_requested`;
2. increments cancellation generation;
3. invalidates old WriterFence/promotion authority;
4. records provider-cancel intent;
5. reconciles the actual physical outcome later.

Cancellation and authoritative completion race through durable control-plane preconditions:

- completion wins first -> later cancel reports already completed/not cancellable;
- cancellation wins first -> late provider success remains an observation and cannot regain canonical write/promotion authority.

Provider kill acknowledgement is not semantic/domain cancellation.

## Operational completion plan

Only the current authorized Attempt may establish one immutable operational-completion basis for Execution.

`completed_operationally` means runtime realization finished authoritatively; Learning/Generation/Evaluation still own their semantic completion barriers.

A fenced Attempt may physically succeed without making Execution complete.

Semantic validation failure may leave Execution correctly `completed_operationally` while the owning domain activity fails or follows its own allowed same-commitment continuation path.

## Persistence impact plan

Future bounded control responsibilities include equivalents of:

```text
execution
execution_state
execution_attempt
runtime_invocation
attempt_platform_correlation
launch_intent
checkpoint
execution_checkpoint_head
recovery_decision
cancellation_intent
operational_completion
operation_idempotency
```

They reuse 005-D ResourceRef/StateVersion/SchemaVersion/CAS/transaction/outbox/tombstone conventions.

No migration is created during Phase 005.

## Verification mapping

005-G primarily owns future V7 and directly maps:

```text
AF-04 checkpoint/candidate/runtime != semantic result
AF-06 stale canonical state rejected
AF-07 stale Attempt writers fenced
AF-08 scoped idempotent effects
AF-09 runtime/platform success != semantic completion
AF-18 crash-window/outbox/reconciliation consistency
AF-19 Evaluation retry does not double-count
AF-20 platform jobs/native retries remain subordinate
```

Critical future scenarios include concurrent Attempt creation, stale writer wake-up, lost launch acknowledgement, unresolved external side effects, invalid/incomplete checkpoints, cross-Execution resume rejection, safe immutable-effect adoption, Evaluation deduplication, cancellation/completion races, provider-cancel failure, coordinator restart and PostgreSQL concurrent-writer behavior.

## Future implementation sequence

Only after a later phase explicitly authorizes coding:

```text
G1  Execution/Attempt identity, states and public views
G2  AttemptEpoch/current-authority/CAS persistence
G3  RuntimeInvocation ownership + WriterFence plumbing
G4  operation idempotency + launch intent/correlation
G5  checkpoint commit/head + resume assessment
G6  recovery/restart/resume/reconciliation coordination
G7  stale-writer enforcement + safe immutable-effect adoption
G8  cancellation-generation and cancellation/completion races
G9  operational-completion barrier + semantic-owner handoff
G10 V7 failure-injection/conformance/Q1-Q2 integration
```

None of G1-G10 is executed during Phase 005.

## Deferred ownership

005-G leaves to:

- 005-H — Evidence, Provenance, historical query and reproducibility treatment of operational history;
- 005-I — current authorization, credentials, trust, security and no-egress enforcement;
- 005-J — concrete scheduler/launcher/lease/checkpoint/platform adapters, observability and support matrices;
- 005-K — final cross-slice delivery sequencing and implementation-readiness audit.

## No upstream revision required

005-G requires no change to the eleven accepted concepts, fifteen synchronizations, Phase 003 experience contract, Phase 004 architecture/ADR set, or 005-C through 005-F implementation-planning authority.

No new architecture ADR is required.

## Exit criteria

- [x] planning-only boundary preserved;
- [x] Execution/Attempt/epoch identity plan defined;
- [x] observed state and mutation authority separated;
- [x] isolation-first WriterFence model defined;
- [x] lease/heartbeat kept distinct from fencing;
- [x] Attempt-owned immutable runtime invocation defined;
- [x] durable launch/correlation/unknown-response model defined;
- [x] operation-scoped idempotency defined;
- [x] checkpoint commitment/immutability/resume qualification defined;
- [x] restart/resume/reconcile recovery modes defined;
- [x] safe prior-effect adoption and Evaluation deduplication seams defined;
- [x] cancellation/completion linearization defined;
- [x] operational completion separated from semantic completion;
- [x] persistence/API/error impacts mapped;
- [x] V7/fitness obligations mapped;
- [x] future G1-G10 coding sequence defined without execution.

## Exit decision

**005-G — implementation plan complete; no production implementation performed.**

Next:

**005-H — Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan**.
