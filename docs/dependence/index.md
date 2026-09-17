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
D1-D4                             CURRENTLY CLOSED
E1-E5                             CURRENTLY CLOSED
Phase 010                         COMPLETE
F1-F5                             CURRENTLY CLOSED
Phase 011                         COMPLETE
G1-G7                             CURRENTLY CLOSED
Phase 012                         COMPLETE
H1/H2                             CURRENTLY CLOSED
Jackson concept design            COMPLETE FOR CURRENT PRODUCT SCOPE
```

Phase 012's whole-current-state audit confirms no dependence/application-family reopen.

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

## Phase 013 boundary

Phase 013 must not translate inclusion edges mechanically into module dependencies, services, transactions or deployment units. Architecture must preserve semantic optionality without treating the full eleven-concept family as one mandatory runtime workflow.

## Current next boundary

**Phase 013 — Post-Concept Representation & Architecture Reconciliation** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
