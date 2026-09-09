---
type: Experience Contract
title: Phase 006 Recovery, Security, Degraded, Historical & Topology Experience Contract
status: active
---

# Phase 006 Recovery, Security, Degraded, Historical & Topology Experience Contract

## Purpose

Extend the [Phase 003 Consolidated Experience Contract](phase-003-consolidated-experience-contract.md) with the actor-visible and programmatic experience obligations discovered during Phase 006 post-planning design validation.

This contract covers recovery continuity, resource/admission states, runtime-distribution closure, authorization/disclosure, privacy/release boundaries, historical uncertainty, structured-data topology and the interaction among those concerns.

It does **not** introduce a new Workflow, Experience, Status, Recovery, Security, Privacy, Topology, Relationship, DegradedMode, Actionability or History concept, and it does not select a final UI, SDK, REST, CLI or storage representation.

## Governing authority

This experience contract is downstream of:

- [Phase 003 Consolidated Experience Contract](phase-003-consolidated-experience-contract.md);
- [Operational Authority Continuity & Regressive Recovery Contract](../authority/operational-authority-continuity-regressive-recovery-contract.md);
- [Self-Contained Execution & Runtime Distribution Closure Contract](../authority/self-contained-execution-runtime-distribution-closure-contract.md);
- [Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract](../authority/enterprise-scale-resource-admission-approximation-degraded-operation-contract.md);
- [Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract](../authority/privacy-disclosure-formal-guarantee-release-boundary-contract.md);
- [Structured-Data Topology & Relationship Semantics Contract](../authority/structured-data-topology-relationship-semantics-contract.md);
- [Core Synchronizations](../synchronizations/core-synchronizations.md).

Where this contract refines a Phase 003 experience statement, the Phase 006 refinement governs current experience design without rewriting the historical Phase 003 record.

## Governing experience rule

> **Every human or programmatic surface must make it possible to distinguish what is semantically true, what is operationally happening, whether the requested action can proceed now, whether current authority is trustworthy, what the actor is allowed to know, and how complete the historical knowledge is—without collapsing those questions into one status, Boolean, exception string or platform state.**

## Orthogonal experience dimensions

The experience composes several dimensions that can vary independently.

A surface may present them compactly, but it MUST preserve the distinction among at least:

1. **owner semantic state** — Learning, Generation, Evaluation, Evidence, Learned State or other owning-concept state;
2. **operational state** — Execution/Attempt realization, progress, failure, cancellation or reconciliation;
3. **current actionability** — whether the requested next action can proceed now and why;
4. **authority continuity** — whether current write/promote/cancel authority is established after recovery;
5. **compatibility/limitation** — whether the selected Strategy/method/topology/deployment can realize the requested semantics;
6. **disclosure state** — what the current actor may know or inspect;
7. **historical-knowledge state** — whether the system can establish the relevant past facts completely, partially, through reconstruction, or not at all.

These are not required universal enums. They are semantic axes that later representation must preserve.

### Example composition

A valid experience may communicate:

```text
Generation: committed
Execution: waiting for capacity
Actionability: queued; no semantic blocker
Authority continuity: established
Strategy/topology compatibility: compatible
History: complete through current state
```

Another may communicate:

```text
Generation: fulfilling
Execution: recovery pending
Actionability: write-capable actions restricted
Authority continuity: unverified after restore
Historical knowledge: post-backup interval incomplete
Candidate material: present but non-final
```

Neither case should be reduced to a generic `pending` or `degraded` status.

## Actionability experience

### Runnable / ready now

The relevant semantic, policy, dependency, runtime and authority requirements are currently sufficient for the requested action.

This does not imply the domain result is already successful.

### Queued / deferred

The action is valid and remains semantically eligible, but current capacity/admission policy delays operational realization.

Queueing SHOULD communicate:

- that the commitment remains unchanged;
- why work is waiting;
- whether capacity is the only known blocker;
- any meaningful queue/admission context that can be exposed safely.

Queueing MUST NOT be rendered as domain failure.

### Blocked

The action cannot currently proceed because a remediable prerequisite or permission is unresolved or unavailable, such as:

- exact dependency unavailable;
- authorization not established;
- source/reference unavailable;
- required worker runtime closure unavailable;
- recovery reconciliation incomplete;
- required semantic meaning unresolved.

Blocked does not automatically mean the committed activity has terminally failed.

