---
type: Phase Record
title: 001-D — Candidate Concept Discovery & Boundary Hypotheses
status: complete
---

# 001-D — Candidate Concept Discovery & Boundary Hypotheses

## Objective

Derive a first-pass set of SYNGAN concept candidates from accepted purposes, actor needs, outcomes, scale consequences, and domain semantics without allowing implementation objects or glossary entries to dictate the concept model.

The phase also records candidate boundary and synchronization hypotheses so Phase 001-E can challenge the catalog rather than merely polish it.

## Governing authority

This phase is governed by:

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Terminology Policy](../../authority/terminology-policy.md)
- [Problem Knowledge](../../problem/index.md)
- [Domain Terminology](../../terminology/index.md)

Durable discovery hypotheses produced by this phase live under [Concept Discovery](../../discovery/index.md). They remain provisional and are not accepted concept specifications.

## Scope

001-D covers:

- purpose-driven concept candidate derivation;
- candidate purpose, state, actions, and motivating actor needs at hypothesis level;
- confidence/status for each candidate;
- explicit god-concept decomposition hypotheses;
- boundary alternatives and contested candidates;
- synchronization hypotheses;
- purpose/outcome/actor coverage checks;
- handoff tests for Phase 001-E.

## Non-goals

001-D does not:

- accept the final concept catalog;
- finalize concept names;
- fully specify state/actions/invariants;
- produce final operational principles;
- define public APIs or Python classes;
- select Spark ML abstractions;
- select model/training runtimes;
- choose persistence formats;
- define authorization or enterprise policy architecture;
- decide the initial implementation release scope for relational synthesis;
- decide formal benchmark limits.

## Canonical discovery artifacts created

1. [Concept Discovery Index](../../discovery/index.md)
2. [Candidate Concept Catalog](../../discovery/candidate-concept-catalog.md)
3. [Boundary Hypotheses](../../discovery/boundary-hypotheses.md)
4. [Synchronization Hypotheses](../../discovery/synchronization-hypotheses.md)
5. [Purpose / Outcome Coverage](../../discovery/purpose-outcome-coverage.md)

## Discovery method

Candidates were derived primarily from:

- distinct actor purposes in 001-B;
- observable outcome responsibilities;
- places where scale creates independent lifecycle/authority needs;
- distinctions established by 001-C;
- potential state that must outlive one operation or implementation object;
- coordination needs that would otherwise become hidden coupling.

The 001-C term-status register was used as a completeness cross-check only. High-signal vocabulary was not mechanically converted into concepts.

## First-pass candidate catalog

001-D retains twenty candidates at different confidence levels:

### Strong candidates

1. Data Meaning
2. Synthesis Strategy
3. Learning
4. Learned State
5. Generation Request
6. Generation
7. Constraint
8. Evaluation Criterion
9. Evaluation
10. Evidence
11. Execution
12. Provenance

### Moderate / contested candidates

13. Condition
14. Attempt
15. Artifact Identity
16. Reproducibility Contract
17. Privacy Objective / Guarantee

### Supporting / weak / edge candidates

18. Dataset Identity
19. Relationship
20. Use / Release Decision

These statuses are not acceptance grades. They describe how much independent-purpose evidence is visible before 001-E's stricter tests.

## Principal conclusions

### 1. A monolithic `Synthesizer` is currently a poor concept hypothesis

The problem evidence supports distinct purposes for at least:

- choosing/configuring a synthesis strategy;
- learning reusable source-informed state;
- identifying/reusing learned state;
- expressing desired generation output;
- producing synthetic data;
- evaluating outputs;
- controlling long-running execution.

An SDV-style or other API may later compose these into one ergonomic object, but that would be an experience/representation choice rather than evidence that they are one concept.

### 2. Data semantics appear independently purposeful

Data Meaning is currently a strong candidate because declared versus inferred interpretation has actor-visible value independent of any particular synthesis algorithm.

However, a generic `Metadata` concept is rejected at this stage because it would mix semantic, structural, provenance, artifact, constraint, and operational information.

### 3. Learning and Learned State should be tested as independent concepts

