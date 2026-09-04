---
type: Architecture Authority
title: Architecture Authority, Representation Principles, Layering & Dependency Direction
status: active
---

# Architecture Authority, Representation Principles, Layering & Dependency Direction

## Purpose

Establish the governing architecture rules that translate SYNGAN's accepted semantic and experience contracts into implementation-facing structures without allowing package, storage, runtime, platform, or API convenience to redefine domain authority.

This document is the canonical Phase 004-A architecture authority. It defines principles and dependency direction, not a final package tree or technology selection.

## Governing authority

Architecture is downstream of:

1. [Design Authority](../authority/index.md);
2. [Accepted Concepts](../concepts/index.md);
3. [Accepted Synchronizations](../synchronizations/index.md);
4. [Experience & Workflow Design](../experience/index.md);
5. [Phase 003 Consolidated Experience Contract](../experience/phase-003-consolidated-experience-contract.md).

When architecture discovers that an upstream contract is infeasible or contradictory, it MUST surface that conflict explicitly and request an upstream design revision. It MUST NOT silently redefine the contract inside architecture.

## Architecture authority boundary

Architecture owns representation and technical composition decisions such as:

- interface and resource boundaries;
- durable identity/reference representation;
- persistence and transaction boundaries;
- control-plane/data-plane separation;
- runtime and adapter boundaries;
- dependency direction;
- extension contracts;
- execution/recovery mechanisms;
- integration boundaries;
- deployment and portability structure.

Architecture does not own the semantic meaning of Data Meaning, Constraint, Synthesis Strategy, Learning, Learned State, Generation, Evaluation Criterion, Evaluation, Evidence, Execution, or Provenance.

One concept does not imply one class, module, service, table, endpoint, or process. Conversely, one implementation component MAY support several concepts if authority remains explicit and non-conflicting.

## Core representation principles

### 1. Semantic preservation before convenience

A representation is acceptable only if actors and programmatic users can still determine the distinctions required by upstream authority.

Architecture MUST preserve, where material:

- editable/prepared versus committed state;
- semantic versus operational lifecycle;
- checkpoint/candidate/diagnostic versus promoted result;
- contextual readiness/compatibility versus canonical shared state;
- Evaluation success versus Evidence finding;
- historical truth versus current state;
- reproduction assessment versus re-execution;
- dependency requirement/availability/identity/permission/network/egress distinctions;
- absent/unknown/unavailable/withheld/redacted distinctions.

A convenient representation that erases one of these distinctions is not equivalent.

### 2. Stable logical identity over physical location

Logical SYNGAN identities MUST remain distinguishable from mutable physical locations and platform-native identifiers.

A file path, table name, URL, registry alias, Spark job ID, Databricks run ID, or object-memory address MAY be a locator/reference but MUST NOT become the sole semantic identity where the referenced state can change materially.

Relocation or reserialization MAY preserve logical identity only when later architecture can establish the required equivalence/integrity contract.

### 3. References over copied authority

Cross-boundary relationships SHOULD carry stable references and the minimum typed context required to interpret them rather than duplicate the full state of another authority owner.

This applies especially to:

- Provenance;
- Execution/Attempt platform references;
- Learned State payload location;
- output materialization;
- Evidence diagnostics;
- dependency artifacts;
- source snapshots;
- external catalog/lineage integrations.

A reference architecture MUST NOT create a shadow source of truth merely to simplify joins or API responses.

### 4. Typed state instead of universal status

Architecture MAY reuse shared primitives for lifecycle values, errors, or result envelopes, but owner/context MUST remain explicit.

There MUST NOT be one universal `status` enum whose values ambiguously mix readiness, Learning, Generation, Evaluation, Evidence applicability, Execution, policy, disclosure, and reproducibility state.

Similarly, generic `success`, `failed`, `blocked`, `restricted`, or `indeterminate` representations MUST retain the owning context and reason.

### 5. Semantic promotion is an authority transition

Physical durability is not semantic promotion.

Architecture MUST provide a distinguishable authoritative transition for:

- Learning -> primary Learned State;
- Generation -> completed logical output;
- Evaluation -> legitimate Evidence finding(s).

The mechanism may later use transactions, manifests, fencing, compare-and-set, catalog state, or another technique, but duplicate physical work MUST NOT create ambiguous duplicate authoritative results.

