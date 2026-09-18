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
- [Operational Authority Continuity & Regressive Recovery Contract](operational-authority-continuity-regressive-recovery-contract.md) — reconciled to current synchronization authority in 013-C
- [Phase 013 Index](../phases/013/index.md)
- [013-B Representation Reconciliation](../architecture/phase-013-b-representation-layering-public-contract-identity-view-reconciliation.md) — current representation baseline
- [013-C Persistence Reconciliation](../architecture/phase-013-c-control-persistence-history-concurrency-migration-recovery-reconciliation.md) — current control-persistence baseline
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
013-C                                COMPLETE
013-D                                NEXT ELIGIBLE
R1 architecture reconciliation       DOWNSTREAM / IN PROGRESS
whole-design completion              NOT YET — PHASE 014
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Phase 013 results through 013-C

013-A established the retained-corpus inventory, precedence reset, AR-0..AR-9 taxonomy, AMAT-0..AMAT-3 materiality, canonical dispositions and residual-register contract.

013-B retained the representation spine with bounded clarification and found **0 AMAT-2, 0 AMAT-3, 0 AR-9, no upstream reopen**.

013-C retained the control-persistence/history/concurrency/migration/recovery spine with bounded clarification and found **0 AMAT-2, 0 AMAT-3, 0 AR-9, no upstream reopen**.

Current persistence rules include:

- storage makes owner-established authority durable rather than creating authority;
- cross-owner atomic co-commit does not merge ownership;
- durable coordination intent does not become synchronization-owned state;
- CAS/state versions do not replace semantic validation or non-regressing recovery authority;
- exact historical references do not silently resolve to current/latest values;
- reconstruction remains qualified by evidence strength;
- migration changes representation by default;
- regressive restore requires fresh recovery authority before ordinary writes resume;
- control persistence remains bounded/reference-first at Spark scale.

The active recovery contract now reflects current Phase 009 semantics: historical `SYNC-15` is reserved/reclassified, not active.

Historical 007-D/007-E synchronization-count wording remains tracked for 013-I corpus cleanup.

## Durable current quality rules

Temporal integrity:

> **Later status, restriction, retirement, supersession or invalidation changes current/future reliance where owned; it does not silently rewrite exact historical bindings or transfer authority to another concept.**

Provider-evidence qualification:

> **A provider fact is consumed only at the evidentiary strength it actually establishes; provider vocabulary never automatically escalates into stronger SYNGAN semantics.**

Future rediscovery:

> **Rediscover before architecture/implementation when future scope introduces an independent product-facing purpose with durable state/history and independently meaningful actions/lifecycle.**

## Phase 013 boundary

Phase 013 uses `RETAIN / CLARIFY / SUPERSEDE / CORRECT / DEFER / UPSTREAM-REOPEN`. Only a demonstrated AR-9 contradiction may justify upstream reopen, and only 013-J may close R1.

Current dependency-safe sequence:

```text
013-A  authority / corpus inventory / precedence / taxonomy                    COMPLETE
013-B  representation / layering / public contract / identity / views          COMPLETE
013-C  persistence / history / concurrency / migration / recovery              COMPLETE
013-D  distributed data / topology / manifest / candidate-seal-promotion       NEXT
013-E  Strategy/runtime / dependency / security / offline-no-egress
013-F  Execution / Attempt / recovery / fencing / admission
013-G  Evaluation / Evidence / Provenance / history / disclosure
013-H  deployment / scale / observability / portability / platform integration
013-I  cross-architecture / ADR / legacy / M6 / residual register
013-J  consolidation / R1 decision / Phase 014 handoff
```

## Remaining design sequence

```text
013    Post-Concept Representation & Architecture Reconciliation — ACTIVE
014    Whole-Design Consolidation & Implementation-Readiness Decision
---
015    Implementation Authority & Controlled Delivery — FUTURE ONLY
```

Only Phase 014 may set implementation **READY / NOT STARTED / NEXT**; Phase 015 is still required to begin implementation.

## Current next boundary

**013-D — Distributed Data Boundary, Structured Topology, Manifest, Candidate/Seal/Promotion & Large-State Reconciliation** is next eligible.
