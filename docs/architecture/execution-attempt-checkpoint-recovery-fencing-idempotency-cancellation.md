---
type: Architecture Authority
title: Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture
status: active
---

# Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture

## Purpose

Define the durable operational architecture by which one committed Learning, Generation, or Evaluation can survive platform retries, coordinator loss, worker replacement, partial side effects, checkpoint/resume, cancellation races, and ambiguous platform outcomes without changing committed domain semantics or creating duplicate canonical results.

This document establishes the canonical Phase 004-F operational architecture beneath [Execution](../concepts/execution.md), the Phase 003 execution experience, the 004-C control-plane consistency model, the 004-D candidate/materialization boundary, and the 004-E runtime-adapter boundary.

It defines logical Attempt identity, Attempt epochs/write authority, checkpoint state, retry/resume qualification, idempotency scopes, unknown-state reconciliation, cancellation coordination, and the operational obligations needed for single semantic promotion. It does **not** select a scheduler, lock service, database, queue, lease technology, checkpoint format, or platform-specific job API.

## Governing authority

This architecture remains downstream of:

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md);
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md);
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md);
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](strategy-extension-learning-generation-evaluation-runtime-adapter.md);
- [Execution](../concepts/execution.md);
- [Execution Monitoring, Failure, Recovery & Cancellation Experience](../experience/execution-monitoring-failure-recovery-cancellation.md);
- [Core Synchronizations](../synchronizations/core-synchronizations.md), especially SYNC-04, SYNC-07, SYNC-11, SYNC-14 and SYNC-15.

## Primary decision

SYNGAN SHALL implement operational continuation around one stable logical Execution and an ordered sequence of distinguishable Attempts.

Every Attempt that may mutate framework-owned operational/data-plane state receives an **Attempt epoch / fencing generation** whose authority is validated at material mutation boundaries.

Conceptually:

```text
Committed domain activity
        ↓
Execution EX7
        ↓
Attempt A1 / epoch 1
        ↓ failure / unknown / recovery decision
Attempt A2 / epoch 2
        ↓
Attempt A3 / epoch 3
```

A later epoch supersedes earlier write authority even if older physical processes continue running.

The architecture therefore targets:

> **at-least-once physical realization with fenced, idempotent, and reconcilable canonical side effects.**

It does not require exactly-once computation.

## Execution identity and current authority

### One Execution per operationalized committed activity

Under the current model, one committed Learning, Generation, or Evaluation that requires operational realization has one primary logical Execution identity.

Execution identity remains stable across:

- platform resubmissions;
- cluster replacement;
- worker/process replacement;
- retry from start;
- checkpoint resume;
- compatible resource-topology changes;
- scheduler failover;
- temporary loss and later reconciliation of platform state.

A material change to the committed domain activity requires a new activity and therefore a different Execution. Operational recovery never edits the commitment snapshot.

### Execution current-state projection

Execution has owner-specific current operational state and a conflict-detectable state version as required by 004-C.

Material transitions such as:

- start Attempt;
- enter recovery pending;
- request cancellation;
- classify completed/failed/cancelled/indeterminate;
- adopt a reconciliation result;

must be persisted against expected current state/version rather than silent last-writer-wins.

### Current Attempt authority

Execution SHOULD retain a bounded current-authority projection equivalent to:

```text
execution_id
current_attempt_id
current_attempt_epoch
execution_state
state_version
cancellation_generation / intent when present
```

Historical Attempts remain append-preserved even when they no longer hold current authority.

## Attempt architecture

### Attempt identity

An Attempt is a durable subordinate operational record under one Execution.

It preserves or references enough information equivalent to:

- stable Attempt identity;
- parent Execution identity;
- monotonic Attempt epoch/fencing generation;
- exact runtime invocation specification identity from 004-E;
- recovery/restart basis;
- platform submission/run references;
- material runtime/resource/dependency facts;
- start/end timing where known;
- operational outcome;
- checkpoint/candidate/diagnostic references created or consumed;
- cancellation acknowledgement facts;
- reconciliation/supersession relationships.

