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

- [Inclusion-Dependence Pairwise Inventory](inclusion-dependence-pairwise-inventory.md) — 009-A.
- [Inclusion-Dependence Graph & Ordering](inclusion-dependence-graph-ordering.md) — 009-B.
- [Application Family & Valid Subsets](application-family-valid-subsets.md) — 009-C.
- [Contraction / Extension Consequences](contraction-extension-consequences.md) — 009-D.
- [Phase 009 Consolidation](../authority/phase-009-dependence-composition-consolidation.md).
- [Phase 010 Concept Mapping Consolidation](../authority/phase-010-concept-mapping-consolidation.md).
- [011-E Synergy / Simplicity Audit](../authority/composed-synergy-simplicity-generic-fitness-burden-audit.md).
- [011-G Adversarial / Recovery / Scale / Provider Stress Validation](../authority/adversarial-degraded-recovery-scale-provider-semantic-leakage-validation.md).
- [011-H Future-Scope / Extensibility Audit](../authority/future-scope-extensibility-new-capability-rediscovery-audit.md) — **current extension/rediscovery revalidation**.

## Current phase state

```text
Phase 008                         COMPLETE
Phase 009                         COMPLETE
009-A..009-H                      COMPLETE
D1 inclusion-dependence graph     CURRENTLY CLOSED
D2 application family             CURRENTLY CLOSED
D3 explanation/design ordering    CURRENTLY CLOSED
D4 add/remove consequences        CURRENTLY CLOSED
E1-E5 composition                 CURRENTLY CLOSED
Phase 010                         COMPLETE
F1-F5 mapping                     CURRENTLY CLOSED
Phase 011                         ACTIVE
011-A..011-H                      COMPLETE
011-I                             NEXT ELIGIBLE
G1-G6                             CURRENTLY CLOSED
G7 residual misfit                PARTIAL — 011-I OWNS CLOSURE
```

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

## 011-H extension result

011-H revalidates Phase 009-D's distinction between ordinary extension and new-concept discovery.

Future capability pressure is classified as:

```text
F-1  fits existing concept unchanged
F-2  fits new state/action within existing purpose
F-3  requires new synchronization only
F-4  requires application-family capability refinement
F-5  requires genuine concept rediscovery
F-6  remains external authority / non-goal
F-7  insufficient evidence
```

Current likely extensions such as new Strategy families, richer structured topology, advanced text, new Evaluation methods, runtime/accelerator breadth and new source-derived Learned State forms require **no current inclusion-dependence change**.

Current result:

```text
universal inclusion edge change          NONE
SCC change                               NONE
conditional family rule change           NONE
new current family kernel                NONE
current new concept                      NONE
current new synchronization              NONE
R010-07                                  NO DEFECT
G6                                       CURRENTLY CLOSED
```

## Rediscovery before family redesign

When future scope introduces an independent product-facing purpose with durable state/history and independently meaningful actions/lifecycle, concept discovery happens **before** application-family edges are invented.

Known future `M8` triggers include:

- formal composable privacy/accounting;
- product-owned governance/release;
- independent output publication/versioning/retirement;
- independently reusable request/cohort definitions;
- independently governed graph/relationship state;
- durable streaming/session/feed state not reducible to bounded activities;
- product-owned economic/resource accounting;
- product-owned reusable knowledge/memory beyond Strategy/Learned State.

If a future concept is accepted, D1-D4 and relevant synchronizations must be designed afresh for that concept. No implementation bundle, plugin, feature flag, package extra or provider object determines those relations automatically.

## Synchronization-only / capability-refinement extensions

A future `F-3` synchronization candidate is valid only when existing concepts remain the owners, a genuinely new cross-concept relation is required, and the existing synchronization inventory cannot express it.

A future `F-4` application-family refinement is valid when current concepts remain sufficient but a newly advertised capability needs a more explicit optional inclusion/conditional-composition rule.

011-H finds no current case requiring either change.

## Product-scope documentation rule

A family member may remain coherent while losing a former advertised capability after deliberate contraction. Downstream mapping and representation must describe the actual included concepts/capabilities and remove stale promises.

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

**011-I — Residual Conceptual Misfit Register, Reopen/Defer/Accept Decisions & Closure Preparation** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
