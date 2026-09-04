# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project is deliberately completing conceptual design before implementation. Daniel Jackson's concept-design methodology governs discovery and specification, and canonical design knowledge is maintained as an OKF 0.2 bundle.

## Design documentation

Start with [`docs/index.md`](docs/index.md).

## Current status

**Phase 001 — Design Foundation & Concept Discovery is complete.**

**Phase 002 — Concept Specification & Invariant Refinement is complete.**

Phase 002 closed with eleven accepted concepts, fifteen synchronization rules, offline/no-outbound-network-capable core semantics, stable commitment/historical binding, semantic result promotion, typed Provenance, qualified reproducibility, and enterprise-scale no-full-driver-materialization requirements.

**Phase 003 — Experience & Workflow Design is complete.**

The [Phase 003 Consolidated Experience Contract](docs/experience/phase-003-consolidated-experience-contract.md) freezes readiness/commitment, semantic/operational, promotion, Evidence, historical/current, reproducibility, dependency/network/egress, disclosure, programmatic-parity, and enterprise-scale experience obligations.

**Current phase: Phase 004 — Representation & Architecture Design.**

See [`docs/architecture/index.md`](docs/architecture/index.md) and [`docs/phases/004/index.md`](docs/phases/004/index.md).

Completed:

- **004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction**
- **004-B — Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping**

004-A establishes the canonical [`architecture constitution`](docs/architecture/architecture-authority-representation-layering.md): architecture remains downstream of semantic/experience authority; logical identity stays separate from physical/platform locators; bounded control-plane state references distributed data-plane payloads; dependencies point inward; runtime/platform integrations remain adapters; Spark-native means distributed Spark-scale data behavior rather than universal Spark ML; and model/runtime convenience cannot create god-state ownership.

004-B establishes the canonical [`typed public resource/handle architecture`](docs/architecture/public-api-resource-handle-workflow-semantic-mapping.md):

- editable Learning/Generation/Evaluation specifications remain distinct from committed activity identities;
- readiness/compatibility is contextual and inspectable rather than global mutable state;
- committed activities expose durable typed handles that survive client/process turnover;
- Learned State, completed synthetic output, and Evidence are promoted result resources distinct from model/DataFrame/metric payloads;
- checkpoint/candidate/diagnostic material remains explicitly non-final;
- Execution and ordered Attempt history remain operationally distinct from domain semantic state;
- semantic commitment and operational submission remain separate transitions even when a convenience call combines them;
- blocking/future-style helpers may exist, but process-local Future identity is not the canonical identity of long-running work;
- payload access is explicit and Spark/distributed-scale safe rather than requiring driver collection;
- `fit`/`generate`-style conveniences may exist without making runtime models/DataFrames the sole public contract;
- one universal Session/Context/Result/Registry/Model/status object is rejected as canonical ownership.

Decision rationale: [`ADR-0001 — Typed Resource/Handle Public API`](docs/decisions/ADR-0001-typed-resource-handle-public-api.md).

Next:

- **004-C — Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture**

No final Python package/module tree or exact public class names, persistence engine, identifier/version format, handle serialization, Spark output-manifest/promotion mechanism, strategy plugin loader, scheduler/orchestrator, checkpoint/fencing mechanism, provenance store, authorization engine, egress-control technology, model registry, or deployment topology should be treated as settled until the relevant later Phase 004 group accepts it.
