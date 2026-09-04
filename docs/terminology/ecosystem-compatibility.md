---
type: Compatibility Vocabulary
 title: SYNGAN Ecosystem Compatibility Vocabulary
status: active
---

# SYNGAN Ecosystem Compatibility Vocabulary

## Purpose

SYNGAN will coexist with established data, ML, Spark, and synthetic-data ecosystems. This document records important vocabulary collisions so compatibility does not silently become design authority.

External terms are descriptive evidence only. The [Domain Lexicon](domain-lexicon.md) remains canonical for SYNGAN domain meaning.

## SDV vocabulary

### Metadata

Current SDV documentation describes metadata as the description of the dataset to synthesize, including tables, columns, data types, and relationships, and treats that metadata as ground truth for synthesis and evaluation.

SYNGAN intentionally uses `metadata` more broadly as an umbrella term and does **not** assume a single monolithic metadata object. Later concept discovery may identify separate responsibilities for structural description, semantic declarations, relationships, constraints, or other descriptive knowledge.

Compatibility implication: an SDV metadata object could later be translated into one or more SYNGAN representations without requiring SYNGAN to adopt SDV's semantic boundary.

### Synthesizer

SDV exposes synthesizer classes such as `CTGANSynthesizer`, `TVAESynthesizer`, and `GaussianCopulaSynthesizer`. Their common workflow uses a synthesizer object configured with metadata, `fit(data)`, and `sample(...)` to produce synthetic data.

SYNGAN treats `synthesizer` as compatibility vocabulary, not yet as a canonical concept name. The domain lexicon instead distinguishes synthesis, synthesis strategy, learning, learned state, and generation.

### fit

SDV uses `fit` for learning from real data across both neural and classical statistical synthesizers.

SYNGAN retains `fit` as a compatibility/API candidate but uses `learning` as the neutral domain term because not every strategy necessarily performs iterative model training.

### sample

SDV commonly uses `sample(...)` to create synthetic data.

SYNGAN prefers `generate` in domain documentation because Spark and statistical usage commonly use `sample` to mean selecting observations from data that already exists. A future API MAY expose `sample` for ecosystem familiarity if its semantics are explicit.

### synthetic data and privacy

SDV includes both ordinary synthesizers and explicitly differentially private synthesizers with privacy-budget configuration.

SYNGAN therefore preserves the domain distinction that synthetic origin alone does not constitute a privacy guarantee.

## Spark / PySpark vocabulary

### DataFrame

A Spark DataFrame is a representation used for distributed structured data processing.

SYNGAN MAY eventually use Spark DataFrames as a primary public data representation, but `source dataset`, `synthetic dataset`, `record`, `field`, and `structural schema` remain representation-independent domain terms.

### sample

Spark DataFrames expose `sample` operations for randomly selecting records from an existing DataFrame.

This collides directly with synthetic-data libraries that use `sample` to mean generate new synthetic observations. SYNGAN domain language therefore qualifies subset sampling and prefers `generate` for synthetic production.

### Estimator and Model

Spark ML uses `Estimator` and `Model` as framework abstractions.

SYNGAN MUST NOT infer from these names that its eventual learning and learned-state concepts should map one-to-one onto Spark ML classes. Whether Spark ML integration is appropriate remains a representation-design question.

### partition

Spark partitions are physical/distributed execution units. They MUST NOT be confused with logical dataset boundaries, domain segments, relational tables, model segments, or generation scopes merely because those might later be executed per partition.

## PyTorch vocabulary

### model

PyTorch commonly uses `model` for an `nn.Module` or other executable learned structure.

SYNGAN treats `model` as overloaded because the same word may also refer to a model family, a definition, learned parameters, Spark ML `Model`, or a persisted artifact.

### state_dict

PyTorch distinguishes a model object from its `state_dict`, which contains parameter and buffer state used for persistence/restoration.

This supports SYNGAN's distinction between a model implementation, learned state, and a durable artifact. SYNGAN does not adopt `state_dict` as a domain concept.

### checkpoint

PyTorch uses checkpoints to persist state for later loading or distributed recovery; distributed checkpointing may involve multiple files and rank-local materializations.

SYNGAN therefore treats `checkpoint` as an operational/recovery term rather than a synonym for one final portable model artifact.

## General ML/statistical vocabulary collisions

### train versus fit versus learn

- `train` often implies optimization of parameters;
- `fit` is common in estimator-style APIs and may cover both statistical fitting and ML training;
- `learn` is the preferred neutral SYNGAN domain verb for deriving reusable source-informed state.

### inference

In supervised ML, `inference` usually means applying a learned model to input observations to produce predictions.

Synthetic-data generation may involve executing a learned neural network, but `generation` is the preferred SYNGAN domain term because the result is new synthetic data rather than a prediction over an existing input record.

### model artifact

Industry usage often calls any persisted learned object a `model artifact`.

SYNGAN uses `artifact` more broadly because persisted outputs may include learned state, generated datasets, evaluation results, manifests, checkpoints, or other governed outputs.

## Compatibility rule

External API familiarity is valuable but subordinate to semantic clarity.

A future SYNGAN API MAY intentionally use familiar names such as `fit`, `sample`, `model`, `metadata`, or Spark ML types. When it does, the representation/API specification MUST map that name back to the canonical SYNGAN domain meaning and document any semantic narrowing or overload.

## Sources

- SDV Metadata: https://docs.sdv.dev/sdv/concepts/metadata
- SDV CTGANSynthesizer: https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/ctgansynthesizer
- SDV GaussianCopulaSynthesizer: https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/gaussiancopulasynthesizer
- SDV DPGCSynthesizer: https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/dpgcsynthesizer
- Apache Spark PySpark API: https://spark.apache.org/docs/latest/api/python/
- PyTorch save/load tutorial: https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html
- PyTorch distributed checkpoint tutorial: https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html
