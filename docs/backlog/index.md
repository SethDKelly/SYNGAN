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

**Status:** semantic/synchronization closure accepted; experience/architecture propagation pending 006-H and 006-I.

006-B established the canonical [Operational Authority Continuity & Regressive Recovery Contract](../authority/operational-authority-continuity-regressive-recovery-contract.md). 006-C adversarially validated the synchronization consequences without creating `SYNC-16`.

Remaining work is downstream propagation rather than unresolved concept semantics.

### BDR-002 — post-planning adversarial end-to-end validation

**Status:** resolved by 006-C for the accepted eleven-concept / fifteen-synchronization model.

006-G conceptually replayed the topology-sensitive multi-table/time-series/privacy scenarios after resolving Relationship as Data Meaning-owned structural semantics. The existing synchronization set remains coherent.

006-I/006-J must replay affected scenarios only if architecture/planning reconciliation materially changes accepted coordination.

### BDR-003 — representative Strategy/method and topology design probes

**Status:** resolved by 006-D.

The current model survived Learning-based, direct, text, composite, time-series, multi-table, deterministic/statistical Evaluation, large-state and Spark-distribution probes.

006-G's topology decision does not invalidate the runtime probe result: topology semantics remain upstream of Strategy/runtime implementation.

### BDR-004 — initial-baseline scope and future-extensibility closure

**Status:** **resolved by 006-G**.

Canonical authority: [Structured-Data Topology & Relationship Semantics Contract](../authority/structured-data-topology-relationship-semantics-contract.md).

The first **complete structured-data capability baseline** includes:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

Implementation may be staged and individual Strategies may support subsets, but the complete baseline claim requires at least one supported self-contained Strategy path for each family.

`Relationship` is not a standalone concept. Material shared-key/sequence structural semantics are Data Meaning-owned descriptive state; Constraint owns prescriptive validity; Generation owns requested topology/scope; Strategy owns capability.

Topology presets may be exposed through future API convenience syntax, but the durable model must permit composition and cannot be reduced to one mutually exclusive enum.

No Phase 006 concept/scope blocker remains open after 006-G. 006-H/006-I still must propagate the accepted design into experience and architecture/planning before 006-J can judge implementation readiness.

## Baseline scope decisions

### BSD-001 — relational/multi-table shared-key synthesis

**Status:** **included in the complete baseline capability target by 006-G**.

The baseline covers explicit shared-key relationships and common relational shapes such as one-to-one, one-to-many/many-to-one, composite keys and association tables when supported by the Strategy.

Arbitrary recursive/cyclic graph synthesis is not a universal baseline promise. Strategy capability may support, limit or reject those shapes explicitly.

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

**Status:** **included in the complete baseline capability target by 006-G**.

Time-series must preserve explicit entity/series membership and temporal/order semantics through Data Meaning, temporal validity through Constraints, requested horizon/scope through Generation, and method-specific capability through Strategy.

The baseline does not promise every sequence-model family, streaming/online generation, regular cadence, or arbitrary temporal hierarchy.

## Implementation/release debt

### IRD-001 — exact provider/runtime support matrix

Select exact Spark/Python/PyTorch/Databricks/storage/runtime versions only when later implementation and conformance evidence exists.

### IRD-002 — exact IAM/secret/network/KMS/DLP products

005-I/Phase 006 define the contracts; concrete enterprise products remain deployment selections.

### IRD-003 — benchmark thresholds and support claims

Exact support thresholds must come from reproducible implementation evidence rather than design assertion.

### IRD-004 — SLO/SLA and capacity policies

Operational objectives, queue/admission defaults and capacity policy remain delivery/operator decisions after benchmark evidence exists.

### IRD-005 — public package/name/ecosystem review

Before public release, verify PyPI/package naming, project-name collisions, trademarks and adjacent ecosystem usage. SynGAN remains the current brand; do not publicly define it as a Spark port of CTGAN.

### IRD-006 — exact Spark/runtime distribution mechanism

006-D establishes runtime distribution closure but intentionally does not select one universal packaging/distribution mechanism. Later delivery must choose and verify profile-specific approaches while preserving exact closure across all material workers.

### IRD-007 — concrete privacy/disclosure Evaluation catalog

006-F keeps privacy/disclosure-risk Evaluation in the framework capability surface but does not select a universal attack suite or privacy score. Later delivery may choose a small reference/conformance set while preserving threat-model/scope/claim-strength distinctions.

### IRD-008 — concrete baseline topology Strategy catalog

006-G defines the complete capability target but does not select the exact first algorithms for all topology families.

Later implementation/delivery must provide at least one supported self-contained Strategy path for:

- single-table;
- time-series;
- multi-table shared-key.

The algorithms may differ materially and must continue to preserve model/topology neutrality rather than becoming framework semantics.

## Governance debt

### GOV-001 — strict external OKF 0.2 normalization

The repository uses a project-specific OKF-oriented profile. Strict external OKF 0.2 reserved-file/frontmatter conformance has not been asserted as complete.

This remains non-blocking unless it creates authority ambiguity.

## Backlog discipline

Closing or changing a backlog item does not itself change design authority.

If resolution changes a concept, synchronization, experience contract, architecture contract or implementation plan, the canonical owner must be updated explicitly and the backlog item should link to that accepted change.
