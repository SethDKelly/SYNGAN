---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design & Implementation Knowledge
status: active
---

# SYNGAN Design & Implementation Knowledge

This directory is the canonical knowledge bundle for SYNGAN.

## Authority order

```text
methodology / design authority
  > problem knowledge
  > concepts
  > dependence / application family / synchronization / composition
  > concept mapping / experience
  > representation / architecture design
  > implementation planning history
  > code / tests / deployment evidence
  > ADR rationale / phase history / backlog / examples
```

Existing architecture, source or tests never become upstream concept-design authority merely because they exist or pass.

## Current governing authority

- [Concept Design Methodology](authority/design-methodology.md)
- [Jackson Design Completion & Implementation Hold](authority/jackson-design-completion-implementation-hold.md)
- [Jackson Methodology Completion Matrix](authority/jackson-methodology-completion-matrix.md)
- [Current Problem Knowledge](problem/index.md)
- [Accepted Concept Catalog](concepts/index.md)
- [Concept Dependence & Application Family](dependence/index.md)
- [Synchronization Authority](synchronizations/index.md)
- [Phase 009 Consolidation](authority/phase-009-dependence-composition-consolidation.md)
- [Concept Mapping Authority](mapping/index.md)
- [010-A Mapping Control Authority](mapping/mapping-authority-coverage-actor-surface-evidence-baseline.md)
- [010-B Concept Action Mapping](mapping/concept-action-actor-intent-interaction-mapping.md)
- [Phase 010](phases/010/index.md)

## Current state

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
Phase 010 decomposition              COMPLETE
010-A                                COMPLETE
010-B                                COMPLETE
010-C                                NEXT ELIGIBLE
F1                                   CURRENTLY CLOSED
F2                                   PARTIAL
F3                                   PARTIAL TO STRONG
F4                                   PARTIAL
F5                                   STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Current mapping program

010-A established the mapping schema, coverage model, actor/surface taxonomy, application-family tags and evidence baseline.

010-B now establishes complete surface-neutral semantic mapping for all normalized state-changing actions:

```text
normalized command groups     66
semantically mapped           66
blocked by mapping misfit      0
```

The action map does not equate conceptual commands with buttons/endpoints. System-established actions such as Learned State/Evidence establishment, Attempt outcome recording and Provenance relationship recording remain observable without requiring direct user controls.

The map preserves:

- valid reduced application-family variants;
- direct versus learned Generation;
- activity-owned compatibility/readiness;
- semantic commitment versus operational realization;
- candidate versus authoritative result;
- cancellation request versus terminal cancellation;
- Evaluation success versus favorable Evidence;
- Evidence versus approval/release/privacy authority;
- Provenance relation versus source-fact ownership;
- current/future-use status versus exact historical truth;
- conditional Execution and Provenance capabilities.

## Current Phase 010 sequence

```text
010-A  COMPLETE — mapping authority / coverage / actor-surface taxonomy / evidence baseline
010-B  COMPLETE — action -> actor intent / interaction mapping
010-C  NEXT — state/query/history/explanation -> inspection mapping
010-D  linguistic / vocabulary / typed status / disclosure semantics
010-E  physical interaction across candidate surface families
010-F  application-family workflow composition / progressive disclosure
010-G  human-programmatic parity / degraded-recovery-scale mapping misfit
010-H  mapping consolidation / Phase 011 handoff
```

Phase 003/006 experience documents remain supporting evidence and are normalized against Phase 008/009/010 current authority.

## Implementation status rule

Through Phases 010-014:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

Do not translate concepts, application-family variants, synchronization IDs or mapping records mechanically into packages, services, schemas, transactions, events, APIs, UI components, deployment units or product SKUs.

Only a positive Phase 014 may make implementation **READY / NOT STARTED / NEXT**; implementation itself still requires Phase 015.

## Current next boundary

**010-C — Concept State, Query, History & Explanation → Inspection Mapping** is next eligible.
