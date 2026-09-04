---
type: Discovery Knowledge Index
title: SYNGAN Concept Discovery
status: active
---

# Concept Discovery

This directory contains provisional design knowledge produced while discovering SYNGAN concepts.

Discovery artifacts are authoritative for the hypotheses and review decisions they record, but **they are not accepted concept specifications**. Candidates may still be renamed, exceptionally reclassified, or revised during Phase 001-H consolidation.

## Current 001-H handoff

The eleven candidates have now passed purpose, independence/genericity, operational-principle, and composition/synchronization review.

- [Candidate Operational Principles](operational-principles.md) — archetypal scenarios, owned state/actions, and synchronization pressure for each candidate.
- [Operational Principle Falsification Review](operational-principle-review.md) — confirms all eleven candidates survive 001-F and records narrowed boundaries.
- [Concept Composition & Dependency Model](composition-dependency-model.md) — authority-oriented composition graph, dependency classes, historical binding, direct-generation path, and cycle analysis.
- [Candidate Synchronization Specification](synchronization-specification.md) — fifteen provisional synchronization rules derived from the validated candidate set.
- [Composition, Coupling & Dependency Risk Review](composition-risk-review.md) — stress-tests hidden coordination, cycles, god-concept regression, infrastructure overreach, and future relational compatibility.

All eleven candidates are now **composition-validated but still provisional**. Phase 001-H is the first phase authorized to promote accepted concept authority into `docs/concepts/` and stable synchronization authority into `docs/synchronizations/`.

## Current candidate set

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

Removal or subordination of a candidate does not authorize loss of its semantic distinction.

## 001-G composition guardrails

The current handoff carries several non-negotiable composition results:

- state has one canonical concept owner;
- activities bind stable upstream revisions rather than subscribing to mutable authority;
- compatibility is contextual validation, not a global concept/state hub;
- Learning → Learned State and Evaluation → Evidence are production synchronizations;
- Generation may operate directly from Strategy when reusable Learned State is not required;
- domain activity semantic completion is separate from Execution operational completion;
- Attempt remains Execution-owned history;
- Provenance has high fan-in but low authority fan-out;
- reproducibility is assembled from stable concept-owned facts rather than duplicated configuration;
- stable dataset/artifact references remain infrastructure obligations;
- no permanent single-table conceptual invariant has been introduced.

## Phase 001-E / 001-F reduction history

- [Concept Review Criteria](concept-review-criteria.md) — tests for distinct purpose, independence, genericity, representation independence, synchronization economy, completeness, and operational-principle readiness.
- [Candidate Disposition Review](candidate-disposition-review.md) — reduction decisions from twenty candidates to eleven.
- [Reduced Candidate Set for 001-F](reduced-candidate-set.md) — the eleven-candidate set before operational-principle validation.
- [Completeness, Independence & Genericity Review](completeness-genericity-review.md) — confirms outcome/actor coverage after reduction.

`Synthesis Strategy` and `Evaluation Criterion` entered 001-F conditionally and both passed operational-principle testing with strict genericity boundaries.

## Phase 001-D discovery history

The following artifacts preserve the broader first-pass discovery hypotheses and remain useful provenance for why boundaries were tested:

- [Candidate Concept Catalog](candidate-concept-catalog.md) — original twenty purpose-driven candidates and confidence levels.
- [Boundary Hypotheses](boundary-hypotheses.md) — proposed separations, merger risks, and unresolved alternatives.
- [Synchronization Hypotheses](synchronization-hypotheses.md) — coordination needs implied by the original candidate set before later reduction/composition review.
- [Purpose / Outcome Coverage](purpose-outcome-coverage.md) — initial coverage matrix.

Earlier discovery artifacts MUST NOT be mistaken for the current handoff where later phases have recorded more recent dispositions.

## Authority boundary

Accepted concept specifications will live under `docs/concepts/` only after Phase 001-H consolidation.

Accepted cross-concept coordination knowledge will live under `docs/synchronizations/` only after 001-H decides which 001-G provisional synchronization rules are stable enough to promote.

No class, package, Spark job, PyTorch object, file format, API shape, storage scheme, event architecture, transaction mechanism, or plugin architecture may be inferred directly from the candidates in this directory.

See [Concept Design Methodology](../authority/design-methodology.md) and [Domain Terminology](../terminology/index.md).
