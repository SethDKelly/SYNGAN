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
- [`007-I Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation`](docs/architecture/phase-007-i-evaluation-evidence-provenance-historical-query-reproducibility-disclosure-foundation.md)
- [`007-J Reference Vertical-Slice Scope Re-evaluation, Architecture Completeness & Implementation-Proof Boundary`](docs/architecture/phase-007-j-reference-vertical-slice-scope-re-evaluation-architecture-completeness-implementation-proof-boundary.md)
- [`Phase 007 index`](docs/phases/007/index.md)

## Status

- Phases 001–006 — retained design/planning/readiness history
- 007-A through 007-C — retained historical/provisional bootstrap work
- **007-D through 007-J — complete as architecture/design work**
- **007-K — next eligible consolidation / implementation-reentry readiness subgroup**
- **Production implementation expansion — frozen**

Phase 006 historically concluded that design was complete enough to consider implementation. The project later reopened architecture design so existing source/tests would not prematurely harden unsettled representation choices.

## Current architecture result

007-D through 007-I establish technology-neutral architecture for exact identity/commitment/history, persistence and distributed data state, composable topology, runtime/dependency/security closure, Execution/recovery/admission, and Evaluation/Evidence/Provenance/history/reproducibility/disclosure.

007-J establishes the implementation-proof boundary. It distinguishes:

```text
architecture-conformance proof
capability proof
runtime/platform-profile proof
resilience/adversarial proof
scale/release qualification
```

A self-contained learning-based single-table/Spark-local path is the recommended first bounded reference proof after later implementation re-entry because it can exercise a broad end-to-end architecture path without introducing unnecessary topology complexity.

That proof is deliberately limited. It cannot by itself establish:

- direct-generation neutrality;
- self-contained free-form-text capability;
- time-series support;
- multi-table shared-key support;
- composite-topology representability;
- distributed cluster/runtime closure;
- regressive-recovery safety;
- managed-platform support;
- enterprise scale;
- privacy guarantees or release approval.

Those claims require separate conformance evidence.

## Provisional executable scaffold

The repository still contains the 007-B/007-C package/tool/test scaffold. It is feasibility/history evidence, **not upstream design authority**.

Before production work resumes, 007-K/re-entry must explicitly decide which package boundaries, Import Linter contracts, tool choices and existing fitness checks remain compatible with architecture through 007-J.

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

**007-K — Phase 007 Consolidation, Architecture-Fitness Audit, Evidence Review & Implementation-Reentry Readiness Decision** is next eligible as a **design/governance** subgroup.

Production implementation remains frozen until 007-K explicitly decides whether re-entry is justified and which bounded tranche, if any, may begin.