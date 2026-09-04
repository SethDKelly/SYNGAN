---
type: Phase Record
title: 001-E — Concept Criteria, Independence, Genericity & Completeness Review
status: complete
---

# 001-E — Concept Criteria, Independence, Genericity & Completeness Review

## Objective

Aggressively challenge the Phase 001-D candidate catalog and reduce it to the smallest set of independently purposeful concepts that still preserves SYNGAN's accepted actor needs, outcomes, enterprise-scale semantics, and protected domain distinctions.

This phase is intentionally adversarial toward the candidate catalog. Its goal is not to make all twenty candidates look defensible.

## Governing authority

This phase is governed by:

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Terminology Policy](../../authority/terminology-policy.md)
- [Problem Knowledge](../../problem/index.md)
- [Domain Terminology](../../terminology/index.md)
- [Phase 001-D Concept Discovery](../../discovery/index.md)

The current 001-E handoff remains provisional discovery knowledge under `docs/discovery/`. Accepted concept specifications are still intentionally absent from `docs/concepts/`.

## Scope

001-E covers:

- explicit concept review criteria;
- purpose and lifecycle independence;
- authority independence;
- genericity and anti-infrastructure review;
- representation-independence review;
- synchronization-cost review;
- outcome and actor completeness after reduction;
- candidate merge/subordination/reclassification/defer decisions;
- explicit operational-principle proof obligations for 001-F.

## Non-goals

001-E does not:

- finalize concept state/actions/invariants;
- establish final operational principles;
- promote provisional candidates to accepted concept specifications;
- define public Python APIs;
- choose Spark/PyTorch execution architecture;
- choose persistence or artifact formats;
- define a plugin architecture;
- introduce differential privacy or another privacy mechanism into scope;
- commit relational/multi-table synthesis to the first implementation boundary.

## Canonical discovery artifacts created

1. [Concept Review Criteria](../../discovery/concept-review-criteria.md)
2. [Candidate Disposition Review](../../discovery/candidate-disposition-review.md)
3. [Reduced Candidate Set for 001-F](../../discovery/reduced-candidate-set.md)
4. [Completeness, Independence & Genericity Review](../../discovery/completeness-genericity-review.md)

## Review criteria established

A candidate was tested for:

1. distinct purpose;
2. meaningful state/history;
3. meaningful actions/lifecycle;
4. independent change;
5. authority independence;
6. domain-specific genericity;
7. representation independence;
8. synchronization economy;
9. scale-semantic significance;
10. contribution to accepted outcomes;
11. non-duplication;
12. readiness for an independent operational principle.

The review explicitly rejects both maximal decomposition and maximal consolidation.

## Candidate reduction

001-D retained twenty candidates.

001-E carries **eleven** candidates into 001-F:

### Carry to 001-F

1. Data Meaning
2. Learning
3. Learned State
4. Generation
5. Constraint
6. Evaluation
7. Evidence
8. Execution
9. Provenance

### Carry conditionally to 001-F

10. Synthesis Strategy
11. Evaluation Criterion

Conditional means that 001-F MUST specifically prove an independent operational principle. If it cannot, the candidate should be subordinated or reclassified rather than preserved for catalog symmetry.

## Dispositions for removed standalone candidates

### Generation Request → subordinate to Generation

The distinction between requested output and execution/result remains important, but no independently valuable request lifecycle is currently established.

Generation should own pre-execution/request state such as amount, scope, conditions, relevant learned-state/strategy references, and applicable reproducibility/constraint requirements.

### Condition → subordinate to Generation

Condition remains semantically distinct from Constraint but currently exists to direct a specific Generation rather than satisfy its own independent purpose/lifecycle.

### Attempt → subordinate to Execution

Operators must be able to inspect retry/attempt history, but an attempt exists to realize one logical Execution. The distinction therefore belongs in Execution state/history unless later experience requirements show independently useful attempt operations.

### Artifact Identity → representation/integration contract

Stable references, durable locations, compatibility, and lifecycle metadata remain required. However, actors care primarily about Learned State, synthetic data, Evidence, or recovery state rather than a generic artifact identity service.

Later architecture must provide stable identity/reference contracts without creating a conceptual `Artifact` god-object.

### Reproducibility Contract → cross-cutting contract/policy

Reproducibility is a required inspectable contract spanning strategy, data/source identity, semantic versions, software/environment, seeds, execution, and comparison expectations.

It lacks sufficient independent actions/lifecycle to justify a standalone concept at this stage.

### Privacy Objective / Guarantee → reject generic concept; defer mechanism-specific discovery

A generic privacy concept is too heterogeneous. Differential privacy budgets, confidentiality policies, disclosure-risk thresholds, and de-identification claims do not share one coherent state/action model merely because they use the word privacy.

The design retains strict separation between formal privacy guarantees and empirical disclosure-risk evidence. If a supported mechanism introduces independently purposeful state/actions, it must receive mechanism-specific concept discovery.

### Dataset Identity → representation/integration contract

Stable logical dataset references remain necessary for provenance and reproducibility, but SYNGAN does not currently have a purpose to own general enterprise dataset cataloging or source lifecycle.

### Relationship → defer

Relational/multi-table semantics remain an intentional future edge. The current design must avoid single-table invariants, but current initial-scope evidence is insufficient to justify carrying Relationship into core operational-principle work.

### Use / Release Decision → external authority boundary

