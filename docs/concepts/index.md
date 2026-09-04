---
type: Concept Catalog Index
title: SYNGAN Initial Accepted Concept Catalog
status: active
---

# SYNGAN Initial Accepted Concept Catalog

This directory contains the canonical concept specifications accepted at the end of Phase 001.

The concept catalog is authoritative for concept purpose, owned state/actions, invariants, and boundaries. Cross-concept coordination is authoritative under [Synchronizations](../synchronizations/index.md).

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

## Authority rule

These specifications replace the provisional candidate authority under `docs/discovery/` for the accepted concept boundaries. Discovery remains design history and provenance.

No Python class, Spark API, PyTorch object, storage format, job type, or package module is implied by one concept document.

## Deferred/non-concept responsibilities

The following remain intentionally outside the accepted standalone concept catalog:

- Generation Request and Condition — subordinate to Generation;
- Attempt — subordinate to Execution;
- stable dataset/artifact identity — representation/integration obligation;
- reproducibility — cross-cutting contract;
- privacy objectives/guarantees — mechanism-specific future discovery;
- Relationship — deferred relational-synthesis edge;
- Use / Release Decision — external authority boundary;
- Source Characterization/Profile — supporting observation/method.
