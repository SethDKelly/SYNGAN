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
- [`Core Synchronizations`](docs/synchronizations/core-synchronizations.md)
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

- accepted concept/synchronization counts remained **11 / 15**;
- `GenerationMode` / `DataTopologyMode` is not a concept;
- single-table generation remains the current baseline capability;
- time-series generation is an explicit Phase 006 design target;
- multi-table shared-key generation reopens `Relationship` as a provisional candidate for 006-G.

### 006-B — complete

006-B established the cross-cutting [`Operational Authority Continuity & Regressive Recovery Contract`](docs/authority/operational-authority-continuity-regressive-recovery-contract.md).

Its core rule is:

```text
restored historical control state
        !=
current mutation authority
```

Potentially regressive recovery therefore enters continuity-unverified/recovery-quarantine semantics until a non-regressing authority boundary is established and surviving work/effects are reconciled.

### 006-C — complete

006-C replayed the design against twenty-four normal/adversarial scenarios including ambiguous launch, stale writers, cancellation races, current-policy/dependency change, mixed versions, regressive restore, repeated Evaluation work, partial multi-table output and interrupted time-series continuation.

Result:

```text
PASS WITH TARGETED SYNCHRONIZATION REFINEMENT
```

The synchronization count remains **15**; no `SYNC-16` is currently justified.

Canonical refinements were made to:

- SYNC-04 / 07 / 11 — current continuation qualification and restore-safe authority continuity;
- SYNC-08 — coordinated logical-output completion applies to the whole committed scope;
- SYNC-14 — rollback/history reconstruction truthfulness;
- SYNC-15 — continuity gaps constrain reproducibility claims.

BDR-002 is resolved for the current eleven-concept/fifteen-synchronization baseline. If a later Phase 006 group accepts `Relationship` or materially changes coordination, affected scenarios must be replayed before the final readiness exit.

## Structured-data capability direction

Phase 006 is explicitly validating:

```text
single-table generation
time-series table generation
multi-table shared-key generation
```

A future API may expose these through a parameter or typed specification, but selection syntax cannot own relationship, temporal-order, validity, completion or Evidence semantics.

## Remaining Phase 006 groups

- **006-D — Reference Strategy/Method and Topology Design Probes & Algorithm-Neutrality Stress Test — next**
- 006-E — Enterprise Scale, Resource/Approximation, Backpressure & Degraded-Mode Design Validation
- 006-F — Privacy, Disclosure, Release-Governance Boundary & Mechanism-Specific Scope Decision
- 006-G — Structured-Data Topology: Single-Table, Time-Series & Multi-Table Relationship Concept/Extensibility Audit
- 006-H — Human/Programmatic Experience Closure for Recovery, Security, Degraded & Historical Workflows
- 006-I — Architecture/ADR Reconciliation, Canonical Authority Promotion & Planning Back-Propagation
- 006-J — Consolidation, Residual Design-Debt Audit & Implementation-Authority Readiness Decision

Jackson-style completeness is judged by design evidence, not by a fixed number of phases. A positive 006-J result would still require a **later explicit implementation-authority phase** before production coding begins.

## Current next group

**006-D — Reference Strategy/Method and Topology Design Probes & Algorithm-Neutrality Stress Test**
