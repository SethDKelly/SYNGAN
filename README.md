# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project deliberately completes conceptual, experience, architecture and implementation-planning work before production coding is authorized. Daniel Jackson's concept-design methodology governs discovery/specification, and canonical knowledge is maintained as an OKF-oriented bundle.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Primary authority:

- [`Phase 003 Consolidated Experience Contract`](docs/experience/phase-003-consolidated-experience-contract.md)
- [`Phase 004 Consolidated Architecture Contract`](docs/architecture/phase-004-consolidated-architecture-contract.md)
- [`Phase 005 Consolidated Implementation-Planning Contract`](docs/implementation/phase-005-consolidated-implementation-planning-contract.md)
- [`Phase 006`](docs/phases/006/index.md) for current post-planning design refinement

Repository-wide automated-agent rules are in [`AGENTS.md`](AGENTS.md).

## Status

- **Phase 001 — Design Foundation & Concept Discovery: complete**
- **Phase 002 — Concept Specification & Invariant Refinement: complete**
- **Phase 003 — Experience & Workflow Design: complete**
- **Phase 004 — Representation & Architecture Design: complete**
- **Phase 005 — Implementation Planning & Delivery Decomposition: complete as planning only**
- **Phase 006 — Post-Planning Design Validation & Adversarial Refinement: current**

### Phase 005 exit

005-A through 005-J produced a coherent future implementation plan covering governance/verification, source topology, control persistence, distributed data, runtime extensions, Execution/recovery, Evidence/history, enterprise security and deployment/platform scale.

005-K audited the plans as one system and **did not authorize implementation**.

The audit concluded:

```text
FURTHER CONCEPT / SYNCHRONIZATION / EXPERIENCE /
ARCHITECTURE / PLANNING REFINEMENT REQUIRED
```

See [`005-K`](docs/phases/005/005-K-cross-slice-integration-delivery-sequencing-backlog-closure-jackson-methodology-completeness-implementation-readiness-exit.md).

The preserved planning baseline is [`docs/implementation/phase-005-consolidated-implementation-planning-contract.md`](docs/implementation/phase-005-consolidated-implementation-planning-contract.md).

## Why Phase 006 is required

Phase 005 exposed four design-readiness blockers:

1. **Temporal authority after regressive restore.** Restoring older control state while newer external workers survive can make stale write authority appear current unless the design includes a non-regressing recovery boundary.
2. **Post-planning adversarial validation.** The concrete A-J seams must be revalidated end-to-end under retry, cancellation, revocation, degraded dependencies/platforms, mixed versions, retention loss and disaster recovery.
3. **Representative method probes.** The model-neutral design must be stress-tested against materially different synthesis/evaluation shapes before infrastructure code hardens hidden algorithm assumptions.
4. **Initial-scope/future-extensibility closure.** Deferred relational/multi-table, formal-privacy, external release-governance and broader method-catalog scope must remain deliberate rather than accidental implementation constraints.

Tracked details are in [`docs/backlog/index.md`](docs/backlog/index.md).

## Phase 006

[`Phase 006 — Post-Planning Design Validation & Adversarial Refinement`](docs/phases/006/index.md) is **design-only**.

It does not authorize production package scaffolding, source code, schema/migrations, adapters, tests, CI, deployment infrastructure or benchmarks.

Planned groups are:

- 006-A — Post-Planning Concept Completeness, Mechanism-vs-Concept & Scope-Boundary Revalidation
- 006-B — Temporal Authority, Disaster Recovery, Rollback, Fork & Historical-Truth Refinement
- 006-C — End-to-End Scenario, Exception, Failure & Adversarial Synchronization Validation
- 006-D — Reference Strategy/Method Design Probes & Algorithm-Neutrality Stress Test
- 006-E — Enterprise Scale, Resource/Approximation, Backpressure & Degraded-Mode Design Validation
- 006-F — Privacy, Disclosure, Release-Governance Boundary & Mechanism-Specific Scope Decision
- 006-G — Relational/Multi-Table Extensibility & Future-Concept Compatibility Audit
- 006-H — Human/Programmatic Experience Closure for Recovery, Security, Degraded & Historical Workflows
- 006-I — Architecture/ADR Reconciliation, Canonical Authority Promotion & Planning Back-Propagation
- 006-J — Consolidation, Residual Design-Debt Audit & Implementation-Authority Readiness Decision

Jackson-style completeness is judged by design evidence, not by a fixed number of phases. A positive 006-J result would still require a **later explicit implementation-authority phase** before production coding begins.

## Current next group

**006-A — Post-Planning Concept Completeness, Mechanism-vs-Concept & Scope-Boundary Revalidation**

No production implementation has begun.