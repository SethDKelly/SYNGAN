---
type: Concept Dependence Index
title: SYNGAN Concept Dependence & Application Family
status: active
---

# SYNGAN Concept Dependence & Application Family

## Purpose

This directory contains current Jackson-style application inclusion-dependence and application-family authority for SYNGAN.

Inclusion dependence remains distinct from synchronization, runtime, import, storage, service, or dataflow dependency.

## Current authority

- [Inclusion-Dependence Pairwise Inventory](inclusion-dependence-pairwise-inventory.md) — 009-A.
- [Inclusion-Dependence Graph & Explanation Ordering](inclusion-dependence-graph-ordering.md) — 009-B.
- [Application Family & Valid Subsets](application-family-valid-subsets.md) — 009-C.
- [Contraction / Extension Consequences](contraction-extension-consequences.md) — 009-D.
- [Current Synchronization Authority](../synchronizations/index.md) — downstream composition authority.

## Current phase state

```text
Phase 009                         ACTIVE
009-A                             COMPLETE
009-B                             COMPLETE
009-C                             COMPLETE
009-D                             COMPLETE
009-E                             COMPLETE
009-F                             COMPLETE
009-G                             NEXT ELIGIBLE
D1 inclusion-dependence graph     CURRENTLY CLOSED
D2 application family             CURRENTLY CLOSED
D3 explanation/design ordering    CURRENTLY CLOSED
D4 add/remove consequences        CURRENTLY CLOSED
E1 synchronization inventory      CURRENTLY CLOSED
E2 synchronization ownership      CURRENTLY CLOSED
```

## Dependence / family result

The canonical direct universal graph remains:

```text
Learning      -> Data Meaning
Learning      -> Synthesis Strategy
Learning      -> Learned State
Learned State -> Learning

Generation    -> Data Meaning
Generation    -> Synthesis Strategy

Evaluation    -> Evaluation Criterion
Evaluation    -> Evidence
Evidence      -> Evaluation
```

Two legitimate SCCs remain:

```text
L-CLUSTER = { Learning, Learned State }
E-CLUSTER = { Evaluation, Evidence }
```

Canonical kernels remain:

```text
L-KERNEL = Data Meaning + Synthesis Strategy + Learning + Learned State
G-KERNEL = Data Meaning + Synthesis Strategy + Generation
E-KERNEL = Evaluation Criterion + Evaluation + Evidence
```

Execution and Provenance retain their non-binary family prerequisites.

## Handoff into current composition authority

009-E/F do not alter D1-D4.

Current composition summary:

```text
historical synchronization IDs          15
active synchronizations                 13
required-relational                      6
capability/occurrence conditional        7
SYNC-08                                  retired
SYNC-15                                  reclassified
SYNC-16                                  not justified
```

`SYNC-06` is currently conditional Generation/Learned State reuse coordination, so direct G-KERNEL does not acquire a new inclusion dependency on Learning/Learned State.

This is important: synchronization conditionality continues to preserve the direct-generation counterexample underlying the dependence graph.

## Ownership compatibility with dependence

009-F confirms that synchronization does not create new concept owners:

```text
consumer binding/assessment -> consuming activity
producer identity            -> Learned State / Evidence
operational parent binding   -> Execution
typed history assertion      -> Provenance
synchronization state        -> NONE
```

Therefore no synchronization result introduces a new inclusion-dependence edge or hidden concept.

## Current next boundary

**009-G — Composition Economy, Coupling, Synergy & Integrity Closure**.

Dependence/application-family authority remains reopenable only if 009-G exposes a genuine J2/J3 misfit.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.