Attempt identity is not a platform job ID.

### Attempt epoch

Each write-capable Attempt SHALL have an epoch/generation that can be ordered relative to prior Attempts for the same Execution.

The epoch is operational authority, not domain semantic version.

A new Attempt epoch is issued only through Execution's concurrency-controlled recovery/start transition.

The exact representation may be an integer generation, opaque fencing token plus ordering metadata, CAS-issued sequence, or equivalent. The architecture requires monotonic supersession semantics, not a specific encoding.

### At most one current framework mutation epoch

At any moment, framework-owned mutable surfaces for an Execution SHALL recognize at most one current Attempt epoch as authorized for canonical mutation.

Older Attempts may still be:

- physically running;
- producing logs;
- completing abandoned compute;
- writing to physically isolated Attempt-local scratch space;

but MUST be prevented from mutating the current candidate manifest, checkpoint head, Execution current state, semantic-promotion intent, or another current framework-owned authority after their epoch is superseded.

### Attempt overlap is not forbidden

The architecture does not require physically stopping an old Attempt before a new one can exist when fencing/isolation is sufficiently strong.

However, if the prior Attempt may still perform an externally visible effect that cannot be fenced or deduplicated, a new Attempt MUST NOT blindly repeat that effect until reconciliation establishes a safe continuation path.

## Lease versus fencing semantics

### Lease is liveness coordination

A lease MAY be used to indicate which coordinator/Attempt is expected to be active and to detect abandonment.

A lease alone is insufficient as write safety because an expired or partitioned writer can later resume.

### Fencing is mutation authority

Material framework-owned writes SHOULD carry the current Attempt epoch/fencing token and be accepted only when it is still current for the target Execution/resource boundary.

Conceptually:

```text
A1 holds epoch 7
A1 pauses
lease expires
A2 starts with epoch 8
A1 resumes

write(epoch=7) -> REJECT
write(epoch=8) -> ACCEPT if other preconditions hold
```

The exact enforcement point depends on the resource adapter but the invariant is architectural.

### Resource-local fences may be stronger

Candidate materialization, checkpoint heads, distributed component indexes, external provider transactions, or other resources MAY have resource-local generations in addition to the parent Attempt epoch.

Those local generations do not replace Execution/Attempt identity; they refine mutation safety at the physical boundary.

## Runtime invocation and launch architecture

### Invocation is frozen before launch

Each Attempt references an immutable 004-E runtime invocation specification derived from the same committed domain activity.

A retry/resume may differ in operationally allowed values such as:

- Attempt identity/epoch;
- compatible compute placement;
- resource count within allowed semantics;
- recovery/checkpoint reference;
- retry-specific scratch namespace;

but MUST NOT change material semantic bindings.

### Platform submission is idempotency-aware

Starting an Attempt may race with client/network/coordinator failure after a platform submission was accepted but before SYNGAN persisted the returned platform ID.

The platform-launch adapter therefore SHOULD support one or more of:

- provider idempotency keys;
- deterministic/external submission correlation keys;
- discoverable labels/tags containing Execution/Attempt identity;
- durable pre-submission intent plus post-submission reconciliation;
- another mechanism sufficient to avoid accidental unbounded duplicate launch.

Duplicate platform launch may still occur where providers cannot guarantee deduplication. Such duplication remains physical work and must be fenced from canonical side effects.

## Idempotency architecture

### Idempotency is scoped, not universal

SYNGAN SHALL NOT define one global idempotency key for every operation.

Material operations require idempotency semantics appropriate to their authority boundary.

Relevant scopes include:

