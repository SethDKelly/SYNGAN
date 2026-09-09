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

**No identified design-readiness blocker remains open after Phase 006-J.**

006-J's canonical decision is recorded in the [Phase 006 Consolidated Design Readiness Contract](../authority/phase-006-consolidated-design-readiness-contract.md):

```text
DESIGN COMPLETE ENOUGH FOR A LATER
EXPLICIT IMPLEMENTATION-AUTHORITY PHASE
```

This does not authorize implementation; it closes the known design blockers sufficiently to enter a later explicit implementation-authority phase.

### BDR-001 — regressive restore and temporal authority closure

**Resolved.**

Closure: 006-B semantic authority; 006-C synchronization validation; 006-H actor/programmatic experience; 006-I architecture/ADR/planning propagation; 006-J replay confirmation.

### BDR-002 — post-planning adversarial end-to-end validation

**Resolved.**

006-C completed the adversarial synchronization pass; 006-G replayed topology-sensitive implications; 006-J replayed materially affected cases against the reconciled architecture/planning baseline.

### BDR-003 — representative Strategy/method and topology probes

**Resolved.**

006-D tested Learning-based, direct, text, time-series, multi-table, Evaluation, large-state and distributed-runtime shapes; 006-J found no hidden one-algorithm assumption after reconciliation.

### BDR-004 — initial-baseline scope and future-extensibility closure

**Resolved.**

Complete structured-data baseline target = single-table + time-series + multi-table shared-key, with composable topology and self-contained supported paths.

## Baseline scope decisions

### BSD-001 — relational/multi-table shared-key synthesis

**Included** in complete baseline capability target.

### BSD-002 — mechanism-specific formal privacy

**Deferred** from initial baseline. Future composable DP requires new concept discovery before implementation.

### BSD-003 — external use/release governance

**External** to current SYNGAN concept authority.

### BSD-004 — broader Strategy/Evaluation catalog

**Deferred** beyond the minimum baseline/conformance capability set.

### BSD-005 — time-series / temporal-table synthesis

**Included** in complete baseline capability target.

## Implementation/release debt

These are non-blocking for creation of an implementation-authority phase but must be resolved/evidenced during implementation/release work as appropriate.

### IRD-001 — exact provider/runtime support matrix

Select and verify exact Spark/Python/PyTorch/Databricks/storage/runtime versions during implementation/conformance.

### IRD-002 — exact IAM/secret/network/KMS/DLP products

Select deployment-specific enterprise products while preserving current security contracts.

### IRD-003 — benchmark thresholds and support claims

Establish from reproducible implementation evidence rather than design assertion.

### IRD-004 — SLO/SLA and capacity policies

Set after benchmark/operational evidence exists.

### IRD-005 — public package/name/ecosystem review

Before public release, verify PyPI/package naming, project-name collisions, trademarks and adjacent ecosystem usage.

### IRD-006 — exact Spark/runtime distribution mechanism

ADR-0010 defines required closure; later implementation selects/verifies profile-specific mechanism(s).

### IRD-007 — concrete privacy/disclosure Evaluation catalog

Select a bounded reference/conformance set without implying one universal privacy score.

### IRD-008 — concrete baseline topology Strategy catalog

Provide at least one supported self-contained Strategy path for single-table, time-series and multi-table shared-key before claiming the complete baseline.

### IRD-009 — exact actionability/result/error representation

Select Python/SDK/REST/wire representations while preserving current semantic distinctions.

### IRD-010 — exact non-regressing recovery realization

Select and verify a compliant recovery-authority mechanism (`ControlPlaneIncarnation`/external monotonic fence/provider-native generation/credential-namespace rotation combination or equivalent).

### IRD-011 — exact source-derived text algorithm

Select the baseline local/source-derived free-form-text technique during implementation. It must remain self-contained and must not make a pretrained/network dependency mandatory.

## Governance debt

### GOV-001 — strict external OKF 0.2 normalization

The repository uses a project-specific OKF-oriented profile. Strict external OKF 0.2 normalization remains non-blocking while current authority is unambiguous.

## Phase 006 exit note

The absence of open design blockers does not mean every implementation choice is predetermined. The methodology intentionally permits implementation choices when they are primarily representational and constrained by stable upstream authority.

A later explicit implementation-authority phase must still define what implementation work is authorized and what evidence gates completion.

## Backlog discipline

Closing or changing a backlog item does not itself change design authority. Canonical owner documents govern current truth.
