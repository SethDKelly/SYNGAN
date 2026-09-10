---
type: Architecture Authority
title: Phase 007-H Execution/Attempt, Idempotency, Fencing, Non-Regressing Recovery, Checkpoint, Cancellation & Admission Foundation
status: active
---

# Phase 007-H — Execution/Attempt, Idempotency, Fencing, Non-Regressing Recovery, Checkpoint, Cancellation & Admission Foundation

## Purpose

Refine SYNGAN's operational-realization architecture for stable Execution identity, distinguishable Attempts, operation-scoped idempotency, stale-writer fencing, non-regressing authority recovery, checkpoint/restart/resume, reconciliation, cancellation, and resource/runtime admission **without selecting a scheduler, queue, lock/lease service, fencing-token encoding, database schema, checkpoint format, retry library, admission algorithm, platform job API, or executable verification implementation**.

007-H continues the architecture/design track governed by the [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md). It is design authority, not permission to implement execution/recovery behavior.

## Governing authority

007-H is downstream of:

- [Concept Design Methodology](../authority/design-methodology.md);
- [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md);
- [Execution](../concepts/execution.md);
- [Execution Monitoring, Failure, Recovery & Cancellation Experience](../experience/execution-monitoring-failure-recovery-cancellation.md);
- [Operational Authority Continuity & Regressive Recovery Contract](../authority/operational-authority-continuity-regressive-recovery-contract.md);
- [Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract](../authority/enterprise-scale-resource-admission-approximation-degraded-operation-contract.md);
- [007-D Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation](phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md);
- [007-E Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline](phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md);
- [007-F Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation](phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md);
- [007-G Strategy/Method Binding, Dependency Trust, Authorization, Secrets & Distributed Runtime Closure Foundation](phase-007-g-strategy-method-binding-dependency-trust-authorization-secrets-distributed-runtime-closure-foundation.md);
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md);
- [Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture](deployment-scalability-observability-portability-compatibility-platform-integration.md);
- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](../decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md);
- [ADR-0007 — Explicit Dependency Resolution & Scoped Capability Security](../decisions/ADR-0007-explicit-dependency-resolution-scoped-capability-security.md);
- [ADR-0009 — Non-Regressing Authority After Regressive Control-State Recovery](../decisions/ADR-0009-non-regressing-authority-after-regressive-control-state-recovery.md);
- accepted synchronizations, especially SYNC-04, SYNC-07, SYNC-11, SYNC-14 and SYNC-15.

The Phase 005-G execution/recovery implementation plan remains downstream feasibility/planning evidence. Its concrete type names, package layout, enum spelling and persistence/API assumptions are not architecture premises during the current design freeze.

## Design result

007-H accepts the following operational foundation:

> **One committed domain activity may have one stable logical Execution and many distinguishable physical Attempts. Duplicate physical work is acceptable where unavoidable; duplicate or ambiguous canonical semantic promotion is not.**

> **Current mutation authority is stronger than an Attempt number. Where regressive recovery is possible, write authority composes a non-regressing recovery-authority frontier, current Execution/Attempt authority, resource-local mutation preconditions where needed, and current action authorization. A restored row, old lease, queue ticket, platform job or stale Attempt epoch cannot recreate authority by itself.**

> **Potentially regressive restore enters continuity-unverified recovery quarantine. Old writers are excluded first; surviving effects are then reconciled, reconstructed or adopted by current authority. Recovery never gives an old writer its former authority back merely because its work survived.**

> **Admission is current operational eligibility to begin or continue material work under the exact committed activity and current environment. Admission is not semantic readiness, authorization by itself, a scheduling guarantee, a queue position, or write authority.**

The resulting operational target remains:

```text
at-least-once physical realization
        +
current non-regressing authority
        +
operation-scoped idempotency
        +
stale-writer fencing / isolation
        +
reconciliation of ambiguous effects
        ↓
at-most-one authoritative semantic result transition
```

Exactly-once physical computation is not required.

## 1. Architecture roles and non-concepts

007-H uses architecture/integration roles equivalent to:

- Attempt;
- Attempt observation/outcome;
- Attempt mutation authority;
- recovery-authority frontier/incarnation;
- lease/heartbeat/liveness observation;
- fence/fencing generation;
- resource-local write generation/precondition;
- idempotency request/effect identity;
- launch intent/provider correlation;
- checkpoint candidate/committed checkpoint;
- resume-compatibility assessment;
- recovery decision/plan;
- reconciliation observation/conclusion;
- cancellation intent/generation;
- admission request/decision/reservation/queue observation;
- platform/runtime work correlation.

These remain subordinate Execution state or architecture mechanisms.

007-H does **not** create domain concepts named `Attempt`, `Checkpoint`, `Retry`, `Resume`, `Recovery`, `Fence`, `Lease`, `Idempotency`, `Cancellation`, `Admission`, `Queue`, `Job`, `Run`, `Incident`, `Reservation`, `Capability`, or `Recovery Frontier`.