1. **Attempt creation/start** — repeated client/control requests should resolve to the intended Attempt or a conflict, not silently create unlimited new Attempts.
2. **Platform submission** — repeated submission of one Attempt should be deduplicated/reconciled where provider capability allows.
3. **Checkpoint commit** — retrying commit for one checkpoint identity should not establish multiple conflicting checkpoint snapshots.
4. **Candidate component/manifest mutation** — repeated writes are accepted only according to candidate membership and current fence semantics.
5. **Candidate seal** — repeated sealing of the same immutable candidate generation should resolve to the same sealed snapshot or detect incompatible mutation.
6. **Evaluation partial aggregation** — repeated partition/shard results must not be double-counted unless the committed method explicitly defines duplication semantics.
7. **Semantic result promotion** — Learning result establishment, Generation output promotion, and Evaluation/Evidence establishment must be fenced/idempotent under owner contracts.
8. **Cancellation request** — repeated equivalent cancellation requests should preserve one durable intent rather than create contradictory terminal states.

### Idempotency identity includes semantic target

An idempotency key/token MUST be scoped strongly enough that reuse cannot cause one operation's effect to be mistaken for another materially different operation.

For example, candidate sealing should bind the candidate/materialization identity and expected manifest generation, not merely a human request ID.

### Idempotency does not excuse stale authority

A previously valid idempotency key does not permit an obsolete Attempt epoch to mutate current state after supersession.

Fencing/precondition validation is evaluated together with idempotency.

## Side-effect classification

Operational recovery SHALL distinguish side-effect classes equivalent to:

### 1. Attempt-local / disposable

Scratch files, temporary logs, isolated intermediate components, or recomputable work that cannot be mistaken for canonical state.

May usually be repeated safely.

### 2. Framework-staged / non-final

Candidate components, checkpoint staging, partial Evaluation aggregates, or other data tracked under framework identity/fencing.

May be reused or repeated only through the relevant manifest/checkpoint/recovery contract.

### 3. Framework-canonical

Execution current state, sealed snapshot references, promoted result associations, durable Evidence/Provenance authority transitions.

Requires owner-specific concurrency, idempotency, and fencing.

### 4. External but deduplicable/fenceable

External effects for which the provider offers transaction/version/fencing/idempotency semantics sufficient for safe retry.

### 5. External irreversible or weakly identifiable

Effects that may have occurred but cannot be safely fenced, queried, or deduplicated.

Such ambiguity may block automatic retry and require reconciliation/operator intervention or terminal indeterminacy.

This classification is architectural guidance, not a new domain taxonomy.

## Checkpoint architecture

### Checkpoint is recovery state, not semantic result

A checkpoint is an operationally persisted snapshot intended to continue one Execution.

It does not become Learned State, completed output, or Evidence merely because it is durable.

### Open versus committed checkpoint representation

Checkpoint writing MAY itself be multi-component/distributed.

Architecture SHOULD distinguish an in-progress checkpoint write from a committed immutable checkpoint snapshot/reference.

Conceptually:

```text
checkpoint workspace
     ↓ write components
checkpoint candidate
     ↓ integrity/closure commit
Checkpoint CP12
immutable recovery snapshot
```

A failed/incomplete checkpoint write remains non-resumable unless later reconciliation can establish a valid committed snapshot.

### Checkpoint reference

A committed checkpoint should preserve or resolve enough information equivalent to:

- checkpoint identity;
- parent Execution and producing Attempt;
- producing Attempt epoch;
- exact committed activity / commitment-snapshot identity;
- runtime invocation / implementation-binding identity;
- state codec/format/version;
- source/input/subject references when material to continuation;
- dependency/base-artifact identities;
- progress/completion scope represented by the checkpoint;
- component/manifest identity and integrity basis;
- randomness/RNG continuation facts where required;
- runtime/software compatibility requirements;
- creation/commit state and representation schema version.

Large checkpoint payload remains data-plane state; the control plane stores bounded identity/reference facts.

### Checkpoint immutability

Once CP12 is committed as a recovery snapshot, its material contents/meaning are immutable under that identity.

A later checkpoint is CP13 or another distinguishable snapshot rather than an in-place rewrite of CP12.