### 6. No hidden side effects

Operations that may materially affect network access, dependency acquisition/substitution, data egress, semantic commitment, or result promotion MUST be explicit in the architectural contract.

A missing dependency, cache miss, retry, or platform failure MUST NOT silently trigger remote acquisition, materially different fallback, or expanded egress.

### 7. Enterprise scale is architectural, not optional tuning

Ordinary supported workflows MUST NOT require collecting full source/output/Learned State/diagnostic/telemetry payloads into driver-local memory.

Control-plane state SHOULD remain bounded by material semantic/activity/history facts and stable references, not row/task/log volume.

### 8. Convenience facades do not own canonical state

A future high-level API MAY make common workflows concise, but convenience facades/builders/sessions MUST delegate to the same canonical contracts used by lower-level interfaces.

They MUST NOT become alternate semantic owners or hide material committed state permanently.

## Control-plane and data-plane boundary

SYNGAN architecture distinguishes a **control plane** from a **distributed data plane**.

This is an architectural boundary, not a new domain concept.

### Control plane

The control plane contains bounded state needed to define, coordinate, inspect, and explain SYNGAN work, including representations of:

- stable logical identities and revisions;
- draft/prepared/committed activity specifications;
- lifecycle transitions;
- contextual readiness/compatibility outcomes;
- exact bound references at commitment;
- logical Learned State/output/Evidence identities;
- result/promotion state;
- Execution/Attempt summaries and platform references;
- dependency declarations and resolved identities;
- Evidence summaries/claim-strength context;
- typed Provenance relationships;
- reproducibility-relevant retained facts;
- disclosure/policy result references where external authority supplies them.

Control-plane state MAY reference large physical data but SHOULD NOT absorb it by default.

### Distributed data plane

The data plane contains potentially large or distributed payloads such as:

- source records;
- generated/candidate/completed output records;
- Learned State physical components;
- checkpoints and recovery payloads;
- detailed Evaluation diagnostic datasets;
- large intermediate summaries/materializations when not appropriate for canonical control-plane storage.

The data plane MAY use Spark-native distributed objects/tables/files or other later-approved distributed representations.

### Platform observability detail

Full task logs, executor metrics, scheduler events, and similar platform telemetry remain primarily platform-native operational detail. The control plane retains selected material references/summaries rather than copying complete telemetry.

### Boundary invariant

A data-plane payload becoming physically present does not by itself change its semantic authority. Promotion occurs through the owning control-plane transition.

## Layering model

004-A accepts an inward dependency principle without mandating a specific named framework such as hexagonal, clean, onion, or layered architecture.

The architecture MUST preserve responsibilities equivalent to the following layers.

### Layer A — semantic/control contracts

Contains portable representations/contracts for accepted semantic ownership, identity, lifecycle, commitments, results, and cross-concept coordination.

This layer MUST NOT depend on concrete Spark platform integrations, Databricks APIs, PyTorch training implementations, remote model services, specific databases, schedulers, or security vendors.

It MAY define abstractions required to refer to distributed data and external capabilities without importing their concrete implementation authority.

### Layer B — application coordination

Coordinates use cases such as preparation, commitment, promotion, historical inspection, and operational handoff using Layer A contracts.

Application coordination MAY combine multiple concepts to execute an experience workflow but MUST NOT become a new domain owner.

This layer depends inward on Layer A contracts and outward only through explicit ports/contracts.

### Layer C — ports and extension contracts

Defines implementation-facing contracts for capabilities whose concrete realization varies, such as:

- persistence;
- source/output reference resolution;
- distributed materialization;
- Strategy runtime execution;
- Evaluation methods;
- Execution/scheduler realization;
- dependency/artifact resolution;
- provenance/history storage/query;
- authorization/disclosure hooks;
- observability/platform references.

A port describes what the core needs, not the API of a preferred vendor.

### Layer D — adapters and integrations

Contains concrete integrations with technologies/platforms such as Spark storage/catalogs, PyTorch runtimes, Databricks, schedulers, external lineage systems, artifact registries, security/policy systems, or optional remote services.

Adapters depend on the contracts they implement. The semantic/control layer MUST NOT depend back on concrete adapters.

### Layer E — composition/bootstrap

Selects concrete adapters and deployment configuration for a particular runtime/deployment profile.

