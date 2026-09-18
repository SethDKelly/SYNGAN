---
type: Architecture Reconciliation Authority
title: Phase 013-C — Control Persistence, Historical Reference, Transaction/Concurrency, Migration & Recovery-State Reconciliation
status: active
---

# Phase 013-C — Control Persistence, Historical Reference, Transaction/Concurrency, Migration & Recovery-State Reconciliation

## Purpose

Reconcile SYNGAN's retained durable control-plane architecture against the completed concept design, current Phase 009 synchronization authority, 013-B representation rules, and current recovery authority before distributed-data and runtime architecture are reconciled.

013-C asks:

> **Can control persistence preserve exact historical meaning, owner-specific mutation, cross-boundary consistency, migration neutrality and non-regressing recovery without becoming a generic semantic owner or imposing one transaction/storage/event architecture?**

Current answer:

```text
YES — THE CONTROL-PERSISTENCE SPINE REMAINS SOUND WITH BOUNDED CLARIFICATIONS.
NO AMAT-2 PERSISTENCE DEFECT IS FOUND.
NO AMAT-3 BLOCKER OR AR-9 UPSTREAM CONTRADICTION IS FOUND.
```

This authority is downstream of:

- the completed Phase 012 concept-design authority;
- current Phase 009 dependence / application-family / synchronization authority;
- current Phase 010 mapping authority;
- [Phase 013 Architecture Reconciliation Authority](../authority/phase-013-architecture-reconciliation-authority.md);
- [Phase 013-B Representation Reconciliation](phase-013-b-representation-layering-public-contract-identity-view-reconciliation.md);
- [Operational Authority Continuity & Regressive Recovery Contract](../authority/operational-authority-continuity-regressive-recovery-contract.md).

---

## 1. Reconciliation subjects

Primary retained subjects reviewed here are:

- `control-plane-identity-revision-state-persistence-historical-reference.md`;
- `phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md`;
- persistence/recovery portions of `phase-006-architecture-reconciliation-contract.md`;
- ADR-0002 and ADR-0009 as rationale inputs;
- current Phase 009 synchronization ownership;
- current recovery-authority continuity rules.

Distributed data/manifest promotion remains 013-D. Runtime/dependency/security realization remains 013-E. Execution/Attempt mechanics remain 013-F. Evidence/Provenance storage/query detail remains 013-G.

---

## 2. Governing persistence rule

> **Persistence preserves and makes durable authority established by the owning concept or operational authority. Persistence does not create semantic authority merely because a row, document, event, message, projection, checkpoint or external record exists.**

The durable control plane must therefore preserve:

```text
stable logical identity
exact immutable semantic revision / commitment
owner-specific current mutable state
current-state observation / conflict token
representation schema version
material historical transitions and exact references
qualified reconstruction / continuity state
bounded cross-boundary coordination intent where required
```

These are representation/consistency responsibilities, not a new `Persistence`, `Transaction`, `History`, `Recovery`, `Migration`, `Outbox`, `Registry`, `Metadata`, or `Workflow` concept.

---

## 3. Persistence ownership reconciliation

The retained logical mutation boundaries remain useful:

```text
revisioned semantic-authority persistence
committed activity persistence
owner-specific established-result persistence
Execution / operational persistence
Provenance relationship persistence
derived index / read-model persistence
bounded coordination-intent persistence where atomic crossing is impossible
```

They are not physical database counts, package names, tables, services, aggregates or concept mergers.

Several owners may share one physical transaction/store. One owner may span multiple stores when scale/security/deployment requires it.

### No generic CRUD authority

A shared persistence engine MAY provide storage primitives, transactions, compare-and-set, indexing and query acceleration.

It MUST NOT expose a semantic bypass equivalent to:

```text
set_status(any_resource, arbitrary_value)
save_detached_object_as_truth(...)
mark_sync_complete(...)
mark_result_valid(...)
```

without the owning authority validating the transition.

---

## 4. Cross-owner atomicity does not merge ownership

Retained architecture correctly requires some facts to become durably consistent together. Current Phase 009 ownership qualifies how this must be interpreted.

Examples include:

```text
Learning completion        + Learned State establishment/reference
Generation completion      + Generation-owned completed-output association
Evaluation completion      + Evidence establishment/reference
material owner transition  + required Provenance relationship intent/record
```

A single local transaction MAY commit several owner-owned facts together when they share one atomic boundary.

That transaction does not make:

- Learning the owner of Learned State;
- Evaluation the owner of Evidence;
- Evidence the owner of Generation completion;
- Provenance the owner of source facts;
- persistence the owner of the synchronization.

The transaction is a technical consistency boundary over distinct canonical facts.

Where distinct owner transitions cannot be completed atomically, the architecture must retain enough durable intent/state to make incompleteness detectable and reconcilable without fabricating completion.

---

## 5. Durable coordination intent / outbox reconciliation

`Outbox`, `inbox`, `transition intent`, delivery record or equivalent names remain architecture mechanisms.

A durable coordination-intent record MAY establish:

