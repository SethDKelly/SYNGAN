---
type: Design Authority
title: Operational Authority Continuity & Regressive Recovery Contract
status: active
---

# Operational Authority Continuity & Regressive Recovery Contract

## Purpose

Define the cross-cutting rules SYNGAN must preserve when canonical control persistence may regress while later operational work, external effects, credentials, immutable material, or semantic transitions may have occurred.

This contract exists to prevent a restored historical control-state projection from being mistaken for current operational authority or from silently rewriting historical truth.

It is **not** a new domain concept. It constrains existing concept ownership, especially [Execution](../concepts/execution.md), semantic result owners, [Provenance](../concepts/provenance.md), current authorization/security behavior, and downstream deployment/recovery architecture.

## Governing rule

> **A regressed persistence view may describe what SYNGAN knew at an earlier point, but it MUST NOT by itself reactivate superseded write authority, erase later historical reality, or prove that later work never occurred. Current write authority must be re-established under a non-regressing recovery boundary before write-capable operation resumes.**

## Scope

This contract applies when recovery can produce a control-state view older than one or more potentially surviving facts, including:

- Attempt/fencing authority;
- cancellation intent/generation;
- platform launch/correlation state;
- candidate/checkpoint/state materialization;
- provider transactions or external effects;
- semantic promotion/result establishment;
- security capabilities/credentials;
- required Provenance/outbox/history state.

Ordinary coordinator restart or failover that preserves non-regressed canonical authority does not automatically trigger the full recovery-quarantine contract.

## Key distinctions

### Persistence recovery versus authority recovery

Restoring a backup, replica, snapshot, database image, or equivalent persistence state is **persistence recovery**.

It is not proof that restored current-state values remain the correct current operational authority.

### Historical state versus current authority

A restored snapshot may be a valid historical representation of state at its restore point while being unsafe as a current mutation-authority projection.

These facts must remain distinguishable.

### External observation versus canonical transition

A surviving file, platform job, provider transaction, credential, checkpoint component, or audit event may be evidence that something occurred.

Its existence does not automatically establish a missing canonical semantic or operational transition.

### Fork/divergence versus dual authority

After rollback there may be divergent evidence between restored canonical knowledge and surviving later effects.

This condition MUST NOT create two concurrently authoritative semantic branches. One current authority frontier is re-established only after recovery qualification/reconciliation.

## Continuity-unverified state

When a recovery may have regressed control-state authority, SYNGAN MUST treat current write authority as **continuity unverified** until recovery establishes otherwise.

The actor/operator experience may call this condition **recovery quarantine**.

While continuity is unverified:

- new authoritative Attempts MUST NOT be started as ordinary write-capable work;
- stale/restored writer tokens MUST NOT be trusted merely because restored rows consider them current;
- candidate/state/checkpoint adoption or sealing MUST NOT rely solely on restored authority projections;
- semantic promotion/result establishment MUST NOT rely solely on restored lifecycle state;
- protected write/use/export/network actions MUST NOT rely solely on pre-recovery authorization/capability state;
- read-only/historical inspection MAY remain available only when the possibility of incomplete post-restore-point history is represented truthfully.

Recovery quarantine is cross-cutting operational/experience state, not a new lifecycle state owned by every domain concept.

## Non-regressing recovery boundary

Before write-capable operation resumes, recovery MUST establish a current authority boundary that cannot be satisfied accidentally by replaying the restored state.

The architecture may realize this through one or more mechanisms such as:

- a fresh control-plane incarnation/generation;
- an external monotonic authority generation;
- provider-native fencing/namespace generation;
- rotated/revoked workload credentials;
- isolated post-recovery write namespaces;
- another mechanism providing equivalent stale-authority exclusion.

The mechanism itself is downstream architecture.

A mechanism is insufficient if restoring the same persistence state can replay its authority in a form that an old writer can still satisfy without consulting or possessing the fresh post-recovery boundary.

## No authority resurrection

A regressive restore MUST NOT by itself:

- make a superseded Attempt authoritative again;
- undo a later cancellation generation and thereby reactivate old mutation rights;
- restore a previously revoked capability as current permission;
- make a stale provider credential acceptable merely because the corresponding old grant row reappears;
- allow a previously fenced writer to register, adopt, seal, promote, or complete through restored state;
- treat a lost projection/index as evidence that its underlying historical transition never occurred.

