# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project is deliberately completing conceptual, architectural, and implementation planning before coding is treated as implementation-complete. Daniel Jackson's concept-design methodology governs discovery/specification, and canonical knowledge is maintained as an OKF-oriented bundle.

## Documentation

Start with [`docs/index.md`](docs/index.md).

For implementation planning, the primary authority chain is:

- [`Phase 003 Consolidated Experience Contract`](docs/experience/phase-003-consolidated-experience-contract.md)
- [`Phase 004 Consolidated Architecture Contract`](docs/architecture/phase-004-consolidated-architecture-contract.md)
- [`Implementation Planning & Delivery Authority`](docs/implementation/index.md)

Repository-wide automated-agent rules are in [`AGENTS.md`](AGENTS.md).

## Current status

- **Phase 001 — Design Foundation & Concept Discovery: complete**
- **Phase 002 — Concept Specification & Invariant Refinement: complete**
- **Phase 003 — Experience & Workflow Design: complete**
- **Phase 004 — Representation & Architecture Design: complete**

## Current phase

**Phase 005 — Implementation Planning & Delivery Decomposition is current and planning-only.**

See [`docs/phases/005/index.md`](docs/phases/005/index.md).

Completing a Phase 005 group means its future implementation plan is complete. No production package, schema, migration, runtime/security/platform adapter, Evidence/Provenance store, test suite, CI workflow, or deployment infrastructure is created merely by completing these planning groups.

Completed:

- **005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement**
- **005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**
- **005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement**
- **005-D — Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan**
- **005-E — Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan**
- **005-F — Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan**
- **005-G — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan**
- **005-H — Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan**
- **005-I — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan**

Canonical implementation-planning authority is under [`docs/implementation/`](docs/implementation/index.md).

### Implementation-planning baseline through 005-I

The future implementation is planned around:

- one `src/syngan` package with inward `foundation`, `domain`, `ports`, `application`, `api`, `adapters`, and `bootstrap` boundaries;
- one durable ResourceRef/revision/state/schema model shared across downstream slices;
- exact distributed source-state/candidate/sealed-snapshot/output identity;
- model-neutral Strategy/method binding and activity-specific runtime contracts;
- Learned-State logical identity separated from representation, codec and loaded runtime object;
- one stable Execution with multiple Attempts, epoch fencing, launch reconciliation, checkpoint/recovery and cancellation/completion linearization;
- owner-established Evidence, typed canonical Provenance and bounded derived historical/reproducibility views;
- dependency availability, exact identity, integrity/authenticity, trust/approval, compatibility and current authorization kept distinct;
- no hidden runtime package/model acquisition, remote fallback, public-registry lookup, telemetry or egress;
- a first-class offline/no-egress profile after approved local/private provisioning;
- action-oriented authorization and Attempt-scoped capabilities rather than handle-as-credential authority;
- non-secret SecretRef values with ephemeral bearer credentials resolved at use time;
- separate permissions for source, Learned-State use/raw-read/export, candidate/output, diagnostics and history/query actions;
- truthful redaction/withholding across canonical records, reverse indexes, counts, comparison and reproducibility reasons;
- security audit kept separate from Provenance and telemetry;
- tenant/security-domain isolation across control/data/history/cache/runtime surfaces;
- optional Spark/PyTorch/runtime/platform capability families without making any framework or platform semantic authority.

No production implementation has begun.

## Jackson/design completeness gate

The project does **not** assume that reaching the end of Phase 005 automatically means coding should begin.

005-K must explicitly audit whether concept discovery/specification, synchronizations, experience design, architecture and implementation planning are sufficiently complete under the Jackson methodology. If gaps remain, another design-refinement phase is the correct next step.

Even a positive 005-K readiness result still requires a later explicit implementation-authority phase before production coding begins.

Next:

- **005-J — Deployment/Platform Adapters, Observability, Compatibility, Scale & Performance Implementation Plan**

005-J will plan concrete deployment/platform capability profiles for runtime launch, storage, workload identity, secrets, network isolation, private dependency distribution, observability/audit, compatibility, HA, backup/restore, scale and performance—while surfacing unsupported guarantees rather than weakening the common architecture contract.
