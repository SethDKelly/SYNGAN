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
- [`Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract`](docs/authority/privacy-disclosure-formal-guarantee-release-boundary-contract.md)
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

006-A through 006-C retained the current **11 accepted concepts / 15 synchronizations**, reopened `Relationship` provisionally, established restore-safe operational-authority continuity, and adversarially refined the current synchronization set without introducing `SYNC-16`.

006-D established a self-contained source-derived free-form-text baseline and cluster-wide runtime-distribution closure. Driver import success is not Spark executor readiness, optional pretrained/network text remains explicit, and large state/model distribution cannot universally require driver loading/broadcast.

006-E established that enterprise scale is multidimensional, resource pressure cannot silently weaken committed semantics, approximation remains owner-specific, backpressure must preserve mandatory logical scope, and degraded operation is capability-specific.

### 006-F — complete

006-F established the [`Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract`](docs/authority/privacy-disclosure-formal-guarantee-release-boundary-contract.md).

Key rules:

```text
synthetic data
    != automatically private/anonymized

favorable disclosure-risk Evidence
    != formal privacy guarantee

Generation completed
    != release approved

offline/self-contained
    != privacy guarantee
```

Disclosure/memorization remain threat-model-specific Criterion/Evaluation/Evidence concerns rather than new standalone concepts.

Differential privacy is **not part of the initial implementation baseline**. If SYNGAN later adds a composable formal DP mechanism, Jackson-style concept discovery must reopen before implementation so privacy-unit/budget/allocation/consumption/composition state is not hidden inside generic Strategy metadata, Evidence or quota configuration.

Use/Release Decision remains external to current SYNGAN concept authority. SYNGAN may supply exact Evidence/Provenance and enforce current access decisions through security adapters, but it does not become the enterprise release-approval authority.

## Structured-data capability direction

Phase 006 is explicitly validating:

```text
single-table generation
time-series table generation
multi-table shared-key generation
```

A future API may expose these through a parameter or typed specification, but selection syntax cannot own relationship, temporal-order, validity, completion, privacy or Evidence semantics.

## Remaining Phase 006 groups

- **006-G — Structured-Data Topology: Single-Table, Time-Series & Multi-Table Relationship Concept/Extensibility Audit — next**
- 006-H — Human/Programmatic Experience Closure for Recovery, Security, Degraded & Historical Workflows
- 006-I — Architecture/ADR Reconciliation, Canonical Authority Promotion & Planning Back-Propagation
- 006-J — Consolidation, Residual Design-Debt Audit & Implementation-Authority Readiness Decision

Jackson-style completeness is judged by design evidence, not by a fixed number of phases. A positive 006-J result would still require a **later explicit implementation-authority phase** before production coding begins.

## Current next group

**006-G — Structured-Data Topology: Single-Table, Time-Series & Multi-Table Relationship Concept/Extensibility Audit**