Learning is an activity with source inputs, lifecycle, failure, and diagnostics. Learned State is a reusable source-derived result that can survive learning completion and support multiple generations.

The distinction is especially important for retry/recovery and provenance at enterprise scale.

### 4. Generation intent deserves independent investigation

Output quantity, conditions, target semantics, and reproducibility intent can be meaningful before an execution begins.

Generation Request is therefore a strong candidate, though 001-E must test whether it should merge into Generation.

### 5. Conditions and constraints must remain semantically distinct

Even if Condition becomes subordinate to Generation Request, it must not merge semantically with Constraint.

A condition directs a requested population; a constraint states a rule output must satisfy.

### 6. Evaluation decomposes into question, activity, and evidence

The current discovery strongly supports separating:

- Evaluation Criterion — what property/question matters;
- Evaluation — the activity/method used to examine it;
- Evidence — the durable result/context that can support later claims or decisions.

This structure prevents metric implementations or aggregate scores from silently becoming generic fitness or governance authority.

### 7. Evidence is not decision authority

Use/release approval appears meaningful but may belong outside the core package.

SYNGAN should be capable of producing and preserving evidence without claiming that evidence itself authorizes a use, release, or privacy conclusion.

### 8. Long-running execution is likely a cross-cutting concept

Learning, Generation, and Evaluation can all be long-running and retryable.

Execution is therefore a strong candidate for shared lifecycle identity, progress, cancellation, failure, retry, and operational state.

However, 001-E must verify that a generic Execution concept does not erase meaningful workflow-specific semantics.

### 9. Attempt is semantically useful but may not be independent

The distinction between logical execution and one concrete try is important for retries, recovery, diagnostics, and provenance.

It remains unclear whether Attempt needs its own concept or should be structured state owned by Execution.

### 10. Artifact Identity is intentionally narrower than `Artifact`

The broad word `artifact` is too heterogeneous to define one concept. The candidate is narrowed to stable identity, lifecycle, compatibility, and resolution of durable outputs.

Learned State, synthetic datasets, evidence, and checkpoints retain their own meanings rather than becoming mere artifact subtypes conceptually.

001-E must still test whether artifact identity is functionality or representation infrastructure.

### 11. Provenance appears independently valuable but must remain relational/contextual

Provenance is a strong candidate for explaining derivation and execution context across concepts.

It must not duplicate the substantive state owned by every concept and thereby become a shadow data model of the entire framework.

### 12. Reproducibility may be better expressed as a contract/policy

Reproducibility has strong actor value but weak evidence of a standalone lifecycle.

001-E should specifically test whether Reproducibility Contract belongs as state/policy synchronized with Strategy, Learning, Generation, Evaluation, Execution, and Provenance rather than as an independent concept.

### 13. Privacy guarantee and disclosure-risk evidence must not merge

A formal privacy mechanism/objective and empirical disclosure-risk evaluation answer different questions.

Even if the generic Privacy Objective / Guarantee candidate is later decomposed or moved to a policy layer, the semantic separation from risk evidence is non-negotiable unless earlier authority is revised explicitly.

### 14. Dataset identity is needed conceptually, but ownership is unclear

Provenance requires stable references to source and synthetic datasets, yet SYNGAN should not accidentally become an enterprise data catalog.

Dataset Identity therefore remains a supporting candidate or integration contract rather than a strong core concept.

### 15. Relational support remains an intentional edge, not an accidental omission

Relationship remains a deferred candidate because multi-table initial scope is unresolved.

The concept design must avoid embedding assumptions that make one-table synthesis a permanent semantic invariant.

## Candidate synchronization structure

The current candidates imply explicit coordination such as:

- Data Meaning ↔ Strategy compatibility;
- Data Meaning + Strategy → Learning;
- Learning → Learned State;
- Learned State/Strategy → Generation Request validation;
- Condition → Generation Request;
- Constraint ↔ Learning/Generation/Evaluation;
- Generation Request → Generation;
- Generation → synthetic dataset/artifact identity;
- Criterion → Evaluation → Evidence;
- Evidence → external use/release decision boundary;
- privacy objective ↔ strategy/workflow and separately ↔ evaluation/evidence;
- Learning/Generation/Evaluation ↔ Execution;
- Execution → Attempt/checkpoint history;
- material transitions → Provenance;
- reproducibility expectations ↔ strategy/execution/provenance.

