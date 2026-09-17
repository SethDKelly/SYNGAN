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
- [011-E Synergy / Simplicity Audit](../authority/composed-synergy-simplicity-generic-fitness-burden-audit.md).
- [011-F Archetypal / Exceptional Replay](../authority/archetypal-exceptional-progressive-disclosure-misfit-replay.md) — **current family-history revalidation**.

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
011-F                             COMPLETE
011-G                             NEXT ELIGIBLE
G1 specificity                    CURRENTLY CLOSED
G2 familiarity                    CURRENTLY CLOSED
G3 integrity                      STRONG EVIDENCE / 011-G STRESS REVALIDATION REQUIRED
G4 synergy / simplicity           CURRENTLY CLOSED
G5 scenario / adversarial         STRONG EVIDENCE / 011-G STRESS REVALIDATION REQUIRED
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

## Phase 011 revalidation through 011-F

011-E confirms the application family is a primary simplicity mechanism rather than merely a correctness constraint.

011-F then replays all ten required family/capability histories through archetypal and exceptional branches:

```text
authority-only definition / reuse                 PASS
new Learning -> Learned State                     PASS
reuse existing Learned State -> Generation        PASS
direct Generation                                 PASS
Evaluation-only use                               PASS
evidence-gated Generation                         PASS
Constraint-aware Generation/Evaluation            PASS
Execution-bearing long-running work               PASS
Provenance-bearing historical explanation         PASS
full-capability composition                       PASS
```

Each scenario also passes a material exceptional branch.

Application-family consequences remain intact:

- direct Generation does not acquire a failed/missing Learning stage;
- existing Learned State may be reused without replaying Learning;
- evaluation-only use does not require Generation;
- optional Constraint, Execution and Provenance absence remains absence, not failure;
- full-capability membership does not imply all concepts are executed in each invocation;
- historical/current divergence does not change inclusion dependence.

No application-family edge or conditional rule is reopened by 011-F.

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

011-G now stress-revalidates the current family under adversarial/degraded/recovery/scale/provider pressure. A genuine defect may reopen the smallest Phase 009 authority, but a provider object graph, UI convenience, package layout, feature flag or product SKU is not inclusion-dependence evidence.

## Current next boundary

**011-G — Adversarial, Degraded, Recovery, Scale & Provider-Semantic-Leakage Validation** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
