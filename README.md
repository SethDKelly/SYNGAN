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

004-A establishes the canonical [`architecture constitution`](docs/architecture/architecture-authority-representation-layering.md): architecture remains downstream of semantic/experience authority; logical identity stays separate from physical/platform locators; bounded control-plane state references distributed data-plane payloads; dependencies point inward; runtime/platform integrations remain adapters; Spark-native means distributed Spark-scale data behavior rather than universal Spark ML; and model/runtime convenience cannot create god-state ownership.

004-B establishes the canonical [`typed public resource/handle architecture`](docs/architecture/public-api-resource-handle-workflow-semantic-mapping.md): editable specifications remain distinct from committed activities; readiness is contextual; committed Learning/Generation/Evaluation and promoted Learned State/output/Evidence expose durable typed identities; Execution remains operationally separate; long-running work is re-resolvable rather than process-Future identity; and payload access remains explicit.

004-C establishes the canonical [`control-plane identity/state architecture`](docs/architecture/control-plane-identity-revision-state-persistence-historical-reference.md):

- stable resource identity is independent of mutable aliases, client objects, physical locations and platform run IDs;
- semantic revision/commitment snapshot, lifecycle state version and representation schema version are separate axes;
- bindable semantic revisions and committed activity snapshots are immutable in material meaning;
- persisted drafts remain distinct from committed Learning/Generation/Evaluation occurrence identity;
- Learned State/output/Evidence identity remains stable while current lifecycle/applicability changes independently;
- material lifecycle writes require stale-write/conflict detection rather than silent last-writer-wins;
- significant transition/audit history is retained without mandating universal event sourcing;
- logical mutation authority remains distinct across semantic revisions, activities, results, Execution/Attempts, Provenance and derived indexes even if one physical database technology is shared;
- coupled semantic transitions require detectable/recoverable consistency across failures;
- exact historical references never silently substitute current/latest state;
- withheld/redacted, unavailable, unknown/indeterminate, invalid-reference and absent states remain distinguishable;
- representation-schema migration does not create new semantic history;
- canonical control-plane persistence remains bounded rather than scaling with every row, task, tensor, diagnostic or log line.

Architecture decision rationale:

- [`ADR-0001 — Typed Resource/Handle Public API`](docs/decisions/ADR-0001-typed-resource-handle-public-api.md)
- [`ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State`](docs/decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md)

Next:

- **004-D — Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture**

No final Python package/module tree or exact public class names, database engine, ID encoding, physical persistence schema, source fingerprint/manifest format, Spark output-promotion mechanism, strategy plugin loader, scheduler/orchestrator, checkpoint/fencing mechanism, provenance physical store, authorization engine, egress-control technology, model registry, or deployment topology should be treated as settled until the relevant later Phase 004 group accepts it.
