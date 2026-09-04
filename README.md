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

Phase 004 architecture now establishes:

- downstream architecture authority with bounded control-plane/distributed-data-plane separation;
- durable typed public specifications, activity handles, result handles, Execution/Attempt inspection, and explicit payload access;
- stable resource identity, immutable semantic revisions/commitment snapshots, conflict-versioned lifecycle state, exact historical resolution, and bounded persistence ownership;
- exact Spark-scale source-state/read binding, distributed manifests, sealed Generation candidates, and one idempotently promoted output without mandatory row copying;
- semantic Strategy/Evaluation-method authority separated from executable implementation bindings and Attempt-scoped runtime realization;
- runtime adapters that consume immutable resolved activity specifications, read exact source/state references, write non-final learned/output/diagnostic material through framework-owned ports, and report runtime facts without domain-completion authority;
- Learned State identity distinct from loaded PyTorch/Spark/statistical objects and compatible with distributed state representations;
- first-class direct Generation without fabricated Learning;
- Evaluation method adapters that preserve coverage/uncertainty/diagnostics and leave Evidence establishment to Evaluation;
- Spark-native structured-data boundaries compatible with non-Spark model runtimes while rejecting ordinary full-corpus driver collection as a generic bridge;
- explicit dependency/network/egress behavior with no hidden runtime acquisition or fallback;
- no universal CTGAN, GAN, PyTorch, Spark ML, Databricks, HuggingFace, LLM, plugin loader, or runtime family assumption.

Architecture decision rationale:

- [`ADR-0001 — Typed Resource/Handle Public API`](docs/decisions/ADR-0001-typed-resource-handle-public-api.md)
- [`ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State`](docs/decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md)
- [`ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion`](docs/decisions/ADR-0003-sealed-manifest-gated-output-promotion.md)
- [`ADR-0004 — Semantic Extension & Runtime Binding Separation`](docs/decisions/ADR-0004-semantic-extension-runtime-binding-separation.md)

Next:

- **004-F — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture**

No final Python package/module tree or exact public class names, database engine, ID encoding, physical persistence schema, Spark table/file provider, source fingerprint/hash algorithm, manifest serialization, plugin discovery mechanism, distributed ML runtime choice, scheduler/orchestrator, checkpoint/fencing implementation, provenance physical store, authorization engine, egress-control technology, model registry, or deployment topology should be treated as settled until the relevant later Phase 004 group accepts it.
