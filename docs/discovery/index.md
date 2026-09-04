---
type: Discovery Knowledge Index
title: SYNGAN Concept Discovery History
status: historical
---

# SYNGAN Concept Discovery History

This directory preserves the hypotheses, alternatives, falsification tests, boundary reviews, operational-principle work, and composition analysis that produced the accepted Phase 001 model.

**It is no longer the current source of truth for accepted concept or synchronization semantics.**

Current authority:

- [Accepted Concepts](../concepts/index.md)
- [Accepted Synchronizations](../synchronizations/index.md)
- [Phase 001 Exit](../phases/001/001-H-phase-001-consolidation-initial-concept-catalog.md)

When an earlier provisional statement conflicts with accepted authority, accepted authority wins unless a later explicit design revision supersedes it.

## Final Phase 001 discovery handoff

The following documents supplied the direct evidence for 001-H:

- [Candidate Operational Principles](operational-principles.md)
- [Operational Principle Falsification Review](operational-principle-review.md)
- [Concept Composition & Dependency Model](composition-dependency-model.md)
- [Candidate Synchronization Specification](synchronization-specification.md)
- [Composition, Coupling & Dependency Risk Review](composition-risk-review.md)

These documents explain *why* the eleven accepted concepts and fifteen accepted synchronization rules survived.

## Accepted outcome of discovery

The following candidates were promoted to accepted concepts:

1. Data Meaning
2. Synthesis Strategy
3. Learning
4. Learned State
5. Generation
6. Constraint
7. Evaluation Criterion
8. Evaluation
9. Evidence
10. Execution
11. Provenance

See [docs/concepts](../concepts/index.md) for canonical definitions.

## Subordinate/reclassified results preserved by history

- Generation Request → Generation-owned state;
- Condition → Generation-owned state, distinct from Constraint;
- Attempt → Execution-owned history;
- stable dataset/artifact references → representation/integration obligation;
- reproducibility → cross-cutting contract;
- generic Privacy → rejected; mechanism-specific discovery when needed;
- Relationship → deferred relational edge;
- Use / Release Decision → external authority;
- Source Characterization/Profile → supporting observation/method.

## Earlier discovery layers

### Phase 001-E / 001-F

- [Concept Review Criteria](concept-review-criteria.md)
- [Candidate Disposition Review](candidate-disposition-review.md)
- [Reduced Candidate Set](reduced-candidate-set.md)
- [Completeness, Independence & Genericity Review](completeness-genericity-review.md)

### Phase 001-D

- [Candidate Concept Catalog](candidate-concept-catalog.md)
- [Boundary Hypotheses](boundary-hypotheses.md)
- [Synchronization Hypotheses](synchronization-hypotheses.md)
- [Purpose / Outcome Coverage](purpose-outcome-coverage.md)

These remain design provenance, not active concept authority.

## Representation boundary

Nothing in this historical directory directly defines Python classes, package modules, Spark jobs, PyTorch objects, file formats, storage schemes, event architectures, transaction mechanisms, or plugin architectures.
