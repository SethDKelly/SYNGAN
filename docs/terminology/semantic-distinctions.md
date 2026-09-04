---
type: Semantic Distinction Register
title: SYNGAN Semantic Distinctions
status: active
---

# SYNGAN Semantic Distinctions

## Purpose

This document records domain distinctions that later concept, experience, architecture, API, and test design MUST preserve unless an explicit design decision supersedes them.

These are semantic guardrails, not a concept catalog.

## Core distinctions

### Source data != source representation

The logical data supplied to synthesis is distinct from the DataFrame, table, files, partitions, or storage system that currently represent it.

A later API MAY use Spark DataFrames as a primary representation without redefining the domain meaning of source data.

### Structural schema != data semantics

Physical/logical field structure does not fully encode domain meaning.

A string may be a free-text value, identifier, constrained code, category, timestamp encoding, or reference. Later design MUST NOT assume that physical dtype alone is sufficient semantic evidence.

### Declared semantics != inferred semantics

Semantics explicitly supplied or approved by an authoritative actor are distinct from semantics inferred by software from observed data.

Inference MAY assist configuration, but an inferred interpretation MUST remain distinguishable from a declared interpretation where that distinction affects behavior, trust, or governance.

### Synthesis != training

Synthesis is the broader production problem. Training is one possible learning mechanism within some synthesis strategies.

A strategy that uses distributions, rules, sketches, deterministic transforms, or other methods may synthesize data without neural-network training.

### Learning != generation

Deriving reusable source-informed state is distinct from using applicable state and intent to produce synthetic records.

The two may occur in one workflow, but later design MUST preserve their differing lifecycle and evidence implications when those matter.

### Learned state != implementation object

Reusable source-derived information is a domain idea. The Python object, Spark ML model, neural module, serialized file, checkpoint directory, or distributed state that represents it is an implementation choice.

### Model family != learned state != artifact

A model family identifies an algorithmic approach. Learned state is source-derived reusable information. An artifact is a durable materialization.

One artifact MAY contain learned state associated with a model family, but the terms are not interchangeable.

### Condition != constraint != filter

- A **condition** expresses desired characteristics during generation.
- A **constraint** expresses a rule outputs must satisfy.
- A **filter** selects among records that already exist.

A system MAY implement one using another internally, but that implementation MUST NOT silently erase the user-visible semantic difference.

### Generate != source sampling

Producing synthetic records is distinct from selecting a subset of source records.

The overloaded verb `sample` MUST be qualified when ambiguity exists.

### Synthetic != anonymized != private

Synthetic origin does not automatically establish anonymity or privacy.

Any privacy, anonymization, or disclosure-safety claim requires its own scope and evidence.

### Fidelity != utility != validity != privacy/disclosure risk

These answer different questions:

- **fidelity** — how well selected source properties are reproduced;
- **utility** — how useful the data is for a stated downstream purpose;
- **validity** — whether applicable structural/domain rules hold;
- **privacy/disclosure risk** — what sensitive information may be exposed under a stated scope or threat model.

No one dimension is a substitute for the others.

### Metric != criterion != decision

A metric measures something. A criterion defines what is being judged. An acceptance/release/use decision applies policy or judgment to evidence.

Later design MUST NOT allow a metric result to masquerade as an automatic governance decision unless policy explicitly makes it so.

### Evidence != claim

Evidence can support a claim; it is not the claim itself.

Claims SHOULD identify the scope under which evidence is considered sufficient.

### Execution != attempt

A logical body of requested work may have multiple attempts because of retries or recovery.

Later lifecycle design SHOULD preserve enough identity to distinguish retries when auditability, recovery, cost, or provenance depends on it.

### Checkpoint != final artifact

Intermediate recoverable state is not automatically suitable as a portable or approved final artifact.

### Provenance != lineage

Lineage captures derivational relationships. Provenance is broader and may additionally capture configuration, software identity, actor/authority context, execution circumstances, and evidence history.

### Reproducibility != determinism

Exact repeatability is one possible reproducibility target, not the only one.

Distributed or stochastic methods MAY support a weaker but explicit reproducibility contract without being fully deterministic.

### Distributed != scalable

Distributing computation can still yield unacceptable shuffles, coordinator bottlenecks, memory growth, runtime, artifact growth, or evaluation cost.

A scalability claim must be scoped to an explicit workload envelope and required behavior.

### Driver-local != forbidden

Small control-plane state, configuration, summaries, or coordination MAY appropriately be driver-local.

The risk arises when state or computation grows with the corpus without a bounded or justified design.

### Spark-native != Spark-only

Spark-native workflow continuity does not require every mathematical operation to be implemented inside Spark primitives.

Later architecture may legitimately use external runtimes, accelerators, native libraries, or distributed ML systems provided the framework preserves its Spark-facing scale and lifecycle obligations.

### Platform portability != identical execution

A portable framework may use different physical execution strategies on different compatible platforms while preserving the same domain semantics and documented guarantees.

## Concept-discovery use

001-D MUST use these distinctions as tests against premature merging.

If two candidate responsibilities fall on opposite sides of one of these distinctions, combining them into a single concept requires explicit justification rather than convenience of implementation.
