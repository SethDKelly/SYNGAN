---
type: Authority Index
title: SYNGAN Design Authority
status: active
---

# SYNGAN Design Authority

These documents define how SYNGAN design knowledge is created, interpreted, changed, and eventually implemented.

## Current methodology and governance

- [Concept Design Methodology](design-methodology.md)
- [Jackson Design Completion & Implementation Hold](jackson-design-completion-implementation-hold.md)
- [Jackson Methodology Completion Matrix](jackson-methodology-completion-matrix.md)
- [Documentation Governance](documentation-governance.md)
- [Terminology Policy](terminology-policy.md)
- [Source & Provenance Policy](source-provenance-policy.md)
- [Design Quality Validation Authority](design-quality-validation-authority.md)
- [Composed Specificity, Purpose Alignment & Boundary Sharpness Audit](composed-specificity-purpose-boundary-audit.md)
- [Familiarity, Reuse, Vocabulary & External-Model Comparison Audit](composed-familiarity-reuse-vocabulary-external-model-audit.md)

## Current design authority chain

- [Problem Knowledge](../problem/index.md)
- [Accepted Concept Catalog](../concepts/index.md)
- [Phase 008 Individual-Concept Design Consolidation](../concepts/phase-008-individual-concept-consolidation.md)
- [Concept Dependence & Application Family](../dependence/index.md)
- [Synchronization Authority](../synchronizations/index.md)
- [Phase 009 Dependence, Application Family & Composition Consolidation](phase-009-dependence-composition-consolidation.md)
- [Concept Mapping Authority](../mapping/index.md)
- [Phase 010 Concept Mapping Consolidation](phase-010-concept-mapping-consolidation.md)
- [Design Quality Validation Authority](design-quality-validation-authority.md)
- [Composed Specificity Audit](composed-specificity-purpose-boundary-audit.md)
- [Composed Familiarity / External-Model Audit](composed-familiarity-reuse-vocabulary-external-model-audit.md)
- [Phase 011](../phases/011/index.md)
- [011 Entry & Decomposition](../phases/011/011-entry-decomposition.md)
- [011-A Phase Record](../phases/011/011-A-validation-authority-evidence-hierarchy-probe-taxonomy-misfit-reopen-rules.md)
- [011-B Phase Record](../phases/011/011-B-composed-specificity-purpose-alignment-boundary-sharpness-audit.md)
- [011-C Phase Record](../phases/011/011-C-familiarity-reuse-vocabulary-external-model-comparison-audit.md)

## Current posture

