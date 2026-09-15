---
type: Concept Mapping Index
title: SYNGAN Concept Mapping, Interaction & Linguistic Design
status: active
---

# SYNGAN Concept Mapping, Interaction & Linguistic Design

## Purpose

This directory contains current Jackson-style concept mapping authority for SYNGAN.

Concept mapping translates accepted concept actions, state, queries, history and composition into actor-visible and programmatic interaction semantics. It is downstream of concept/dependence/composition authority and upstream of representation/architecture.

A mapping describes what actors/programmatic consumers must be able to do, see, distinguish, inspect or understand. It does not by itself select classes, methods, endpoints, widgets, schemas, services, packages, storage or runtime mechanisms.

## Current phase

```text
Phase 009                    COMPLETE
Phase 010                    ACTIVE
010-A                        COMPLETE
010-B                        COMPLETE
010-C                        COMPLETE
010-D                        COMPLETE
010-E                        COMPLETE
010-F                        NEXT ELIGIBLE
F1                           CURRENTLY CLOSED
F2                           CURRENTLY CLOSED
F3                           CURRENTLY CLOSED
F4                           PARTIAL TO STRONG
F5                           STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
Jackson concept design       NOT COMPLETE
implementation readiness     NOT READY
implementation start         NOT STARTED
implementation next          NOT YET
```

## Current mapping authority

- [010-A Mapping Control](mapping-authority-coverage-actor-surface-evidence-baseline.md)
- [010-B Concept Action → Actor Intent & Interaction Mapping](concept-action-actor-intent-interaction-mapping.md)
- [010-C Concept State, Query, History & Explanation → Inspection Mapping](concept-state-query-history-explanation-inspection-mapping.md)
- [010-D Linguistic Mapping, Vocabulary, Typed Status & Disclosure Semantics](linguistic-mapping-vocabulary-typed-status-disclosure-semantics.md)
- [010-E Package, Notebook, Automation, Host-Platform & Optional Presentation Interaction Mapping](package-notebook-automation-host-platform-interaction-mapping.md) — **current physical/surface responsibility authority**

## Current mapping coverage

```text
66 / 66 command groups                    SEMANTICALLY MAPPED
52 / 52 query groups                      SEMANTICALLY MAPPED
11 / 11 lifecycle/history envelopes       SEMANTICALLY MAPPED
5 explanation patterns                    SEMANTICALLY MAPPED
11 / 11 accepted concept names            LINGUISTICALLY ALIGNED
66 / 66 command groups                    PHYSICAL RESPONSIBILITY MAPPED
52 / 52 query groups                      PHYSICAL RESPONSIBILITY MAPPED
```

## Core mapping rules

> **Inspection exposes owned or validly derived truth; it does not create a second owner for that truth.**

> **Words may simplify presentation, but they may not erase ownership, semantic dimension, historical scope, uncertainty or disclosure meaning.**

> **Physical interaction may adapt to the host, but it may not redefine SYNGAN semantics.**

## Product form

SYNGAN is a deployable Python/Spark framework package.

Its current product-form rule is:

> **SYNGAN is agnostic across compliant Spark-capable hosting and infrastructure platforms.**

010-E therefore resolves the interaction hierarchy as:

```text
P1  Python package / SDK contract              PRIMARY / REQUIRED
P2  notebook / interactive package use        PRIMARY HUMAN-PROGRAMMATIC HOST
P3  embedded job / pipeline / automation      PRIMARY PROGRAMMATIC HOST
P4  CLI adapter                               OPTIONAL
P5  report / exported review                  OPTIONAL
P6  rich / graphical presentation             OPTIONAL HOST/COMPANION PRESENTATION
P7  host-platform / operator integration      HOST INTEGRATION RESPONSIBILITY
P8  external integration / handoff            EXTERNAL BOUNDARY
```

The earlier 010-A S1-S7 taxonomy remains candidate-surface evidence, not a requirement to ship seven peer interfaces.

`API` means the programmatic package contract by default. A network service/API is optional. A standalone graphical application is not required. Host platforms ordinarily own authentication shells, job/cluster administration, detailed telemetry, storage browsing and infrastructure UI.

## Typed linguistic dimensions

SYNGAN keeps distinct:

```text
revision/current-use status
semantic activity lifecycle
contextual assessment
Execution/Attempt operational lifecycle
Generation material finality
Evidence finding / claim strength
Constraint handling / applicability
Disclosure state
historical-knowledge quality
```

No global Status, Validation, Quality, Approval, History, Artifact, Run or Lineage authority is introduced.

## Enterprise-scale boundedness

Routine interaction remains reference/summary-first. Bulk source/output data, Learned State payloads, detailed diagnostics and other large material remain distributed or separately referenced where scale requires it.

Notebook/report/UI convenience may not introduce a mandatory driver-local materialization boundary.

## Application-family preservation

Optional concepts do not appear as mandatory empty workflow steps. Direct Generation does not fabricate Learning/Learned State. Execution and Provenance interaction appears only when those capabilities exist.

010-F now owns full workflow replay and progressive disclosure across the actual Phase 009 application family.

## Phase 010 sequence

```text
010-A  COMPLETE — mapping authority / coverage / actor-surface taxonomy / evidence baseline
010-B  COMPLETE — concept action -> actor intent / interaction mapping
010-C  COMPLETE — state/query/history/explanation -> inspection mapping
010-D  COMPLETE — linguistic / vocabulary / typed status / disclosure semantics
010-E  COMPLETE — package/notebook/automation/host physical interaction mapping
010-F  NEXT — application-family workflow composition / progressive disclosure
010-G  human-programmatic parity / degraded-recovery-scale mapping misfit
010-H  consolidation / Phase 011 handoff
```

## Current next boundary

**010-F — Application-Family Workflow Composition, Optional-Capability Experience & Progressive Disclosure** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
