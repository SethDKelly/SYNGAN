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

**Status:** semantic closure accepted in 006-B; synchronization validation completed in 006-C; experience/architecture propagation pending 006-H and 006-I.

006-B established the canonical [Operational Authority Continuity & Regressive Recovery Contract](../authority/operational-authority-continuity-regressive-recovery-contract.md).

Accepted design consequences include:

- persistence restore is not proof of current writer authority;
- potentially regressive recovery enters recovery quarantine / continuity-unverified state;
- a non-regressing post-recovery authority boundary is required before ordinary writes resume;
- rollback cannot resurrect superseded Attempts, lost cancellation generations or old capabilities/credentials;
- surviving effects are reconciled rather than automatically accepted or denied as history;
- missing post-backup canonical facts remain reconstructable/unknown/unavailable according to evidence rather than being silently treated as absence;
- `ControlPlaneIncarnation`/equivalent remains an architecture realization candidate, not a concept.

006-C adversarially validated this contract against SYNC-01 through SYNC-15 and refined existing synchronization wording without creating `SYNC-16`. The original semantic/synchronization gap is closed; 006-H and 006-I still own experience and architecture/planning propagation.

### BDR-002 — post-planning adversarial end-to-end validation

**Status:** resolved by 006-C for the current eleven-concept / fifteen-synchronization baseline.

[006-C](../phases/006/006-C-end-to-end-scenario-exception-failure-adversarial-synchronization-validation.md) evaluated twenty-four normal/adversarial scenarios covering Learning-based and direct Generation, ambiguous launch, stale writers, cancellation races, authorization/dependency changes, projection outage, retention loss, mixed versions, platform fallback, security isolation, regressive recovery, repeated Evaluation work, and topology-sensitive time-series/multi-table cases.

The result was **PASS WITH TARGETED SYNCHRONIZATION REFINEMENT**. SYNC-04, SYNC-07, SYNC-08, SYNC-11, SYNC-14 and SYNC-15 were refined while the synchronization count remained fifteen.

If later Phase 006 work accepts a new `Relationship` concept or materially changes accepted coordination/architecture, affected scenarios must be replayed conceptually in 006-I/006-J before readiness approval.

### BDR-003 — representative Strategy/method and topology design probes

**Status:** resolved by 006-D for the current concept/runtime baseline.

[006-D](../phases/006/006-D-reference-strategy-method-topology-design-probes-algorithm-neutrality-stress-test.md) stress-tested the design against Learning-based deep-generative, direct-generation, self-contained and pretrained/network text, composite mixed-field, time-series, multi-table shared-key, deterministic/bounded and statistical/approximate Evaluation, large/sharded Learned State, and Spark cluster-distribution shapes.

The result was **PASS WITH TARGETED CROSS-CUTTING REFINEMENT**.

006-D established the canonical [Self-Contained Execution & Runtime Distribution Closure Contract](../authority/self-contained-execution-runtime-distribution-closure-contract.md), including:

- at least one supported baseline source-derived/local text-capable synthesis path requiring no pretrained artifact or runtime network service;
- optional local-artifact and runtime-network text capability remaining explicit and non-baseline;
- exact implementation closure may contain multiple code/runtime/model/tokenizer/codec components;
- driver import/availability is not proof of Spark executor readiness;
- all material workers, including dynamically allocated workers, must satisfy compatible runtime distribution closure;
- large model/state distribution cannot universally require driver-local materialization/broadcast.

No new domain concept or synchronization was required. If 006-G/006-I materially changes Strategy/topology/runtime architecture, affected probes must be replayed before 006-J readiness approval.

### BDR-004 — initial-baseline scope and future-extensibility closure

**Status:** open — Phase 006 blocking; principal unresolved topology decision remains 006-G.

Phase 006 must explicitly determine the initial implementation scope while proving that deferred capabilities are not accidentally made impossible by current concept/API/schema/architecture assumptions.

The structured-data topology decision includes:

```text
single-table                current baseline capability
time-series                 explicit candidate capability
multi-table shared-key      explicit candidate capability; Relationship reopened
```

006-G owns the concept/extensibility decision. A future function parameter may select a topology, but the parameter cannot substitute for the underlying descriptive relationship/temporal semantics.

The baseline self-contained text-bearing requirement is already accepted by 006-D. 006-F has now also closed the privacy/release scope ambiguity: disclosure-risk Evaluation is in-scope, formal DP is deferred behind future concept discovery, and release/use governance remains external.

## Baseline scope decisions

### BSD-001 — relational/multi-table shared-key synthesis

**Status:** candidate capability; initial-implementation inclusion TBD in Phase 006.

Current contracts must not hard-code a permanent single-table invariant. Phase 006-A reopened `Relationship` as a candidate concept because shared-key linkage may have reusable descriptive purpose independent of Data Meaning and Constraint.

