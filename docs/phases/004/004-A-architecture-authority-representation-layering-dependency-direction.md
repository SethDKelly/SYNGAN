---
type: Phase Record
title: 004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction
status: complete
---

# 004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction

## Objective

Establish the architecture authority, representation principles, control-plane/data-plane boundary, layering model, dependency direction, portability/platform specialization rules, Spark-native/model-neutral boundaries, anti-bloat rules, and decision-recording discipline that all later Phase 004 architecture work must preserve.

004-A intentionally avoids selecting the final Python package layout, database, scheduler, plugin loader, storage format, security engine, or deployment topology.

## Governing authority

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Accepted Concepts](../../concepts/index.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Experience & Workflow Design](../../experience/index.md)
- [Phase 003 Consolidated Experience Contract](../../experience/phase-003-consolidated-experience-contract.md)
- [Phase 003 Exit](../003/003-I-cross-workflow-consistency-phase-003-consolidation-review.md)
- [Architecture Index](../../architecture/index.md)

## Canonical architecture authority created

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](../../architecture/architecture-authority-representation-layering.md)
- [Architecture Decision Record Index](../../decisions/index.md)

004-A also corrects the documentation-governance authority order so accepted experience contracts explicitly precede architecture. Architecture may report an upstream infeasibility but may not silently override experience merely because the representation is inconvenient.

## Main decisions

### 1. Architecture is downstream authority

The governing direction is:

```text
Design Authority
      ↓
Concepts
      ↓
Synchronizations
      ↓
Experience
      ↓
Architecture
      ↓
Implementation planning / code
```

Architecture owns representation/composition choices. It does not redefine semantic ownership.

If an upstream semantic/experience contract is infeasible, architecture must surface that conflict explicitly and request an upstream revision.

### 2. Representation equivalence requires semantic preservation

An API, database schema, class model, status type, table layout, or platform integration is acceptable only if it preserves material upstream distinctions.

The architecture cannot replace:

- semantic versus operational state;
- prepared versus committed state;
- candidate/checkpoint/diagnostic versus promoted result;
- contextual readiness versus global truth;
- Evaluation success versus Evidence finding;
- historical truth versus current state;
- withheld versus unknown;
- network requirement versus egress authorization;

with convenient but semantically lossy scalar fields.

### 3. Logical identity is independent of physical location

Logical identity and historical distinguishability remain separate from paths, aliases, table names, URLs, registry tags, platform run IDs, or in-memory objects.

Mutable locators may reference state but cannot become sole historical identity when the referenced state may change.

Physical relocation/reserialization may preserve logical identity only if later architecture establishes sufficient integrity/equivalence semantics.

### 4. References are preferred to copied authority

Cross-layer and cross-system representation should use typed stable references plus the minimum contextual information needed for interpretation rather than copying entire canonical states.

This applies particularly to Provenance, platform telemetry, data/output/Learned State payloads, Evidence diagnostics, dependency artifacts, and external catalog/lineage systems.

### 5. Universal status is rejected

004-A explicitly rejects a single universal status enum spanning readiness, domain activities, Evidence, Execution, policy/disclosure, and reproducibility.

Shared primitives are allowed, but owner/context and reason must remain explicit.

`blocked`, `restricted`, `withheld`, and `indeterminate` remain context-specific semantics rather than globally interchangeable values.

### 6. Semantic promotion is distinct from physical durability

Architecture must provide a distinguishable authority transition for:

- Learning -> primary Learned State;
- Generation -> completed logical output;
- Evaluation -> legitimate Evidence findings.

Physical files/tables/checkpoints/diagnostic output can pre-exist promotion.

Repeated physical work is allowed; ambiguous duplicate authoritative results are not.

### 7. Hidden material side effects are prohibited

Architecture must make material network access, dependency acquisition/substitution, egress, semantic commitment, and result promotion explicit.

A missing dependency, cache miss, retry, or runtime failure cannot silently invoke a remote fallback or change the material dependency set.

### 8. Enterprise scale constrains architecture

Ordinary supported workflows must not require full source/output/Learned State/diagnostic/telemetry collection to driver-local memory.