## 2. Stable Execution and distinguishable Attempts

### 2.1 Execution remains the operational owner

Execution owns operational realization of one committed Learning, Generation or Evaluation occurrence.

Its identity survives ordinary same-semantics:

- worker/process replacement;
- scheduler/provider retry beneath one still-coherent Attempt;
- platform resubmission;
- cluster replacement;
- retry from start;
- validated checkpoint resume;
- coordinator/service failover;
- reconciliation of ambiguous provider state;
- recovery across a non-regressing authority frontier when the parent activity/Execution continuity can still be established.

Changing material committed semantics is never disguised as Execution recovery.

### 2.2 Attempt is immutable realization history

A distinguishable Attempt binds or references, where material:

```text
parent Execution identity
Attempt identity/history position
recovery-authority frontier in force when write authority was issued
Attempt authority epoch/generation
exact immutable 007-G invocation / implementation closure
recovery/restart/resume basis
platform/runtime correlations
material resource/dependency/runtime facts
checkpoint/candidate/diagnostic inputs and effects
observed outcome / reconciliation history
```

The exact representation is deferred.

The immutable invocation/history identity of an Attempt does not mutate when later observations clarify whether the physical work succeeded, failed, was cancelled, remained running, or became superseded. A current outcome projection may be refined by reconciliation while preserving the earlier observation/history that justified the reconciliation.

### 2.3 Provider retry versus new SYNGAN Attempt

A platform may internally retry tasks, workers or jobs while SYNGAN still treats the work as one Attempt when all material realization facts remain within the same immutable Attempt invocation/authority boundary.

A new SYNGAN Attempt is required when SYNGAN intentionally issues a new operational try or recovery decision that materially changes the operational realization boundary, such as:

- issuing new current mutation authority after a prior Attempt lost authority;
- restart from start after a failed/unknown Attempt;
- resume from a selected checkpoint;
- selecting a different compatible 007-G implementation binding for a later try;
- crossing a non-regressing recovery-authority frontier after regressive restore;
- another recovery action that must remain independently attributable.

Provider retry count is therefore not the Attempt identity or Attempt epoch.

### 2.4 Observed state and mutation authority remain separate

An Attempt may be physically `running` while already fenced from current framework mutation.

Conversely, a currently authoritative Attempt may temporarily be `unknown` from the coordinator's perspective while reconciliation is pending.

No single status enum should collapse:

```text
what the platform appears to be doing
what historical outcome is currently known
whether this Attempt may mutate current framework state
```

## 3. Non-regressing authority and fencing

### 3.1 Effective mutation authority is composite

For material framework-owned writes, architecture must be able to enforce authority equivalent to:

```text
current mutation authority
    = current recovery-authority frontier
      ∩ current Execution/Attempt authority
      ∩ current resource-local generation/precondition where required
      ∩ current action authorization/capability
```

The exact token, database, credential, lease or provider mechanism is deferred.

Not every operation needs all dimensions physically encoded in one token. The architecture requires the combined invariants, not a universal composite field.

### 3.2 Attempt epoch is scoped beneath the recovery frontier

An ordered Attempt epoch/generation remains useful for superseding Attempts within one Execution authority lineage.

However, **Attempt epoch alone is insufficient after potentially regressive control-state recovery**. A restored older database could otherwise revive an older `current_attempt_epoch` or reissue an epoch that surviving pre-restore writers can satisfy.

Therefore any architecture that uses an Attempt epoch must combine it with a post-recovery authority boundary that cannot be recreated merely by replaying the restored persistence state.

The representation may use:

- a separate recovery-frontier/incarnation identity;
- an externally monotonic generation;
- credential/namespace rotation;
- provider-native fencing;
- an equivalent non-replayable authority boundary.

007-H does not select one.

### 3.3 Lease is liveness coordination, not stale-writer safety

A lease/heartbeat may help determine which coordinator/Attempt is expected to be active.

Lease expiry, timeout or missed heartbeat does not prove that the old writer stopped. Material safety still depends on current fences/preconditions/isolation.

### 3.4 Stale writers may continue physically

A losing Attempt may still:

- consume compute;
- finish tasks;
- write Attempt-isolated scratch;
- emit logs/telemetry;
- return late provider success.

It must not regain authority to mutate current:

- Execution state;
- checkpoint head/commit authority;
- candidate membership/seal state;
- result-establishment/promotion intent;
- current recovery/admission state;
- another material framework-owned authority boundary.

### 3.5 Resource-local fencing/isolation may be stronger

Candidate manifests, checkpoint workspaces, distributed component indexes, provider transactions or other mutable surfaces may need their own generation, expected version, isolated namespace, transaction identity or equivalent protection in addition to the parent Attempt authority.

A resource-local fence refines the Attempt boundary; it does not become a new domain owner.

