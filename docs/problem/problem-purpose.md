---
type: Problem Statement
title: SYNGAN Problem & Purpose
status: active
---

# SYNGAN Problem & Purpose

## Core problem

Organizations need synthetic structured data for development, testing, analytics, modeling, controlled sharing, experimentation, privacy-risk reduction, and related uses. Existing synthetic-data tooling often works well while data can be represented and processed comfortably in one analytical process, but that assumption becomes restrictive when source datasets contain tens or hundreds of millions of rows or otherwise exceed the practical memory, transfer, execution, or governance limits of one machine or one Python process.

At enterprise scale, synthetic-data work is not only a model-fitting problem. It is also a semantic-interpretation, distributed-data, operational-lifecycle, evaluation, provenance, governance, failure-recovery, dependency, and portability problem.

A framework that merely wraps a local synthesizer in Spark orchestration can preserve the same central bottleneck if core stages still require the complete corpus, output, model state, or evaluation subject to be collected, converted, or reasoned about locally.

## Purpose

SYNGAN exists to make high-quality synthetic-data workflows practical for large structured datasets represented in PySpark while preserving explicit control over data meaning, synthesis behavior, generation intent, evaluation, evidence, provenance, and operational execution.

The framework must allow useful supported synthesis work to remain conceptually valid when the relevant source or generated dataset cannot reasonably fit in driver memory or be materialized as one local pandas DataFrame.

The purpose is broader than implementing one GAN algorithm or one train-then-sample workflow. CTGAN and related methods are candidate synthesis techniques, but SYNGAN's purpose is Spark-scale synthetic structured-data generation with method-neutral semantics, not allegiance to a particular model family, runtime, or managed platform.

## Why a dedicated framework is needed

The problem includes several interacting pressures:

1. **Scale pressure** — source, generated, learned, and evaluation state may exceed a mandatory single-node materialization boundary.
2. **Statistical pressure** — structured data may contain mixed types, skew, sparsity, high-cardinality categories, multimodal distributions, missingness, dependencies, constraints, and free-form text-bearing fields whose semantics cannot be inferred safely from physical type alone.
3. **Algorithm pressure** — different datasets and uses may require materially different synthesis strategies; no single algorithm or `fit -> sample` lifecycle should silently define framework semantics.
4. **Topology pressure** — supported structured data includes single-table, time-series, multi-table shared-key, and composable combinations whose semantic relationships must not be flattened into one table merely for implementation convenience.
5. **Operational pressure** — long-running distributed work requires observable progress, durable identity, bounded resource behavior, cancellation, recoverable failure handling, and explicit distinction between operational and semantic completion.
6. **Evaluation pressure** — fidelity, utility, validity, privacy/disclosure risk, and other questions are distinct concerns and may themselves require large-scale or approximate computation.
7. **Governance pressure** — enterprise use requires traceability from source interpretation and configuration through learned state, generated output, execution, evaluation, and durable evidence.
8. **Privacy pressure** — synthetic output may reduce direct exposure to source records, but synthetic data is not automatically private and privacy or disclosure claims require explicit scope, method, assumptions, and evidence.
9. **Dependency/egress pressure** — enterprise environments may require offline or no-egress operation and cannot assume hidden first-use package/model acquisition or remote inference fallback.
10. **Portability pressure** — Spark is the required data-processing environment, but one commercial platform, one model runtime, or one provider-specific execution representation must not become the semantic definition of SYNGAN.

## Current primary scope

The current design scope is synthetic generation for structured data that can be represented through Spark-oriented logical data subjects and processed in PySpark workflows.

The complete structured-data capability target currently includes:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

The design must also permit composable structured topology where those families legitimately overlap. A convenience topology label must not require flattening or erase material relationship, sequence, or temporal semantics.

The supported baseline also includes **text-bearing structured data** where Data Meaning identifies a field as free-form/source-language text. At least one supported baseline synthesis path must be capable of deriving such text behavior from source/local information without requiring a pretrained public model, model hub, hidden first-use download, or runtime inference service. This is a structured-data requirement; it is not a promise of general-purpose language generation.

The surrounding scope necessary to make synthesis useful and trustworthy includes source/structure interpretation, preparation, Learning where a Strategy requires reusable source-informed state, direct Generation where it does not, reusable Learned State, Constraints, Generation intent and completion, Evaluation Criteria, Evaluation, durable Evidence, Provenance, and operational Execution.

## Scope boundaries retained

The current baseline does **not** promise:

- arbitrary recursive/cyclic graph synthesis merely because multi-table shared-key generation is supported;
- a universal relational model covering every database topology;
- real-time/streaming synthetic-data serving;
- that every Strategy supports every topology, field type, Constraint, or Evaluation method;
- that every synthesis method performs Learning or consumes every source row directly;
- that every supported path is equally exact, deterministic, fast, or resource-efficient.

Strategy-specific capability and limitation differences must remain explicit rather than being hidden by a falsely uniform workflow.

## Non-goals

SYNGAN is not currently defined as:

- a Spark rewrite of SDV;
- a distributed rewrite of CTGAN;
- a guarantee of differential privacy or any other privacy property by default;
- a guarantee that synthetic data is safe for unrestricted disclosure;
- an organizational release/use approval authority;
- a replacement for Spark's execution engine or storage ecosystem;
- a Databricks-only package;
- a PyTorch-only package;
- a framework whose public abstraction must mirror Spark ML `Estimator`/`Model`;
- a general system for unstructured image, audio, document, or free-standing text generation;
- a real-time synthetic-data serving platform;
- a promise that every synthesis method must consume every training row directly;
- a promise that externally hosted model/API access is available or permitted.

Text-bearing fields inside structured data remain in scope despite the general unstructured-generation non-goal.

## Fundamental problem constraints

A successful design MUST NOT require the complete source dataset to be collected into the Spark driver or materialized as a single local DataFrame as an unavoidable condition of ordinary large-scale use.

The same principle applies to generated output and other potentially large material state: ordinary supported enterprise use must not rely on a universal driver-local representation simply because it is convenient for one method.

These are problem-level scalability constraints, not prescriptions for specific mechanisms. A later Strategy may legitimately use distributed statistics, partition-local processing, bounded sampling, staged Learning, distributed model training, local source-derived text behavior, or another justified method, provided the framework does not impose one full-corpus local or hidden-network boundary as universal semantics.

## Relationship to current concept design

This document owns the problem and product-purpose boundary, not the concept catalog.

The accepted concept catalog is authoritative under [`docs/concepts/`](../concepts/index.md). The current [Concept-Justification Traceability](concept-justification-traceability.md) records how those concept purposes trace back to this problem, actor needs, and desired outcomes.

If later concept design reveals that a problem statement here cannot be satisfied coherently, the problem/design relationship must be reviewed explicitly. Existing architecture or implementation artifacts may not silently narrow this scope.