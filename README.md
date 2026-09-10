# SYNGAN

SYNGAN is a design-first synthetic-data generation framework intended for Spark-scale workloads.

SYNGAN follows Daniel Jackson-style concept design and explicitly requires the full design program to complete before implementation can become ready.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current authority:

- [`Concept Design Methodology`](docs/authority/design-methodology.md)
- [`Jackson Design Completion & Implementation Hold`](docs/authority/jackson-design-completion-implementation-hold.md)
- [`Jackson Methodology Completion Matrix`](docs/authority/jackson-methodology-completion-matrix.md)
- [`Problem Knowledge`](docs/problem/index.md)
- [`Phase 008 — Individual Concept Design Normalization & Completeness`](docs/phases/008/index.md)
- [`Phase 007 Consolidated Architecture Contract`](docs/architecture/phase-007-consolidated-architecture-contract.md) as downstream architecture evidence

## Status

```text
Phase 008                  ACTIVE
008-A                      COMPLETE
008-B                      COMPLETE
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

008-A established the full methodology completion ledger and design-only guardrails.

008-B reconciled the current problem/purpose baseline, established [concept-justification traceability](docs/problem/concept-justification-traceability.md), and made the current O1-O16 outcome set explicit. The structured-data target now explicitly includes single-table, time-series, and multi-table shared-key generation, while text-bearing structured fields require at least one self-contained source-derived/local baseline path. All eleven accepted concepts remain justified at the purpose level; no catalog change was made.

Phase 007 remains valuable architecture work, but its 007-K implementation-reentry conclusion is superseded because the fuller Jackson methodology still has unresolved design obligations.

## Remaining design roadmap

```text
008  Individual Concept Design Normalization & Completeness
009  Concept Dependence, Application Family, Composition & Synchronization Closure
010  Concept Mapping, Interaction, Linguistic & Experience Alignment
011  Specificity, Familiarity, Integrity, Synergy, Misfit & Adversarial Design Validation
012  Jackson Concept-Design Consolidation & Completion Decision
013  Post-Concept Representation & Architecture Reconciliation
014  Whole-Design Consolidation, Residual Debt Audit & Implementation-Readiness Decision
---
015  Implementation Authority & Controlled Delivery — FUTURE ONLY
```

Phases 009-014 will each be divided into dependency-safe subgroups immediately before starting.

## Methodology boundary

SYNGAN does not treat architecture completeness, implementation planning, a green test suite, or an existing scaffold as proof that concept design is complete.

After Phase 012 positively closes Jackson concept design, retained representation/architecture must still be reconciled in Phase 013. Only Phase 014 may determine that the *entire* design is ready for implementation.

A positive Phase 014 may set:

```text
IMPLEMENTATION READINESS   READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NEXT
```

That still does not start implementation; a future explicit Phase 015 must establish implementation authority.

## Current semantic baseline

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
current desired outcomes   16
```

These remain subject to genuine design correction if later Jackson work demonstrates a missing or invalid concept/synchronization.

## Current next boundary

**008-C — Concept State Model, Identity, History & Invariant Normalization** is next.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.