### 3.6 External weakly fenceable effects remain a retry boundary

A database/Attempt fence cannot retroactively stop an already-issued external effect.

If an effect cannot be queried, uniquely correlated, deduplicated, compensated, isolated or fenced strongly enough, automatic retry may remain blocked until reconciliation/operator action establishes a safe path. If safety cannot be established, indeterminacy is a truthful terminal/holding condition.

## 4. Operation-scoped idempotency

### 4.1 No universal idempotency key

Idempotency is scoped to the material command/effect boundary.

Relevant operations include:

- start/admit one intended Execution continuation;
- create/authorize one Attempt;
- submit one Attempt invocation to a provider;
- commit one checkpoint identity;
- register one candidate component/generation mutation;
- seal one exact candidate generation;
- aggregate one logical Evaluation work unit;
- establish one semantic result under the owning transition;
- request one cancellation intent;
- dispatch one durable cross-boundary intent.

### 4.2 Idempotency identity binds the intended effect

An idempotency identity must be scoped strongly enough that two materially different effects cannot be confused merely because a caller reused a convenient request string.

Depending on the operation, the identity may need to bind information equivalent to:

```text
operation role
owner / semantic target
request fingerprint or immutable intent identity
relevant representation / candidate / checkpoint generation
relevant authority context
```

This is a responsibility model, not a committed key schema.

### 4.3 Idempotency never grants stale authority

A previously accepted idempotency key, provider transaction ID, outbox identity or cancellation request ID cannot bypass a newer recovery frontier, Attempt fence, owner-state version, revocation or cancellation state.

After authority changes, the prior idempotency record may prove that an effect already happened; it does not automatically authorize performing the effect again.

### 4.4 Idempotent replay has qualified outcomes

A repeated request may resolve to outcomes equivalent to:

- same effect already established; return/reference that result;
- request is still pending/ambiguous; reconcile;
- request conflicts with a different immutable fingerprint/target;
- prior effect exists but current authorization/authority requires requalification;
- no effect established; safe to attempt under current authority;
- effect cannot be determined safely.

`same key -> blindly re-run code` is not the architecture.

### 4.5 Cross-boundary intent composes with 007-E

A durable outbox/transition intent may be delivered more than once physically.

Target acceptance uses operation-scoped idempotency plus current authority requalification where required. The existence of an old durable intent does not override later cancellation, recovery quarantine, permission revocation, dependency incompatibility or semantic-owner state.

## 5. Ordinary recovery versus potentially regressive recovery

### 5.1 Ordinary non-regressive failover

Coordinator/process failover does not require a new recovery frontier merely because a process restarted when canonical current authority is known to be non-regressed and existing fencing/current-state facts remain valid.

The replacement coordinator reconstructs current state from durable authority and continues/reconciles according to the current Attempt contract.

### 5.2 Potentially regressive restore enters quarantine

If control persistence may have been restored to an older point than surviving Attempts, cancellation, candidate/checkpoint effects, provider transactions, authorization changes, outbox delivery or semantic promotion, current mutation authority is **continuity unverified**.

During that state:

- ordinary new write-capable Attempts are not admitted;
- restored `current Attempt`/epoch rows do not grant authority;
- restored cancellation absence does not reactivate writers;
- restored authorization/capability state does not grant current sensitive access;
- candidate/checkpoint/result adoption is not based only on restored state;
- read/history surfaces qualify possible post-restore gaps truthfully.

### 5.3 Establish stale-writer exclusion before ordinary writes

Recovery first establishes a fresh non-regressing current authority boundary sufficient to exclude surviving old writers.

Only then may recovery reconcile or adopt surviving state with confidence that old authority cannot race current repair.

### 5.4 Reconciliation after regressive recovery

Recovery may inspect independent durable evidence such as:

- provider/platform correlations;
- immutable candidate/checkpoint manifests;
- external transaction identities;
- storage generations/version history;
- security/audit facts;
- retained outbox/delivery facts;
- promoted-result/provenance evidence;
- surviving runtime observations.

These observations are evidence for reconstruction/reconciliation. Their existence alone does not establish missing semantic transitions.

### 5.5 History reconstruction is owner-qualified

A missing operational/semantic transition may be reconstructed only when retained independent evidence proves the exact identity, transition and normal completion basis strongly enough under the owning authority.

Reconstruction should preserve both the historical transition being re-established and the later recovery action that reconstructed it.

Unknown/unavailable facts remain unknown/unavailable when the evidence is insufficient.

### 5.6 Immutable-effect adoption is current-authority action

A surviving immutable checkpoint/candidate/state component may be adopted/referenced after recovery only when its exact producing context, integrity, scope/completeness, semantic compatibility, security domain and conflict status can be established sufficiently.

The old producing Attempt does not regain write authority. Current recovery authority performs the adoption.

### 5.7 Same-Execution continuation is conditional

