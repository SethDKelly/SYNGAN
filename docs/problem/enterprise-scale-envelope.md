---
type: Scale Envelope
title: SYNGAN Enterprise Scale Envelope
status: active
---

# SYNGAN Enterprise Scale Envelope

## Purpose

This document defines the scale conditions the design must take seriously. It is an envelope for concept and representation design, not a benchmark promise or service-level objective.

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

These bands are intentionally approximate. A very wide, text-heavy, highly relational, high-cardinality, or long-sequence dataset can be harder than a much larger narrow table.

### Dataset size versus machine memory

The strongest scale boundary is not a particular row number:

> The ordinary supported enterprise workflow must remain conceptually valid when the complete source dataset does not fit in Spark driver memory or in the memory of one worker process.

The same caution applies to generated output and other potentially large material state. Later representation design must identify state that grows with source/output size and preserve a viable distributed, bounded, summarized, sampled, spilled, streamed, or otherwise controlled realization where required.

### Width

The design must consider narrow and wide structured datasets.

Width affects semantic interpretation, Strategy parameterization, dependency complexity, encoding size, memory use, Evaluation cost, generated-row size, and actor comprehension.

No exact supported-column maximum is a problem-level promise.

### Cardinality

High-cardinality categorical or identifier-like fields may dominate memory, encoding, parameter count, relationship complexity, or generated-quality behavior even at modest row counts.

Material limitations or Strategy-specific restrictions must eventually be inspectable rather than appearing as an undocumented local-memory cliff.

### Distribution shape

Scale includes difficult distributions such as severe category imbalance, long tails, rare events, multimodal continuous values, heavy skew, sparse values, substantial missingness, correlated features, and highly uneven partitions.

A workflow that technically accepts many rows but becomes unusable under ordinary enterprise skew is not meaningfully scalable.

### Structured-topology scale

The current supported structured-data target includes single-table, time-series, multi-table shared-key, and legitimate compositions of those shapes.

Topology scale therefore includes more than total row count. Relevant dimensions include:

- number of logical scopes/tables;
- key cardinality and width;
- parent/child or association fan-out;
- join selectivity and skew;
- optional versus required participation;
- cross-scope Constraint burden;
- whole-result completeness across several distributed constituents;
- amount of state needed to preserve relationship semantics during Learning, Generation, and Evaluation.

A design that scales each table independently but requires the complete relationship structure to be centralized can still violate the enterprise-scale problem.

### Time-series and sequence scale

For ordered/longitudinal subjects, relevant dimensions also include:

- entity/series count;
- observations per entity;
- sequence-length distribution;
- cadence/gap irregularity;
- temporal horizon;
- static/context versus event-varying width;
- cross-time dependency length;
- longitudinal Evaluation and privacy/memorization cost.

Time-series scale must not be reduced to `row count + timestamp` when sequence/entity semantics materially affect behavior.

### Text-bearing structured-data scale

Free-form/source-language text fields inside structured data can dominate data size and computational behavior even when row count is moderate.

Relevant dimensions include:

- text length distribution;
- vocabulary/token diversity;
- multilingual/domain-specific variation where supported;
- sparsity and rare-string behavior;
- memory/state size for source-derived text behavior;
- generation cost;
- semantic/quality Evaluation cost;
- memorization and disclosure-risk evaluation burden.

The baseline self-contained text requirement does not imply that all text can be collected or modeled in one driver-local object, nor does it promise foundation-model-level quality.

### Source partitioning and placement

Enterprise source data will normally already be partitioned and distributed.

The design must consider the semantic and cost consequences of repartitioning, shuffling, scanning, sampling, caching, spilling, and data movement. These are problem consequences, not commitments to specific mechanisms.

### Generated volume

Generation is not assumed to be one-source-row-to-one-output-row.

Supported workflows may need to generate small samples, datasets comparable in size to source, multiple outputs from one Learned State, outputs materially larger than source, several related table/scopes, or many longitudinal sequences.

The product model must therefore not assume that generated data is a small driver-local return value.

### Evaluation volume

