---
type: Decision Index
title: SYNGAN Architecture Decision Records
status: active
---

# SYNGAN Architecture Decision Records

## Purpose

Preserve durable rationale, considered alternatives, compatibility consequences and supersession history for material architecture decisions.

ADRs explain **why** a choice was made. They do not outrank current canonical concept or architecture authority.

## Current authority relationship

Interpret ADRs under this order:

1. methodology / completion / cross-cutting authority;
2. completed Phase 012 concept design;
3. current concepts, dependence/application-family and synchronization authority;
4. [Phase 013 Consolidated Architecture Contract](../architecture/phase-013-consolidated-architecture-contract.md);
5. detailed Phase 013 architecture authority;
6. ADR rationale;
7. retained pre-013 architecture/history;
8. implementation planning, source, tests and provider realization evidence.

A record with `status: active` is active retained rationale, not a second normative architecture layer.

## Final Phase 013 disposition

All ten ADRs remain retained. No ADR is superseded, deprecated or newly required by Phase 013.

| ADR | Final disposition | Current qualification |
|---|---|---|
| [ADR-0001 — Typed Resource/Handle Public API](ADR-0001-typed-resource-handle-public-api.md) | **RETAIN** | Handles/views resolve or project owner state; generic result terminology creates no shared result owner. |
| [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md) | **RETAIN** | Semantic revision, mutable state version, representation schema and recovery frontier remain distinct. |
| [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](ADR-0003-sealed-manifest-gated-output-promotion.md) | **RETAIN WITH CLARIFICATION** | Seal means immutable physical-subject closure, not mandatory literal manifest; promotion remains Generation-owned. |
| [ADR-0004 — Semantic Extension & Runtime Binding Separation](ADR-0004-semantic-extension-runtime-binding-separation.md) | **RETAIN** | Implementation binding may narrow realization but may not silently broaden Strategy semantics. |
| [ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution](ADR-0005-attempt-epoch-fencing-recoverable-at-least-once-execution.md) | **RETAIN WITH CLARIFICATION** | Attempt epoch remains subordinate to a non-regressing recovery frontier after rollback. |
| [ADR-0006 — Typed Canonical Provenance & Derived Historical Projections](ADR-0006-typed-provenance-canonical-derived-history-projections.md) | **RETAIN** | Provenance owns typed relationships; query/history projections remain derived. |
| [ADR-0007 — Explicit Dependency Resolution & Scoped Capability Security](ADR-0007-explicit-dependency-resolution-scoped-capability-security.md) | **RETAIN** | Dependency identity/trust/authorization/no-egress and disclosure remain independent. |
| [ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters](ADR-0008-portable-core-capability-negotiated-platform-adapters.md) | **RETAIN WITH CLARIFICATION** | Architecture compatibility, implementation, conformance verification and scale qualification remain distinct. |
| [ADR-0009 — Non-Regressing Authority After Regressive Control-State Recovery](ADR-0009-non-regressing-authority-after-regressive-control-state-recovery.md) | **RETAIN** | Current cross-cutting recovery authority; no supersession. |
| [ADR-0010 — Self-Contained Distributed Runtime Closure](ADR-0010-self-contained-distributed-runtime-closure.md) | **RETAIN** | Closure applies to every material runtime role; no hidden acquisition/fallback. |

```text
retained ADRs          10
superseded ADRs         0
deprecated ADRs         0
new ADRs                0
undecided ADRs          0
Phase 013               COMPLETE
R1                      CURRENTLY CLOSED
```

## Legacy relationship

The Phase 007 Consolidated Architecture Contract remains useful historical synthesis. It is not current architecture authority where Phase 013 differs.

## Future ADR rule

Create another ADR only for a genuinely consequential architecture choice requiring durable rationale. Do not use an ADR to smuggle independent product purpose/state/actions/lifecycle into architecture; concept rediscovery comes first.

## Current next boundary

**Phase 014 pre-phase start gate — whole-design/readiness decomposition** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
