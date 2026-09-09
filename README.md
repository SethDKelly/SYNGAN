# SYNGAN

SYNGAN is a design-first synthetic-data generation framework intended for Spark-scale workloads.

SYNGAN follows Daniel Jackson-style concept design: problem/concept/experience authority precedes representation and implementation choices.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current design posture:

- [`Phase 007 Design Continuation & Implementation Freeze`](docs/authority/phase-007-design-continuation-implementation-freeze.md)
- [`Phase 007-D Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation`](docs/architecture/phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md)
- [`Phase 007 index`](docs/phases/007/index.md)

Repository-wide automated-agent rules are in [`AGENTS.md`](AGENTS.md).

## Status

- Phases 001–006 — retained design/planning/readiness history
- 007-A through 007-C — retained historical/provisional bootstrap work
- **007-D — complete as architecture design**
- **007-E — next eligible design subgroup, not started**
- **Production implementation expansion — frozen**

Phase 006 historically concluded that the design was complete enough to consider implementation. The project has since explicitly reopened architecture design so existing source/tests do not prematurely harden unsettled representation choices.

## 007-D architecture result

007-D separates:

```text
authority / namespace scope
stable logical identity
exact semantic revision / commitment snapshot
mutable state version / view freshness
representation schema version
external/provider identity or locator when material
```

It also establishes that:

- typed references preserve exact historical identity rather than silently resolving `latest`;
- handles resolve/present authority rather than own canonical state;
- handles are not inherently credentials;
- local handle/view mutation is not canonical mutation;
- serialization is representation, not write authority;
- schema migration is distinct from semantic revision;
- programmatic views preserve semantic/current, historical, actionability, operational, Evidence/Provenance, disclosure and topology-summary concerns without collapsing them into one universal status/result;
- bounded control-plane views reference large/distributed payloads rather than collecting them.

007-D intentionally did **not** select concrete identifier formats, Python public classes, wire formats, serializers, persistence schemas, CAS/outbox mechanisms, migration tooling, tests or executable architecture restrictions.

## Provisional executable scaffold

The repository still contains the 007-B/007-C package/tool/test scaffold, including `src/syngan/`, the existing verification workflow and Import Linter rules.

That scaffold is retained as feasibility/history evidence. It is **not upstream design authority** and may be revised during a later implementation re-entry if current architecture design requires it.

No new implementation/test enforcement is being added while architecture design remains active.

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

**007-E — Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline** is next eligible as a **design** subgroup.

An explicit proceed decision is required before it begins. Production implementation remains frozen independently of design progression.
