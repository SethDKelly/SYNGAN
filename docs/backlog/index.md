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
- **implementation/release debt** — resolved during later delivery or publication work rather than by redefining concepts now;
- **governance debt** — documentation/process work that does not currently block product-design readiness unless it causes authority ambiguity.

Canonical facts remain under `docs/authority/`, `docs/concepts/`, `docs/synchronizations/`, `docs/experience/`, `docs/architecture/`, and `docs/implementation/`.

## Blocking design refinement

### BDR-001 — regressive restore and temporal authority closure

**Status:** open — Phase 006 blocking.

005-J exposed the case where restoring older control state while newer external workers/effects survive can resurrect stale writer authority unless restore introduces a non-regressing recovery boundary.

Phase 006 must validate the observable semantics across Execution, cancellation, security, history, recovery and operator experience, and promote the necessary invariant upstream. `ControlPlaneIncarnation`/equivalent remains a candidate realization rather than unquestioned concept authority.

### BDR-002 — post-planning adversarial end-to-end validation

**Status:** open — Phase 006 blocking.

A full-system scenario audit must re-test the eleven concepts and fifteen synchronizations against the concrete A-J plans, including ambiguous launch, stale writers, retry/resume, cancellation races, revocation, projection outages, mixed versions, retention loss, platform fallback, security-domain isolation and disaster recovery.

### BDR-003 — representative Strategy/method design probes

**Status:** open — Phase 006 blocking.

The model-neutral runtime architecture must be stress-tested against materially different synthesis/evaluation shapes before infrastructure implementation begins. At minimum, design probes should cover a Learning-based deep-generative family, a direct/simple generation path, and representative large-scale Evaluation methods.

This does not authorize implementation of CTGAN or any other algorithm during design refinement.

### BDR-004 — initial-baseline scope and future-extensibility closure

**Status:** open — Phase 006 blocking.

The current implementation baseline intentionally excludes several possible future product domains. Phase 006 must explicitly reaffirm which are outside the first baseline and validate that existing concept/experience/architecture contracts do not accidentally make those exclusions permanent implementation assumptions.

The relevant scope items are BSD-001 through BSD-004 below.

## Baseline scope decisions

### BSD-001 — relational/multi-table synthesis

**Status:** deferred from initial baseline; extensibility validation required in Phase 006.

Current structured/tabular scope must not hard-code a permanent single-table invariant. Relationship/multi-table concepts are reopened only through explicit upstream design authority.

### BSD-002 — mechanism-specific formal privacy

**Status:** deferred from initial baseline; scope boundary revalidation required in Phase 006.

Privacy/disclosure-risk Evaluation and Evidence remain valid without claiming a formal privacy mechanism. Differential privacy or another mechanism with independent budget/state/actions may require new concept discovery if introduced.

### BSD-003 — external use/release governance

**Status:** external to current SYNGAN concept authority.

Generation completion and favorable Evidence do not imply release/use approval. Phase 006 should confirm this remains an intentional external authority seam.

### BSD-004 — broader Strategy/Evaluation catalog

**Status:** deferred beyond minimum reference design probes.

The framework should not attempt to design every method before implementation. A minimum diverse reference set is required for design validation; broader catalog breadth can remain backlog.

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