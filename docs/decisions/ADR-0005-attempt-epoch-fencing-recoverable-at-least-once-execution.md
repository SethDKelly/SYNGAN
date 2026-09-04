---
type: Architecture Decision Record
title: ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution
status: active
---

# ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution

## Decision context

SYNGAN must tolerate distributed retries, coordinator loss, overlapping platform work, partial writes, checkpoints, and cancellation races while preserving one logical Execution and at most one authoritative semantic result.

Exactly-once physical execution is generally unavailable or unnecessarily restrictive across Spark, distributed ML, external schedulers, object/table storage, and optional remote services. Conversely, simple leases or scheduler retry flags cannot prevent a paused/stale writer from waking after recovery and mutating current candidate/checkpoint/control state.

The architecture therefore needs a portable operational model that accepts duplicate physical work while making canonical mutations unambiguous and recoverable.

## Governing authority

- [Execution](../concepts/execution.md)
- [Execution Monitoring, Failure, Recovery & Cancellation Experience](../experience/execution-monitoring-failure-recovery-cancellation.md)
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md)
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md)
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md)

## Decision

SYNGAN adopts an operational model equivalent to **at-least-once physical realization with Attempt-epoch fencing, scoped idempotency, and explicit reconciliation**.

Each write-capable Attempt belongs to one stable logical Execution and receives a supersedable ordered Attempt epoch/fencing generation. Framework-owned material mutations validate current epoch/preconditions so a newer Attempt can invalidate older write authority even when old processes remain alive.

Leases may coordinate liveness but are not sufficient as write safety by themselves.

Checkpoint snapshots are immutable recovery state bound to exact Execution/activity/runtime/dependency context. Resume eligibility is contextual and must be established before reuse.

Unknown platform/side-effect state remains explicit. A newer Attempt is started only when prior effects are safely fenced, deduplicated, reconciled, or otherwise classified sufficiently. External effects that cannot be fenced/query/deduplicated may block automatic retry.

Idempotency is operation-scoped rather than one global token. Semantic result establishment/promotion remains owner-side and at-most-once in authority even when computation is repeated.

Cancellation is durable intent followed by reconciliation to an actual operational outcome; it is not an instantaneous rewrite of Execution or domain state.

## Alternatives considered

### 1. Exactly-once physical execution

Rejected as a universal requirement because Spark/distributed runtimes may legitimately retry/speculate/recompute and many external systems cannot guarantee exactly-once computation. SYNGAN needs single semantic authority, not single physical execution.

### 2. Lease-only exclusive execution

Rejected because an expired/partitioned worker can later resume. Lease expiry proves liveness expectations, not that stale writes are impossible. Fencing/precondition checks are still required at material mutation boundaries.

### 3. One global distributed lock for an entire Execution

Rejected as a universal architecture because it couples SYNGAN to a lock service, can impede distributed work, and still does not solve external effects after lock loss unless receivers validate fencing/idempotency. Resource-local coordination may use locks when appropriate.

### 4. Scheduler-native retry/run identity as authority

Rejected because provider retry semantics vary and platform runs do not own SYNGAN committed semantics, candidate membership, checkpoint validity, or semantic promotion.

### 5. Last-writer-wins recovery

Rejected because stale Attempts could overwrite newer recovery state or candidate/control records and make history/canonical result ambiguous.

### 6. Checkpoint file existence implies resume

Rejected because checkpoint compatibility depends on commitment, Strategy/method, implementation binding, codec, dependency, integrity, progress scope, and other contextual facts.

### 7. Assume unknown Attempt means failed

Rejected because a side effect or platform submission may actually have succeeded. Retrying from that assumption can duplicate externally visible effects or corrupt candidate membership.

### 8. One universal idempotency key per Execution

Rejected because launch, checkpoint commit, candidate seal, Evaluation aggregation, cancellation, and semantic promotion have different target identities/preconditions. Idempotency must be scoped to the operation being protected.

## Consequences

### Positive

- retries/speculation/recomputation remain compatible with Spark-scale execution;
- stale writers can be rejected after recovery without requiring old processes to terminate cleanly first;
- coordinator loss does not force false success/failure classification;
- checkpoints can support resume without becoming semantic results;
- platform duplicate submission can be detected/reconciled rather than becoming new Execution identity;
- candidate sealing and semantic promotion can remain at-most-once in authority;
- cancellation races preserve actual history rather than rewriting it;
- architecture remains portable across schedulers/storage providers that expose different coordination primitives.

### Costs

- mutable side-effect adapters must carry/check Attempt epoch or equivalent fencing context;
- recovery requires durable Attempt/invocation/correlation/checkpoint identity;
- external services without idempotency/query/fencing may require manual reconciliation or remain indeterminate;
- implementation tests must cover stale writer, crash-window, duplicate launch, cancellation, and double-counting races;
- checkpoint compatibility and idempotency contracts add explicit state beyond a simple retry counter.

## Compatibility / migration impact

There is no implemented Execution architecture to migrate yet.

Future persistence/runtime APIs must reserve distinct fields/contracts for Execution identity, Attempt identity, Attempt epoch/fence, state-version concurrency, operation-scoped idempotency, checkpoint identity, and platform correlation. They must not overload platform job IDs or one generic `version`/`retry_id` value for all of these roles.

## Canonical architecture affected

- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md)

## Supersession

Supersedes: none.

Superseded by: none.
