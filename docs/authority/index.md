---
type: Authority Index
title: SYNGAN Design Authority
status: active
---

# SYNGAN Design Authority

These documents define how SYNGAN design knowledge is created, interpreted, changed, and eventually implemented.

## Current methodology and governance

- [Concept Design Methodology](design-methodology.md)
- [Jackson Design Completion & Implementation Hold](jackson-design-completion-implementation-hold.md)
- [Jackson Methodology Completion Matrix](jackson-methodology-completion-matrix.md)
- [Phase 009 Dependence, Application Family & Composition Consolidation](phase-009-dependence-composition-consolidation.md)
- [Documentation Governance](documentation-governance.md)
- [Terminology Policy](terminology-policy.md)
- [Source & Provenance Policy](source-provenance-policy.md)

## Current design authority chain

- [Problem Knowledge](../problem/index.md)
- [Accepted Concept Catalog](../concepts/index.md)
- [Phase 008 Individual-Concept Design Consolidation](../concepts/phase-008-individual-concept-consolidation.md)
- [Concept Dependence & Application Family](../dependence/index.md)
- [Synchronization Authority](../synchronizations/index.md)
- [Phase 009 Consolidation](phase-009-dependence-composition-consolidation.md)
- [Concept Mapping Authority](../mapping/index.md)
- [010-A Mapping Control Authority](../mapping/mapping-authority-coverage-actor-surface-evidence-baseline.md)
- [Phase 010](../phases/010/index.md)

## Current posture

```text
accepted concepts                    11
current desired outcomes             16
historical synchronization IDs       15
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
D1-D4                                CURRENTLY CLOSED
E1-E5                                CURRENTLY CLOSED
Phase 010                            ACTIVE
010-A                                COMPLETE
010-B                                NEXT ELIGIBLE
F1                                   PARTIAL
F2                                   PARTIAL
F3                                   PARTIAL TO STRONG
F4                                   PARTIAL
F5                                   STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Phase 010 mapping control

010-A now defines what every later mapping must account for before a mapping can advance toward closure.

Current control model:

```text
actor roles                             7
surface families                        7
application-family applicability tags  10
coverage dimensions                    12
canonical mapping fields               19
```

Every later mapping must preserve, where material:

- canonical concept ownership;
- actor intent/need;
- surface-neutral interaction or inspection obligation;
- precondition/result/non-success semantics;
- application-family conditionality;
- synchronization relevance without synchronization-owned state;
- temporal orientation;
- typed disclosure/history-quality state;
- enterprise-scale boundedness;
- candidate surface families and vocabulary risk;
- evidence traceability and explicit misfit/reopen status.

Current documentation coverage progression:

```text
SOURCE IDENTIFIED
  -> SEMANTICALLY MAPPED
  -> LINGUISTICALLY ALIGNED
  -> SURFACE-MAPPED
  -> FAMILY-REPLAYED
  -> PARITY-VALIDATED
```

A material mapping may instead become `BLOCKED BY MISFIT`, triggering the smallest appropriate reopen.

## Evidence baseline

Phase 003/006 experience evidence remains strong but is no longer automatically current mapping authority.

010-A preserves the semantic/operational, candidate/final, Evidence/decision, historical/current, disclosure/history-quality, recovery and scale distinctions while normalizing stale assumptions:

```text
15 historical SYNC IDs != 15 active rules
SYNC-08 retired
SYNC-15 reclassified
Learning not universal for Generation
Evaluation/Evidence not universal for Generation
Execution not universal
Provenance not universal
Readiness/Validation not global owners
```

## Architecture boundary

The [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md) remains downstream evidence pending Phase 013 reconciliation.

Concept mapping may identify interaction obligations and candidate surface families but does not prescribe imports, concrete APIs, widgets, events, transactions, queues, schemas, services, packages, deployment topology, runtime orchestration, or observer/subscription mechanisms.

## Remaining design sequence

```text
010-B  concept action -> actor intent / interaction mapping
010-C  state/query/history -> inspection mapping
010-D  linguistic / vocabulary / typed status / disclosure semantics
010-E  physical interaction mapping
010-F  application-family workflow composition / progressive disclosure
010-G  human-programmatic parity / difficult-condition mapping misfit
010-H  mapping consolidation / Phase 011 handoff
011    final concept-design quality / misfit
012    Jackson concept-design completion decision
013    representation / architecture reconciliation
014    whole-design completion / implementation-readiness decision
```

## Implementation-readiness rule

Only Phase 014 may set **READY / NOT STARTED / NEXT** after the whole design passes. Phase 015 is still required before implementation begins.

## Current next boundary

**010-B — Concept Action → Actor Intent & Interaction Mapping** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
