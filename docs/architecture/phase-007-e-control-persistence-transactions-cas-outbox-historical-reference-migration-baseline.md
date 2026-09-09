---
type: Architecture Authority
title: Phase 007-E Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline
status: active
---

# Phase 007-E — Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline

## Purpose

Refine SYNGAN's control-plane persistence architecture for canonical ownership, transaction boundaries, stale-write protection, durable cross-boundary intent, material history, exact historical resolution, migration, and recovery **without selecting a database, ORM, event store, identifier encoding, migration framework, table/document schema, or executable test implementation**.

007-E continues the Phase 007 architecture-design track established by the [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md). It is design authority, not permission to implement persistence.

## Governing authority

007-E is downstream of:

- [Concept Design Methodology](../authority/design-methodology.md);
- [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md);
- [Phase 007-D Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation](phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md);
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md);
- [Phase 006 Architecture Reconciliation Contract](phase-006-architecture-reconciliation-contract.md);
- [Operational Authority Continuity & Regressive Recovery Contract](../authority/operational-authority-continuity-regressive-recovery-contract.md);
- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](../decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md);
- [ADR-0009 — Non-Regressing Authority After Regressive Control-State Recovery](../decisions/ADR-0009-non-regressing-authority-after-regressive-control-state-recovery.md);
- accepted concepts, synchronizations and experience authority.

Earlier Phase 005-D concrete technology choices are implementation-planning evidence, not binding architecture under the current design freeze.

## Design result

007-E accepts the following persistence foundation:

> **Persistence preserves authority; it does not create semantic authority merely by storing a row, document, event, message, or file.**

> **A material owner transition must either commit its required same-boundary canonical facts atomically, or leave durable recoverable intent/state that makes incomplete cross-boundary coordination detectable and reconcilable.**

> **Compare-and-set protects the mutable authority state a caller observed; it does not decide whether the requested semantic transition is valid.**

> **Migration changes representation unless an explicit upstream semantic correction says otherwise. A schema migration must never silently rewrite historical meaning.**

## 1. Persistence responsibilities and non-responsibilities

### 1.1 Canonical control persistence

Canonical control persistence stores or durably references bounded authority facts required to identify, coordinate, inspect and explain SYNGAN work, including roles equivalent to:

- stable logical identities and authority scopes;
- immutable semantic revisions;
- immutable committed activity snapshots;
- owner-specific current lifecycle/applicability state;
- state-version/concurrency observations;
- promoted result associations;
- material transition/history facts;
- exact typed historical references;
- durable cross-boundary transition intent where required;
- tombstone/reference facts where retained history outlives payload availability;
- recovery-authority context required by later recovery architecture.

### 1.2 Data-plane payload is not ordinary control persistence

Control persistence does not absorb row-scale source/output data, large Learned State components, checkpoints, diagnostic datasets or full platform telemetry merely because those artifacts are durable.

Those remain data-plane/platform material referenced by bounded control state.

### 1.3 Physical durability is not semantic completion

A persisted candidate row, object-store file, message, checkpoint or external provider record does not by itself establish Learning completion, Generation completion, Evidence, cancellation, release approval or another owner's semantic transition.

The owning transition must be established through its own canonical authority contract.

## 2. Logical persistence ownership boundaries

007-E retains logical ownership rather than choosing one database/table per concept.

Architecture must preserve mutation authority equivalent to these boundaries:

1. **Revisioned semantic authority** — exact revisions and current future-use state for Data Meaning, Constraint, Strategy/configuration and Evaluation Criterion.
2. **Committed activity authority** — Learning, Generation and Evaluation occurrence identity, immutable commitment snapshot, current semantic lifecycle and result associations.
3. **Promoted-result authority** — Learned State, completed logical output and Evidence identity/current applicability or lifecycle as owned by each concept.
4. **Execution/operational authority** — Execution and subordinate operational history, refined later under the Execution/recovery design.
5. **Provenance authority** — typed historical assertions/relationships and corrections.
6. **Cross-boundary coordination state** — durable transition intent/dispatch/reconciliation facts when required coordination cannot complete atomically with the source owner.
7. **Derived read/search projections** — rebuildable/non-authoritative query acceleration and actor-facing composition.

These are logical mutation boundaries. Several may share one physical store; one logical boundary may span more than one physical mechanism when scale/security/deployment requires it.

A common technical persistence engine must not become a universal semantic `MetadataStore`, `Registry`, or generic CRUD owner.

## 3. Canonical write boundary

### 3.1 Owner validates; persistence commits

The semantic/application owner decides whether a material transition is allowed under its concept, synchronization, current authorization and other prerequisites.

