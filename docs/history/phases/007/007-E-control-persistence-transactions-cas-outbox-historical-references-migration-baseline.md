---
type: Phase Record
title: 007-E — Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline
status: complete
---

# 007-E — Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline

## Objective

Refine the control-plane persistence architecture beneath the Phase 007-D identity/reference foundation without allowing prior implementation planning or the provisional 007-A through 007-C scaffold to harden concrete storage technologies prematurely.

007-E remains architecture/design work under the Phase 007 implementation freeze.

## Governing authority reviewed

007-E reconciled and refined:

- `docs/architecture/phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md`;
- `docs/architecture/control-plane-identity-revision-state-persistence-historical-reference.md`;
- `docs/architecture/phase-006-architecture-reconciliation-contract.md`;
- `docs/authority/operational-authority-continuity-regressive-recovery-contract.md`;
- ADR-0002 and ADR-0009;
- the historical Phase 005-D persistence implementation plan as implementation-planning evidence.

## Result

**PASS — CONTROL PERSISTENCE / TRANSACTION / CAS / DURABLE-INTENT / HISTORICAL-REFERENCE / MIGRATION FOUNDATION REFINED AS ARCHITECTURE DESIGN.**

Canonical result:

`docs/architecture/phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md`

## Core decisions

007-E establishes:

> Persistence preserves authority; storing a row/document/event/message/file does not by itself create semantic authority.

> Same-boundary canonical facts required for one material owner transition must become visible atomically or not at all.

> Required coordination that cannot complete in one atomic boundary must leave durable detectable/reconcilable transition intent.

> Compare-and-set protects an observed mutable authority state but does not decide whether the semantic transition is valid.

> Migration changes representation by default; semantic change/correction remains owned upstream.

## Persistence ownership

Architecture preserves logical mutation authority for:

- revisioned semantic authorities;
- committed activity occurrences and immutable commitment snapshots;
- promoted semantic results;
- Execution/operational state;
- Provenance assertions/history;
- cross-boundary durable intent/reconciliation state;
- derived read/search projections.

These logical boundaries do not imply one physical database per owner or one universal database for all owners.

A shared persistence technology must not become a universal semantic MetadataStore/Registry/CRUD owner.

## Canonical write and transaction boundary

Owner/application logic validates semantic legality and current prerequisites.

Persistence durably applies the authorized transition under the required conflict/transaction preconditions.

Where one atomic boundary owns all required facts, facts such as commitment + snapshot, Generation completion + output association, or Evaluation completion + Evidence association must commit together or not at all.

No universal global transaction, distributed two-phase commit or event-sourcing model is required.

## CAS / stale-write boundary

Material mutable state requires conflict-detectable observation/version semantics.

A stale write cannot silently win.

A CAS success proves only that the protected observation/precondition still held; it does not prove transition legality, current authorization, dependency/runtime compatibility, recovery qualification, external side-effect success or semantic result establishment.

The exact token type and storage mechanism remain deferred.

## Durable outbox / transition intent

`Outbox` is treated as an architectural role, not a required table/broker/product.

When a committed source transition requires later work outside its atomic boundary, durable state must preserve the exact intent/source identity and enough idempotency/reconciliation context to survive process failure and duplicate physical delivery.

Intent existence does not mean the target action succeeded.

Retry/dispatch must requalify against current authority where cancellation, revocation, dependency, security or recovery state matters.

## Material history

The control plane retains append-preserving material transition history sufficient for explanation/recovery without requiring universal full event sourcing.

History records explain transitions and retain exact material references; they do not become duplicated mutable owner state.

Reconstructed post-recovery history remains explicitly distinguishable from directly retained original history.

## Historical references

Historical resolution remains exact-target-first and never silently substitutes current/latest.

Architecture retains distinctions equivalent to:

```text
resolved
withheld/redacted/non-disclosing
known but unavailable
unknown / indeterminate
invalid / integrity defective
unsupported representation/schema
```

`Absent` remains separate.

Where detailed payload expires but retained history still points to the identity, bounded tombstone/reference state may preserve the known historical relationship rather than rewriting it as absence.

## Migration baseline

007-E distinguishes:

```text
semantic revision
current-state version
representation schema version
deployment migration revision
recovery-authority frontier
```

A migration revision is not another name for any of the other axes.

Schema migration must preserve logical identity, historical meaning and typed references when semantics have not changed.

Large migrations may be staged/incremental, but partial state must remain explicit and safely restartable/reconcilable rather than masquerading as a uniformly migrated corpus.

## Rollback / recovery distinction

A compatible code/schema rollback that does not regress canonical authority is a deployment/representation concern.

A database restore, migration rollback or other operation that may replace current canonical state with older control state is a potentially regressive recovery event governed by ADR-0009:

```text
restored persistence
        !=
current mutation authority
```

A schema tool's reverse-migration capability is never permission to erase/reverse domain history by convenience.

## Backup/clone identity

007-E distinguishes disaster-recovery continuation of the same logical authority from a copied/forked/test deployment.

A clone does not automatically inherit the original authority scope simply because it copied database bytes.

The exact authority-scope encoding remains deferred.

## Phase 005-D technology disposition

The earlier plan selected UUIDv4, JSON codecs, SQLAlchemy Core, Alembic, PostgreSQL, SQLite, Psycopg and concrete class/repository names.

007-E does not reject those choices as future implementation candidates, but it no longer treats them as settled architecture.

They remain feasibility/planning evidence to be re-evaluated at implementation re-entry after architecture design is complete.

## Falsification scenarios reviewed

007-E tested the design against:

- competing stale lifecycle writes;
- same-store Generation promotion + history;
- cross-boundary external action after source commit;
- crash before outbox dispatch;
- duplicate dispatch;
- exact historical revision whose payload has expired;
- failed read/search projection with intact canonical persistence;
- schema layout migration without semantic change;
- interrupted large migration leaving mixed representation state;
- database restore behind surviving workers;
- reverse migration that would erase newer historical meaning;
- cloned database used as a separate test deployment.

The architecture remained coherent without a new concept or synchronization.

## Concept / synchronization audit

```text
accepted concepts          11
accepted synchronizations  15
new concepts               0
new synchronizations       0
SYNC-16                     absent
```

Transaction, CAS token, outbox/intent, journal, tombstone, migration and projection remain architecture mechanisms.

## Explicitly deferred

007-E intentionally does not select:

- database/storage technology;
- SQL vs document vs key/value vs event-oriented realization;
- ORM/query/data-access library;
- identifier encoding;
- transaction isolation/locking mechanism;
- CAS token representation;
- literal outbox mechanism or broker;
- physical schema/table/document names;
- migration framework/tool;
- PostgreSQL/SQLite/provider support;
- retention periods or erasure policy;
- backup technology;
- online migration algorithm;
- public/persistence codecs;
- concrete repository/unit-of-work classes;
- persistence/migration tests or enforcement.

## Repository change boundary

007-E changed documentation/architecture authority only.

It introduced:

- no production source behavior;
- no persistence dependency;
- no database schema;
- no migration configuration;
- no repository/transaction/CAS/outbox implementation;
- no new tests;
- no Import Linter changes;
- no CI/deployment enforcement.

The retained Phase 007-A through 007-C scaffold remains provisional evidence under the implementation freeze.

## Exit decision

**007-E DESIGN: COMPLETE.**

**007-E IMPLEMENTATION: NOT AUTHORIZED.**

The next eligible **design** subgroup is:

**007-F — Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation**.

007-F does not begin automatically; explicit proceed authority is required.
