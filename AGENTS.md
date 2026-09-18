# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**Jackson concept design is complete. Phase 013 architecture reconciliation is complete and R1 is currently closed. Phase 014 — Whole-Design Consolidation & Implementation-Readiness Decision — is next. Implementation remains held.**

Start with:

- `docs/index.md`
- `docs/problem/problem-purpose.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/phases/013/013-J-phase-013-consolidation-r1-completion-decision-phase-014-handoff.md`
- `docs/architecture/phase-013-consolidated-architecture-contract.md`
- `docs/authority/phase-013-residual-architecture-misfit-register.md`
- `docs/synchronizations/current-cross-concept-synchronizations.md`
- `docs/phases/014/index.md`

## Current state

```text
accepted concepts                    11
active synchronizations              13
Jackson concept design               COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013                            COMPLETE
013-A..013-J                         COMPLETE
R1 architecture reconciliation       CURRENTLY CLOSED
representation / architecture       RECONCILED / CURRENT
Phase 014                            NEXT ELIGIBLE
R2                                   OPEN
R3                                   OPEN
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Primary authority rule

> **Completed concept design and the Phase 013 Consolidated Architecture Contract are upstream authority. Historical architecture, ADR rationale, code, tests and provider models may expose genuine contradictory evidence, but may not redefine current semantics merely to preserve historical choices.**

Only genuine contradictory evidence may reopen the smallest affected authority.

## Current architecture baseline

Use `docs/architecture/phase-013-consolidated-architecture-contract.md` as the architecture entry point.

Preserve at least:

- semantic ownership above representation/storage/runtime/provider machinery;
- stable identity and exact historical bindings independent of provider/runtime identity;
- persistence as durability rather than semantic ownership;
- non-regressing recovery authority;
- Generation-owned candidate/finality/completed-output establishment;
- Strategy semantics separate from executable/runtime realization;
- no hidden dependency acquisition, remote fallback or egress expansion;
- distributed runtime closure across all material runtime roles;
- stable Execution separate from Attempts/provider jobs and semantic completion;
- scoped fencing/idempotency/checkpoint/cancellation/recovery/admission boundaries;
- Evaluation semantic validity separate from runtime success;
- Evidence as durable bounded finding authority, not approval/privacy/release authority;
- Provenance as typed relationship authority with low authority fan-out;
- historical knowledge distinct from current availability/applicability/disclosure;
- Reproducibility as derived cross-cutting assessment;
- provider/product identity separate from capability guarantees;
- architecture-compatible separate from implemented/conformance-verified/scale-qualified support;
- application-family optionality rather than a universal pipeline;
- no M8 future-scope placeholders without concept rediscovery.

## Current synchronization authority

```text
historical synchronization IDs   15
active synchronizations           13
SYNC-08                           retired — Generation-local behavior
SYNC-15                           historical/reclassified — Reproducibility contract
synchronization-owned state       NONE
```

Use `docs/synchronizations/current-cross-concept-synchronizations.md` for current interpretation.

## Phase 014 next scope

Phase 014 owns:

```text
R2  whole-design end-to-end audit
R3  explicit implementation-readiness decision
```

The next action is the Phase 014 **phase-intention / dependency-safe decomposition gate**. Before any `014-A` work:

1. review the Phase 014 intention against current repository state;
2. inventory the full R2/R3 evidence surface;
3. divide Phase 014 into the smallest dependency-safe subphases;
4. define entry/exit evidence and reopen rules;
5. reserve the final subgroup for explicit R2/R3 consolidation and decision.

Do not invent implementation work during this decomposition.

## Durable quality rules

Decision-material disclosure:

> **Do not hide a qualifier whose omission could change the actor's immediate semantic decision or make current state appear stronger than its owner supports.**

Provider evidence:

> **Consume provider facts only at the evidentiary strength they actually establish.**

Future rediscovery:

> **New independent product-facing purpose/state/actions/lifecycle returns to concept discovery before architecture or implementation.**

## Implementation boundary

Until Phase 014 explicitly decides R3:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

Even after a positive R3 decision, Phase 015 explicit implementation authority remains required before production implementation begins.

## Current next boundary

**Phase 014 pre-phase start gate — define the dependency-safe Whole-Design Consolidation & Implementation-Readiness subphase plan** is next eligible.
