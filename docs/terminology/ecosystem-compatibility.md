---
type: Compatibility Vocabulary
title: SYNGAN Ecosystem Compatibility Vocabulary
status: active
---

# SYNGAN Ecosystem Compatibility Vocabulary

## Purpose

SYNGAN will coexist with established data, ML, Spark, synthetic-data, evaluation, experiment-tracking and lineage ecosystems. This document records important vocabulary collisions so compatibility does not silently become design authority.

External terms are descriptive/familiarity evidence only. The [Domain Lexicon](domain-lexicon.md), accepted concept specifications and current design-quality authority remain canonical for SYNGAN meaning.

Phase 011-C revalidated this compatibility vocabulary against current external documentation on **2026-09-16**. Version-sensitive external terminology should be rechecked when an integration is actually designed.

## Compatibility rule

External familiarity is useful only when the external term preserves the conceptual job being communicated.

Use this one-way rule:

> **An external term may explain or label a compatible projection of SYNGAN semantics; it must not redefine the canonical SYNGAN owner, lifecycle, scope or guarantee.**

Therefore a compatibility term may be:

- a **qualified alias** when its intended SYNGAN meaning is unambiguous in context;
- an **explanatory analogue** when it helps recognition but is not safe as a synonym;
- **rejected as a generic alias** when the external term collapses multiple SYNGAN concepts or imports a materially different lifecycle/authority.

No compatibility mapping below implies a future API name.

---

## SDV vocabulary

### Metadata

Current SDV documentation describes **Metadata** as the description of the dataset to synthesize, including tables, columns, data types and relationships, and states that synthesizers refer to metadata as ground truth when creating or evaluating synthetic data.

SYNGAN intentionally does not adopt one monolithic `Metadata` concept. Related SYNGAN semantics are distributed across:

```text
Data Meaning          synthesis-relevant descriptive semantics
Constraint            reusable prescriptive rules
external/physical schema and dataset identity
other owner-specific configuration or historical references
```

**Disposition:** explanatory analogue / compatibility object only; **reject as a generic canonical alias** for Data Meaning.

An SDV metadata object may later be translated into several SYNGAN representations without requiring SYNGAN to adopt SDV's semantic boundary.

### Synthesizer

SDV exposes synthesizer classes such as `CTGANSynthesizer`, and its current workflow creates/configures a synthesizer, calls `fit(data)`, can save/load the trained synthesizer, and calls `sample(...)` to create synthetic data.

That object spans concerns SYNGAN deliberately separates:

```text
Synthesis Strategy    reusable synthesis behavior/capabilities
Learning              source-informed derivation activity, when required
Learned State         reusable source-derived result, when established
Generation            one requested synthetic-data production occurrence
implementation object persistence / loading
```

**Disposition:** useful ecosystem/implementation analogue; **reject as a canonical concept alias** because it collapses multiple owners.

A future adapter may legitimately expose a `synthesizer` object if its specification maps operations back to canonical SYNGAN semantics.

### fit

SDV uses `fit` to learn from real data.

SYNGAN uses **Learning** as the neutral domain activity because source-informed reusable derivation need not always be iterative ML training.

**Disposition:** **qualified alias/verb for Learning** when the Strategy actually derives reusable source-informed state. `fit` is not a universal lifecycle name.

### train

SDV's CTGAN documentation also uses `train` for GAN-specific modeling behavior.

**Disposition:** qualified Learning verb only when the Strategy genuinely performs model training/optimization.

### sample

SDV uses `sample(...)` to create new synthetic records. Spark and statistical libraries also use `sample` to select observations from existing data.

SYNGAN therefore prefers **generate** for canonical synthetic production language.

**Disposition:** compatibility/API verb for Generation only when the operation clearly means create new synthetic data; otherwise qualify the meaning.

### synthetic data and privacy

Synthetic origin does not itself establish a privacy guarantee. Empirical disclosure/privacy-risk questions remain Criterion → Evaluation → Evidence concerns; future formal privacy mechanisms require mechanism-specific concept rediscovery when their independent state/lifecycle enters scope.

---

## Spark / PySpark vocabulary

### DataFrame

A Spark DataFrame is a representation used for distributed structured data processing.

SYNGAN may use Spark DataFrames as a primary physical/public representation, but `source dataset`, `synthetic dataset`, `record`, `field`, semantic scope and Data Meaning remain conceptually distinct from that representation.

**Disposition:** representation term, not a concept alias.

### sample

Spark DataFrames expose `sample` operations for selecting records from an existing DataFrame. This directly collides with synthetic-data libraries that use `sample` to mean generation.

**Disposition:** qualify subset sampling; prefer `generate` for SYNGAN Generation.

### Estimator

Spark ML uses `Estimator` for an abstraction that can be fit to produce a `Model`/Transformer.

This is a useful analogue for a subset of Learning behavior, but one Spark Estimator object can package algorithm, parameters and fit mechanics in a way that does not map one-to-one to SYNGAN Strategy + Learning.