Persistence is responsible for durably applying the already-authorized transition under the required consistency/concurrency preconditions.

A generic persistence layer must not provide an authority-bypassing operation equivalent to:

```text
set_status(resource_kind, resource_id, arbitrary_value)
```

where doing so would evade owner-specific transition rules.

### 3.2 Same-boundary coupled facts

When several canonical facts are required for one authority transition and are controlled by the same atomic persistence boundary, they must become visible together or not at all.

Examples include roles equivalent to:

- committed activity identity + immutable commitment snapshot;
- Learning completion + Learned State establishment/reference;
- Generation completion + completed-output association;
- Evaluation completion + established Evidence association;
- material lifecycle transition + required local material-history record;
- source owner state + durable outbox/transition intent for a required external follow-up.

The exact physical transaction mechanism is deferred.

### 3.3 No universal global transaction requirement

SYNGAN does not require one global ACID transaction, distributed two-phase commit, one database, or one event store across every authority and platform.

Where a synchronization crosses an atomic boundary, architecture requires **detectable, durable and reconcilable coordination**, not universal global atomicity.

## 4. Compare-and-set / stale-write architecture

### 4.1 Material mutable state needs conflict detection

Material current lifecycle/applicability state must support a conflict-detectable observed version/token equivalent to the Phase 007-D current-state version/freshness axis.

A mutation conceptually supplies:

```text
resource identity
expected current-state observation/version
requested owner action/transition
```

The write succeeds only if the relevant current authority still matches the required precondition.

### 4.2 CAS is not transition validation

A successful compare-and-set only proves that the observed mutable state had not been superseded at the protected boundary.

It does **not** prove that:

- the requested transition is semantically legal;
- current authorization remains sufficient unless authorization is part of the precondition;
- required dependency/runtime/recovery conditions hold;
- an external side effect occurred;
- the semantic result was established.

Those requirements remain owned by their respective authorities/synchronizations.

### 4.3 Conflict outcome is explicit

A stale or conflicting material write is not silently last-writer-wins.

Architecture must permit an outcome equivalent to:

```text
conflict / stale observation
→ refresh / recompute qualification / reconcile
```

The exact exception/result type is deferred.

### 4.4 CAS scope is owner-specific

There is no requirement for one global monotonically increasing version across all SYNGAN state.

The conflict token is scoped to the canonical mutable boundary whose concurrent mutation must be protected.

## 5. Transaction boundary design

### 5.1 Transaction follows invariant scope

A transaction boundary should be large enough to preserve one required invariant but not enlarged merely for convenience.

The architecture does not assume that every resource touched by one user workflow belongs in one transaction.

### 5.2 Read consistency is purpose-dependent

Current-state inspection, historical resolution, pre-commit readiness and high-consequence mutation may require different consistency/freshness guarantees.

007-E does not select snapshot isolation, serializable isolation, locking mode or provider-specific transaction levels universally.

A later persistence design must state which observation boundary is required for each material action rather than relying on a database default as semantic authority.

### 5.3 Time is not ordering authority

Timestamps are historical facts and diagnostics. They are not the sole concurrency or authority ordering mechanism for material transitions.

## 6. Durable outbox / transition-intent architecture

`Outbox` in 007-E names an **architectural role**, not necessarily a table, queue product, Kafka topic, message broker, library or particular event pattern.

### 6.1 When durable intent is required

If a canonical source-owner transition commits a requirement for a later action outside the same atomic boundary, architecture must retain durable state sufficient to establish:

- what required follow-up is intended;
- the exact source transition/identity it belongs to;
- enough idempotency/reconciliation identity to avoid ambiguous duplicate authority;
- current delivery/acknowledgement/reconciliation state where material;
- whether the follow-up remains current/authorized when retried.

### 6.2 Intent is not target success

Persisting an outbox/intent record establishes only that a follow-up is durably required/eligible under the source transition.

It does not establish that the target concept/platform performed or accepted the action.

### 6.3 At-least-once realization is compatible

Cross-boundary delivery may occur more than once physically.

The architecture must therefore permit idempotent acceptance, deduplication, fencing, receipt comparison or explicit reconciliation rather than assuming exactly-once physical delivery.

007-E does not select the mechanism.

### 6.4 Follow-up must be requalified where current authority matters

A durable old intent must not automatically bypass newer cancellation, revocation, recovery-authority, dependency or security state.

Where current authority is required at realization time, dispatch/retry must requalify against current authority before producing a new effect.

### 6.5 No generic event bus as semantic owner

Events/messages may transport facts or intent later, but a broker record cannot become the source of semantic truth merely because it is easier to consume than the canonical owner.