- which source transition requires follow-up;
- exact source identity/revision/state involved;
- idempotency/reconciliation identity;
- technical delivery/acknowledgement/reconciliation state;
- whether realization must be requalified against current authority.

It does **not** establish:

```text
Synchronization.status
Composition.status
target semantic success
Execution success
Generation completion
Evidence establishment
Provenance source truth
```

Current Phase 009 rule remains:

```text
synchronization-owned canonical state = NONE
```

Technical delivery/reconciliation state is subordinate architecture state. It exists to preserve recoverability of a required relationship/action across technical boundaries, not to create a hidden workflow coordinator.

At-least-once physical delivery remains compatible when target effects are idempotent/fenced/reconciled. Exactly-once physical delivery is not a universal architecture requirement.

---

## 6. CAS / state-version reconciliation

The retained conflict-detection rule remains valid:

- material mutable owner state must reject or explicitly reconcile stale conflicting writes;
- wall-clock timestamps are not sufficient as the sole write-order authority;
- one global version counter is not required;
- CAS/version matching does not validate semantic legality, current authorization, dependency readiness, recovery authority or semantic completion.

### Recovery qualification

A state-version/concurrency token is authoritative only within the current valid authority frontier it protects.

After a potentially regressive control-state restore:

```text
restored state_version / CAS token
        !=
proof of current mutation authority
```

The restored token may accurately describe the restore-point state while being unsafe for current writes.

ADR-0009 / recovery authority therefore remains a distinct axis from:

```text
semantic revision
commitment snapshot
current state version
representation schema version
Attempt epoch
migration revision
package/application version
```

A fresh non-regressing recovery-authority frontier must be established before ordinary mutation authority resumes where restore may have regressed canonical authority.

---

## 7. Historical reference reconciliation

The retained exact-reference rules remain current:

1. resolve the exact bound identity/revision/snapshot first;
2. never substitute `latest`, current aliases, replacement dependencies, newer Learned State or newer Evidence silently;
3. distinguish exact resolution from withheld, unavailable, unknown/indeterminate, invalid/integrity-defective and unsupported representation outcomes;
4. keep `absent` distinct from a known-but-unavailable/withheld relationship;
5. preserve bounded tombstone/reference identity when policy permits history to outlive retained payload;
6. authorization may change the actor-safe outward view without rewriting underlying history.

### Current projection reconstruction qualification

A materialized current projection MAY be rebuilt from retained canonical transition/history facts only when the owning authority's required current state can actually be established from sufficient retained evidence.

If history is incomplete after failure/recovery, rebuild must preserve:

```text
reconstructed
partial
unavailable
unknown / indeterminate
continuity unverified
```

as applicable rather than manufacturing a stronger current state.

A derived projection being rebuildable does not mean missing canonical history is reconstructible by default.

---

## 8. Material history and correction

The architecture retains append-preserving material history sufficient to explain consequential transitions without requiring universal event sourcing.

Current rules:

- correction does not silently rewrite exact historical/as-bound truth;
- current reliance may change through the owning concept's correction/supersession/invalidation action;
- reconstructed history remains distinguished from directly retained original history;
- a Provenance correction does not mutate referenced source facts;
- storage/history records explain authority transitions but do not become duplicated semantic owners;
- every read/cache/internal write need not become a canonical event.

Full event sourcing remains an implementation option, not an architecture mandate.

---

## 9. Transaction/isolation architecture remains non-prescriptive

Architecture requires invariant-preserving consistency, not one transaction technology.

Compatible realizations may later include:

```text
local atomic transaction
owner-scoped compare-and-set
recoverable durable transition intent
outbox/inbox realization
idempotent establishment/promotion records
fencing + reconciliation
other equivalent consistency mechanisms
```

Phase 013 does not choose:

- relational versus document/event/key-value storage;
- ACID isolation level universally;
- distributed 2PC;
- one event bus;
- one unit-of-work pattern;
- one repository/ORM abstraction;
- one database technology.

Transaction boundaries follow invariant scope, not a user-visible workflow or application-family membership.

---

## 10. Migration reconciliation

Migration changes representation by default.

It MUST NOT silently create or alter:

```text
semantic revision
committed activity occurrence
owner-established result
Evidence finding
historical binding
unknown/unavailable -> known/success
semantic correction
```

Migration sequence/progress is technical architecture state, distinct from semantic state.

Incremental migration may expose a mixed representation state internally, but must not present a partially migrated corpus as uniformly migrated when that distinction is decision-material.

Interrupted migrations must be restartable/reconcilable where the migration can partially execute.

### Down migration / rollback

A reversible schema operation does not imply reversible domain history.

Representation rollback MUST NOT erase semantic transitions merely because an older schema cannot conveniently represent them.

If compatibility cannot preserve material historical meaning, rollback must be blocked, qualified or accompanied by an explicit preservation strategy.

---

## 11. Recovery-state reconciliation

Persistence recovery and authority recovery remain distinct.

A potentially regressive restore enters continuity-unverified / recovery-restricted operation until a non-regressing authority frontier is established.

Restored persistence may establish restore-point historical facts but cannot by itself:

