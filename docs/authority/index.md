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
- [013-B Representation Phase Record](../phases/013/013-B-representation-layering-public-contract-identity-revision-handle-view-reconciliation.md)
- [013-B Representation Reconciliation Authority](../architecture/phase-013-b-representation-layering-public-contract-identity-view-reconciliation.md) — **current representation baseline**
- [Phase 013 Entry & Decomposition](../phases/013/013-entry-decomposition.md)
- [Representation & Architecture Index](../architecture/index.md)

Retained Phase 004/006/007 architecture remains downstream reconciliation material except where a completed Phase 013 subgroup has explicitly retained/clarified its current meaning.

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
013-B                                COMPLETE
013-C                                NEXT ELIGIBLE
R1 architecture reconciliation       DOWNSTREAM / IN PROGRESS
whole-design completion              NOT YET — PHASE 014
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## 013-A method result

013-A established the retained corpus inventory, precedence reset, AR-0..AR-9 taxonomy, AMAT-0..AMAT-3 materiality, canonical dispositions and residual-register contract. It declared no AMAT-2/AMAT-3 defect and no upstream reopen.

## 013-B representation result

```text
representation spine                 RETAINED WITH BOUNDED CLARIFICATION
AMAT-2 representation defects        0
AMAT-3 blockers                      0
AR-9 contradictions                  0
upstream reopen                      NONE
new concepts                         0
new synchronizations                 0
```

Current representation rules now explicitly preserve:

- architecture as representation of semantic authority rather than a second semantic owner;
- logical layering without mandatory package/service/API-tier mapping;
- package-first primary surfaces and optional CLI/report/graphical/service integrations;
- stable logical identity distinct from locator/provider identity;
- separate identity, semantic revision/commitment, current-state version/freshness and representation-schema version axes;
- exact historical binding alongside refreshable current views;
- handles/views as resolvers/projections rather than detached canonical entities;
- Execution ownership of retry/resume/reconcile/cancel operational state;
- owner-specific Learned State / Generation-output / Evidence establishment rather than a shared Result lifecycle;
- D0-D4 as semantic disclosure depth rather than architecture tiers.

Historical `007-D` synchronization-count wording and pre-Phase-013 representation precedence wording remain tracked for 013-I corpus cleanup, but current semantic ambiguity is removed.

## Durable current quality rules

Temporal integrity:

> **Later status, restriction, retirement, supersession or invalidation changes current/future reliance where owned; it does not silently rewrite exact historical bindings or transfer authority to another concept.**

Decision-material disclosure:

> **Progressive disclosure may defer explanatory depth, but it must not defer a qualifier whose omission could change the actor's immediate semantic decision or make current state appear stronger than the owning concept supports.**

Provider-evidence qualification:

> **A provider fact is consumed only at the evidentiary strength it actually establishes; provider vocabulary never automatically escalates into stronger SYNGAN semantics.**

Future rediscovery:

> **Genericity means accepting new instances within a stable purpose. Rediscover before implementation when future scope introduces an independent product-facing purpose with durable state/history and independently meaningful actions/lifecycle.**

## Residual state carried through Phase 013

```text
unresolved current conceptual defects         0
MAT-3 conceptual blockers                     0
resolved M1 quality-rule families             2
bounded M6 Phase-013 deferrals                1
M8 future-rediscovery finding groups          4
```

M6 historical synchronization wording remains a downstream architecture/documentation cleanup obligation. M8 triggers remain future design-governance gates, not architecture pre-approvals.

## Phase 013 boundary

Phase 013 continues to use:

```text
RETAIN
CLARIFY
SUPERSEDE
CORRECT
DEFER
UPSTREAM-REOPEN
```

Only a demonstrated AR-9 genuine semantic contradiction may justify upstream reopen.

Current dependency-safe sequence:

```text
013-A  authority / corpus inventory / precedence / discrepancy taxonomy  COMPLETE
013-B  representation / layering / public contract / identity / views   COMPLETE
013-C  persistence / history / transaction-concurrency / migration      NEXT
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

**013-C — Control Persistence, Historical Reference, Transaction/Concurrency, Migration & Recovery-State Reconciliation** is next eligible.