Physical representation migration may preserve one checkpoint identity only under an explicit equivalence/integrity contract, analogous to other distributed representations.

## Resume compatibility architecture

### Resume is a contextual assessment

Checkpoint existence does not imply resume eligibility.

Before a new Attempt uses a checkpoint, recovery logic SHALL assess compatibility against the same Execution and committed activity.

The assessment considers, where material:

- exact parent Execution/activity identity;
- commitment snapshot identity;
- Strategy/method semantic revision/configuration;
- implementation binding/runtime compatibility;
- state codec compatibility;
- source/input/subject/reference identity;
- Learned State/direct-generation basis;
- dependency/base-artifact identity;
- network/no-egress posture;
- checkpoint integrity/completeness;
- represented progress scope;
- randomness/reproducibility continuity;
- candidate/materialization context already affected;
- known implementation-specific resume limitations.

### Qualification outcome

Architecture must preserve outcomes equivalent to:

- **eligible to resume**;
- **eligible with explicit operational limitations**;
- **restart required; checkpoint not reusable**;
- **incompatible with same Execution semantics**;
- **indeterminate; reconciliation required**.

This is derived operational state, not a new concept.

### Resume does not imply no recomputation

A valid resume may recompute work already represented in the checkpoint if the algorithm/runtime requires it and correctness remains preserved.

Exactly-once training steps/partition work are not a package-wide requirement.

### Cross-activity checkpoint use

A checkpoint from one Execution MUST NOT be used as a `resume` checkpoint for another committed activity.

If a future workflow explicitly supports using recovery state as an input/seed to a new activity, that must be represented as a new domain derivation/reference contract rather than mislabeled resume.

## Recovery decision architecture

### Retry from start versus resume

Recovery explicitly chooses between:

```text
retry from clean/isolated state
resume from validated checkpoint/recovery snapshot
reconcile first
cannot continue same Execution
```

The decision is based on committed-semantics continuity and side-effect safety, not merely on availability of files.

### Recovery plan

A recovery action SHOULD persist or reference a bounded recovery decision containing enough information to explain:

- prior Attempt/outcome;
- retry/resume/reconcile choice;
- checkpoint/recovery basis if used;
- side effects retained, fenced, ignored, or quarantined;
- compatibility assessment and material limitations;
- new Attempt identity/epoch;
- operator/automation origin where audit requires it.

A recovery plan is Execution-owned operational history, not a new domain concept.

## Unknown-state and reconciliation architecture

### Unknown is durable

If SYNGAN loses sufficient knowledge of a platform job, candidate write, checkpoint commit, external call, or other side effect, Execution/Attempt may enter an unknown/indeterminate state.

Architecture MUST NOT coerce unknown into failure merely to retry or into success because some output exists.

### Reconciliation works from durable identities

Reconciliation uses stable Execution/Attempt IDs, platform correlation IDs, candidate/checkpoint references, provider transaction/version identities, idempotency keys, and current fences to determine what actually happened to the degree possible.

It SHOULD answer only material questions needed for safe classification/continuation, such as:

- is the prior Attempt still active?;
- did platform submission occur once or multiple times?;
- which Attempt epoch produced a candidate component?;
- did checkpoint CP12 commit fully?;
- did candidate CM9 seal as SC9?;
- did an external idempotent operation commit?;
- did semantic promotion already succeed?;
- can prior effects be fenced/ignored/reused safely?;

### Reconciliation result

Possible outcomes include:

- previous Attempt still authoritative/running;
- prior Attempt completed operationally;
- prior Attempt failed/cancelled;
- safe to issue newer Attempt epoch;
- safe to resume from identified checkpoint;
- prior effects quarantined/fenced;
- semantic result already promoted;
- continued indeterminacy.

A reconciliation conclusion is persisted as material Execution history where it affects retry/cancellation/terminal classification.

### Unresolvable external ambiguity

When an external side effect cannot be queried, fenced, or deduplicated sufficiently, SYNGAN may be unable to prove retry safety.