## 7. Material transition history

### 7.1 Append-preserving material history

The control plane must retain enough append-preserving history to explain material state changes, establishment/promotion, supersession/invalidation, cancellation/reconciliation, correction, and other transitions whose historical occurrence matters.

### 7.2 Full event sourcing remains optional

007-E does not require every current state field to be rebuilt from a universal event stream and does not require every read/cache/internal update to become an immutable event.

A deployment may use event sourcing if it satisfies the same authority contracts, but the canonical architecture supports current-state projections plus material historical records.

### 7.3 History record is not copied domain authority

A transition-history record explains that an authority transition occurred and retains the material references/basis required for audit/history.

It should not become a duplicated mutable copy of the entire referenced authority state.

### 7.4 Reconstruction remains qualified

After recovery, a transition may be reconstructed from retained evidence only under the owner-specific reconstruction rules established by Phase 006.

Reconstructed history must remain distinguishable from directly retained original history.

## 8. Historical-reference resolution

### 8.1 Exact target first

Historical resolution attempts the exact typed identity/revision/snapshot referenced.

It must never silently replace the target with:

- current/latest semantic revision;
- newest Learned State;
- current alias target;
- replacement dependency;
- newest Evidence;
- a newly generated resource with superficially equivalent content.

### 8.2 Resolution outcomes

Internal architecture must preserve outcomes equivalent to:

- resolved exact target;
- withheld/redacted or intentionally non-disclosing;
- known identity but retained representation unavailable;
- unknown/indeterminate;
- invalid/integrity-defective reference;
- unsupported representation/schema.

`Absent` remains distinct: no such relationship/value was established in the relevant authority context.

### 8.3 Tombstone/reference preservation

When policy permits detailed payload/state to expire but retained history still references the identity, architecture should preserve enough bounded identity/reference information to avoid rewriting the history as if the target never existed.

The exact retention/erasure policy is not selected here.

### 8.4 Actor-safe resolution

Authorization/disclosure may alter what an actor is told about resolution without changing the underlying reference identity or internal canonical history.

## 9. Derived indexes and projections

Search indexes, lists, dashboards, navigation graphs and denormalized read models may combine several authority families for efficient interaction.

They are derived projections and must:

- retain enough source identity/version/freshness context to interpret results;
- not acquire canonical mutation authority;
- tolerate rebuild/repair when their platform is unavailable or stale;
- not be accepted as proof of a semantic transition when canonical authority disagrees or is unknown.

Projection failure therefore does not automatically imply canonical-history failure.

## 10. Persistence representation and serialization

007-D separated portable reference serialization, actor-safe bounded views and persistence-oriented representation. 007-E preserves that separation.

Persistence representation may choose a technology-specific shape later, but must preserve:

- logical identity;
- exact semantic revision/commitment meaning;
- mutable state-version semantics;
- representation schema version;
- typed references;
- material history/reconstruction quality;
- disclosure/history distinctions where applicable.

Persistence representation is not automatically the public wire schema.

## 11. Schema migration architecture

### 11.1 Migration is representation change by default

A persistence-schema migration changes how canonical facts are stored/interpreted.

It must not silently create:

- a new semantic revision;
- a new committed activity;
- a new promoted result;
- a new Evidence finding;
- a semantic correction;
- a change from unknown/unavailable to known/success.

If a product/design correction changes meaning, that correction must use the owning semantic authority in addition to any representation migration required to store it.

### 11.2 Migration revision is another technical axis

A deployment's migration sequence/revision is distinct from:

- resource identity;
- semantic revision;
- commitment snapshot;
- mutable state version;
- representation schema version;
- Attempt epoch;
- recovery-authority frontier/incarnation;
- package/application version.

Do not overload one generic `version` field across these roles.

### 11.3 Migration preserves historical referenceability

Compatible migration must preserve enough mapping/equivalence that retained references continue to resolve to the same logical historical authority where the target remains retained and supported.

### 11.4 Large migrations may be incremental

Architecture allows online, staged, background or chunked migration where necessary for enterprise-scale control state.

Incremental migration must retain explicit compatibility/transition state rather than exposing a partially migrated representation as though one uniform schema already exists.

007-E does not choose dual-write, shadow tables, expand/contract, copy-on-write or another mechanism.

### 11.5 Migration must be restartable/reconcilable where interruption is possible

If migration may partially execute, architecture must have enough durable migration state/progress/identity to determine what has happened and safely continue, reconcile or abort according to the migration's contract.

A deployment must not infer completion solely from process exit or elapsed time.

