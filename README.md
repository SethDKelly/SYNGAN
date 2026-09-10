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
- [`007-H Execution/Attempt, Idempotency, Fencing, Non-Regressing Recovery, Checkpoint, Cancellation & Admission Foundation`](docs/architecture/phase-007-h-execution-attempt-idempotency-fencing-non-regressing-recovery-checkpoint-cancellation-admission-foundation.md)
- [`Phase 007 index`](docs/phases/007/index.md)

## Status

- Phases 001–006 — retained design/planning/readiness history
- 007-A through 007-C — retained historical/provisional bootstrap work
- **007-D — complete as architecture design**
- **007-E — complete as architecture design**
- **007-F — complete as architecture design**
- **007-G — complete as architecture design**
- **007-H — complete as architecture design**
- **007-I — next eligible design subgroup, not started**
- **Production implementation expansion — frozen**

Phase 006 historically concluded that design was complete enough to consider implementation. The project later reopened architecture design so existing source/tests do not prematurely harden unsettled representation choices.

## Current architecture results

007-D separates logical identity, immutable semantic revision/commitment, mutable current-state version/freshness and representation schema version.

007-E establishes technology-neutral persistence, transaction, CAS, durable-intent, exact-history and migration/recovery boundaries.

007-F establishes the distributed data-state foundation: logical subject versus physical representation, bounded logical scopes, exact source-state/coordination strength, bounded manifests, candidate/seal separation and Generation-owned promotion.

007-G establishes the executable realization/security/runtime foundation: semantic Strategy/method authority remains distinct from exact implementation/dependency closure, current trust/authorization, secrets and role-specific distributed runtime realization.

007-H establishes the execution/recovery/admission foundation:

```text
committed activity / stable Execution
        ↓
current admission + recovery-continuity qualification
        ↓
non-regressing recovery-authority frontier
        ↓
current Attempt authority + resource-local preconditions
        ↓
immutable Attempt invocation
        ↓
physical work and non-final effects
        ↓
reconciliation + semantic-owner validation
```

Important consequences include:

- Attempt physical/observed state is distinct from current mutation authority;
- operation-scoped idempotency does not replace fencing or authorization;
- Attempt epoch alone cannot safely survive a potentially regressive control-state restore;
- regressive recovery establishes fresh stale-writer exclusion before ordinary writes resume;
- surviving immutable effects may be adopted by current authority without reviving the old producer;
- checkpoint durability is distinct from current resume compatibility;
- accepted cancellation blocks ordinary new admission and cannot be undone merely by restoring older control state;
- admission is operational eligibility rather than semantic readiness, queue position or write authority;
- temporary resource shortage remains distinguishable from true incompatibility;
- at-least-once physical work remains acceptable while canonical semantic promotion remains singular and owner-controlled.

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

**007-I — Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation** is next eligible as a **design** subgroup.

An explicit proceed decision is required before it begins. Production implementation remains frozen independently of design progression.
