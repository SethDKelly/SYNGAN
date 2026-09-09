---
type: Discovery Record
title: Temporal Authority, Regressive Recovery & Historical-Truth Revalidation
status: historical
---

# Temporal Authority, Regressive Recovery & Historical-Truth Revalidation

## Purpose

Preserve the design reasoning used by Phase 006-B to close the failure mode exposed by 005-J: canonical control persistence may be restored to an older point while platform workers, credentials, object-store effects, provider transactions, checkpoints, candidates, or even semantic transitions from a later period may still exist.

This record is design evidence. Current accepted authority is established separately under `docs/authority/` and existing concept authority.

## Trigger scenario

```text
T1  control-store backup
T2  Execution/Attempt authority advances
T3  external worker/effects continue
T4  control persistence becomes unavailable or corrupt
T5  T1 backup is restored
```

The restored rows may say an earlier Attempt is current, omit a later cancellation, omit an Attempt entirely, or omit a semantic transition that actually committed after T1.

The central design question is therefore not merely "how do we restore PostgreSQL?" It is:

> What can SYNGAN truthfully claim about current authority and historical state after the persistence substrate used to remember those facts has regressed?

## Candidate concept review

### Candidate: Control Plane Incarnation / Authority Epoch as a concept

**Disposition: reject as a standalone concept.**

Purpose test fails at the product/domain level. Actors do not need an independent reusable domain object whose purpose is "be the current control-plane incarnation." The state exists to implement stale-authority exclusion after a recovery boundary.

It remains a legitimate architecture mechanism when a deployment needs a fresh authority generation/fence that cannot be replayed from the restored projection.

### Candidate: Recovery / Disaster Recovery as a concept

**Disposition: reject.**

Recovery remains an Execution-owned operational action/experience plus deployment realization. Disaster recovery changes the conditions under which that action occurs but does not create a distinct domain purpose that owns semantic results.

### Candidate: Historical Fork as a concept

**Disposition: reject.**

A fork is a diagnostic condition in which restored canonical knowledge and surviving later observations/effects disagree or have incomplete continuity. It is not a durable owner of the underlying state.

### Candidate: Temporal Authority / Authority Continuity as a cross-cutting contract

**Disposition: accept as cross-cutting authority, not a concept.**

The failure crosses Execution, current security authorization, semantic promotion, Provenance/history and deployment realization. The invariant is analogous to the existing Reproducibility and Network/External Dependency contracts: several owners must preserve one cross-cutting rule without transferring ownership into a new concept.

## Core finding — restored persistence is evidence, not proof of current authority

A backup snapshot is authoritative evidence of canonical state **at the point represented by that backup**. It is not proof that the same state remains current after restore when later external activity may have occurred.

Consequences:

1. restored `AttemptEpoch`, cancellation generation, lifecycle state or authorization-related projection cannot by itself reactivate old mutation authority;
2. a pre-restore process that survives does not become authoritative merely because restored rows make its earlier token appear current;
3. a post-backup process omitted by restored history is not thereby proven never to have existed;
4. semantic transitions that may have committed after the restore point are not automatically undone as historical truth merely because the restored store does not contain them.

## Current-authority continuity

After a recovery that may regress canonical control state, write-capable current authority is **continuity-unverified** until a fresh non-regressing authority frontier is established and relevant surviving effects are reconciled.

During this condition:

- no new write-capable Attempt may be treated as ordinarily authorized;
- no candidate/state/checkpoint adoption or seal may rely solely on restored fence values;
- no semantic promotion may rely solely on restored lifecycle projections;
- no old capability/credential should be assumed current merely because its historical grant is visible;
- read-only inspection may continue only when the interface truthfully exposes possible continuity/history incompleteness.

This actor/deployment condition is referred to as **recovery quarantine**. The name is experience/architecture vocabulary, not a new concept lifecycle state.

## Non-regressing authority frontier

Recovery must establish a boundary that old writers cannot satisfy accidentally by replaying restored state.

Candidate realizations include:

- a fresh `ControlPlaneIncarnation` or cryptographically/randomly unique authority generation issued after restore;
- a monotonic generation held in a non-regressing authority service;
- provider-native fence/namespace generation;
- short-lived workload credentials rotated after recovery;
- combinations of the above.

The design requirement is stronger than "store another integer in the same database." If restoring the database can replay the value in a way that old writers can still satisfy, the mechanism does not close the gap.

A fresh incarnation can be stored in restored persistence **after** recovery begins, provided all material mutation/adoption boundaries validate the fresh value and old workers cannot bypass those boundaries. Shared mutable providers that cannot perform such validation require credential/namespace/native-fence rotation or are incompatible with this recovery profile.

## Historical-truth model

