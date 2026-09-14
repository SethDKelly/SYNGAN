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
Phase 010                    ACTIVE
010-A                        COMPLETE
010-B                        COMPLETE
010-C                        NEXT ELIGIBLE
F1                           CURRENTLY CLOSED
architecture corpus          RETAINED AS DOWNSTREAM DESIGN EVIDENCE
architecture reconciliation  PLANNED FOR PHASE 013
implementation readiness     NOT READY
implementation start         NOT STARTED
implementation next          NOT YET
```

## Current upstream mapping authority

- [Concept Mapping Authority](../mapping/index.md)
- [010-A Mapping Control Authority](../mapping/mapping-authority-coverage-actor-surface-evidence-baseline.md)
- [010-B Concept Action Mapping](../mapping/concept-action-actor-intent-interaction-mapping.md)

010-B establishes 66 surface-neutral semantic action mappings.

Architecture MUST NOT translate that inventory mechanically into:

```text
one command mapping -> one method/endpoint
one concept action  -> one event/message
one lifecycle       -> one status enum/table
one concept         -> one service/package
one actor role      -> one UI persona/ACL role
one surface family -> one mandatory product component
```

System-established actions may have no direct physical control. Conversely, one conceptual action may require several physical interactions later.

## 010-C remains upstream design

010-C will map state/query/history/explanation into actor/programmatic inspection obligations.

Architecture may provide feasibility/counterexample evidence but must not preempt that work by treating current database tables, public resources, telemetry objects, graph structures, dashboards or platform job APIs as canonical inspection mappings.

A composed inspection view may join several concept-owned facts for comprehension while canonical ownership remains upstream.

## Phase 007 architecture status

The [Phase 007 Consolidated Architecture Contract](phase-007-consolidated-architecture-contract.md) remains the strongest retained architecture synthesis through 007-J.

It remains subject to Phase 013 reconciliation after Jackson concept design is completed in Phase 012.

## Phase 013 obligation

After a positive Phase 012 Jackson completion decision, Phase 013 must reconcile retained architecture with final concept/dependence/application-family/composition/mapping authority.

## Phase 014 gate

Only after Phase 013 may Phase 014 decide implementation readiness.

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## Current next boundary

**010-C — Concept State, Query, History & Explanation → Inspection Mapping** is next eligible.

Architecture reconciliation remains deferred to Phase 013.
