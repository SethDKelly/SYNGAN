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
- [Concept Mapping Authority](../mapping/index.md) — current downstream consumer of synchronization semantics.

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

Later revision/status changes therefore do not silently rewrite exact historical bindings.

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
Phase 009                 COMPLETE
D1-D4                     CURRENTLY CLOSED
E1-E5                     CURRENTLY CLOSED
Phase 010                 ACTIVE
Phase 010 decomposition   COMPLETE
010-A                     NEXT ELIGIBLE
```

## Active Phase 010 mapping implications

Concept mapping must expose the distinctions synchronization preserves without turning them into implementation machinery.

010-A must make synchronization applicability/ownership available to the coverage model so later mappings can distinguish required-relational from capability/occurrence-conditional coordination.

Later mapping must preserve:

- semantic versus operational completion;
- candidate versus completed Generation output;
- exact authority/result bindings;
- Evidence finding versus approval/release authority;
- Provenance relation versus source ownership;
- conditional synchronization activation;
- current status versus historical binding truth;
- occurrence-scoped/non-reactive coordination;
- human/programmatic semantic parity.

No surface should expose a generic synchronization-owned `status`, `validation`, `quality`, `workflow` or `approval` state.

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

**010-A — Mapping Authority, Coverage Model, Actor/Surface Taxonomy & Evidence Baseline** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.