After a regressive restore, continuation under the same Execution requires sufficient continuity of:

- parent committed activity identity/snapshot;
- Execution identity/history;
- relevant Attempts/effects;
- current non-regressing authority;
- same-semantics recovery basis.

If the restored state predates a surviving Execution and its missing identity/history cannot be reconstructed strongly enough, the surviving work cannot be relabeled as an ordinary retry/resume.

## 6. Recovery decision and continuation modes

A recovery decision distinguishes at least:

```text
continue observing / reconcile current Attempt
retry from clean or isolated state
resume from a validated checkpoint
wait for admission/resource/security condition
cannot continue the same Execution safely
```

A later Attempt is issued only after the chosen path is compatible with the unchanged committed activity and side-effect history.

### 6.1 Retry from start

Retry from start does not imply reuse of prior mutable work. Prior Attempt-local or candidate effects are isolated, fenced, reused only through explicit qualified adoption, or ignored/quarantined according to their owner contract.

### 6.2 Resume

Resume intentionally reuses a committed compatible checkpoint/recovery snapshot and creates a new distinguishable Attempt/invocation.

### 6.3 Reconcile first

If prior provider/effect state is unknown enough to make duplicate work unsafe, recovery remains in reconciliation rather than manufacturing a failure solely to trigger retry.

### 6.4 Different compatible implementation on later Attempt

Consistent with 007-G, a later Attempt may use another executable binding only when the unchanged semantic commitment permits implementation-neutral realization.

Resume adds an additional requirement: the new binding/runtime closure must explicitly be compatible with the selected checkpoint representation/state semantics. A semantically compatible Strategy implementation is not automatically checkpoint-compatible.

The later Attempt always receives its own immutable exact invocation/history.

## 7. Side-effect recovery classes

007-H retains a practical architectural distinction among effects:

1. **Attempt-local / disposable** — isolated scratch or recomputable intermediate work that cannot be confused with canonical state.
2. **Framework-staged / non-final** — candidate components, checkpoint staging and partial Evaluation material under framework identity/fencing.
3. **Framework-canonical** — current Execution state, committed checkpoint reference/head, sealed representation association, semantic-owner result transitions and material history.
4. **External but deduplicable/fenceable/queryable** — provider effects with sufficient identity/version/idempotency semantics for safe recovery.
5. **External irreversible or weakly identifiable** — effects whose occurrence cannot be established/repeated safely enough for automatic continuation.

This is architecture guidance, not a new domain taxonomy.

## 8. Checkpoint foundation

### 8.1 Checkpoint is operational recovery state

A checkpoint is durable recovery material for one Execution. It is not Learned State, completed Generation output, Evidence or proof of operational completion merely because bytes exist.

### 8.2 Staging and committed checkpoint remain distinct

Distributed checkpoint creation may require several components.

Architecture preserves a boundary equivalent to:

```text
Attempt-scoped checkpoint workspace
        ↓
component/material closure + integrity
        ↓
committed immutable checkpoint identity/reference
```

Incomplete staging is not resumable merely because some files are readable.

### 8.3 Checkpoint context

A committed checkpoint must preserve or resolve enough information, where material, to establish:

- checkpoint identity;
- parent Execution;
- producing Attempt and authority frontier/epoch context;
- exact committed activity/snapshot;
- exact or declared-compatible Strategy/method/runtime binding context;
- state representation/codec identity;
- source/input/subject and Learned-State/direct-generation basis;
- dependency/base-artifact identities;
- represented progress/completion scope;
- randomness/nondeterminism continuation facts;
- candidate/output side effects already represented;
- distributed component/manifest identity and integrity basis;
- representation schema/compatibility requirements.

Secret values, reusable bearer capabilities and ambient credentials are excluded from checkpoint payload/history under 007-G.

### 8.4 Checkpoint identity survives producer authority loss

A committed immutable checkpoint may remain valid data after its producing Attempt is fenced or after recovery crosses to a fresh authority frontier.

Its **use** still requires current resume qualification/adoption. The producer's old write authority is never transferred with the checkpoint.

### 8.5 Resume compatibility is contextual

Checkpoint existence/integrity and resume eligibility remain separate.

A current assessment may conclude:

- eligible to resume;
- eligible with explicit operational limitations compatible with the commitment;
- restart required;
- incompatible with the same Execution realization;
- indeterminate/reconciliation required.

### 8.6 No cross-activity masquerading

A checkpoint from one committed activity cannot be called a resume checkpoint for another activity.

If future design permits a new activity to consume prior operational state as an explicit input/seed, that is a new derivation/reference contract, not same-Execution resume.

### 8.7 Distributed boundedness

Large checkpoint payloads/components remain distributed data-plane state. Control state retains bounded identities/manifests/references rather than collecting all components or model state to the driver/coordinator.

## 9. Cancellation foundation

### 9.1 Cancellation is durable intent before terminal outcome

