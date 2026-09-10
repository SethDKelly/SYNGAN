---
type: Problem / Concept Traceability
title: SYNGAN Concept-Justification Traceability
status: active
---

# SYNGAN Concept-Justification Traceability

## Purpose

Record the current Phase 008-B trace from SYNGAN's problem, actors, desired outcomes, and scale conditions to the distinct purpose of each accepted concept.

This document answers a narrow Jackson-design question:

> **Why does the full SYNGAN application currently need each accepted concept, and what problem-facing capability or safeguard would be lost if that concept were absent?**

It does **not** decide Jackson application inclusion dependence. A concept can be justified in the complete SYNGAN design without being required in every valid reduced application. Phase 009 will determine which concept subsets are meaningful and which concepts depend on which others for inclusion.

This traceability is governed by:

- [Problem & Purpose](problem-purpose.md);
- [Actors & Needs](actors.md);
- [Desired Outcomes](outcomes.md);
- [Enterprise Scale Envelope](enterprise-scale-envelope.md);
- [Accepted Concept Catalog](../concepts/index.md);
- [Concept Design Methodology](../authority/design-methodology.md).

## Current problem pressures

008-B consolidates the present problem into ten interacting pressures:

| Pressure | Problem-facing concern |
|---|---|
| P1 — Scale | Supported work must remain viable beyond one driver/local process. |
| P2 — Statistical/semantic complexity | Mixed types, ambiguity, constraints, skew, high cardinality, missingness, relationships, and text-bearing fields need explicit semantics. |
| P3 — Algorithm diversity | Different synthesis approaches have materially different capabilities and lifecycles. |
| P4 — Structured topology | Single-table, time-series, multi-table shared-key, and composed structured subjects must not be semantically flattened. |
| P5 — Operational lifecycle | Long-running distributed work needs durable operational identity, observability, recovery, cancellation, and uncertainty. |
| P6 — Evaluation plurality | Fidelity, utility, validity, privacy/disclosure risk, and other questions must remain separable. |
| P7 — Governance/traceability | Material states/results must remain attributable and historically interpretable. |
| P8 — Privacy/disclosure | Synthetic origin is not itself a privacy guarantee or release decision. |
| P9 — Dependency/egress | Supported enterprise profiles may require self-contained/offline/no-egress behavior with no hidden acquisition/fallback. |
| P10 — Portability/extensibility | Spark is the data environment, but one platform, runtime, algorithm, or extension must not redefine core semantics. |

## Current outcome set

The current desired-outcome authority contains sixteen outcomes:

```text
O1   Large-data viability
O2   Spark workflow continuity
O3   Explicit data meaning
O4   Multiple synthesis strategies
O5   Scalable generation
O6   Separable evidence of fitness
O7   No implicit privacy claim
O8   Reproducible and attributable work
O9   Observable long-running execution
O10  Recoverable enterprise operation
O11  Resource-responsible behavior
O12  Governable results and provenance
O13  Platform portability within the Spark ecosystem
O14  Extension without semantic erosion
O15  Structured-topology breadth without semantic flattening
O16  Self-contained text-bearing structured-data capability
```

O15 and O16 were made explicit in 008-B because later accepted design had already established those durable scope commitments while the original Phase 001 problem documents still described them as open or out of scope.

## Concept-purpose justification matrix

