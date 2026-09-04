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

Architecture may choose representations and technical composition. It MUST NOT redefine an upstream semantic/experience contract merely because one class, module, table, API, service, or platform primitive is convenient.

If architecture discovers upstream infeasibility, it must surface the conflict explicitly for upstream revision.

## Current canonical architecture authority

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md) — Phase 004-A architecture constitution covering semantic-preserving representation, stable logical identity, control-plane/data-plane separation, inward dependency direction, ports/adapters/composition responsibilities, Spark-native/model-neutral boundaries, portability, anti-bloat rules, ADR discipline, and validation obligations.
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](public-api-resource-handle-workflow-semantic-mapping.md) — Phase 004-B public representation architecture covering editable specifications, contextual readiness, committed activity handles, promoted result handles, subordinate non-final/operational views, long-running identity, payload separation, typed statuses/issues, and convenience façade boundaries.
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md) — Phase 004-C durable control-plane architecture covering stable typed identity, immutable semantic revisions/commitment snapshots, versioned mutable lifecycle state, persistence ownership, concurrency, exact historical resolution, correction, schema migration, and bounded derived indexes.
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md) — Phase 004-D distributed data-plane architecture covering stable source-state resolution, Spark DataFrame access boundaries, bounded/distributed manifests, candidate materialization/sealing, exact Evaluation subject binding, writer-fencing obligations, and one idempotently promoted completed output.

Decision rationale/history is preserved under [Architecture Decision Records](../decisions/index.md) when a material choice warrants an ADR. Current normative architecture remains here under `docs/architecture/`.

## Accepted architecture baseline

Later architecture MUST preserve at least:

- authority flows from design authority -> concepts -> synchronizations -> experience -> architecture;
- representation convenience never redefines semantic ownership;
- logical identity remains distinct from physical location/platform identity;
- bounded control-plane state references rather than absorbs large distributed payloads;
- physical data/checkpoint/diagnostic existence does not imply semantic promotion;
- dependency direction points toward stable semantic/control contracts;
- concrete platform/runtime adapters do not become dependencies of the semantic/control core;
- bidirectional semantic synchronization does not justify circular package dependencies;
- optional/runtime-network integrations remain isolatable from supported offline/no-egress paths;
- Spark-native means distributed Spark-scale data semantics, not universal Spark ML;
- model-neutral means no universal CTGAN/GAN/PyTorch/HuggingFace/LLM/runtime assumption;
- convenience facades may compose workflows but do not own unrelated canonical state;
- editable specification values remain distinct from committed activity identities;
- readiness/compatibility remains contextual and derived;
- committed activities and promoted results expose durable typed resource/handle roles;
- checkpoint/candidate/diagnostic material remains explicitly non-final;
- Execution/Attempt state remains separately inspectable from parent semantic activity state;
- long-running work is re-resolvable rather than process-Future identity;
- payload access is explicit and downstream of result authority;
- resource identity, semantic revision/commitment snapshot, lifecycle state version, and representation schema version remain distinct;
- bindable semantic revisions and committed snapshots are immutable in material meaning;
- current lifecycle/applicability state advances through owner-specific conflict-detectable transitions;
- silent last-writer-wins is prohibited for material authority changes;
- exact historical references never silently substitute current/latest state;
- known withheld/unavailable history is not flattened to ordinary absence/null;
- logical persistence ownership remains explicit even if multiple owners share one physical database technology;
- derived indexes/read models do not become canonical write authority;
- required coupled semantic transitions have detectable/recoverable consistency;
- Spark DataFrames/table/path aliases remain access/locator representations rather than durable historical source/output identity;
- mutable source selectors resolve to stable exact source-state/read boundaries before committed work relies on them;
- source snapshotting/manifesting and output materialization remain distributed and do not require full driver collection;
- physical structural schema remains separate from Data Meaning authority;
- manifests remain representation mechanisms with bounded control-plane roots and optional distributed component indexes;
- candidate materialization must seal an immutable exact snapshot before required completion Evaluation or promotion relies on it;
- sealing establishes physical identity/integrity, not Generation semantic completion;
- Evidence used for Generation completion binds the exact sealed candidate;
- open/sealed-unpromoted/quarantined candidate material does not appear as normal completed output;
- stale writers must be fenceable and duplicate physical work must not create ambiguous candidate membership;
- Generation promotion is a separately idempotent/fenced transition yielding at most one completed logical output;
- semantic promotion may reuse candidate bytes in place and does not universally require copy-on-promotion;
- completed-output identity remains independent of Spark DataFrame/table/file layout and arbitrary downstream transformations;
- physical representation changes preserve an output identity only under explicit equivalence/integrity semantics;
- platform-specific adapters may add capability but cannot silently weaken common guarantees;
- enterprise-scale workflows cannot require ordinary full driver-local source/output/model/diagnostic/log materialization.

For decision rationale, see:

- [ADR-0001 — Typed Resource/Handle Public API](../decisions/ADR-0001-typed-resource-handle-public-api.md)
- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](../decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md)
- [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](../decisions/ADR-0003-sealed-manifest-gated-output-promotion.md)

## Phase 004 status

**Phase 004 — Representation & Architecture Design** is current.

See [Phase 004 index](../phases/004/index.md).

Completed:

- [004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction](../phases/004/004-A-architecture-authority-representation-layering-dependency-direction.md)
- [004-B — Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../phases/004/004-B-public-api-resource-handle-workflow-semantic-mapping.md)
- [004-C — Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../phases/004/004-C-control-plane-identity-revision-state-persistence-historical-reference-architecture.md)
- [004-D — Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../phases/004/004-D-spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion-architecture.md)

Next:

**004-E — Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture**

## Representation boundary

No final Python package layout/class spelling, database technology, concrete Spark storage/table format, source fingerprint/hash algorithm, manifest serialization, writer-fencing mechanism, provenance physical store, scheduler/orchestrator, strategy plugin loader, security engine, or deployment topology is accepted merely because Phase 004 is active.

Those choices are resolved incrementally by later Phase 004 groups under the accepted architecture authorities above.