The architecture MUST permit remaining indeterminate or requiring explicit operator/governance action rather than guessing.

## Candidate/output recovery integration

004-D candidate materialization integrates with Attempt fencing as follows:

```text
Execution EX7
  Attempt A1 / epoch 1
      ↓ candidate writes
  A1 fails
      ↓
  reconcile candidate state
      ↓
  Attempt A2 / epoch 2
      ↓ writes accepted only under epoch 2
      ↓
  seal candidate snapshot
      ↓
  required Evaluation
      ↓
  Generation promotion
```

### Candidate ownership

A candidate materialization records enough Attempt/epoch membership information that losing/stale Attempt writes can be rejected, isolated, or excluded from the sealed snapshot.

### Sealing precondition

A candidate cannot be sealed while there is unresolved authoritative-writer ambiguity for the candidate generation being sealed.

The seal operation is idempotent for an exact candidate/manifest generation and must reject incompatible post-seal mutation.

### Promotion precondition

Generation promotion validates canonical Generation state, exact sealed candidate identity, required Evidence, and expected state/fence conditions.

Attempt success alone never grants promotion authority.

## Learning recovery integration

Learning recovery distinguishes at least:

- checkpoint/restart material;
- candidate final Learned State representation;
- established Learned State.

A later Attempt may resume from an eligible checkpoint and eventually create/seal a candidate learned-state representation.

Learning result establishment is an owner-side idempotent/fenced semantic transition, yielding zero or one primary Learned State.

A stale runtime process cannot establish the Learned State directly.

## Evaluation recovery integration

Evaluation recovery may reuse partial distributed examination state only when identity, coverage, method configuration, and aggregation semantics remain valid for the same committed Evaluation.

### Duplicate observation protection

For shard/partition-based Evaluation, durable partial-result aggregation MUST distinguish logical work-unit identity strongly enough that retry does not double-count the same unit unless the Evaluation method intentionally defines repeated observations as separate samples.

### Method result versus Evidence

Recovered runtime measurements remain method-result material. Evaluation establishes Evidence only after validating final coverage, assumptions, uncertainty, and interpretability.

Repeated Attempts must not establish ambiguous duplicate Evidence for one semantic finding.

## Cancellation architecture

### Cancellation intent is durable and monotonic

Cancellation begins with a durable request against expected Execution state/version.

The request records enough facts equivalent to:

- Execution identity;
- cancellation request identity/generation;
- requester/origin where required;
- request time;
- currently authoritative Attempt/epoch observed;
- optional reason;
- whether semantic activity had already reached a terminal result when checked.

Repeated equivalent cancellation requests are idempotent.

### Cancellation revokes future operational authority

Once cancellation is accepted for processing, Execution SHALL prevent issuance of new ordinary Attempts unless an explicit reconciliation/administrative rule later determines that cancellation did not become terminal and continuation is permitted.

Current Attempts are instructed to stop through their platform/runtime adapters.

Where possible, cancellation also invalidates or advances write authority so work completing after the cancellation decision cannot silently mutate current framework-owned state.

### Cancellation cannot erase prior authority

Cancellation does not undo:

- immutable commitment snapshots;
- prior Attempt history;
- an already sealed historical candidate/checkpoint;
- a semantic result already promoted before cancellation took effect.

Cleanup/retention is separate.

### Cancellation race classification

After cancellation request, reconciliation may yield:

- **cancelled** — authoritative work stopped and no unresolved operational effect prevents terminal classification;
- **completed before cancellation took effect** — operational endpoint had already been reached;
- **failed while cancelling**;
- **indeterminate/reconciliation pending**.

The parent Learning/Generation/Evaluation independently determines its semantic terminal state.

### Late completion after cancellation request

A platform job may report success after cancellation was requested.

That report is accepted as an operational fact about the Attempt, not automatic permission for candidate sealing, Learned State establishment, Evidence establishment, or Generation promotion.

