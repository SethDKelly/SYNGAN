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

006-A through 006-C retained the current **11 accepted concepts / 15 synchronizations**, established restore-safe operational-authority continuity, and adversarially refined the synchronization set without introducing `SYNC-16`.

006-D established a self-contained source-derived free-form-text baseline and cluster-wide runtime-distribution closure. Driver import success is not Spark executor readiness, optional pretrained/network text remains explicit, and large state/model distribution cannot universally require driver loading/broadcast.

006-E established that enterprise scale is multidimensional, resource pressure cannot silently weaken committed semantics, approximation remains owner-specific, backpressure must preserve mandatory logical scope, and degraded operation is capability-specific.

006-F established that synthetic/offline output is not automatically private, favorable disclosure Evidence is not a formal guarantee, differential privacy is deferred behind future mechanism-specific concept discovery, and release/use governance remains external.

### 006-G — complete

006-G established the [`Structured-Data Topology & Relationship Semantics Contract`](docs/authority/structured-data-topology-relationship-semantics-contract.md).

`Relationship` is **not** a twelfth concept. Material shared-key and sequence/order structural semantics are descriptive state owned by Data Meaning. Constraint remains prescriptive authority; Generation owns requested topology/scope; Strategy owns topology capability.

The first **complete structured-data capability baseline** now includes:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

Implementation may be staged and Strategies may support subsets, but a release must not claim the complete baseline until at least one supported self-contained Strategy path exists for each family.

A future API can offer convenient presets such as `single_table`, `time_series`, or `multi_table`, but those labels are not semantic authority. Composite structures—such as a customer table with a time-series observations child—must remain representable rather than being blocked by a permanently exclusive topology enum.

BDR-004 is resolved. No Phase 006 concept/scope blocker remains open.

## Remaining Phase 006 groups

- **006-H — Human/Programmatic Experience Closure for Recovery, Security, Degraded & Historical Workflows — next**
- 006-I — Architecture/ADR Reconciliation, Canonical Authority Promotion & Planning Back-Propagation
- 006-J — Consolidation, Residual Design-Debt Audit & Implementation-Authority Readiness Decision

Jackson-style completeness is judged by design evidence, not by a fixed number of phases. A positive 006-J result would still require a **later explicit implementation-authority phase** before production coding begins.

## Current next group

**006-H — Human/Programmatic Experience Closure for Recovery, Security, Degraded & Historical Workflows**