```text
accepted concepts                    11
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
D1-D4                                CURRENTLY CLOSED
E1-E5                                CURRENTLY CLOSED
Phase 010                            COMPLETE
010-A..010-H                         COMPLETE
F1-F5                                CURRENTLY CLOSED
concept mapping                      COMPLETE ENOUGH FOR PHASE 011
Phase 011                            ACTIVE
Phase 011 decomposition              COMPLETE
011-A                                COMPLETE
011-B                                COMPLETE
011-C                                COMPLETE
011-D                                NEXT ELIGIBLE
G1 specificity                       CURRENTLY CLOSED
G2 familiarity                       CURRENTLY CLOSED
G3 integrity                         PARTIAL TO STRONG
G4 synergy / simplicity              PARTIAL TO STRONG
G5 scenario / adversarial            PARTIAL TO STRONG
G6 future-scope                      STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
G7 residual misfit register          PARTIAL
Jackson design completion            IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Completed mapping authority

Phase 010 remains current upstream authority for actor/programmatic mapping:

```text
66 / 66 normalized command groups       SEMANTICALLY MAPPED
52 / 52 normalized query groups         SEMANTICALLY MAPPED
11 / 11 lifecycle/history envelopes     SEMANTICALLY MAPPED
5 / 5 explanation patterns              SEMANTICALLY MAPPED
11 / 11 concept names                   LINGUISTICALLY ALIGNED
66 / 66 commands                        PHYSICAL RESPONSIBILITY MAPPED
52 / 52 queries                         PHYSICAL RESPONSIBILITY MAPPED
10 / 10 family/capability replays       PASS
20 / 20 difficult-condition probes      PASS
```

Phase 011 may reopen the smallest affected mapping authority only when a concrete quality/misfit finding demonstrates that the current result is wrong or incomplete.

## Phase 011 validation authority

011-A establishes the common audit method for G1-G7.

The governing rule is:

> **Evidence may challenge any prior conclusion, but only a demonstrated semantic consequence can justify changing upstream design authority.**

Material findings use `MAT-0` through `MAT-3`; unresolved `MAT-3` conceptual blockers prevent positive Phase 011 exit. Misfit routing uses `M0-M8`, and any material upstream correction follows the smallest-authority reopen rule with bounded downstream revalidation.

## G1 composed specificity authority

011-B closes the dedicated current G1 audit:

```text
11 / 11 concepts               PASS composed specificity
reduced family replay          PASS
full anti-umbrella replay      PASS
MAT-2 findings                 0
MAT-3 blockers                 0
catalog changes                0
upstream reopens               0
R010-01                        NO DEFECT
G1 specificity                 CURRENTLY CLOSED
```

## G2 composed familiarity authority

011-C closes composed familiarity/reuse and B4 revalidation:

```text
11 / 11 canonical names retained
application-family vocabulary reuse     PASS
external-model comparison               PASS
MAT-2 findings                          0
MAT-3 blockers                          0
upstream reopens                        0
R010-02                                 NO DEFECT — COMPATIBILITY GUIDANCE STRENGTHENED
B4 familiarity / reuse                  CURRENTLY CLOSED
G2 familiarity                          CURRENTLY CLOSED
```

External vocabulary is explicitly compatibility-only unless its conceptual job matches current authority. Qualified mappings include `fit/train` to Learning, model-shaped `model` to Learned State, synthetic-production `sample` to Generation, validation result to Evidence and `lineage` to a derivational subset of Provenance. Generic `run`, `job`, `artifact`, `metadata`, `metric`, `validation`, `synthesizer` and similar terms do not become concept owners.

The [Ecosystem Compatibility Vocabulary](../terminology/ecosystem-compatibility.md) is the current durable collision/alias guide.

## Product-form boundary

SYNGAN remains a deployable Python/Spark package:

> **Agnostic across compliant Spark-capable hosting and infrastructure platforms.**

Package/SDK, notebook and embedded automation remain primary. CLI, reports, graphical/service surfaces and operator/admin presentation remain optional or host-integrated.

## Architecture boundary

The [Phase 007 Consolidated Architecture Contract](../architecture/phase-007-consolidated-architecture-contract.md) remains downstream evidence pending Phase 013 reconciliation.

Phase 011 may use architecture/code/provider models as counterexample, feasibility or familiarity evidence only. It does not select APIs, classes, persistence, widgets, services, packages, queues, event models, platform adapters or deployment topology.

## Remaining design sequence

```text
011-A  COMPLETE — validation authority / evidence / probes / reopen rules
011-B  COMPLETE — specificity / purpose alignment / boundary sharpness
011-C  COMPLETE — familiarity / reuse / vocabulary / external-model comparison
011-D  NEXT — integrity under synchronization / correction / invalidation / history
011-E..J remaining Phase 011 quality/misfit validation
012    Jackson concept-design completion decision
013    representation / architecture reconciliation
014    whole-design completion / implementation-readiness decision
---
015    implementation authority / controlled delivery — FUTURE ONLY
```

## Implementation-readiness rule

Only Phase 014 may set **READY / NOT STARTED / NEXT** after the whole design passes. Phase 015 is still required before implementation begins.

## Current next boundary

**011-D — Integrity Under Synchronization, Correction, Invalidation & Historical Composition** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