This invariant applies even when the old worker/process remains physically alive.

## Execution continuity

[Execution](../concepts/execution.md) remains the owner of operational realization and Attempt history.

After regressive recovery:

1. surviving prior workers/Attempts are non-current until continuity is re-established;
2. their external/immutable effects may be reconciled but cannot regain authority merely by survival;
3. a same-Execution continuation requires that the parent committed activity and Execution identity remain sufficiently established;
4. any continuing work uses fresh current Attempt/runtime authority under the post-recovery boundary;
5. if the restored state predates creation of a surviving Execution/Attempt, that surviving work is orphaned/non-authoritative unless the missing canonical identity/history can be reconstructed from sufficient durable evidence;
6. inability to reconstruct the relevant Execution/activity history prevents the system from pretending that orphaned work is an ordinary retry/resume.

## Cancellation continuity

A backup may predate a cancellation request or later cancellation generation.

Recovery MUST therefore invalidate pre-recovery write authority before determining the historical cancellation outcome.

If independent evidence shows cancellation was requested or took effect after the restore point, that fact is reconciled into history to the degree it can be established.

A missing cancellation row in the restored snapshot MUST NOT by itself reactivate the earlier writer.

## Current authorization and security continuity

Historical authorization decisions and capability grants are not permanent current permission.

After a regressive recovery:

- sensitive operations are authorized again under current policy;
- Attempt-scoped capability grants from the prior authority frontier are not trusted as current write/use authority;
- surviving credentials are revoked/rotated when needed to enforce stale-writer exclusion;
- inability to establish current authorization fails closed for protected actions;
- security-audit observations may support reconciliation but do not become semantic state or canonical Provenance merely by existence.

## Historical-truth rules

### Restore-point truth

A restored snapshot may establish canonical historical state up to the strength/time represented by that snapshot.

### Post-restore-point uncertainty

Facts after the restore point may be:

- independently recoverable;
- externally observed but not sufficient to prove a canonical transition;
- unavailable;
- unknown/indeterminate;
- irreconcilable under retained evidence.

The system MUST preserve these distinctions.

### No fabricated rollback of history

If a semantic/operational transition may have committed after the restore point, the absence of that transition from the restored store MUST NOT automatically be presented as proof that it never happened.

Likewise, physical material alone MUST NOT be presented as proof that the corresponding semantic transition did happen.

### Historical reconstruction

A missing canonical historical transition MAY be reconstructed only when retained independent evidence establishes the exact transition, target identity, material preconditions, and required completion basis strongly enough to satisfy the owning concept's rules.

When reconstruction is accepted, history SHOULD preserve both:

- the original historical fact/transition being restored; and
- the later recovery/reconstruction action that re-established its canonical representation.

Reconstruction is not a license to invent current state from incomplete evidence.

### Unresolvable gaps

When exact history cannot be reconstructed sufficiently, the affected fact remains `unknown`, `unavailable`, or otherwise explicitly unresolved according to the owning context.

The system MUST NOT silently substitute success, failure, absence, or a new current/latest value.

## Semantic result continuity

Physical bytes, model/state files, candidate snapshots, diagnostic output, or provider success are insufficient by themselves to restore semantic result authority after rollback.

If a post-backup semantic transition such as Learned State establishment, Generation promotion, or Evidence establishment is missing from restored canonical state:

- the material remains non-authoritative until the owning transition can be reconstructed/proven under its normal completion rules;
- single semantic promotion/result cardinality remains in force;
- an apparently complete physical result MUST NOT be blindly re-promoted if doing so could duplicate or contradict a transition that already occurred;
- when proof is insufficient, the result remains unresolved/non-final from the current system's knowledge perspective.

## Immutable effect adoption

Recovery MAY adopt surviving immutable effects only when it can establish enough of the following to preserve correctness:

- exact producing activity/Execution/Attempt context;
- exact committed semantic context;
- physical identity/integrity;
- effect scope/completeness;
- no conflict with a known authoritative result;
- current authorization and security-domain compatibility;
- current post-recovery adoption authority.

