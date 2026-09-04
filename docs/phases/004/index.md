---
type: Phase Index
title: Phase 004 — Representation & Architecture Design
status: active
---

# Phase 004 — Representation & Architecture Design

Phase 004 translates SYNGAN's accepted concept, synchronization, and experience contracts into coherent implementation-facing architecture without allowing representation convenience to redefine semantic ownership.

## Entry authority

- [Design Authority](../../authority/index.md)
- [Accepted Concepts](../../concepts/index.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Experience & Workflow Design](../../experience/index.md)
- [Phase 003 Consolidated Experience Contract](../../experience/phase-003-consolidated-experience-contract.md)
- [Architecture Authority](../../architecture/index.md)
- [004-A Architecture Constitution](../../architecture/architecture-authority-representation-layering.md)
- [004-B Public API/Resource Architecture](../../architecture/public-api-resource-handle-workflow-semantic-mapping.md)

## Groups

| Group | Scope | Status |
|---|---|---|
| **004-A** | [**Architecture Authority, Representation Principles, Layering & Dependency Direction**](004-A-architecture-authority-representation-layering-dependency-direction.md) | **complete** |
| **004-B** | [**Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping**](004-B-public-api-resource-handle-workflow-semantic-mapping.md) | **complete** |
| **004-C** | **Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture** | **next** |
| 004-D | Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture | planned |
| 004-E | Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture | planned |
| 004-F | Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture | planned |
| 004-G | Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture | planned |
| 004-H | Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture | planned |
| 004-I | Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture | planned |
| 004-J | Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit | planned |

## Completed architecture refinement

### 004-A

004-A established the canonical [Architecture Authority, Representation Principles, Layering & Dependency Direction](../../architecture/architecture-authority-representation-layering.md).

Key accepted architecture rules include:

- architecture is downstream of authority, concepts, synchronizations, and experience;
- documentation-governance precedence was corrected so architecture cannot override experience silently;
- representation must preserve material semantic/experience distinctions;
- stable logical identity remains independent of mutable physical/platform locators;
- cross-boundary architecture prefers typed stable references over copied authority;
- universal status/state/session/metadata representations cannot erase owner/context;
- semantic promotion remains distinct from physical durability;
- a bounded control plane is distinct from the distributed data plane;
- large source/output/Learned State/checkpoint/diagnostic payloads remain outside canonical control-plane storage by default;
- architecture follows an inward dependency principle without mandating one named framework;
- semantic/control, application coordination, ports/extension contracts, adapters/integrations, and composition/bootstrap responsibilities remain distinguishable;
- concrete platform/runtime adapters do not become dependencies of the semantic/control core;
- bidirectional semantic synchronization does not justify cyclic package dependencies;
- optional network/runtime integrations should remain isolatable from supported offline/no-egress paths;
- Spark-native means distributed Spark-scale data behavior, not universal Spark ML;
- model-neutral architecture does not universally depend on CTGAN/GAN/PyTorch/HuggingFace/LLM/runtime families;
- platform specialization may add capability but cannot silently weaken common guarantees;
- catch-all Context/Session/Manager/Metadata/Registry/Service/Repository/Engine objects cannot gain broad authority by naming alone;
- convenience facades may compose workflows but cannot become alternate canonical state owners;
- ADR governance is established under [`docs/decisions/`](../../decisions/index.md) for durable rationale/supersession history;
- enterprise-scale architecture must avoid ordinary full driver-local source/output/model/diagnostic/log materialization.

### 004-B

004-B established [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../../architecture/public-api-resource-handle-workflow-semantic-mapping.md) and [ADR-0001 — Typed Resource/Handle Public API](../../decisions/ADR-0001-typed-resource-handle-public-api.md).

Key accepted architecture rules include:

- editable Learning/Generation/Evaluation specifications remain distinct from committed activity identity;
- pre-commit readiness/compatibility is an inspectable contextual result, not global semantic state;
- committed Learning/Generation/Evaluation expose durable typed activity-handle roles;
- Learned State, completed synthetic output, and Evidence expose durable promoted result roles distinct from physical/runtime payloads;
- checkpoint/recovery, partial/candidate output, and diagnostic material remain explicitly non-final subordinate representations;
- one logical Execution handle exposes ordered Attempt history independently of platform jobs;
- handles represent stable logical identity and resolve canonical state rather than becoming mutable client-side authority;
- semantic commitment and operational submission remain distinct transitions even when combined by convenience APIs;
- long-running work is re-resolvable and does not use process-local Future/promise identity as the canonical lifecycle;
- completed output payload access is explicit and Spark/distributed rather than payload identity replacing output authority;
- Learned State loading is runtime-specific and cannot replace logical Learned State identity;
- convenience `fit`/`generate`-style façades may exist but must expose the durable underlying activity/result resources;
- public status/issues remain typed by semantic/operational/policy/disclosure context rather than one global enum;
- typed resource navigation follows stable references without copying authority into a mutable object graph;
- human/programmatic surfaces map to equivalent semantic roles;
- universal mutable Session/Context/Result/Registry/Model/DataFrame abstractions are rejected as canonical state ownership.

004-B intentionally does not yet choose exact class/method spellings, identifier format, persistence technology, handle serialization, REST schema, async primitives, or payload-resolution mechanisms.

## Phase 004 guardrails

Phase 004 MUST NOT:

- redesign accepted concept semantics merely to simplify package structure;
- erase experience distinctions behind generic API status/metadata/session objects;
- make one runtime/platform mandatory unless the semantic contract requires it;
- force ordinary enterprise source/output materialization to driver-local memory;
- make network/resource acquisition implicit;
- treat physical storage existence as semantic promotion;
- equate platform exactly-once claims with SYNGAN semantic promotion;
- turn Provenance into a shadow copy of all domain/runtime data;
- make security redaction falsify historical existence;
- create package dependency cycles merely because semantic synchronizations are bidirectional;
- make process-local object/Future identity the durable identity of distributed work;
- jump prematurely into implementation task breakdown before architecture boundaries are accepted.

## Phase 004 exit target

Phase 004 should leave SYNGAN with enough accepted representation/architecture authority that Phase 005 can map:

```text
concept / experience contract
        ↓
architecture boundary / interface
        ↓
module / implementation slice
        ↓
tests / acceptance evidence
```

without reopening core semantics.

## Current next phase

**004-C — Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture**
