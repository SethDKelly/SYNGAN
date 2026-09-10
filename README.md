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
- [`007-G Strategy/Method Binding, Dependency Trust, Authorization, Secrets & Distributed Runtime Closure Foundation`](docs/architecture/phase-007-g-strategy-method-binding-dependency-trust-authorization-secrets-distributed-runtime-closure-foundation.md)
- [`Phase 007 index`](docs/phases/007/index.md)

## Status

- Phases 001–006 — retained design/planning/readiness history
- 007-A through 007-C — retained historical/provisional bootstrap work
- **007-D — complete as architecture design**
- **007-E — complete as architecture design**
- **007-F — complete as architecture design**
- **007-G — complete as architecture design**
- **007-H — next eligible design subgroup, not started**
- **Production implementation expansion — frozen**

Phase 006 historically concluded that design was complete enough to consider implementation. The project later reopened architecture design so existing source/tests do not prematurely harden unsettled representation choices.

## Current architecture results

007-D separates logical identity, immutable semantic revision/commitment, mutable current-state version/freshness and representation schema version.

007-E establishes technology-neutral persistence, transaction, CAS, durable-intent, exact-history and migration/recovery boundaries.

007-F establishes the distributed data-state foundation: logical subject versus physical representation, bounded logical scopes, exact source-state/coordination strength, bounded manifests, candidate/seal separation and Generation-owned promotion.

007-G establishes the executable realization/security/runtime foundation:

```text
semantic Strategy / method / activity commitment
        ↓
implementation binding
        ↓
exact implementation + dependency closure
        ↓
identity / integrity / trust / compatibility
        ↓
current authorization + network/egress qualification
        ↓
role-specific distributed runtime closure
        ↓
immutable Attempt invocation
        +
current scoped capabilities / secret access
        ↓
physical runtime realization
```

Important consequences include:

- semantic Strategy/method identity is not a plugin/package/model/runtime identity;
- one binding may resolve multiple exact implementation/artifact components;
- one Attempt cannot silently hot-swap a missing binding/dependency/model/service;
- a later Attempt may use another compatible binding only when the unchanged semantic commitment permits that operational choice and history records the new realization;
- dependency presence, exact identity, integrity/authenticity, trust/approval, compatibility and current authorization remain distinct;
- explicit provisioning is separate from execution and missing runtime dependencies cannot trigger hidden installation/model-hub access/remote fallback;
- network connectivity is not the same thing as data-egress permission;
- live runtime capabilities and secret values do not become durable semantic authority;
- driver readiness does not imply executor/worker readiness;
- dynamic workers must inherit/prove the required role-specific closure before material work;
- large Learned State/model/artifact loading cannot universally depend on driver broadcast;
- implementation topology limitations cannot simplify or redefine committed topology semantics.

Earlier concrete Phase 005 implementation choices remain possible candidates to reassess at implementation re-entry rather than current architecture requirements.

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

**007-H — Execution/Attempt, Idempotency, Fencing, Non-Regressing Recovery, Checkpoint, Cancellation & Admission Foundation** is next eligible as a **design** subgroup.

An explicit proceed decision is required before it begins. Production implementation remains frozen independently of design progression.
