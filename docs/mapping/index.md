---
type: Concept Mapping Index
title: SYNGAN Concept Mapping, Interaction & Linguistic Design
status: active
---

# SYNGAN Concept Mapping, Interaction & Linguistic Design

## Purpose

This directory contains current Jackson-style concept mapping authority for SYNGAN.

Concept mapping translates accepted concept actions, state, queries, history and composition into actor-visible and programmatic interaction semantics. It is downstream of concept/dependence/composition authority and upstream of representation/architecture.

A mapping may describe what an actor must be able to do, see, distinguish, inspect or understand. It does not by itself select classes, endpoints, commands, widgets, schemas, services, packages, storage or runtime mechanisms.

## Current phase

```text
Phase 009                    COMPLETE
Phase 010                    ACTIVE
Phase 010 decomposition      COMPLETE
010-A                        NEXT ELIGIBLE
F1                           PARTIAL
F2                           PARTIAL
F3                           PARTIAL TO STRONG
F4                           PARTIAL
F5                           STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
Jackson concept design       NOT COMPLETE
implementation readiness     NOT READY
implementation start         NOT STARTED
implementation next          NOT YET
```

## Current governing inputs

- [Concept Design Methodology](../authority/design-methodology.md)
- [Phase 009 Dependence, Application Family & Composition Consolidation](../authority/phase-009-dependence-composition-consolidation.md)
- [Accepted Concept Catalog](../concepts/index.md)
- [Current Synchronization Authority](../synchronizations/index.md)
- [Actors & Needs](../problem/actors.md)
- [Domain Terminology](../terminology/index.md)
- [Phase 003 Consolidated Experience Contract](../experience/phase-003-consolidated-experience-contract.md)
- [Phase 006 Recovery/Security/Degraded/History/Topology Experience Contract](../experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md)
- [Phase 010 Entry & Decomposition](../phases/010/010-entry-decomposition.md)

## Mapping discipline

Current mapping work must proceed in three layers:

```text
1. surface-neutral semantic mapping
   concept action/state/query -> actor intent / inspection obligation

2. linguistic mapping
   concept meaning -> actor/programmatic vocabulary and typed status language

3. physical/interaction mapping
   semantic mapping -> candidate SDK/notebook/CLI/API/report/UI/operator interaction
```

Only after those layers exist may Phase 010 evaluate application-family workflow composition and human/programmatic semantic parity.

## Surface families

Phase 010 may reason about these surface families without choosing their implementation:

- SDK/API automation;
- notebook-oriented interaction;
- CLI/operational interaction;
- reports/history/review artifacts;
- graphical UI where useful;
- operator/admin interaction;
- external integration/handoff where current scope requires it.

These categories are mapping lenses, not mandatory product editions or architecture components.

## Upstream invariants mapping must preserve

1. the eleven accepted concepts remain distinct;
2. application-family subsets remain honest and optional capabilities remain optional;
3. synchronization is relation/occurrence-scoped rather than permanent reactive subscription;
4. synchronization owns no canonical state;
5. exact bindings remain historical and inspectable;
6. semantic and operational completion remain distinct;
7. physical existence does not imply semantic result authority;
8. Evidence remains finding authority, not approval/release authority;
9. Provenance remains relationship authority, not source-fact authority;
10. current status and historical bound status may legitimately differ;
11. disclosure and historical-knowledge states remain typed where material;
12. mapping must remain viable at enterprise scale without ordinary full local materialization.

## Retained experience evidence

Phase 003 and Phase 006 contain substantial workflow evidence, but Phase 010 must replay that evidence against the normalized Phase 008 concept model and completed Phase 009 application-family/composition model.

Historical workflow documents therefore remain supporting evidence rather than automatically complete F1-F5 mapping authority.

## Misfit rule

If an accepted concept/action/query cannot be mapped intelligibly without violating its purpose, ownership, application-family or synchronization semantics, Phase 010 must record a real mapping misfit and reopen the smallest affected upstream authority under the J0-J7 discipline.

It must not solve the problem by inventing a generic `Run`, `Artifact`, `Metric`, `Validation`, `Quality`, `Workflow`, `History` or `Approval` authority unless fresh concept discovery independently justifies one.

## Phase 010 sequence

```text
010-A  NEXT — mapping authority / coverage / actor-surface taxonomy
010-B  action -> interaction mapping
010-C  state/query/history -> inspection mapping
010-D  linguistic / vocabulary / typed status mapping
010-E  physical / interaction surface mapping
010-F  application-family workflow composition / progressive disclosure
010-G  human-programmatic parity / degraded-recovery-scale misfit audit
010-H  consolidation / Phase 011 handoff
```

## Current next boundary

**010-A — Mapping Authority, Coverage Model, Actor/Surface Taxonomy & Evidence Baseline** is next eligible.