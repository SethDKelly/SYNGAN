---
type: Phase Record
title: 011-C — Familiarity, Reuse, Vocabulary & External-Model Comparison Audit
status: active
---

# 011-C — Familiarity, Reuse, Vocabulary & External-Model Comparison Audit

## Objective

Complete the dedicated Phase 011 familiarity/reuse audit after 011-B closed composed specificity.

011-C must decide whether the current eleven-concept vocabulary is understandable and reusable across the final application family without copying external product/object models or weakening current semantic distinctions.

---

## Governing authority

- [Design Quality Validation Authority](../../../authority/design-quality-validation-authority.md)
- [Composed Specificity, Purpose Alignment & Boundary Sharpness Audit](../../authority/composed-specificity-purpose-boundary-audit.md)
- [Concept Independence, Genericity, Familiarity & Reuse Normalization](../../concepts/independence-genericity-familiarity-reuse-normalization.md)
- [Linguistic Mapping, Vocabulary, Typed Status & Disclosure Semantics](../../../mapping/linguistic-mapping-vocabulary-typed-status-disclosure-semantics.md)
- [Ecosystem Compatibility Vocabulary](../../../terminology/ecosystem-compatibility.md)
- current concept/application-family/mapping authority

External sources are familiarity/counterexample evidence only under the 011-A `E8` rule.

---

## External analogue set

011-C compares the current design with familiar vocabulary from:

```text
SDV
Apache Spark ML
PyTorch — retained compatibility evidence
MLflow
Great Expectations
OpenLineage
```

The comparison is by conceptual job rather than word similarity.

The current official documentation was reviewed on 2026-09-16 where version-sensitive external terminology mattered.

---

## Primary result

```text
accepted concept names                         11
canonical names retained                       11 / 11
concepts requiring rename                      0
application-family vocabulary reuse            PASS
external-model comparison                      PASS
MAT-2 familiarity findings                     0
MAT-3 familiarity blockers                     0
upstream reopen                                NONE
R010-02                                        NO DEFECT — COMPATIBILITY GUIDANCE STRENGTHENED
B4 familiarity/reuse                           CURRENTLY CLOSED
G2 familiarity                                 CURRENTLY CLOSED
```

No concept, synchronization, application-family edge or Phase 010 mapping rule changes.

---

## Principal findings

### External bundles do not define SYNGAN boundaries

Several familiar systems deliberately package concerns that SYNGAN keeps independent:

```text
SDV Synthesizer
  ~= Strategy implementation + fit/Learning + trained state + sample/Generation + persistence

MLflow Run
  ~= one tracked code execution carrying metrics/artifacts/models

Great Expectations Expectation / Validation Result
  ~= assertion-oriented validation workflow and result

OpenLineage Job / Run / Dataset
  ~= external lineage/execution entities
```

Those models are useful for recognition/integration but do not demonstrate that SYNGAN should collapse its own boundaries.

### Familiarity is intentionally asymmetric

Accepted qualified compatibility forms include:

```text
fit / train            -> Learning when that concrete behavior applies
model                   -> Learned State analogue only for model-shaped state
sample                  -> Generation verb only when clearly synthetic production
validation result       -> Evidence analogue in validation-oriented cases
lineage                 -> derivational subset of Provenance
```

Terms that remain unsafe as generic aliases include:

```text
metadata
synthesizer
model
run
job
artifact
metric
expectation
validation
result
lineage
```

They may be used only with enough qualification to recover canonical ownership.

### Less conventional names remain justified

Three names have bounded first-use familiarity cost:

```text
Data Meaning
Learned State
Evaluation Criterion
```

But their familiar replacements introduce larger semantic errors:

```text
Data Meaning          != generic Metadata / physical Schema
Learned State         != universal Model / Artifact
Evaluation Criterion  != Metric / organizational Acceptance Criterion
```

Presentation may add explanatory glosses without renaming the concepts.

### Reuse remains stable across the application family

The vocabulary remains coherent for:

- authority-only members;
- direct Generation without Learning/Learned State;
- learned-state-assisted Generation;
- evaluation-focused family members;
- Execution-bearing and Execution-light variants;
- Provenance-bearing and Provenance-light variants;
- full composition.

No concept requires a different canonical name in different family members.

---

## Finding summary

```text
Q-FAM-001  canonical name set                    MAT-1 / M0 / NO DEFECT
Q-FAM-002  Model pressure on Learned State       MAT-1 / M0 / NO DEFECT
Q-FAM-003  Run/Job pressure on Execution         MAT-0 / M0 / NO DEFECT
Q-FAM-004  validation/metric/expectation cluster MAT-1 / M0 / NO DEFECT
Q-FAM-005  Lineage pressure on Provenance        MAT-0 / M0 / NO DEFECT
```

No `MAT-2` or `MAT-3` finding is produced.

---

## Durable authority changes

011-C creates/updates:

- [Familiarity, Reuse, Vocabulary & External-Model Comparison Audit](../../authority/composed-familiarity-reuse-vocabulary-external-model-audit.md) — current G2 authority;
- [Ecosystem Compatibility Vocabulary](../../../terminology/ecosystem-compatibility.md) — stronger current compatibility/alias/collision guidance and refreshed external source paths.

The compatibility-vocabulary update is additive semantic clarification. It does not reopen F3 linguistic mapping because it preserves the Phase 010-D owner-qualified vocabulary contract.

---

## Explicit non-decisions

011-C does not choose public APIs, public method names, UI copy, adapters, integration architecture, registry/tracking technology, lineage event schemas or platform mappings.

No current design conclusion requires implementation work.

---

## Completion decision

```text
011-C                              COMPLETE
B4 FAMILIARITY / REUSE             CURRENTLY CLOSED
G2 FAMILIARITY                     CURRENTLY CLOSED
R010-02                            NO DEFECT — COMPATIBILITY GUIDANCE STRENGTHENED
UPSTREAM REOPEN                    NONE
JACKSON CONCEPT DESIGN             NOT COMPLETE
IMPLEMENTATION READINESS           NOT READY
IMPLEMENTATION START               NOT STARTED
IMPLEMENTATION NEXT                NOT YET
```

## Handoff

**011-D — Integrity Under Synchronization, Correction, Invalidation & Historical Composition** is next eligible.