The composition boundary MAY depend on multiple concrete components because its purpose is wiring. It MUST NOT become a new semantic state owner.

## Dependency direction rules

### Inward dependency rule

Dependencies flow toward stable semantic/control contracts.

Conceptually:

```text
composition/bootstrap
        ↓
adapters/integrations
        ↓
ports/extension contracts
        ↓
application coordination
        ↓
semantic/control contracts
```

Actual package structure MAY differ, but the dependency direction and authority boundaries MUST remain equivalent.

### No adapter-to-core authority inversion

A platform adapter MUST NOT force the core to adopt the platform's lifecycle, identity, retry, storage, or permission semantics as universal SYNGAN semantics.

Examples:

- Databricks run status does not define Execution state;
- Spark job IDs do not define Attempt identity;
- Delta table existence does not define Generation completion;
- MLflow model registration does not define Learned State validity;
- a provider's `approved` flag does not define SYNGAN Evidence or release authority.

### No cyclic package dependency requirement

A bidirectional semantic synchronization does not justify a circular module dependency.

In particular, Activity <-> Execution coordination MUST be representable through contracts/events/references or another later-approved mechanism without requiring semantic modules to import one another cyclically.

### Optional integration isolation

Runtime-network-dependent or otherwise optional integrations SHOULD be separable so that installing/importing/using the supported offline core does not automatically activate or require them.

The exact packaging mechanism is deferred, but dependency direction MUST make an offline/no-egress core feasible.

## Spark-native architecture boundary

`Spark-native` in SYNGAN means large structured/tabular source and output workflows are designed around distributed Spark-scale data movement and computation rather than mandatory driver-local pandas/materialization.

It does NOT mean:

- every concept maps to Spark ML;
- every Strategy implementation must be a Spark estimator/model;
- PyTorch or another runtime is prohibited;
- control-plane state must be stored in Spark;
- Databricks is the only deployment target.

The data boundary SHOULD interoperate naturally with Spark DataFrames/tables/files while retaining logical identities and semantic promotion independently of one DataFrame object.

## Model-neutral architecture boundary

SYNGAN's semantic/control and public workflow architecture MUST NOT make CTGAN, GANs, PyTorch, Spark ML, HuggingFace, LLMs, or another model/runtime family a universal prerequisite.

Strategy and Evaluation implementations are capabilities behind explicit extension/runtime contracts.

A direct-generation Strategy MUST remain possible without fabricated Learning/Learned State architecture.

A Learning-based Strategy MUST be able to persist a logical Learned State composed of one or many physical components without equating that state with a single framework object.

## Portability and platform specialization

### Portable core

Where semantic behavior does not depend on a platform, the relevant control contracts and application logic SHOULD remain portable.

### Platform adapters

Platform-specific capabilities MAY provide:

- optimized source snapshot/reference integration;
- table/catalog promotion;
- distributed runtime execution;
- scheduler integration;
- telemetry links;
- credential/security hooks;
- managed artifact storage;
- deployment conveniences.

Such adapters MAY expose additional platform-native detail but MUST preserve the common semantic contract.

### Capability differences stay explicit

Portability does not require pretending every platform can provide identical guarantees.

If a platform cannot provide a required identity, fencing, reproducibility, no-egress, or disclosure guarantee, the limitation MUST remain explicit in compatibility/readiness rather than being hidden by an adapter.

## Anti-bloat and anti-god-module rules

Architecture MUST resist consolidating unrelated authority into catch-all components.

### Prohibited catch-all ownership

Names such as `Context`, `Session`, `Manager`, `Metadata`, `Registry`, `Service`, `Repository`, `State`, `Utils`, or `Engine` do not justify broad ownership by themselves.

Such components MAY exist only with a narrow, explicit responsibility and MUST NOT become the sole store/orchestrator for unrelated semantic state merely for convenience.

### Module boundary test

A proposed module/component SHOULD have:

- one coherent responsibility/volatility boundary;
- explicit owned representation state, if any;
- clear inward/outward dependencies;
- a reason it can evolve independently;
- no need to reinterpret upstream semantic authority.

### No one-class-per-concept dogma

Concept boundaries guide authority and testing, not mechanical class count.

Several concepts MAY share representation infrastructure when ownership remains distinguishable. One concept MAY require multiple implementation components when scale, persistence, runtime, or access boundaries justify them.

### No universal workflow/session object

