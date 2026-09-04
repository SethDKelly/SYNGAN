---
type: Discovery Knowledge Index
title: SYNGAN Concept Discovery
status: active
---

# Concept Discovery

This directory contains provisional design knowledge produced while discovering SYNGAN concepts.

Discovery artifacts are authoritative for the hypotheses and review decisions they record, but **they are not accepted concept specifications**. Candidates may still be split, merged, renamed, rejected, or reframed by later Phase 001 work.

## Current 001-F handoff

- [Candidate Operational Principles](operational-principles.md) — archetypal purpose/state/action scenarios for all eleven surviving candidates.
- [Operational Principle Falsification Review](operational-principle-review.md) — pass/fail analysis, conditional-candidate decisions, ownership guardrails, and 001-G stress tests.
- [Reduced Candidate Set](reduced-candidate-set.md) — the 001-E working set that entered operational-principle testing.
- [Candidate Disposition Review](candidate-disposition-review.md) — disposition of all twenty original 001-D candidates.
- [Completeness, Independence & Genericity Review](completeness-genericity-review.md) — actor/outcome coverage and genericity constraints after reduction.

All eleven 001-E candidates pass operational-principle testing. `Synthesis Strategy` and `Evaluation Criterion` resolve their prior conditional status to pass, but with strict genericity boundaries recorded in the 001-F review.

The eleven candidates now proceed to 001-G for composition/synchronization analysis:

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

They remain provisional until 001-G and 001-H complete.

## Subordinate and reclassified responsibilities

The following remain design obligations without standalone candidate status:

- Generation Request — requested/pre-execution state owned by Generation;
- Condition — request-specific state owned by Generation, semantically distinct from Constraint;
- Attempt — one concrete try preserved in Execution history;
- stable dataset/artifact references — representation/integration obligations;
- reproducibility — cross-cutting inspectable contract/policy;
- privacy objectives/guarantees — mechanism-specific future discovery rather than generic Privacy;
- Relationship — deferred relational-synthesis edge;
- Use / Release Decision — external governance authority;
- Source Characterization/Profile — attributable supporting observation/method rather than a standalone concept.

## Phase 001-E review history

- [Concept Review Criteria](concept-review-criteria.md) — tests for distinct purpose, independence, genericity, representation independence, synchronization economy, completeness, and operational-principle readiness.
- [Candidate Disposition Review](candidate-disposition-review.md) — reduction decisions from twenty candidates to eleven.
- [Reduced Candidate Set for 001-F](reduced-candidate-set.md) — the eleven-candidate set before operational-principle validation.
- [Completeness, Independence & Genericity Review](completeness-genericity-review.md) — confirms outcome/actor coverage after reduction.

## Phase 001-D discovery history

The following artifacts preserve the broader first-pass discovery hypotheses and remain useful provenance for why boundaries were tested:

- [Candidate Concept Catalog](candidate-concept-catalog.md) — original twenty purpose-driven candidates and confidence levels.
- [Boundary Hypotheses](boundary-hypotheses.md) — proposed separations, merger risks, and unresolved alternatives.
- [Synchronization Hypotheses](synchronization-hypotheses.md) — coordination needs implied by the original candidate set.
- [Purpose / Outcome Coverage](purpose-outcome-coverage.md) — coverage matrix used before reduction.

Earlier discovery artifacts MUST NOT be mistaken for the current candidate handoff where later phases have recorded more recent dispositions.

## Authority boundary

Accepted concept specifications will live under `docs/concepts/` only after Phase 001 has tested composition/synchronization and performed final consolidation.

No class, package, Spark job, PyTorch object, file format, API shape, storage scheme, or plugin architecture may be inferred directly from the candidates in this directory.

## Discovery discipline

A candidate survives because it demonstrates a distinct purpose, meaningful state/actions, actor value, and coherent operational principle—not because a glossary term, external library, or implementation framework exposes an object with the same name.

Removal or subordination of a candidate does not authorize loss of its semantic distinction. Condition remains distinct from Constraint even though Generation owns it; Attempt remains distinct from logical Execution even though Execution owns attempt history.

See [Concept Design Methodology](../authority/design-methodology.md) and [Domain Terminology](../terminology/index.md).