Control-plane state should scale with logical revisions, commitments, summaries, relationships, result references, and material history—not row/task/log volume.

## Control-plane/data-plane decision

004-A accepts a conceptual architecture boundary between a bounded control plane and distributed data plane.

### Control plane

Contains representations of:

- identities and revisions;
- prepared/committed specifications;
- lifecycle transitions;
- contextual readiness/compatibility results;
- bound historical references;
- logical result identities;
- promotion state;
- Execution/Attempt summaries;
- dependency declarations/resolved identities;
- Evidence summaries and claim context;
- typed Provenance relationships;
- reproducibility-relevant retained facts;
- external policy/disclosure result references where applicable.

### Data plane

Contains potentially large/distributed payloads:

- source records;
- candidate/completed generated records;
- physical Learned State components;
- checkpoint/recovery payloads;
- large Evaluation diagnostic datasets;
- large intermediates inappropriate for canonical control-plane state.

### Observability detail

Full platform logs/task metrics/scheduler events remain primarily platform-native, with selected material references/summaries retained in control-plane Execution/Provenance state.

### Boundary invariant

Physical existence in the data plane never establishes semantic authority on its own.

## Layering decision

004-A accepts an **inward dependency principle** without requiring one named architecture framework.

Responsibilities equivalent to these layers must remain distinguishable:

1. **Semantic/control contracts** — portable representation of accepted semantic ownership, identities, commitments, lifecycle and results.
2. **Application coordination** — composes use cases without becoming a new domain owner.
3. **Ports/extension contracts** — contracts for persistence, data references, runtimes, schedulers, history, security hooks and other replaceable capabilities.
4. **Adapters/integrations** — Spark/platform/runtime/vendor implementations of those contracts.
5. **Composition/bootstrap** — deployment-specific wiring of concrete components.

The final package tree may differ, but dependency direction must remain equivalent.

## Dependency-direction decisions

### Inward dependencies

Dependencies point toward stable semantic/control contracts.

Concrete adapters depend on contracts; the semantic/control core does not import concrete adapters.

### Platform semantics do not flow inward

A platform adapter cannot define universal SYNGAN semantics.

Therefore:

- platform run status does not define Execution state;
- Spark job IDs do not define Attempt identity;
- table existence does not define Generation completion;
- model registry state does not define Learned State validity;
- vendor approval fields do not define Evidence or release authority.

### Semantic synchronization does not justify import cycles

The bidirectional domain activity/Execution synchronization must be representable without circular package dependencies.

Contracts, references, events, or another later-approved mechanism may realize the relationship.

### Optional integration isolation

Network-dependent and other optional integrations should remain separable so supported offline/no-egress paths do not require importing/initializing them.

## Spark-native decision

`Spark-native` means distributed Spark-scale source/output behavior and no mandatory driver-local pandas/full-corpus boundary.

It does not mean:

- every concept maps to Spark ML;
- every Strategy must be a Spark estimator/model;
- PyTorch or another runtime is disallowed;
- control-plane state must live in Spark;
- Databricks is mandatory.

The data boundary should interoperate naturally with Spark DataFrames/tables/files while logical result authority remains independent of one DataFrame object.

## Model-neutral decision

The core semantic/control architecture cannot universally depend on CTGAN, GANs, PyTorch, Spark ML, HuggingFace, LLMs, or one model family/runtime.

Strategy/Evaluation implementations sit behind explicit extension/runtime contracts.

Direct-generation Strategies remain valid without fabricated Learning/Learned State.

Learning-based Strategies may establish one logical Learned State backed by multiple physical components.

## Portability decision

Portable semantics/control logic should remain platform-neutral when platform differences do not affect the domain contract.

Platform-specific adapters may add optimized snapshot/catalog/promotion/runtime/scheduler/telemetry/security capabilities.

Portability does not require pretending guarantees are identical. A platform limitation must surface as explicit capability/compatibility/readiness limitation rather than adapter-level semantic weakening.

## Anti-bloat decisions

### No catch-all ownership by naming

Names such as `Context`, `Session`, `Manager`, `Metadata`, `Registry`, `Service`, `Repository`, `State`, `Utils`, or `Engine` do not authorize broad ownership.