Owner-side state/fence checks decide which subsequent transitions remain legitimate.

## Terminal Execution classification

Execution may become operationally completed only when:

- all authoritative required operational work has reached its endpoint;
- there is no unresolved current Attempt or side-effect ambiguity that invalidates completion classification;
- current framework-owned side effects are in a coherent state sufficient for the parent domain workflow to continue its semantic completion checks;
- cancellation has not already resolved terminally in a conflicting way.

Execution may become failed when no valid same-semantics retry/resume/reconciliation path remains.

Execution may become cancelled when cancellation has been operationally resolved sufficiently.

Execution remains indeterminate when the architecture cannot support a stronger truthful classification.

None of these outcomes alone determines parent domain semantic completion.

## Failure taxonomy architecture

004-F does not freeze one public exception enum, but operational failure records SHOULD preserve structured dimensions sufficient to distinguish:

- category: infrastructure/resource/dependency/access/runtime/storage/coordination/cancellation/unknown/etc.;
- retryability assessment and basis;
- whether same-semantics recovery is possible;
- side-effect ambiguity level;
- checkpoint/recovery availability;
- policy/network implications;
- platform-native error/reference;
- human-safe summary;
- detailed diagnostic reference where authorized.

A raw exception string is not sufficient canonical operational state.

## Automation and retry policy boundary

Automatic retry is permitted only when the same retry-safety checks apply as for manual retry.

A retry policy MAY consider:

- failure category;
- attempt count;
- elapsed time/deadline;
- backoff;
- checkpoint availability;
- resource availability;
- side-effect safety;
- cancellation state;
- policy limits.

But policy MUST NOT infer semantic safety merely from exception type or platform retryability.

Retry counts/backoff values are implementation/deployment policy and remain deferred.

## Platform adapter contract

A platform/execution adapter may provide capabilities such as:

- submit Attempt using a correlation/idempotency key;
- query platform state by durable correlation/reference;
- cancel platform work;
- retrieve bounded progress/health;
- expose native run/job/log links;
- discover orphan/duplicate submissions;
- report provider transaction/idempotency results;
- help reconcile ambiguous state.

It MUST NOT:

- decide domain semantic completion;
- make native run identity equal Execution/Attempt identity;
- silently retry with changed domain semantics;
- bypass current Attempt fencing;
- infer canonical success solely from native job success;
- automatically enable undeclared dependency/network behavior.

## Persistence boundaries

### Canonical operational state

Control-plane persistence SHOULD retain bounded canonical facts equivalent to:

- Execution identity/current state/state version;
- current Attempt/epoch authority;
- Attempt records/outcomes;
- immutable invocation references;
- material checkpoint/recovery references;
- retry/resume/reconciliation decisions;
- cancellation request/outcome;
- material platform correlations;
- failure summaries;
- side-effect/promotion facts required for safe recovery;
- transition/provenance references.

### Non-canonical detailed telemetry

Platform-native systems remain appropriate for:

- every Spark task/stage metric;
- executor logs;
- worker heartbeats;
- fine-grained GPU telemetry;
- per-record processing logs;
- exhaustive scheduler events.

SYNGAN may retain links/summaries but does not duplicate this data by default.

## Crash-consistency sequences

### Start Attempt

A valid sequence is conceptually:

```text
1. validate Execution is recoverable/startable
2. allocate Attempt ID + next epoch atomically/CAS
3. persist immutable invocation reference + launch intent
4. submit to platform with correlation/idempotency metadata
5. persist returned platform reference when available
6. reconcile if the client/coordinator fails between 3-5
```

No requirement is made that steps 3-5 share one distributed transaction with the external scheduler.

### Commit checkpoint

Conceptually:

```text
1. write checkpoint components to Attempt-scoped staging
2. establish component closure/integrity
3. commit immutable checkpoint identity under current epoch/fence
4. persist checkpoint reference/history
5. repeated commit resolves idempotently
```

