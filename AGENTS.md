# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in architecture/design refinement, not production implementation.**

Current design authority includes:

- `docs/authority/phase-007-design-continuation-implementation-freeze.md`
- `docs/architecture/phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md`
- `docs/architecture/phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md`
- `docs/phases/007/index.md`

Current progression:

```text
007-A..007-C  historical/provisional bootstrap work
007-D         DESIGN COMPLETE
007-E         DESIGN COMPLETE
007-F         next eligible DESIGN subgroup — not started
implementation expansion   FROZEN
```

Accepted counts remain 11 concepts / 15 synchronizations / 10 ADRs. No `SYNC-16`.

## Primary rule

> **Design may invalidate provisional implementation; provisional implementation may not veto design.**

The existing `src/syngan`, tests, Import Linter rules and CI are retained feasibility/history artifacts from 007-B/007-C. They are not upstream architecture authority.

## What agents may do now

For an explicitly entered design subgroup, agents may:

- inspect directly relevant problem/concept/synchronization/experience/architecture authority;
- create/refine architecture documentation;
- compare alternatives and preserve unresolved choices;
- record future verification obligations as non-executable design requirements;
- update canonical navigation when design is accepted;
- create an ADR only when a material architecture choice benefits from durable alternatives/rationale.

## What agents must not do during the design freeze

Unless later implementation re-entry explicitly authorizes it, do not:

- add production source behavior;
- add persistence schemas/migrations;
- add Spark/runtime/model/platform/security adapters;
- add concrete public API classes merely to crystallize a hypothesis;
- add production serialization/wire schemas;
- add runtime/build dependencies for future capability work;
- add new tests or executable architecture/fitness restrictions for evolving design;
- add Import Linter constraints for evolving design;
- add CI/deployment/release enforcement for evolving architecture.

Existing verification may continue. Its assertions are provisional where they encode earlier delivery-state assumptions.

## Current design distinctions

Preserve at minimum:

- logical identity != semantic revision != mutable state version != representation schema version;
- handle/view != canonical state owner;
- serialization != mutation authority;
- persistence durability != semantic completion;
- owner semantic validation != persistence CAS success;
- durable outbox/intent != target success;
- exact historical reference != current/latest substitution;
- material history != derived read/search projection;
- migration revision != semantic/state/schema/recovery version;
- representation migration != semantic correction;
- canonical-state rollback = potentially regressive recovery requiring ADR-0009 qualification;
- restored stale control state != current mutation authority;
- semantic completion != runtime/platform success;
- candidate/checkpoint/diagnostic material != promoted result;
- favorable empirical privacy Evidence != formal privacy guarantee != external release approval.

## 007-E design result

007-E is technology-neutral. It does **not** mandate SQL, SQLAlchemy, Alembic, PostgreSQL, SQLite, UUIDv4, JSON, a literal outbox table or a global event bus.

Earlier Phase 005-D concrete selections remain implementation-planning evidence to reconsider only after architecture design reaches explicit implementation re-entry.

## Progressive disclosure

For design work:

1. read `docs/index.md`;
2. read the Phase 007 design-continuation/freeze authority;
3. read `docs/phases/007/index.md`;
4. read only the concepts/synchronizations/experience/architecture directly relevant to the active design question;
5. use phase/implementation history only for rationale/feasibility evidence.

Do not load or duplicate the full corpus by default.

## Current next boundary

**007-F — Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation** is the next eligible **design** subgroup.

Do not begin 007-F until explicitly requested. Do not resume production implementation unless a separate implementation-reentry decision is made.
