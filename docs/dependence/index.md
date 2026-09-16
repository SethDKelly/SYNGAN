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
- [Phase 009 Consolidation](../authority/phase-009-dependence-composition-consolidation.md) — current dependence/composition consolidation authority.
- [Phase 010 Concept Mapping Consolidation](../authority/phase-010-concept-mapping-consolidation.md) — downstream validation that mapping preserves this authority.
- [011-B Composed Specificity Audit](../authority/composed-specificity-purpose-boundary-audit.md) — current downstream revalidation that reduced/full family members preserve distinct concept purposes.

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
011-C                             NEXT ELIGIBLE
G1 specificity                    CURRENTLY CLOSED
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

## Contraction / extension authority

```text
remove Data Meaning or Synthesis Strategy
  => Learning + Learned State + Generation cannot remain

remove Evaluation Criterion
  => Evaluation + Evidence cannot remain

remove one member of L-CLUSTER or E-CLUSTER
  => remove its mutual-inclusion partner
```

Removing Generation, Constraint, Execution or Provenance may be capability-only contraction where remaining rules hold.

Ordinary extension uses accepted concepts plus required closure/side conditions. Fresh discovery is reserved for genuinely new independent purpose/state/action lifecycles.

## Phase 010 validation result

Phase 010 preserves this family exactly rather than turning the eleven concepts into one mandatory workflow.

All ten required family/capability replays pass, including authority-only, L-KERNEL, direct G-KERNEL, learned-state-assisted Generation, E-KERNEL, evaluation-gated Generation, Constraint-aware, Execution-bearing/light, Provenance-bearing/light and full composition.

Controlling mapping rule:

> **Concept inclusion defines available capability; it does not require every included concept to be re-executed in every invocation.**

## 011-B specificity revalidation

011-B uses reduced family members as a direct test of whether concept purposes survive omission of common companions.

Result:

```text
authority-only members          PASS
L-KERNEL                        PASS
Direct G-KERNEL                 PASS
E-KERNEL                        PASS
Execution-bearing members       PASS
Provenance-bearing members      PASS
full eleven-concept member      PASS
specificity-driven edge change  NONE
catalog change                  NONE
G1 specificity                  CURRENTLY CLOSED
```

Important implications:

- the Learning/Learned State SCC remains a legitimate activity/result split rather than an artificial concept split;
- the Evaluation/Evidence SCC remains a legitimate examination/finding split;
- direct G-KERNEL demonstrates Generation is independently meaningful without learned or evaluation capability;
- Execution's one-of prerequisite strengthens its purpose boundary rather than making it a standalone scheduler;
- Provenance's witness prerequisite keeps it from becoming an empty lineage/metadata platform.

No Phase 009 dependence/application-family reopening is justified by 011-B.

## Product-scope documentation rule

A family member may remain coherent while losing a former advertised capability after contraction. Downstream mapping and representation must describe the actual included concepts/capabilities and remove stale promises.

Application-family validity remains distinct from product packaging or implementation modularity.

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

011-C may compare familiar external models/terminology against the current application family, but familiar product packaging, object graphs or API dependencies do not redefine Jackson inclusion dependence.

Later 011-D/G may reopen the smallest Phase 009 authority only if a genuine integrity/adversarial semantic defect is demonstrated.

## Current next boundary

**011-C — Familiarity, Reuse, Vocabulary & External-Model Comparison Audit** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