Cancellation records a durable current request against the relevant Execution state/authority boundary before assuming the platform stopped.

Repeated equivalent cancellation requests are idempotent.

### 9.2 Cancellation blocks ordinary new admission

Once cancellation is accepted as current intent, ordinary new Attempts must not be admitted/authorized merely because queued work, retry policy or an old outbox message still exists.

Work that has not yet acquired Attempt/write authority may be removed/withdrawn from admission without fabricating a physical Attempt merely to cancel it.

### 9.3 In-flight Attempts are stopped and/or fenced

The platform/runtime adapter should attempt to stop current physical work where supported.

Independent of best-effort physical stop, current framework mutation authority is revoked/advanced/fenced as required so late work cannot silently mutate current canonical state after cancellation takes effect.

### 9.4 Late success is historical fact, not regained authority

A provider may report success after cancellation was requested or after its Attempt was fenced.

That observation may refine the Attempt's historical physical outcome. It does not automatically authorize checkpoint head mutation, candidate sealing, Learned State establishment, Evidence establishment or Generation promotion.

### 9.5 Regressive restore cannot erase cancellation authority

If a restore point predates cancellation, the missing restored cancellation row does not reactivate old write authority.

Fresh recovery-frontier establishment excludes stale work first; cancellation history is then reconciled/reconstructed to the degree independent evidence supports it.

### 9.6 Cancellation is not silently reversible

A stale retry/resume request cannot `uncancel` an Execution.

If future current authority permits continuation after a non-terminal cancellation race or explicit administrative recovery rule, that continuation is a new qualified transition under current state, authorization, recovery and admission rules—not revival of the old Attempt.

### 9.7 Terminal classification remains truthful

After reconciliation, operational state may resolve to cancelled, completed-before-cancellation, failed-while-cancelling or indeterminate.

The parent Learning/Generation/Evaluation remains responsible for its semantic terminal state.

## 10. Admission foundation

### 10.1 Admission is operational eligibility

Admission answers whether a prepared/recoverable Execution continuation may begin material work **now** in a particular deployment/runtime context.

It is downstream of semantic commitment and must not become a second semantic readiness concept.

Admission is distinct from:

```text
semantic readiness / commitment
current action authorization
007-G executable/dependency/runtime closure
recovery-continuity verification
resource/capacity availability
queue/scheduler placement
Attempt write authority
```

A single implementation may evaluate several of these together, but their reasons and authority remain distinguishable.

### 10.2 Admission inputs

Where material, admission requalifies facts equivalent to:

- Execution is still startable/recoverable under the same committed activity;
- no current cancellation/terminal state forbids start;
- recovery continuity is verified and the current non-regressing authority frontier is valid;
- exact intended 007-G invocation/dependency/runtime closure can be satisfied;
- current authorization, secret resolution and network/egress posture permit the intended action;
- required source/checkpoint/candidate references remain resolvable and compatible;
- deployment/platform capabilities satisfy required guarantees;
- resource class/capacity/quota/concurrency envelope is currently available or reservable;
- applicable operational deadline/budget/policy constraints allow start.

Admission must not reinterpret the domain commitment merely because resources are scarce.

### 10.3 Admission outcomes preserve cause

Architecture should preserve outcomes equivalent to:

- admitted / currently eligible to proceed;
- queued/deferred/waiting for capacity or policy window;
- blocked by current authorization/security/dependency state;
- incompatible because required guarantees cannot be provided;
- reconciliation/recovery qualification required;
- indeterminate because required current facts cannot be established;
- cancelled/terminally ineligible.

Resource shortage is not automatically semantic incompatibility. Conversely, a deployment that cannot ever provide a required guarantee must not queue forever while pretending the workload is merely waiting.

### 10.4 Admission may expire or be revoked before launch

Admission is a current contextual decision, not perpetual permission.

If material state changes between admission and Attempt launch/write-authority establishment—such as cancellation, authorization revocation, recovery-frontier change, dependency drift, resource loss or platform capability change—the operation must requalify rather than rely on a stale queue/admission record.

### 10.5 Queue position and reservation are not write authority

A queue ticket, scheduling reservation, semaphore slot, resource claim or provider placement decision may coordinate capacity.

None grants permission to mutate framework-owned canonical state or bypass current fencing/authorization.

### 10.6 Attempt authority is established only after current admission qualification

Architecture permits a durable Attempt record to be prepared before provider submission if useful for crash consistency and correlation.

However, the transition that makes an Attempt current/write-capable must occur only after current admission/recovery/authorization/invocation prerequisites are satisfied and must be concurrency protected under 007-E.

If an Attempt record was prepared but never became authoritative/launched, history may retain that fact without pretending material execution occurred.

### 10.7 Dynamic worker admission is role-specific closure

Within one distributed Attempt, newly added/replaced workers must satisfy their 007-G role-specific executable/dependency/security closure before receiving material work.

