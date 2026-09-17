---
type: Concept Dependence Index
title: SYNGAN Concept Dependence & Application Family
status: complete-current
---

# SYNGAN Concept Dependence & Application Family

## Purpose

This directory contains current Daniel Jackson-style application inclusion-dependence and application-family authority for SYNGAN.

Inclusion dependence remains distinct from reference, validation, production, operational/runtime, provenance, persistence, synchronization, import or dataflow dependency.

## Current authority

- [Inclusion-Dependence Pairwise Inventory](inclusion-dependence-pairwise-inventory.md)
- [Inclusion-Dependence Graph & Ordering](inclusion-dependence-graph-ordering.md)
- [Application Family & Valid Subsets](application-family-valid-subsets.md)
- [Contraction / Extension Consequences](contraction-extension-consequences.md)
- [Phase 009 Consolidation](../authority/phase-009-dependence-composition-consolidation.md)
- [Phase 011 Consolidation](../authority/phase-011-design-quality-misfit-consolidation.md)

## Current phase state

```text
Phase 009                         COMPLETE
D1 inclusion-dependence graph     CURRENTLY CLOSED
D2 application family             CURRENTLY CLOSED
D3 explanation/design ordering    CURRENTLY CLOSED
D4 add/remove consequences        CURRENTLY CLOSED
E1-E5 composition                 CURRENTLY CLOSED
Phase 010                         COMPLETE
F1-F5 mapping                     CURRENTLY CLOSED
Phase 011                         COMPLETE
G1-G7                             CURRENTLY CLOSED
H1/H2                             OPEN — PHASE 012
```

Phase 011 finds no residual dependence/application-family defect and no Phase 009 reopen.

## Canonical graph result

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

Transitive findings:

```text
Learned State -> Data Meaning
Learned State -> Synthesis Strategy
Evidence      -> Evaluation Criterion
```

Legitimate SCCs:

```text
L-CLUSTER = { Learning, Learned State }
E-CLUSTER = { Evaluation, Evidence }
```

The condensed graph remains acyclic.

## Application-family rule

A non-empty subset is coherent only if it:

1. is closed under the universal graph;
2. satisfies `Execution => Learning OR Generation OR Evaluation` when Execution is present;
3. gives Provenance a meaningful typed relationship/history witness when Provenance is present;
4. includes all concepts required by every advertised capability;
5. preserves accepted concept purposes/boundaries.

Canonical kernels:

```text
L-KERNEL = Data Meaning + Synthesis Strategy + Learning + Learned State
G-KERNEL = Data Meaning + Synthesis Strategy + Generation
E-KERNEL = Evaluation Criterion + Evaluation + Evidence
```

Authority-only coherent members include Data Meaning, Synthesis Strategy, Constraint and Evaluation Criterion independently.

## Phase 011 closure result

```text
universal inclusion edge change          NONE
SCC change                               NONE
conditional family rule change           NONE
new current family kernel                NONE
current new concept                      NONE
current new synchronization              NONE
Phase 009 reopen                         NONE
```

Future M8 triggers do not establish family membership now. Concept rediscovery must occur before future inclusion edges or family rules are invented for a genuinely new independent purpose.

Application-family validity remains distinct from product packaging, implementation modularity, SKUs, runtime feature flags or deployment profiles.

## Dependence-derived explanation ordering

```text
Data Meaning / Synthesis Strategy before Learning / Learned State
Data Meaning / Synthesis Strategy before Generation
Evaluation Criterion before Evaluation / Evidence
```

Within SCCs:

```text
Learning before Learned State
Evaluation before Evidence
```

This is explanation/design order, not implementation order or a mandatory runtime wizard.

## Phase 012 boundary

Phase 012 must verify this dependence/application-family authority against the current problem, concept catalog, synchronization inventory, mapping and Phase 011 quality results as one whole design.

## Current next boundary

**Phase 012 — Jackson Concept-Design Consolidation & Completion Decision** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
