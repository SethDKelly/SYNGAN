---
type: Concept Dependence Index
title: SYNGAN Concept Dependence & Application Family
status: complete-current
---

# SYNGAN Concept Dependence & Application Family

This directory contains current Jackson-style inclusion-dependence and application-family authority for SYNGAN. Inclusion dependence remains distinct from implementation/runtime/reference dependencies.

## Current state

```text
Phase 009                         COMPLETE
D1-D4 / E1-E5                   CURRENTLY CLOSED
Phase 010-012                    COMPLETE
F1-H2                            CURRENTLY CLOSED
Jackson concept design            COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013                         COMPLETE
R1 architecture reconciliation    CURRENTLY CLOSED
Phase 014                         ACTIVE
Phase 014 sequencing authority  docs/phases/014/index.md
R2                                OPEN
R3                                OPEN
```

Phase 012 confirmed no dependence/application-family reopen, and Phase 013 preserved the resulting optionality in architecture.

## Canonical graph

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

Legitimate SCCs remain `L-CLUSTER = {Learning, Learned State}` and `E-CLUSTER = {Evaluation, Evidence}`.

## Application-family kernels

```text
L-KERNEL = Data Meaning + Synthesis Strategy + Learning + Learned State
G-KERNEL = Data Meaning + Synthesis Strategy + Generation
E-KERNEL = Evaluation Criterion + Evaluation + Evidence
```

Execution remains valid only with at least one realizable Learning/Generation/Evaluation activity. Provenance requires a meaningful relationship/history witness. Constraint remains capability-conditional.

Direct Generation remains valid without Learning/Learned State. Evaluation/Evidence are not universal Generation prerequisites.

## Current closure result

```text
universal inclusion edge change          NONE
SCC change                               NONE
conditional family rule change           NONE
new current family kernel                NONE
Phase 009 reopen                         NONE
```

Future M8 triggers do not establish family membership. Future independent-purpose scope must return to concept discovery before new inclusion edges or family rules are added.

Application-family validity remains distinct from SKUs, feature flags, package bundles, modules or deployment profiles.

## Phase 014 boundary

Phase 014 must test the dependence/application-family model as part of whole-design composition. In particular it must verify that current mapping and architecture do not force the full eleven-concept family into one universal workflow and that reduced valid applications remain semantically and architecturally supportable.

Inclusion edges must not be reinterpreted as module dependencies, services, transactions or deployment units.

## Current next boundary

Current Phase 014 subgroup sequencing is governed by [`docs/phases/014/index.md`](../phases/014/index.md).

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
