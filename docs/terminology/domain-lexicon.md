---
type: Domain Lexicon
title: SYNGAN Domain Lexicon
status: active
---

# SYNGAN Domain Lexicon

## Purpose

This document defines preferred domain vocabulary for SYNGAN before concept boundaries are selected.

Definitions here are semantic, not representational. A defined term MUST NOT be assumed to correspond one-to-one with a Python class, Spark abstraction, persisted object, service, or concept.

## Data and structure

### Source data

Data supplied as evidence from which synthetic-data behavior may be derived, assessed, or configured.

`Source data` does not imply that every source record must be used for learning, nor that the source must be locally materialized.

### Source dataset

A logically bounded collection of source data considered together for a synthesis purpose.

Its logical boundary is independent of physical files, Spark partitions, tables, DataFrames, or storage systems.

### Synthetic data

Generated data intended to preserve selected properties, relationships, semantics, or utility of source data or a declared specification without being a simple copy of source records.

The term makes **no automatic claim** of anonymity, privacy, non-identifiability, disclosure safety, fidelity, or downstream fitness.

### Synthetic dataset

A logically bounded collection of synthetic data produced for a stated purpose or request.

### Structured data

Data whose fields, records, relationships, or other organization can be described explicitly enough to support structured interpretation and generation.

`Structured data` is broader than a single flat table.

### Tabular data

Structured data represented primarily as rows and named columns within one table-like relation.

### Relational data

Structured data whose meaning includes relationships among multiple logical record collections, commonly involving identifiers, keys, references, cardinalities, or other cross-collection rules.

### Record

One logical observation, entity instance, event, transaction, or other row-like unit within a data collection.

The domain term does not require a particular Spark `Row` representation.

### Field

A named logical attribute or component of a record.

The domain term does not require a particular Spark `Column` representation.

### Structural schema

The declared or observed structural organization of data, such as field names, physical or logical data types, nullability, nesting, and table/record shape.

Structural schema alone does not fully describe domain meaning.

### Data semantics

The intended meaning, role, interpretation, and significant relationships of data beyond mere storage type or physical schema.

Examples may include whether a field is an identifier, category, amount, event time, constrained code, or reference to another record collection.

### Metadata

Descriptive information about data, synthesis work, artifacts, configuration, execution, or evidence.

`Metadata` is intentionally an umbrella word and MUST NOT be assumed to identify one independent concept or one monolithic metadata object. More specific terms SHOULD be used when the kind of metadata matters.

### Identifier

A value or combination of values used to distinguish or refer to a logical record or domain entity within some scope.

Uniqueness, persistence, sensitivity, and referential meaning are separate properties and MUST NOT be inferred from the word alone.

### Relationship

A meaningful association among records, fields, tables, entities, events, or other domain objects.

A relationship may carry cardinality, referential, temporal, semantic, or other rules.

## Synthesis and learning

### Synthesis

The broader activity of producing synthetic data in accordance with source evidence, declared semantics, selected strategy, generation intent, and applicable rules or guarantees.

Synthesis is broader than neural-network inference and broader than any one model family.

### Synthesis strategy

A method or family of methods used to derive or produce synthetic data.

Examples may eventually include statistical, rule-based, GAN, VAE, diffusion, hybrid, or externally supplied approaches.

A synthesis strategy is domain vocabulary; whether it becomes an independent concept is deferred.

### Synthesis implementation

A concrete software implementation of a synthesis strategy.

This is representation vocabulary and MUST NOT be confused with the strategy's domain meaning.

### Learning

The process of deriving reusable statistical, algorithmic, or parameterized state from source data or source-derived evidence for later synthesis behavior.

`Learning` is the preferred neutral domain term when the process is not necessarily neural-network training.

### Training

A form of learning involving optimization or iterative adjustment of parameters according to an objective.

Not all synthesis strategies require training.

### Fit

A compatibility term commonly used by statistical and ML libraries for deriving fitted or learned state from data.

SYNGAN MUST NOT assume that `fit` and `training` are universal synonyms. Public API naming is deferred.

### Learned state

Reusable state derived through learning from source data or source-derived evidence and used to influence later generation.

Learned state may include model parameters, distributions, sketches, statistics, encodings, lookup structures, or other learned information.

It is deliberately broader than a neural-network `model`.

### Model family

A recognized class of mathematical or algorithmic models sharing a common modeling approach, such as a GAN family or variational autoencoder family.

### Model

An overloaded compatibility term.

Within SYNGAN design documents, `model` SHOULD NOT be used without qualification when it could mean a model family, model definition, learned parameters, executable object, Spark ML `Model`, or persisted artifact.

Prefer a more specific term such as `model family`, `learned state`, `model definition`, or `artifact`.

### Generate

Produce synthetic records or data using applicable source-derived state, declared semantics, strategy, generation intent, and rules.

`Generate` is the preferred domain verb for production of synthetic data.

### Sample

An overloaded term that may mean either selecting a subset from existing data or generating observations from a learned distribution.

SYNGAN domain documents SHOULD qualify it as `source sample`, `evaluation sample`, or another specific kind when referring to subset selection. `Generate` SHOULD be preferred for production of synthetic data unless a mathematical sampling meaning is specifically intended.

### Generation intent

The requested characteristics of a generation operation, such as desired quantity, conditions, scope, seed/reproducibility controls, or other requested output behavior.

This term does not yet imply an independent concept.

### Condition

A requested property, value, relationship, or predicate intended to influence what data is generated.

A condition expresses desired generation behavior; it is not automatically a validity rule.

### Constraint

A rule that generated data is required or expected to satisfy within a stated scope.

