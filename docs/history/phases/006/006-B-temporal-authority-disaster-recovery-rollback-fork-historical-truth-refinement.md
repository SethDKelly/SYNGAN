---
type: Phase Record
title: 006-B — Temporal Authority, Disaster Recovery, Rollback, Fork & Historical-Truth Refinement
status: complete
---

# 006-B — Temporal Authority, Disaster Recovery, Rollback, Fork & Historical-Truth Refinement

## Objective

Close the design gap exposed by Phase 005-J and 005-K where canonical control persistence may be restored to an older point while later Attempts, cancellations, credentials, external effects, immutable material, or semantic transitions may have occurred or remain physically alive.

The phase determines the correct Jackson-style ownership, historical-truth semantics, current-authority rules, and downstream experience/architecture obligations **without implementing disaster-recovery machinery**.

**Phase 006 remains design-only. No production implementation is authorized or performed.**

## Governing authority

006-B is downstream of:

- [Concept Design Methodology](../../authority/design-methodology.md);
- [Accepted Concepts](../../concepts/index.md);
- [Core Synchronizations](../../synchronizations/core-synchronizations.md);
- [Execution Monitoring, Failure, Recovery & Cancellation Experience](../../experience/execution-monitoring-failure-recovery-cancellation.md);
- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [Phase 005 Consolidated Implementation-Planning Contract](../../implementation/phase-005-consolidated-implementation-planning-contract.md);
- [006-A Concept/Scope Revalidation](006-A-post-planning-concept-completeness-mechanism-vs-concept-scope-boundary-revalidation.md).

## Discovery evidence

006-B preserves its alternatives/falsification reasoning in:

[Temporal Authority, Regressive Recovery & Historical-Truth Revalidation](../../discovery/temporal-authority-regressive-recovery-revalidation.md).

That record is design evidence rather than current authority.

## Canonical authority established

006-B creates the active cross-cutting:

[Operational Authority Continuity & Regressive Recovery Contract](../../authority/operational-authority-continuity-regressive-recovery-contract.md).

The new contract is upstream of future architecture/implementation realization and constrains Execution, semantic result owners, Provenance/history, current authorization/security behavior and deployment recovery.

## Jackson concept decision

006-B explicitly considered whether the restore problem requires a new standalone concept.

### `ControlPlaneIncarnation` / `AuthorityEpoch`

**Rejected as a concept.**

A fresh incarnation/generation can be an essential realization mechanism, but its purpose is to enforce stale-authority exclusion after a recovery boundary. It does not own an independent product/domain purpose separate from Execution/security/deployment.

### `Recovery` / `Disaster Recovery`

**Rejected as a concept.**

Recovery remains Execution-owned operational behavior plus deployment realization.

### `Historical Fork`

**Rejected as a concept.**

Divergence between restored canonical knowledge and surviving later evidence is a diagnostic/reconciliation condition, not a new owner of the underlying state.

### Operational authority continuity

**Accepted as a cross-cutting design contract, not a concept.**

The same invariant constrains several existing owners and cannot safely be hidden only inside a deployment mechanism.

## Core distinction — restore point versus current authority

006-B establishes:

```text
restored control snapshot
        =
valid historical evidence at its represented point

restored control snapshot
        !=
proof of current mutation authority
```

A backup may legitimately say `Attempt A1 / epoch 1 was current at T1` while later history/effects mean A1 is no longer authorized at recovery time.

The absence of post-T1 rows does not prove that post-T1 work never happened.

## Recovery quarantine

A potentially regressive restore places the affected control plane into a cross-cutting condition equivalent to:

```text
continuity unverified
        ↓
recovery quarantine
```

During that condition:

- restored Attempt/fence values are not trusted as current write authority;
- no ordinary write-capable Attempt starts;
- candidate/state/checkpoint adoption/seal does not rely solely on restored tokens;
- semantic promotions do not rely solely on restored lifecycle state;
- protected write/use/export/network actions do not rely on pre-recovery capability state;
- read-only inspection may continue only with truthful continuity/history qualification.