### Incompatible

The requested semantics cannot be preserved by the selected Strategy/method/topology/deployment/runtime profile under the known facts.

Examples include:

- Strategy cannot support the requested topology shape;
- no-egress commitment conflicts with a runtime-network-only implementation;
- shared mutable sink cannot preserve required fencing;
- required model/runtime cannot execute on the selected platform.

The experience SHOULD explain which requirement is incompatible and, where legitimate, route the actor to pre-commit selection or a **new** semantic commitment rather than presenting a silent fallback as remediation.

### Supported with limitations

A capability may be supported with explicit limitations only when those limitations are compatible with the owning semantic contract.

The experience MUST name material limitations before commitment when known and preserve them in later history/result interpretation.

A limitation cannot silently waive a mandatory Constraint, quantity, horizon, topology constituent, privacy Criterion, security posture or Evidence-strength requirement.

### Indeterminate

The system cannot establish enough trustworthy information to determine readiness, compatibility, policy, recovery or historical state.

Indeterminate remains a legitimate result. It is not optimistic compatibility and not automatic failure.

## Recovery-continuity experience

### Potentially regressive recovery is not ordinary retry

After a control-state restore or another event that may regress current authority, the experience must expose an actor-comprehensible state equivalent to:

```text
Recovery in progress
Current write/promote authority is not yet verified
Read-only inspection may be available
Surviving jobs/material are being reconciled
```

The UI/API MAY use friendlier wording than `operational-authority continuity`, `recovery quarantine` or `ControlPlaneIncarnation`.

It MUST NOT simply show:

```text
Execution: running
```

because the restored database happened to contain a previously current Attempt.

### Recovery-restricted actions

While authority continuity is unverified, surfaces must prevent or clearly reject actions that could establish new canonical effects under restored stale authority, including where applicable:

- new authoritative writes;
- candidate/state/checkpoint adoption;
- semantic promotion;
- same-Execution retry/resume;
- cancellation decisions relying only on restored state;
- sensitive capability issuance based solely on restored grants.

Read-only inspection may continue when it can be served truthfully and securely.

### Surviving work classification

Actors should be able to understand surviving post-backup work/material through bounded classifications such as:

- verified immutable effect eligible for current-authority adoption;
- stale/non-authoritative effect;
- quarantined pending reconciliation;
- externally observed but canonical meaning unproven;
- unknown/unavailable.

The experience MUST NOT say that a surviving worker is `resumed` merely because its process still exists.

### Missing post-backup history

When the system cannot establish whether a post-backup semantic transition occurred, the experience must expose uncertainty rather than present the restored database as complete truth.

For example:

```text
Historical continuity: incomplete after restore point
Output material: observed
Generation promotion: not established from retained evidence
Current action: reconciliation required
```

If a missing transition is reconstructed from sufficient independent evidence, the experience must identify it as **reconstructed** and retain the reconstruction basis/provenance.

## Historical versus current experience

### Explicit temporal orientation

Historical views must identify the state/context being inspected strongly enough that actors do not confuse it with current truth.

A surface should be able to communicate distinctions equivalent to:

- current state;
- historical state as bound/known at a particular revision/commitment/event;
- reconstructed historical fact;
- historical interval with incomplete/unknown knowledge.

Current aliases, current policy, current Evidence applicability or current dependency availability MUST NOT silently replace historical bindings.

### Historical truth and current feasibility may diverge

A historical Generation may be known to have used a remote dependency while current policy prohibits the same behavior.

The experience must be able to say both:

```text
Historical fact: remote dependency R4 was used
Current reproduction feasibility: blocked by current no-egress policy
```

without rewriting either statement.

### Historical knowledge quality

When material, the experience preserves distinctions equivalent to:

- directly established canonical history;
- reconstructed from independently sufficient evidence;
- partially known;
- unavailable because required retained material is gone;
- unknown/indeterminate because occurrence cannot be established.

A `history complete=true/false` Boolean alone is insufficient when the missing area materially changes interpretation.

## Capability-specific degraded experience

There is no universal actor-facing `degraded=true` state.

The experience identifies the affected capability and consequence.

### Canonical persistence unavailable

Communicate that new authoritative transitions cannot currently be established. Do not render pending transitions as successful.

### Projection/search unavailable

Communicate limited search/explain convenience while preserving that canonical work/history may remain available.

### Optional telemetry unavailable