## 12. Rollback, restore and migration interaction

007-E distinguishes two fundamentally different operations.

### 12.1 Representation/code rollback without authority regression

A deployment may roll back application code or schema compatibility posture while canonical current authority remains non-regressed, if the retained representation remains safely interpretable under the supported compatibility contract.

This is a compatibility/deployment operation, not automatically a semantic recovery event.

### 12.2 Canonical-state/data rollback

Any migration rollback, database restore or storage operation that may replace current canonical control state with an older point is a **potentially regressive restore**.

It therefore invokes the Phase 006/ADR-0009 recovery rules:

```text
restored persistence
        !=
current mutation authority
```

A fresh non-regressing recovery-authority frontier and reconciliation are required before ordinary mutation authority resumes.

### 12.3 `Down migration` cannot undo historical semantics by convenience

A schema tool's ability to run a reverse migration must not be interpreted as permission to erase or reverse domain transitions that occurred while the newer schema was active.

Representation rollback and semantic correction are different authorities.

## 13. Backup/restore identity and cloning

Persistence architecture must distinguish:

- **disaster recovery continuation** — restoration intends to continue the same logical authority, subject to non-regressing recovery rules;
- **clone/fork/test copy** — copied state becomes a distinct authority scope unless an explicit federation/continuation contract says otherwise.

A clone must not accidentally present itself as the original authority merely because it copied the original database bytes.

The exact authority-scope encoding remains deferred.

## 14. Security and sensitive persistence

007-E does not select encryption/KMS/secrets products, but persistence architecture must remain capable of:

- storing secret references instead of long-lived bearer secrets in ordinary canonical records;
- separating actor-safe views from precise internal authorization/audit facts;
- applying retention/erasure policy without falsifying unrelated canonical history;
- keeping security audit distinct from semantic transition history while linking them by stable references where material.

## 15. Enterprise-scale control-state boundary

Control persistence must remain bounded by logical resources, revisions, transitions, Attempts/checkpoints, manifests/references, Evidence summaries and other material control facts—not source/output row counts, individual tokens, executor task events or full diagnostic datasets.

A persistence design that requires row-per-generated-record control authority or whole-output embedding into canonical control records violates the architecture.

## 16. Design scenarios / falsification probes

### Scenario A — stale current-state mutation

Two actors observe Generation state version 12. One valid transition commits and advances current state. The second attempts a material transition against its stale observation.

**Result:** stale write is rejected/requalified; persistence does not use silent last-writer-wins.

### Scenario B — Generation promotion and history in one store

Generation completion, completed-output association and required local transition history are within one atomic control boundary.

**Result:** they commit together or not at all.

### Scenario C — semantic transition requires external effect

A committed owner transition requires a later platform/catalog action that cannot be in the same transaction.

**Result:** source transition commits with durable cross-boundary intent; external effect may realize at least once and is reconciled/idempotent. Intent existence is not target success.

### Scenario D — crash after source commit before dispatch

The process dies after the source transaction commits but before external follow-up starts.

**Result:** durable intent survives and permits later reconciliation without fabricating source rollback or target success.

### Scenario E — duplicate dispatch

A worker retries an unacknowledged cross-boundary action and the external call occurs twice physically.

**Result:** duplicate physical realization does not create duplicate semantic authority; target acceptance/reconciliation uses stable identity/idempotency/fencing as later designed.

### Scenario F — historical revision unavailable

A historical Generation references Data Meaning R1; its detailed retained representation has expired while the identity/tombstone remains.

**Result:** reference resolves as known-but-unavailable, not to current R4 and not to ordinary absence.

### Scenario G — read projection lost

A search/index store is unavailable while canonical owner persistence remains intact.

**Result:** search/navigation is degraded; canonical truth is not considered lost merely because the projection disappeared.

### Scenario H — migration changes field layout only

Persistence schema S1 is migrated to S2 with the same logical Generation and commitment meaning.

**Result:** logical identity and semantic snapshot remain unchanged; only representation/migration state changes.

### Scenario I — partial enterprise migration

A large migration transforms only part of the control corpus before interruption.

**Result:** migration state records the mixed/partial condition and supports restart/reconciliation; the deployment does not pretend the entire corpus is uniformly S2.

### Scenario J — database restored behind current workers

A control-store snapshot predating a newer Attempt/cancellation/security state is restored.

**Result:** restored rows are historical evidence, not current writer authority; ADR-0009 recovery restriction/frontier applies.

### Scenario K — reverse migration wants to delete a newly introduced field containing material historical context

A schema rollback would make newer retained material unrepresentable.

