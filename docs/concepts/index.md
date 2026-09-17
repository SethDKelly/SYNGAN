---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and normalized through Phase 008.

Cross-concept dependence/composition is consolidated by [Phase 009 Dependence, Application Family & Composition Consolidation](../authority/phase-009-dependence-composition-consolidation.md). Concept mapping is consolidated by [Phase 010 Concept Mapping Consolidation](../authority/phase-010-concept-mapping-consolidation.md). Current Phase 011 quality authority includes composed specificity, familiarity, integrity, synergy/simplicity/generic-fitness, scenario replay and hostile/degraded/provider stress validation.

## Accepted concepts

1. [Data Meaning](data-meaning.md)
2. [Synthesis Strategy](synthesis-strategy.md)
3. [Learning](learning.md)
4. [Learned State](learned-state.md)
5. [Generation](generation.md)
6. [Constraint](constraint.md)
7. [Evaluation Criterion](evaluation-criterion.md)
8. [Evaluation](evaluation.md)
9. [Evidence](evidence.md)
10. [Execution](execution.md)
11. [Provenance](provenance.md)

## Current concept/design state

```text
accepted concepts                    11
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
Phase 010                            COMPLETE
F1-F5 mapping                        CURRENTLY CLOSED
Phase 011                            ACTIVE
011-A                                COMPLETE
011-B                                COMPLETE
011-C                                COMPLETE
011-D                                COMPLETE
011-E                                COMPLETE
011-F                                COMPLETE
011-G                                COMPLETE
011-H                                NEXT ELIGIBLE
G1 composed specificity              CURRENTLY CLOSED
G2 composed familiarity              CURRENTLY CLOSED
G3 integrity                         CURRENTLY CLOSED
G4 synergy / simplicity              CURRENTLY CLOSED
G5 scenario / adversarial            CURRENTLY CLOSED
G6 future-scope                      STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
```

Phase 009 found no reason to add, remove, merge, split or rename a concept. Phase 010 found no mapping/composition reason to reopen that conclusion. 011-B through 011-G continue to retain the same eleven under specificity, familiarity, integrity, burden, scenario and hostile/provider stress.

## 011-G catalog stress result

No stress case exposes a missing current independent purpose/state/action lifecycle.

```text
stale / contradictory authority            PASS
concurrent / superseded work               PASS
regressive recovery / stale writer         PASS
runtime distribution closure               PASS
enterprise scale / approximation            PASS
multi-table / time-series pressure          PASS
text-bearing dependency pressure            PASS
provider job/run pressure                   PASS
provider lineage/catalog/model pressure     PASS
combined hostile composition                PASS
concept add/remove/merge/split              NONE
MAT-2 / MAT-3 findings                      0 / 0
```

Current repeated pressures still do **not** justify umbrella concepts such as:

```text
Workflow
Status
Validation / Quality
Artifact / Result
Recovery
Degraded Mode
Provider Job / Run
Model / Artifact
Lineage
Relationship / Topology
Text / Tokenizer
Privacy
Approval / Release Decision
```

Those concerns remain owned by existing concepts, cross-cutting contracts, external authority or future rediscovery triggers as appropriate.

## Provider/host boundary

Provider objects may be authoritative in their own domain, but current concept ownership remains:

```text
provider job/run          -> Execution correlation/evidence, not parent semantic owner
provider model/artifact   -> representation/integration fact, not Strategy/Learned State/result by default
provider lineage          -> possible Provenance evidence, not complete Provenance authority
provider catalog/schema   -> representation/metadata fact, not Data Meaning authority
provider identity/ACL     -> authorization input, not universal protected-action authority
```

Provider vocabulary never strengthens a SYNGAN claim merely by naming resemblance.

## Recovery / scale boundaries

No Recovery or Degraded Mode concept is required because current state remains owner-qualified and cross-cutting:

- restored state does not resurrect write authority;
- unresolved history remains unknown/partial rather than fabricated;
- resource pressure cannot silently weaken semantic commitment;
- approximation belongs to the concept whose semantics it changes;
- distributed runtime closure remains an operational compatibility condition rather than a new domain purpose.

## Core boundaries preserved

```text
Data Meaning          != Constraint
Synthesis Strategy    != implementation/plugin/runtime/provider model
Learning              != Learned State
Learning/Generation/
Evaluation             != Execution
Generation Condition  != Constraint
Evaluation Criterion  != Evaluation != Evidence
Evidence               != Provenance
Execution              != Attempt != platform job
```

Generation owns request/Condition and candidate-to-completed logical output semantics. Synthetic Output is not a separate concept. Reproducibility remains cross-cutting. Generic Privacy remains deferred pending mechanism-specific discovery. Use/Release Decision remains external authority.

## Application-family result

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Direct Generation remains valid without Learning/Learned State. Evaluation/Evidence are not universal prerequisites for Generation. Constraint, Execution and Provenance remain capability-conditional.

## Current next boundary

**011-H — Future-Scope, Extensibility, New-Capability Pressure & Rediscovery Triggers** is next eligible.

011-H may reopen discovery only when future pressure demonstrates a genuinely independent purpose + state + action/lifecycle, not merely an implementation/provider abstraction.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
