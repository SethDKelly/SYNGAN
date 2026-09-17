---
type: Concept Dependence Index
title: SYNGAN Concept Dependence & Application Family
status: complete-current
---

# SYNGAN Concept Dependence & Application Family

## Purpose

This directory contains current Daniel Jackson-style application inclusion-dependence and application-family authority for SYNGAN.

Inclusion dependence remains distinct from reference, validation, production, operational/runtime, provenance, persistence, synchronization, import or dataflow dependency.

For concepts `C1` and `C2`, the governing question is:

> **If `C1` is included in an application, does including `C1` make sense only if `C2` is also included?**

## Current authority

- [Inclusion-Dependence Pairwise Inventory](inclusion-dependence-pairwise-inventory.md)
- [Inclusion-Dependence Graph & Ordering](inclusion-dependence-graph-ordering.md)
- [Application Family & Valid Subsets](application-family-valid-subsets.md)
- [Contraction / Extension Consequences](contraction-extension-consequences.md)
- [Phase 009 Consolidation](../authority/phase-009-dependence-composition-consolidation.md)
- [Future-Scope / Extensibility Audit](../authority/future-scope-extensibility-new-capability-rediscovery-audit.md)
- [Residual Conceptual Misfit Register](../authority/residual-conceptual-misfit-register.md)

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
Phase 011                         ACTIVE
011-A..011-I                      COMPLETE
011-J                             NEXT ELIGIBLE
G1-G7                             CURRENTLY CLOSED
```

011-I finds no residual dependence/application-family defect and no Phase 009 reopen.

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

## Residual / future result

```text
universal inclusion edge change          NONE
SCC change                               NONE
conditional family rule change           NONE
new current family kernel                NONE
current new concept                      NONE
current new synchronization              NONE
Phase 009 reopen                         NONE
```

Likely Strategy, structured-topology, text, Evaluation, runtime/accelerator and source-derived reusable-state extensions fit existing purposes without current graph change.

When future scope introduces an independent product-facing purpose with durable state/history and independently meaningful actions/lifecycle, concept discovery happens **before** application-family edges are invented. M8 triggers therefore do not establish family membership now.

A future F-3 synchronization or F-4 family refinement must be justified semantically after the future capability is designed; package bundles, plugins, feature flags and provider object models are not application-family evidence.

## Product-scope documentation rule

A family member may remain coherent while losing a former advertised capability after deliberate contraction. Downstream mapping and representation must describe actual included concepts/capabilities and remove stale promises.

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

## Current next boundary

**011-J — Phase 011 Consolidation, G1-G7 Completion Decision & Phase 012 Handoff** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
