---
type: Decision Index
title: SYNGAN Architecture Decision Records
status: active
---

# SYNGAN Architecture Decision Records

## Purpose

This directory preserves durable decision rationale, considered alternatives, compatibility consequences, and supersession history for material architecture/governance decisions.

Decision records support canonical authority; they do not replace it.

Current accepted architecture rules belong under [`docs/architecture/`](../architecture/index.md). An ADR explains **why** a material choice was made, which alternatives were considered, and what later record supersedes it when the decision changes.

## Authority relationship

Interpret architecture knowledge using this order:

1. upstream design authority, concepts, synchronizations, and experience contracts;
2. current canonical architecture authority under `docs/architecture/`;
3. accepted ADR rationale/history under `docs/decisions/`;
4. phase records preserving design execution history.

If an ADR summary conflicts with newer canonical architecture authority, the canonical architecture document governs current implementation and the ADR SHOULD be marked superseded or linked to the replacing decision.

## Active decisions

- [ADR-0001 — Typed Resource/Handle Public API](ADR-0001-typed-resource-handle-public-api.md) — adopts typed specification/activity/result/Execution/history resource roles rather than a universal mutable Session, payload-only API, universal Spark ML model, generic Result object, or process-local Future as canonical identity.
- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md) — separates stable resource identity, immutable semantic revision/commitment snapshots, mutable lifecycle state versions, and representation schema versions while requiring stale-write detection without mandating universal event sourcing.
- [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](ADR-0003-sealed-manifest-gated-output-promotion.md) — separates mutable distributed candidate materialization, immutable sealed candidate identity, and Generation semantic promotion so Evaluation binds the exact candidate while at most one completed output is established without requiring copy-on-promotion or exactly-once physical writes.

## When to create an ADR

Use an ADR when a decision is materially consequential and benefits from preserved rationale, for example when it:

- selects among credible architectural alternatives;
- establishes a durable compatibility boundary;
- changes dependency direction or layer ownership;
- selects a persistence/transaction/identity approach;
- commits to a distributed materialization/promotion mechanism;
- chooses an extension/runtime/plugin boundary;
- selects execution/recovery/fencing semantics;
- selects provenance/history/security integration architecture;
- introduces significant migration or portability consequences;
- supersedes a previously accepted architecture decision.

Do not create an ADR merely to repeat an invariant already stated canonically.

## Suggested ADR shape

A record SHOULD contain:

```text
Title / stable decision ID
Status
Decision context / problem
Governing upstream authority
Decision
Alternatives considered
Consequences / tradeoffs
Compatibility / migration impact
Canonical architecture documents affected
Supersedes / superseded by
```

Exact filenames/ID formatting may be refined later, but stable identifiers SHOULD be used once ADRs are referenced externally.

## Lifecycle

Decision records SHOULD use documentation lifecycle states such as:

- `proposed`;
- `active`;
- `deprecated`;
- `superseded`;
- `archived`.

A replaced ADR SHOULD retain historical rationale and link to the replacing decision rather than being silently rewritten to make the past appear different.

## Anti-duplication rule

An ADR SHOULD summarize the accepted decision sufficiently to explain its rationale but SHOULD link to the canonical architecture document for the full current normative rule.

Large architecture specifications MUST NOT be copied wholesale into ADRs.
