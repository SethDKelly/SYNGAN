# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**Jackson concept design is complete for the current product scope. Phase 013 architecture reconciliation is ACTIVE; 013-A through 013-I are complete, and 013-J is next. Implementation remains held.**

Start with:

- `docs/index.md`
- `docs/problem/problem-purpose.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-013-architecture-reconciliation-authority.md`
- `docs/authority/phase-013-residual-architecture-misfit-register.md`
- `docs/phases/013/index.md`
- `docs/phases/013/013-I-cross-architecture-composition-adr-legacy-m6-residual-reconciliation.md`
- `docs/architecture/phase-013-i-cross-architecture-composition-legacy-m6-residual-reconciliation.md`
- `docs/synchronizations/current-cross-concept-synchronizations.md`
- `docs/architecture/index.md`

## Current state

```text
accepted concepts                    11
active synchronizations              13
Phase 012                            COMPLETE
A1-H2                                CURRENTLY CLOSED
Jackson concept design               COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013                            ACTIVE
013-A                                COMPLETE
013-B                                COMPLETE
013-C                                COMPLETE
013-D                                COMPLETE
013-E                                COMPLETE
013-F                                COMPLETE
013-G                                COMPLETE
013-H                                COMPLETE
013-I                                COMPLETE
013-J                                NEXT ELIGIBLE
R1 architecture reconciliation       DOWNSTREAM / IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Primary authority rule

> **Completed concept design and completed Phase 013 reconciliation decisions are upstream authority. Retained legacy architecture, ADR rationale, code, tests and provider models may expose genuine contradictory evidence, but they may not redefine current semantics merely to preserve historical choices.**

Only a demonstrated `AR-9` contradiction may justify `UPSTREAM-REOPEN`.

## Current reconciliation result through 013-I

Preserve the reconciled architecture invariants established by 013-B through 013-H, including semantic ownership above representation/storage/runtime/platform mechanisms, exact identity/history, non-regressing recovery, Generation-owned finality, Strategy/runtime separation, Execution/Attempt separation, Evidence/Provenance/history boundaries, actor-safe disclosure, provider guarantee qualification, application-family optionality and private/offline/no-egress behavior.

013-I additionally establishes:

```text
cross-architecture composition              PASS
M6 synchronization drift                    CLOSED
ADR final disposition                       COMPLETE — 10 / 10 RETAINED
legacy current-authority ambiguity          CLOSED
historical implementation re-entry          SUPERSEDED AS CURRENT AUTHORIZATION
M8 placeholder leakage                      NOT FOUND
unresolved AMAT-2                           0
unresolved AMAT-3                           0
unresolved AR-3..AR-9                       0
upstream reopen                              NONE
```

Current synchronization authority is:

```text
historical synchronization IDs   15
active synchronizations           13
SYNC-08                           retired — Generation-local behavior
SYNC-15                           historical/reclassified — Reproducibility contract
synchronization-owned state       NONE
```

Use `docs/synchronizations/current-cross-concept-synchronizations.md` rather than inferring current active status from historical anchors in `core-synchronizations.md` or pre-Phase-009 documents.

Pre-013 Phase 004/006/007 architecture remains retained historical rationale/evidence. Historical `active/current/canonical` wording does not outrank Phase 013. Phase 007-A..C scaffold is feasibility evidence only; Phase 007-K implementation re-entry is superseded as current authorization.

## 013-J next scope

013-J is a consolidation/completion-decision pass. It must:

- verify the Phase 013-A..013-I evidence is mutually consistent;
- verify the residual architecture register remains at zero unresolved AMAT-2/AMAT-3/AR-3..AR-9 findings;
- confirm the current architecture authority chain is unambiguous;
- explicitly decide whether R1 is `CURRENTLY CLOSED`;
- if R1 closes, mark Phase 013 complete and hand off to Phase 014;
- preserve the implementation hold regardless of a positive R1 decision;
- avoid inventing implementation work or treating architecture completion as implementation readiness.

If new contradictory evidence appears, update the residual register and reopen the smallest affected authority rather than forcing closure.

## Durable quality rules

Decision-material disclosure:

> **Do not hide a qualifier whose omission could change the actor's immediate semantic decision or make current state appear stronger than its owner supports.**

Provider evidence:

> **Consume provider facts only at the evidentiary strength they actually establish.**

Future rediscovery:

> **New independent product-facing purpose/state/actions/lifecycle returns to concept discovery before architecture or implementation.**

## Implementation boundary

Phase 013 is design/reconciliation only.

Do not begin production behavior, migrations, schemas, data-plane implementation, runtime/security integrations, Execution/recovery machinery, Evidence/Provenance/history services, platform adapters, deployment automation, public API stabilization, package refactoring, benchmarks or executable conformance work.

```text
Phase 013  architecture reconciliation — ACTIVE
Phase 014  whole-design / implementation-readiness decision
Phase 015  implementation authority — FUTURE ONLY
```

Until Phase 014 positively passes:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## Current next boundary

**013-J — Phase 013 Consolidation, R1 Completion Decision & Phase 014 Handoff** is next eligible.