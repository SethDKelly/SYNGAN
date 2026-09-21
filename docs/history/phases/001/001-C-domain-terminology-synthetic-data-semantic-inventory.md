---
type: Phase Record
title: 001-C — Domain Terminology & Synthetic-Data Semantic Inventory
status: complete
---

# 001-C — Domain Terminology & Synthetic-Data Semantic Inventory

## Objective

Establish precise, implementation-neutral language for the synthetic-data problem space before candidate concepts are proposed.

The phase exists to prevent vocabulary inherited from SDV, Spark, PyTorch, statistics, or ordinary ML practice from silently determining SYNGAN's concept boundaries.

## Governing authority

This phase is governed by:

- [Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Terminology Policy](../../authority/terminology-policy.md)
- [Source & Provenance Policy](../../authority/source-provenance-policy.md)
- [Problem Knowledge](../../problem/index.md)

Durable terminology produced by this phase lives under [Domain Terminology](../../terminology/index.md). This phase record preserves history and conclusions rather than acting as a parallel glossary.

## Scope

001-C covers:

- preferred domain vocabulary;
- overloaded and ambiguous terms;
- important semantic distinctions;
- external ecosystem terminology collisions;
- term maturity/status;
- concept-candidate signals for later investigation;
- lexical guardrails for 001-D and later phases.

## Non-goals

001-C does not:

- accept the final concept catalog;
- establish one concept per defined term;
- select public API names;
- choose Python classes or package modules;
- adopt Spark ML abstractions;
- select model families;
- define persistence formats;
- decide whether relational/multi-table synthesis is in the initial implementation release;
- define privacy guarantees or algorithms.

## Canonical artifacts created

1. [Domain Terminology Index](../../terminology/index.md)
2. [Domain Lexicon](../../terminology/domain-lexicon.md)
3. [Semantic Distinctions](../../terminology/semantic-distinctions.md)
4. [Ecosystem Compatibility Vocabulary](../../terminology/ecosystem-compatibility.md)
5. [Term Status Register](../../terminology/term-status-register.md)

## Principal conclusions

### 1. Domain terms, concept names, and representation names are different lexical layers

A domain term names something meaningful in the problem space.

A candidate concept name hypothesizes an independent functional boundary.

A representation term names an API, framework, storage, runtime, or implementation mechanism.

A compatibility term may be retained because an external ecosystem uses it.

Shared spelling does not collapse these layers.

### 2. `metadata` is too broad to be presumed one concept

The term may encompass structural schema, semantic meaning, identifiers, relationships, constraints, execution description, artifact description, or other descriptive information.

SYNGAN will use more specific terminology when responsibility matters. 001-D must investigate which descriptive responsibilities are independently purposeful rather than beginning from a monolithic `Metadata` class/object assumption.

### 3. `synthesizer` is compatibility vocabulary, not yet a concept boundary

Libraries such as SDV commonly expose one synthesizer object that owns metadata configuration, fitting, learned state, sampling, and persistence behavior.

SYNGAN does not assume that these responsibilities form one concept merely because an established API packages them together.

The preferred domain vocabulary distinguishes synthesis, synthesis strategy, learning, learned state, generation, and artifacts.

### 4. `model` is too overloaded to carry unqualified design authority

`Model` can mean a mathematical family, a neural-network definition, learned parameters, an executable runtime object, a Spark ML `Model`, or a persisted file.

Where the intended meaning is source-derived reusable information, SYNGAN prefers `learned state`.

Where the intended meaning is an approach family, it prefers `model family` or `synthesis strategy` as appropriate.

### 5. generation and source sampling require separate language

Synthetic-data libraries often use `sample` to mean create new synthetic records, while Spark/statistics also use sampling to mean select observations from data that already exists.

SYNGAN domain documents therefore prefer `generate` for producing synthetic data and qualify source/evaluation sampling when subset selection is intended.

This is a semantic decision, not yet a public API decision.

### 6. learning, training, and fitting are not universal synonyms

`Learning` is the neutral domain activity of deriving reusable source-informed state.

`Training` is a form of learning involving iterative/optimization-based parameter adjustment.

`Fit` remains compatibility/API vocabulary and may cover several learning strategies.

This prevents a neural-training lifecycle from being imposed on statistical, rule-based, sketch-based, or future strategies.

### 7. condition, constraint, and filter must remain distinct

A condition requests characteristics during generation.

A constraint states a rule output must satisfy.

A filter selects records after they already exist.

A future implementation may use one mechanism to assist another, but cannot silently change the externally meaningful semantics.

### 8. quality is plural and `quality` is an umbrella word

The domain lexicon distinguishes at least fidelity, utility, validity, privacy, and disclosure risk.

The phase also separates criteria, metrics, scores, evidence, claims, and decisions.

This prevents a single metric or aggregate score from silently becoming authority for release, privacy, or downstream fitness.

### 9. synthetic, anonymized, private, and low-risk are different claims

Synthetic origin is a provenance/property statement about how data was produced.

Anonymization, privacy guarantees, and disclosure-risk conclusions require separate definitions, scope, mechanism, threat models, policies, or evidence as applicable.

### 10. execution vocabulary must support recovery semantics

The phase distinguishes logical execution from an individual attempt and distinguishes checkpoints from final artifacts.

This vocabulary preserves room for retries, resumability, partial failure, cost attribution, and provenance without prematurely selecting a Spark/job orchestration representation.

