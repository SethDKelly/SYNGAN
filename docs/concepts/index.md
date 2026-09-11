---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and refined through current Phase 008 authority.

Cross-concept coordination is governed by [Synchronizations](../synchronizations/index.md), while inclusion-dependence/application-family work is governed by [Concept Dependence & Application Family](../dependence/index.md) and [Phase 009](../phases/009/index.md).

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

## Current catalog/composition state

```text
accepted concepts                       11
historical synchronization IDs          15
active synchronizations                 13
required-relational                      6
capability/occurrence conditional        7
missing current concept                 NONE FOUND
D1-D4                                   CURRENTLY CLOSED
E1                                      CURRENTLY CLOSED
E2                                      CURRENTLY CLOSED
```

No Phase 009 work through 009-F requires adding, removing, merging, splitting, or renaming a concept.

## Core boundary results

```text
Data Meaning          != Constraint
Synthesis Strategy    != implementation/plugin/runtime
Learning              != Learned State
Learning/Generation/
Evaluation             != Execution
Generation Condition  != Constraint
Evaluation Criterion  != Evaluation != Evidence
Evidence               != Provenance
Execution              != Attempt != platform job
```

Generation owns request/Condition and candidate-to-completed logical output semantics. Synthetic Output remains Generation-owned result state rather than a standalone concept.

## Current synchronization ownership result

009-F strengthens concept independence by making cross-concept ownership singular.

### Consuming activities

Learning, Generation and Evaluation own:

- exact reusable-authority/result bindings they commit to use;
- contextual compatibility/applicability/sufficiency assessments controlling their own lifecycle.

Reusable authorities are queried/bound, not mutated by consumers.

### Durable result concepts

```text
Learned State owns producing Learning identity
Evidence owns producing Evaluation identity
```

Producer activities own semantic completion. A reverse producer→result view may be derived instead of becoming duplicate mutable authority.

### Execution

Execution owns:

- exact parent activity binding;
- logical operational identity;
- Attempt history;
- retry/resume/recovery/cancellation/indeterminate operational state.

Learning/Generation/Evaluation do not absorb those semantics when Execution is present or absent.

### Provenance

Provenance owns typed assertions only. It does not own the concept facts it relates.

### Synchronization

No synchronization owns canonical state.

## SYNC-06 refinement and catalog boundary

`SYNC-06` is now conditional Generation/Learned State reuse compatibility/binding.

This reinforces existing boundaries:

```text
Generation owns reuse decision/binding
Learned State owns intrinsic result/restrictions
```

Direct Generation does not need Learned State and does not activate `SYNC-06`.

No intermediary Model/Artifact/Compatibility concept is introduced.

## Retired/reclassified IDs

`SYNC-08` remains retired because output promotion is Generation-local behavior and Output remains non-conceptual under current scope.

`SYNC-15` remains the cross-cutting Reproducibility Contract; no Reproducibility concept/state owner is introduced.

No `SYNC-16` is justified.

## Hidden-coordinator finding

009-F finds no missing concept behind synchronization for:

- Compatibility / Validation / Readiness;
- Workflow / Run;
- Promotion / Artifact;
- Quality / Approval;
- Reproducibility;
- Composition / Synchronization status.

If later design actually requires independent purpose/state/actions for such a candidate, rediscovery must reopen rather than creating shadow infrastructure authority.

## Future rediscovery triggers

Fresh Jackson-style discovery remains required before materially expanded scope such as:

- composable formal privacy/accounting;
- product-owned governance/release decisions;
- independently reusable/negotiable request or cohort definitions;
- independent synthetic-output publication/versioning/retirement/transformation lifecycle;
- arbitrary graph/recursive topology that creates independent relationship behavior;
- product-owned economic/resource allocation/budget/quota management.

Implementation objects, IDs, tables, services, manifests or status enums do not themselves justify a concept.

## Authority rule

No implementation resource or architecture dependency may redefine concept ownership or synchronization merely because it exists.

Synchronization trigger/precondition/postcondition semantics do not imply one package/module/service/event/transaction boundary.

## Current next boundary

**009-G — Composition Economy, Coupling, Synergy & Integrity Closure**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.