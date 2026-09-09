# SYNGAN

SYNGAN is a design-first synthetic-data generation framework intended for Spark-scale workloads.

SYNGAN follows Daniel Jackson-style concept design: problem/concept/experience authority precedes representation and implementation choices.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current architecture/design posture:

- [`Phase 007 Design Continuation & Implementation Freeze`](docs/authority/phase-007-design-continuation-implementation-freeze.md)
- [`007-D Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation`](docs/architecture/phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md)
- [`007-E Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline`](docs/architecture/phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md)
- [`Phase 007 index`](docs/phases/007/index.md)

## Status

- Phases 001–006 — retained design/planning/readiness history
- 007-A through 007-C — retained historical/provisional bootstrap work
- **007-D — complete as architecture design**
- **007-E — complete as architecture design**
- **007-F — next eligible design subgroup, not started**
- **Production implementation expansion — frozen**

Phase 006 historically concluded that design was complete enough to consider implementation. The project later reopened architecture design so existing source/tests do not prematurely harden unsettled representation choices.

## Current architecture results

007-D separates logical identity, immutable semantic revision/commitment, mutable current-state version/freshness and representation schema version. Handles resolve/present authority; serialization is representation rather than write authority.

007-E establishes a technology-neutral persistence baseline:

```text
owner validates semantic transition
        ↓
persistence commits under consistency preconditions
        ↓
same-boundary coupled facts atomically visible
        ↓
required cross-boundary work gets durable reconcilable intent
```

It also preserves:

- stale-write conflict detection without treating CAS as semantic validation;
- material transition history without universal event sourcing;
- exact historical references without silent `latest` substitution;
- derived indexes/search views as non-authoritative;
- migration as representation change by default;
- migration revision distinct from semantic/state/schema/recovery versions;
- canonical-state rollback as potentially regressive recovery under ADR-0009.

Earlier Phase 005-D choices such as UUIDv4, JSON codecs, SQLAlchemy Core, Alembic, PostgreSQL and SQLite remain possible implementation candidates, not current architecture requirements.

## Provisional executable scaffold

The repository still contains the 007-B/007-C package/tool/test scaffold. It is feasibility/history evidence, **not upstream design authority**, and may be revised at a later implementation re-entry.

No new tests or executable architecture enforcement are being added while architecture design remains active.

## Locked semantic baseline

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
```

No `SYNC-16`.

Complete structured-data target:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

The complete supported baseline also requires source-derived/local free-form-text synthesis without mandatory public model-hub or runtime inference-service dependency.

## Current next boundary

**007-F — Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation** is next eligible as a **design** subgroup.

An explicit proceed decision is required before it begins. Production implementation remains frozen independently of design progression.
