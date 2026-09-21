---
type: Implementation Authority
title: Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan
status: active
---

# Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan

## Purpose

Define the concrete **future implementation plan** for SYNGAN's durable operational-realization substrate: Execution and Attempt identity/state, Attempt epochs and writer fencing, immutable Attempt-scoped runtime invocation, platform launch intent/correlation, checkpoint commitment and resume qualification, retry/restart/reconciliation, operation-scoped idempotency, unknown-state handling, cancellation races, and operational-completion handoff to the semantic owner.

This document is the canonical Phase 005-G implementation-planning authority.

**Phase 005 remains planning-only.** This plan does not create production source, database schema, migration, scheduler adapter, checkpoint store, Spark/PyTorch runtime, tests, CI workflow, or deployment infrastructure.

## Governing authority

005-G is downstream of:

- [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md);
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md);
- [005-B Verification Strategy](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [005-C Source Topology](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md);
- [005-D Public Resource/Control-Plane Plan](public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md);
- [005-E Spark Data Boundary Plan](spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md);
- [005-F Runtime/SPI/Learned-State Plan](strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md).

The governing implementation-planning rule is:

> **One stable Execution may contain multiple Attempts and duplicate or ambiguous physical work, but only the currently authorized Attempt epoch may advance framework-owned operational state or contribute effects to later semantic promotion.**

The target remains **at-least-once physical realization with fenced, idempotent, and reconcilable canonical effects**, not exactly-once computation.

## Planning-only boundary

Names below such as `ExecutionHandle`, `AttemptRef`, `AttemptEpoch`, `WriterFence`, `CheckpointRef`, `RecoveryDecision`, and `LaunchIntent` identify accepted future implementation roles and intended contracts. They are not current production classes or database tables.

The G1-G10 sequence later in this document is a future coding sequence only.

## Accepted future implementation choices

005-G accepts the following baseline:

- `Execution`, `Attempt`, committed checkpoint, and immutable runtime invocation become durable 005-D `ResourceRef`-addressable operational resources where stable referenceability is required;
- one committed Learning/Generation/Evaluation occurrence has at most one primary logical Execution under the current architecture;
- one Execution may have many immutable/distinguishable Attempts;
- every write-capable Attempt receives a positive monotonic `AttemptEpoch` scoped to its Execution;
- `AttemptEpoch` remains distinct from `StateVersion`, semantic revision, schema version, candidate generation, checkpoint sequence, package/runtime version, and platform retry count;
- Attempt observed/runtime state remains separate from current framework mutation authority;
- one Execution current-authority projection identifies the current Attempt/epoch, while older Attempts remain historical and may continue physically without write authority;
- lease/heartbeat information is liveness evidence only and does not substitute for fencing;
- writer fencing is validated at framework-controlled mutation/adoption/seal boundaries; Attempt-isolated immutable physical namespaces are preferred so no database fence check is required for every row/file write;
- a shared mutable physical target is conformant only if the provider can enforce a real resource-local version/fence/CAS contract;
- platform launch is modeled as a durable intent plus provider correlation/reconciliation boundary so loss of the submission acknowledgement does not imply launch failure;
- operation idempotency is scoped by command/effect target and request fingerprint rather than one global Execution idempotency key;
- committed checkpoints are immutable recovery snapshots with exact Execution/Attempt/invocation/codec/input/dependency identity and bounded manifest/reference state;
- checkpoint existence is never equivalent to resume eligibility;
- recovery explicitly chooses restart, resume, reconcile-first, or cannot-continue-same-Execution;
- unknown/indeterminate platform or side-effect state remains durable and may block automatic retry;
- cancellation becomes a durable linearized intent; accepting cancellation revokes ordinary current write/promotion authority even if the physical platform process cannot be stopped immediately;
- operational completion remains separate from Learning/Generation/Evaluation semantic completion;
- scheduler/platform job IDs, native retries, leases, and success signals remain subordinate observations/integrations rather than Execution/Attempt identity or semantic authority;
- 005-G selects no scheduler/queue/lock service/lease service/checkpoint backend or platform launcher. Concrete launch/platform mappings remain 005-J responsibility.

## Future package ownership

005-G refines the 005-C package plan with responsibilities equivalent to:

```text
src/syngan/
├── domain/
│   └── execution/
│       ├── state.py
│       ├── attempt.py
│       ├── recovery.py
│       └── cancellation.py
├── ports/
│   └── execution/
│       ├── persistence.py
│       ├── launcher.py
│       ├── checkpoints.py
│       ├── reconciliation.py
│       └── fencing.py
├── application/
│   └── execution/
│       ├── start.py
│       ├── launch.py
│       ├── retry.py
│       ├── recover.py
│       ├── reconcile.py
│       ├── cancel.py
│       └── complete.py
├── api/
│   └── execution.py
└── adapters/
    └── persistence/
        └── sql/
            └── execution_records/
```

Exact leaf-file spelling may change during the later coding phase if cohesion improves, but ownership and dependency direction must remain equivalent.

Checkpoint physical storage and concrete scheduler/provider launchers remain adapters behind the execution/runtime ports and do not move platform dependencies inward.

## Resource and identity plan

### Additional `ResourceKind` roles

005-G reserves future infrastructure/resource kinds equivalent to:

```text
execution
execution_attempt
runtime_invocation
checkpoint
```

These are implementation/reference roles. `Execution` is already an accepted domain concept; Attempt/checkpoint/runtime invocation remain subordinate operational/representation state and do not become new concepts merely because they receive durable IDs.

### `ExecutionHandle`

005-G now accepts the concrete public `ExecutionHandle` role anticipated by 005-D.

It contains a typed `ResourceRef(kind=execution)` and no scheduler session, platform client, database session, bearer credential, or mutable runtime object.

Public inspection resolves an owner-specific `ExecutionView` rather than mutating data attached to the handle.

### `AttemptRef`

An Attempt is referenced by:

```text
AttemptRef
    ResourceRef(kind=execution_attempt)
```

and persists its parent Execution plus immutable Attempt facts.

Attempt identity is never derived from Databricks run ID, Spark application ID, Kubernetes job name, process ID, or another provider identity.

### `AttemptEpoch`

`AttemptEpoch` is a positive monotonic integer scoped to one Execution.

Initial write-capable Attempt uses epoch 1. Creating a later write-capable Attempt atomically allocates an epoch greater than every prior epoch for that Execution.

The allocation occurs through the Execution mutation transaction/CAS path; timestamp ordering and platform retry number are not valid substitutes.

## Execution state model

005-G plans an owner-specific `ExecutionState` equivalent to:

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

Exact future enum spelling may be refined if transition tests demonstrate a smaller equivalent state model, but these distinctions must remain representable.

Important rules:

- `completed_operationally` means the authoritative operational realization finished and returned a result suitable for semantic-owner inspection; it does not mean Learning/Generation/Evaluation completed;
- failed Attempt does not automatically mean failed Execution;
- `indeterminate` may later reconcile to running/completed/failed/cancelled;
- `cancellation_requested` is not terminal cancellation;
- `recovery_pending` allows a failed/unknown Attempt to remain non-terminal while same-commitment continuation is assessed.

Execution current state uses 005-D `StateVersion` CAS.

## Attempt state and authority dimensions

005-G deliberately avoids one giant Attempt status enum.

### Observed operational state

A future `AttemptObservedState` preserves what SYNGAN currently knows about the physical try, equivalent to:

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

Provider-specific states map into this bounded operational vocabulary without becoming canonical state names themselves.

### Mutation authority

Mutation authority is a separate dimension derived from/preserved by Execution current authority:

```text
current_authorized
fenced
never_write_authorized / read-only where applicable
```

An Attempt may therefore be:

```text
observed state: running
authority: fenced
```

when an old platform job continues after a newer Attempt takes over.

A missed heartbeat or provider timeout may instead yield:

```text
observed state: unknown
authority: still current
```

until the control layer deliberately fences/reconciles it.

This separation prevents liveness observations from silently becoming write-authority decisions.

## Current-authority projection

The future Execution current-state row/projected control record retains bounded authority information equivalent to:

```text
execution_ref
execution_state
state_version
current_attempt_ref?
current_attempt_epoch?
cancellation_generation
last_authority_transition
```

`cancellation_generation` is a positive monotonic operational barrier generation, initially 0, advanced when cancellation is accepted. It is distinct from AttemptEpoch.

A future `WriterFence` carries enough information equivalent to:

```text
WriterFence
    execution_ref
    attempt_ref
    attempt_epoch
    cancellation_generation
```

The fence is an authority discriminator, not a secret/bearer credential. 005-I later adds actual authorization/capability security.

A framework mutation is authorized only if the execution/attempt/epoch/cancellation generation still match the current allowed authority and the target's resource-local preconditions also hold.

## Fencing enforcement model

### Isolation-first scalable default

For Spark-scale and model-state writes, the preferred future pattern is:

```text
Attempt A7 / epoch 7
    ↓
unique Attempt-local physical namespace
    ↓
immutable/staged components
    ↓
framework registration/adoption/seal
    ↓ validate WriterFence once at bounded authority boundary
```

This avoids requiring a database lookup or fence check for every generated row/file/parameter write.

An old Attempt may continue writing into its isolated stale namespace, but it cannot register those effects into the current candidate/checkpoint/state manifest after fencing.

### Shared mutable targets

If an adapter must write a shared mutable target, the provider must supply a genuine conditional/fencing primitive such as versioned transaction/CAS/fencing semantics strong enough to reject stale writers.

A provider that cannot enforce this must either use Attempt-isolated writes or report incompatibility for recovery modes that require concurrent/stale-writer safety.

### Required future fence points

Writer/authority validation must be planned at least for:

- candidate component/index registration and candidate seal from 005-E;
- Learned-State candidate/representation registration and seal from 005-F;
- checkpoint commitment/head update;
- Evaluation partial-result/aggregate contribution acceptance where retries can duplicate work;
- authoritative Attempt operational completion;
- semantic-owner completion/promotion barrier where cancellation/current-authority state is material.

## Lease and heartbeat plan

Leases/heartbeats may support:

- coordinator ownership hints;
- suspected worker loss;
- retry timing;
- operational health views;
- automatic recovery policy.

They do not prove that an old process has stopped.

A lease expiration may allow the coordinator to **decide to fence** the old Attempt through durable authority transition, but the fence—not the expired lease—is what prevents later authoritative mutation.

Clock time is therefore never the sole ordering authority for stale-writer exclusion.

## Immutable runtime invocation ownership

005-F planned one immutable runtime invocation per Attempt. 005-G gives that invocation durable operational ownership.

A `RuntimeInvocationRef` uses `ResourceRef(kind=runtime_invocation)` and binds:

- parent Attempt/Execution;
- exact committed activity and `SnapshotId`;
- exact implementation binding and `RuntimeSpiVersion`;
- exact source/state/subject/output targets;
- resolved dependency/network posture;
- permitted operational tuning;
- `WriterFence`/authority context;
- optional validated checkpoint input for resume;
- invocation schema version.

An Attempt cannot change its invocation in place after launch. A materially different invocation creates a different Attempt or, if semantics change, a different domain commitment.

## Platform launch and correlation plan

### Launcher port

005-G defines a future technology-neutral `WorkloadLauncher`/equivalent port responsible for:

```text
submit exact Attempt invocation
query/reconcile provider state by stable correlation
request provider cancellation
return bounded platform references/observations
```

It does not define Execution semantics and does not expose platform jobs as canonical resources.

Concrete Spark/Databricks/Kubernetes/other launchers remain 005-J adapters.

### Durable launch intent

External submission follows a durable intent pattern:

```text
persist LaunchIntent + idempotency/correlation identity
        ↓ commit
submit to provider
        ↓
record provider observation/correlation
```

A `LaunchIntent` is technical Execution-owned state containing bounded facts equivalent to:

- operation identity/idempotency scope;
- AttemptRef and RuntimeInvocationRef;
- provider/launcher kind;
- stable provider correlation/idempotency token if supported;
- request fingerprint;
- submission observation state;
- provider job/run references when known;
- last reconciliation facts.

`LaunchIntent` is not a domain concept, not an Attempt substitute, and not an outbox replacement when the 005-D outbox is used to dispatch the launch.

### Lost acknowledgement case

If provider submission succeeds but acknowledgement is lost, SYNGAN persists/returns `unknown` rather than assuming failure.

Reconciliation must first use the durable correlation token/provider query capability to discover the effect. Only when the provider/effect is provably safe to repeat may a new submission occur.

If the provider cannot identify/deduplicate the side effect, automatic retry may remain blocked while the Execution remains indeterminate.

## Operation-scoped idempotency plan

005-G standardizes a technical future `IdempotencyKey`/operation record pattern without introducing one global semantic key.

The scope includes at least:

```text
operation family
exact target ResourceRef(s)
request fingerprint
caller-supplied/generated idempotency key
stored resulting logical effect/reference
```

Rules:

- same key + same request fingerprint returns the same accepted effect/result;
- same key + materially different request fingerprint is an explicit conflict;
- stale `WriterFence` remains invalid even if the idempotency key previously succeeded;
- idempotency controls logical effects, not whether physical provider work ran exactly once.

Future operation families include:

- establish/start Execution;
- create next Attempt/recovery action;
- dispatch one Attempt launch;
- commit one checkpoint;
- request cancellation;
- reconcile one identified ambiguous effect;
- candidate seal/promotion and semantic result establishment through their owning 005-E/005-H contracts.

## Attempt creation transaction

Creating a new Attempt is one bounded 005-D control transaction equivalent to:

```text
load Execution at expected StateVersion
validate same-commitment recovery/start eligibility
validate prior side-effect/reconciliation safety
allocate next AttemptEpoch
create AttemptRef
create immutable RuntimeInvocationRef
persist RecoveryDecision if applicable
set current Attempt/epoch
advance Execution state/version
append transition history
persist required launch/outbox intent
commit
```

Concurrent retry requests race on Execution `StateVersion`/epoch allocation; at most one becomes the newly authorized current Attempt for the intended recovery operation.

The losing request refreshes/resolves idempotently or receives a structured conflict. It cannot silently create another current writer.

## Checkpoint model

### `CheckpointRef`

A committed checkpoint is represented by:

```text
CheckpointRef
    ResourceRef(kind=checkpoint)
```

The checkpoint's immutable descriptor records or references bounded facts equivalent to:

```text
parent ExecutionRef
producing AttemptRef + AttemptEpoch
RuntimeInvocationRef
committed activity + SnapshotId
checkpoint format/codec identity + version
exact source/input/subject/state refs where material
dependency/base-artifact refs
represented progress/recovery cursor
randomness/RNG continuation facts where material
component/manifest root
integrity descriptor
runtime/software compatibility requirements
creation/commit context
SchemaVersion
```

Large checkpoint payload remains outside SQL/control rows.

### Staged versus committed checkpoint

Runtime may write an Attempt-local checkpoint workspace/candidate, but `CheckpointRef` is established only after required closure/integrity checks and current-fence validation succeed.

An incomplete directory/file/object set is not a checkpoint merely because bytes exist.

Committed checkpoint contents are immutable under that CheckpointRef. A later checkpoint gets another identity.

### Checkpoint discovery/head

Execution may maintain a bounded `checkpoint_head`/latest-known committed checkpoint pointer for navigation/performance, but it is not proof that the pointed checkpoint is currently eligible to resume.

Checkpoint timestamps are not the sole ordering/selection criterion.

Attempt epoch, checkpoint ordinal/progress descriptor, exact invocation compatibility, integrity, and current recovery context are considered before resume.

## Resume compatibility plan

A future `ResumeAssessment` is a derived operational value equivalent to:

```text
eligible
eligible_with_limitations
restart_required
incompatible
indeterminate
```

It must inspect material continuity including:

- same Execution/activity/commitment snapshot;
- exact Strategy/method semantics;
- implementation binding/runtime compatibility;
- state/checkpoint codec compatibility;
- exact source/input/subject refs;
- Learned-State/direct-generation basis;
- dependency/base-artifact identities;
- network/no-egress posture;
- checkpoint integrity/completeness;
- represented progress;
- randomness/reproducibility continuity;
- candidate/state material already produced;
- current security authorization when 005-I is composed.

A checkpoint from another Execution cannot be called `resume` state. Reusing it as an input to new semantic work would need an explicit later derivation contract.

## Recovery modes and decision record

005-G accepts future `RecoveryMode` values equivalent to:

```text
restart
resume
reconcile_first
cannot_continue_same_execution
```

A durable `RecoveryDecision` under Execution records bounded explanation such as:

- prior AttemptRef/outcome;
- selected mode;
- ResumeAssessment/checkpoint basis;
- side effects retained, ignored, fenced, quarantined, or adopted;
- material compatibility/limitation facts;
- new AttemptRef/Epoch when continuation occurs;
- automation/operator origin when audit-relevant.

This remains operational history, not a new `Recovery` concept.

## Safe reuse/adoption of prior physical work

Enterprise scale makes unconditional discard of all prior work undesirable, but reuse must never bypass current authority.

005-G therefore permits **verified adoption of immutable prior effects** under current authority.

Examples include:

- immutable Generation candidate components written by a prior Attempt into isolated namespaces;
- sealed/committed checkpoint components;
- immutable Learning-state components;
- Evaluation partial aggregates with exact logical work-unit identity.

Adoption requires proof of:

- same committed activity semantics;
- exact component identity/integrity;
- no post-fence mutable contamination;
- unambiguous work-unit/membership ownership;
- no gap/duplicate effect under the owning manifest/aggregation protocol;
- current WriterFence/current-authority approval.

A fenced Attempt's late result can never become authoritative merely by finishing. Current authority must explicitly verify/adopt the immutable effect.

Mutable or weakly identified side effects produced after fencing are ineligible for automatic adoption.

## Evaluation retry/double-count prevention

005-G fixes the operational seam required by AF-19.

Evaluation implementations that can resume/merge distributed work must expose an exact logical contribution/work-unit identity so repeated physical computation can be deduplicated.

Conceptually:

```text
work unit W17
A1 produces contribution C1
A1 outcome becomes unknown
A2 repeats W17 -> C2

aggregation accepts one logical W17 contribution
not C1 + C2 as two independent observations
```

The exact work-unit key is method/runtime-specific and is not a new domain concept.

If an Evaluation method cannot safely identify/merge resumable partial state, the recovery contract must require restart from clean aggregate state rather than guessing.

005-H later ensures resulting Evidence claim strength remains consistent with actual coverage.

## Unknown and reconciliation model

### Unknown remains durable

Provider timeout, lost coordinator response, disconnected Spark driver, uncertain checkpoint commit, uncertain candidate seal, or another ambiguous external effect may place an Attempt/Execution in `unknown`/`indeterminate` state.

Unknown is never automatically mapped to failed or successful solely to allow progress.

### Reconciliation port

Future reconciliation uses a narrow `OperationalReconciler`/equivalent port plus relevant provider/data/checkpoint ports to answer bounded material questions using stable IDs and correlations.

It may determine:

- whether launch occurred and how many provider jobs correlate;
- whether the prior job remains active;
- whether a checkpoint committed;
- whether candidate/state material is sealed or only staged;
- whether semantic promotion already occurred;
- whether prior effects can be fenced/ignored/adopted;
- whether a newer Attempt can safely receive authority.

Platform observations are inputs to the reconciliation decision, not authority over the domain activity.

### Coordinator restart

A new coordinator process reconstructs Execution management from durable 005-D records, Attempt/runtime-invocation history, checkpoint/candidate references, launch intents, provider correlations, and current fence state.

No process-local Future, lock, object graph, SparkSession, or in-memory retry counter is required for durable recovery identity.

## Cancellation model

### Cancellation command

A future cancellation request is operation-idempotent and targets one Execution.

Its control transaction checks current Execution/domain state and linearizes one of the following outcomes:

```text
already completed / no longer cancellable
already cancellation-requested
cancellation accepted
conflict / indeterminate requiring refresh
```

If cancellation is accepted:

1. Execution transitions to `cancellation_requested` under expected `StateVersion`;
2. `cancellation_generation` advances;
3. ordinary current Attempt writer/promotion authorization using the old `WriterFence` becomes invalid;
4. a durable provider-cancel intent is recorded/dispatched;
5. later reconciliation observes whether physical work stopped, succeeded, failed, or remains unknown.

Advancing cancellation generation does not claim the platform process stopped.

### Cancellation versus completion linearization

The control plane must make the cancellation/completion race explicit.

If authoritative operational/semantic completion linearizes first, a later cancel reports already completed/not cancellable and does not undo the result.

If cancellation acceptance linearizes first, the prior Attempt's old fence cannot subsequently establish authoritative operational completion or semantic promotion even if the provider later reports success.

The semantic owner may later transition the parent Learning/Generation/Evaluation to cancelled only when its own lifecycle requirements and the reconciled Execution outcome permit it.

### Provider cancellation is not domain cancellation

Provider `CANCELLED`, `KILLED`, or equivalent is an operational observation.

Likewise a provider cancellation failure does not restore old write authority. SYNGAN can remain `cancellation_requested`/indeterminate while stale physical work continues non-authoritatively.

## Operational completion barrier

Only the current authorized Attempt may establish an Execution's authoritative operational-completion basis.

A future immutable bounded `OperationalCompletionRecord`/equivalent stores:

```text
ExecutionRef
AttemptRef + AttemptEpoch
RuntimeInvocationRef
runtime-result reference/summary
material candidate/state/diagnostic refs
provider/runtime observations
completion timestamp/context
SchemaVersion
```

Execution state transitions to `completed_operationally` using expected `StateVersion`, current Attempt/epoch, cancellation-generation and resource-local preconditions.

A physically successful but fenced Attempt remains historical Attempt success and cannot establish this record directly.

### Operational completion versus semantic completion

After `completed_operationally`:

- Learning still validates/seals candidate state and establishes Learned State;
- Generation still seals/validates the exact candidate, obtains required Evaluation/Evidence, and promotes output;
- Evaluation still interprets method result and establishes Evidence.

If semantic validation fails, Execution may correctly remain `completed_operationally` while the parent domain activity fails or follows its own same-commitment retry rules.

Platform/runtime success is therefore never enough to update the parent semantic lifecycle directly.

## Retry policy boundary

Automatic retry policy is operational configuration, not domain authority.

A future policy may consider:

- failure class;
- Attempt count;
- deadline/backoff;
- checkpoint availability;
- resource capability;
- side-effect safety;
- cancellation state.

It may vary only semantically neutral operational values permitted by the 005-F implementation binding/invocation contract.

It cannot silently:

- switch Strategy or Evaluation method;
- change source/subject/Conditions/Constraint handling;
- substitute Learned State;
- change material dependency identity;
- enable network/egress;
- weaken no-egress;
- change precision/topology when that is material to semantics/reproducibility.

Such changes require explicit upstream/new-commitment handling.

## Persistence impact plan

The future SQL control-store implementation requires bounded ownership records equivalent to:

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

These are logical persistence responsibilities, not a mandate for one physical table per label.

They reuse 005-D:

- ResourceRef/SchemaVersion;
- `StateVersion` CAS;
- bounded transactions/locks;
- unique constraints/idempotency;
- append-preserving transition history;
- transactional outbox/durable intent;
- tombstone/historical resolution.

No schema or migration is created during Phase 005.

### Key future constraints

The SQL adapter must be able to enforce or participate in constraints equivalent to:

- at most one primary Execution per committed activity under current architecture;
- unique AttemptRef and unique `(execution, attempt_epoch)`;
- current-authority transition only under expected Execution StateVersion;
- immutable Attempt/runtime-invocation/checkpoint descriptors after establishment;
- operation-idempotency key/request-fingerprint uniqueness within scope;
- one authoritative operational completion per Execution;
- cancellation/completion CAS race cannot both win incompatibly.

## Public/API plan

005-G adds future public roles equivalent to:

```text
ExecutionHandle
ExecutionView
AttemptView
CheckpointSummary / CheckpointRef where authorized
RecoveryAssessmentView
CancellationResult
```

`SynGANClient` may later expose owner-specific operations such as:

```text
resolve execution
start operational realization
request retry/recovery
inspect attempts
inspect checkpoints
request reconciliation
request cancellation
```

These calls remain application/use-case coordination. Public API callers never mutate Execution SQL rows directly and never use platform job IDs as the primary API identity.

## Failure/error model

Future structured operational errors/results must distinguish at least:

```text
stale execution state
stale/fenced Attempt
launch acknowledgement unknown
provider correlation ambiguous
checkpoint incomplete
checkpoint incompatible
resume indeterminate
unsafe retry due to unresolved external side effect
cancellation already requested
completion won cancellation race
cancellation won completion race
platform outcome unknown
resource-local fence failure
idempotency key payload conflict
```

These are not collapsed into one opaque exception string or generic `retry failed` state when programmatic recovery can distinguish them.

## Verification mapping

005-G primarily owns future V7 — Execution/failure-injection/recovery verification — with material V2/V4/V5/V6/V10 contributions.

Direct architecture-fitness obligations include:

```text
AF-04  checkpoint/candidate/runtime material != semantic result
AF-06  stale current-state writes rejected
AF-07  stale Attempt writers are fenced
AF-08  scoped idempotent sealing/promotion/completion effects
AF-09  runtime/platform success != semantic completion
AF-18  crash-window transition/outbox/reconciliation consistency
AF-19  Evaluation retry does not double-count logical work
AF-20  platform jobs/native retries remain subordinate
```

Required future deterministic/failure scenarios include:

1. concurrent retry requests allocate one new current Attempt epoch;
2. A1 loses lease, A2 gets newer epoch, A1 resumes and its current-state/candidate/checkpoint registration is rejected;
3. old Attempt continues writing only to isolated namespace and cannot seal/register under the newer fence;
4. provider accepts launch but acknowledgement is lost; reconciliation discovers/adopts it rather than blind duplicate submit;
5. provider cannot deduplicate/query an ambiguous side effect; automatic retry remains blocked/indeterminate;
6. checkpoint bytes exist but closure commit fails; resume rejects them;
7. same-Execution compatible checkpoint resumes; cross-Execution checkpoint is rejected;
8. state-codec/runtime incompatibility yields restart/incompatible rather than silent substitution;
9. verified immutable prior components can be adopted only by current authority;
10. duplicate Evaluation work-unit contributions are deduplicated or restart is required;
11. cancellation CAS wins before completion; late platform success cannot regain write/promotion authority;
12. completion CAS wins first; later cancellation cannot undo the completed operational/semantic result;
13. provider cancellation fails while stale work continues; canonical writes remain fenced;
14. failed Attempt leaves Execution recovery-pending rather than automatically failed;
15. coordinator restart reconstructs Execution/Attempt/launch/checkpoint state without process-local memory;
16. provider/native retry/job IDs cannot replace Execution/Attempt IDs;
17. operation idempotency same-key/same-payload returns same effect, same-key/different-payload conflicts;
18. operationally successful runtime with semantically invalid result does not rewrite Execution as failed merely to match domain failure.

Real concurrent persistence tests belong in the PostgreSQL Q2 profile; scheduler/provider-specific conformance belongs to 005-J adapters.

## Acceptance evidence requirements

When a later coding phase implements 005-G, completion evidence must include at least:

- authority/plan revision used;
- Execution/Attempt/checkpoint persistence schema/migration revisions;
- stale-writer and concurrent-Attempt test results;
- launch crash-window/reconciliation results;
- checkpoint compatibility/restart/resume scenario results;
- cancellation/completion race results;
- Evaluation duplicate-contribution protection results;
- provider launcher conformance results for claimed platforms;
- PostgreSQL concurrent-writer evidence;
- known provider fencing/idempotency limitations;
- any waiver allowed by 005-B governance.

## Future implementation sequence

Only after a later phase explicitly authorizes coding:

```text
G1  Execution/Attempt identity, states and public views
G2  AttemptEpoch/current-authority/CAS persistence
G3  immutable RuntimeInvocation ownership and WriterFence plumbing
G4  operation idempotency + launch-intent/outbox/correlation ports
G5  checkpoint descriptor/commit/head + resume assessment
G6  recovery/restart/resume/reconciliation coordination
G7  stale-writer enforcement and safe immutable-effect adoption
G8  cancellation generation + cancellation/completion linearization
G9  operational-completion barrier and parent-domain handoff
G10 V7 failure-injection/conformance/Q1-Q2 integration
```

None of G1-G10 is executed during Phase 005.

## Deferred ownership

005-G leaves to later planning:

- Evidence establishment/provenance of Attempts/checkpoints/recovery and reproducibility impact — 005-H;
- current authorization, credential revocation, secret access, extension/checkpoint trust and no-egress enforcement — 005-I;
- concrete scheduler/launcher/lease/storage/platform integrations, observability correlation, platform compatibility and operational scaling — 005-J;
- final cross-slice migration/delivery sequencing and implementation-readiness audit — 005-K.

## Rejected alternatives

005-G rejects as the future universal implementation model:

- platform job/run identity as Execution/Attempt identity;
- exactly-once physical computation as a package-wide requirement;
- lease expiry as proof a stale writer stopped;
- one global distributed lock around all Execution work;
- last-writer-wins current state;
- blind resubmission after unknown platform launch;
- one global idempotency key per Execution;
- checkpoint-file existence as resume proof;
- checkpoint identity equal to Learned State/output/Evidence identity;
- cancellation signal sent equal to terminal cancellation;
- platform `SUCCESS` equal to semantic completion;
- retry policy that silently changes committed semantics;
- new Attempt writing the same unfenced mutable workspace as the old Attempt;
- automatic adoption of a fenced Attempt's late mutable effects.

## No new concepts or upstream revision

005-G adds no Retry, Recovery, Checkpoint, Lease, Fence, Operation, Launch Intent, Scheduler Job, or Cancellation Request concept.

No change is required to the eleven accepted concepts, fifteen synchronizations, Phase 003 experience contract, Phase 004 architecture/ADR set, or 005-C through 005-F implementation-planning authority.

No new architecture ADR is required.

## Exit criteria

- [x] planning-only boundary preserved;
- [x] Execution/Attempt/resource identities and AttemptEpoch defined;
- [x] observed Attempt state separated from mutation authority;
- [x] current-authority/WriterFence/cancellation-generation model defined;
- [x] scalable isolation-first fence enforcement defined;
- [x] lease/heartbeat role kept separate from fencing;
- [x] immutable Attempt runtime-invocation ownership defined;
- [x] launch intent/correlation/unknown-response model defined;
- [x] operation-scoped idempotency model defined;
- [x] checkpoint identity/commit/immutability/head model defined;
- [x] resume compatibility and recovery modes defined;
- [x] safe immutable-effect adoption and Evaluation deduplication seams defined;
- [x] unknown/reconciliation/coordinator-restart model defined;
- [x] cancellation/completion linearization defined;
- [x] operational completion kept separate from semantic completion;
- [x] future persistence/API/error impacts mapped;
- [x] V7/AF verification and acceptance evidence mapped;
- [x] G1-G10 future coding sequence defined without execution.

## Exit decision

**005-G — implementation plan complete; no production implementation performed.**

Next:

**005-H — Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan**.