006-C confirmed that Generation/Constraint/Evaluation coordination can already represent one logical multi-table result and prevent partial constituent completion from being mistaken for total completion. 006-D confirmed that multi-component Strategy/Learned-State/runtime shapes do not by themselves require architecture redesign. 006-E added shared-key cardinality/fan-out/whole-result scale obligations. 006-F added the requirement that disclosure-risk Evaluation may need to bind joined/whole-output topology scope. 006-G must still decide whether the descriptive shared-key structure itself requires `Relationship` or another narrower boundary.

### BSD-002 — mechanism-specific formal privacy

**Status:** resolved for initial baseline by 006-F — deferred; future formal mechanism requires concept discovery before implementation.

The canonical [Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract](../authority/privacy-disclosure-formal-guarantee-release-boundary-contract.md) establishes:

- synthetic origin is not a privacy/anonymization guarantee;
- disclosure/memorization questions remain Criterion/Evaluation/Evidence concerns;
- favorable empirical Evidence does not become a formal privacy guarantee;
- differential privacy is not part of the initial implementation baseline;
- a future composable DP/formal mechanism with independent state/actions must reopen Jackson-style concept discovery before implementation;
- privacy-budget/accounting state must not be hidden inside generic Strategy metadata, Evidence, deployment quota or implementation configuration.

This item no longer blocks current initial-baseline readiness when that deferral boundary is preserved.

### BSD-003 — external use/release governance

**Status:** reaffirmed external to current SYNGAN concept authority by 006-F.

Generation completion and favorable Evidence do not imply release/use approval.

SYNGAN may provide Evidence/Provenance to external governance systems and enforce their current authorization decisions through security adapters, but external policy must not create hidden semantic `approved` state on Generation, Output or Evidence.

This item is a deliberate product boundary rather than an unresolved design blocker.

### BSD-004 — broader Strategy/Evaluation catalog

**Status:** deferred beyond the minimum diverse reference design probes.

006-D has completed the minimum diverse falsification set. The framework should not attempt to design every synthesis/Evaluation family before implementation; broader catalog breadth can remain backlog.

Privacy/disclosure-risk Evaluation is part of the framework capability surface, but concrete attack-suite breadth remains delivery/catalog work rather than a reason to design every privacy method now.

### BSD-005 — time-series / temporal-table synthesis

**Status:** candidate capability; initial-implementation inclusion TBD in Phase 006.

Time-series must not be reduced to “single-table plus timestamp.” Phase 006 must validate entity/series identity, temporal ordering, horizon/continuation semantics, temporal Constraints, Strategy capability, Evaluation claim strength, checkpoint/recovery consequences and enterprise-scale behavior.

006-C confirmed that interrupted time-series continuation and validation-later temporal rules compose with existing activity/Execution/Evaluation synchronizations. 006-D confirmed that representative sequence-model/runtime/checkpoint shapes fit the current runtime model. 006-E added sequence-cardinality/horizon/resource obligations. 006-F confirmed that disclosure-risk Evaluation may need trajectory-level rather than row-level subjects. 006-G must still test whether reusable sequence membership/order semantics fit the reopened generic `Relationship` candidate or remain adequately owned by existing concepts.

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

### IRD-006 — exact Spark/runtime distribution mechanism

006-D establishes runtime distribution closure as an invariant but intentionally does not select one universal mechanism. Later implementation/deployment work must choose and verify profile-specific delivery such as immutable cluster/container environments, Spark-native pure-Python shipping where sufficient, packed environments/archives/PEX/equivalent, provider-managed libraries, and exact distributed artifact/model/state resolution.

A selected mechanism must satisfy the canonical [Self-Contained Execution & Runtime Distribution Closure Contract](../authority/self-contained-execution-runtime-distribution-closure-contract.md); driver-only package availability is insufficient.

### IRD-007 — concrete privacy/disclosure Evaluation catalog

006-F keeps privacy/disclosure-risk Evaluation in the initial framework capability surface but does not select a universal attack suite or privacy score.

Later implementation may choose a small reference/conformance set of Criteria/method bindings for duplication/memorization/disclosure testing. Method breadth must preserve threat-model/scope/claim-strength distinctions and must not imply formal privacy or release approval.

## Governance debt

### GOV-001 — strict external OKF 0.2 normalization

The repository uses a project-specific OKF-oriented profile. Strict external OKF 0.2 reserved-file/frontmatter conformance has not been asserted as complete.

This is non-blocking for current product-design refinement unless authority ambiguity is discovered, but it should be audited separately before claiming strict conformance.

## Backlog discipline

Closing or changing a backlog item does not itself change design authority.

If resolution changes a concept, synchronization, experience contract, architecture contract or implementation plan, the canonical owner must be updated explicitly and the backlog item should link to that accepted change.
