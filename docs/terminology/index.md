---
type: Terminology Index
title: SYNGAN Domain Terminology
status: active
---

# SYNGAN Domain Terminology

This directory is the canonical navigation layer for SYNGAN domain terminology established during Phase 001-C, interpreted for actor/programmatic mapping by Phase 010-D, and revalidated for composed familiarity/external-model compatibility by Phase 011-C.

Terminology here describes the problem/domain and compatibility vocabulary. It does not, by itself, establish that a term is an independent software concept, public API type, class, package, storage representation, execution primitive or runtime enum.

## Canonical documents

- [Domain Lexicon](domain-lexicon.md) — preferred domain terms and canonical meanings.
- [Semantic Distinctions](semantic-distinctions.md) — distinctions that MUST remain visible during later design.
- [Ecosystem Compatibility Vocabulary](ecosystem-compatibility.md) — current collision/alias guidance for SDV, Spark, PyTorch, MLflow, Great Expectations, OpenLineage and common ML/data vocabulary.
- [Term Status Register](term-status-register.md) — term maturity, ambiguity and concept-candidate signals without deciding concept boundaries.
- [010-D Linguistic Mapping Authority](../mapping/linguistic-mapping-vocabulary-typed-status-disclosure-semantics.md) — current actor/programmatic vocabulary, typed-status, disclosure and history-quality mapping authority.
- [011-C Familiarity / External-Model Audit](../history/authority/composed-familiarity-reuse-vocabulary-external-model-audit.md) — current composed familiarity/reuse authority.

## Governing authority

Terminology is governed by [Terminology Policy](../authority/terminology-policy.md).

Phase 010-D defines how canonical meanings may be expressed downstream without semantic collapse. Phase 011-C revalidates those choices against familiar external models without reopening F3.

## Semantic-layer rule

SYNGAN distinguishes four lexical layers:

1. **domain term** — names an idea in the synthetic-data problem space;
2. **candidate/accepted concept name** — names or hypothesizes an independent concept boundary;
3. **representation term** — names an implementation, storage, framework, runtime or API representation;
4. **compatibility term** — retained because an external ecosystem or user community commonly uses it.

A word MAY appear in more than one layer, but its meaning MUST be explicit when ambiguity could affect design. Shared spelling does not imply shared semantics.

## Current familiarity result

```text
accepted concept names                11
canonical names retained              11 / 11
B4 familiarity / reuse                CURRENTLY CLOSED
G2 familiarity                        CURRENTLY CLOSED
R010-02                               NO DEFECT — COMPATIBILITY GUIDANCE STRENGTHENED
```

No external model justifies renaming, merging or splitting a current concept.

Current one-way compatibility guidance includes:

```text
fit / train         -> qualified Learning verbs
model               -> qualified Learned State analogue when model-shaped
sample              -> Generation verb only when clearly synthetic production
validation result   -> qualified Evidence analogue
lineage             -> derivational subset of Provenance
run / job           -> external operational terms; qualify owner
artifact            -> physical material term, not semantic authority
metadata            -> external umbrella, not a Data Meaning synonym
metric              -> method/observation term, not Criterion/Evidence by itself
synthesizer         -> external/implementation aggregate, not a canonical concept
```

`Data Meaning`, `Learned State` and `Evaluation Criterion` retain their canonical names despite bounded first-use familiarity cost because common replacements introduce larger semantic distortion.

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

A canonical or compatibility term may carry a concept-candidate signal, but only accepted concept-design authority establishes an independent concept.

Phase 011-C found no familiarity/reuse reason to add, remove, split, merge or rename the eleven accepted concepts.

## Current next boundary

**011-D — Integrity Under Synchronization, Correction, Invalidation & Historical Composition** is next eligible.
