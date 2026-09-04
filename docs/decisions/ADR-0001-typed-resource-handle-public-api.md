---
type: Architecture Decision Record
title: ADR-0001 — Typed Resource/Handle Public API
status: active
---

# ADR-0001 — Typed Resource/Handle Public API

## Decision context

SYNGAN must provide an ergonomic Python/programmatic surface for long-running Spark-scale synthetic-data workflows while preserving the semantic distinctions established in Phases 001–003.

Several superficially convenient public models would erase those distinctions:

- one mutable `Session`/`Context` owning all workflow state;
- `fit()` returning only a runtime model object;
- `generate()` returning only a DataFrame;
- one generic `Result`/`status` object for semantic, operational, Evidence, policy, and reproducibility state;
- process-local futures/promises as the identity of long-running work.

The architecture must also survive client/process/cluster turnover, expose historical commitments, and keep large data/model payloads outside bounded control-plane objects.

## Governing authority

- [Phase 003 Consolidated Experience Contract](../experience/phase-003-consolidated-experience-contract.md)
- [Architecture Authority, Representation Principles, Layering & Dependency Direction](../architecture/architecture-authority-representation-layering.md)
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../architecture/public-api-resource-handle-workflow-semantic-mapping.md)

## Decision

Adopt a **typed resource/handle public architecture** with separate representation roles for:

1. editable specification values;
2. contextual readiness/compatibility results;
3. committed Learning/Generation/Evaluation activity handles;
4. promoted Learned State/completed-output/Evidence result resources;
5. logical Execution handles with subordinate Attempt views;
6. explicitly non-final checkpoint/candidate/diagnostic descriptors;
7. derived Provenance/history/reproducibility/dependency/disclosure views.

Handles represent stable logical identity and resolve canonical state. They are not the canonical mutable state themselves and do not depend on one client process, SparkSession, platform job object, or local Future remaining alive.

High-level convenience façades are allowed, but they must delegate to the same resource model and must not make raw payloads the sole representation of successful work.

## Alternatives considered

### Universal mutable workflow/session object

Rejected as the canonical model.

It would tend to accumulate Data Meaning, Strategy, Learning, Generation, Evaluation, Execution, Evidence, Provenance, dependency state, and results in one mutable authority surface, recreating the god-object problem rejected upstream.

A narrow client/session façade may still exist for connection/configuration ergonomics if it does not own canonical domain state.

### Payload-first API

Examples include `fit() -> model` and `generate() -> DataFrame` as the complete public contract.

Rejected as the canonical model because payloads cannot by themselves express commitment identity, semantic versus operational lifecycle, candidate versus promoted state, Evidence obligations, Provenance, or current restrictions.

Payload convenience access remains supported through result handles.

### Spark ML estimator/model as universal abstraction

Rejected because direct-generation Strategies need not have Learning/Learned State and non-Spark-ML runtimes such as distributed PyTorch may be legitimate Strategy implementations.

Compatibility adapters remain possible.

### One generic polymorphic resource/result type

Rejected as the primary public model because it would encourage universal `status`, loosely typed metadata, and accidental interchange among activity, operational, result, Evidence, policy, and reproducibility semantics.

Shared internal protocols/transport envelopes remain possible if public semantic roles stay typed.

### Process-local asynchronous future as work handle

Rejected as canonical identity because long-running work must survive client/process turnover and be re-resolvable from durable logical identity.

Blocking/future-like helpers may exist as convenience over durable activity handles.

## Consequences

### Positive

- Preserves Phase 003 semantic barriers in the public API.
- Supports durable long-running work independent of client process lifetime.
- Keeps Spark-scale payloads separate from bounded control-plane resources.
- Makes candidate/checkpoint/result authority hard to confuse accidentally.
- Supports both direct-generation and Learning-based Strategies.
- Allows ergonomic façades without creating alternate state ownership.
- Enables Python, CLI, REST, notebook, and future UI surfaces to map to the same resource semantics.
- Supports future persistence, authorization, and historical inspection architecture cleanly.

### Costs / tradeoffs

- The public API is richer than a simple `fit/sample` library.
- Users who only want a DataFrame may need one additional dereference/read step unless a convenience façade combines it.
- More typed status/result structures must be maintained and documented.
- Client implementations need resource refresh/re-resolution behavior.
- Later persistence/API versioning must preserve stable handle/reference compatibility.

These costs are accepted because collapsing the model would lose semantics required for enterprise correctness, auditability, recovery, and scale.

## Compatibility and migration impact

No existing released Python API exists, so there is no user-facing migration requirement yet.

Future compatibility façades may expose SDV/Spark-ML-like ergonomics, but they must map into this resource architecture and preserve inspectability of the underlying committed activity/result.

## Canonical architecture affected

- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../architecture/public-api-resource-handle-workflow-semantic-mapping.md)

## Supersession

Supersedes: none.

Superseded by: none.