Communicate reduced observability, not semantic failure, unless the deployment explicitly requires that monitoring capability for protected execution.

### Exact dependency/artifact unavailable

Communicate which exact requirement cannot resolve and whether work is blocked, rather than silently selecting another artifact.

### Source/reference unavailable

Communicate exact-reference unavailability. Do not resolve `latest` or another source as a convenience fallback.

### Output/checkpoint storage unavailable

Communicate partial/non-final material and recovery state. Do not report truncated or incomplete result success.

### Compatible worker/accelerator pool unavailable

Communicate queued/blocked resource realization and any compatible resource alternatives that preserve semantics. Do not imply that any available worker is acceptable.

### Security/authorization unavailable or indeterminate

Protected actions fail closed. The actor-visible response must respect disclosure policy and may intentionally reveal less detail than internal audit state.

## Resource/backpressure experience

Queue/admission status must remain distinct from semantic status.

Actors should be able to distinguish:

```text
waiting for capacity
```

from:

```text
cannot run on this deployment
```

from:

```text
cannot run because a dependency is missing
```

from:

```text
cannot run because current authorization denies the action
```

Progress and ETA remain operational estimates unless a domain contract defines stronger semantics.

`100% tasks`, `all partitions launched` or `100% estimated` MUST NOT be presented as semantic completion.

Resource pressure must never be represented as authorization to reduce requested quantity, time-series horizon, multi-table scope, required Evaluation coverage or Constraint strength.

## Runtime-distribution experience

### Driver readiness versus cluster readiness

The experience must distinguish:

```text
SYNGAN/import/runtime available on the driver
```

from:

```text
all material worker roles can execute the exact implementation closure
```

When worker closure is incomplete, actors should receive a bounded explanation such as:

```text
Strategy implementation is available to the coordinator
Worker runtime closure: incomplete
Missing/incompatible role: Spark executor
Required component: <exact binding/artifact role>
Automatic public acquisition: disabled
Actionability: blocked until compatible worker environment is available
```

A human need not learn the exact packaging mechanism, but the experience must make the distributed readiness problem intelligible.

### Dynamic workers

If the deployment can add workers dynamically, experience must not claim permanent readiness merely from currently observed workers.

It may instead report that the selected deployment profile guarantees or currently satisfies the required worker-closure contract, or that the guarantee is indeterminate/limited.

## Authorization and disclosure experience

### Permission and existence are separate

The experience must preserve the distinction between:

- the action being denied;
- a resource/detail being withheld;
- the fact being absent;
- the fact being unknown;
- the fact being unavailable;
- an authorized redacted/summary view.

However, when policy protects **existence itself**, the outward response may deliberately avoid revealing whether the protected resource/detail exists.

In such cases, human/programmatic surfaces must use a non-disclosing response while internal security audit retains the more precise reason where permitted.

### View-time redaction

Redaction/withholding transforms what the actor may see. It does not mutate canonical state/history.

An authorized summary should be recognizable as a summary rather than being serialized as the original value.

### Current authorization is not permanent approval

A previously permitted action may later be denied after revocation or policy change.

Historical permission does not imply current permission; current denial does not rewrite the historical activity.

## Privacy/disclosure/release experience

The experience must prevent a user from inferring privacy or release status from synthetic origin alone.

Where privacy-related information is material, surfaces should preserve a layered distinction equivalent to:

```text
Output type: synthetic
Privacy/disclosure Evidence: <findings or not evaluated>
Formal privacy guarantee: <none / mechanism-specific if one exists later>
Current export authorization: <current security decision where disclosable>
Release/use approval: external governance state, not SYNGAN semantic completion
```

### No `safe` shortcut

The experience MUST NOT collapse those dimensions into universal labels such as:

```text
private=true
safe=true
safe_to_release=true
```

unless a future mechanism/external authority explicitly defines a narrower, correctly scoped statement and the surface names that authority.

### Evidence interpretation

Privacy/disclosure Evidence must expose enough threat-model/method/scope/coverage/uncertainty information to prevent one favorable result from being interpreted universally.

`not evaluated` must remain distinct from `low observed risk` and from a formal privacy guarantee.

### Differential privacy baseline

Initial-baseline surfaces must not advertise built-in formal differential privacy.

If a future mechanism-specific DP concept is accepted, its guarantee/accounting state must be shown separately from empirical disclosure Evidence and external release approval.