### Seal Generation candidate

Conceptually:

```text
1. verify current candidate generation and writer fence
2. establish manifest/component closure
3. establish immutable sealed snapshot identity
4. persist seal atomically/CAS where possible
5. later stale writes are rejected/excluded
```

### Promote semantic result

Promotion remains owner-specific but operational architecture requires:

```text
1. validate expected owner state/version
2. validate exact non-final representation/result basis
3. validate required semantic prerequisites
4. establish at-most-one result association idempotently
5. record required Provenance/transition intent consistently
6. reconcile crash ambiguity rather than issuing a second result blindly
```

004-G refines Evidence/Provenance transaction/query architecture.

## Reproducibility and historical execution facts

Execution/Attempt history preserves only material operational facts needed for explanation/reproduction, such as:

- Attempt order and outcomes;
- exact implementation/runtime invocation references;
- checkpoint resume basis;
- resource/runtime changes materially affecting behavior;
- dependency/service identities;
- recovery/reconciliation decisions;
- material nondeterminism/seed continuation facts;
- cancellation timing/outcome;
- platform references for drill-down.

The existence of retries does not itself make an activity unreproducible, but recovery/runtime differences may constrain the supported reproduction class.

## Security and authorization boundary

004-F assumes that start/retry/resume/cancel/reconcile/cleanup operations will be authorization-controlled by 004-H.

Operational authority to retry or cancel does not imply authority to change semantic commitments, access withheld diagnostics, transmit data, substitute dependencies, or release outputs.

Fencing tokens, idempotency keys, checkpoint locators, and platform correlation data may themselves be sensitive operational material and should not be exposed indiscriminately.

## Scale architecture

Execution state remains bounded by logical Attempts/material transitions rather than platform task count.

The architecture MUST support:

- hours/days-long work;
- process/coordinator restart;
- cluster replacement;
- millions of Spark tasks beneath one Attempt;
- very large candidate/checkpoint state referenced distributively;
- bounded progress aggregation;
- no full telemetry collection to driver/control-plane memory.

## Architecture invariants

1. One operationalized committed activity has one stable primary Execution identity under the current model.
2. A valid retry/resume creates a distinguishable Attempt under the same Execution and same committed semantics.
3. Each write-capable Attempt has a supersedable ordered epoch/fencing generation.
4. At most one Attempt epoch may hold current framework mutation authority for an Execution boundary at a time.
5. Lease expiry alone is insufficient to guarantee stale-writer safety; material writes require fencing/precondition enforcement where ambiguity matters.
6. Physical Attempt overlap/duplicate computation may occur, but losing/stale work cannot mutate current canonical state.
7. Platform job identity remains subordinate reference, not Execution/Attempt identity.
8. Runtime invocation is immutable per Attempt and cannot silently change the parent commitment.
9. Idempotency is scoped to the material operation/semantic target and does not replace fencing.
10. Checkpoint existence does not imply committed checkpoint integrity or resume compatibility.
11. A committed checkpoint is immutable recovery state bound to exact Execution/activity/runtime/dependency context.
12. Resume compatibility is contextual and may be eligible, restart-required, incompatible, or indeterminate.
13. Cross-activity checkpoint use cannot masquerade as same-Execution resume.
14. Unknown side-effect/platform state remains explicit until reconciled or safely fenced.
15. External unfenceable/undeduplicable ambiguity may block automatic retry rather than being guessed away.
16. Candidate sealing requires resolved authoritative-writer state and exact immutable manifest identity.
17. Repeated physical work cannot create multiple Learned States, multiple completed outputs, or ambiguous duplicate Evidence for one committed semantic result.
18. Evaluation recovery must prevent accidental double-counting of repeated logical work units.
19. Cancellation request is durable intent, not immediate terminal cancellation.
20. Cancellation does not erase committed history or already established semantic results.
21. Late platform success after cancellation does not automatically regain semantic promotion authority.
22. Execution terminal state remains operational and does not establish Learning/Generation/Evaluation semantic completion.
23. Automatic retry obeys the same safety/compatibility rules as manual retry.
24. Canonical Execution history remains bounded and does not become a shadow platform observability store.
25. Ordinary recovery/checkpoint/output handling does not require full driver-local payload materialization.
26. No retry/recovery mechanism may silently enable network access, substitute dependencies, or weaken the committed semantic contract.

