---
type: Decision Index
title: SYNGAN Architecture Decision Records
status: active
---

# SYNGAN Architecture Decision Records

## Purpose

This directory preserves durable decision rationale, considered alternatives, compatibility consequences and supersession history for material architecture/governance decisions.

Decision records support canonical authority; they do not replace it.

Current accepted architecture begins with the [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md), with 007-D through 007-J supplying detailed authority where needed.

## Authority relationship

Interpret architecture knowledge using this order:

1. upstream design authority, concepts, synchronizations and experience contracts;
2. current [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md);
3. detailed current 007-D through 007-J architecture authorities;
4. accepted ADR rationale/history;
5. implementation planning and historical phase records.

If an ADR conflicts with newer canonical architecture authority, canonical architecture governs and the ADR should be marked superseded or linked to its replacement.

## Active decisions

- [ADR-0001 — Typed Resource/Handle Public API](ADR-0001-typed-resource-handle-public-api.md) — typed specification/activity/result/Execution/history resource roles rather than a universal mutable Session or payload-only identity.
- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md) — separates stable identity, semantic revisions/commitments, lifecycle concurrency and representation schema versions.
- [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](ADR-0003-sealed-manifest-gated-output-promotion.md) — separates candidate materialization, sealed exact subject and semantic promotion.
- [ADR-0004 — Semantic Extension & Runtime Binding Separation](ADR-0004-semantic-extension-runtime-binding-separation.md) — separates Strategy/method authority from executable implementation binding/runtime realization.
- [ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution](ADR-0005-attempt-epoch-fencing-recoverable-at-least-once-execution.md) — ordered Attempt epochs, stale-writer fencing, scoped idempotency, checkpoints, reconciliation and cancellation races.
- [ADR-0006 — Typed Canonical Provenance & Derived Historical Projections](ADR-0006-typed-provenance-canonical-derived-history-projections.md) — canonical typed Provenance with rebuildable derived history/query/reproducibility views.
- [ADR-0007 — Explicit Dependency Resolution & Scoped Capability Security](ADR-0007-explicit-dependency-resolution-scoped-capability-security.md) — dependency/network/egress semantics, current authorization and scoped runtime capabilities remain distinct.
- [ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters](ADR-0008-portable-core-capability-negotiated-platform-adapters.md) — portable core with explicit platform capability negotiation, semantics-preserving fallback or declared incompatibility.
- [ADR-0009 — Non-Regressing Authority After Regressive Control-State Recovery](ADR-0009-non-regressing-authority-after-regressive-control-state-recovery.md) — adds a fresh non-regressing recovery-authority frontier so restoring stale persistence cannot resurrect writer/cancellation/security authority. **Extends ADR-0005; does not supersede it.**
- [ADR-0010 — Self-Contained Distributed Runtime Closure](ADR-0010-self-contained-distributed-runtime-closure.md) — requires both acquisition closure and exact compatible runtime closure across every material distributed worker, including dynamically added workers. **Extends ADR-0004 and ADR-0008; does not supersede them.**

## Phase 007 consolidation result

007-K reviewed ADR-0001 through ADR-0010 against the consolidated identity, persistence, distributed-data/topology, runtime/security, Execution/recovery, Evidence/history/disclosure and implementation-proof architecture.

No ADR requires supersession or amendment before controlled implementation re-entry.

The active ADR count remains **10**.

007-J/007-K add no ADR because they define proof/claim and re-entry governance boundaries under the existing architecture rather than selecting a new technical alternative requiring independent rationale.

## When to create an ADR

Use an ADR when a decision is materially consequential and benefits from preserved rationale, particularly when it:

- selects among credible architecture alternatives;
- establishes a durable compatibility boundary;
- changes dependency direction/layer ownership;
- selects persistence/transaction/identity behavior;
- commits to distributed promotion/recovery/runtime-distribution behavior;
- selects provenance/history/security/platform integration architecture;
- introduces significant migration/portability consequences;
- supersedes or materially extends a prior decision.

Do not create an ADR merely to repeat an invariant already canonical elsewhere.

## ADR lifecycle

Decision records use states such as `proposed`, `active`, `deprecated`, `superseded` or `archived`.

A replaced decision retains its historical rationale and points to the replacement.

## Anti-duplication rule

ADRs explain *why* a choice was made. Full current normative rules belong in canonical architecture documents.

For current implementation-facing architecture, begin with:

[Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md).