## Structured-topology experience

### Topology orientation

Before commitment, actors must be able to inspect the resolved topology semantics rather than only a convenience `mode` token.

A human-facing summary may use concise labels such as:

- single table;
- time series grouped by `<entity role>` ordered by `<time role>`;
- multi-table with `<N>` scopes and `<N>` structural links;
- composite multi-table + time-series.

Programmatic surfaces must expose the exact logical scopes and stable structural-semantic references required to reconstruct that summary.

### Strategy compatibility

Topology support is contextual and Strategy-specific.

The experience should be able to explain limitations such as:

- single-table supported;
- time-series supported up to a declared capability envelope;
- one-to-many shared-key topology supported;
- cyclic/self-referential relationship shape unsupported;
- composite relational + sequence topology unsupported by the selected Strategy;
- topology compatibility indeterminate because Data Meaning structural semantics are unresolved.

It MUST NOT silently flatten the requested topology to one the Strategy can support.

### Whole-result completion

For coordinated outputs, the experience must show constituent progress without mistaking one constituent's completion for whole-result completion.

Example:

```text
Generation G9
customers: candidate complete
orders: candidate complete
payments: materializing
cross-scope referential validation: pending
Completed logical output: no
```

Likewise, a time-series Generation may show entity/horizon coverage while remaining incomplete until the committed whole scope and required validation are completion-sufficient.

### Topology correction/history

When structural semantics change through a new Data Meaning revision, historical workflows must continue to show the relationship/order semantics actually bound at the time.

A newer corrected topology may be offered for new work or a new Evaluation of historical output, but it must not silently reinterpret the original Generation.

## Next-action experience

For any non-terminal or blocked condition, human/programmatic surfaces SHOULD expose legitimate next actions where they can do so safely.

Examples include:

- wait for admitted capacity;
- provision the exact approved dependency;
- request or restore authorization through the external security process;
- reconcile unknown external effects;
- resume from a qualified checkpoint;
- retry from start under the same commitment;
- select a compatible Strategy **before commitment**;
- create a new Generation/Learning/Evaluation when semantics must change;
- inspect bounded historical/recovery details;
- use an authorized summary when raw diagnostics are withheld.

A suggested next action must never disguise a material semantic change as retry or silently widen network/security/topology/privacy semantics.

## Programmatic result and error contract

A future programmatic surface must provide typed/bounded information sufficient to distinguish material failure/actionability categories rather than relying only on exceptions or strings.

Representation may differ, but clients must be able to determine, where authorized:

- the requested action and subject;
- owner semantic state when relevant;
- operational state when relevant;
- whether the request succeeded, queued, blocked, conflicted, was denied, is incompatible or remains indeterminate;
- safe reason/category and affected requirement;
- whether retry/resume is actually qualified;
- whether recovery continuity is established;
- whether returned details are full, redacted, withheld or unavailable;
- legitimate next actions where available;
- stable references needed for historical inspection.

### Error response boundaries

A generic thrown exception such as `RuntimeError("failed")` is insufficient for normal lifecycle/actionability states.

Likewise, normal queueing or readiness blockage should not necessarily be represented as an exceptional domain failure.

Conversely, stale-write conflicts, incompatible committed semantics, authorization denial and integrity defects must remain distinguishable when disclosure policy permits because their safe next actions differ materially.

### Non-disclosing errors

When revealing `not found` versus `forbidden` would leak protected existence, the public response may intentionally combine them into a non-disclosing outward category.

That outward ambiguity is a security feature, not permission to corrupt canonical/internal audit distinctions.

## Human/programmatic parity

Human UI, notebook, CLI, SDK and service API may optimize for different levels of detail, but they MUST preserve equivalent material semantics.

Human surfaces may summarize internal identifiers with friendly labels and drill-down.

Programmatic surfaces may expose exact typed references and reason codes.

Neither surface may uniquely hide a material distinction needed to understand:

- semantic versus operational completion;
- retry/resume safety;
- current authority continuity;
- queue/block/incompatibility/limitation;
- exact dependency/runtime closure;
- disclosure state;
- current versus historical truth;
- privacy Evidence versus formal guarantee/release authority;
- topology scope and whole-result completion.

## Bounded enterprise-scale experience

All summaries in this contract must remain bounded at enterprise scale.

Human/programmatic orientation should rely on:

- logical resource/Execution references;
- bounded constituent/topology summaries;
- material blocker/limitation reasons;
- bounded progress/coverage summaries;
- checkpoint/candidate/state/output references;
- Evidence summaries plus distributed diagnostic references;
- selected platform/telemetry links;
- historical/reconstruction references.

No ordinary experience requires all rows, all executor/task state, all provenance edges, all diagnostics or all model components to be loaded into one client/driver/UI process.

## Experience invariants

1. No universal status may replace owner semantic state plus operational/actionability context.
2. Queued/deferred work MUST remain distinguishable from blocked, incompatible, denied and terminally failed work.
3. Resource pressure MUST NOT be presented as permission to weaken committed semantics.
4. Potentially regressive recovery MUST expose that current mutation authority is unverified until a non-regressing boundary is established.
5. Restored state MUST NOT be presented as complete current truth when post-backup history may be missing.
6. Reconstructed historical facts MUST remain distinguishable from directly retained canonical history.
7. Surviving physical work/material MUST NOT be presented as current authority merely because it exists.
8. Capability-specific degradation MUST identify the affected capability/consequence rather than relying only on `degraded=true`.
9. Driver runtime availability MUST NOT be presented as proof of distributed worker runtime closure.
10. Withheld/redacted/unknown/unavailable/absent states MUST remain semantically distinct where policy permits disclosure of that distinction.
11. Security policy MAY intentionally obscure existence in outward responses without rewriting canonical/internal history.
12. Synthetic origin MUST NOT be rendered as privacy, formal guarantee or release approval.
13. Privacy Evidence MUST remain threat-model/method/scope/coverage/uncertainty specific.
14. Topology convenience labels MUST NOT replace exact logical scope and Data Meaning structural semantics.
15. Whole-result completion MUST remain distinguishable from constituent completion.
16. Strategy topology limitations MUST be explicit and MUST NOT trigger silent topology simplification.
17. Human and programmatic surfaces MUST preserve equivalent material distinctions.
18. Normal queueing/readiness states MUST NOT require generic exception handling as the only programmatic interface.
19. Next-action guidance MUST NOT disguise material semantic changes as retry/recovery.
20. All ordinary experience summaries MUST remain bounded at enterprise scale.

## Architecture and planning handoff

006-I must reconcile this experience contract into architecture and Phase 005 planning, including future representations for:

- orthogonal semantic/operational/actionability/continuity/disclosure/history dimensions;
- recovery-restricted commands and historical-reconstruction views;
- typed compatibility/readiness/result/reason structures;
- worker-runtime closure visibility;
- capability-specific degraded states;
- non-disclosing security errors and redacted/withheld field states;
- privacy Evidence/formal-guarantee/release-boundary presentation;
- composable topology summaries and exact semantic references;
- bounded constituent progress and whole-result completion;
- programmatic next-action/retry qualification;
- human/programmatic parity and bounded enterprise-scale query surfaces.

006-H does not choose concrete classes, HTTP codes, exception hierarchies, UI components, command names, status strings or persistence fields.

## Operational principles

### Regressive recovery

A practitioner opens a Generation after control persistence was restored from backup. The interface shows that the Generation's committed semantics are intact but current mutation authority is being re-established. A surviving candidate is visible as quarantined/non-final, post-backup history is marked incomplete, and retry/promote actions are unavailable until reconciliation establishes a fresh authority boundary. The actor can inspect safe historical context without being told the Generation merely `failed`.

### Resource pressure

A time-series Generation is committed for twelve months and waits for compatible accelerator capacity. The experience shows `queued for compatible capacity`, not `failed`, and continues to show the twelve-month committed horizon. When capacity appears, the same commitment proceeds; no hidden nine-month fallback occurs.

### Security/disclosure

A reviewer may inspect a privacy Evidence summary but lacks permission for nearest-neighbor diagnostics. The finding is shown with its threat model and coverage while the diagnostic field is marked withheld/authorized-summary. The absence of raw diagnostics is not presented as `null` or as evidence that no sensitive examples exist.

### Composite topology

A Generation includes customer metadata plus an ordered observations table per customer. A convenience preset may call the request `multi-table`, but the review surface shows the customer-to-observation relationship and the observations series entity/time roles. Candidate progress is per scope, while the completed-output state remains pending until the whole coordinated topology and required cross-scope/temporal validation are completion-sufficient.
