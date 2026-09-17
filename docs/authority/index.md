---
type: Authority Index
title: SYNGAN Design Authority
status: active
---

# SYNGAN Design Authority

These documents define how SYNGAN design knowledge is created, interpreted, changed, reconciled downstream, and eventually implemented.

## Current methodology and governance

- [Concept Design Methodology](design-methodology.md)
- [Jackson Design Completion & Implementation Hold](jackson-design-completion-implementation-hold.md)
- [Jackson Methodology Completion Matrix](jackson-methodology-completion-matrix.md)
- [Documentation Governance](documentation-governance.md)
- [Terminology Policy](terminology-policy.md)
- [Source & Provenance Policy](source-provenance-policy.md)

## Completed concept-design authority

- [Phase 009 Dependence / Composition Consolidation](phase-009-dependence-composition-consolidation.md)
- [Phase 010 Concept Mapping Consolidation](phase-010-concept-mapping-consolidation.md)
- [Phase 011 Design Quality / Misfit Consolidation](phase-011-design-quality-misfit-consolidation.md)
- [Residual Conceptual Misfit Register](residual-conceptual-misfit-register.md)
- [Phase 012 Jackson Concept-Design Consolidation](phase-012-jackson-concept-design-consolidation.md) — **current Jackson completion authority**

## Active Phase 013 architecture-reconciliation authority

- [Phase 013 Architecture Reconciliation Authority](phase-013-architecture-reconciliation-authority.md) — **current Phase 013 method authority**
- [Phase 013 Index](../phases/013/index.md)
- [013-A Reconciliation Authority / Corpus Inventory / Taxonomy](../phases/013/013-A-reconciliation-authority-retained-corpus-inventory-precedence-reset-discrepancy-taxonomy.md)
- [Phase 013 Entry & Decomposition](../phases/013/013-entry-decomposition.md)
- [Representation & Architecture Index](../architecture/index.md)

Retained Phase 004/006/007 architecture remains downstream reconciliation material until Phase 013 explicitly retains, clarifies, supersedes, corrects, defers, or reopens the relevant authority.

## Current posture

```text
accepted concepts                    11
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
Phase 010                            COMPLETE
Phase 011                            COMPLETE
Phase 012                            COMPLETE
A1-H2                                CURRENTLY CLOSED
Jackson concept design               COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013                            ACTIVE
013-A                                COMPLETE
013-B                                NEXT ELIGIBLE
R1 architecture reconciliation       DOWNSTREAM / IN PROGRESS
whole-design completion              NOT YET — PHASE 014
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## 013-A method result

```text
retained substantive architecture docs   19
retained ADRs                             10
AR-0..AR-9 discrepancy taxonomy           ESTABLISHED
AMAT-0..AMAT-3 materiality                ESTABLISHED
canonical dispositions                    ESTABLISHED
known entry candidates                     6
AMAT-2 defects declared by 013-A           0
AMAT-3 blockers declared by 013-A          0
upstream reopen                           NONE
```

The six entry candidates cover historical synchronization count/ID drift, retained precedence wording and superseded implementation-reentry assumptions. Later groups determine whether any deeper material architecture defect exists.

## Durable current quality rules

Temporal integrity:

> **Later status, restriction, retirement, supersession or invalidation changes current/future reliance where owned; it does not silently rewrite exact historical bindings or transfer authority to another concept.**

Decision-material disclosure:

> **Progressive disclosure may defer explanatory depth, but it must not defer a qualifier whose omission could change the actor's immediate semantic decision or make current state appear stronger than the owning concept supports.**

Provider-evidence qualification:

> **A provider fact is consumed only at the evidentiary strength it actually establishes; provider vocabulary never automatically escalates into stronger SYNGAN semantics.**

Future rediscovery:

> **Genericity means accepting new instances within a stable purpose. Rediscover before implementation when future scope introduces an independent product-facing purpose with durable state/history and independently meaningful actions/lifecycle.**

## Residual state carried into Phase 013

```text
unresolved current conceptual defects         0
MAT-3 conceptual blockers                     0
resolved M1 quality-rule families             2
bounded M6 Phase-013 deferrals                1
M8 future-rediscovery finding groups          4
```

The M6 item includes historical `11 / 15` synchronization assumptions and older `SYNC-08` / `SYNC-15` roles in retained Phase 006/007 architecture material. Current Phase 009 synchronization semantics are authoritative; Phase 013 owns reconciliation.

M8 triggers remain conditional future design-governance gates, not architecture pre-approvals.

## Phase 013 boundary

Completed concept design is upstream authority for representation/architecture reconciliation.

Phase 013 uses the canonical dispositions:

```text
RETAIN
CLARIFY
SUPERSEDE
CORRECT
DEFER
UPSTREAM-REOPEN
```

Only a demonstrated AR-9 genuine semantic contradiction may justify upstream reopen. Historical architecture convenience, provider preference, implementation cost or existing code shape cannot.

Current dependency-safe sequence:

```text
013-A  authority / corpus inventory / precedence / discrepancy taxonomy  COMPLETE
013-B  representation / layering / public contract / identity / views   NEXT
013-C  persistence / history / transaction-concurrency / migration
013-D  distributed data / topology / manifest / candidate-seal-promotion
013-E  Strategy/runtime / dependency / security / offline-no-egress
013-F  Execution / Attempt / recovery / fencing / admission
013-G  Evaluation / Evidence / Provenance / history / disclosure
013-H  deployment / scale / observability / portability / platform integration
013-I  cross-architecture / ADR / legacy / M6 / residual register
013-J  consolidation / R1 decision / Phase 014 handoff
```

Only 013-J may close R1.

## Remaining design sequence

```text
013    Post-Concept Representation & Architecture Reconciliation — ACTIVE
014    Whole-Design Consolidation & Implementation-Readiness Decision
---
015    Implementation Authority & Controlled Delivery — FUTURE ONLY
```

Only Phase 014 may set implementation **READY / NOT STARTED / NEXT**; Phase 015 is still required to begin implementation.

## Current next boundary

**013-B — Representation Layering, Public Contract, Identity, Revision, Handle & View Reconciliation** is next eligible.
