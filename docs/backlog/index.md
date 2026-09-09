---
type: Backlog
title: SYNGAN Design & Delivery Backlog
status: active
---

# SYNGAN Design & Delivery Backlog

## Purpose

Track unresolved or deliberately deferred work without allowing backlog notes to become canonical design authority.

Canonical facts remain under `docs/authority/`, `docs/concepts/`, `docs/synchronizations/`, `docs/experience/`, `docs/architecture/`, and `docs/implementation/`.

## Blocking design refinement

### BDR-001 — regressive restore and temporal authority closure

**Status: resolved through 006-I.**

Closure chain:

- semantic authority — 006-B, [Operational Authority Continuity & Regressive Recovery Contract](../authority/operational-authority-continuity-regressive-recovery-contract.md);
- synchronization validation — 006-C;
- actor/programmatic experience — 006-H, [Phase 006 Recovery, Security, Degraded, Historical & Topology Experience Contract](../experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md);
- architecture/ADR/planning propagation — 006-I, [Phase 006 Architecture Reconciliation Contract](../architecture/phase-006-architecture-reconciliation-contract.md) + [Phase 006 Implementation-Planning Reconciliation](../implementation/phase-006-implementation-planning-reconciliation.md) + ADR-0009.

Potentially regressive restore cannot resurrect stale writer/cancellation/security authority. A fresh non-regressing recovery-authority frontier is required before ordinary mutation resumes.

### BDR-002 — post-planning adversarial end-to-end validation

**Status: resolved by 006-C for the accepted eleven-concept / fifteen-synchronization model.**

006-G conceptually replayed topology-sensitive scenarios after resolving Relationship as Data Meaning-owned structural semantics. 006-J must replay materially affected scenarios against the reconciled 006-I architecture/planning baseline as an exit check, not because the underlying blocker remains open.

### BDR-003 — representative Strategy/method and topology design probes

**Status: resolved by 006-D.**

The current model survived Learning-based, direct, text, composite, time-series, multi-table, deterministic/statistical Evaluation, large-state and Spark-distribution probes. 006-I propagated the resulting runtime-distribution and topology obligations into architecture/planning.

### BDR-004 — initial-baseline scope and future-extensibility closure

**Status: resolved by 006-G.**

The first complete structured-data capability baseline includes:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

Implementation may be staged and individual Strategies may support subsets, but the complete baseline claim requires at least one supported self-contained Strategy path for each family.

`Relationship` is not a standalone concept. Shared-key/sequence structural semantics remain Data Meaning-owned descriptive state; Constraint owns prescriptive validity; Generation owns requested topology/scope; Strategy owns capability.

### Phase 006 blocking status

**No identified Phase 006 design blocker remains open after 006-I.**

This does not itself approve implementation. 006-J must perform the final residual design-debt/readiness audit and may still discover a new blocker.

## Baseline scope decisions

### BSD-001 — relational/multi-table shared-key synthesis

**Status:** included in the complete baseline capability target by 006-G.

The baseline covers explicit shared-key relationships and common relational shapes such as one-to-one, one-to-many/many-to-one, composite keys and association tables when supported by the Strategy.

Arbitrary recursive/cyclic graph synthesis is not a universal baseline promise.

### BSD-002 — mechanism-specific formal privacy

**Status:** resolved for initial baseline by 006-F — deferred.

Differential privacy/formal composable privacy accounting is not part of the initial baseline. A future mechanism with independent reusable/accounting state must reopen Jackson-style concept discovery before implementation.

### BSD-003 — external use/release governance

**Status:** reaffirmed external to current SYNGAN concept authority by 006-F.

Generation completion and favorable Evidence do not imply release/use approval. SYNGAN may hand off Evidence/Provenance and enforce current authorization decisions without creating hidden semantic approval state.

### BSD-004 — broader Strategy/Evaluation catalog

**Status:** deferred beyond the minimum diverse reference design probes.

006-D completed the minimum falsification set. Broader Strategy/Evaluation/privacy-attack catalog breadth remains later delivery work.

### BSD-005 — time-series / temporal-table synthesis

**Status:** included in the complete baseline capability target by 006-G.

Time-series preserves explicit entity/series membership and temporal/order semantics through Data Meaning, temporal validity through Constraints, requested horizon/scope through Generation, and method-specific capability through Strategy.

The baseline does not promise every sequence-model family, streaming/online generation, regular cadence, or arbitrary temporal hierarchy.

## Implementation/release debt

### IRD-001 — exact provider/runtime support matrix

Select exact Spark/Python/PyTorch/Databricks/storage/runtime versions only when implementation and conformance evidence exists.

### IRD-002 — exact IAM/secret/network/KMS/DLP products

Current architecture defines required contracts; concrete enterprise products remain deployment selections.

### IRD-003 — benchmark thresholds and support claims

Exact support thresholds must come from reproducible implementation evidence rather than design assertion.

### IRD-004 — SLO/SLA and capacity policies

Operational objectives, queue/admission defaults and capacity policy remain delivery/operator decisions after benchmark evidence exists.

### IRD-005 — public package/name/ecosystem review

Before public release, verify PyPI/package naming, project-name collisions, trademarks and adjacent ecosystem usage. SynGAN remains the current brand; do not publicly define it as a Spark port of CTGAN.

### IRD-006 — exact Spark/runtime distribution mechanism

ADR-0010 and the Phase 006 runtime-closure authority define what must be true, but not one universal packaging/distribution mechanism. Later delivery must choose and verify profile-specific approaches.

### IRD-007 — concrete privacy/disclosure Evaluation catalog

The framework supports privacy/disclosure-risk Evaluation but does not select one universal attack suite or privacy score. Later delivery may choose a small reference/conformance set while preserving threat-model/scope/claim-strength distinctions.

### IRD-008 — concrete baseline topology Strategy catalog

Later authorized implementation/delivery must provide at least one supported self-contained Strategy path for:

- single-table;
- time-series;
- multi-table shared-key.

The algorithms may differ materially and must preserve model/topology neutrality.

### IRD-009 — exact actionability/result/error representation

006-H/006-I require typed programmatic distinctions for queue/block/incompatibility/denial/recovery/disclosure/history, but do not select exact Python exception classes, SDK result objects, REST status codes or wire enums.

### IRD-010 — exact non-regressing recovery realization

ADR-0009 requires a fresh recovery-authority frontier, but exact realization (`ControlPlaneIncarnation`, external monotonic fence, provider-native generation, credential/namespace rotation combination, etc.) remains deployment implementation work.

## Governance debt

### GOV-001 — strict external OKF 0.2 normalization

The repository uses a project-specific OKF-oriented profile. Strict external OKF 0.2 reserved-file/frontmatter conformance has not been asserted as complete.

This remains non-blocking unless it creates authority ambiguity.

## Backlog discipline

Closing or changing a backlog item does not itself change design authority.

If resolution changes a concept, synchronization, experience contract, architecture contract or implementation plan, the canonical owner must be updated explicitly and the backlog item should link to that accepted change.
