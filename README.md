# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project deliberately completes conceptual, experience, architecture and implementation-planning work before production coding is authorized. Daniel Jackson's concept-design methodology governs discovery/specification, and canonical knowledge is maintained as an OKF-oriented bundle.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Primary authority:

- [`Phase 003 Consolidated Experience Contract`](docs/experience/phase-003-consolidated-experience-contract.md)
- [`Phase 004 Consolidated Architecture Contract`](docs/architecture/phase-004-consolidated-architecture-contract.md)
- [`Phase 005 Consolidated Implementation-Planning Contract`](docs/implementation/phase-005-consolidated-implementation-planning-contract.md)
- [`Operational Authority Continuity & Regressive Recovery Contract`](docs/authority/operational-authority-continuity-regressive-recovery-contract.md)
- [`Phase 006`](docs/phases/006/index.md) for current post-planning design refinement

Repository-wide automated-agent rules are in [`AGENTS.md`](AGENTS.md).

## Status

- **Phase 001 — Design Foundation & Concept Discovery: complete**
- **Phase 002 — Concept Specification & Invariant Refinement: complete**
- **Phase 003 — Experience & Workflow Design: complete**
- **Phase 004 — Representation & Architecture Design: complete**
- **Phase 005 — Implementation Planning & Delivery Decomposition: complete as planning only**
- **Phase 006 — Post-Planning Design Validation & Adversarial Refinement: current**

No production implementation has begun or been authorized.

## Phase 006 progress

### 006-A — complete

006-A re-tested Phase 005 mechanisms against Jackson concept criteria.

Key results:

- accepted concept/synchronization counts remain **11 / 15**;
- `GenerationMode` / `DataTopologyMode` is not a concept;
- single-table generation remains the current baseline capability;
- time-series generation is an explicit Phase 006 design target;
- multi-table shared-key generation reopens `Relationship` as a provisional candidate for 006-G.

### 006-B — complete

006-B closed the semantic core of the regressive-control-state recovery problem.

The new cross-cutting [`Operational Authority Continuity & Regressive Recovery Contract`](docs/authority/operational-authority-continuity-regressive-recovery-contract.md) establishes that:

```text
restored historical control state
        !=
current mutation authority
```

A potentially regressive recovery therefore enters recovery-quarantine / continuity-unverified semantics until a non-regressing authority boundary is established and surviving work/effects are reconciled.

Rollback cannot by itself resurrect:

- superseded Attempt authority;
- a cancellation generation omitted by the backup;
- stale capability/credential authority;
- semantic result authority merely because physical bytes survive.

Likewise, missing post-backup rows do not prove that later historical events never occurred. Exact history may be reconstructed only from evidence sufficient for the owning concept's normal invariants; otherwise the state remains explicitly unknown/unavailable.

`ControlPlaneIncarnation` remains a downstream architecture realization candidate rather than a new concept.

## Structured-data capability direction

Phase 006 is explicitly validating:

```text
single-table generation
time-series table generation
multi-table shared-key generation
```

A future API may expose these through a parameter or typed specification, but selection syntax cannot own relationship, temporal-order, validity, completion or Evidence semantics.

## Remaining Phase 006 groups

- **006-C — End-to-End Scenario, Exception, Failure & Adversarial Synchronization Validation — next**
- 006-D — Reference Strategy/Method and Topology Design Probes & Algorithm-Neutrality Stress Test
- 006-E — Enterprise Scale, Resource/Approximation, Backpressure & Degraded-Mode Design Validation
- 006-F — Privacy, Disclosure, Release-Governance Boundary & Mechanism-Specific Scope Decision
- 006-G — Structured-Data Topology: Single-Table, Time-Series & Multi-Table Relationship Concept/Extensibility Audit
- 006-H — Human/Programmatic Experience Closure for Recovery, Security, Degraded & Historical Workflows
- 006-I — Architecture/ADR Reconciliation, Canonical Authority Promotion & Planning Back-Propagation
- 006-J — Consolidation, Residual Design-Debt Audit & Implementation-Authority Readiness Decision

Jackson-style completeness is judged by design evidence, not by a fixed number of phases. A positive 006-J result would still require a **later explicit implementation-authority phase** before production coding begins.

## Current next group

**006-C — End-to-End Scenario, Exception, Failure & Adversarial Synchronization Validation**
