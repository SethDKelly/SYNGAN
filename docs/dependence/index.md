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
- [011-B Composed Specificity Audit](../authority/composed-specificity-purpose-boundary-audit.md).
- [011-E Synergy / Simplicity Audit](../authority/composed-synergy-simplicity-generic-fitness-burden-audit.md) — **current reduced-family burden revalidation**.

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
011-A                             COMPLETE
011-B                             COMPLETE
011-C                             COMPLETE
011-D                             COMPLETE
011-E                             COMPLETE
011-F                             NEXT ELIGIBLE
G1 specificity                    CURRENTLY CLOSED
G2 familiarity                    CURRENTLY CLOSED
G3 integrity                      STRONG EVIDENCE / 011-G STRESS REVALIDATION REQUIRED
G4 synergy / simplicity           CURRENTLY CLOSED
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

The condensed graph is acyclic.

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

## Phase 011 revalidation through 011-E

011-B confirms each reduced member preserves distinct concept purpose. 011-C confirms stable vocabulary reuse. 011-D confirms optionality does not collapse under historical composition. 011-E then directly tests whether the family structure actually reduces conceptual burden.

Result:

```text
authority-only members            PASS — no synchronization burden
L-KERNEL                          PASS
Direct G-KERNEL                   PASS
E-KERNEL                          PASS
Constraint increments             capability-local
Execution increments              capability-local
Learned-State reuse               capability-local
Evidence gating                   capability-local
Provenance increments             relationship-local
full eleven-concept member        PASS without universal workflow
application-family edge change    NONE
catalog change                    NONE
R010-04                           NO DEFECT
G4                                CURRENTLY CLOSED
```

The application family is therefore a primary **simplicity mechanism** rather than merely a correctness constraint.

Important consequences:

- direct Generation does not pay Learning/Learned State burden;
- evaluation-only capability does not pay Generation burden;
- authority-only uses do not pay activity or synchronization burden;
- existing reusable authority/results may be selected without replaying their creation lifecycle;
- optional Constraint, Execution and Provenance do not create empty mandatory stages;
- full-suite membership does not imply all concepts are executed in every invocation.

No application-family contraction/extension rule is reopened by 011-E.

## Product-scope documentation rule

A family member may remain coherent while losing a former advertised capability after contraction. Downstream mapping and representation must describe the actual included concepts/capabilities and remove stale promises.

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

## Active Phase 011 boundary

011-F now replays archetypal and exceptional family-member histories to determine whether the progressive-disclosure mapping remains truthful in actual task sequences. 011-G later stress-revalidates integrity under hostile/degraded/recovery conditions.

A later finding may reopen the smallest Phase 009 authority only when a genuine semantic defect is demonstrated. UI convenience, package layout, feature flags or product packaging are not inclusion-dependence evidence.

## Current next boundary

**011-F — Archetypal, Exceptional & Progressive-Disclosure Misfit Replay** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
