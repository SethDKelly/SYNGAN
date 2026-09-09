# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project deliberately completes conceptual, experience, architecture and implementation-planning work before production coding is authorized. Daniel Jackson's concept-design methodology governs discovery/specification, and canonical knowledge is maintained as an OKF-oriented bundle.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current implementation-facing authority now includes:

- [`Phase 006 Architecture Reconciliation Contract`](docs/architecture/phase-006-architecture-reconciliation-contract.md)
- [`Phase 006 Implementation-Planning Reconciliation`](docs/implementation/phase-006-implementation-planning-reconciliation.md)
- [`Phase 006 Recovery, Security, Degraded, Historical & Topology Experience Contract`](docs/experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md)
- [`Operational Authority Continuity & Regressive Recovery Contract`](docs/authority/operational-authority-continuity-regressive-recovery-contract.md)
- [`Self-Contained Execution & Runtime Distribution Closure Contract`](docs/authority/self-contained-execution-runtime-distribution-closure-contract.md)
- [`Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract`](docs/authority/enterprise-scale-resource-admission-approximation-degraded-operation-contract.md)
- [`Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract`](docs/authority/privacy-disclosure-formal-guarantee-release-boundary-contract.md)
- [`Structured-Data Topology & Relationship Semantics Contract`](docs/authority/structured-data-topology-relationship-semantics-contract.md)
- [`Core Synchronizations`](docs/synchronizations/core-synchronizations.md)

Historical baselines remain under the Phase 003 experience, Phase 004 architecture and Phase 005 implementation-planning contracts where not refined by Phase 006.

Repository-wide automated-agent rules are in [`AGENTS.md`](AGENTS.md).

## Status

- **Phase 001 — Design Foundation & Concept Discovery: complete**
- **Phase 002 — Concept Specification & Invariant Refinement: complete**
- **Phase 003 — Experience & Workflow Design: complete historical baseline**
- **Phase 004 — Representation & Architecture Design: complete historical baseline**
- **Phase 005 — Implementation Planning & Delivery Decomposition: complete as planning only**
- **Phase 006 — Post-Planning Design Validation & Adversarial Refinement: current**

No production implementation has begun or been authorized.

## Phase 006 progress

006-A through 006-H retained the **11 accepted concepts / 15 synchronizations** while closing recovery, runtime-distribution, scale/degraded-operation, privacy/release, structured-topology and actor/programmatic experience design questions.

### 006-I — complete

006-I reconciled those decisions into current architecture and implementation planning.

Current architecture precedence is:

```text
Phase 006 upstream authority / experience
        ↓
Phase 006 Architecture Reconciliation
        ↓
Phase 004 architecture baseline
        ↓
Phase 006 Implementation-Planning Reconciliation
        ↓
Phase 005 planning details
```

Two additive ADRs were accepted:

- **ADR-0009 — Non-Regressing Authority After Regressive Control-State Recovery**
- **ADR-0010 — Self-Contained Distributed Runtime Closure**

ADR-0001 through ADR-0008 remain active and are not superseded.

Key reconciled rules include:

```text
restored stale control state
    != current mutation authority

driver/runtime import succeeds
    != cluster worker readiness

resource pressure
    != permission to reduce semantics

topology preset
    != durable topology meaning

privacy Evidence
    != formal privacy guarantee
    != release approval
```

The first complete structured-data capability baseline remains:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

with at least one supported self-contained Strategy path required for each family before claiming complete baseline support. The baseline also requires a source-derived/local free-form-text-capable path with no required pretrained model hub or runtime inference service.

The previously identified BDR-001 through BDR-004 blockers now have accepted closure through 006-I. This does **not** itself authorize implementation.

## Remaining Phase 006 group

- **006-J — Phase 006 Consolidation, Residual Design-Debt Audit & Implementation-Authority Readiness Decision — next**

006-J must replay materially affected scenarios/probes against the reconciled architecture/planning baseline and decide whether design is complete enough to create a later explicit implementation-authority phase or whether further design refinement is required.

Even a positive 006-J result will not itself authorize coding.
