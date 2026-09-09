---
type: Backlog
title: SYNGAN Design & Delivery Backlog
status: active
---

# SYNGAN Design & Delivery Backlog

## Purpose

Track unresolved or deliberately deferred work without allowing backlog notes to become canonical design authority.

Items are classified as:

- **blocking design refinement** — must be resolved before a later implementation-authority phase may begin;
- **baseline scope decision** — may remain out of the first implementation if explicitly reaffirmed and extensibility is preserved;
- **implementation/release debt** — resolved during later delivery/publication work;
- **governance debt** — documentation/process work that does not currently block product-design readiness unless it causes authority ambiguity.

Canonical facts remain under `docs/authority/`, `docs/concepts/`, `docs/synchronizations/`, `docs/experience/`, `docs/architecture/`, and `docs/implementation/`.

## Blocking design refinement

### BDR-001 — regressive restore and temporal authority closure

**Status:** semantic closure accepted in 006-B; adversarial/experience/architecture propagation pending 006-C, 006-H and 006-I.

006-B established the canonical [Operational Authority Continuity & Regressive Recovery Contract](../authority/operational-authority-continuity-regressive-recovery-contract.md).

Accepted design consequences include:

- persistence restore is not proof of current writer authority;
- potentially regressive recovery enters recovery quarantine / continuity-unverified state;
- a non-regressing post-recovery authority boundary is required before ordinary writes resume;
- rollback cannot resurrect superseded Attempts, lost cancellation generations or old capabilities/credentials;
- surviving effects are reconciled rather than automatically accepted or denied as history;
- missing post-backup canonical facts remain reconstructable/unknown/unavailable according to evidence rather than being silently treated as absence;
- `ControlPlaneIncarnation`/equivalent remains an architecture realization candidate, not a concept.

The original semantic/design gap is closed. The item remains in this section until 006-C validates synchronization behavior, 006-H closes actor/programmatic experience and 006-I reconciles architecture/planning authority.

### BDR-002 — post-planning adversarial end-to-end validation

**Status:** open — 006-C next.

A full-system scenario audit must re-test the accepted concepts/synchronizations against the concrete Phase 005 plans and the 006-B continuity contract, including ambiguous launch, stale writers, retry/resume, cancellation races, revocation, projection outages, mixed versions, retention loss, platform fallback, security-domain isolation, disaster recovery and topology-sensitive partial-output cases.

### BDR-003 — representative Strategy/method and topology design probes

**Status:** open — Phase 006 blocking.

The model-neutral runtime architecture must be stress-tested against materially different synthesis/evaluation shapes before infrastructure implementation begins.

At minimum, design probes must cover:

- a Learning-based single-table deep-generative family;
- a direct/simple single-table generation path;
- a time-series Strategy shape;
- a multi-table shared-key Strategy shape;
- representative deterministic/bounded and statistical/approximate Evaluation methods.

These are design/feasibility probes only. They do not authorize implementation of CTGAN, TimeGAN, a relational synthesizer or another algorithm during Phase 006.

### BDR-004 — initial-baseline scope and future-extensibility closure

**Status:** open — Phase 006 blocking.

Phase 006 must explicitly determine the initial implementation scope while proving that deferred capabilities are not accidentally made impossible by current concept/API/schema/architecture assumptions.

The structured-data topology decision includes:

```text
single-table                current baseline capability
time-series                 explicit candidate capability
multi-table shared-key      explicit candidate capability; Relationship reopened
```

006-G owns the concept/extensibility decision. A future function parameter may select a topology, but the parameter cannot substitute for the underlying descriptive relationship/temporal semantics.

## Baseline scope decisions

### BSD-001 — relational/multi-table shared-key synthesis

**Status:** candidate capability; initial-implementation inclusion TBD in Phase 006.

Current contracts must not hard-code a permanent single-table invariant. Phase 006-A reopened `Relationship` as a candidate concept because shared-key linkage may have reusable descriptive purpose independent of Data Meaning and Constraint.

006-G must decide whether existing concepts suffice, Relationship should be accepted, or a narrower boundary is required.

### BSD-002 — mechanism-specific formal privacy

**Status:** deferred from initial baseline; scope-boundary revalidation required in Phase 006.

Privacy/disclosure-risk Evaluation and Evidence remain valid without claiming a formal privacy mechanism. Differential privacy or another mechanism with independent budget/state/actions may require new concept discovery if introduced.

### BSD-003 — external use/release governance

**Status:** external to current SYNGAN concept authority.

Generation completion and favorable Evidence do not imply release/use approval. Phase 006 should confirm this remains an intentional external authority seam.

### BSD-004 — broader Strategy/Evaluation catalog

**Status:** deferred beyond the minimum diverse reference design probes.

The framework should not attempt to design every method before implementation. A minimum reference set is required to falsify hidden assumptions; broader catalog breadth can remain backlog.

### BSD-005 — time-series / temporal-table synthesis

**Status:** candidate capability; initial-implementation inclusion TBD in Phase 006.

Time-series must not be reduced to “single-table plus timestamp.” Phase 006 must validate entity/series identity, temporal ordering, horizon/continuation semantics, temporal Constraints, Strategy capability, Evaluation claim strength, checkpoint/recovery consequences and enterprise-scale behavior.

006-A did not accept a standalone `Series`, `Temporal Structure` or `TimeSeriesMode` concept. 006-G must test whether reusable temporal sequence structure fits the reopened generic `Relationship` candidate or remains adequately owned by existing concepts.

## Implementation/release debt

### IRD-001 — exact provider/runtime support matrix

Select exact Spark/Python/PyTorch/Databricks/storage/runtime versions only when later implementation and conformance evidence exists.

### IRD-002 — exact IAM/secret/network/KMS/DLP products

005-I defines the required contracts; concrete enterprise products remain deployment selections.

### IRD-003 — benchmark thresholds and support claims

005-J defines methodology dimensions. Exact support thresholds must come from reproducible implementation evidence rather than design assertion.

### IRD-004 — SLO/SLA and capacity policies

Operational objectives, queue/admission defaults and capacity policy remain delivery/operator decisions after benchmark evidence exists.

### IRD-005 — public package/name/ecosystem review

Before public release, verify PyPI/package naming, project-name collisions, trademarks and adjacent ecosystem usage. SynGAN remains the current brand; the framework must not be publicly described as a Spark port of CTGAN.

## Governance debt

### GOV-001 — strict external OKF 0.2 normalization

The repository uses a project-specific OKF-oriented profile. Strict external OKF 0.2 reserved-file/frontmatter conformance has not been asserted as complete.

This is non-blocking for current product-design refinement unless authority ambiguity is discovered, but it should be audited separately before claiming strict conformance.

## Backlog discipline

Closing or changing a backlog item does not itself change design authority.

If resolution changes a concept, synchronization, experience contract, architecture contract or implementation plan, the canonical owner must be updated explicitly and the backlog item should link to that accepted change.