Worker replacement that preserves the same immutable Attempt invocation and authority boundary need not create a new Attempt merely because a process changed. A change that crosses the Attempt's exact realization/recovery boundary requires a new Attempt.

### 10.8 Admission policy details remain deployment concerns

Fairness, priority, quota formulas, preemption, reservation duration, queue implementation and cost optimization remain deferred unless later product requirements make them semantic/experience authority.

## 11. Launch and crash-consistency boundary

### 11.1 Admission/start sequence

A valid architecture sequence is equivalent to:

```text
1. committed activity / Execution exists
2. record or identify start/recovery intent idempotently where needed
3. evaluate current admission + recovery continuity + authorization + runtime closure
4. concurrency-protect establishment of current Attempt identity/authority under the current recovery frontier
5. persist immutable Attempt invocation + durable launch intent/correlation identity
6. submit to provider/runtime with available idempotency/correlation support
7. persist returned provider reference when available
8. reconcile if coordinator/client fails across steps 5-7
```

The exact placement of Attempt-record creation around steps 3-5 may vary, but no queued/prepared record gains write authority before the current prerequisites pass.

No global transaction with an external scheduler is required.

### 11.2 Submission acknowledgement loss does not imply failure

If the provider accepted work but SYNGAN lost the acknowledgement, the Attempt may become submission-unknown.

Recovery uses durable launch intent/correlation/provider discovery before deciding whether another physical submission is safe.

### 11.3 Duplicate provider work remains physically possible

When provider deduplication cannot guarantee one physical launch, duplicate jobs may run.

They still share or map to the intended Attempt correlation according to the adapter contract, and only current fenced framework effects may become canonical.

## 12. Candidate / Learned State / Evaluation integration

### 12.1 Generation candidate integration

007-F candidate materialization composes with 007-H authority as follows:

```text
Execution
  ↓
current Attempt / recovery frontier
  ↓
Attempt-scoped or resource-fenced candidate writes
  ↓
reconcile partial effects after failure/unknown
  ↓
new admitted Attempt when needed
  ↓
exact whole-candidate seal
  ↓
required semantic Evaluation/Evidence
  ↓
Generation-owned promotion
```

Candidate seal requires resolved authoritative-writer ambiguity for the generation being sealed.

### 12.2 Learning integration

Checkpoint/recovery state remains distinct from a candidate final Learned-State representation and from an established Learned State.

Only Learning's owner-side transition can establish the primary Learned State. A stale runtime cannot do so merely because it produced durable model bytes.

### 12.3 Evaluation integration

Recovered/retried partial Evaluation work must preserve logical work-unit/coverage identity strongly enough to avoid accidental duplicate aggregation.

Repeated computation is allowed; repeated contribution to the same logical observation/coverage unit is not assumed valid unless the method explicitly defines it.

Runtime method result remains distinct from established Evidence.

### 12.4 Single semantic promotion remains the objective

Operational recovery ensures physical retries cannot manufacture multiple authoritative semantic results for one committed activity.

Attempt/provider success alone never creates:

- a Learned State;
- a completed Generation output;
- Evidence;
- external release approval.

## 13. Regressive-recovery interaction with semantic promotion

A restored control store may predate a semantic promotion that could have happened externally or in another surviving durable boundary.

Recovery therefore must not:

- assume the missing promotion never occurred;
- blindly promote surviving bytes a second time;
- infer promotion merely from sealed/complete-looking physical material.

Current authority reconciles/reconstructs the owning transition only when retained evidence proves its normal completion basis strongly enough. Otherwise current knowledge remains unresolved.

This preserves both single-result cardinality and historical truth.

## 14. Persistence and bounded operational history

Canonical control persistence should retain or durably reference bounded facts equivalent to:

- Execution identity/current operational state/state version;
- continuity/recovery-quarantine state where material;
- current recovery-authority frontier identity/status;
- current Attempt identity/authority context;
- immutable Attempt records/invocation references;
- launch intents/provider correlations;
- material admission/start/recovery decisions;
- checkpoint identities/recovery bases;
- cancellation request/outcome;
- reconciliation/reconstruction/adoption decisions;
- structured failure/retryability summaries;
- material candidate/result-transition correlations needed for safe recovery;
- historical/provenance references.

The non-regressing frontier mechanism may require authority outside the restored database. Persisting a frontier identifier does not by itself satisfy the stale-writer-exclusion contract if replaying the restored bytes can recreate the authority.

Detailed platform task/stage logs, executor heartbeats and fine-grained telemetry remain non-canonical platform/observability data unless a specific material fact must be promoted into bounded operational history.

## 15. Failure and retryability dimensions

007-H does not freeze a public exception hierarchy.

Operational failure/history must be able to preserve dimensions sufficient to distinguish, where material:

