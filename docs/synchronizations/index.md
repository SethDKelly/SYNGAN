---
type: Synchronization Index
title: SYNGAN Accepted Synchronizations
status: active
---

# SYNGAN Accepted Synchronizations

This directory contains canonical cross-concept coordination rules accepted in Phase 001 and refined through Phase 002.

Concept specifications own their own purpose, state, actions, lifecycle, and invariants. This layer owns coordination where a meaningful transition crosses concept boundaries.

## Canonical synchronization set

- [Core Synchronizations](core-synchronizations.md) — SYNC-01 through SYNC-15.

[002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](../phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md) confirms that the fifteen-rule set remains sufficient after Phase 002. No new synchronization ID is required at the Phase 002 exit.

## Dependency taxonomy

The accepted model distinguishes:

1. **Reference / binding** — bind stable state owned elsewhere.
2. **Contextual validation** — assess another concept's authority for a local context.
3. **Production** — semantic completion establishes a durable logical result.
4. **Operational realization** — a domain activity coordinates with Execution while retaining semantic authority.
5. **Historical/provenance recording** — material transitions record typed derivation/context.
6. **Controlled handoff** — Evidence is consumed by Generation completion or authority outside the current SYNGAN concept boundary without transferring Evidence ownership.

Ordinary references and reads MUST NOT be promoted into synchronizations merely because an implementation uses events, callbacks, queues, or services.

## Core composition guardrails

- state has one canonical concept owner;
- historical activities bind stable revisions/identities rather than mutable upstream aliases;
- compatibility is contextual validation, not globally mutable shared state;
- Execution operational completion does not define domain semantic completion;
- Attempt remains subordinate operational history;
- exactly-once physical work is not required, but authoritative result promotion must remain unambiguous;
- Evidence claim strength cannot exceed the producing method's support;
- Provenance is high fan-in but low authority fan-out;
- reproducibility is a cross-cutting [inspectable contract](../authority/reproducibility-contract.md), not a concept;
- stable dataset/artifact references remain representation/integration obligations;
- network/external dependencies remain explicit and policy-compatible rather than hidden core prerequisites.
