---
type: Authority Index
title: SYNGAN Design Authority
status: active
---

# SYNGAN Design Authority

These documents define how SYNGAN design knowledge is created, reconciled, audited for readiness, and eventually implemented.

## Current methodology / completion authority

- [Concept Design Methodology](design-methodology.md)
- [Jackson Design Completion & Implementation Hold](jackson-design-completion-implementation-hold.md)
- [Jackson Methodology Completion Matrix](jackson-methodology-completion-matrix.md)
- [Phase 014 Whole-Design Consolidation & Readiness Authority](phase-014-whole-design-readiness-authority.md)

## Completed upstream authority

- [Phase 012 Jackson Concept-Design Consolidation](phase-012-jackson-concept-design-consolidation.md)
- [Phase 013 Consolidated Architecture Contract](../architecture/phase-013-consolidated-architecture-contract.md)
- [Phase 013 Residual Architecture Misfit Register](phase-013-residual-architecture-misfit-register.md)
- [Current Cross-Concept Synchronization Contract](../synchronizations/current-cross-concept-synchronizations.md)

Detailed Phase 013-B through 013-I architecture authorities remain current supporting detail beneath the consolidated Phase 013 contract.

Retained Phase 004/006/007 architecture and ADR rationale remain historical rationale/evidence. Historical `active/current/canonical` language does not outrank current authority.

## Current posture

```text
accepted concepts                    11
active synchronizations              13
Jackson concept design               COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013                            COMPLETE
R1 architecture reconciliation       CURRENTLY CLOSED
Phase 014 start gate                 COMPLETE
Phase 014                            ACTIVE
014-A                                NEXT ELIGIBLE
R2                                   OPEN
R3                                   OPEN
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Phase 014 authority discipline

Phase 014 audits the full chain from problem/outcomes through architecture. It uses `WMAT-0..WMAT-3` for whole-design materiality and keeps readiness-only concerns separate as `READINESS-NOTE`, `READINESS-RISK`, or `READINESS-BLOCK`.

A whole-design defect reopens only the smallest owning authority. Implementation inconvenience, provider preference, existing code/tests, prior package structure or cost is not by itself a design contradiction.

## Approved sequence

```text
014-A  evidence baseline / traceability / reopen rules — NEXT
014-B  problem / actor / outcome / scope / concept-purpose coverage
014-C  concept / dependence / application-family / synchronization integrity
014-D  mapping / interaction / disclosure / semantic parity
014-E  architecture realization / authority / traceability
014-F  cross-layer scenario / failure / recovery / scale / security / portability
014-G  implementation-neutral completeness / handoff sufficiency / residual register
014-H  R2 decision / R3 readiness decision / Phase 015 handoff
```

R3 may be decided only after the R2 evidence chain is complete.

## Durable guardrails

- later/current state does not rewrite exact historical/as-bound truth;
- decision-material qualifiers cannot be hidden by progressive disclosure;
- provider facts are consumed only at their actual evidentiary strength;
- architecture mechanisms do not become concepts by addressability/durability;
- Evidence does not become approval or formal privacy authority;
- Provenance does not become copied canonical truth;
- application-family optionality must not become a universal workflow;
- future independent purpose/lifecycle returns to concept discovery before architecture/implementation.

## Implementation boundary

Phase 014 is design/readiness work only.

Until R3 is explicitly decided:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

Even a positive R3 requires explicit Phase 015 implementation authority.

## Current next boundary

**014-A — Whole-Design Audit Authority, Evidence Baseline, Traceability & Reopen Rules** is next eligible.