- failure category/source;
- current retryability and basis;
- same-semantics continuation possibility;
- side-effect ambiguity;
- recovery-continuity status;
- checkpoint availability/compatibility;
- current admission/resource state;
- dependency/security/network implications;
- platform/provider correlation/error facts;
- actor-safe summary and protected diagnostic reference.

`provider says retryable` is not sufficient evidence that same-Execution retry is safe.

## 16. Security boundary

Start, admit, retry, resume, reconcile, adopt, cancel, inspect protected diagnostics and perform semantic promotion are independently authorization-sensitive actions where applicable.

Important consequences:

- historical permission does not become current permission;
- idempotency keys and fencing tokens are not generic bearer credentials;
- long-lived typed handles do not carry ambient operational authority;
- secret values do not enter Attempt invocation history/checkpoints/provenance merely for reproducibility;
- regressive recovery re-evaluates current sensitive authorization and may require credential/capability rotation to enforce stale-writer exclusion;
- admission/security denial may need disclosure-safe outward representation while retaining precise internal cause.

## 17. Scale and distributed-operation rules

Execution/Attempt canonical state scales with logical Attempts and material transitions, not every worker/task/row.

007-H preserves support for:

- hours/days-long work;
- coordinator/service restart;
- cluster replacement;
- millions of Spark tasks beneath one Attempt;
- dynamic worker replacement/admission;
- large distributed checkpoints/candidates referenced through bounded manifests;
- bounded progress/health aggregation;
- admission/queue systems that need not move source/output/model payload through the control plane;
- no ordinary requirement to collect complete checkpoint/candidate/task state to driver memory.

Admission/resource pressure may delay or reject material work without redefining semantic truth.

## 18. Falsification scenarios reviewed

007-H was checked against at least these scenarios:

1. a caller repeats `start` after losing the response;
2. the external platform accepts a submission but the coordinator dies before persisting the returned run ID;
3. an old Attempt pauses, its lease expires, a newer Attempt becomes current, and the old process resumes;
4. a backup from before the newer Attempt is restored while that newer Attempt still runs;
5. the restored backup also predates a cancellation request;
6. immutable checkpoint components survive a regressive restore while their producing Attempt no longer has current authority;
7. a remote irreversible side effect may or may not have occurred and the provider cannot query/deduplicate it;
8. a later compatible implementation binding is available but cannot consume the prior checkpoint format safely;
9. a dynamic worker joins with a missing/untrusted native dependency;
10. admission is denied temporarily because accelerator/capacity quota is exhausted;
11. admission passed, then authorization is revoked before launch;
12. cancellation occurs while work is queued but before any write-capable Attempt exists;
13. a fenced/cancelled provider job later reports success;
14. repeated Evaluation shard work returns the same logical observation twice;
15. a stale Attempt writes after the candidate generation was superseded/sealed;
16. a restore loses canonical evidence of an earlier semantic promotion while physical output survives;
17. worker replacement occurs inside one Attempt with unchanged invocation/closure and no recovery-boundary change;
18. a resource shortage is temporary versus a platform that can never satisfy a required semantic/runtime guarantee.

The architecture remains coherent without a new concept, synchronization or ADR.

## 19. Architecture invariants

1. One operationalized committed activity has one stable primary Execution identity under the current model.
2. A valid retry/resume preserves the exact committed activity semantics.
3. Material same-Execution re-realization requiring a new recovery decision/authority receives a distinguishable Attempt.
4. Platform task/job/run identity never replaces Execution or Attempt identity.
5. Attempt invocation/executable closure is immutable for that Attempt.
6. Attempt observed physical state and current framework mutation authority remain separate.
7. Exactly-once physical computation is not required.
8. Duplicate physical work must not create ambiguous duplicate canonical semantic results.
9. Lease/heartbeat expiry alone is insufficient stale-writer protection.
10. Attempt epoch alone is insufficient stale-writer protection after potentially regressive restore.
11. Potentially regressive recovery establishes a fresh non-regressing authority boundary before ordinary write-capable operation resumes.
12. Restored state cannot resurrect a previously superseded Attempt/capability/cancellation authority.
13. Old writers may continue physically but cannot regain current canonical mutation authority.
14. Resource-local fencing/isolation may strengthen Attempt fencing without becoming semantic ownership.
15. Idempotency is scoped to an intended operation/effect and does not replace fencing/current authorization.
16. A prior idempotency record may prove a past effect but cannot grant stale authority after the current authority changes.
17. Unknown provider/side-effect state remains explicit until reconciled or safely isolated/fenced.
18. Weakly identifiable irreversible external ambiguity may block automatic retry.
19. Checkpoint existence does not imply committed checkpoint integrity or resume eligibility.
20. Committed checkpoints are immutable recovery state bound to exact sufficient context.
21. Producer Attempt authority does not transfer with a checkpoint across fencing/recovery-frontier change.
22. Cross-activity checkpoint use cannot masquerade as same-Execution resume.
23. A different later implementation binding requires both unchanged semantic compatibility and, for resume, checkpoint compatibility.
24. Cancellation request is durable intent distinct from terminal cancellation.
25. Accepted cancellation blocks ordinary new admission/Attempt issuance until a current explicit rule permits otherwise.
26. Late provider success after cancellation/fencing does not restore semantic-promotion authority.
27. Regressive restore cannot erase cancellation merely by restoring a pre-cancellation row set.
28. Admission is current operational eligibility, not semantic readiness or write authority.
29. Queue position/reservation does not grant mutation authority.
30. Material admission prerequisites are requalified when stale/current-state change can invalidate them.
31. Temporary resource shortage remains distinguishable from true incompatibility.
32. Dynamic workers prove role-specific closure before material work.
33. Candidate sealing requires resolved writer authority and exact immutable representation closure.
34. Execution operational completion never establishes Learning/Generation/Evaluation semantic completion by itself.
35. Regressive recovery cannot infer or repeat missing semantic promotion solely from surviving physical material.
36. Canonical operational history remains bounded and does not become a shadow platform telemetry store.
37. Ordinary recovery/checkpoint/admission handling must not require full distributed payload collection to the driver/coordinator.
38. Recovery/admission may not silently enable network access, dependency substitution or semantic weakening.