**Result:** rollback is blocked/qualified until compatibility or preservation strategy exists; a migration tool's `down` capability cannot silently erase historical meaning.

### Scenario L — copied database starts as a test deployment

A development environment copies production-like control state.

**Result:** the copy needs a distinct authority scope unless deliberately acting as the same recovered authority under an explicit recovery contract.

No scenario requires a new domain concept or synchronization.

## 17. Earlier Phase 005-D implementation choices

Phase 005-D selected concrete implementation technologies and encodings to make implementation planning executable at that time, including roles equivalent to UUIDv4 identifiers, JSON codecs, SQLAlchemy Core, Alembic, PostgreSQL, SQLite and Psycopg.

Under the current architecture-design continuation:

- those choices remain valuable feasibility/planning evidence;
- they are **not current architecture requirements**;
- 007-E neither accepts nor rejects them as eventual implementation selections;
- a later implementation re-entry must re-evaluate them against the final architecture, current ecosystem and deployment requirements before adoption.

Likewise concrete Phase 005-D names such as `AuthorityId`, `ResourceId`, `ResourceRef`, `StateVersion`, repository classes or `SynGANClient` remain implementation spellings unless independently promoted by later architecture.

## 18. Deferred architecture/implementation choices

007-E intentionally leaves open:

- relational vs document vs key/value vs event-oriented persistence technology;
- one store vs several physical stores;
- exact identifier encoding;
- exact transaction/isolation/locking mechanism;
- exact CAS token type;
- literal outbox table vs queue/log/intent-store realization;
- broker/event technology;
- ORM/query-builder/data-access library;
- PostgreSQL/SQLite/other database support;
- migration framework/tool;
- physical schema/table/document names;
- indexing strategy;
- retention periods and erasure policy;
- exact backup technology;
- exact online migration algorithm;
- exact public/wire codecs;
- concrete repository/unit-of-work class names;
- executable persistence tests or migration harness.

## 19. Concept / synchronization audit

007-E introduces **no new concept**.

Persistence transaction, state token, outbox/intent, migration, tombstone, journal and projection remain architecture mechanisms.

Accepted concept count remains **11**.

007-E introduces **no new synchronization**. Existing concept synchronizations remain sufficient; 007-E specifies how later persistence may preserve them across atomic and non-atomic technical boundaries.

Accepted synchronization count remains **15**. No `SYNC-16` is created.

## 20. Architecture invariants

1. Persistence does not create semantic authority merely by storing physical state.
2. Canonical mutation remains owner-controlled; generic persistence cannot bypass lifecycle/synchronization rules.
3. Same-boundary facts required for one authority transition become visible atomically or not at all.
4. Cross-boundary required work retains durable detectable/reconcilable intent when atomic completion is impossible.
5. Durable intent is not proof of target success.
6. Duplicate physical delivery/effect must not create duplicate semantic authority.
7. Material current-state writes use conflict-detectable observation/version semantics; no silent last-writer-wins.
8. CAS does not substitute for semantic transition validation or current authorization/recovery qualification.
9. No universal global transaction/2PC/event-store architecture is required.
10. Material historical transitions remain append-preserving enough for explanation/recovery; full event sourcing remains optional.
11. Historical resolution attempts the exact referenced target and never silently substitutes `latest`.
12. Known-unavailable/unknown/withheld/invalid/unsupported remain distinguishable from absence where disclosure permits.
13. Derived indexes/projections do not become canonical mutation authority.
14. Schema migration changes representation unless explicit semantic authority says meaning changed.
15. Migration revision remains distinct from semantic revision, state version, representation schema version and recovery authority.
16. Interrupted migrations must remain detectable/restartable/reconcilable where partial execution is possible.
17. A canonical-state rollback is a potentially regressive recovery event and cannot revive stale mutation authority.
18. Representation rollback cannot silently erase or reverse semantic history.
19. A copied control store does not automatically retain the original authority scope when used as a clone/fork.
20. Control persistence remains bounded and does not absorb distributed row-scale payloads by default.
21. Earlier Phase 005-D technology choices remain provisional planning evidence until explicit implementation re-entry.
22. 007-E does not authorize production persistence implementation or new executable enforcement.

## Exit condition

007-E design is complete when:

- persistence ownership and canonical write boundaries are explicit;
- transaction/CAS/outbox roles preserve owner authority without selecting technology prematurely;
- historical resolution and projection boundaries remain truthful under retention/failure;
- migration and rollback are separated from semantic change and regressive recovery;
- earlier concrete implementation-planning choices are clearly classified as provisional;
- no new concept/synchronization is required;
- implementation remains frozen pending later design completion/re-entry.