006-B distinguishes three questions after rollback:

### 1. What is known to have been canonical at or before the restore point?

The restored snapshot can answer this to the strength of the backup/integrity guarantee.

### 2. What may have happened after the restore point?

Possible post-restore-point facts may be supported by:

- surviving provider transaction identities;
- immutable object/candidate/checkpoint manifests;
- external audit/security records;
- platform launch/correlation records;
- replica/WAL/archive evidence outside the restored snapshot;
- signed/immutable transition or outbox evidence where a future architecture provides it.

These are observations/evidence for reconciliation. Their existence does not automatically establish the missing canonical domain transition.

### 3. What can be reconstructed as canonical historical truth?

A missing post-backup canonical transition may be restored to history only when evidence is strong enough to establish the exact transition and its preconditions without inventing state.

When that is possible, recovery records both:

- the original historical transition/fact; and
- the later recovery/reconstruction action that restored its representation.

When it is not possible, SYNGAN preserves `unknown`, `unavailable`, or another truthful unresolved state. It must not silently substitute "never happened," "failed," or "succeeded."

## Fork/divergence semantics

A regressive restore can temporarily expose two evidence lines:

```text
restored canonical knowledge through T1
             +
surviving observations/effects after T1
```

SYNGAN does **not** treat these as two equally current semantic branches that can both mutate the system.

Instead:

- write authority remains quarantined;
- post-T1 effects are reconciled as immutable adoptable facts, non-authoritative/stale effects, or unresolved observations;
- mutable canonical state is not merged by last-writer-wins;
- one fresh current authority frontier is established after reconciliation;
- unresolved divergence remains explicit in history/availability rather than being hidden.

## Execution continuity

An existing Execution may continue across disaster recovery only when its committed parent activity and identity remain sufficiently established and recovery can issue a fresh Attempt under the new authority frontier.

If the restored snapshot predates the creation of a surviving Execution/Attempt entirely:

- the surviving workload is non-authoritative by default;
- its effects may be inspected/reconciled but not adopted merely because they exist;
- the missing Execution/activity history must be reconstructed from sufficient durable evidence before same-Execution continuation can be claimed;
- otherwise the orphaned work remains quarantined/non-authoritative and any valid new work begins through the owning domain workflow.

## Cancellation continuity

A restored backup may omit a cancellation request or later cancellation generation.

Recovery must never reactivate pre-cancellation mutation authority simply because the cancellation row was lost in the restored snapshot.

The fresh authority frontier invalidates all pre-recovery writer capability first. Reconciliation then establishes the historical cancellation request/outcome to the degree evidence supports it.

## Security continuity

Current authorization is re-evaluated after recovery.

Rules:

- historical grants/decisions are not permanent current permission;
- Attempt-scoped capabilities issued before the recovery boundary are not trusted as current authority;
- secret/provider credentials used by surviving workers are revoked/rotated where needed to enforce the fresh frontier;
- inability to establish current permission fails closed for protected write/use/export/network actions;
- security-audit evidence may inform what happened but does not become canonical Provenance or semantic state by itself.

## Semantic-result continuity

Physical result material is not enough to reconstruct semantic completion.

If a post-backup Learned State establishment, Generation promotion or Evidence establishment is absent after restore:

- existing payload/candidate/diagnostic bytes remain non-authoritative until the exact owner transition and completion basis can be proven;
- if exact canonical transition evidence survives, history may be reconstructed explicitly;
- if it does not, the system must not "re-promote" solely because the physical bytes look complete;
- the owning concept's single-promotion and historical-binding rules remain in force.

This protects against duplicate or contradictory semantic authority after recovery.

## Provenance and history

Provenance may record material relationships such as:

- Execution recovered after a regressive restore;
- Attempt/effects reconciled from a pre-recovery authority frontier;
- immutable material adopted after verification;
- historical representation reconstructed from independent durable evidence;
- an unresolved continuity gap affecting reproducibility or investigation.

Provenance does not decide that an underlying transition occurred merely because an external effect exists.

## Synchronization assessment

006-B finds no new concept pair requiring a new synchronization ID.

The continuity rule constrains existing coordination:

- SYNC-04 / 07 / 11 — domain activity ↔ Execution operational realization;
- SYNC-14 — Provenance recording of material transitions/recovery;
- SYNC-15 — reproducibility-relevant historical facts.

006-C must adversarially test these existing synchronizations under the new continuity contract and may recommend wording refinements, but 006-B does not create `SYNC-16`.

## Design outcome

006-B supports one new cross-cutting contract and no new standalone concept:

```text
new accepted concept             0
new accepted synchronization     0
new cross-cutting authority       1
```

`ControlPlaneIncarnation` remains one downstream realization candidate rather than accepted semantic authority.
