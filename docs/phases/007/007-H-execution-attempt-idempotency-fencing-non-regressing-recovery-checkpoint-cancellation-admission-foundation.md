---
type: Phase Record
title: 007-H — Execution/Attempt, Idempotency, Fencing, Non-Regressing Recovery, Checkpoint, Cancellation & Admission Foundation
status: complete
---

# 007-H — Execution/Attempt, Idempotency, Fencing, Non-Regressing Recovery, Checkpoint, Cancellation & Admission Foundation

## Objective

Refine the operational-realization architecture beneath 007-D identity, 007-E persistence, 007-F distributed data state and 007-G executable/runtime closure without allowing historical Phase 005-G planning or the provisional 007-A through 007-C scaffold to freeze execution types, scheduler/queue technology, fencing encodings, checkpoint formats, retry policy, admission algorithms or executable checks prematurely.

007-H remains architecture/design work under the Phase 007 implementation freeze.

## Governing authority reviewed

007-H reconciled and refined:

- `docs/concepts/execution.md`;
- `docs/experience/execution-monitoring-failure-recovery-cancellation.md`;
- `docs/authority/operational-authority-continuity-regressive-recovery-contract.md`;
- `docs/authority/enterprise-scale-resource-admission-approximation-degraded-operation-contract.md`;
- 007-D through 007-G architecture authorities;
- `docs/architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md`;
- `docs/architecture/deployment-scalability-observability-portability-compatibility-platform-integration.md`;
- ADR-0002, ADR-0007 and ADR-0009;
- the historical Phase 005-G implementation plan as downstream feasibility/planning evidence.

## Result

**PASS — EXECUTION / ATTEMPT / IDEMPOTENCY / FENCING / NON-REGRESSING RECOVERY / CHECKPOINT / CANCELLATION / ADMISSION FOUNDATION REFINED AS ARCHITECTURE DESIGN.**

Canonical result:

`docs/architecture/phase-007-h-execution-attempt-idempotency-fencing-non-regressing-recovery-checkpoint-cancellation-admission-foundation.md`

## Core separation

007-H preserves this operational authority chain:

```text
committed Learning / Generation / Evaluation
        ↓
stable logical Execution
        ↓
current admission + recovery-continuity qualification
        ↓
current non-regressing recovery-authority frontier
        ↓
current Attempt authority + resource-local preconditions
        ↓
immutable Attempt invocation / exact 007-G realization
        ↓
physical runtime work
        ↓
checkpoint / candidate / method-result effects
        ↓
reconciliation / owner validation
        ↓
at-most-one authoritative semantic result transition
```

Provider job identity, queue position, lease ownership, physical success and persisted bytes remain subordinate operational facts rather than semantic authority.

## Execution and Attempt

Execution remains one stable logical operational identity for one committed activity under the current model.

Attempt remains subordinate operational history. A material retry/resume/re-realization requiring new current mutation authority receives a distinguishable Attempt, while provider-internal worker/task retry may remain within one Attempt when its immutable invocation and authority boundary do not change.

Attempt physical/observed state is distinct from current framework mutation authority. An old Attempt can still be physically running after it is fenced.

## Fencing and non-regressing authority

007-H retains Attempt epochs/generations as useful same-Execution ordering, but rejects them as sufficient after potentially regressive restore.

Material write authority must compose the current recovery-authority frontier, current Execution/Attempt authority, resource-local write preconditions where needed, and current authorization/capability.

Potentially regressive restore enters continuity-unverified recovery quarantine. A fresh non-regressing authority boundary is established before ordinary write-capable work resumes. Restored rows, old leases, prior credentials or stale Attempt epochs cannot resurrect superseded authority.

Old writers may continue physically but cannot mutate current framework-owned authority once fenced.

## Idempotency

Idempotency remains operation-scoped rather than one universal key.

Material scopes include Attempt start/authorization, provider launch, checkpoint commit, candidate mutation/seal, Evaluation work-unit aggregation, semantic promotion, cancellation and durable cross-boundary intent.

A prior idempotency record may establish that an effect already happened; it does not override newer fencing, cancellation, authorization, owner-state or recovery-frontier authority.

## Recovery and reconciliation

007-H distinguishes ordinary non-regressive failover from potentially regressive persistence restore.

Recovery chooses explicitly among continued observation/reconciliation, retry from clean or isolated state, resume from a validated checkpoint, waiting for current admission/resource/security conditions, or inability to continue the same Execution safely.

Unknown provider/side-effect state remains explicit. Weakly identifiable irreversible external ambiguity may block automatic retry rather than being guessed away.

After regressive recovery, surviving immutable effects may be adopted only by current authority after exact producing context, integrity, scope, compatibility, conflict status and security conditions are established sufficiently. The old producer never regains authority merely because its bytes survived.

