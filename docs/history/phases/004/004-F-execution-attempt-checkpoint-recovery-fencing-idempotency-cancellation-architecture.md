---
type: Phase Record
title: 004-F — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture
status: complete
---

# 004-F — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture

## Objective

Translate accepted Execution semantics, the Phase 003 monitoring/recovery experience, and the 004-C/004-D/004-E persistence/data/runtime boundaries into an operational architecture that can survive retries, coordinator loss, partial effects, checkpoint/resume, and cancellation races without changing committed domain semantics or creating ambiguous authoritative results.

## Governing authority

- [Execution](../../concepts/execution.md)
- [Execution Monitoring, Failure, Recovery & Cancellation Experience](../../experience/execution-monitoring-failure-recovery-cancellation.md)
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md)
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md)
- [Core Synchronizations](../../synchronizations/core-synchronizations.md)

## Canonical architecture created

- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](../../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md)

## ADR created

- [ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution](../../decisions/ADR-0005-attempt-epoch-fencing-recoverable-at-least-once-execution.md)

## Main decisions

### 1. One stable Execution survives valid retries/resumes

One operationalized committed Learning, Generation, or Evaluation retains one logical Execution identity across scheduler submissions, worker/cluster replacement, checkpoint resume, and compatible operational recovery.

Material semantic change remains a new domain activity and new Execution.

### 2. Attempts receive ordered fencing authority

Each write-capable Attempt receives a supersedable ordered Attempt epoch/fencing generation.

The epoch is operational authority, not semantic revision or control-plane state version.

### 3. At most one current framework mutation epoch

Framework-owned mutable surfaces recognize at most one current Attempt epoch for canonical mutation at a time.

Older physical work may continue, but stale epochs must be rejected or isolated from current candidate/checkpoint/control state.

### 4. Lease and fence have different roles

A lease may express expected liveness and detect abandonment.

Lease expiry alone is insufficient to prevent a stale writer from resuming later. Material mutation boundaries require fence/precondition enforcement where ambiguity matters.

### 5. Attempt overlap/duplicate compute remains possible

The architecture does not require all prior physical work to terminate before recovery when strong fencing/isolation exists.

Duplicate physical computation remains acceptable; duplicate canonical authority does not.

### 6. Immutable Attempt-scoped runtime invocation

Every Attempt references an immutable invocation derived from the same committed activity.

Recovery may change only operationally permitted fields such as Attempt identity/epoch, compatible resource placement, recovery basis, or scratch namespace.

### 7. Platform submission must be correlatable/reconcilable

A crash may occur after an external scheduler accepts work but before SYNGAN records the platform run ID.

Launch adapters therefore need provider idempotency keys, stable correlation labels, durable submission intent, lookup/reconciliation, or equivalent mechanisms. Platform duplicate launch remains physical duplication and cannot become new Execution identity.

### 8. Idempotency is operation-scoped

No universal idempotency key is accepted.

Separate scopes exist for Attempt creation/launch, checkpoint commit, candidate mutation/seal, Evaluation aggregation, semantic promotion, and cancellation.

An idempotency key does not bypass stale Attempt fencing.

### 9. Side effects are classified by recovery risk

Architecture distinguishes disposable Attempt-local effects, framework-staged non-final effects, framework-canonical effects, external deduplicable/fenceable effects, and external irreversible/weakly identifiable effects.

External effects that cannot be safely reconciled may block automatic retry.

### 10. Checkpoint is immutable recovery state

Checkpoint remains operational state rather than Learned State/output/Evidence.

A committed checkpoint is an immutable recovery snapshot after distributed component closure/integrity is established.

Incomplete checkpoint writes remain non-resumable unless reconciliation proves a valid committed checkpoint.

### 11. Checkpoint identity binds exact context

Checkpoint references preserve parent Execution/Attempt/epoch, commitment snapshot, implementation binding/runtime invocation, state codec, relevant source/input/dependency identities, progress scope, integrity basis, and randomness/reproducibility facts where material.

### 12. Resume compatibility is contextual

Resume qualification may be eligible, eligible with operational limitations, restart-required, incompatible, or indeterminate/reconciliation-required.

File existence is insufficient.

A checkpoint from another committed activity cannot masquerade as same-Execution resume.

### 13. Recovery explicitly selects restart/resume/reconcile/terminate

A bounded recovery decision records why prior effects can be retained/fenced/ignored and which new Attempt epoch becomes authoritative.

Recovery remains Execution-owned operational history, not a new concept.

### 14. Unknown state remains durable

Lost platform/job/write/external-call knowledge remains indeterminate until sufficient reconciliation/fencing exists.

Unknown is not coerced to failure simply to enable retry.

### 15. Reconciliation uses durable identities

Execution/Attempt IDs, platform correlation IDs, candidate/checkpoint references, provider transaction/idempotency identities, and fences are used to determine what happened and whether continuation is safe.

Unresolvable external ambiguity may remain indeterminate.

### 16. 004-D candidate writes use Attempt fencing

Candidate membership carries enough Attempt/epoch context that stale writes can be rejected, isolated, or omitted from the sealed candidate.

Candidate seal is blocked while current-writer authority remains ambiguous.

### 17. Seal is idempotent and preconditioned

Repeated seal for the same exact candidate/manifest generation resolves to the same sealed snapshot or detects incompatible mutation.

A stale Attempt cannot mutate sealed state.

### 18. Semantic promotion remains owner-side and at-most-once in authority

Learning result establishment, Generation output promotion, and Evaluation/Evidence establishment remain separate semantic transitions protected by expected owner state/version and exact result basis.

