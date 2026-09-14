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
010-C                        NEXT ELIGIBLE
F1                           CURRENTLY CLOSED FOR SEMANTIC ACTION MAPPING
F2                           PARTIAL
F3                           PARTIAL TO STRONG
F4                           PARTIAL
F5                           STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
Jackson concept design       NOT COMPLETE
implementation readiness     NOT READY
implementation start         NOT STARTED
implementation next          NOT YET
```

## Current mapping authority

- [Mapping Authority, Coverage Model, Actor/Surface Taxonomy & Evidence Baseline](mapping-authority-coverage-actor-surface-evidence-baseline.md) — 010-A control authority.
- [Concept Action → Actor Intent & Interaction Mapping](concept-action-actor-intent-interaction-mapping.md) — **010-B current semantic action-mapping authority**.
- [Phase 010 Entry & Decomposition](../phases/010/010-entry-decomposition.md)
- [Phase 009 Consolidation](../authority/phase-009-dependence-composition-consolidation.md)
- [Accepted Concept Catalog](../concepts/index.md)
- [Actors & Needs](../problem/actors.md)
- [Domain Terminology](../terminology/index.md)
- Phase 003/006 experience documents — retained mapping evidence.

## 010-A control model

010-A established:

```text
accepted concepts                       11
actor roles adopted                      7
surface families adopted                 7
application-family applicability tags   10
mapping coverage dimensions             12
canonical mapping fields                19
Phase 003/006 evidence baseline         ESTABLISHED
```

Controlled mapping states remain:

```text
SOURCE IDENTIFIED
SEMANTICALLY MAPPED
LINGUISTICALLY ALIGNED
SURFACE-MAPPED
FAMILY-REPLAYED
PARITY-VALIDATED
BLOCKED BY MISFIT
```

These are documentation coverage states, not runtime/domain states.

## 010-B action mapping result

010-B maps all normalized command groups from Phase 008-D:

```text
Data Meaning             7 / 7
Synthesis Strategy       4 / 4
Learning                 8 / 8
Learned State            4 / 4
Generation              11 / 11
Constraint               4 / 4
Evaluation Criterion     4 / 4
Evaluation               8 / 8
Evidence                 3 / 3
Execution                11 / 11
Provenance               2 / 2
                         ------
TOTAL                    66 / 66  SEMANTICALLY MAPPED
```

F1 therefore has current surface-neutral semantic action coverage across the whole accepted catalog.

This does **not** mean every conceptual command becomes a direct user control. System-established/synchronized transitions such as `LearnedState.Establish`, `Evidence.Establish`, `Execution.RecordAttemptOutcome`, and `Provenance.RecordTypedRelationship` may be observable without having a dedicated button/endpoint.

## Action-mapping invariants

Current action mapping preserves:

- semantic commitment versus operational start;
- cancellation request versus terminal cancellation;
- Attempt outcome versus parent semantic outcome;
- candidate output versus completed Generation output;
- Evaluation completion versus favorable Evidence;
- Evidence versus approval/release/privacy guarantee;
- reusable-authority effectiveness versus consumer compatibility;
- future-use status versus historical bound truth;
- Provenance relationship assertions versus source facts;
- activity-owned validation/readiness rather than global mutable readiness.

No global Workflow, Run, Artifact, Validation, Quality, Compatibility, Readiness or Approval owner is introduced.

## Application-family preservation

The action map remains conditional by actual family membership/capability.

```text
authority-only use              remains valid
direct Generation               requires no fabricated Learning/Learned State
learned Generation              adds actual Learning/Learned State semantics
evaluation-focused use          remains valid without Generation
evidence-gated Generation       preserves Generation completion ownership
Execution-bearing variants      add Execution actions only under AF-X
Provenance-bearing variants     add Provenance actions only under AF-P
```

The full eleven-concept workflow is not a universal mapping template.

## Synchronization visibility

Synchronization relevance is expressed through concept-owned actions; there is no mapped “execute synchronization” action.

Examples:

```text
Learning.Commit                    -> SYNC-01 / 02 / optional 03
Learning.InitiateRealization       -> SYNC-04
Learning.Complete                  -> SYNC-05
Generation.Commit                  -> SYNC-01 / 02 / optional 03 / 06
Generation.InitiateFulfillment     -> SYNC-07
Generation.EvaluateCompletionBasis -> optional SYNC-13
Evaluation.Commit                  -> SYNC-09
Evaluation.ValidateMethodContext   -> SYNC-10
Evaluation.Initiate                -> SYNC-11
Evaluation.Complete                -> SYNC-12
Provenance.RecordTypedRelationship -> SYNC-14
```

`SYNC-08` remains retired and `SYNC-15` remains reclassified.

## Current coverage position

For action subjects:

```text
SOURCE IDENTIFIED -> SEMANTICALLY MAPPED
```

Queries, state, history and explanation remain for 010-C. No action is yet claimed linguistically aligned, surface-mapped, family-replayed or parity-validated.

## Core mapping guardrails

- upstream semantics win;
- mapping is not implementation representation;
- application-family optionality remains visible;
- synchronization owns no state/control;
- semantic and operational completion remain distinct;
- candidate/intermediate material is not authoritative result by physical existence;
- exact historical binding is inspectable and non-reactive by default;
- Evidence remains finding authority, not approval/release authority;
- Provenance remains relationship authority, not source-fact authority;
- disclosure/history-quality states remain typed where material;
- ordinary inspection remains bounded at enterprise scale;
- human/programmatic parity means equivalent material semantics, not identical ergonomics.

## Phase 010 sequence

```text
010-A  COMPLETE — mapping authority / coverage / actor-surface taxonomy / evidence baseline
010-B  COMPLETE — concept action -> actor intent / interaction mapping
010-C  NEXT — state/query/history/explanation -> inspection mapping
010-D  linguistic / vocabulary / typed status mapping
010-E  physical / interaction surface mapping
010-F  application-family workflow composition / progressive disclosure
010-G  human-programmatic parity / degraded-recovery-scale misfit audit
010-H  consolidation / Phase 011 handoff
```

## Current next boundary

**010-C — Concept State, Query, History & Explanation → Inspection Mapping** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
