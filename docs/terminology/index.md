---
type: Terminology Index
title: SYNGAN Domain Terminology
status: active
---

# SYNGAN Domain Terminology

This directory is the canonical navigation layer for SYNGAN domain terminology established during Phase 001-C and interpreted for actor/programmatic mapping by Phase 010-D.

Terminology here describes the problem domain. It does not, by itself, establish that a term is an independent software concept, public API type, class, package, storage representation, execution primitive or runtime enum.

## Canonical documents

- [Domain Lexicon](domain-lexicon.md) — preferred domain terms and canonical meanings.
- [Semantic Distinctions](semantic-distinctions.md) — distinctions that MUST remain visible during later design.
- [Ecosystem Compatibility Vocabulary](ecosystem-compatibility.md) — mappings and collision notes for SDV, Spark, PyTorch and common synthetic-data vocabulary.
- [Term Status Register](term-status-register.md) — term maturity, ambiguity and concept-candidate signals without deciding concept boundaries.
- [010-D Linguistic Mapping Authority](../mapping/linguistic-mapping-vocabulary-typed-status-disclosure-semantics.md) — current actor/programmatic vocabulary, typed-status, disclosure and history-quality mapping authority.

## Governing authority

Terminology is governed by [Terminology Policy](../authority/terminology-policy.md).

Phase 010-D does not replace the domain lexicon. It defines how canonical meanings may be expressed downstream without semantic collapse.

## Semantic-layer rule

SYNGAN distinguishes four lexical layers:

1. **domain term** — names an idea in the synthetic-data problem space;
2. **candidate/accepted concept name** — names or hypothesizes an independent concept boundary;
3. **representation term** — names an implementation, storage, framework, runtime or API representation;
4. **compatibility term** — retained because an external ecosystem or user community commonly uses it.

A word MAY appear in more than one layer, but its meaning MUST be explicit when ambiguity could affect design. Shared spelling does not imply shared semantics.

## Current linguistic mapping rule

> **Words may simplify presentation, but they may not erase ownership, semantic dimension, historical scope, uncertainty or disclosure meaning.**

Accordingly, terms such as `model`, `run`, `job`, `artifact`, `metric`, `metadata`, `validation`, `valid`, `passed`, `ready`, `quality`, `safe`, `private`, `reproducible`, `current`, `latest` and `complete` require qualification where ambiguity matters.

No global Status, Validation, Quality, Run, Artifact, Metric, History, Lineage or Approval authority is implied by those words.

## Typed-status discipline

Phase 010-D keeps distinct:

```text
revision/current-use status
semantic activity lifecycle
contextual assessment
Execution/Attempt operational lifecycle
Generation material finality
Evidence finding / claim strength
Constraint handling / applicability
Disclosure state
historical-knowledge quality
```

These semantic types may later map to different physical representations. They are not a requirement for one universal enum hierarchy.

## Disclosure / history language

Preferred disclosure meanings are:

```text
visible
authorized summary / redacted
withheld
unavailable
unknown
absent
```

`not applicable` is separate from absence.

Historical-knowledge language is:

```text
directly retained
reconstructed
partial / incomplete
history unavailable
history indeterminate
```

Disclosure and history quality remain orthogonal.

## Concept-discovery boundary

A canonical term may carry a concept-candidate signal, but only the accepted concept-design authority establishes an independent concept.

Phase 010-D found no linguistic reason to add, remove, split, merge or rename the eleven accepted concepts.