Recovery quarantine is not added as a lifecycle state to Learning, Generation, Evaluation, Evidence, or every other concept.

## Non-regressing authority boundary

Before ordinary write-capable operation resumes, recovery must create a boundary that old/pre-recovery writers cannot satisfy by replaying restored state.

Possible future realizations include:

- fresh `ControlPlaneIncarnation`/recovery generation;
- external monotonic authority generation;
- provider-native fencing/namespace generation;
- rotated/revoked short-lived credentials;
- isolated post-recovery write namespaces.

The accepted design rule is mechanism-neutral:

> merely restoring another old counter/value from the same regressed projection is not sufficient if old writers can still satisfy it.

005-J's `ControlPlaneIncarnation` remains a credible realization and will be reconciled formally through 006-I rather than being promoted to semantic authority here.

## No authority resurrection

006-B adds the invariant that rollback/restore cannot by itself:

- make a superseded Attempt current again;
- remove a later cancellation and thereby revive old mutation rights;
- reactivate an earlier capability/credential as current permission;
- allow a previously fenced writer to register/adopt/seal/promote because restored rows look older;
- treat missing projection/history rows as proof that their underlying transition never occurred.

The rule is about current authority, not about forcing every old process to stop physically before recovery can progress.

## Execution continuity after restore

An existing Execution may continue after disaster recovery only when the parent committed activity and Execution identity remain sufficiently established.

Continuation occurs through **fresh current Attempt/runtime authority**, never by restoring an old worker's authority.

If the restored snapshot predates a surviving Execution/Attempt entirely:

1. the surviving work is orphaned/non-authoritative by default;
2. its immutable effects may be inspected/reconciled;
3. same-Execution continuation requires sufficient reconstruction of the missing canonical activity/Execution history;
4. if that history cannot be established, the orphaned work cannot be relabeled ordinary retry/resume.

The one-logical-Execution invariant therefore survives disaster recovery when continuity can be proven; it is not weakened into platform-run identity.

## Cancellation continuity

A restore may lose a later cancellation request/generation.

The fresh recovery boundary invalidates prior mutation authority first. Reconciliation then determines the historical cancellation request/outcome to the strength of available evidence.

A missing cancellation row in restored persistence is not permission to reactivate the earlier writer.

## Security continuity

Current authorization remains current-state authority and is therefore re-evaluated after regressive recovery.

Pre-recovery Attempt capabilities/credentials are not trusted merely because an old grant is visible in the restored store.

Where stale workers could still affect protected external systems, recovery may require credential/namespace/provider-fence rotation.

If current permission is indeterminate, protected actions fail closed.

Security audit may support reconciliation but does not become semantic state or Provenance authority.

## Historical truth and reconstruction

006-B rejects the simplistic model that database rollback rewrites reality.

After restore, post-restore-point facts fall into distinguishable classes:

```text
independently recoverable canonical fact
external/surviving observation only
unavailable
unknown / indeterminate
irreconcilable under retained evidence
```

### Missing semantic transitions

If a post-backup Learned State establishment, Generation promotion or Evidence establishment is missing from restored control state:

- physical bytes/provider success alone do not prove the semantic transition;
- absence from the restored store does not prove the transition never occurred;
- exact history may be reconstructed only when retained independent evidence satisfies the owning concept's normal transition/completion invariants;
- accepted reconstruction records both the historical transition and the later recovery/reconstruction action;
- insufficient evidence remains explicit as unknown/unavailable rather than being guessed.

This preserves single semantic promotion and avoids duplicate authority after recovery.

## Fork/divergence model

A restore can temporarily create:

```text
restored canonical knowledge through T1
             +
surviving observations/effects after T1
```

006-B does not model these as two equally current semantic branches.

Instead:

- write authority is quarantined;
- surviving effects are classified as adoptable immutable facts, stale/non-authoritative effects, or unresolved observations;
- mutable canonical state is never merged by last-writer-wins;
- one new current authority frontier is established after reconciliation;
- unresolved divergence remains explicit in history/availability.

## Immutable effect adoption

Current post-recovery authority may adopt surviving immutable material when exact identity, committed context, integrity, scope, security-domain compatibility, non-conflict and current authorization can be established sufficiently.

Adoption does not restore the producing old Attempt's authority.

Mutable external state that cannot be fenced/versioned/isolated/reconciled may require rotation/recreation/quarantine or render that recovery profile incompatible.

## Provenance and reproducibility

Material recovery history may include relationships showing:

- restore/recovery boundary;
- surviving Attempt/effect reconciliation;
- verified immutable effect adoption;
- reconstruction/correction of missing historical representation;
- unresolved continuity gap;
- new operational realization after recovery.

Provenance records established relationships but does not decide that a semantic transition happened from external bytes alone.

An unresolved continuity gap may weaken current reproducibility support because exact Attempt/dependency/checkpoint/promotion history cannot be defended. It does not rewrite facts that remain known.

## Synchronization decision

006-B introduces **no new synchronization ID**.

The new authority contract constrains existing:

- SYNC-04 — Learning operational realization;
- SYNC-07 — Generation operational realization;
- SYNC-11 — Evaluation operational realization;
- SYNC-14 — Provenance recording;
- SYNC-15 — reproducibility-relevant commitment snapshot.

006-C must now adversarially test these synchronization rules under regressive recovery and determine whether their canonical wording needs refinement. A new `SYNC-16` is required only if that scenario work proves genuinely new concept-to-concept coordination.

## Concept/synchronization count

At 006-B exit:

```text
accepted concepts             11
accepted synchronizations     15
new accepted concepts          0
new accepted synchronizations  0
new cross-cutting contracts    1
```

The reopened Relationship candidate from 006-A remains unaffected and provisional.

## Architecture/implementation consequence

006-B intentionally establishes the upstream rule before rewriting downstream mechanisms.

006-I must later reconcile:

- 004-F Execution/fencing architecture;
- 004-H security architecture where needed;
- 004-G historical/reproducibility architecture where needed;
- 004-I deployment/DR architecture;
- ADRs if a material architecture choice warrants one;
- affected Phase 005 plans, especially 005-G/005-H/005-I/005-J.

Phase history is not rewritten.

## Experience consequence

006-H must later formalize human/programmatic presentation for:

- recovery quarantine / continuity unverified;
- reconciliation progress;
- restored historical state versus current authority;
- observed surviving effect versus established canonical transition;
- reconstructed versus unavailable/unknown post-restore history;
- legitimate next actions after recovery.

006-B nevertheless establishes those semantics now so 006-C scenarios have a stable oracle.

## Backlog impact

BDR-001 — regressive restore and temporal authority closure — is **semantically resolved by 006-B**.

Its remaining downstream propagation is tracked through 006-C adversarial synchronization validation, 006-H experience closure, and 006-I architecture/planning reconciliation rather than leaving the original design question open.

BDR-002 through BDR-004 remain open.

## Exit assessment

**Status: complete.**

Findings:

- regressive persistence recovery is separated from current-authority recovery;
- a new cross-cutting Operational Authority Continuity contract is accepted;
- no new domain concept is justified;
- `ControlPlaneIncarnation` remains an architecture mechanism, not a concept;
- recovery quarantine and non-regressing authority-frontier semantics are defined;
- cancellation/security authority cannot resurrect through rollback;
- historical reconstruction/unknown-state rules are defined;
- fork/divergence does not create dual current authority;
- no new synchronization is introduced pending 006-C validation;
- production implementation remains unauthorized.

## Next group

**006-C — End-to-End Scenario, Exception, Failure & Adversarial Synchronization Validation**.
