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
- [010-B Concept Action Mapping](../mapping/concept-action-actor-intent-interaction-mapping.md)
- [010-C Inspection Mapping](../mapping/concept-state-query-history-explanation-inspection-mapping.md)
- [Phase 010](../phases/010/index.md)

## Current posture

```text
accepted concepts                    11
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
D1-D4                                CURRENTLY CLOSED
E1-E5                                CURRENTLY CLOSED
Phase 010                            ACTIVE
010-A                                COMPLETE
010-B                                COMPLETE
010-C                                COMPLETE
010-D                                NEXT ELIGIBLE
F1                                   CURRENTLY CLOSED
F2                                   CURRENTLY CLOSED
F3                                   PARTIAL TO STRONG
F4                                   PARTIAL
F5                                   STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Current mapping authority

010-A defines record schema, coverage, actors/surfaces, family applicability and evidence rules.

010-B supplies complete semantic action mapping:

```text
66 / 66 normalized command groups  SEMANTICALLY MAPPED
```

010-C supplies complete semantic inspection mapping:

```text
52 / 52 normalized query groups        SEMANTICALLY MAPPED
11 / 11 lifecycle/history envelopes    SEMANTICALLY MAPPED
5 cross-concept explanation patterns   SEMANTICALLY MAPPED
```

The 010-C inspection rule is:

> **Inspection exposes owned or validly derived truth; it does not create a second owner for that truth.**

Accordingly, current mapping preserves current versus exact historical truth, semantic versus operational state, candidate versus authoritative result, Evidence interpretation context, Provenance/source-fact boundaries, typed disclosure/history-quality distinctions and enterprise-scale boundedness without introducing a new Dashboard/Status/History/Explanation/Lineage owner.

## Architecture boundary

The [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md) remains downstream evidence pending Phase 013 reconciliation.

Neither action mappings nor inspection mappings prescribe concrete APIs, classes, widgets, reports, database/materialized views, graph/search technologies, caches, schemas, events, transactions, services, packages, queues or deployment topology.

010-C categories such as reconstructed/partial/withheld/unknown are semantic mapping distinctions pending linguistic alignment, not public/runtime enum authority.

## Remaining design sequence

```text
010-D  linguistic / vocabulary / typed status / disclosure semantics — NEXT
010-E  physical interaction mapping
010-F  application-family workflow replay
010-G  parity / degraded / recovery / scale misfit audit
010-H  Phase 010 consolidation
011    final concept-design quality / misfit
012    Jackson concept-design completion decision
013    representation / architecture reconciliation
014    whole-design completion / implementation-readiness decision
```

## Implementation-readiness rule

Only Phase 014 may set **READY / NOT STARTED / NEXT** after the whole design passes. Phase 015 is still required before implementation begins.

## Current next boundary

**010-D — Linguistic Mapping, Vocabulary, Typed Status & Disclosure Semantics** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
