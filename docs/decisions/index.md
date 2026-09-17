---
type: Decision Index
title: SYNGAN Architecture Decision Records
status: active
---

# SYNGAN Architecture Decision Records

## Purpose

This directory preserves durable decision rationale, considered alternatives, compatibility consequences and supersession history for material architecture/governance decisions.

Decision records support canonical authority; they do not replace it.

## Current Phase 013 relationship

SYNGAN has completed Jackson concept design and is actively reconciling retained architecture in Phase 013.

Current interpretation begins with:

1. [Phase 013 Architecture Reconciliation Authority](../authority/phase-013-architecture-reconciliation-authority.md);
2. completed Phase 012 concept-design authority and current concepts/dependence/synchronizations/mapping;
3. completed Phase 013 reconciliation decisions;
4. retained Phase 004/006/007 architecture under reconciliation;
5. ADR rationale under reconciliation;
6. implementation planning, source, tests and historical phase records.

The [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md) remains the strongest retained pre-completion synthesis, but it is a Phase 013 reconciliation subject rather than automatically current architecture authority.

A historical ADR frontmatter state of `active` records its prior accepted decision lifecycle. It does not pre-decide the Phase 013 retain/clarify/amend/supersede outcome. 013-I owns the final ADR disposition sweep.

## Retained decisions

- [ADR-0001 — Typed Resource/Handle Public API](ADR-0001-typed-resource-handle-public-api.md) — typed specification/activity/result/Execution/history resource roles rather than a universal mutable Session or payload-only identity.
- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md) — separates stable identity, semantic revisions/commitments, lifecycle concurrency and representation schema versions.
- [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](ADR-0003-sealed-manifest-gated-output-promotion.md) — separates candidate materialization, sealed exact subject and semantic promotion.
- [ADR-0004 — Semantic Extension & Runtime Binding Separation](ADR-0004-semantic-extension-runtime-binding-separation.md) — separates Strategy/method authority from executable implementation binding/runtime realization.
- [ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution](ADR-0005-attempt-epoch-fencing-recoverable-at-least-once-execution.md) — ordered Attempt epochs, stale-writer fencing, scoped idempotency, checkpoints, reconciliation and cancellation races.
- [ADR-0006 — Typed Canonical Provenance & Derived Historical Projections](ADR-0006-typed-provenance-canonical-derived-history-projections.md) — canonical typed Provenance with rebuildable derived history/query/reproducibility views.
- [ADR-0007 — Explicit Dependency Resolution & Scoped Capability Security](ADR-0007-explicit-dependency-resolution-scoped-capability-security.md) — dependency/network/egress semantics, current authorization and scoped runtime capabilities remain distinct.
- [ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters](ADR-0008-portable-core-capability-negotiated-platform-adapters.md) — portable core with explicit platform capability negotiation, semantics-preserving fallback or declared incompatibility.
- [ADR-0009 — Non-Regressing Authority After Regressive Control-State Recovery](ADR-0009-non-regressing-authority-after-regressive-control-state-recovery.md) — adds a fresh non-regressing recovery-authority frontier so restoring stale persistence cannot resurrect writer/cancellation/security authority. Historically extends ADR-0005.
- [ADR-0010 — Self-Contained Distributed Runtime Closure](ADR-0010-self-contained-distributed-runtime-closure.md) — requires acquisition closure and compatible runtime closure across material distributed workers. Historically extends ADR-0004 and ADR-0008.

Retained ADR count: **10**.

## Phase 013 ADR disposition discipline

013-B through 013-H may identify ADR implications while reconciling their owned architecture domains. 013-I performs the cross-ADR final sweep.

Possible outcomes include:

```text
RETAIN
CLARIFY
AMEND / CORRECT THROUGH CURRENT ARCHITECTURE + UPDATED RATIONALE
SUPERSEDE
DEFER IMPLEMENTATION-SPECIFIC DETAIL
```

An ADR cannot justify an upstream semantic change merely because an older architecture decision would otherwise need revision.

## Known 013-A precedence finding

`A13-A-005` records the former index statement that current accepted architecture begins with Phase 007 as:

```text
class        AR-2 authority / precedence drift
materiality  AMAT-1
status       CLARIFIED BY 013-A
final ADR disposition sweep  013-I
```

This is not an architecture blocker and requires no upstream reopen.

## Historical Phase 007 result

Phase 007 historically reviewed ADR-0001 through ADR-0010 and found no amendment necessary under the architecture known at that time. That conclusion remains useful history, not a substitute for Phase 013 reconciliation against the completed concept design.

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

During Phase 013, begin with the [Phase 013 Architecture Reconciliation Authority](../authority/phase-013-architecture-reconciliation-authority.md) and [Representation & Architecture Index](../architecture/index.md), then follow only the architecture/ADR subjects owned by the active subgroup.
