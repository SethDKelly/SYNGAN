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
- **004-C — Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture**
- **004-D — Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture**
- **004-E — Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture**
- **004-F — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture**
- **004-G — Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture**
- **004-H — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture**
- **004-I — Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture**

Phase 004 architecture now establishes, among other guarantees:

- bounded control-plane/distributed-data-plane separation and inward dependency direction;
- durable typed resource handles with stable identity independent of client/runtime lifetime;
- immutable commitments plus conflict-versioned lifecycle state;
- exact Spark-scale source-state binding, sealed candidates and idempotent semantic promotion;
- model-neutral Strategy/runtime adapters, including first-class direct Generation;
- one stable Execution across many fenced/reconcilable Attempts with immutable checkpoint recovery state;
- semantic Evidence, typed canonical Provenance and qualified reproducibility rather than generic quality/lineage/status shortcuts;
- explicit dependency identity/trust/authorization and offline/no-egress operation without hidden acquisition or fallback;
- non-bearing handles, scoped runtime capabilities, secret isolation and security-aware historical/query projections;
- portable semantic/application/control contracts with capability-negotiated platform adapters;
- restartable durable-state-first coordinators rather than process-local session authority;
- multi-dimensional enterprise-scale disclosure without unsupported generic row-count promises;
- canonical semantic/operational history separated from detailed runtime telemetry and security audit;
- Databricks as an important managed integration target rather than package/semantic identity;
- generic/self-managed Spark as a legitimate target when required guarantees are supplied;
- non-Spark model runtimes behind scale-compatible distributed bridges;
- multi-axis compatibility across schemas, Strategy/binding/SPI/codec/runtime/platform/dependency versions;
- local/private package/plugin/dependency provisioning for supported offline environments;
- deployment-level enforcement requirements for workload identity, storage scope, secrets, network/egress and tenant/query isolation;
- no universal CTGAN, GAN, PyTorch, Spark ML, Databricks, scheduler, graph database, IAM/policy engine, secret manager, observability vendor, or runtime-family assumption.

Architecture decision rationale is preserved in [`docs/decisions/`](docs/decisions/index.md), currently ADR-0001 through **ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters**.

Next:

- **004-J — Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit**

No final Python package/module tree or exact public class names, database/storage/catalog technology, plugin discovery mechanism, concrete scheduler/orchestrator, provenance query engine, IAM/policy/secret/network stack, observability vendor, exact Databricks API topology, CI/CD design, SLO/SLA values, or benchmark/support-matrix claims should be treated as settled before Phase 004 exits and implementation planning explicitly chooses them.
