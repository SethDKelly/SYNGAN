---
type: Discovery Knowledge Index
title: SYNGAN Concept Discovery
status: active
---

# Concept Discovery

This directory contains provisional design knowledge produced while discovering SYNGAN concepts.

Discovery artifacts are authoritative for the hypotheses and review decisions they record, but **they are not accepted concept specifications**. Candidates may still be split, merged, renamed, rejected, or reframed by later Phase 001 work.

## Current 001-E handoff

- [Concept Review Criteria](concept-review-criteria.md) — tests for distinct purpose, independence, genericity, representation independence, synchronization economy, completeness, and operational-principle readiness.
- [Candidate Disposition Review](candidate-disposition-review.md) — disposition of all twenty 001-D candidates.
- [Reduced Candidate Set for 001-F](reduced-candidate-set.md) — current eleven-candidate working set for operational-principle development.
- [Completeness, Independence & Genericity Review](completeness-genericity-review.md) — confirms actor/outcome coverage after reduction and records genericity limits.

The reduced set contains nine direct carries and two conditional candidates. `Synthesis Strategy` and `Evaluation Criterion` must prove independent operational principles in 001-F or be further subordinated/reclassified.

## Phase 001-D discovery history

The following artifacts preserve the broader first-pass discovery hypotheses and remain useful provenance for why boundaries were tested:

- [Candidate Concept Catalog](candidate-concept-catalog.md) — original twenty purpose-driven candidates and confidence levels.
- [Boundary Hypotheses](boundary-hypotheses.md) — proposed separations, merger risks, and unresolved alternatives.
- [Synchronization Hypotheses](synchronization-hypotheses.md) — coordination needs implied by the original candidate set.
- [Purpose / Outcome Coverage](purpose-outcome-coverage.md) — coverage matrix used before reduction.

These 001-D artifacts MUST NOT be mistaken for the current candidate handoff where 001-E has recorded a later disposition.

## Current reduced candidate set

Candidates carried to 001-F:

1. Data Meaning
2. Synthesis Strategy — conditional
3. Learning
4. Learned State
5. Generation
6. Constraint
7. Evaluation Criterion — conditional
8. Evaluation
9. Evidence
10. Execution
11. Provenance

Standalone candidates removed from the working set remain semantically accounted for through subordination, cross-cutting contracts/policy, representation/integration contracts, deferred scope, mechanism-specific future discovery, or external authority boundaries.

## Authority boundary

Accepted concept specifications will eventually live under `docs/concepts/` only after Phase 001 has tested operational principles, composition, synchronization, and final consolidation.

No class, package, Spark job, PyTorch object, file format, API shape, or plugin architecture may be inferred directly from the candidates in this directory.

## Discovery discipline

A candidate survives because it appears to have a distinct purpose, meaningful state/lifecycle, independent actor need, or synchronization responsibility—not because a glossary term, external library, or implementation framework exposes an object with the same name.

Removal of a candidate does not authorize loss of its semantic distinction. For example, Condition remains distinct from Constraint even though Condition is now subordinate to Generation, and Attempt remains distinct from logical Execution even though it is now subordinate Execution history.

See [Concept Design Methodology](../authority/design-methodology.md) and [Domain Terminology](../terminology/index.md).
