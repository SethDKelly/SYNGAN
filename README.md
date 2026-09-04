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

004-A establishes the canonical [`architecture constitution`](docs/architecture/architecture-authority-representation-layering.md): architecture remains downstream of semantic/experience authority; logical identity stays separate from physical/platform locators; bounded control-plane state references distributed data-plane payloads; dependencies point inward; runtime/platform integrations remain adapters; Spark-native means distributed Spark-scale data behavior rather than universal Spark ML; and model/runtime convenience cannot create god-state ownership.

004-B establishes the canonical [`typed public resource/handle architecture`](docs/architecture/public-api-resource-handle-workflow-semantic-mapping.md): editable specifications remain distinct from committed activities; readiness is contextual; committed Learning/Generation/Evaluation and promoted Learned State/output/Evidence expose durable typed identities; Execution remains operationally separate; long-running work is re-resolvable rather than process-Future identity; and payload access remains explicit.

004-C establishes the canonical [`control-plane identity/state architecture`](docs/architecture/control-plane-identity-revision-state-persistence-historical-reference.md): stable resource identity is separate from semantic revision/commitment snapshot, lifecycle state version, and representation schema version; immutable history and exact reference resolution are preserved; material writes use conflict detection; logical persistence ownership remains bounded and explicit; and coupled semantic transitions must be recoverably consistent.

004-D establishes the canonical [`Spark data boundary and distributed materialization architecture`](docs/architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md):

- Spark DataFrames, table names, paths, queries, and aliases are access/locator forms rather than durable source/output identity;
- committed source-dependent work resolves an exact stable source-state/read boundary through provider snapshots, materialized snapshots, manifests, fingerprints with explicit strength, or equivalent authority;
- source snapshotting/manifesting remains distributed and does not require full-corpus driver collection;
- structural Spark/storage schema remains distinct from Data Meaning;
- manifests use bounded control-plane roots plus distributed component indexes/provider snapshots where needed;
- Generation candidate materialization remains non-final while open and must establish an immutable sealed candidate before required completion Evaluation or promotion relies on it;
- sealing proves the exact physical subject and declared integrity/extent, not Generation semantic completion;
- completion Evidence binds the exact sealed candidate;
- stale writers must be fenceable and duplicate physical computation may occur without duplicate authority;
- Generation promotion is a separate idempotent/fenced transition that yields at most one completed logical output;
- promotion may reuse the sealed candidate's physical bytes and does not universally require copying hundreds of millions of rows;
- completed-output identity remains distinct from Spark DataFrame/table/file layout and arbitrary downstream Spark transformations;
- physical representation changes preserve one output identity only under explicit equivalence/integrity semantics;
- no concrete Spark table/file provider, hash algorithm, manifest serialization, or writer-fencing technology is yet selected.

Architecture decision rationale:

- [`ADR-0001 — Typed Resource/Handle Public API`](docs/decisions/ADR-0001-typed-resource-handle-public-api.md)
- [`ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State`](docs/decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md)
- [`ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion`](docs/decisions/ADR-0003-sealed-manifest-gated-output-promotion.md)

Next:

- **004-E — Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture**

No final Python package/module tree or exact public class names, database engine, ID encoding, physical persistence schema, Spark table/file provider, source fingerprint/hash algorithm, manifest serialization, strategy plugin loader, scheduler/orchestrator, checkpoint/fencing implementation, provenance physical store, authorization engine, egress-control technology, model registry, or deployment topology should be treated as settled until the relevant later Phase 004 group accepts it.
