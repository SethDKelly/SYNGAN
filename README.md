# SYNGAN

SYNGAN is a design-first synthetic-data generation framework intended for Spark-scale workloads.

SYNGAN follows Daniel Jackson-style concept design: problem/concept/experience authority precedes representation and implementation choices.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current authority:

- [`Phase 007 Consolidated Architecture Contract`](docs/architecture/phase-007-consolidated-architecture-contract.md)
- [`Phase 007 Consolidated Architecture & Implementation-Reentry Readiness Contract`](docs/authority/phase-007-consolidated-architecture-implementation-reentry-readiness-contract.md)
- [`007-K Phase Record`](docs/phases/007/007-K-phase-007-consolidation-architecture-fitness-audit-evidence-review-implementation-reentry-readiness-decision.md)
- [`Phase 007 index`](docs/phases/007/index.md)

## Status

- Phases 001–006 — retained design/planning/readiness history
- 007-A through 007-C — retained historical/provisional bootstrap work
- **007-D through 007-J — complete architecture/design authorities**
- **007-K — complete; Phase 007 consolidated**
- **Controlled implementation re-entry — approved for R0/008-A only after explicit proceed**
- **Domain/runtime feature implementation — not yet authorized**

The Phase 007 design freeze is closed. It is not replaced by blanket coding authority: implementation re-entry starts by reconciling the retained scaffold and executable verification against the now-consolidated architecture.

## Current architecture result

The consolidated architecture preserves technology-neutral boundaries for:

- exact identity, revision, references and views;
- owner-controlled persistence, concurrency, durable coordination and history;
- distributed logical data state, composable topology, manifests and Generation promotion;
- Strategy/method semantics separate from executable/dependency/runtime realization;
- trust, authorization, secrets, network/egress and distributed worker closure;
- stable Execution, distinguishable Attempts, idempotency, fencing, non-regressing recovery, checkpoints, cancellation and admission;
- Evaluation/Evidence, typed Provenance, historical query, qualified reproducibility and actor-safe disclosure.

## Implementation-proof boundary

Implementation evidence must distinguish:

```text
architecture-conformance proof
capability proof
runtime/platform-profile proof
resilience/adversarial proof
scale/release qualification
```

A self-contained learning-based single-table local/Spark-local path remains a suitable first eventual user-visible proof because it exercises a broad architecture path with bounded topology complexity.

It cannot by itself establish direct-generation neutrality, self-contained text support, time-series, multi-table shared-key, distributed cluster/runtime closure, regressive-recovery safety, managed-platform guarantees, enterprise scale, privacy guarantees or release approval.

## Provisional executable scaffold

The repository still contains the 007-B/007-C package/tool/test scaffold as feasibility/history evidence.

007-K confirmed that `tests/fitness/test_phase_007_authority_boundary.py` is stale relative to the completed design progression, and the exact seven-package topology plus Import Linter contracts remain provisional until explicitly revalidated.

The next tranche exists specifically to reconcile these executable assumptions before feature code is added.

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

The complete supported baseline also requires source-derived/local free-form-text synthesis without mandatory pretrained model, public model hub, first-use model download or runtime inference service.

## Current next boundary

**008-A — Implementation Re-entry Authority, Scaffold Reconciliation & Verification Re-baseline** is next after an explicit proceed decision.

008-A may reconcile historical implementation authority, package boundaries, Import Linter contracts, stale fitness tests, tool/lock/verification metadata and repository evidence gates. It does not authorize owner-specific domain, persistence, Spark/runtime, Strategy, Execution/recovery, Evidence/history, security/provider or benchmark implementation.