These are synchronization hypotheses, not final synchronization specifications.

## Candidate boundaries under greatest pressure

001-E should concentrate on:

1. Data Meaning vs structural schema/profile;
2. Strategy vs configuration/representation;
3. Generation Request vs Generation;
4. Condition vs Generation Request;
5. Execution vs workflow-specific lifecycle;
6. Execution vs Attempt;
7. Learned State vs Artifact Identity;
8. Dataset Identity vs Artifact Identity / external catalog identity;
9. Reproducibility Contract vs cross-cutting policy;
10. generic Privacy Objective / Guarantee vs mechanism-specific concepts;
11. Relationship vs Data Meaning/Constraint;
12. Evidence vs explicit Claim/Decision concepts.

## Potential missing candidate discovered

### Source Characterization / Profile

Source statistics and observations may support semantic inference, strategy compatibility, learning preparation, and evaluation.

001-D deliberately does **not** add a `Profile` candidate because its purpose may be derivative of Data Meaning or Evaluation rather than independently valuable.

001-E must test this omission explicitly so profiling does not later enter architecture as an unexamined hidden subsystem.

## God-concept decisions carried forward

001-D rejects the following as acceptable default concept boundaries:

- `Synthesizer` as strategy + learning + learned state + generation + persistence + evaluation + execution;
- `Metadata` as schema + semantics + identifiers + relationships + constraints + provenance + artifact description;
- `Quality` as criterion + metric + score + evidence + decision;
- `Run` as logical execution + concrete attempt + platform job;
- `Model` as model family + implementation + learned state + artifact.

A later experience or representation layer MAY intentionally expose convenient composites, but it must map those composites back to accepted concept responsibilities.

## Scale conclusions

The enterprise scale envelope materially strengthens the case for several candidate distinctions:

- Learning vs Learned State — durable results outlive expensive learning executions;
- Generation Request vs output — generated volumes may be large and asynchronous;
- Evaluation vs Evidence — evaluation itself may be distributed/expensive while evidence must remain reviewable;
- Execution vs Attempt — retries must preserve history rather than rewrite one opaque job state;
- Artifact/Dataset identity — outputs may be distributed data-plane objects rather than local return values;
- Provenance — source/configuration/execution context must survive long-running distributed work.

Scale does not by itself dictate Spark/PyTorch representations for these concepts.

## Coverage assessment

The candidate set provisionally covers all fourteen desired outcomes from 001-B.

That is a completeness signal only. The catalog likely contains over-separated candidates, particularly among operational/supporting responsibilities. Phase 001-E is expected to reduce, merge, or reclassify candidates where independent purpose cannot be defended.

## Exit criteria

001-D is complete when:

- [x] candidates are derived from purposes/actors rather than implementation objects;
- [x] each retained candidate has a purpose hypothesis;
- [x] candidate state/actions are sketched only far enough to test boundaries;
- [x] high-risk god-concepts are explicitly decomposed and challenged;
- [x] contested candidates remain visible rather than silently resolved;
- [x] synchronization needs are recorded as hypotheses;
- [x] actor/outcome coverage is checked;
- [x] potential omissions are identified;
- [x] relational scope remains visible without premature commitment;
- [x] no public API or package architecture has been selected;
- [x] accepted concept specifications have not yet been created.

## Exit assessment

**Status: complete.**

SYNGAN now has a purpose-driven candidate catalog with enough explicit alternatives and synchronization pressure to begin rigorous independence, genericity, and completeness review.

## Next phase

**001-E — Concept Criteria, Independence, Genericity & Completeness Review**

001-E should aggressively challenge every candidate, reduce over-separation, identify missing purposes, test whether candidates are generic without becoming abstract infrastructure, distinguish concepts from policies/representations/external systems, and produce a smaller set of concept candidates worthy of operational-principle development in 001-F.
