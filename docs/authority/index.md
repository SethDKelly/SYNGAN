---
type: Authority Index
title: SYNGAN Design Authority
status: active
---

# Design Authority

These documents define how SYNGAN design knowledge is created, interpreted, changed, and eventually implemented.

## Current methodology and governance

- [Concept Design Methodology](design-methodology.md)
- [Jackson Design Completion & Implementation Hold](jackson-design-completion-implementation-hold.md)
- [Jackson Methodology Completion Matrix](jackson-methodology-completion-matrix.md)
- [Documentation Governance](documentation-governance.md)
- [Terminology Policy](terminology-policy.md)
- [Source & Provenance Policy](source-provenance-policy.md)

## Current design authority chain

- [Problem Knowledge](../problem/index.md)
- [Accepted Concept Catalog](../concepts/index.md)
- [Phase 008 Individual-Concept Design Consolidation](../concepts/phase-008-individual-concept-consolidation.md)
- [Concept Dependence & Application Family](../dependence/index.md)
- [009-D Contraction & Extension Consequences](../dependence/contraction-extension-consequences.md)
- [Current Synchronization Authority](../synchronizations/index.md)
- [009-E Synchronization Inventory Revalidation](../synchronizations/application-family-revalidation.md)

## Current posture

```text
accepted concepts                    11
historical synchronization IDs       15
active synchronizations              13
current desired outcomes             16
Phase 008                            COMPLETE
Phase 009                            ACTIVE
009-A                                COMPLETE
009-B                                COMPLETE
009-C                                COMPLETE
009-D                                COMPLETE
009-E                                COMPLETE
009-F                                NEXT ELIGIBLE
D1-D4                                CURRENTLY CLOSED
E1                                   CURRENTLY CLOSED
E2-E3                                REVALIDATION REQUIRED
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Current composition result

The historical fifteen synchronization IDs now have these current dispositions:

```text
active required-relational            7
active capability/occurrence          6
retired concept-local                 1  SYNC-08
reclassified cross-cutting contract   1  SYNC-15
new synchronization                   0
SYNC-16                               NOT JUSTIFIED
```

`SYNC-08` semantics remain Generation-owned result lifecycle. `SYNC-15` semantics remain under the Reproducibility Contract. `SYNC-13` active internal scope is evidence-gated Generation consuming exact Evidence; external Evidence handoff is a later mapping/integration boundary.

Historical IDs remain reserved.

## Architecture boundary

The [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md) remains downstream evidence pending Phase 013 reconciliation.

Architecture may expose a counterexample but cannot define synchronization membership from imports, events, transactions, queues, persistence references, service calls, deployment topology, or runtime orchestration.

The active synchronization inventory MUST NOT be mirrored mechanically into technical topology.

## Remaining design sequence

```text
009-F  synchronization trigger / pre-post / ownership / hidden coordinator
009-G  composition economy / synergy / integrity
009-H  Phase 009 consolidation / Phase 010 handoff
010    concept mapping / interaction / language / experience
011    final concept-design quality / misfit
012    Jackson concept-design completion decision
013    representation / architecture reconciliation
014    whole-design completion / implementation-readiness decision
```

## Implementation-readiness rule

Phases 009-013 cannot make implementation ready. Only Phase 014 may set **READY / NOT STARTED / NEXT** after the whole design passes, and Phase 015 is still required before implementation begins.

## Current next boundary

**009-F — Synchronization Trigger, Preconditions/Postconditions, State Ownership & Hidden-Coordinator Audit**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
