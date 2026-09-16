---
type: Architecture Index
title: SYNGAN Representation & Architecture Design
status: retained-pending-reconciliation
---

# SYNGAN Representation & Architecture Design

## Purpose

Preserve SYNGAN representation/architecture design as downstream evidence while Jackson concept design remains active.

Current governing authority: [Jackson Design Completion & Implementation Hold](../authority/jackson-design-completion-implementation-hold.md).

## Current posture

```text
Jackson concept design       IN PROGRESS
Phase 008                    COMPLETE
Phase 009                    COMPLETE
D1-D4                        CURRENTLY CLOSED
E1-E5                        CURRENTLY CLOSED
Phase 010                    COMPLETE
F1-F5                        CURRENTLY CLOSED
Phase 011                    ACTIVE
011-A                        COMPLETE
011-B                        COMPLETE
011-C                        COMPLETE
011-D                        NEXT ELIGIBLE
G1 specificity               CURRENTLY CLOSED
G2 familiarity               CURRENTLY CLOSED
architecture corpus          RETAINED AS DOWNSTREAM DESIGN EVIDENCE
architecture reconciliation  PLANNED FOR PHASE 013
implementation readiness     NOT READY
implementation start         NOT STARTED
implementation next          NOT YET
```

## Current upstream design authority

- [Phase 010 Concept Mapping Consolidation](../authority/phase-010-concept-mapping-consolidation.md)
- [Concept Mapping Authority](../mapping/index.md)
- [Design Quality Validation Authority](../authority/design-quality-validation-authority.md)
- [Composed Specificity Audit](../authority/composed-specificity-purpose-boundary-audit.md)
- [Composed Familiarity / External-Model Audit](../authority/composed-familiarity-reuse-vocabulary-external-model-audit.md)
- [Phase 011](../phases/011/index.md)

Phase 011 is upstream design-quality/misfit validation. Architecture may expose counterexamples or feasibility concerns but does not define the audit criteria merely because a structure already exists.

## Completed mapping implications

Architecture must eventually preserve package-first product form/Spark-host agnosticism, current versus exact historical state, semantic versus operational state, candidate versus authoritative result, Evidence interpretation context, Provenance without source-fact ownership, authorization-relative disclosure/history quality, recovery authority continuity, optional application-family capabilities, bounded enterprise-scale inspection and human/programmatic semantic parity.

Phase 010 does not select database/materialized views, resource/query schemas, GraphQL/REST shapes, graph/search technology, event-sourced persistence, dashboards, public Python API shapes or platform adapter implementations. Those remain downstream representation choices for Phase 013 reconciliation.

## 011-B / 011-C implications

011-B confirms all eleven concepts retain distinct composed purposes without architecture-driven split/merge/add/remove decisions.

011-C confirms familiar external object models remain analogues rather than architecture requirements. In particular:

```text
SDV Synthesizer              != mandatory aggregate architecture object
Spark ML Estimator / Model   != required SYNGAN class hierarchy
MLflow Run / Model / Artifact != required tracking/registry architecture
Great Expectations objects   != required validation architecture
OpenLineage Job/Run/Dataset  != required provenance representation
fit / sample / run / model   != selected public API names
```

Qualified compatibility vocabulary may later influence adapter ergonomics, but Phase 013 must still select representations against completed concept authority rather than copying the external models.

Current bounded watch points remain conceptual:

- Synthesis Strategy must not become a plugin/runtime/configuration registry by architecture convenience;
- Provenance's high fan-in must not cause a graph/catalog/lineage representation to become owner truth.

## Phase 011 evidence boundary

Phase 011 may use retained architecture as counterexample, feasibility, provider-semantic-leakage or familiarity evidence. It may not infer concept boundaries, canonical lifecycle, dependence or synchronization from existing services/packages/APIs/job models/artifacts/tests.

011-D now tests synchronization/correction/history integrity. Architecture must remain observational during that audit; transactional/event/storage mechanisms are Phase 013 concerns.

## Phase 007 architecture status

The [Phase 007 Consolidated Architecture Contract](phase-007-consolidated-architecture-contract.md) remains the strongest retained architecture synthesis through 007-J and is subject to Phase 013 reconciliation after Jackson concept design is completed in Phase 012.

## Phase 014 gate

Only after Phase 013 may Phase 014 decide implementation readiness.

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## Current next boundary

**011-D — Integrity Under Synchronization, Correction, Invalidation & Historical Composition** is next eligible.

Architecture reconciliation remains deferred to Phase 013.
