---
type: Synchronization Index
title: SYNGAN Accepted Synchronizations
status: active
---

# SYNGAN Accepted Synchronizations

This directory contains canonical cross-concept coordination rules accepted at the end of Phase 001.

Concept specifications own their own purpose, state, actions, and invariants. This layer owns coordination where a meaningful transition crosses concept boundaries.

## Canonical synchronization set

- [Core Synchronizations](core-synchronizations.md) — SYNC-01 through SYNC-15.

## Dependency taxonomy

The accepted model distinguishes:

1. **Reference** — bind stable state owned elsewhere.
2. **Validation** — assess another concept's authority for a local context.
3. **Production** — semantic completion establishes a durable result.
4. **Operational realization** — a domain activity coordinates with Execution while retaining semantic authority.
5. **Historical/provenance recording** — material transitions record derivation/context.
6. **External handoff** — Evidence is consumed by authority outside the current SYNGAN concept boundary.

Ordinary references and reads MUST NOT be promoted into synchronizations merely because an implementation uses events, callbacks, or services.

## Core composition guardrails

- state has one canonical concept owner;
- historical activities bind stable revisions rather than mutable upstream state;
- compatibility is contextual validation, not globally mutable shared state;
- Execution operational completion does not define domain semantic completion;
- Provenance is sink-oriented in authority;
- reproducibility is a cross-cutting inspectable contract, not a concept;
- stable dataset/artifact references remain representation/integration obligations.