Adoption is performed by current authority. It does not restore the old writer's authority.

Mutable external state that cannot be fenced, versioned, isolated, or reconciled strongly enough may require rotation/quarantine/recreation or may make that recovery profile incompatible.

## Provenance and historical explanation

[Provenance](../concepts/provenance.md) SHOULD preserve material relationships needed to explain regressive recovery, such as:

- recovery from a specific restore point;
- reconciliation of surviving Attempt/effect state;
- adoption of verified immutable material;
- reconstruction/correction of missing historical representation;
- unresolved continuity gaps material to investigation/reproducibility;
- new operational realization following the recovery boundary.

Provenance records relationships to facts established by the owning concepts. It MUST NOT infer that a semantic transition occurred merely because a surviving external effect exists.

## Reproducibility consequence

A continuity gap may weaken current reproducibility support when exact Attempt, dependency, checkpoint, runtime, or promotion history cannot be reconstructed.

The gap does not rewrite what is known historically; it constrains the strongest claim that can currently be defended.

## Synchronization consequence

This contract constrains existing synchronizations rather than creating a new concept-to-concept synchronization by itself.

In particular:

- SYNC-04 / SYNC-07 / SYNC-11 remain the domain activity ↔ Execution operational-realization boundaries;
- SYNC-14 remains responsible for required material Provenance relationships;
- SYNC-15 remains responsible for reproducibility-relevant historical facts.

Phase 006-C must adversarially validate whether the wording of those existing synchronizations needs refinement. No `SYNC-16` is introduced by this contract.

## Operator/programmatic truthfulness

Human and programmatic interfaces MUST be able to distinguish at least:

- normal operation;
- recovery quarantine / continuity unverified;
- reconciliation in progress;
- continuity re-established;
- history reconstructed;
- history unavailable/unknown after restore point;
- surviving effect observed but not canonically established.

A restored `running`, `completed`, `cancelled`, or `current Attempt` value must not be shown without qualification when authority continuity is known to be unverified.

## Invariants

1. Restored historical state MUST NOT by itself establish current mutation authority after a potentially regressive recovery.
2. A superseded writer MUST NOT regain authority because a restored snapshot predates its supersession.
3. A missing later cancellation record MUST NOT reactivate pre-cancellation authority.
4. Pre-recovery capability/credential state MUST NOT be treated as current permission merely because it exists in restored persistence.
5. Recovery MUST establish a non-regressing authority boundary before ordinary write-capable operation resumes.
6. Divergent surviving effects do not create multiple current semantic authorities.
7. Physical material MUST NOT establish a missing semantic result transition by existence alone.
8. Missing restored history MUST NOT be presented as proof that later events never occurred.
9. Historical reconstruction requires evidence sufficient for the owning concept's normal invariants and must remain auditable.
10. Unresolvable post-restore-point history MUST remain explicitly unknown/unavailable rather than fabricated.
11. Current authority performs any adoption of verified surviving material; old writers do not regain authority.
12. Same-Execution continuation after rollback requires sufficient continuity of the parent committed activity/Execution identity.
13. Security authorization is re-evaluated under current policy after recovery.
14. Provenance records recovery relationships but does not become the owner of reconstructed semantic state.
15. Recovery/deployment implementation mechanisms MUST preserve this contract without becoming new domain concepts merely because they are durable.

## Operational principle

A Generation Execution has Attempt A2 running when a control-store backup from before A2 is restored. A2 still exists on the platform and has written immutable candidate components. The restored store would otherwise make A1 appear current.

SYNGAN enters recovery quarantine rather than trusting A1 or A2. A fresh non-regressing authority boundary is established and old write capability is invalidated. Recovery reconciles platform correlation and candidate manifests. A2's immutable components are adopted only if their exact Generation/Attempt context and integrity can be proven; A2 itself does not regain write authority. A new Attempt receives current authority if continuation is valid.

If a Generation promotion had occurred after the backup but cannot be proven from retained independent evidence, the restored system does not blindly re-promote the surviving bytes or claim the promotion never happened. The affected history remains unresolved until sufficient evidence is recovered or the owning workflow determines a safe future path.
