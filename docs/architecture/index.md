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
013-B                           NEXT ELIGIBLE
architecture corpus             UNDER RECONCILIATION
R1 architecture reconciliation  DOWNSTREAM / IN PROGRESS
whole-design completion         NOT YET — PHASE 014
implementation readiness        NOT READY
implementation start            NOT STARTED
implementation next             NOT YET
```

Completed concept design is upstream authority for architecture.

## Current Phase 013 authority

- [Phase 013 Architecture Reconciliation Authority](../authority/phase-013-architecture-reconciliation-authority.md)
- [Phase 013 Index](../phases/013/index.md)
- [013-A Reconciliation Authority / Corpus Inventory / Taxonomy](../phases/013/013-A-reconciliation-authority-retained-corpus-inventory-precedence-reset-discrepancy-taxonomy.md)
- [Phase 013 Entry & Decomposition](../phases/013/013-entry-decomposition.md)
- [Phase 012 Jackson Concept-Design Consolidation](../authority/phase-012-jackson-concept-design-consolidation.md)

## 013-A retained corpus inventory

Phase 013 reconciles:

```text
Phase 004 detailed architecture                 9
Phase 004 consolidated architecture             1
Phase 006 architecture reconciliation overlay   1
Phase 007-D..007-I refined architecture         6
Phase 007-J proof-boundary architecture         1
Phase 007 consolidated architecture             1
--------------------------------------------------
substantive retained architecture docs          19

ADR-0001..ADR-0010                              10
```

Phase 005 planning, Phase 007-A..C scaffold/bootstrap work, Phase 007-K readiness history, source and tests are supporting evidence rather than architecture authority.

A historical `status: active` or `canonical` statement does not outrank completed Phase 012 authority or a later Phase 013 reconciliation decision.

## Reconciliation taxonomy

Phase 013 uses:

```text
AR-0  aligned architecture
AR-1  terminology / count / identifier drift
AR-2  authority / precedence drift
AR-3  semantic ownership leakage / duplicate authority
AR-4  semantic-strength inflation
AR-5  temporal / recovery / historical-truth distortion
AR-6  application-family / composition distortion
AR-7  architecture over-prescription / implementation leakage
AR-8  unauthorized future-scope reservation
AR-9  genuine upstream semantic contradiction
```

Materiality:

```text
AMAT-0  editorial / historical-only
AMAT-1  bounded architecture clarification
AMAT-2  material architecture defect
AMAT-3  architecture blocker / upstream contradiction candidate
```

Allowed dispositions:

```text
RETAIN
CLARIFY
SUPERSEDE
CORRECT
DEFER
UPSTREAM-REOPEN
```

Only a demonstrated AR-9 finding may justify upstream reopen.

## Known 013-A entry findings

Six bounded candidates are registered:

```text
A13-A-001  historical 15-sync inventory shown as current         AR-1 / AMAT-1
A13-A-002  historical SYNC-08 role                               AR-1 / AMAT-1
A13-A-003  historical SYNC-15 role                               AR-1 / AMAT-1
A13-A-004  retained Phase 006/007 current/canonical wording      AR-2 / AMAT-1
A13-A-005  ADR-index Phase-007-as-current precedence             AR-2 / AMAT-1
A13-A-006  historical implementation-reentry/scaffold assumptions AR-7 / AMAT-0..1
```

013-A declares no AMAT-2 defect, no AMAT-3 blocker and no upstream reopen. Later groups determine whether deeper architecture defects exist.

## Architecture constraints from completed concept design

Phase 013 must preserve unless a genuine explicit upstream reopen is justified:

- package-first Python/Spark product form and Spark-host agnosticism;
- eleven concept boundaries and singular ownership;
- thirteen occurrence-scoped active synchronizations;
- application-family optionality and capability-local burden;
- current versus exact historical truth;
- semantic versus operational state/completion;
- candidate/non-final versus authoritative Generation result;
- Criterion/Evaluation/Evidence question-method-finding separation;
- Evidence claim strength/applicability without approval/release/privacy takeover;
- Provenance relationship authority without source-fact takeover;
- recovery authority continuity and explicit unresolved state;
- provider facts only at actual evidentiary strength;
- material approximation as explicit and owner-scoped;
- decision-material qualifiers when they affect immediate semantic decisions;
- future rediscovery before architecture for new independent product purposes.

## Phase 013 sequence

```text
013-A  reconciliation authority / corpus inventory / precedence / discrepancy taxonomy  COMPLETE
013-B  representation / layering / public contract / identity / views                   NEXT
013-C  persistence / history / transaction-concurrency / migration
013-D  distributed data / topology / manifest / candidate-seal-promotion
013-E  Strategy/runtime / dependency / security / offline-no-egress
013-F  Execution / Attempt / recovery / fencing / admission
013-G  Evaluation / Evidence / Provenance / history / disclosure
013-H  deployment / scale / observability / portability / platform integration
013-I  cross-architecture / ADR / legacy / M6 / residual register
013-J  consolidation / R1 decision / Phase 014 handoff
```

## M6 explicit reconciliation item

Current Phase 009 authority controls:

```text
historical IDs                 15
active synchronizations        13
SYNC-08                        retired — Generation-local behavior
SYNC-15                        reclassified — Reproducibility contract
```

Phase 013 must remove current ambiguity without reopening synchronization semantics merely to preserve old architecture language.

## M8 exclusion

Formal composable privacy/accounting, product-owned governance/release, independent output publication/versioning, reusable request/cohort lifecycles, independently governed graph relationships, durable streaming/session/feed lifecycle, product-owned resource/economic accounting and product-owned reusable knowledge/memory remain future rediscovery triggers.

They are not architecture reservations.

## Implementation boundary

Phase 013 remains design/reconciliation only.

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

No production implementation, migration, provider integration, package refactor or API stabilization is authorized.

## Current next boundary

**013-B — Representation Layering, Public Contract, Identity, Revision, Handle & View Reconciliation** is next eligible.