- resurrect a superseded Attempt/writer;
- undo later cancellation/revocation;
- restore stale capability as current permission;
- prove post-backup work never occurred;
- prove surviving physical effects were semantically completed;
- authorize re-promotion/adoption blindly.

Surviving immutable effects may be adopted only by current authority after exact context/integrity/completeness and conflict conditions are sufficiently established.

When post-restore-point history cannot be established, the system preserves uncertainty rather than substituting success/failure/absence/latest.

Recovery quarantine remains cross-cutting operational/experience qualification, not a new lifecycle copied into every concept.

---

## 12. Backup, restore, clone and authority scope

The retained distinction remains valid:

```text
disaster-recovery continuation
  -> may continue the same logical authority only under recovery continuity rules

clone / fork / test copy
  -> distinct authority scope unless an explicit continuation/federation contract says otherwise
```

Copying database bytes does not duplicate current authority automatically.

The exact namespace/incarnation/federation mechanism remains deferred.

---

## 13. Derived indexes / read models

Search, navigation, dashboards and composed read models may combine owner facts for performance.

They remain derived and must:

- retain sufficient source identity/version/freshness context;
- never acquire canonical mutation authority;
- be repairable/rebuildable where their contract claims rebuildability;
- not prove a semantic transition merely because an indexed row exists;
- expose or tolerate staleness according to the material user/programmatic contract.

Loss of a projection does not by itself mean canonical history was lost.

---

## 14. Enterprise-scale persistence boundary

Control persistence remains bounded by logical resources, revisions, transitions, references, Attempts/checkpoints summaries, manifests/references, Evidence summaries and other material control facts.

It MUST NOT require ordinary row-per-generated-record canonical control state, full source/output embedding, full diagnostic datasets or complete platform telemetry simply for control/history semantics.

This remains necessary for Spark-scale product claims.

---

## 15. Finding ledger

```text
A13-C-001  generic promoted-result persistence terminology
             AR-3 / AR-6  AMAT-1  CLARIFY              RESOLVED

A13-C-002  cross-owner facts described as one persistence transition
             AR-3 / AR-6  AMAT-1  CLARIFY              RESOLVED

A13-C-003  durable outbox/coordination state could resemble sync-owned state
             AR-3 / AR-6  AMAT-1  CLARIFY              RESOLVED

A13-C-004  CAS/state-version could be overread as non-regressing authority
             AR-5         AMAT-1  CLARIFY              RESOLVED

A13-C-005  projection rebuild wording under incomplete history
             AR-5         AMAT-1  CLARIFY              RESOLVED

A13-C-006  migration progress/status as technical state
             AR-7         AMAT-0  RETAIN + GUARDRAIL   CLOSED

A13-C-007  backup clone/fork authority scope
             AR-0         AMAT-0  RETAIN                CLOSED

A13-C-008  007-E historical synchronization count = 15
             AR-1         AMAT-1  CLARIFY/SUPERSEDE    SEMANTICALLY RESOLVED
                                                    CORPUS CLEANUP -> 013-I

A13-C-009  recovery contract historical SYNC-15 synchronization wording
             AR-1         AMAT-1  CORRECT              RESOLVED IN 013-C
```

---

## 16. Retained subject disposition

```text
Phase 004-C control persistence/history          ALIGNED-WITH-CLARIFICATION
Phase 007-E persistence/transaction baseline     ALIGNED-WITH-CLARIFICATION
Phase 006 persistence/recovery refinements       ALIGNED-WITH-CLARIFICATION
ADR-0002                                         PROVISIONAL RETAIN
ADR-0009                                         PROVISIONAL RETAIN
```

ADR-0002 and ADR-0009 remain directionally compatible with current design. 013-I retains final ADR lifecycle/status disposition authority.

Historical Phase 005-D database/ORM/migration-tool choices remain implementation-planning evidence only.

---

## 17. Materiality result

```text
AMAT-2 persistence defects       0
AMAT-3 blockers                  0
AR-9 contradictions              0
upstream reopen                  NONE
new concepts                     0
new synchronizations             0
mandatory database/event model   0
```

No current concept, application-family, synchronization or mapping authority is reopened.

---

## 18. 013-D handoff

013-D must preserve:

- stable control identity independent of physical distributed representations;
- exact semantic revision/commitment bindings;
- owner-specific state and semantic finality;
- candidate/checkpoint/material existence != semantic completion;
- bounded control references to distributed payload;
- cross-owner atomicity without ownership merger;
- durable coordination intent without synchronization-owned state;
- recovery uncertainty and non-regressing authority;
- migration/representation changes without semantic mutation.

013-D may reconcile manifests/sealing/promotion/data topology, but persistence facts or physical durability may not become Generation/Learned State/Evidence authority by themselves.

---

## Exit decision

```text
013-C                         COMPLETE
control-persistence spine     RETAINED WITH BOUNDED CLARIFICATION
AMAT-2                        0
AMAT-3                        0
AR-9                          0
upstream reopen               NONE
R1                            DOWNSTREAM / IN PROGRESS
013-D                         NEXT ELIGIBLE
```

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