SYNGAN should produce evidence that organizational actors/systems can consume. It does not currently own the authority to approve downstream use or release.

## Source Characterization / Profile decision

001-D identified profiling as a possible missing candidate.

001-E does **not** add it as a standalone concept.

Source characterization currently serves other purposes:

- observations may inform Data Meaning inference;
- summaries may support strategy compatibility or Learning preparation;
- comparisons may be Evaluation methods producing Evidence.

Material observations that affect behavior must remain attributable and inspectable; they must not be hidden inside model-private preprocessing.

## Strong separations preserved

### Data Meaning vs Constraint

Retain separately because descriptive interpretation and prescriptive validity rules have different purposes and authorities.

### Learning vs Learned State

Retain separately because the activity can fail/retry while the reusable result can outlive the execution and support many generations.

### Learning / Generation / Evaluation vs Execution

Retain domain activities separately from operational lifecycle. Execution answers how long-running work is being realized; domain concepts answer why the work exists and what completion means.

### Evaluation vs Evidence

Retain separately because the activity and its durable result/context have different lifecycles.

### Evidence vs Provenance

Retain separately because Evidence answers what was observed; Provenance answers how material states/results came to exist and relate.

### formal privacy guarantee vs disclosure-risk evidence

This distinction remains mandatory even without a generic Privacy concept.

## Conditional candidate: Synthesis Strategy

Synthesis Strategy remains useful because practitioners and extension authors need to reason about method capability, requirements, configuration, compatibility, and limitations across different learning/generation activities.

However, it risks being only a plugin registry/configuration object.

### 001-F proof obligation

An operational principle must demonstrate actor-visible value for selecting/configuring/validating the strategy independently of one concrete Learning or Generation occurrence.

If the best principle is only "choose implementation class and pass options," Strategy should not survive as a concept.

## Conditional candidate: Evaluation Criterion

Evaluation Criterion remains useful because the question being asked can differ from the method used to answer it, and actors may define/reuse questions such as fidelity, utility, validity, or disclosure risk independently.

However, it may still be specification state owned by Evaluation.

### 001-F proof obligation

An operational principle must demonstrate independent actor value in defining/selecting/reusing/governing criteria across evaluations.

If criterion has no lifecycle outside a particular Evaluation request, it should become subordinate state while preserving the criterion/method distinction.

## Genericity conclusions

The surviving candidates are intentionally bounded:

- Data Meaning is not an enterprise metadata catalog;
- Synthesis Strategy is not a generic plugin registry;
- Learning is not a generic ML training system;
- Learned State is not a universal Artifact abstraction;
- Generation is not a generic batch workflow;
- Constraint is not a general policy engine;
- Evaluation is not a generic metrics platform;
- Evidence is not an enterprise evidence warehouse;
- Execution is not a workflow scheduler;
- Provenance is not a duplicate enterprise lineage/catalog database.

Genericity is accepted only where it follows naturally from synthetic-data purposes.

## Completeness assessment

After reduction, all fourteen outcomes from 001-B retain plausible ownership.

No lost purpose requires restoring a removed standalone candidate.

Important obligations remain explicit even when reclassified:

- stable dataset/artifact references;
- request and condition semantics;
- retry/attempt history;
- reproducibility scope;
- privacy guarantee/risk distinction;
- future relational compatibility;
- external decision authority;
- inspectable source characterization when it materially affects behavior.

## Anti-god-concept assessment

001-E continues to reject the following as concept boundaries:

- `Synthesizer = Strategy + Learning + Learned State + Generation + Evaluation + Execution`;
- `Metadata = Data Meaning + Constraint + Provenance + schema + artifact information`;
- `Quality = Criterion + Evaluation + Evidence + approval`;
- `Run = domain activity + logical Execution + Attempt + platform job`;
- `Model = model family + implementation + Learned State + persisted artifact`;
- `Privacy = guarantee + mechanism + risk evaluation + organizational release decision`.

## Exit criteria

001-E is complete when:

- [x] explicit candidate review criteria exist;
- [x] every 001-D candidate has a recorded disposition;
- [x] over-separated request/condition/attempt candidates are reduced without losing their semantics;
- [x] representation/integration responsibilities are distinguished from concepts;
- [x] external governance authority is kept outside the current product boundary;
- [x] generic privacy is rejected without weakening privacy discipline;
- [x] source profiling/characterization is explicitly reviewed rather than silently omitted;
- [x] genericity limits are documented for retained candidates;
- [x] all 001-B outcomes remain covered after reduction;
- [x] conditional candidates have explicit proof obligations;
- [x] no accepted concept specifications are created prematurely.

## Exit assessment

**Status: complete.**

The Phase 001-D catalog has been reduced from twenty candidates to eleven candidates worthy of operational-principle testing, with nine candidates explicitly subordinated, reclassified, deferred, rejected generically, or moved to an external authority boundary.

The resulting set is materially smaller while preserving the problem outcomes and important semantic separations.

## Next phase

**001-F — Operational Principle Development**

001-F should develop archetypal operational principles for each of the eleven retained candidates and use those principles as another falsification test. In particular, it must decide whether Synthesis Strategy and Evaluation Criterion survive their conditional status.

001-F should also ensure that subordinate semantics—Generation request/conditions and Execution attempts—appear naturally inside the operational principles of their owning concepts rather than disappearing from the design.
