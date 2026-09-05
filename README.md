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

Phase 004 architecture now establishes:

- bounded control-plane/distributed-data-plane separation and inward dependency direction;
- durable typed specifications, committed activity/result handles, Execution/Attempt inspection, and explicit payload access;
- stable resource identity, immutable semantic revisions/commitment snapshots, conflict-versioned lifecycle state, exact historical resolution, and bounded persistence ownership;
- exact Spark-scale source-state/read binding, distributed manifests, sealed Generation candidates, and one idempotently promoted output without mandatory row copying;
- Strategy/Evaluation-method semantic authority separated from executable implementation binding and Attempt-scoped runtime realization;
- runtime adapters that read exact resolved inputs and write only non-final learned/output/diagnostic material through framework-owned ports;
- Learned State identity distinct from checkpoints and loaded PyTorch/Spark/statistical runtime objects;
- first-class direct Generation without fabricated Learning;
- one stable logical Execution spanning many Attempts/platform runs;
- ordered Attempt epochs/fencing generations that revoke stale framework mutation authority;
- lease/liveness coordination separated from stale-writer fencing;
- operation-scoped idempotency for launches, checkpoint commits, candidate seals, Evaluation aggregation, semantic promotion, and cancellation;
- immutable checkpoint snapshots with contextual resume qualification rather than file-existence semantics;
- durable unknown-state handling and explicit retry/resume/reconcile/cannot-continue recovery outcomes;
- Evidence established only after Evaluation semantic validation, with idempotent independent finding identities and immutable historical finding semantics;
- exact Generation promotion history retaining the candidate/requirement/Criterion/Evidence basis actually used;
- canonical typed Provenance assertions over stable references without copying canonical resource payloads;
- append/supersede Provenance correction and recoverable consistency with material transitions;
- historical explain/compare query services using rebuildable derived indexes rather than a master metadata graph;
- qualified current reproducibility assessment assembled from historical identity, dependencies, runtime, randomness, approximation, representation-equivalence, and material recovery facts;
- explicit dependency requirement/resolution/integrity/trust/authorization distinctions rather than a single availability/permission flag;
- offline/no-egress operation after approved local provisioning with no hidden model/package acquisition or remote fallback;
- network capability separated from typed data-egress authorization;
- action-oriented current authorization that can change without rewriting historical semantic commitments;
- durable resource handles as identifiers rather than bearer credentials;
- Attempt runtimes receiving scoped data/dependency/network/secret capabilities instead of broad ambient enterprise authority;
- independently protected source, Learned State, candidate/output, Evidence-diagnostic, Provenance and historical-query access;
- secret references/brokered short-lived credentials rather than persisted bearer secret values;
- actor-specific truthful withholding/redaction with `absent`, `unknown`, `unavailable`, and `withheld` distinctions;
- security-aware historical/query/reproducibility projections that cannot bypass canonical access boundaries;
- retry/recovery security revalidation plus Attempt fencing under revocation;
- multi-security-domain/tenant isolation even when physical persistence/index/cache infrastructure is shared;
- security audit separated from Provenance and canonical domain truth;
- no universal CTGAN, GAN, PyTorch, Spark ML, Databricks, HuggingFace, LLM, scheduler, graph database, IAM/policy engine, secret manager, or runtime-family assumption.

Architecture decision rationale:

- [`ADR-0001 — Typed Resource/Handle Public API`](docs/decisions/ADR-0001-typed-resource-handle-public-api.md)
- [`ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State`](docs/decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md)
- [`ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion`](docs/decisions/ADR-0003-sealed-manifest-gated-output-promotion.md)
- [`ADR-0004 — Semantic Extension & Runtime Binding Separation`](docs/decisions/ADR-0004-semantic-extension-runtime-binding-separation.md)
- [`ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution`](docs/decisions/ADR-0005-attempt-epoch-fencing-recoverable-at-least-once-execution.md)
- [`ADR-0006 — Typed Canonical Provenance & Derived Historical Projections`](docs/decisions/ADR-0006-typed-provenance-canonical-derived-history-projections.md)
- [`ADR-0007 — Explicit Dependency Resolution & Scoped Capability Security`](docs/decisions/ADR-0007-explicit-dependency-resolution-scoped-capability-security.md)

Next:

- **004-I — Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture**

No final Python package/module tree or exact public class names, database engine, ID encoding, physical persistence schema, Spark table/file provider, source fingerprint/hash algorithm, manifest serialization, plugin discovery mechanism, distributed ML runtime choice, scheduler/orchestrator, concrete checkpoint/fencing implementation, provenance physical store/query engine, IAM/policy engine, secret manager, egress-control technology, artifact repository, model registry, or deployment topology should be treated as settled until the relevant later Phase 004 group accepts it.