Evaluation can require comparing large source and synthetic subjects and may be as expensive as—or more expensive than—Generation.

This includes per-field, cross-field, relational, temporal, downstream-utility, privacy/disclosure, and text-related questions. The design must distinguish methods that can operate distributively from methods requiring bounded samples/summaries and methods whose cost makes them unsuitable for routine large-scale use.

### Runtime duration

Large Learning, Generation, or Evaluation work may run long enough that interactive-function-call assumptions fail.

The design must anticipate durations where actors need progress visibility, durable operational identity, failure diagnosis, cancellation, retry/recovery, reconciliation, and separation of partial material from authoritative semantic results.

No runtime SLO is established here.

### Compute heterogeneity

Some techniques may be CPU-oriented; others may require or benefit from GPUs or other accelerators. Some distribute naturally by data partitions; others may require coordinated model training or specialized text/sequence processing.

The framework must not hide material compute requirements or force all Strategies into an execution pattern that only fits one algorithm family.

### Dependency and distribution closure

Enterprise scale includes the number and heterogeneity of runtime participants. Driver-local availability is not enough when workers/executors perform material work.

Problem-level concerns include:

- environment consistency across distributed roles;
- dynamically admitted/replaced workers;
- large reusable state or locally provisioned artifacts;
- installations that require offline/no-egress operation;
- avoiding hidden per-worker acquisition or remote fallback.

The exact distribution mechanism remains downstream design.

### Concurrency

Enterprise environments may execute multiple Learning, Generation, or Evaluation workloads concurrently.

Exact scheduling and isolation guarantees are deferred, but the design must not depend on global mutable state that makes independent work inherently unsafe to colocate.

### Persistence and durable-result scale

Learned State, summaries, checkpoints, Evidence, Provenance, and generated outputs may vary greatly in size.

The design must preserve the distinction between bounded conceptual/control state and potentially large distributed material without assuming that all durable results belong inside one local serialized object.

## Enterprise operability envelope

Scale also changes non-numeric expectations. Enterprise-scale use implies that the design must account for:

- repeatable committed configuration;
- operational identity and status;
- Provenance and historical explanation;
- inspectable failure and uncertainty;
- resource visibility and admission limitations;
- compatibility/version behavior;
- Evidence supporting quality or privacy claims;
- safe handling of failed, partial, invalidated, or superseded work;
- offline/no-egress and explicit dependency behavior where required;
- operation in managed and self-managed Spark environments where feasible.

These are problem consequences, not architectural solutions.

## Design-center statement

SYNGAN's design center is not the smallest dataset on which an algorithm can be demonstrated. It is a distributed structured-data workflow where source and/or generated material may exceed one machine's practical capacity, may contain meaningful relational/temporal/text semantics, and where Learning, Generation, and Evaluation can be operationally significant work.

## Anti-benchmark rule

The row bands and scale dimensions in this document MUST NOT be advertised as supported performance guarantees until benchmark methodology, representative workload classes, hardware/runtime profiles, Strategy families, and acceptance criteria are defined later.

A statement such as "supports 100 million rows" is incomplete without relevant width, cardinality, topology, sequence/text characteristics, data size, Strategy, cluster resources, runtime, and evaluated outcome quality.

## Consequences for current concept design

Current concept design must be capable of expressing, without prematurely selecting implementation mechanisms:

- semantic interpretation of fields, relationships, topology, and text-bearing roles;
- reusable Strategy capability/limitation differences;
- Learning and reusable Learned State where applicable;
- direct Generation where Learning is not applicable;
- large and multi-part Generation intent/results;
- prescriptive Constraints at field, record, aggregate, relational, and temporal scope where supported;
- scalable Evaluation and bounded Evidence claims;
- durable Provenance and historical interpretation;
- long-running operational Execution, failure, retry/recovery, cancellation, and uncertainty;
- resource/dependency/network limitations that remain visible without becoming hidden semantic defaults.

Whether those responsibilities remain correctly divided among the current eleven concepts is evaluated by Phase 008 rather than assumed by this scale envelope.