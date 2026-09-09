# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project deliberately completes conceptual, experience, architecture and implementation-planning work before production coding is authorized. Daniel Jackson's concept-design methodology governs discovery/specification, and canonical knowledge is maintained as an OKF-oriented bundle.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Primary authority:

- [`Accepted Concepts`](docs/concepts/index.md)
- [`Phase 003 Consolidated Experience Contract`](docs/experience/phase-003-consolidated-experience-contract.md)
- [`Phase 004 Consolidated Architecture Contract`](docs/architecture/phase-004-consolidated-architecture-contract.md)
- [`Phase 005 Consolidated Implementation-Planning Contract`](docs/implementation/phase-005-consolidated-implementation-planning-contract.md)
- [`Phase 006`](docs/phases/006/index.md) for current post-planning design refinement

## Status

- **Phase 001 — Design Foundation & Concept Discovery: complete**
- **Phase 002 — Concept Specification & Invariant Refinement: complete**
- **Phase 003 — Experience & Workflow Design: complete**
- **Phase 004 — Representation & Architecture Design: complete**
- **Phase 005 — Implementation Planning & Delivery Decomposition: complete as planning only**
- **Phase 006 — Post-Planning Design Validation & Adversarial Refinement: current**

No production implementation has begun.

## Phase 006 capability revalidation

006-A is complete and keeps the accepted catalog at **eleven concepts / fifteen synchronizations**.

The current structured-data capability direction being tested is:

```text
single-table generation
time-series table generation
multi-table generation with shared-key relationships
```

Current disposition:

- **single-table** — existing baseline capability;
- **time-series** — explicit Phase 006 design target; initial implementation inclusion still to be decided;
- **multi-table shared-key** — explicit Phase 006 design target; initial implementation inclusion still to be decided.

A future API may make these ergonomic through a function parameter or typed structure specification. That selection is an API/experience mechanism only; it cannot replace the semantics required to describe series identity/order, shared-key linkage, cardinality, Constraints, Generation scope, Evaluation or history.

Multi-table shared-key synthesis has reopened the previously deferred **Relationship** candidate for Phase 006-G. It is **not yet an accepted concept**. Time-series is being used as a falsification case for whether one generic Relationship boundary can also represent sequence membership/order without overloading Data Meaning or Constraint.

See:

- [`006-A`](docs/phases/006/006-A-post-planning-concept-completeness-mechanism-vs-concept-scope-boundary-revalidation.md)
- [`Post-Planning Concept Revalidation & Structured-Data Topology Candidates`](docs/discovery/post-planning-concept-revalidation-structured-topology-candidates.md)

## Why Phase 006 is required

Phase 005 exposed four design-readiness blockers:

1. temporal operational authority after regressive restore;
2. post-planning adversarial validation;
3. representative Strategy/method and topology design probes;
4. initial-scope/future-extensibility closure.

[`Phase 006`](docs/phases/006/index.md) remains **design-only**. It does not authorize production package scaffolding, source code, schemas/migrations, adapters, tests, CI, deployment infrastructure or benchmarks.

## Current next group

**006-B — Temporal Authority, Disaster Recovery, Rollback, Fork & Historical-Truth Refinement**

Here `temporal` refers to operational authority across rollback/restore, not time-series data semantics.

Jackson-style completeness is judged by design evidence, not a fixed phase count. Even a positive Phase 006 exit would require a later explicit implementation-authority phase before production coding begins.