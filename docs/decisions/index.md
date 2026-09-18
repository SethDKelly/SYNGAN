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

Phase 013-I completed the final ADR reconciliation sweep, and Phase 013-J closed R1.

Interpret ADRs under this order:

1. methodology / Phase 014 whole-design authority;
2. completed Phase 012 concept design;
3. current concepts, dependence/application-family and synchronization authority;
4. current mapping authority;
5. Phase 013 Consolidated Architecture Contract;
6. ADR rationale;
7. retained pre-013 architecture/history;
8. implementation planning, source, tests and provider realization evidence.

A decision record with `status: active` is **active retained rationale**, not a second normative architecture layer.

## Final Phase 013 disposition

All ten ADRs remain retained. No ADR is superseded, deprecated, or newly required by Phase 013.

| ADR | Phase 013 disposition | Current qualification |
|---|---|---|
| [ADR-0001 — Typed Resource/Handle Public API](ADR-0001-typed-resource-handle-public-api.md) | **RETAIN** | 013-B: handles/views resolve or project owner state; generic result terminology creates no shared result owner. |
| [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md) | **RETAIN** | 013-B/C: semantic revision, mutable state version, representation schema and recovery frontier remain distinct. |
| [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](ADR-0003-sealed-manifest-gated-output-promotion.md) | **RETAIN WITH CLARIFICATION** | 013-D: seal means immutable physical-subject closure, not a mandatory literal manifest; promotion remains Generation-owned result establishment. |
| [ADR-0004 — Semantic Extension & Runtime Binding Separation](ADR-0004-semantic-extension-runtime-binding-separation.md) | **RETAIN** | 013-E: implementation binding may narrow realization but may not silently broaden Strategy semantics. |
| [ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution](ADR-0005-attempt-epoch-fencing-recoverable-at-least-once-execution.md) | **RETAIN WITH CLARIFICATION** | 013-F/ADR-0009: Attempt epoch remains subordinate to a non-regressing recovery frontier after rollback. |
| [ADR-0006 — Typed Canonical Provenance & Derived Historical Projections](ADR-0006-typed-provenance-canonical-derived-history-projections.md) | **RETAIN** | 013-G: Provenance owns typed relationships; query/history projections remain derived and non-authoritative. |
| [ADR-0007 — Explicit Dependency Resolution & Scoped Capability Security](ADR-0007-explicit-dependency-resolution-scoped-capability-security.md) | **RETAIN** | 013-E/G: dependency identity/trust/authorization/no-egress and actor disclosure remain independent. |
| [ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters](ADR-0008-portable-core-capability-negotiated-platform-adapters.md) | **RETAIN WITH CLARIFICATION** | 013-H: architecture compatibility, implemented support, conformance verification and scale qualification remain distinct. |
| [ADR-0009 — Non-Regressing Authority After Regressive Control-State Recovery](ADR-0009-non-regressing-authority-after-regressive-control-state-recovery.md) | **RETAIN** | Current cross-cutting recovery authority; no supersession. |
| [ADR-0010 — Self-Contained Distributed Runtime Closure](ADR-0010-self-contained-distributed-runtime-closure.md) | **RETAIN** | 013-E/H: closure applies to every material runtime role; no hidden acquisition or fallback. |

```text
retained ADRs          10
superseded ADRs         0
deprecated ADRs         0
new ADRs                0
undecided ADRs          0
```

## Phase 014 boundary

Phase 014 may use ADRs as rationale/evidence while auditing the full design. An ADR does not justify reopening upstream semantics simply because a different implementation choice would be convenient.

If whole-design evidence demonstrates that an ADR-backed architecture decision conflicts with current upstream authority, reopen the smallest architecture authority and update/supersede the ADR only as a downstream consequence.

## Current phase state

```text
Phase 013   COMPLETE
R1          CURRENTLY CLOSED
Phase 014   ACTIVE
Current subgroup sequencing  SEE docs/phases/014/index.md
R2          OPEN
R3          OPEN
```

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