## Checkpoint

Checkpoint remains operational recovery state, not Learned State, completed Generation output or Evidence.

Distributed checkpoint staging is distinct from committed immutable checkpoint identity.

Resume compatibility is contextual and binds enough exact activity, Execution, invocation/runtime, source/state, dependency, representation, progress, randomness and candidate-effect context to preserve same-semantics continuation.

A committed checkpoint may survive producer fencing/recovery-frontier change, but its later use requires current qualification. Producer write authority does not travel with checkpoint bytes.

A later implementation binding may be semantically compatible yet still checkpoint-incompatible.

## Cancellation

Cancellation remains durable intent before terminal outcome.

Accepted cancellation blocks ordinary new admission/Attempt issuance, attempts best-effort physical stop, and fences/advances current mutation authority as needed so late work cannot silently mutate canonical state.

Late provider success is a historical operational fact, not renewed promotion authority.

Regressive restore cannot undo cancellation simply because the restored snapshot predates its request.

## Admission

007-H adds explicit architecture for operational admission.

Admission asks whether an Execution continuation may begin material work now under the exact committed activity and current environment.

It remains distinct from semantic readiness, current authorization, executable/runtime closure, recovery continuity, resource availability, scheduler placement and Attempt write authority.

Admission may depend on current recovery continuity, cancellation/terminal state, 007-G runtime closure, authorization/security/network posture, reference/checkpoint compatibility, platform guarantees and resource/quota/capacity envelope.

Admission outcomes preserve reason: admitted, queued/deferred, blocked, incompatible, recovery/reconciliation required, indeterminate or terminally ineligible.

Temporary resource shortage is not semantic incompatibility. Queue position/reservation is not write authority. Material admission must be requalified when current state changes before launch.

Dynamic workers must independently satisfy their 007-G role-specific closure before receiving material work.

## Crash-consistency / launch boundary

007-H retains durable start/launch intent and correlation rather than assuming an external scheduler transaction.

If provider submission succeeds but acknowledgement is lost, the Attempt becomes submission-unknown and is reconciled using durable correlation/provider evidence before blind resubmission.

Duplicate provider work may remain physically possible; current fencing/idempotency prevents duplicate canonical authority.

## Semantic owner integration

Generation candidate sealing requires resolved writer authority and exact immutable closure. Learning result establishment remains owner-controlled. Evaluation retry/recovery must not double-count repeated logical work units accidentally.

Execution/Attempt success never by itself creates Learned State, completed Generation output, Evidence or release approval.

Regressive recovery likewise cannot infer or repeat a missing semantic promotion solely from surviving physical material.

## Phase 005-G technology disposition

Earlier planning proposed concrete implementation choices including:

- `ExecutionHandle`, `AttemptRef`, `AttemptEpoch`, `WriterFence`, `CheckpointRef`, `RecoveryDecision`, `LaunchIntent`;
- concrete `ResourceKind` additions;
- positive integer Attempt epochs beginning at one;
- concrete Execution/Attempt enums;
- specific domain/ports/application/api/adapters package layout;
- SQL-oriented persistence repository spelling and concrete ports/services.

007-H retains their responsibility intent but reclassifies these names/shapes as implementation candidates to reassess only at explicit implementation re-entry.

## Concept / synchronization / ADR audit

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

ADR-0002, ADR-0007 and ADR-0009 remain sufficient.

## Explicitly deferred

007-H intentionally does not select:

- scheduler/orchestrator/queue;
- admission fairness/priority/preemption algorithm;
- quota/resource reservation implementation;
- database/ORM/event store;
- lock/lease service or heartbeat interval;
- recovery-frontier/incarnation provider/encoding;
- Attempt epoch/fence encoding;
- idempotency key/storage mechanism;
- retry/backoff/attempt limits;
- checkpoint backend/format/retention;
- provider launch mapping;
- exact failure/exception hierarchy;
- cancellation protocol;
- recovery/reconstruction/adoption API/UI;
- security/IAM/secret products;
- execution/recovery/admission tests or executable enforcement.

## Repository change boundary

007-H changes architecture/documentation only.

It introduces no production source behavior, persistence schema, scheduler/queue adapter, fencing/lease implementation, checkpoint backend, retry/cancellation behavior, admission manager, dependency, test, Import Linter rule or CI/deployment enforcement.

The retained Phase 007-A through 007-C scaffold remains provisional implementation evidence.

## Exit decision

**007-H DESIGN: COMPLETE.**

**007-H IMPLEMENTATION: NOT AUTHORIZED.**

The next eligible **design** subgroup is:

**007-I — Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation**.

007-I does not begin automatically; explicit proceed authority is required.