A convenience workflow/session facade MAY coordinate operations but MUST NOT become the canonical owner of Data Meaning, Strategy, Learning, Generation, Evaluation, Execution, Evidence, Provenance, dependency policy, and results in one mutable object.

### No metadata shadow model

Architecture MUST NOT create a generic metadata object/database that becomes a duplicated master copy of all concept state, provenance, runtime state, dependency data, and results.

## Architecture decision discipline

Material architecture decisions MUST be traceable to upstream purpose/constraint and one current canonical architecture authority.

Use [Architecture Decision Records](../decisions/index.md) when a decision benefits from durable alternatives/rationale/supersession history.

An ADR records **why** a decision was taken and what it supersedes; canonical architecture documents record the current accepted rule.

Architecture changes SHOULD therefore:

1. identify upstream authority/requirement;
2. state alternatives considered where material;
3. record the accepted representation choice;
4. document compatibility/migration consequences;
5. update canonical architecture authority;
6. create/update an ADR when durable rationale is useful;
7. mark replaced architecture/ADR material superseded rather than leaving active contradictions.

## Architecture validation obligations

Later implementation/planning MUST be able to validate at least the following architectural properties:

- lower semantic/control layers do not import concrete platform adapters;
- optional network integrations are not required by supported offline core paths;
- ordinary large-data workflows do not require full driver collection;
- material commitments are immutable/historically identifiable;
- candidate/checkpoint/diagnostic state cannot be mistaken for promoted results;
- retry/recovery cannot create duplicate authoritative semantic results;
- public/programmatic interfaces preserve typed status and Evidence distinctions;
- mutable aliases are not sufficient historical identity where content can change;
- Provenance references rather than duplicates canonical payload/state;
- dependency/network/egress behavior has no hidden fallback/acquisition path;
- platform-specific adapters cannot silently weaken semantic guarantees.

Exact linting, test tooling, package import rules, CI enforcement, and fitness functions are deferred to later architecture/implementation planning.

## Deferred decisions

004-A intentionally does not yet choose:

- Python package/module names;
- public class hierarchy;
- repository/service implementation pattern;
- database/storage engine;
- event bus/queue;
- transaction/locking mechanism;
- Spark table/file/catalog technology;
- manifest/hash/fingerprint scheme;
- scheduler/orchestrator;
- strategy plugin loader;
- PyTorch distribution mechanism;
- model registry;
- provenance store;
- authorization/policy engine;
- deployment topology;
- Databricks-specific implementation.

These are addressed by later Phase 004 groups under the rules established here.

## Architecture invariants

1. Architecture MUST remain downstream of authority, concepts, synchronizations, and experience contracts.
2. Representation convenience MUST NOT redefine semantic ownership.
3. One concept MUST NOT be assumed to equal one class/module/table/service.
4. Logical identity MUST remain distinguishable from physical location/platform identity.
5. Control-plane state SHOULD remain bounded and reference large distributed payloads rather than absorb them.
6. Data-plane physical existence MUST NOT imply semantic promotion.
7. Dependency direction MUST point toward stable semantic/control contracts.
8. Concrete platform/runtime adapters MUST NOT become dependencies of the semantic/control core.
9. Bidirectional semantic synchronization MUST NOT require cyclic package dependencies.
10. Spark-native MUST mean distributed Spark-scale data semantics, not universal Spark ML implementation.
11. Model-neutral core semantics MUST NOT depend universally on CTGAN/GAN/PyTorch/LLM/model-hub behavior.
12. Supported offline/no-egress core paths MUST remain architecturally feasible without optional runtime-network integrations.
13. Hidden dependency acquisition, remote fallback, or egress MUST NOT be introduced by adapters.
14. Convenience facades MAY compose workflows but MUST NOT own unrelated canonical state.
15. Architecture MUST preserve typed lifecycle/status/disclosure context rather than collapsing it into universal scalars.
16. Provenance/integration architecture MUST prefer typed stable references over copied authority.
17. Platform specialization MAY add capability but MUST NOT silently weaken common guarantees.
18. Enterprise-scale architecture MUST NOT require ordinary full-corpus/output/model/log driver-local materialization.
19. Material architecture decisions MUST remain traceable to upstream authority and current canonical architecture documentation.
20. Deferred technology choices MUST remain explicitly deferred until their Phase 004 group resolves them.