| Concept | Distinct current purpose | Principal actors served | Primary outcome trace | What is lost if absent? | 008-B verdict |
|---|---|---|---|---|---|
| **Data Meaning** | Establish, inspect, and revise descriptive semantic interpretation independently of physical type or model preprocessing. | Data Practitioner; Data Owner/Steward; Reviewer; Extension Author | O3, O6, O8, O12, O15, O16 | Ambiguous field, relationship, temporal, identifier, and text semantics become hidden in implementation/model behavior; historical work cannot state which interpretation it used. | **JUSTIFIED** |
| **Synthesis Strategy** | Make reusable synthesis behavior, capabilities, prerequisites, limitations, and configuration inspectable without making one algorithm universal semantics. | Data Practitioner; Platform Operator; Maintainer; Extension Author | O4, O11, O13, O14, O15, O16 | Algorithm/runtime assumptions leak into universal framework meaning; actors cannot reason about direct vs learned generation, topology/text capability, resources, or dependency/network differences before commitment. | **JUSTIFIED** |
| **Learning** | Own the semantic activity that derives reusable source-informed state when a Strategy requires it. | Data Practitioner; Maintainer; Extension Author; Operator | O1, O4, O8, O9, O10, O11, O12, O14, O16 | Reusable source-informed derivation collapses into a training job or model API call; source/meaning/Strategy/Constraint commitments and semantic completion become hidden inside operational execution. | **JUSTIFIED** |
| **Learned State** | Preserve reusable source-derived knowledge independently of the Learning occurrence, runtime object, or checkpoint that produced it. | Data Practitioner; Consumer; Reviewer; Maintainer | O4, O5, O8, O10, O12, O14, O16 | Reuse requires re-Learning or elevates a model/checkpoint/file into accidental domain authority; later Generation cannot select, compare, restrict, retire, or historically interpret reusable learned results independently. | **JUSTIFIED** |
| **Generation** | Define and fulfill an actor's intent to produce one logical synthetic-data result under explicit committed semantics and completion conditions. | Data Practitioner; Consumer; Steward; Reviewer | O1, O2, O5, O8, O10, O12, O15, O16 | The core product outcome becomes only a sampler invocation; requested quantity/scope/Conditions, direct vs learned basis, candidate vs completed result, topology-wide completion, and failure/cancellation semantics lose an owner. | **JUSTIFIED** |
| **Constraint** | Let authorized actors state reusable prescriptive rules independently of the Strategy/activity that may enforce or evaluate them. | Data Owner/Steward; Data Practitioner; Consumer; Reviewer | O3, O6, O8, O12, O14, O15 | Domain validity rules become hidden in generators, preprocessing, or metrics; different Strategies cannot share the same authoritative requirement and historical work cannot bind the exact rule revision. | **JUSTIFIED** |
| **Evaluation Criterion** | State and reuse the evaluative question/standard independently of the method used to examine it. | Data Practitioner; Consumer; Steward; Reviewer | O6, O7, O8, O14, O15, O16 | Available metrics silently define what “quality” means; fidelity, utility, validity, disclosure risk, relational/temporal correctness, or text-related questions cannot be separated cleanly from implementation methods. | **JUSTIFIED** |
| **Evaluation** | Own the committed examination method/lifecycle used to answer explicit Criteria under known scope, coverage, approximation, and uncertainty. | Data Practitioner; Consumer; Reviewer; Operator; Extension Author | O1, O6, O7, O8, O9, O10, O11, O14, O15, O16 | A metric/runtime result is mistaken for a valid examination; method assumptions, coverage, large-scale approximation, operational failure, and semantic completion lack a domain owner. | **JUSTIFIED** |
| **Evidence** | Preserve durable, interpretable findings independently of the Evaluation occurrence that established them. | Consumer; Data Practitioner; Steward; Reviewer | O6, O7, O8, O12, O14, O15, O16 | Findings collapse to ephemeral metric values; later actors cannot determine question, scope, uncertainty, claim strength, limitations, or whether an unfavorable/indeterminate result is still valid Evidence. | **JUSTIFIED** |
| **Execution** | Give operationally significant domain work a durable logical identity/lifecycle independent of platform jobs and physical retries. | Data Practitioner; Platform Operator; Maintainer; Extension Author | O1, O5, O8, O9, O10, O11, O13, O14 | Platform/job state becomes confused with Learning/Generation/Evaluation semantics; retries, recovery, cancellation, uncertain state, resource context, and multi-job realization cannot be explained without contaminating domain concepts. | **JUSTIFIED** |
| **Provenance** | Record and traverse typed historical relationships explaining how material states/results came to exist without becoming their current-state owner. | Consumer; Steward; Reviewer; Data Practitioner; Maintainer | O7, O8, O12, O14, O15, O16 | Historical derivation and exact binding relationships must be reconstructed from ad hoc metadata/logs or copied into domain objects; attribution, comparison, audit, and reproducibility context become unreliable. | **JUSTIFIED** |

## Important interpretation of the verdicts

`JUSTIFIED` means only that a distinct problem-facing purpose exists for the concept in the **complete current SYNGAN design**.

It does not mean:

- the concept's state/action specification is complete — 008-C/008-D own that;
- its operational principle is sufficient — 008-E owns that;
- its independence, genericity, or familiarity is finally proven — 008-F owns that;
- no rejected/deferred concept should return — 008-G owns that;
- the concept must appear in every valid SYNGAN subset — Phase 009 owns inclusion dependence;
- its existing architecture representation is final — Phase 013 owns that reconciliation.

## Outcome-to-concept coverage

This reverse mapping checks whether any desired outcome lacks a plausible conceptual basis. “Supporting concepts” below do not necessarily own the entire outcome; some outcomes also require downstream representation/architecture.

| Outcome | Primary conceptual support | Downstream realization still required? |
|---|---|---|
| **O1 Large-data viability** | Strategy, Learning, Generation, Evaluation, Execution | Yes — distributed/bounded representation and runtime realization. |
| **O2 Spark workflow continuity** | Generation plus Data Meaning/Strategy semantics | Yes — Spark-facing representation/mapping. |
| **O3 Explicit data meaning** | Data Meaning; Constraint where rules differ from description | Limited — actor-visible mapping still required. |
| **O4 Multiple synthesis strategies** | Synthesis Strategy; Learning/Generation | Yes — extension/runtime representation. |
| **O5 Scalable generation** | Generation, Strategy, Execution, Learned State where applicable | Yes — distributed output/runtime realization. |
| **O6 Separable evidence of fitness** | Evaluation Criterion, Evaluation, Evidence, Constraint | Yes — scalable Evaluation methods and mapping. |
| **O7 No implicit privacy claim** | Evaluation Criterion, Evaluation, Evidence, Provenance plus external release boundary | Yes — disclosure/security/experience mapping. |
| **O8 Reproducible and attributable work** | Provenance plus exact commitments across Data Meaning, Strategy, Learning, Learned State, Generation, Evaluation, Evidence, Execution | Yes — historical representation/reconstruction. |
| **O9 Observable long-running execution** | Execution synchronized with Learning/Generation/Evaluation | Yes — platform/runtime observation mapping. |
| **O10 Recoverable enterprise operation** | Execution plus stable domain commitments/results | Yes — recovery/fencing/persistence architecture. |
| **O11 Resource-responsible behavior** | Synthesis Strategy and Execution; activity-specific approximation semantics | Yes — admission/resource/runtime architecture. |
| **O12 Governable results and provenance** | Provenance, Evidence, Learned State, Generation, Learning | Yes — durable identity/history/disclosure representation. |
| **O13 Spark-platform portability** | Strategy and Execution boundaries prevent provider semantic ownership | Yes — portable architecture/platform adapters. |
| **O14 Extension without semantic erosion** | Strategy plus all singular concept boundaries/synchronizations; Provenance/Evidence/Execution guardrails | Yes — extension SPI/runtime conformance later. |
| **O15 Structured-topology breadth** | Data Meaning, Constraint, Strategy, Generation, Evaluation, Evidence | Yes — logical/physical topology representation. |
| **O16 Self-contained text-bearing data** | Data Meaning, Strategy, Learning/Learned State where applicable, Generation, Evaluation/Evidence | Yes — concrete supported Strategy/runtime later. |

No desired outcome is conceptually orphaned at 008-B.

## Actor-to-concept coverage

The current actor inventory also has no obvious unserved role at the purpose level:

- **Data Practitioner** — Data Meaning, Strategy, Learning, Learned State, Generation, Evaluation Criterion, Evaluation, Evidence, Execution, Provenance, and Constraints where applicable.
- **Synthetic Data Consumer** — Data Meaning/context, Generation result, Evaluation Criterion/Evaluation/Evidence, Provenance, Constraints, Learned State context where material.
- **Data Owner / Steward** — Data Meaning, Constraint, Evaluation Criterion/Evidence, Provenance, and Generation context.
- **Privacy / Risk / Governance Reviewer** — Criterion/Evaluation/Evidence, Provenance, Data Meaning/Constraint context; release/use approval remains external.
- **Platform Operator** — Execution and Strategy operational requirements, with domain activities providing semantic context.
- **Library Maintainer** — the full concept/synchronization boundary model, especially Strategy/Execution/Provenance for extensibility and historical behavior.
- **Synthesizer / Extension Author** — Strategy plus Learning/Generation/Evaluation integration semantics, Constraints, Execution, Evidence, and Provenance obligations.

