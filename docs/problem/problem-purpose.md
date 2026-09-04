---
type: Problem Statement
title: SYNGAN Problem & Purpose
status: active
---

# SYNGAN Problem & Purpose

## Core problem

Organizations increasingly need synthetic structured data for development, testing, analytics, modeling, sharing, experimentation, privacy-risk reduction, and other controlled uses. Existing synthetic-data tooling often works well when data can be represented and processed comfortably in a single-process analytical environment, but that assumption becomes restrictive when source datasets contain tens or hundreds of millions of rows or otherwise exceed the practical memory, transfer, or execution limits of one machine or one Python process.

At enterprise scale, synthetic-data work is not only a model-fitting problem. It also becomes a distributed data, operational, quality, provenance, governance, failure-recovery, and lifecycle problem.

A framework that merely wraps a local synthesizer in Spark orchestration can still preserve the same central bottleneck if core stages require the full corpus to be collected, converted, or reasoned about locally.

## Purpose

SYNGAN exists to make high-quality synthetic-data workflows practical for large structured datasets represented in PySpark while preserving explicit control over data meaning, synthesis behavior, evaluation, provenance, and operational execution.

The framework should allow useful synthesis work to remain viable when the relevant dataset cannot reasonably fit in driver memory or be materialized as one local pandas DataFrame.

The purpose is broader than implementing one GAN algorithm. CTGAN and related methods are important candidate synthesis techniques, but the framework's purpose is synthetic-data generation at Spark-scale rather than allegiance to a particular model family.

## Why a dedicated framework is needed

The problem includes several interacting pressures:

1. **Scale pressure** — source and generated datasets may be too large for a mandatory single-node materialization boundary.
2. **Statistical pressure** — structured data may contain mixed types, skew, sparsity, high-cardinality categories, multimodal distributions, missingness, dependencies, and constraints that naive generation does not preserve.
3. **Algorithm pressure** — different datasets and uses may require different synthesis strategies; no single algorithm should silently define the framework's semantics.
4. **Operational pressure** — long-running distributed work requires observable progress, bounded resource behavior, recoverable failure handling, and clear lifecycle state.
5. **Evaluation pressure** — fidelity, utility, validity, and privacy risk are distinct concerns and may themselves require distributed computation.
6. **Governance pressure** — enterprise use requires traceability from source interpretation and configuration through generated output and evaluation evidence.
7. **Privacy pressure** — synthetic output may reduce direct exposure to source records, but synthetic data is not automatically private and privacy claims require explicit evidence.
8. **Portability pressure** — Spark is the required data-processing environment, but the design should avoid unnecessary dependence on one managed platform or one model runtime unless later requirements justify it.

## Primary scope

The current design scope is synthetic generation for structured data that can be represented through Spark DataFrames.

This includes the surrounding workflow necessary to make synthesis useful and trustworthy at scale: interpretation of source structure and semantics, preparation, learning or fitting where applicable, generation, validation/evaluation, provenance, persistence of relevant artifacts, and operational execution.

Whether multi-table relational synthesis, streaming synthesis, or other advanced forms belong in the first product boundary remains open and must be resolved by later concept discovery rather than assumed here.

## Non-goals at this stage

SYNGAN is not currently defined as:

- a Spark rewrite of SDV;
- a distributed rewrite of CTGAN;
- a guarantee of differential privacy or any other privacy property by default;
- a guarantee that synthetic data is safe for unrestricted disclosure;
- a replacement for Spark's execution engine or storage ecosystem;
- a Databricks-only package;
- a PyTorch-only package;
- a framework whose public abstraction must mirror Spark ML `Estimator`/`Model`;
- a system for unstructured image, audio, or text generation;
- a real-time synthetic-data serving platform;
- a promise that every synthesis method must consume every training row directly.

These boundaries may evolve through explicit design work.

## Fundamental problem constraint

A successful design MUST NOT require the complete source dataset to be collected into the Spark driver or materialized as a single local DataFrame as an unavoidable condition of ordinary large-scale use.

This is a problem-level scalability constraint, not a prescription for how any particular algorithm must be implemented. A later synthesis strategy may legitimately use distributed statistics, partition-local processing, sampling, staged learning, distributed model training, or another justified mechanism, provided the framework does not impose a full-corpus local bottleneck as its universal architecture.

## Relationship to concept discovery

This document states the problem and purpose only. Terms such as dataset, model, training, generation, constraint, evaluation, privacy, artifact, or execution in this document are ordinary domain language and MUST NOT be interpreted as accepted SYNGAN concepts until Phase 001 concept discovery evaluates them.
