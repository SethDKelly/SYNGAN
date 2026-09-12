---
type: Synchronization Index
title: SYNGAN Accepted Synchronizations
status: complete-current
---

# SYNGAN Accepted Synchronizations

This directory contains current cross-concept composition authority for SYNGAN.

Concept specifications own purpose, state, actions, lifecycle and invariants. Synchronization coordinates already-owned behavior across concept boundaries and owns no independent state.

## Current authority

- [Phase 009 Consolidation](../authority/phase-009-dependence-composition-consolidation.md) — current cross-layer handoff authority.
- [Composition Economy, Coupling, Synergy & Integrity Closure](composition-economy-synergy-integrity.md) — 009-G whole-composition authority.
- [Synchronization Trigger, Preconditions/Postconditions, State Ownership & Hidden-Coordinator Audit](trigger-ownership-normalization.md) — 009-F detailed trigger/ownership authority.
- [Synchronization Inventory Revalidation Across the Application Family](application-family-revalidation.md) — 009-E inventory/scope authority, superseded where 009-F/G refine scope/classification.
- [Core Synchronizations](core-synchronizations.md) — historical source evidence; current membership/scope follows 009-E/F/G/H.

## Current synchronization inventory

```text
accepted concepts                       11
historical synchronization IDs          15
active cross-concept synchronizations   13
required-relational                      6
capability/occurrence conditional        7
retired concept-local IDs                1  (SYNC-08)
reclassified contract IDs                1  (SYNC-15)
new synchronization IDs                  0
SYNC-16                                  NOT JUSTIFIED
```

Historical IDs remain reserved and are never reused.

## Active — required relational

```text
SYNC-01  Data Meaning revision binding
SYNC-02  Strategy selection and compatibility
SYNC-05  Learning produces Learned State
SYNC-09  Evaluation Criterion binding
SYNC-10  Evaluation method compatibility
SYNC-12  Evaluation produces Evidence
```

## Active — capability / occurrence conditional

```text
SYNC-03  Constraint binding and handling disposition
SYNC-04  Learning operational realization
SYNC-06  Generation / Learned State reuse compatibility and exact basis binding
SYNC-07  Generation operational realization
SYNC-11  Evaluation operational realization
SYNC-13  Generation / Evidence evidence-gated completion handoff
SYNC-14  Provenance recording at material transitions
```

`SYNC-06` does not activate for direct Generation.

## Canonical ownership

```text
consumer exact bindings + contextual assessments
  -> Learning / Generation / Evaluation

producing Learning identity
  -> Learned State

producing Evaluation identity
  -> Evidence

Execution parent binding + Attempts/retry/recovery
  -> Execution

Provenance typed relationship assertions
  -> Provenance

synchronization-owned canonical state
  -> NONE
```

## Composition economy

The thirteen rules form five conceptual coordination planes:

```text
A  reusable-authority binding / contextual assessment
B  activity/result establishment
C  reuse / completion gating
D  operational realization
E  historical relationship explanation
```

These are not architecture layers.

Core family-member burden remains:

```text
L-KERNEL         SYNC-01, SYNC-02, SYNC-05
Direct G-KERNEL  SYNC-01, SYNC-02
E-KERNEL         SYNC-09, SYNC-10, SYNC-12
```

Learned-state-assisted Generation adds `SYNC-06`. Evidence-gated Generation adds `SYNC-13`. Constraint, Execution and Provenance add only occurrence-specific coordination.

No active rule is added, removed, merged, or further narrowed at Phase 009 exit.

## Occurrence-scoped / non-propagation rule

A synchronization coordinates one conceptual occurrence/relation. It does not create a permanent reactive subscription.

Therefore later revision/status changes do not silently rewrite exact historical bindings:

- newer Data Meaning does not reinterpret committed work;
- Strategy retirement does not rewrite historical activities;
- Constraint revision does not rewrite prior bindings;
- Learned State retirement does not mutate prior Generation history;
- Criterion revision does not reinterpret historical Evidence;
- Evidence invalidation changes current reliance but does not silently rewrite historical Generation completion;
- Provenance correction does not rewrite source facts.

## Positive composition synergy

Current explicit synergies include:

1. reusable `Learning -> Learned State -> Generation`;
2. evidence-gated Generation;
3. reusable Constraint + Evaluation/Evidence + Generation;
4. shared Execution operational lifecycle across Learning/Generation/Evaluation;
5. exact bindings + Provenance for end-to-end historical explanation;
6. direct and learned Generation coexistence without fabricated Learning.

## Combined-activation integrity

Evaluation-gated Generation remains staged feedback:

```text
Generation candidate
  -> Evaluation
  -> Evidence
  -> Generation-owned completion decision
```

Evaluation needs candidate identity, not completed Generation. Evidence never owns `Generation.Complete`.

Execution cannot establish domain semantic completion. Provenance cannot establish source facts. Optional capabilities remain optional. No hidden coordinator concept is required.

## Retired / reclassified IDs

### SYNC-08

Remains retired as Generation-local candidate/completion/output behavior. No standalone Output concept exists.

### SYNC-15

Remains reclassified under the cross-cutting Reproducibility Contract. No standalone Reproducibility concept or synchronization-owned state exists.

## Current methodology state

```text
Phase 009  COMPLETE
D1-D4      CURRENTLY CLOSED
E1-E5      CURRENTLY CLOSED
Phase 010  NEXT ELIGIBLE
```

## Phase 010 handoff

Concept mapping must expose the distinctions synchronization preserves without turning them into hidden implementation machinery.

In particular Phase 010 must preserve:

- semantic versus operational completion;
- candidate versus completed Generation output;
- exact authority/result bindings;
- Evidence finding versus approval/release authority;
- Provenance relation versus source ownership;
- conditional synchronization activation;
- current status versus historical binding truth;
- human/programmatic semantic parity.

## Composition guardrails

- one canonical state owner per material fact;
- synchronization owns no state;
- concept behavior remains authoritative under synchronization;
- reusable authorities are bound, not mutated;
- contextual assessments remain activity-owned;
- semantic and operational completion remain distinct;
- Evidence never becomes approval or Generation completion authority;
- Provenance never becomes source-fact authority;
- optional concepts/synchronizations remain optional unless a capability requires them;
- synchronization is occurrence-scoped, not permanently reactive;
- conceptual synchronization does not prescribe events, transactions, services, packages, queues, schemas or runtime call direction.

## Current next boundary

**Phase 010 — Concept Mapping, Interaction, Linguistic & Experience Alignment** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