### 11. provenance is broader than lineage

Lineage describes derivational relationships among data or artifacts.

Provenance can additionally describe configuration, software identity, execution circumstances, authority/actor context, and evidence history.

### 12. reproducibility is not the same as determinism

A stochastic or distributed strategy may have a meaningful reproducibility contract without producing bit-identical outputs.

Later design must state the intended reproducibility scope instead of casually promising determinism.

### 13. distributed does not mean scalable

A distributed implementation can still contain driver bottlenecks, unbounded shuffles, corpus-growing coordinator state, unacceptable evaluation cost, or impractical artifact behavior.

`Scalable` is therefore a claim that requires an explicit workload envelope and required behavioral scope.

### 14. Spark-native does not mean Spark-only

SYNGAN's Spark-native objective means natural participation in PySpark/Spark DataFrame workflows and no ordinary requirement for full-corpus driver-local materialization.

It does not require every mathematical operation to be implemented in Spark primitives or prohibit specialized external runtimes/accelerators when later architecture justifies them.

## High-risk terminology clusters

001-C identified five clusters especially likely to produce accidental god-concepts:

1. **metadata cluster** — schema, semantics, identifiers, relationships, constraints;
2. **synthesizer cluster** — strategy, learning, learned state, generation;
3. **quality cluster** — criteria, metrics, fidelity, utility, validity, privacy/disclosure risk;
4. **execution cluster** — logical execution, attempts, checkpoints, artifacts, provenance;
5. **privacy cluster** — privacy objectives/guarantees, disclosure-risk evaluation, anonymization claims.

001-D MUST examine these clusters through purpose and independence rather than preserve or split them mechanically.

## Ecosystem observations

### SDV

Current SDV terminology provides useful compatibility evidence:

- metadata describes tables, columns, data types, and relationships and is treated as ground truth;
- synthesizer APIs typically accept metadata and expose `fit` plus `sample`;
- both neural and classical statistical synthesizers use the fit/sample vocabulary;
- explicitly differentially private synthesizers add distinct privacy configuration rather than making privacy implicit in all synthetic generation.

These observations support several SYNGAN semantic distinctions but do not make SDV's object model authoritative.

### Spark

Spark's DataFrame API uses `sample` for selection from existing data, and Spark ML has its own `Estimator`/`Model` abstractions.

This reinforces the need to distinguish domain language from Spark representation vocabulary.

### PyTorch

PyTorch distinguishes an executable model object from state persisted through `state_dict`, while distributed checkpointing may persist state across multiple files/ranks.

This reinforces SYNGAN's distinctions among implementation object, learned state, checkpoint, and durable artifact.

## Concept-candidate signals handed to 001-D

The term-status register flags several areas for explicit concept investigation, including:

- source/synthetic dataset boundaries;
- data semantics;
- relationships;
- synthesis strategy;
- learning;
- learned state;
- generation and generation intent;
- conditions;
- constraints;
- evaluation and criteria;
- fidelity/utility/validity/privacy/disclosure-risk responsibilities;
- evidence;
- execution and attempts;
- artifacts;
- provenance;
- reproducibility.

These are not an accepted concept list.

001-D must begin from the purposes and actor needs established in 001-B, derive candidate concepts independently, and use this inventory to detect semantic omissions or accidental mergers.

## External sources consulted

- SDV Metadata: https://docs.sdv.dev/sdv/concepts/metadata
- SDV CTGANSynthesizer: https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/ctgansynthesizer
- SDV GaussianCopulaSynthesizer: https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/gaussiancopulasynthesizer
- SDV DPGCSynthesizer: https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/dpgcsynthesizer
- Apache Spark PySpark API: https://spark.apache.org/docs/latest/api/python/
- PyTorch Save/Load tutorial: https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html
- PyTorch Distributed Checkpoint tutorial: https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html

## Exit criteria

001-C is complete when:

- [x] preferred domain vocabulary exists;
- [x] overloaded high-risk terms are identified;
- [x] `metadata`, `synthesizer`, `model`, `sample`, `quality`, `run`, and `artifact` are prevented from silently defining concept boundaries;
- [x] generation is distinguished from source sampling;
- [x] learning is distinguished from training and generation;
- [x] learned state is distinguished from model family, implementation object, and artifact;
- [x] condition, constraint, and filter are distinguished;
- [x] fidelity, utility, validity, privacy, and disclosure risk are separated;
- [x] criteria, metrics, scores, evidence, claims, and decisions are not conflated;
- [x] synthetic data is not treated as automatically private or anonymized;
- [x] execution, attempt, checkpoint, artifact, provenance, and lineage terminology is clarified;
- [x] reproducibility is distinguished from determinism;
- [x] distributed execution is distinguished from scalability;
- [x] Spark-native is distinguished from Spark-only;
- [x] ecosystem terminology collisions are documented;
- [x] concept-candidate signals are recorded without accepting a concept catalog.

## Exit assessment

**Status: complete.**

SYNGAN now has a sufficiently precise semantic vocabulary to conduct candidate concept discovery without inheriting concept boundaries accidentally from SDV, Spark, PyTorch, or generic ML terminology.

## Next phase

**001-D — Candidate Concept Discovery & Boundary Hypotheses**

001-D should derive candidate concepts from purposes and actor needs, test their independence and operational roles, identify likely synchronization needs, and use the 001-C semantic inventory as a cross-check rather than converting the glossary mechanically into concepts.
