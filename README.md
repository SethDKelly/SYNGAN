# SYNGAN

SYNGAN is a design-first synthetic-data generation framework intended for Spark-scale workloads.

SYNGAN follows Daniel Jackson-style concept design: problem/concept/experience authority precedes representation and implementation choices.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current architecture/design posture:

- [`Phase 007 Design Continuation & Implementation Freeze`](docs/authority/phase-007-design-continuation-implementation-freeze.md)
- [`007-D Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation`](docs/architecture/phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md)
- [`007-E Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline`](docs/architecture/phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md)
- [`007-F Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation`](docs/architecture/phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md)
- [`Phase 007 index`](docs/phases/007/index.md)

## Status

- Phases 001–006 — retained design/planning/readiness history
- 007-A through 007-C — retained historical/provisional bootstrap work
- **007-D — complete as architecture design**
- **007-E — complete as architecture design**
- **007-F — complete as architecture design**
- **007-G — next eligible design subgroup, not started**
- **Production implementation expansion — frozen**

Phase 006 historically concluded that design was complete enough to consider implementation. The project later reopened architecture design so existing source/tests do not prematurely harden unsettled representation choices.

## Current architecture results

007-D separates logical identity, immutable semantic revision/commitment, mutable current-state version/freshness and representation schema version. Handles resolve/present authority; serialization is representation rather than write authority.

007-E establishes a technology-neutral persistence baseline around owner validation, atomic same-boundary coupled facts, durable reconcilable cross-boundary intent, stale-write conflict detection, material history, exact historical references, representation-oriented migration and regressive-recovery semantics.

007-F establishes the distributed data-state foundation:

```text
mutable selector/access
        ↓
exact logical data state
        ↓
open distributed candidate
        ↓
sealed immutable physical subject
        ↓
owner validation
        ↓
Generation promotion
        ↓
one logical completed output
```

Important consequences include:

- logical subjects and physical representations remain distinct;
- single-table, time-series, multi-table shared-key and composite subjects use bounded logical scopes rather than one exclusive topology enum;
- exact source-state claims separate identity, rereadability, integrity, retention and cross-scope coordination strength;
- individually exact tables do not automatically imply a coherent multi-table snapshot;
- manifests remain bounded roots over distributed/hierarchical/provider-native detail;
- partial/scope-level candidate completion is never whole-output completion;
- sealing creates an exact immutable physical subject but does not prove Constraints, privacy, fidelity or Generation completion;
- required completion Evaluation binds the exact sealed subject;
- promotion may reuse sealed distributed bytes rather than copying the full corpus;
- later equivalent compaction/relocation can preserve logical output identity while the original promotion basis remains historical fact;
- normal operation must not require full-corpus collection or driver-local enumeration of all distributed components.

Earlier Phase 005-D/E concrete choices such as PostgreSQL/SQLAlchemy/Alembic or a portable Parquet manifest profile remain possible implementation candidates, not current architecture requirements.

## Provisional executable scaffold

The repository still contains the 007-B/007-C package/tool/test scaffold. It is feasibility/history evidence, **not upstream design authority**, and may be revised at a later implementation re-entry.

No new tests or executable architecture enforcement are being added while architecture design remains active. Older delivery-state assertions may therefore remain intentionally stale until implementation re-entry.

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

**007-G — Strategy/Method Binding, Dependency Trust, Authorization, Secrets & Distributed Runtime Closure Foundation** is next eligible as a **design** subgroup.

An explicit proceed decision is required before it begins. Production implementation remains frozen independently of design progression.
