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
- [`Self-Contained Execution & Runtime Distribution Closure Contract`](docs/authority/self-contained-execution-runtime-distribution-closure-contract.md)
- [`Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract`](docs/authority/enterprise-scale-resource-admission-approximation-degraded-operation-contract.md)
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

### 006-A through 006-D — complete

These groups retained the current **11-concept / 15-synchronization** model, reopened `Relationship` only as a provisional candidate, established restore-safe Operational Authority Continuity, adversarially refined SYNC-04/07/08/11/14/15, and validated Learning-based/direct/text/time-series/multi-table/Evaluation/runtime-distribution shapes.

006-D additionally requires:

- at least one self-contained source-derived free-form-text synthesis path in the supported baseline;
- optional pretrained/world-knowledge text to remain explicit local-artifact/runtime-network capability;
- exact compatible runtime closure across every material Spark worker, including dynamically allocated workers;
- no hidden first-use dependency/model acquisition;
- no universal driver-memory load/broadcast requirement for large Learned State/model artifacts.

### 006-E — complete

006-E stress-tested the design under multidimensional enterprise scale, large state/text artifacts, dynamic workers, time-series horizon/entity growth, multi-table fan-out, statistical approximation, concurrent workloads, backpressure and capability-specific failures.

Result:

```text
PASS WITH TARGETED CROSS-CUTTING REFINEMENT
```

It established the [`Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract`](docs/authority/enterprise-scale-resource-admission-approximation-degraded-operation-contract.md).

Core rules now include:

```text
resource pressure
    may queue / block / retry / reduce observability

resource pressure
    MUST NOT silently weaken committed semantics
```

Accordingly:

- enterprise compatibility is workload-specific across rows, bytes, width, cardinality, skew, state size, topology, Evaluation coverage and concurrency—not a row-count flag;
- hidden source-size-proportional driver/single-process stages invalidate enterprise-scale claims for that path;
- approximation must be explicit and owned by Learning, Generation or Evaluation as appropriate;
- exhaustive Evaluation cannot quietly become sampled because resources are scarce;
- backpressure cannot silently truncate Generation quantity, time-series horizon or mandatory multi-table scope;
- caches remain performance mechanisms, not dependency identity;
- dynamically admitted workers must retain runtime-distribution closure;
- degraded operation must state which capability is unavailable—canonical persistence, projection/search, telemetry, dependency source, exact data reference, output/checkpoint storage, worker/accelerator or authorization have different consequences;
- storage pressure does not override authority-aware retention.

No Resource, Backpressure, Approximation, DegradedMode, Cost or Quota concept was added, and no new synchronization ID was required.

## Structured-data capability direction

Phase 006 continues to validate:

```text
single-table generation
time-series table generation
multi-table shared-key generation
```

A future API may expose these through a parameter or typed specification, but selection syntax cannot own relationship, temporal-order, validity, completion or Evidence semantics.

## Remaining Phase 006 groups

- **006-F — Privacy, Disclosure, Release-Governance Boundary & Mechanism-Specific Scope Decision — next**
- 006-G — Structured-Data Topology: Single-Table, Time-Series & Multi-Table Relationship Concept/Extensibility Audit
- 006-H — Human/Programmatic Experience Closure for Recovery, Security, Degraded & Historical Workflows
- 006-I — Architecture/ADR Reconciliation, Canonical Authority Promotion & Planning Back-Propagation
- 006-J — Consolidation, Residual Design-Debt Audit & Implementation-Authority Readiness Decision

Jackson-style completeness is judged by design evidence, not by a fixed number of phases. A positive 006-J result would still require a **later explicit implementation-authority phase** before production coding begins.

## Current next group

**006-F — Privacy, Disclosure, Release-Governance Boundary & Mechanism-Specific Scope Decision**
