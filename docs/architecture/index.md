---
type: Architecture Index
title: SYNGAN Representation & Architecture Design
status: active
---

# SYNGAN Representation & Architecture Design

## Purpose

This directory is the canonical home for representation and architecture decisions that map SYNGAN's accepted semantic and experience contracts into modules, interfaces, identities, persistence boundaries, data/reference models, runtime integrations, execution/recovery mechanisms, provenance/evidence structures, security/disclosure controls, and deployment/platform architecture.

Architecture remains downstream of design authority, accepted concepts/synchronizations, and experience authority. Representation/runtime convenience MUST NOT redefine semantic ownership.

## Current canonical architecture authority

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md) — Phase 004-A architecture constitution.
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](public-api-resource-handle-workflow-semantic-mapping.md) — Phase 004-B typed public resource/handle architecture.
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md) — Phase 004-C durable identity/state/persistence architecture.
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md) — Phase 004-D distributed source/candidate/output architecture.
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](strategy-extension-learning-generation-evaluation-runtime-adapter.md) — Phase 004-E extension/runtime architecture.
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md) — Phase 004-F operational continuation architecture.

Decision rationale/history is preserved under [Architecture Decision Records](../decisions/index.md). Current normative architecture remains here under `docs/architecture/`.

## Accepted architecture baseline

Later architecture MUST preserve at least:

- logical identity remains distinct from physical location, runtime object, and platform job identity;
- bounded control-plane state references distributed payloads rather than absorbing them;
- semantic revisions/commitment snapshots remain immutable while current lifecycle state is conflict-versioned;
- Spark DataFrames/table/path/query aliases remain access/locator representations, not durable source/output identity;
- committed source-dependent work binds stable exact source-state/read boundaries;
- Generation candidates seal exact immutable snapshots before completion Evaluation/promotion;
- sealing and physical durability do not establish semantic completion;
- required Evaluation binds exact immutable subject/reference identities;
- semantic promotion is separately fenced/idempotent and need not require physical row copying;
- Strategy/method semantic authority remains separate from executable implementation binding;
- runtime invocation is immutable per Attempt and runtime adapters cannot directly establish semantic results;
- Learned State remains distinct from checkpoints and loaded model/runtime objects;
- direct-generation Strategies remain first-class;
- Execution remains one logical operational authority across many Attempts/platform runs;
- write-capable Attempts receive supersedable ordered epochs/fencing generations;
- at most one Attempt epoch holds current framework mutation authority per Execution boundary;
- lease/liveness coordination does not replace stale-writer fencing;
- duplicate physical computation is permitted while duplicate canonical authority is prohibited;
- idempotency is scoped to the protected operation/semantic target and does not bypass fencing;
- committed checkpoints are immutable recovery snapshots and checkpoint existence does not imply resume eligibility;
- retry/resume safety remains contextual to exact committed semantics and side-effect state;
- unknown platform/side-effect state remains explicit until reconciled or safely fenced;
- external unfenceable/undeduplicable ambiguity may block automatic retry;
- Evaluation retries must not accidentally double-count logical work units;
- cancellation is durable intent followed by reconciled operational outcome, not instantaneous domain-state rewrite;
- automatic retry has no authority shortcut around semantic/dependency/no-egress/cancellation checks;
- platform specialization may add capability but cannot silently weaken common guarantees;
- enterprise-scale workflows cannot require ordinary full driver-local source/output/Learned-State/diagnostic/telemetry materialization.

## Active ADR rationale

- [ADR-0001 — Typed Resource/Handle Public API](../decisions/ADR-0001-typed-resource-handle-public-api.md)
- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](../decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md)
- [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](../decisions/ADR-0003-sealed-manifest-gated-output-promotion.md)
- [ADR-0004 — Semantic Extension & Runtime Binding Separation](../decisions/ADR-0004-semantic-extension-runtime-binding-separation.md)
- [ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution](../decisions/ADR-0005-attempt-epoch-fencing-recoverable-at-least-once-execution.md)

## Phase 004 status

**Phase 004 — Representation & Architecture Design** is current.

Completed:

- [004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction](../phases/004/004-A-architecture-authority-representation-layering-dependency-direction.md)
- [004-B — Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../phases/004/004-B-public-api-resource-handle-workflow-semantic-mapping.md)
- [004-C — Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../phases/004/004-C-control-plane-identity-revision-state-persistence-historical-reference-architecture.md)
- [004-D — Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../phases/004/004-D-spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion-architecture.md)
- [004-E — Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../phases/004/004-E-strategy-extension-learning-generation-evaluation-runtime-adapter-architecture.md)
- [004-F — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](../phases/004/004-F-execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-architecture.md)

Next:

**004-G — Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture**

## Representation boundary

No final Python package layout/class spelling, database technology, Spark table/file provider, manifest/hash technology, plugin discovery mechanism, distributed-ML runtime choice, scheduler/orchestrator, concrete checkpoint/fencing implementation, provenance physical store, authorization engine, or deployment topology is accepted merely because Phase 004 is active.