**Disposition:** explanatory/representation analogue; not a canonical alias.

### Model

Spark ML exposes `Model` classes as fitted Transformers.

A Spark ML Model may physically represent some or all of a SYNGAN Learned State for a particular Strategy, but `Model` is too overloaded to be canonical because valid Learned State may be statistical, composite, distributed or otherwise not naturally a model object.

**Disposition:** **qualified analogue for Learned State when the concrete Strategy actually produces a model**; reject as a generic alias.

### Transformer / Pipeline / PipelineModel

These are Spark ML framework abstractions. They may later participate in representation/integration design but do not imply SYNGAN concept boundaries or a mandatory pipeline/workflow concept.

**Disposition:** representation vocabulary only.

### partition

Spark partitions are physical/distributed execution units. They must not be confused with logical dataset boundaries, domain segments, relational tables, generation scope or semantic topology merely because work may later be executed per partition.

---

## PyTorch vocabulary

### model

PyTorch commonly uses `model` for an `nn.Module` or other executable learned structure.

SYNGAN treats `model` as overloaded because it may refer to a model family, Strategy implementation, runtime object, learned parameters/state, persisted artifact, or an ecosystem-registered model.

**Disposition:** qualified explanatory term only; never infer ownership from the word itself.

### state_dict

PyTorch distinguishes a model object from its `state_dict`, which contains parameter/buffer state used for persistence/restoration.

This supports SYNGAN's distinction between an implementation object and reusable learned state, but a `state_dict` remains one representation form rather than a domain concept.

**Disposition:** possible physical representation of part/all of Learned State; not a canonical alias.

### checkpoint

PyTorch checkpoints persist state for loading or recovery and can include more than final model parameters.

SYNGAN therefore treats `checkpoint` as operational/recovery material unless the owning semantic concept explicitly validates/promotes some material as its authoritative result.

**Disposition:** representation/Execution-recovery term; not a Learned State synonym by default.

---

## MLflow vocabulary

### Run

Current MLflow Tracking documentation organizes tracking around **runs**, described as executions of data-science code that record metadata, metrics and artifacts.

A single MLflow Run may capture training code, evaluation metrics, artifacts, environment data and other observations that cross several SYNGAN semantic owners.

**Disposition:** useful operational/integration correlate, but **reject as a generic alias** for Learning, Generation, Evaluation or Execution.

When ambiguity matters, qualify terms such as `MLflow Run` versus `SYNGAN Execution` or the owning semantic activity.

### Model / Registered Model

MLflow tracks/logs trained models and its Model Registry manages model versions, lineage, aliases, metadata and lifecycle information.

That familiar lifecycle is useful for integrations, but it can combine physical model packaging, registry state, provenance and deployment governance that SYNGAN keeps separate from Learned State semantics.

**Disposition:** qualified external representation/registry analogue for model-shaped Learned State only; not a canonical alias.

### Artifact

MLflow artifact stores hold output files such as model weights, images and data files produced by runs.

SYNGAN deliberately avoids a universal `Artifact` concept because Learned State, Generation output, Evidence, checkpoints and external files have different owners and finality semantics.

**Disposition:** physical/integration material term; **reject as a canonical concept alias**.

### Metric

MLflow records metrics as tracked values associated with runs/models.

A metric name/value alone is not a SYNGAN Evaluation Criterion, Evaluation or Evidence. The intended question, method, scope, uncertainty and claim strength determine those owners.

**Disposition:** method/observation compatibility term; not a canonical alias for Criterion or Evidence.

---

## Great Expectations vocabulary

### Expectation

Current Great Expectations documentation defines an **Expectation** as a verifiable assertion about data.

Depending on intent, a familiar `Expectation` may resemble either:

```text
Constraint            when it is a reusable prescriptive rule output must obey
Evaluation Criterion  when it states a question/standard to be examined
```

The term therefore does not map safely one-to-one to either concept without inspecting authority and purpose.

**Disposition:** explanatory analogue; **reject as an unconditional canonical alias**.

### Validation Definition / Checkpoint

Great Expectations uses validation definitions/checkpoints to apply expectations to data and produce validation results.

These are useful analogues for a particular validation-oriented Evaluation workflow, but they package orchestration/configuration semantics beyond SYNGAN's generic Evaluation concept.

**Disposition:** qualified workflow/integration analogue; not a canonical alias.

### Validation Result

Great Expectations produces Validation Results containing success/failure and result details for Expectations or suites.

A validation result can be a useful analogue for one kind of SYNGAN Evidence, but SYNGAN Evidence also supports statistical, approximate, diagnostic, comparative, risk and indeterminate findings that do not reduce to pass/fail validation.

**Disposition:** **qualified analogue for Evidence in validation-oriented cases**; reject as a generic Evidence alias.

### validation / passed

Great Expectations legitimately centers validation and pass/fail because its product purpose is assertion checking. SYNGAN Evaluation is broader and may validly complete with unfavorable or inconclusive Evidence.

