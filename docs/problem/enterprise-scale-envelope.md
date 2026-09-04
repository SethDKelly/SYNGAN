---
type: Scale Envelope
title: SYNGAN Enterprise Scale Envelope
status: active
---

# SYNGAN Enterprise Scale Envelope

## Purpose

This document defines the scale conditions the design must take seriously. It is an envelope for discovery and architecture, not a benchmark promise or service-level objective.

The design center includes workloads with tens or hundreds of millions of rows, but enterprise scale is multidimensional and MUST NOT be reduced to row count alone.

## Scale dimensions

### Row volume

The design must remain viable from development-sized datasets through datasets in the tens-of-millions and hundreds-of-millions-of-rows range.

Indicative design bands:

| Band | Approximate row scale | Design interpretation |
|---|---:|---|
| Development | < 1 million | Local experimentation may be convenient, but must not define core semantics. |
| Moderate | 1–10 million | Distributed processing may already be desirable depending on width and types. |
| Large | 10–100 million | A primary SYNGAN design center. Full local materialization should not be assumed. |
| Enterprise | 100 million+ | A primary SYNGAN design center where distributed data and operational lifecycle concerns are first-class. |

These bands are intentionally approximate. A very wide or high-cardinality dataset can be harder than a much larger narrow dataset.

### Dataset size versus machine memory

The strongest scale boundary is not a particular row number:

> The ordinary enterprise workflow must remain conceptually valid when the complete source dataset does not fit in Spark driver memory or in the memory of one worker process.

Later architecture must therefore identify any stage whose state grows with source size and determine whether that state is distributed, bounded, summarized, sampled, spilled, streamed, or otherwise controlled.

### Width

The design must consider narrow and wide structured datasets.

Width affects:

- metadata and type interpretation;
- model parameterization;
- dependency complexity;
- encoding size;
- memory use;
- evaluation cost;
- generated-row size.

No exact supported-column maximum is set in Phase 001.

### Cardinality

High-cardinality categorical or identifier-like fields may dominate memory, encoding, parameter count, or generated-quality behavior even at modest row counts.

The framework must eventually make material cardinality limitations or strategy-specific restrictions inspectable rather than failing through an undocumented local-memory cliff.

### Distribution shape

Scale includes difficult distributions such as:

- severe category imbalance;
- long tails;
- rare events;
- multimodal continuous values;
- heavy skew;
- sparse values;
- substantial missingness;
- correlated features;
- highly uneven partition sizes.

A workflow that technically accepts many rows but becomes unusable under ordinary enterprise skew is not meaningfully scalable.

### Source partitioning and placement

Enterprise source data will normally already be partitioned and distributed.

The design must consider the cost and semantic consequences of repartitioning, shuffling, scanning, sampling, caching, spilling, and data movement. These are not yet commitments to specific mechanisms.

### Generated volume

Generation is not assumed to be one-source-row-to-one-output-row.

Supported workflows may need to generate:

- small samples for inspection;
- datasets comparable in size to the source;
- multiple synthetic datasets from one learned state;
- outputs materially larger than the source.

Architecture must therefore avoid assuming that generation is a small driver-local return value.

### Evaluation volume

Quality and risk evaluation can require comparing large source and synthetic datasets and may be as expensive as—or more expensive than—generation itself.

Later design must distinguish methods that can operate distributively, methods requiring bounded samples or summaries, and methods whose cost makes them inappropriate for routine large-scale execution.

### Runtime duration

Large fitting, generation, or evaluation work may run long enough that interactive-function-call assumptions fail.

The design must anticipate jobs lasting long enough for users to need:

- progress visibility;
- durable execution identity;
- failure diagnosis;
- cancellation or interruption semantics;
- retry/recovery behavior;
- separation of completed and partial outputs.

Phase 001 intentionally sets no runtime SLO.

### Compute heterogeneity

Some techniques may be CPU-oriented; others may require or benefit from GPUs or other accelerators. Some may distribute naturally by data partitions; others may require coordinated model training.

The framework must not hide material compute requirements or force all synthesis methods into an execution pattern that only fits one algorithm family.

### Concurrency

Enterprise environments may execute multiple synthesis, generation, or evaluation workloads concurrently.

Exact scheduling and isolation guarantees are deferred, but later architecture must avoid global mutable state or other assumptions that make independent jobs inherently unsafe to colocate.

### Persistence and artifact scale

Learned state, summaries, metadata, checkpoints, evaluation evidence, and generated outputs may vary greatly in size.

The design must distinguish small control-plane state from potentially large data-plane artifacts and avoid assuming that all artifacts belong in a driver-local serialized object.

## Enterprise operability envelope

Scale also changes non-numeric expectations. Enterprise-scale use implies that later design should account for:

- repeatable configuration;
- execution identity and status;
- provenance and lineage;
- inspectable failures;
- resource visibility;
- compatibility/version behavior;
- access to evidence supporting quality or privacy claims;
- safe cleanup of failed or superseded work;
- separation of control-plane metadata from bulk data where useful;
- operation in managed and self-managed Spark environments where feasible.

These are problem consequences, not yet architectural solutions.

## Design-center statement

SYNGAN's design center is not the smallest dataset on which an algorithm can be demonstrated. It is a distributed structured-data workflow where source and/or generated data may exceed a single machine's practical capacity and where fitting, generation, and evaluation must be treated as operationally meaningful jobs.

## Anti-benchmark rule

The row bands in this document MUST NOT be advertised as supported performance guarantees until benchmark methodology, representative workload classes, hardware profiles, model families, and acceptance criteria are defined in later phases.

A statement such as "supports 100 million rows" is incomplete without at least width, cardinality, data size, model strategy, cluster resources, runtime, and evaluated outcome quality.

## Consequences for later discovery

Later phases must explicitly examine whether candidate concepts are needed for concerns including:

- semantic interpretation of source data;
- learned or derived state;
- long-running work and lifecycle state;
- generation requests and output identity;
- evaluation evidence;
- provenance;
- resource and execution behavior;
- failure, retry, and partial completion;
- privacy or disclosure-risk evidence.

This list is a discovery agenda, not an accepted concept catalog.