Attempt success does not grant promotion authority.

### 19. Evaluation retry cannot double-count accidentally

Shard/partition Evaluation aggregation needs stable logical work-unit identity so repeated work cannot count twice unless repeated observation is explicitly part of the committed method.

### 20. Cancellation is durable intent, then reconciliation

Cancellation request is versioned/idempotent and does not instantly imply `cancelled`.

The operational outcome may be cancelled, completed before stop, failed while cancelling, or indeterminate.

### 21. Cancellation fences future effects where possible

Once cancellation is accepted for processing, ordinary new Attempts are not issued and current runtime work is asked to stop. Framework-owned mutation authority can be invalidated/advanced so late work cannot silently regain authority.

### 22. Late platform success is only an operational fact

A runtime may report success after cancellation request. That does not automatically authorize Learned State establishment, Evidence, candidate sealing, or output promotion.

### 23. Terminal Execution classification requires resolved authoritative work

Execution completion requires no unresolved authoritative operational work/defect under its contract. Failure means no valid same-semantics continuation remains. Cancellation means operational cancellation is sufficiently resolved. Otherwise indeterminate remains valid.

None of those outcomes defines parent semantic completion.

### 24. Structured failure facts replace exception-only state

Operational failures retain category, retryability basis, side-effect ambiguity, checkpoint/recovery state, platform references, and diagnostics sufficient for safe automated/operator decisions.

### 25. Automatic retry has no authority shortcut

Automated retry is allowed only when the same compatibility, side-effect, cancellation, dependency, and no-egress checks that govern manual retry establish safety.

### 26. Platform adapters remain subordinate

Scheduler/runtime adapters may submit/query/cancel/reconcile platform work and provide bounded telemetry, but they cannot decide domain completion or bypass Attempt fencing.

### 27. Canonical operational persistence remains bounded

SYNGAN persists Execution/Attempt/epoch state, invocation references, checkpoint/recovery/cancellation/reconciliation facts, material failures, and selected platform correlations—not every Spark task/log/GPU heartbeat.

### 28. Crash windows are explicitly recoverable

004-F defines logical crash-consistency sequences for Attempt start, checkpoint commit, candidate sealing, and semantic promotion so coordinator failure results in reconciliation rather than duplicate authority.

## Architecture consequences for later groups

### 004-G

Evaluation/Evidence/Provenance architecture must preserve exact Attempt/recovery/result relationships, make Evidence establishment idempotent/coherent, capture material reconciliation/cancellation history, and support historical query without duplicating platform telemetry.

### 004-H

Security architecture must authorize operational actions separately from semantic changes, protect checkpoint/candidate/diagnostic access, and avoid exposing fencing/idempotency/credential material unnecessarily.

### 004-I

Platform integration must map provider-specific leases, transaction/version primitives, idempotency, job correlation, cancellation, and reconciliation capabilities to the canonical contracts and surface guarantee gaps honestly.

### 004-J

Consolidation must verify the 004-C state-version model, 004-D candidate/promotion model, 004-E immutable runtime invocation model, and 004-F Attempt epoch/fencing model compose without overlapping version/authority semantics.

## No new concept result

004-F does not introduce domain concepts for Attempt, Attempt Epoch, Lease, Fence, Checkpoint, Recovery Plan, Retry, Resume, Reconciliation, Idempotency Key, Cancellation Request, Incident, Job, Run, or Orphan Work.

These remain subordinate Execution semantics or architecture mechanisms.

## Deferred decisions

004-F intentionally does not select:

- scheduler/orchestrator;
- concrete lock/lease service;
- fence token encoding;
- lease durations/heartbeat policy;
- retry/backoff/attempt-count defaults;
- checkpoint file/table/object format;
- checkpoint retention/garbage collection;
- platform idempotency technology;
- transaction/outbox implementation;
- error/exception class hierarchy;
- metrics/logging backend;
- operator authorization model.

## Exit criteria

- [x] one stable Execution / many Attempt architecture established;
- [x] ordered Attempt epoch/fencing semantics established;
- [x] lease-versus-fence distinction established;
- [x] stale-writer exclusion established without exactly-once computation requirement;
- [x] immutable Attempt-scoped invocation preserved;
- [x] platform launch crash/reconciliation boundary established;
- [x] operation-scoped idempotency established;
- [x] side-effect risk classification established;
- [x] immutable checkpoint snapshot/reference architecture established;
- [x] contextual resume qualification established;
- [x] restart/resume/reconcile distinction established;
- [x] unknown state preserved as durable operational truth;
- [x] candidate/manifest fencing integration established;
- [x] idempotent seal and at-most-one semantic promotion obligations preserved;
- [x] Evaluation duplicate-count protection established;
- [x] durable cancellation intent/race handling established;
- [x] structured failure/retryability boundary established;
- [x] automatic retry cannot bypass semantic/policy safety;
- [x] canonical monitoring/persistence remains bounded;
- [x] crash-consistency sequences are explicit;
- [x] no scheduler/lock/checkpoint implementation prematurely selected;
- [x] ADR rationale recorded.

## Exit assessment

**Status: complete.**

SYNGAN now has a portable operational architecture that permits retries, speculative/duplicate computation, checkpoint resume, and platform failover while using Attempt epochs, fencing, scoped idempotency, and reconciliation to protect canonical state. Unknown side effects remain explicit; cancellation is resolved rather than assumed; and no runtime/platform success can bypass the owning semantic completion barrier.

## Next phase

**004-G — Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture**