**Disposition:** use `validation`/`passed` only where the bound Criterion actually defines validation/pass semantics.

---

## OpenLineage vocabulary

### Job

OpenLineage defines a Job as an abstract process and records Job/Run/Dataset lineage metadata.

A Job is not equivalent to a SYNGAN semantic activity or Execution. It is an external lineage entity whose relationship to SYNGAN work must be mapped explicitly.

**Disposition:** external integration entity; reject as a generic Execution alias.

### Run

OpenLineage Run state describes an execution occurrence of a Job and uses lifecycle events such as START/RUNNING/COMPLETE/ABORT.

Those states are operational/integration evidence and must not establish Learning/Generation/Evaluation semantic completion.

**Disposition:** external operational correlate; not a canonical alias.

### Dataset

OpenLineage Dataset is an external data/lineage entity identified by namespace/name and facets.

SYNGAN may reference such an identity in Provenance or activity bindings, but OpenLineage Dataset is not a replacement for Data Meaning or Generation result semantics.

**Disposition:** external identity/reference representation.

### lineage

OpenLineage is intentionally a lineage standard. SYNGAN Provenance is broader than derivational data lineage because it includes typed binding, realization, evaluation, dependency, recovery and historical-context relationships.

**Disposition:** **qualified subset alias**: `lineage` may describe derivational portions of Provenance, but must not be used as a complete synonym when broader relationship semantics matter.

---

## General ML/statistical vocabulary collisions

### train versus fit versus learn

- `train` commonly implies optimization of model parameters;
- `fit` is common in estimator/synthesizer APIs and may cover statistical fitting or model training;
- `learn` is the preferred neutral SYNGAN verb for deriving reusable source-informed state.

Use the familiar narrower verb when it truthfully describes the concrete Strategy; keep `Learning` as the canonical concept.

### inference

In supervised ML, `inference` commonly means applying a learned model to input observations to produce predictions.

Synthetic-data production may execute a learned model, but **Generation** remains the preferred SYNGAN domain term because its purpose is to produce a logical synthetic-data result rather than classify/predict an existing record.

### model artifact

Industry usage often calls persisted learned objects model artifacts. In SYNGAN, physical material and semantic authority remain distinct. A physical artifact may represent Learned State, output, Evidence or checkpoint material depending on owner and finality.

### result

`Result` is familiar but too broad to distinguish Generation output, Evidence, activity outcome, Execution outcome or an external validation result.

Use the owner-qualified form when needed: `Generation output`, `Evidence finding`, `Evaluation outcome`, `Execution outcome`, etc.

---

# 011-C familiarity mapping summary

The current canonical names remain preferred:

```text
Data Meaning
Synthesis Strategy
Learning
Learned State
Generation
Constraint
Evaluation Criterion
Evaluation
Evidence
Execution
Provenance
```

Useful compatibility vocabulary is intentionally asymmetric:

```text
fit / train              -> qualified Learning verbs
model                     -> qualified Learned State/implementation analogue
sample                    -> Generation verb only when clearly synthetic production
synthesizer               -> external/implementation aggregate, not a concept alias
expectation               -> inspect purpose: Constraint or Criterion-like
validation result         -> qualified Evidence analogue
run / job                 -> external/operational terms; always qualify owner
artifact                  -> physical material term, not semantic authority
metric                    -> method/observation term, not Criterion/Evidence by itself
lineage                   -> derivational subset of Provenance
metadata                  -> external umbrella; not a Data Meaning synonym
```

No external vocabulary justifies renaming, merging or splitting the current eleven concepts.

## Sources reviewed for 011-C

Current/recent official documentation reviewed on **2026-09-16**:

- SDV Metadata: https://docs.sdv.dev/sdv/integration/metadata.md
- SDV CTGANSynthesizer: https://docs.sdv.dev/sdv/modeling/single-table-synthesizers/ctgansynthesizer.md
- Apache Spark ML API (Estimator / Model / Pipeline / Transformer): https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html
- MLflow Tracking: https://mlflow.org/docs/latest/ml/tracking
- MLflow Model Registry: https://mlflow.org/docs/latest/ml/model-registry
- MLflow Artifact Stores: https://mlflow.org/docs/latest/self-hosting/architecture/artifact-store/
- Great Expectations glossary/API: https://docs.greatexpectations.io/docs/reference/learn/glossary/
- Great Expectations Validation Result API: https://docs.greatexpectations.io/docs/reference/api/core/expectationvalidationresult_class/
- OpenLineage overview: https://openlineage.io/docs/
- OpenLineage Run Cycle: https://openlineage.io/docs/spec/run-cycle/
- OpenLineage naming/core entities: https://openlineage.io/docs/spec/naming/
- PyTorch save/load tutorial: https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html
- PyTorch distributed checkpoint tutorial: https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html

External documentation changes over time. These references support familiarity/collision analysis; they do not become SYNGAN design authority.