Constraints may express structural, domain, relational, range, uniqueness, logical, or other validity requirements.

How constraints are represented or enforced is deferred.

### Filter

A selection operation that removes or retains already-existing records according to a predicate.

Post-generation filtering is not semantically equivalent to conditioning generation, even when both produce data matching the same predicate.

## Evaluation and evidence

### Evaluation

The activity of producing evidence about synthetic data, learned state, synthesis behavior, or a synthesis process against one or more explicit criteria.

### Criterion

A question, requirement, threshold, objective, or standard against which something is evaluated.

### Metric

A defined measurement procedure that produces a quantitative or structured result relevant to a criterion.

A metric does not by itself determine acceptability.

### Score

A result or normalized value produced from a metric or aggregation procedure.

A score MUST NOT be treated as a complete quality judgment unless its interpretation and scope are defined.

### Quality

An umbrella term for fitness relative to stated criteria or intended use.

`Quality` MUST NOT be treated as one universal scalar. More specific dimensions SHOULD be named.

### Fidelity

The degree to which synthetic data reproduces selected statistical, structural, distributional, or relational properties of a reference source within a defined comparison scope.

High fidelity does not imply privacy or downstream utility.

### Utility

The degree to which synthetic data is fit for a specified downstream task, analysis, workflow, or decision-support purpose.

Utility is purpose-relative and cannot be inferred solely from statistical similarity.

### Validity

The degree to which data satisfies applicable structural, semantic, relational, or declared constraints.

Validity does not imply fidelity, utility, or privacy.

### Privacy

Protection of information or persons according to an explicit privacy objective, threat model, mechanism, policy, or guarantee.

`Privacy` MUST NOT be inferred merely because data is synthetic.

### Disclosure risk

The risk that released data, outputs, artifacts, or observable behavior reveal sensitive information about source records, persons, groups, or properties under a stated threat model or analysis.

Disclosure-risk evidence is distinct from fidelity evidence.

### Anonymization

A process or claimed state intended to prevent or materially reduce identification or linkage to persons or records under some definition or policy.

`Anonymization`, `synthetic data`, and `privacy` are not synonyms.

### Evidence

Information produced or retained to support an assessment, claim, decision, reconstruction, or audit.

Evidence may include metrics, observations, configurations, provenance, logs, reports, or other relevant material.

## Execution, persistence, and provenance

### Execution

The performance of synthesis-related work within a particular invocation or operational context.

The domain term is independent of Spark job, stage, task, process, container, or cluster representation.

### Attempt

One try at performing some execution scope, especially when work may fail and be retried.

A retry SHOULD be distinguishable from the original attempt even if both belong to the same logical requested work.

### Run

An overloaded compatibility term for executed work.

Design documents SHOULD prefer `execution`, `attempt`, or a more specific term until concept discovery establishes whether `run` has an independent canonical meaning.

### Checkpoint

Persisted intermediate state intended to support continuation, recovery, resumption, or inspection of incomplete work.

A checkpoint is not automatically the final learned state or final synthesis artifact.

### Artifact

A durable materialized output of synthesis-related work that can be identified, retained, transferred, inspected, reused, or governed.

Examples may include learned-state materializations, generated datasets, reports, evaluation results, manifests, or checkpoints. The term is intentionally broader than `model file`.

### Provenance

Traceable information about the origin, inputs, transformations, configuration, responsible software or actors, and derivation history of data, evidence, or artifacts.

### Lineage

A derivational chain showing how data or artifacts descend from or depend on prior data or artifacts.

Lineage is a part of provenance; provenance may also include contextual information that is not itself a derivation edge.

### Reproducibility

The ability to repeat a defined procedure under stated conditions and obtain results consistent with an explicit reproducibility expectation.

Reproducibility may be exact, statistically equivalent, bounded, or otherwise scoped.

### Determinism

The property that the same defined inputs and conditions lead to the same defined outputs or state transitions.

Determinism is stronger and narrower than reproducibility and MUST NOT be used as a synonym.

## Scale and platform language

### Distributed execution

Execution in which work or state is intentionally divided across multiple execution units, processes, machines, accelerators, or workers.

Distributed execution is an implementation/operational property, not proof of scalability.

### Scalable

Able to remain viable across a stated scale envelope while preserving required behavior, resource bounds, operational control, and evidence quality.

The term MUST be accompanied by a relevant scale scope when used as a substantive claim.

### Spark-native

A project-level compatibility term meaning that SYNGAN is designed to participate naturally in PySpark/Spark DataFrame workflows and not impose full-corpus driver-local materialization as the ordinary enterprise path.

`Spark-native` does not, by itself, require use of Spark ML `Estimator`/`Model`, a particular distributed-learning subsystem, or Spark-only internal implementations.

### Driver-local

State or computation that resides primarily within the Spark driver process or another single coordinating local process.

Driver-local state is not inherently prohibited, but any state that grows materially with the source corpus or generated corpus requires explicit scalability justification.

## Naming guidance

When a precise term exists above, later design documents SHOULD use it instead of a broader overloaded word.

In particular:

- prefer `generate` over ambiguous `sample` for synthetic output production;
- prefer `learned state` over ambiguous `model` when referring to reusable source-derived state;
- qualify `metadata` by kind when its role matters;
- qualify `quality` by criterion or dimension;
- distinguish `condition`, `constraint`, and `filter`;
- distinguish `execution`, `attempt`, and `checkpoint`;
- distinguish `reproducibility` from `determinism`;
- distinguish `privacy` from `synthetic`, `anonymized`, and `low disclosure risk`.
