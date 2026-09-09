# SYNGAN

SYNGAN is a design-first synthetic-data generation framework intended for Spark-scale workloads.

Daniel Jackson concept design and the repository's canonical design/planning work were completed through Phase 006 before production implementation authority was granted.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current implementation authority:

- [`Phase 007 Implementation Authority Lock`](docs/implementation/phase-007-implementation-authority-lock.md)
- [`Phase 007 index`](docs/phases/007/index.md)
- [`Phase 006 Consolidated Design Readiness Contract`](docs/authority/phase-006-consolidated-design-readiness-contract.md)
- [`Phase 006 Architecture Reconciliation Contract`](docs/architecture/phase-006-architecture-reconciliation-contract.md)
- [`Phase 006 Implementation-Planning Reconciliation`](docs/implementation/phase-006-implementation-planning-reconciliation.md)

Repository-wide automated-agent rules are in [`AGENTS.md`](AGENTS.md).

## Status

- Phase 001 — complete
- Phase 002 — complete
- Phase 003 — complete historical experience baseline
- Phase 004 — complete historical architecture baseline
- Phase 005 — complete implementation-planning baseline
- Phase 006 — complete post-planning design/readiness validation
- **Phase 007 — active, incrementally authorized**

### 007-A — complete

007-A locked the canonical implementation baseline, change-control rules, evidence gates and bounded slice authorization.

Current permission:

```text
007-A  COMPLETE
007-B  AUTHORIZED / NEXT
007-C..007-K  NOT AUTHORIZED
```

The active production implementation authority currently covers only **007-B — Repository/Toolchain Bootstrap, Reproducible Environment & Verification Harness**.

007-B may add project metadata, dependency lock state, build/test/static-analysis tooling, verification scripts/bootstrap tests and verification-only CI. It may **not** yet create `src/syngan/` or substantive domain/runtime/platform behavior.

## 007-A entry baseline

```text
repository: SethDKelly/SYNGAN
branch:     main
commit:     843a518c12f7482229cfb012da658887cb92dfaa
```

At entry, `main` was unprotected and had no required status checks. Direct-to-main is permitted for explicitly authorized 007-B work, but it is not independent review/CI evidence. 007-B must establish repository-owned verification entry points.

## Locked design baseline

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
```

Complete structured-data target:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

The complete supported baseline also requires source-derived/local free-form-text synthesis without mandatory public model-hub or runtime inference-service dependency.

## Current implementation rules

```text
restored stale control state
    != current mutation authority

driver import success
    != cluster worker readiness

resource pressure
    != permission to weaken semantics

topology preset
    != durable semantic topology

privacy Evidence
    != formal privacy guarantee
    != release approval
```

Implementation is evidence-gated and incremental. A Class 3 architecture conflict or Class 4 semantic/experience conflict stops ordinary implementation and reopens upstream authority.

## Current next

**007-B — Repository/Toolchain Bootstrap, Reproducible Environment & Verification Harness**