## No new concept result

004-F does not introduce domain concepts for:

- Attempt;
- Attempt Epoch;
- Lease;
- Fence;
- Checkpoint;
- Recovery Plan;
- Retry;
- Resume;
- Reconciliation;
- Idempotency Key;
- Cancellation Request;
- Incident;
- Job;
- Run;
- Orphan Work.

These are subordinate Execution state/actions or architecture mechanisms beneath the accepted concept model.

## Deferred decisions

004-F intentionally does not select:

- scheduler/orchestrator;
- database/lock service;
- lease duration/heartbeat policy;
- concrete fencing-token encoding;
- retry/backoff/attempt-limit values;
- checkpoint file/table/object format;
- checkpoint garbage-collection/retention defaults;
- platform idempotency implementation;
- exact error-code/exception hierarchy;
- dead-letter/incident-management integration;
- distributed queue technology;
- specific transaction/outbox mechanism;
- operator authorization model;
- concrete metrics/logging backend.

## Validation obligations for implementation planning

Phase 005 implementation/test planning must prove at least:

- a stale Attempt cannot mutate current candidate/checkpoint/control state after a newer epoch takes authority;
- coordinator failure after platform submission can be reconciled without assuming submit failure;
- repeated Attempt-start requests do not create uncontrolled duplicate Attempts;
- checkpoint commit is atomic/reconcilable and incomplete checkpoints cannot be resumed as valid;
- incompatible checkpoint/runtime/dependency context blocks resume;
- restart-from-start and resume remain distinguishable;
- duplicated Generation partition writes cannot create ambiguous sealed membership;
- candidate sealing is idempotent and rejects unresolved writer ambiguity;
- repeated semantic-promotion requests establish at most one authoritative result;
- repeated Evaluation shard work cannot double-count accidentally;
- cancellation races preserve actual operational outcome and cannot rewrite an already promoted result;
- unknown external side effects remain indeterminate when no safe reconciliation exists;
- automatic retry cannot bypass same-semantics, no-egress, dependency, or cancellation constraints;
- Execution history remains bounded under large Spark task counts.

## Operational principle

A committed Generation G42 owns Execution EX9. Attempt A1 receives epoch 1 and writes candidate components. Its coordinator disappears after submitting work, so A1 becomes unknown rather than immediately failed.

Reconciliation discovers that the platform job is no longer active but some candidate components committed under epoch 1. The candidate protocol identifies those components unambiguously and no external irreversible effect remains. EX9 enters recovery pending.

Attempt A2 is then created with epoch 2. Any late A1 writes carrying epoch 1 are rejected from current candidate membership. A2 resumes/recomputes safely, seals exact candidate SC42, and completes operationally. Generation remains awaiting required validation. Only after Evaluation/Evidence satisfies the committed completion requirements does Generation idempotently associate one completed output O42.

If cancellation had raced with A2 completion, Execution would preserve the cancellation request and reconcile whether operational completion occurred before stop; neither scheduler status nor cancellation timing would by itself decide whether Generation could semantically complete.

## Phase relationship

004-F supplies the operational substrate required by later architecture:

- **004-G** will refine Evidence establishment, Provenance transition consistency, reproducibility facts, and historical query over Attempt/recovery state;
- **004-H** will refine authorization for start/retry/resume/cancel/reconcile plus protection of checkpoints, diagnostics, and operational credentials/tokens;
- **004-I** will map these contracts onto deployment/platform capabilities and identify provider-specific guarantee gaps;
- **004-J** will audit the combined architecture for consistency and implementation readiness.
