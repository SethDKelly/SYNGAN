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
010-D                        NEXT ELIGIBLE
F1                           CURRENTLY CLOSED
F2                           CURRENTLY CLOSED
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
- [Concept Action → Actor Intent & Interaction Mapping](concept-action-actor-intent-interaction-mapping.md) — 010-B semantic action authority.
- [Concept State, Query, History & Explanation → Inspection Mapping](concept-state-query-history-explanation-inspection-mapping.md) — **010-C current semantic inspection authority**.
- [Phase 010 Entry & Decomposition](../phases/010/010-entry-decomposition.md)
- [Phase 009 Consolidation](../authority/phase-009-dependence-composition-consolidation.md)
- [Accepted Concept Catalog](../concepts/index.md)
- [Actors & Needs](../problem/actors.md)
- [Domain Terminology](../terminology/index.md)
- Phase 003/006 experience documents — retained mapping evidence.

## Current semantic mapping coverage

### Actions — F1

010-B maps all normalized command groups:

```text
normalized command groups     66
semantically mapped           66
blocked by mapping misfit      0
```

F1 is currently closed at the surface-neutral semantic action-mapping layer.

### Inspection — F2

010-C maps all normalized query/observation groups and material lifecycle/history envelopes:

```text
normalized query groups                 52
semantically mapped query groups        52
lifecycle/history envelopes             11 / 11
cross-concept explanation patterns       5
blocked by mapping misfit                0
```

F2 is currently closed at the surface-neutral semantic inspection-mapping layer.

## 010-C inspection authority

The governing rule is:

> **Inspection exposes owned or validly derived truth; it does not create a second owner for that truth.**

A combined dashboard/report/history/explanation may compose facts from multiple concepts, but each fact remains attributable to its canonical owner.

No standalone Dashboard, Status, History, Explanation, Lineage, Artifact, Result, Approval or Inspection concept is introduced.

## Current-versus-historical rule

Inspection must support current and historical truth simultaneously.

Examples:

```text
historical Generation bound Strategy S17
+ S17 is currently retired

historical Generation relied on Evidence E9
+ E9 is currently stale/inapplicable/invalidated for new reliance

historical Learning bound Data Meaning M4
+ M6 is currently effective
```

Current status does not rewrite historical binding truth.

## Semantic / operational inspection

Where Execution exists, inspection must keep separately recoverable:

```text
parent Learning / Generation / Evaluation semantic state
Execution operational state
Attempt history
retry / resume / recovery / cancellation eligibility
```

`Execution.completed` never becomes parent semantic completion through display or query convenience.

## Candidate / finality inspection

Generation inspection must preserve:

```text
partial material
candidate material
candidate complete / awaiting required validation
completion-basis result
completed authoritative logical output
failed/cancelled non-promoted material
```

Physical existence does not establish finality.

## Evidence inspection

Evidence interpretation requires enough context to preserve claim strength:

```text
finding
Criterion
subject / reference
method
scope / coverage
claim strength
uncertainty
limitations
current applicability
```

Evidence remains finding authority rather than approval/release/privacy-guarantee authority.

## Provenance / explanation inspection

Provenance may support typed traversal and historical explanation while remaining relationship authority rather than source-fact authority.

Current derived explanation patterns include:

```text
EX-01  historical Learning
EX-02  historical Generation
EX-03  Evidence
EX-04  current-versus-historical divergence
EX-05  incomplete/reconstructed history
```

These are derived mapping compositions, not new canonical aggregate state.

## Disclosure and history quality

Inspection must preserve material distinctions among:

```text
visible
redacted / authorized summary
withheld
unavailable
unknown
absent
```

History/explanation must also preserve, where material:

```text
DIRECT
RECONSTRUCTED
PARTIAL
UNAVAILABLE
INDETERMINATE
```

These are current mapping-level semantic categories pending 010-D linguistic alignment, not public/runtime enums.

## Enterprise-scale boundedness

Routine inspection is metadata/reference/summary-first.

Current rules require:

- bulk source/output/Learned-State contents remain separate from concept-state inspection;
- Attempt/log/telemetry drill-down remains bounded;
- Provenance traversal remains bounded;
- large Evidence support artifacts may be referenced rather than loaded into routine views.

No concrete query/pagination/storage technology is selected.

## Application-family preservation

Inspection remains conditional on actual family membership:

```text
authority-only use           independently inspectable
L-KERNEL                     no fabricated Generation/Evaluation/Execution/Provenance
direct Generation            no fabricated Learning/Learned State
learned Generation           adds actual learned-state history only
E-KERNEL                     coherent without Generation
evidence-gated Generation    composes exact Evidence while preserving ownership
AF-X                         Execution inspection only when Execution exists
AF-P                         Provenance traversal only when Provenance exists
AF-FULL                      may compose all views without a combined state owner
```

## Coverage progression

Current semantic subjects have advanced:

```text
actions                     SEMANTICALLY MAPPED
queries/observations        SEMANTICALLY MAPPED
lifecycle/history envelopes SEMANTICALLY MAPPED
explanation patterns        SEMANTICALLY MAPPED
```

They are not yet universally:

```text
LINGUISTICALLY ALIGNED
SURFACE-MAPPED
FAMILY-REPLAYED at workflow level
PARITY-VALIDATED
```

Those obligations remain 010-D through 010-G.

## Phase 010 sequence

```text
010-A  COMPLETE — mapping authority / coverage / actor-surface taxonomy / evidence baseline
010-B  COMPLETE — concept action -> actor intent / interaction mapping
010-C  COMPLETE — state/query/history/explanation -> inspection mapping
010-D  NEXT — linguistic / vocabulary / typed status / disclosure semantics
010-E  physical / interaction surface mapping
010-F  application-family workflow composition / progressive disclosure
010-G  human-programmatic parity / degraded-recovery-scale misfit audit
010-H  consolidation / Phase 011 handoff
```

## Current next boundary

**010-D — Linguistic Mapping, Vocabulary, Typed Status & Disclosure Semantics** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