This is purpose coverage, not a UI permission model.

## Purpose-overlap revalidation

008-B specifically retests the strongest apparent overlap pairs.

### Data Meaning vs Constraint

**No purpose collision found.**

Data Meaning answers what a subject means; Constraint states what valid output must obey. Structural relationship or temporal-role description remains different from required referential/temporal validity.

### Learning vs Learned State

**No purpose collision found.**

Learning is the source-informed derivation activity; Learned State is the reusable result that remains meaningful after the activity/Execution ends.

### Generation vs Execution

**No purpose collision found.**

Generation owns the requested synthetic-data outcome and semantic completion. Execution owns operational realization. A completed platform job cannot substitute for a completed Generation.

### Evaluation Criterion vs Evaluation vs Evidence

**No purpose collision found.**

They remain question → examination → durable finding. Collapsing them would allow an available metric or successful runtime call to define both the question and the supported claim.

### Evidence vs Provenance

**No purpose collision found.**

Evidence owns what an Evaluation established. Provenance owns typed historical relationships explaining how material states/results came to exist and relate.

### Strategy vs implementation/runtime

**No purpose collision accepted.**

Strategy remains reusable synthesis-behavior authority. Package/plugin/runtime binding is downstream representation and must not become the Strategy concept merely because it is how a method is loaded.

## Current scope reconciliation performed by 008-B

The problem authority had two material stale statements relative to later accepted design:

1. multi-table relational synthesis was still described as an unresolved future scope question;
2. text generation was stated too broadly as a non-goal, which conflicted with the later accepted requirement for self-contained free-form text fields inside structured data.

008-B reconciles those statements as follows:

- single-table, time-series, and multi-table shared-key generation are current structured-data capability targets;
- legitimate composite structured topology must remain representable;
- arbitrary recursive/cyclic graph synthesis is not a universal baseline promise;
- free-form/source-language text **inside structured data** is in scope;
- general unstructured/free-standing text generation remains out of scope;
- the supported baseline requires at least one self-contained source-derived/local text-capable path without hidden public-model acquisition or runtime inference;
- streaming/real-time serving remains outside the current baseline.

These are problem/scope corrections, not selections of algorithms, APIs, storage, package layout, or runtime mechanisms.

## Purpose gaps deliberately handed forward

008-B finds no immediate concept removal/addition required by problem-purpose traceability, but several boundaries must still be challenged later rather than treated as settled:

- **008-F** — whether all eleven names/forms are independently understandable and appropriately familiar/generic;
- **008-G** — whether Relationship, Generation Request, Condition, Attempt, Dataset/Artifact identity, Reproducibility, privacy-mechanism state, release/use decision, Source Characterization, Resource/Admission/Approximation/Recovery-like candidates remain correctly subordinate/deferred/external;
- **009** — which concepts are actually required together in reduced applications and what inclusion-dependence graph follows;
- **010** — whether actor-facing mappings can expose the distinctions cleanly without forcing conceptual change;
- **011** — whether whole-system specificity, integrity, synergy, or adversarial scenarios reveal purpose defects missed here.

## 008-B conclusion

At the problem/purpose level, the current eleven-concept catalog has complete positive justification coverage and no detected duplicate purpose requiring an immediate catalog change.

The problem authority itself required scope reconciliation, which 008-B performs. The current outcome set is now O1-O16, with O15/O16 making later topology/text commitments explicit at the problem layer.

The resulting state is:

```text
APPLICATION PROBLEM / PURPOSE          CURRENTLY CLOSED FOR PHASE 008
ACTOR NEED BASIS                       CURRENTLY CLOSED FOR PHASE 008
OUTCOME SET                            CURRENTLY CLOSED FOR PHASE 008
PROBLEM/OUTCOME → CONCEPT TRACEABILITY CURRENTLY CLOSED
11-CONCEPT PURPOSE JUSTIFICATION       PASS — NO CATALOG CHANGE IN 008-B
INDIVIDUAL CONCEPT BEHAVIOR            NOT YET REVALIDATED
JACKSON CONCEPT DESIGN                 NOT COMPLETE
IMPLEMENTATION READINESS               NOT READY
IMPLEMENTATION START                   NOT STARTED
IMPLEMENTATION NEXT                    NOT YET
```

Any later misfit may reopen this traceability under the J0-J7 discipline.