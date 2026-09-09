# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project deliberately completes conceptual, experience, architecture and implementation-planning work before production coding is authorized. Daniel Jackson's concept-design methodology governs discovery/specification, and canonical knowledge is maintained as an OKF-oriented bundle.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Primary authority:

- [`Phase 003 Consolidated Experience Contract`](docs/experience/phase-003-consolidated-experience-contract.md)
- [`Phase 006 Recovery, Security, Degraded, Historical & Topology Experience Contract`](docs/experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md)
- [`Phase 004 Consolidated Architecture Contract`](docs/architecture/phase-004-consolidated-architecture-contract.md)
- [`Phase 005 Consolidated Implementation-Planning Contract`](docs/implementation/phase-005-consolidated-implementation-planning-contract.md)
- [`Operational Authority Continuity & Regressive Recovery Contract`](docs/authority/operational-authority-continuity-regressive-recovery-contract.md)
- [`Self-Contained Execution & Runtime Distribution Closure Contract`](docs/authority/self-contained-execution-runtime-distribution-closure-contract.md)
- [`Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract`](docs/authority/enterprise-scale-resource-admission-approximation-degraded-operation-contract.md)
- [`Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract`](docs/authority/privacy-disclosure-formal-guarantee-release-boundary-contract.md)
- [`Structured-Data Topology & Relationship Semantics Contract`](docs/authority/structured-data-topology-relationship-semantics-contract.md)
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

006-A through 006-G retained the current **11 accepted concepts / 15 synchronizations** while closing recovery authority, runtime-distribution, enterprise-scale/degraded-operation, privacy/release, and structured-topology design questions.

The first complete structured-data capability baseline includes:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

`Relationship` is not a twelfth concept; material shared-key and sequence/order structure is Data Meaning-owned descriptive state. Constraint remains prescriptive, Generation owns requested topology/scope, and Strategy owns topology capability.

The supported baseline also requires at least one self-contained source-derived free-form-text path; optional pretrained/network text remains explicit. Driver import success is not Spark executor readiness, and resource pressure cannot silently weaken committed semantics.

Synthetic/offline output is not automatically private, favorable disclosure Evidence is not a formal guarantee, differential privacy is deferred behind future mechanism-specific concept discovery, and release/use governance remains external.

### 006-H — complete

006-H established the [`Phase 006 Recovery, Security, Degraded, Historical & Topology Experience Contract`](docs/experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md).

The Phase 003 four-barrier experience model remains valid, but current surfaces must preserve orthogonal distinctions such as:

```text
semantic state
operational state
current actionability
authority continuity
compatibility / limitations
disclosure state
historical-knowledge quality
```

This keeps `queued` distinct from blocked/incompatible/denied/failure, exposes regressive-recovery authority uncertainty without leaking implementation jargon, distinguishes reconstructed/partial/unknown history, preserves non-disclosing security behavior where existence is protected, and keeps privacy Evidence/formal guarantee/export authorization/release approval separate.

Topology presets remain ergonomic only; users/programs must still be able to inspect the actual logical scope and whole-result completion state.

BDR-001's experience closure is complete. Only architecture/planning propagation remains.

## Remaining Phase 006 groups

- **006-I — Architecture/ADR Reconciliation, Canonical Authority Promotion & Planning Back-Propagation — next**
- 006-J — Consolidation, Residual Design-Debt Audit & Implementation-Authority Readiness Decision

Jackson-style completeness is judged by design evidence, not by a fixed number of phases. A positive 006-J result would still require a **later explicit implementation-authority phase** before production coding begins.

## Current next group

**006-I — Architecture/ADR Reconciliation, Canonical Authority Promotion & Planning Back-Propagation**