## 20. Phase 005-G implementation-planning disposition

007-H retains the responsibility intent of the Phase 005-G plan, including:

- stable Execution identity with many distinguishable Attempts;
- separate Attempt observed state and mutation authority;
- fencing stronger than leases;
- durable launch intent/correlation and reconciliation;
- operation-scoped idempotency;
- immutable committed checkpoint and resume qualification;
- explicit restart/resume/reconcile/cannot-continue recovery decisions;
- durable cancellation intent;
- semantic completion distinct from operational completion.

007-H reclassifies the following as implementation candidates rather than current architecture requirements:

- concrete `ExecutionHandle`, `AttemptRef`, `AttemptEpoch`, `WriterFence`, `CheckpointRef`, `RecoveryDecision`, `LaunchIntent` type names;
- specific `ResourceKind` additions for Attempt/runtime invocation/checkpoint;
- `AttemptEpoch` as specifically a positive integer starting at one;
- exact `ExecutionState` / `AttemptObservedState` enum spelling;
- specific `src/syngan/domain|ports|application|api|adapters` execution package layout;
- SQL-oriented execution-record repository spelling;
- concrete repository/port/service interfaces;
- exact persistence field/table/index design;
- concrete launch, checkpoint, lease, idempotency and reconciliation implementation choices.

The stronger 007-H requirement is semantic/authority separation, including the non-regressing recovery frontier that prevents a restored Attempt epoch from resurrecting stale authority.

## 21. Explicitly deferred

007-H intentionally does not select:

- scheduler/orchestrator/queue;
- fairness/priority/preemption/admission algorithm;
- quota/resource-reservation implementation;
- database/ORM/event store;
- lock or lease service;
- lease duration/heartbeat interval;
- recovery-frontier/incarnation encoding/provider;
- Attempt epoch/fencing-token encoding;
- capability-token format;
- resource-local fence/CAS provider;
- idempotency key/storage implementation;
- retry/backoff/attempt-limit values;
- checkpoint file/table/object/manifest format;
- checkpoint retention/garbage collection;
- platform launch API/provider mapping;
- exact failure/exception hierarchy;
- dead-letter/incident system;
- exact cancellation protocol;
- exact recovery/reconstruction/adoption workflow UI/API;
- cost/budget admission policy;
- security/IAM/secret product;
- metrics/logging/tracing backend;
- execution/recovery/admission tests or executable enforcement.

## 22. Repository change boundary

007-H changes architecture/documentation only.

It introduces:

- no Execution/Attempt production source behavior;
- no persistence schema or migration;
- no queue/scheduler/launcher adapter;
- no lock/lease/fencing implementation;
- no checkpoint backend/format;
- no retry/cancellation implementation;
- no admission/resource manager;
- no new dependency;
- no new test;
- no Import Linter rule;
- no CI/deployment enforcement.

The retained Phase 007-A through 007-C executable scaffold remains provisional feasibility/history evidence.

## 23. Concept / synchronization / ADR audit

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
new concepts               0
new synchronizations       0
new ADRs                    0
SYNC-16                     absent
```

Attempt, recovery frontier, fence, idempotency, checkpoint, cancellation and admission remain subordinate Execution/architecture mechanisms.

ADR-0002, ADR-0007 and ADR-0009 remain sufficient; 007-H composes/refines their consequences rather than superseding them.

## 24. Exit decision

**007-H DESIGN: COMPLETE.**

**007-H IMPLEMENTATION: NOT AUTHORIZED.**

The next eligible **design** subgroup is:

**007-I — Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation**.

007-I does not begin automatically; explicit proceed authority is required.
