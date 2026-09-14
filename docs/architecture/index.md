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
010-B                        NEXT ELIGIBLE
architecture corpus          RETAINED AS DOWNSTREAM DESIGN EVIDENCE
architecture reconciliation  PLANNED FOR PHASE 013
implementation readiness     NOT READY
implementation start         NOT STARTED
implementation next          NOT YET
```

## Current upstream authority

- [Phase 009 Consolidation](../authority/phase-009-dependence-composition-consolidation.md)
- [Concept Dependence & Application Family](../dependence/index.md)
- [Synchronization Authority](../synchronizations/index.md)
- [Concept Mapping Authority](../mapping/index.md)
- [010-A Mapping Control Authority](../mapping/mapping-authority-coverage-actor-surface-evidence-baseline.md)

## Mapping authority is not architecture authority

010-A establishes actor roles, surface-family lenses, application-family applicability tags, coverage dimensions and a nineteen-field mapping schema.

Architecture MUST NOT translate those directly into:

- service/process boundaries;
- packages/modules;
- schemas/tables/resources;
- endpoint shapes;
- UI component trees;
- event/message types;
- aggregates/transactions/sagas;
- deployment units;
- workflow engine states;
- observer/subscription infrastructure.

In particular:

```text
mapping record != public resource schema
actor role != permission role
surface family != architecture component
application-family tag != SKU/package/deployment profile
coverage state != runtime status
```

## 010-B boundary

010-B maps normalized state-changing concept actions to actor intent and **surface-neutral** interaction obligations.

Architecture must not preempt that work by selecting methods, routes, commands, buttons, events or transactions as if they were the conceptual action itself.

Existing architecture/source may expose counterexamples or feasibility pressure only.

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

**010-B — Concept Action → Actor Intent & Interaction Mapping** is next eligible.

Architecture reconciliation remains deferred to Phase 013.
