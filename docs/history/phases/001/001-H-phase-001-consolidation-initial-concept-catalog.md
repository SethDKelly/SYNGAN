---
type: Phase Record
title: 001-H — Phase 001 Consolidation & Initial Concept Catalog
status: complete
---

# 001-H — Phase 001 Consolidation & Initial Concept Catalog

## Objective

Consolidate Phase 001 design knowledge, perform a final contradiction/completeness review, promote the validated concept and synchronization model into canonical authority, preserve discovery history, and define the proper Phase 002 concept-specification program.

## Governing authority

This phase is governed by:

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Terminology Policy](../../authority/terminology-policy.md)
- [Problem Knowledge](../../problem/index.md)
- [Domain Terminology](../../terminology/index.md)
- [Concept Discovery](../../discovery/index.md)
- [001-G Composition Analysis](001-G-concept-composition-synchronization-dependency-analysis.md)

## Consolidation result

Phase 001 accepts eleven initial SYNGAN concepts:

1. [Data Meaning](../../concepts/data-meaning.md)
2. [Synthesis Strategy](../../concepts/synthesis-strategy.md)
3. [Learning](../../concepts/learning.md)
4. [Learned State](../../concepts/learned-state.md)
5. [Generation](../../concepts/generation.md)
6. [Constraint](../../concepts/constraint.md)
7. [Evaluation Criterion](../../concepts/evaluation-criterion.md)
8. [Evaluation](../../concepts/evaluation.md)
9. [Evidence](../../concepts/evidence.md)
10. [Execution](../../concepts/execution.md)
11. [Provenance](../../concepts/provenance.md)

The canonical catalog is [docs/concepts/index.md](../../concepts/index.md).

Phase 001 also accepts fifteen core synchronization rules under [docs/synchronizations](../../synchronizations/index.md).

## Authority transition

Before 001-H, `docs/discovery/` was authoritative for provisional candidate decisions.

After 001-H:

- `docs/concepts/` is authoritative for accepted concept purpose, ownership, actions, invariants, and boundaries;
- `docs/synchronizations/` is authoritative for accepted cross-concept coordination;
- `docs/discovery/` remains authoritative only as design history, falsification evidence, alternatives considered, and provenance of the accepted model;
- phase records remain historical records and MUST NOT become competing concept specifications.

When accepted authority conflicts with an earlier provisional discovery statement, accepted authority wins unless a later explicit design revision supersedes it.

## Final contradiction review

No unresolved contradiction was found among the accepted problem, terminology, concept, and synchronization authorities that prevents Phase 001 exit.

The following tensions are resolved explicitly rather than left ambiguous:

### Spark-native vs implementation neutrality

SYNGAN's problem boundary remains Spark-native for enterprise data workflows, but no accepted concept is defined by Spark classes, Spark ML abstractions, a managed platform, or one execution mechanism.

### CTGAN relevance vs model neutrality

CTGAN remains an important potential Synthesis Strategy/implementation family, not the semantic definition of SYNGAN.

### distributed execution vs scalable semantics

Execution may be distributed, but scalability remains a claim against the enterprise scale envelope. Distribution alone is not treated as evidence of scalability.

### synthetic origin vs privacy

Synthetic origin remains distinct from formal privacy guarantees, disclosure-risk Evidence, and external release/use authority.

### metadata convenience vs concept ownership

`Metadata` remains an umbrella/compatibility term rather than a concept. Data Meaning, Constraint, Provenance, structural facts, and representation metadata retain distinct ownership.

### model convenience vs Learned State

`Model` remains overloaded compatibility vocabulary. Learned State is the accepted concept for reusable source-derived information.

### quality convenience vs evaluation authority

`Quality` remains umbrella vocabulary. Evaluation Criterion, Evaluation, and Evidence remain separate concepts.

### job/run convenience vs Execution

Execution is logical operational lifecycle; Attempt is subordinate history; physical platform jobs/runs remain representations.

## Accepted composition shape

The accepted model can be understood in four roles:

### Declarative authorities

- Data Meaning
- Synthesis Strategy
- Constraint
- Evaluation Criterion

### Domain activities

- Learning
- Generation
- Evaluation

### Durable domain results

- Learned State
- Evidence
- synthetic output references owned by Generation

### Orthogonal cross-cutting concepts

- Execution — operational lifecycle
- Provenance — historical derivation/context

These categories are explanatory groupings, not additional concepts.

## Subordinate/reclassified responsibilities retained

The following decisions are part of the accepted Phase 001 model:

- Generation Request is Generation-owned requested/pre-fulfillment state;
- Condition is Generation-owned directed-output state and remains distinct from Constraint;
- Attempt is Execution-owned retry/try history;
- stable dataset/artifact references are representation/integration obligations;
- reproducibility is a cross-cutting inspectable contract reconstructed from concept-owned facts;
- privacy mechanisms require mechanism-specific concept discovery when they introduce independent state/actions;
- Relationship remains deferred for future relational/multi-table scope;
- Use / Release Decision remains external governance authority;
- Source Characterization/Profile is supporting observation/method, not a standalone concept.

## Phase 001 invariants carried forward

Later phases MUST preserve these unless an explicit design revision changes Phase 001 authority:

1. ordinary enterprise workflows MUST NOT require full source-corpus driver/local materialization;
2. historical activities bind stable semantic/configuration revisions;
3. state has one canonical concept owner;
4. contextual compatibility results belong to the activity context, not globally mutable shared state;
5. Learning and Learned State remain distinct;
6. Generation may operate without Learning/Learned State for strategies that do not require reusable learned information;
7. Condition remains distinct from Constraint;
8. Evaluation Criterion, Evaluation, Evidence, and external decision authority remain distinct;
9. Execution completion does not define domain semantic completion;
10. Attempt remains distinct from physical platform job/run semantics;
11. Provenance has high fan-in but low authority fan-out;
12. synthetic data MUST NOT imply privacy or release safety;
13. reproducibility MUST be scoped and inspectable rather than casually equated with bitwise determinism;
14. accepted concepts MUST NOT be collapsed into `Synthesizer`, `Metadata`, `Model`, `Quality`, `Run`, `Artifact`, or generic `Privacy` god-concepts through implementation convenience;
15. the design MUST NOT introduce a permanent single-table conceptual invariant.

## Deferred design edges

Phase 001 intentionally leaves the following unresolved for later discovery/specification:

- relational/multi-table synthesis and a possible Relationship concept;
- mechanism-specific privacy concepts such as composable privacy-budget state;
- exact reproducibility levels and comparison tolerances;
- stable dataset/artifact reference representation;
- checkpoint representation and recovery mechanics;
- public API composition and ergonomic convenience objects;
- Spark ML integration;
- PyTorch/distributed model execution;
- model persistence formats;
- package/plugin architecture;
- benchmark methodology and formal scale SLOs.

These are not omissions from Phase 001; they are intentionally downstream or conditional design work.

## Phase 002 program derived from the accepted catalog

Phase 002 is **Concept Specification & Invariant Refinement**. It should deepen accepted concepts before experience/API/representation design.

Recommended groups:

| Group | Scope |
|---|---|
| **002-A** | **Data Meaning & Constraint Specification** |
| **002-B** | **Synthesis Strategy Specification & Capability Semantics** |
| **002-C** | **Learning & Learned State Specification** |
| **002-D** | **Generation Specification, Request/Condition Semantics & Output Completion** |
| **002-E** | **Evaluation Criterion, Evaluation & Evidence Specification** |
| **002-F** | **Execution, Attempt History, Failure & Recovery Semantics** |
| **002-G** | **Provenance, Reproducibility Contract & Historical Binding Specification** |
| **002-H** | **Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review** |

This subdivision follows the accepted concept model rather than implementation technologies.

## Phase 001 exit criteria

Phase 001 is complete when:

- [x] design/documentation authority is established;
- [x] problem, actors, outcomes, and enterprise scale envelope are explicit;
- [x] domain terminology and overloaded vocabulary are governed;
- [x] candidate concepts are discovered without implementation bias;
- [x] independence/genericity/completeness review is complete;
- [x] operational principles exist and pass falsification review;
- [x] composition/synchronization analysis finds no pathological authority coupling;
- [x] eleven concepts are promoted to accepted canonical authority;
- [x] stable synchronization rules are promoted to canonical authority;
- [x] discovery history is preserved without remaining the current concept source of truth;
- [x] terminology status is reconciled with accepted concept names;
- [x] deferred edges and external boundaries remain explicit;
- [x] Phase 002 is derived from the accepted catalog.

## Exit assessment

**Phase 001 status: complete.**

SYNGAN now has an accepted initial conceptual model that is sufficiently stable to begin detailed concept specification without selecting a Python package architecture or model/runtime representation.

## Next phase

**002-A — Data Meaning & Constraint Specification**

002-A should deepen the descriptive-vs-prescriptive boundary, state/revision models, authority semantics, applicability, inference/override behavior, and invariants required before these concepts are mapped to APIs or metadata representations.
