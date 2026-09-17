---
type: Architecture Index
title: SYNGAN Representation & Architecture Design
status: active-reconciliation
---

# SYNGAN Representation & Architecture Design

## Purpose

Reconcile retained SYNGAN representation/architecture against the completed Jackson concept design and establish one current architecture baseline for the Phase 014 whole-design completion/readiness gate.

Current governing authority: [Phase 013 Architecture Reconciliation Authority](../authority/phase-013-architecture-reconciliation-authority.md).

## Current posture

```text
Jackson concept design          COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 012                       COMPLETE
H1/H2                           CURRENTLY CLOSED
Phase 013                       ACTIVE
013-A                           COMPLETE
013-B                           COMPLETE
013-C                           NEXT ELIGIBLE
architecture corpus             UNDER RECONCILIATION
R1 architecture reconciliation  DOWNSTREAM / IN PROGRESS
whole-design completion         NOT YET — PHASE 014
implementation readiness        NOT READY
implementation start            NOT STARTED
implementation next             NOT YET
```

Completed concept design and completed Phase 013 reconciliation decisions are upstream authority for unreconciled retained architecture.

## Current Phase 013 authority

- [Phase 013 Architecture Reconciliation Authority](../authority/phase-013-architecture-reconciliation-authority.md)
- [Phase 013 Index](../phases/013/index.md)
- [013-A Reconciliation Authority / Corpus Inventory / Taxonomy](../phases/013/013-A-reconciliation-authority-retained-corpus-inventory-precedence-reset-discrepancy-taxonomy.md)
- [013-B Phase Record](../phases/013/013-B-representation-layering-public-contract-identity-revision-handle-view-reconciliation.md)
- [013-B Representation Reconciliation Authority](phase-013-b-representation-layering-public-contract-identity-view-reconciliation.md)
- [Phase 013 Entry & Decomposition](../phases/013/013-entry-decomposition.md)
- [Phase 012 Jackson Concept-Design Consolidation](../authority/phase-012-jackson-concept-design-consolidation.md)

## 013-A retained corpus inventory

Phase 013 reconciles 19 substantive retained architecture documents plus ADR-0001 through ADR-0010. Phase 005 planning, Phase 007-A..C scaffold/bootstrap work, Phase 007-K readiness history, source and tests are supporting evidence rather than architecture authority.

A historical `status: active` or `canonical` statement does not outrank completed Phase 012 authority or a later Phase 013 reconciliation decision.

## 013-B representation baseline

The current representation spine is now reconciled as:

```text
completed semantic / synchronization / mapping authority
        ↓ represented by
stable logical identity + exact references
        ↓
owner-qualified bounded views / handles
        ↓
application coordination / optional convenience façades
        ↓
ports / adapters / host integration
```

This is dependency/representation direction, not a mandatory runtime workflow or package/service topology.

Current representation invariants include:

- architecture represents upstream semantic authority rather than becoming a second semantic owner;
- logical layers do not imply packages, services, processes, database schemas, API tiers or D0-D4 levels;
- Python package/SDK, notebook and embedded automation remain primary; CLI/report/graphical/service surfaces remain optional/integration roles;
- parity applies to surfaces that exist rather than requiring every optional surface;
- stable logical identity remains distinct from mutable locator/provider identity;
- logical identity, exact semantic revision/commitment, current state version/freshness and representation schema version remain distinct axes;
- exact historical bindings remain non-reactive while current views may refresh;
- handles/views resolve and compose authority but do not become detached canonical entities;
- retry/resume/reconcile/cancel operational state remains Execution-owned even when an activity-facing façade forwards the action;
- `Result handle` is representation shorthand rather than a shared Result concept or lifecycle;
- readiness/actionability remains contextual/derived rather than a global status owner;
- D0-D4 remains semantic disclosure depth rather than technical architecture tiers;
- public/control interaction remains bounded/reference-first at Spark scale.

## 013-B findings

