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
- [011-F Archetypal / Exceptional Replay](../authority/archetypal-exceptional-progressive-disclosure-misfit-replay.md).
- [011-G Adversarial / Recovery / Scale / Provider Stress Validation](../authority/adversarial-degraded-recovery-scale-provider-semantic-leakage-validation.md) — **current stress revalidation**.

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
011-G                             COMPLETE
011-H                             NEXT ELIGIBLE
G1 specificity                    CURRENTLY CLOSED
G2 familiarity                    CURRENTLY CLOSED
G3 integrity                      CURRENTLY CLOSED
G4 synergy / simplicity           CURRENTLY CLOSED
G5 scenario / adversarial         CURRENTLY CLOSED
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

## Phase 011 family revalidation through 011-G

011-E confirms the application family is a primary simplicity mechanism. 011-F confirms all required family/capability histories remain truthful under archetypal/exceptional use. 011-G then stress-tests optionality under recovery, scale and provider pressure.

Stress consequences remain intact:

- direct Generation does not acquire Learning/Learned State because a provider calls an implementation object a `model` or `job`;
- Evaluation/Evidence do not become universal Generation prerequisites because a platform exposes generic validation/quality features;
- provider lineage capability does not make Provenance mandatory for variants that do not claim it;
- absence of Execution remains valid for Execution-light conceptual variants; provider jobs do not create a hidden universal Execution requirement at the concept-family level;
- a recovery condition does not add a Recovery concept to every family member;
- degraded capacity does not add a Degraded Mode concept;
- topology or text pressure does not add Relationship/Text/Tokenizer concepts merely to satisfy a provider/runtime representation;
- scale pressure cannot contract a committed family member's semantics by dropping included capabilities/requirements after commitment.

Current result:

```text
application-family edge change        NONE
conditional-family rule change        NONE
provider-driven inclusion edge        NONE
recovery-driven inclusion edge        NONE
scale-driven inclusion edge           NONE
catalog change                        NONE
R010-03                               NO DEFECT
R010-06                               NO DEFECT
R010-08                               NO DEFECT
```

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

## Future-scope boundary

011-H may refine capability-conditional family rules if a plausible extension can reuse existing concepts but needs a new inclusion condition. It must not add an edge merely because a provider/library implementation happens to bundle objects together.

A genuine new concept requires independent purpose + state + action/lifecycle evidence before application-family inclusion can be defined.

## Current next boundary

**011-H — Future-Scope, Extensibility, New-Capability Pressure & Rediscovery Triggers** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
