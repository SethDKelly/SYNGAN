---
type: Synchronization Index
title: SYNGAN Accepted Synchronizations
status: active
---

# SYNGAN Accepted Synchronizations

This directory contains canonical cross-concept coordination rules accepted in Phase 001 and refined through later concept-specification and design-validation phases.

Concept specifications own their own purpose, state, actions, lifecycle, and invariants. This layer owns coordination where a meaningful transition crosses concept boundaries.

## Canonical synchronization set

- [Core Synchronizations](core-synchronizations.md) — SYNC-01 through SYNC-15.

Phase 002 originally confirmed that the fifteen-rule set remained sufficient after concept specification. [006-C — End-to-End Scenario, Exception, Failure & Adversarial Synchronization Validation](../phases/006/006-C-end-to-end-scenario-exception-failure-adversarial-synchronization-validation.md) re-ran that decision against the concrete Phase 005 planning seams, security/recovery failures, the Phase 006-B Operational Authority Continuity contract, and topology-sensitive time-series/multi-table scenarios.

006-C retained the same fifteen synchronization IDs while refining SYNC-04, SYNC-07, SYNC-08, SYNC-11, SYNC-14 and SYNC-15. No `SYNC-16` is currently justified.

The provisional `Relationship` candidate remains outside the accepted concept catalog pending 006-G. If it is accepted later, its synchronization needs must be evaluated explicitly rather than inferred from topology/API representation.

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
- same-Execution continuation may be blocked by current authorization/dependency/platform capability without rewriting the committed activity;
- restored/regressed persistence does not re-establish current mutation authority;
- missing restored history is not proof of non-occurrence, and surviving physical effects are not proof of semantic transition;
- Evidence claim strength cannot exceed the producing method's support;
- Provenance is high fan-in but low authority fan-out;
- reproducibility is a cross-cutting [inspectable contract](../authority/reproducibility-contract.md), not a concept;
- continuity gaps may weaken current reproducibility without rewriting historical commitments;
- stable dataset/artifact references remain representation/integration obligations;
- network/external dependencies remain explicit and policy-compatible rather than hidden core prerequisites.
