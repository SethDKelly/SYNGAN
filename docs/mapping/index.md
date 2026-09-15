---
type: Concept Mapping Index
title: SYNGAN Concept Mapping, Interaction & Linguistic Design
status: active
---

# SYNGAN Concept Mapping, Interaction & Linguistic Design

## Purpose

This directory contains current Jackson-style concept mapping authority for SYNGAN.

Concept mapping translates accepted concept actions, state, queries, history and composition into actor-visible and programmatic interaction semantics. It is downstream of concept/dependence/composition authority and upstream of representation/architecture.

A mapping describes what actors/programmatic consumers must be able to do, see, distinguish, inspect or understand. It does not by itself select classes, endpoints, commands, widgets, schemas, services, packages, storage or runtime mechanisms.

## Current phase

```text
Phase 009                    COMPLETE
Phase 010                    ACTIVE
Phase 010 decomposition      COMPLETE
010-A                        COMPLETE
010-B                        COMPLETE
010-C                        COMPLETE
010-D                        COMPLETE
010-E                        NEXT ELIGIBLE
F1                           CURRENTLY CLOSED
F2                           CURRENTLY CLOSED
F3                           CURRENTLY CLOSED
F4                           PARTIAL
F5                           STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
Jackson concept design       NOT COMPLETE
implementation readiness     NOT READY
implementation start         NOT STARTED
implementation next          NOT YET
```

## Current mapping authority

- [Mapping Authority, Coverage Model, Actor/Surface Taxonomy & Evidence Baseline](mapping-authority-coverage-actor-surface-evidence-baseline.md) — 010-A control authority.
- [Concept Action → Actor Intent & Interaction Mapping](concept-action-actor-intent-interaction-mapping.md) — 010-B semantic action authority.
- [Concept State, Query, History & Explanation → Inspection Mapping](concept-state-query-history-explanation-inspection-mapping.md) — 010-C semantic inspection authority.
- [Linguistic Mapping, Vocabulary, Typed Status & Disclosure Semantics](linguistic-mapping-vocabulary-typed-status-disclosure-semantics.md) — **010-D current linguistic authority**.
- [Phase 010 Entry & Decomposition](../phases/010/010-entry-decomposition.md)
- [Phase 009 Consolidation](../authority/phase-009-dependence-composition-consolidation.md)
- [Accepted Concept Catalog](../concepts/index.md)
- [Actors & Needs](../problem/actors.md)
- [Domain Terminology](../terminology/index.md)
- Phase 003/006 experience documents — retained mapping evidence.

## Current semantic mapping coverage

```text
normalized command groups               66 / 66 SEMANTICALLY MAPPED
normalized query groups                 52 / 52 SEMANTICALLY MAPPED
lifecycle/history envelopes             11 / 11 SEMANTICALLY MAPPED
cross-concept explanation patterns       5
accepted concept names                  11 / 11 LINGUISTICALLY ALIGNED
mapping blockers                         0
```

F1, F2 and F3 are currently closed at their Phase 010 layers, subject to final 010-H revalidation.

## Inspection authority

> **Inspection exposes owned or validly derived truth; it does not create a second owner for that truth.**

Combined dashboards/reports/history/explanations may compose facts from multiple concepts, but each fact remains attributable to its canonical owner.

Current and historical truth remain simultaneously representable. Semantic and operational state remain orthogonal. Candidate/intermediate material remains visibly non-final. Evidence claim strength and Provenance relationship authority remain explicit.

## Linguistic authority

> **Words may simplify presentation, but they may not erase ownership, semantic dimension, historical scope, uncertainty or disclosure meaning.**

SYNGAN therefore has no universal status state machine. Linguistic mapping keeps distinct:

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

Owner-qualified wording is required where ambiguity matters, for example:

```text
Generation completed
Execution completed operationally
Evaluation completed
Generation compatibility: indeterminate
Constraint handling: validated later
Evidence finding: violated
```

## Disclosure and history quality

Current disclosure meanings are:

```text
visible
authorized summary / redacted
withheld
unavailable
unknown
absent
```

`not applicable` is separate from absence.

Historical-knowledge quality is expressed as:

```text
directly retained
reconstructed
partial / incomplete
history unavailable
history indeterminate
```

Disclosure and history quality are orthogonal dimensions.

## Vocabulary-risk discipline

High-risk terms such as `model`, `run`, `job`, `artifact`, `metric`, `metadata`, `validation`, `valid`, `passed`, `quality`, `safe`, `private`, `reproducible`, `current`, `latest` and `complete` require qualification when ambiguity affects meaning.

Compatibility words such as `fit`, `train`, `sample` and `synthesizer` may be used later only when their mapping to canonical SYNGAN semantics is explicit.

No global Status, Validation, Quality, Approval, History, Artifact, Run or Lineage authority is introduced.

## Enterprise-scale boundedness

Routine inspection remains metadata/reference/summary-first. Bulk data, detailed telemetry, large Evidence support material and Provenance traversal remain separately bounded rather than becoming ordinary driver-local inspection state.

## Application-family preservation

Optional concepts do not appear as mandatory empty workflow steps. Direct Generation does not fabricate Learning/Learned State; Execution and Provenance surfaces appear only when those capabilities actually belong to the selected application family.

## Coverage progression

```text
actions                     SEMANTICALLY MAPPED
queries/observations        SEMANTICALLY MAPPED
lifecycle/history envelopes SEMANTICALLY MAPPED
explanation patterns        SEMANTICALLY MAPPED
vocabulary/status/disclosure LINGUISTICALLY ALIGNED
```

Still pending:

```text
PHYSICAL / INTERACTION SURFACE MAPPING
APPLICATION-FAMILY WORKFLOW REPLAY
DIFFICULT-CONDITION HUMAN/PROGRAMMATIC PARITY VALIDATION
PHASE 010 CONSOLIDATION
```

## Phase 010 sequence

```text
010-A  COMPLETE — mapping authority / coverage / actor-surface taxonomy / evidence baseline
010-B  COMPLETE — concept action -> actor intent / interaction mapping
010-C  COMPLETE — state/query/history/explanation -> inspection mapping
010-D  COMPLETE — linguistic / vocabulary / typed status / disclosure semantics
010-E  NEXT — physical / interaction surface mapping
010-F  application-family workflow composition / progressive disclosure
010-G  human-programmatic parity / degraded-recovery-scale misfit audit
010-H  consolidation / Phase 011 handoff
```

## Current next boundary

**010-E — Physical / Interaction Mapping Across SDK, Notebook, CLI, API, Report, UI & Operator Surfaces** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