```text
A13-B-001  layer-A semantic/control wording              AR-2/AR-3  AMAT-1  RESOLVED
A13-B-002  activity-handle cancellation wording          AR-3       AMAT-1  RESOLVED
A13-B-003  optional-surface parity wording               AR-7       AMAT-1  RESOLVED
A13-B-004  generic promoted-result wording               AR-3/AR-6  AMAT-1  RESOLVED
A13-B-005  007-D historical synchronization count        AR-1       AMAT-1  SEMANTICALLY RESOLVED; CLEANUP 013-I
A13-B-006  historical representation precedence wording AR-2       AMAT-1  CURRENT AMBIGUITY RESOLVED; CLEANUP 013-I
A13-B-007  D0-D4 technical-tier risk                     AR-0       AMAT-0  CLOSED GUARDRAIL
```

Result:

```text
AMAT-2 representation defects   0
AMAT-3 blockers                 0
AR-9 contradictions             0
upstream reopen                 NONE
```

## Retained subject disposition after 013-B

```text
Phase 004-A representation/layering          ALIGNED-WITH-CLARIFICATION
Phase 004-B public handle/resource model     ALIGNED-WITH-CLARIFICATION
Phase 004-C identity/revision/view subset    ALIGNED
Phase 007-D representation refinement        ALIGNED-WITH-CLARIFICATION
ADR-0001                                    PROVISIONAL RETAIN
ADR-0002                                    PROVISIONAL RETAIN
```

Persistence/concurrency aspects of Phase 004-C and ADR-0002 continue into 013-C. Final ADR lifecycle/status disposition remains 013-I work.

## Reconciliation taxonomy

Phase 013 continues to use AR-0..AR-9, AMAT-0..AMAT-3 and the dispositions `RETAIN / CLARIFY / SUPERSEDE / CORRECT / DEFER / UPSTREAM-REOPEN`. Only a demonstrated AR-9 finding may justify upstream reopen.

## Architecture constraints from completed concept design

Phase 013 must preserve unless a genuine explicit upstream reopen is justified:

- package-first Python/Spark product form and Spark-host agnosticism;
- eleven concept boundaries and singular ownership;
- thirteen occurrence-scoped active synchronizations;
- application-family optionality and capability-local burden;
- current versus exact historical truth;
- semantic versus operational state/completion;
- candidate/non-final versus authoritative Generation result;
- Criterion/Evaluation/Evidence separation;
- Evidence without approval/release/privacy takeover;
- Provenance relationship authority without source-fact takeover;
- recovery authority continuity;
- provider facts only at actual evidentiary strength;
- material approximation as explicit and owner-scoped;
- decision-material qualifiers when they affect immediate semantic decisions;
- future rediscovery before architecture for new independent product purposes.

## Phase 013 sequence

```text
013-A  reconciliation authority / corpus inventory / precedence / discrepancy taxonomy  COMPLETE
013-B  representation / layering / public contract / identity / views                   COMPLETE
013-C  persistence / history / transaction-concurrency / migration                      NEXT
013-D  distributed data / topology / manifest / candidate-seal-promotion
013-E  Strategy/runtime / dependency / security / offline-no-egress
013-F  Execution / Attempt / recovery / fencing / admission
013-G  Evaluation / Evidence / Provenance / history / disclosure
013-H  deployment / scale / observability / portability / platform integration
013-I  cross-architecture / ADR / legacy / M6 / residual register
013-J  consolidation / R1 decision / Phase 014 handoff
```

## M6 / M8 carry-forward

Current synchronization authority remains 15 historical IDs / 13 active rules, with SYNC-08 retired and SYNC-15 reclassified. Historical current-looking wording remains a 013-I cleanup obligation.

M8 future rediscovery triggers remain excluded from architecture absent renewed concept discovery.

## Implementation boundary

Phase 013 remains design/reconciliation only.

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## Current next boundary

**013-C — Control Persistence, Historical Reference, Transaction/Concurrency, Migration & Recovery-State Reconciliation** is next eligible.
