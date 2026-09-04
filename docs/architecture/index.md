---
type: Architecture Index
title: SYNGAN Representation & Architecture Design
status: active
---

# SYNGAN Representation & Architecture Design

## Purpose

This directory is the canonical home for representation and architecture decisions that map SYNGAN's accepted semantic and experience contracts into modules, interfaces, identities, persistence boundaries, data/reference models, runtime integrations, execution/recovery mechanisms, provenance/evidence structures, security/disclosure controls, and deployment/platform architecture.

Architecture is downstream of:

1. [Design Authority](../authority/index.md)
2. [Accepted Concepts](../concepts/index.md)
3. [Accepted Synchronizations](../synchronizations/index.md)
4. [Experience & Workflow Design](../experience/index.md)
5. [Phase 003 Consolidated Experience Contract](../experience/phase-003-consolidated-experience-contract.md)

Architecture may choose representations and technical composition. It MUST NOT redefine an upstream semantic/experience contract merely because one class, module, table, API, service, runtime, or platform primitive is convenient.

## Current canonical architecture authority

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md) — Phase 004-A architecture constitution.
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](public-api-resource-handle-workflow-semantic-mapping.md) — Phase 004-B public typed resource/handle architecture.
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md) — Phase 004-C durable identity/state/persistence architecture.
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md) — Phase 004-D distributed source/candidate/output architecture.
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](strategy-extension-learning-generation-evaluation-runtime-adapter.md) — Phase 004-E extension/runtime architecture separating semantic authority, implementation binding, Attempt-scoped invocation, runtime results, and semantic promotion.

Decision rationale/history is preserved under [Architecture Decision Records](../decisions/index.md). Current normative architecture remains here under `docs/architecture/`.

## Accepted architecture baseline

Later architecture MUST preserve at least:

- authority flows from design authority -> concepts/synchronizations -> experience -> architecture;
- representation convenience and runtime convenience never redefine semantic ownership;
- logical identity remains distinct from physical location, Python/runtime object identity, and platform job identity;
- bounded control-plane state references rather than absorbs large distributed payloads;
- committed semantic snapshots remain immutable while current lifecycle state is conflict-versioned;
- semantic revision, lifecycle state version, and representation/schema versions remain distinct;
- exact historical references do not silently substitute current/latest state;
- Spark DataFrames/table/path/query aliases are access/locator representations, not durable source/output identity;
- committed source-dependent work binds a stable exact source-state/read boundary;
- source/output/Learned State/diagnostic materialization remains distributed and avoids ordinary full driver collection;
- manifests and state codecs remain representation mechanisms rather than semantic owners;
- Generation candidates seal an exact immutable snapshot before completion Evaluation/promotion relies on them;
- sealing/physical durability does not establish semantic completion;
- required Evaluation binds exact immutable subject/reference identities;
- semantic promotion is separately fenced/idempotent and need not require physical row copying;
- editable specifications, committed activities, Execution/Attempts, non-final material, and promoted results remain typed/distinguishable;
- Strategy/method semantic authority remains distinct from executable implementation binding;
- implementation bindings may narrow but cannot silently broaden semantic capability;
- exact material implementation/runtime/dependency identity remains attributable when behavior/reproducibility depends on it;
- Attempt runtime invocation preserves one exact committed semantic context;
- runtime adapters report facts/write non-final material through ports and do not directly complete domain activities or create Evidence/result authority;
- checkpoints/intermediate learned material remain distinct from Learned State;
- Learned State remains a logical result distinct from PyTorch/Spark/statistical runtime objects and may remain distributed;
- direct-generation Strategies remain first-class without fabricated Learning;
- Generation runtimes write through candidate sinks and cannot publish completed output directly;
- Evaluation method runtimes return measurements/coverage/uncertainty/diagnostics rather than universal pass/fail or Evidence authority;
- platform jobs/processes remain subordinate to SYNGAN Execution/Attempt identity;
- optional runtime-network integrations remain isolatable from supported offline/no-egress paths;
- missing dependencies/runtime implementations do not trigger hidden downloads or remote fallback;
- Spark-native means distributed Spark-scale data semantics, not universal Spark ML or driver-local pandas bridging;
- model-neutral means no universal CTGAN/GAN/PyTorch/HuggingFace/LLM/runtime assumption;
- platform specialization may add capability but cannot silently weaken common guarantees.

For rationale, see:

- [ADR-0001 — Typed Resource/Handle Public API](../decisions/ADR-0001-typed-resource-handle-public-api.md)
- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](../decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md)
- [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](../decisions/ADR-0003-sealed-manifest-gated-output-promotion.md)
- [ADR-0004 — Semantic Extension & Runtime Binding Separation](../decisions/ADR-0004-semantic-extension-runtime-binding-separation.md)

## Phase 004 status

**Phase 004 — Representation & Architecture Design** is current.

See [Phase 004 index](../phases/004/index.md).

Completed:

- [004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction](../phases/004/004-A-architecture-authority-representation-layering-dependency-direction.md)
- [004-B — Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../phases/004/004-B-public-api-resource-handle-workflow-semantic-mapping.md)
- [004-C — Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../phases/004/004-C-control-plane-identity-revision-state-persistence-historical-reference-architecture.md)
- [004-D — Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../phases/004/004-D-spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion-architecture.md)
- [004-E — Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../phases/004/004-E-strategy-extension-learning-generation-evaluation-runtime-adapter-architecture.md)

Next:

**004-F — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture**

## Representation boundary

No final Python package layout/class spelling, database technology, Spark table/file provider, manifest/hash technology, plugin discovery mechanism, PyTorch/distributed-runtime choice, scheduler/orchestrator, checkpoint/fencing implementation, provenance physical store, authorization engine, or deployment topology is accepted merely because Phase 004 is active.

Those choices are resolved incrementally by later Phase 004 groups under the canonical authorities above.