Such components are acceptable only with narrow explicit responsibility.

### No one-class-per-concept dogma

Concepts define semantic authority, not mechanical class count.

Several concepts can share representation infrastructure where ownership remains distinguishable; one concept can require multiple components where scale/persistence/runtime/access boundaries justify it.

### No universal workflow/session state owner

A convenience facade can coordinate but cannot become the canonical mutable owner of Data Meaning, Strategy, Learning, Generation, Evaluation, Execution, Evidence, Provenance, dependencies and results simultaneously.

### No metadata shadow model

A generic metadata store/object cannot become a duplicated master copy of all domain state, history, runtime, dependency and result information.

## Architecture decision records

004-A establishes `docs/decisions/` as the home for durable architecture decision rationale and supersession history.

The rule is:

- canonical current architecture rule -> `docs/architecture/`;
- why/alternatives/tradeoffs/supersession -> ADR under `docs/decisions/` when useful;
- design execution history -> `docs/phases/004/`.

An ADR does not outrank upstream semantics/experience or newer canonical architecture authority.

No technology-selection ADR is implied yet.

## Documentation-governance correction

During 004-A, the active documentation-governance precedence was found to place accepted architecture above experience documents, contradicting both the concept-design methodology and the Phase 003 handoff.

The order is corrected to:

```text
authority
  > concepts/synchronizations
  > experience
  > architecture/current ADR rationale
  > phase records
  > summaries/examples
  > backlog/exploration
```

This is a documentation-authority repair, not a semantic model change.

The previously identified strict-OKF metadata normalization concern remains separate governance debt and is not falsely declared resolved by 004-A.

## Architecture validation obligations handed forward

Later architecture/implementation planning must be able to prove or test that:

- lower semantic/control layers do not import concrete platform adapters;
- supported offline paths do not require runtime-network integrations;
- large-data workflows do not require full driver collection;
- semantic commitments remain historically identifiable;
- non-final physical state cannot masquerade as promoted results;
- retry/recovery cannot create duplicate authoritative results;
- public interfaces retain typed status/Evidence/disclosure distinctions;
- mutable aliases are not treated as sufficient historical identity;
- Provenance references rather than duplicates canonical payload/state;
- dependency/network/egress behavior has no hidden fallback/acquisition path;
- platform adapters cannot silently weaken upstream guarantees.

The exact CI/linting/fitness-function tooling is deferred.

## Deferred questions

004-A does not select:

- final Python package/module boundaries;
- public API/resource model;
- persistence engine;
- source/output identity mechanism;
- manifest/hash/fingerprint technology;
- Spark output promotion mechanism;
- runtime/plugin discovery mechanism;
- scheduler/orchestrator;
- checkpoint/fencing/transaction approach;
- provenance store;
- security/policy engine;
- deployment topology;
- Databricks-specific design.

These are assigned to later Phase 004 groups.

## Exit criteria

- [x] architecture authority boundary established;
- [x] architecture/upstream precedence made explicit;
- [x] documentation-governance precedence drift corrected;
- [x] representation-preservation rules established;
- [x] logical identity separated from physical location;
- [x] control-plane/data-plane boundary established;
- [x] inward dependency model established;
- [x] semantic/control, coordination, ports, adapters and composition responsibilities distinguished;
- [x] platform adapter authority inversion prohibited;
- [x] semantic synchronization/import-cycle distinction established;
- [x] optional integration isolation established;
- [x] Spark-native boundary clarified;
- [x] model-neutral boundary clarified;
- [x] portability/platform-specialization rule established;
- [x] anti-bloat/god-module rules established;
- [x] ADR governance established;
- [x] architecture validation obligations defined;
- [x] technology/package choices remain intentionally deferred.

## Exit assessment

**Status: complete.**

SYNGAN now has an accepted architecture constitution that constrains all later representation choices without prematurely fixing package layout or technology. The architecture can proceed to public API/resource mapping knowing which dependencies may point inward, which state belongs in the bounded control plane, which payloads remain distributed, which semantic distinctions may not be collapsed, and how platform/model integrations remain adapters rather than universal authority.

## Next phase

**004-B — Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping**
