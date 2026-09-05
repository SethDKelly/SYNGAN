# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Phase 005 is planning-only

Phase 005 does **not** authorize production implementation.

During 005-A through 005-K, agents may update planning/governance/documentation artifacts requested by the active group, but MUST NOT create production source, package scaffolds, database schemas/migrations, runtime/Spark/security/platform adapters, Evidence/Provenance stores, verification suites, CI workflows, or deployment infrastructure merely because the future implementation plan describes them.

A Phase 005 group marked `complete` means its plan is complete, not that the planned code exists.

005-K is an explicit Jackson/design-completeness gate. It may require another concept/synchronization/experience/architecture/planning phase. Even a positive 005-K result does not authorize coding; implementation requires a later explicit implementation-authority phase.

## Progressive disclosure

For material work:

1. read `docs/index.md`;
2. read `docs/architecture/phase-004-consolidated-architecture-contract.md`;
3. read `docs/implementation/index.md` and the relevant implementation plan;
4. read the 005-B verification authority and 005-C package/dependency authority;
5. load 005-D through 005-I only when the task touches their specific boundaries;
6. follow only the detailed concept/experience/architecture links needed for the active slice;
7. use ADRs for rationale, not instead of current canonical authority.

Do not load or copy the entire documentation corpus by default.

## Authority order

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation authority / accepted plan
  > code / deployment
  > examples / generated artifacts / runtime state
```

Existing code never overrides upstream authority.

## Topology and dependency rules

The accepted future production topology is rooted at `src/syngan/` with inward responsibilities:

```text
foundation
domain
ports
application
api
adapters
bootstrap
```

Do not create generic god-owners such as `utils`, universal `Context`, `Config`, `Metadata`, `State`, `Result`, `Manager`, `Registry`, or Session-like authority; move concept behavior into `foundation`; make domain/application/API depend on concrete adapters; or pull optional adapter SDKs into base import-time dependencies.

## Durable identity and control plane

005-D establishes one shared identity/version substrate:

```text
AuthorityId
ResourceId
ResourceKind
ResourceRef
RevisionNumber / RevisionRef
SnapshotId
StateVersion
SchemaVersion
```

Do not substitute database IDs, paths, table names, platform run IDs, model IDs, timestamps, Python objects, or one generic `version` field for these roles. Preserve immutable commitments/history, expected-StateVersion CAS, typed historical resolution, and bounded control-plane payloads.

## Spark/data boundary

005-E requires exact SourceStateRef binding, candidate/sealed-snapshot/output separation, bounded manifests and no mandatory full-driver collection on enterprise paths.

Do not treat DataFrame/query/table/path as durable identity; physical schema as Data Meaning; a sealed snapshot as completed Generation; Evidence for one sealed snapshot as proof for another; or a platform/table format as semantic authority.

## Runtime and Learned State

005-F requires separate semantic revision, ImplementationBindingRef, RuntimeSpiVersion, package/build version, state-codec version, representation schema and runtime/platform version axes.

Do not treat plugin discovery as trust/selection, create a global mutable plugin registry, collapse Learning/Generation/Evaluation into one universal `run(context) -> Result`, let runtime establish semantic results, equate loaded runtime objects/checkpoints/candidate representation with logical Learned State, auto-download/install missing dependencies, or require universal driver-local state loading.

## Execution/recovery/fencing

005-G requires stable Execution identity, durable Attempts, monotonic AttemptEpoch, observed-state versus mutation-authority separation, WriterFence/cancellation generation, launch reconciliation, committed checkpoints, explicit recovery modes and operational-versus-semantic completion separation.

Do not substitute lease expiry or scheduler retry for fencing; blindly resubmit unknown external launches; treat checkpoint bytes as resumable checkpoint; let fenced late success become authoritative; double-count repeated Evaluation work; or allow late completion after cancellation won the control-plane race.

## Evidence, Provenance, history and reproducibility

005-H requires owner-side Evidence establishment, immutable finding versus applicability separation, exact Generation completion basis, typed canonical Provenance and non-authoritative bounded query projections.

Do not let runtime metrics/diagnostics become Evidence; inflate claim strength; overwrite Evidence findings; copy large diagnostics into bounded control rows; make graph/search stores canonical Provenance; use mutable/latest aliases in exact history; destructively rewrite assertions; infer causality/quality from structural comparison; or reduce reproducibility to a Boolean/seed.

## Dependency, offline/no-egress and enterprise security

005-I establishes the future dependency/security contract.

Keep these boundaries distinct:

```text
semantic dependency/network/egress requirement
current environmental resolution
identity/integrity/authenticity
trust/approval
activity/runtime compatibility
current authorization
Attempt-scoped capability
```

Agents MUST NOT:

- treat a mutable model/package/path/tag/URI as exact dependency identity without provider guarantees;
- treat resolver discovery as integrity, trust, compatibility or authorization;
- auto-install packages, auto-download models, query public registries, enable telemetry, or switch to hosted/remote fallback during committed runtime;
- treat acquisition success as approval/trust;
- collapse network connectivity, destination, egress category and authorization into one Boolean;
- treat EgressPlan as permission to transmit;
- let broad user/platform permission widen a committed offline/no-egress or narrower network contract;
- treat commit-time permission as permanent future permission for source read, Learned-State use, retry/resume, export, egress or history traversal;
- treat resource-handle possession as authorization;
- inject broad database credentials or unrestricted network clients into runtime adapters when a narrower capability can express the required operation;
- persist bearer secrets/credentials in commitments, invocation state, handles, Evidence, Provenance, manifests, checkpoints, idempotency records, extension bindings or ordinary logs;
- import/execute discovered third-party extension code before required integrity/trust/authorization checks;
- load unsafe/code-executing Learned-State codecs merely because the codec is installed;
- equate Learned-State `use` permission with raw state read/export;
- equate candidate write with candidate read/export;
- equate Evidence summary access with diagnostic access;
- treat Generation completion as output export permission;
- reveal protected resource/edge existence through reverse indexes, counts, pagination totals, search/autocomplete, comparison fields, reproducibility reasons or error messages;
- convert protected-but-existing information to semantic `absent` during redaction;
- rewrite canonical history to satisfy current policy/redaction;
- treat authorization revocation as a replacement for 005-G fencing or vice versa;
- treat security audit as Provenance or telemetry as authorization;
- omit tenant/security-domain context from caches/indexes/runtime capability composition where cross-domain leakage could occur.

The future runtime capability rule is:

```text
runtime capability
=
semantic requirement
∩ current authorization
∩ deployment capability
```

005-I plans a first-class offline/no-egress profile after approved local/private provisioning. 005-J must report deployment incompatibility/limitations when a platform cannot enforce the required containment strongly enough; it must not weaken the profile silently.

## Dependencies and optional integrations

The base/core distribution remains model/platform neutral.

Do not add PySpark, PyTorch, Databricks/cloud SDKs, MLflow/OpenLineage clients, graph databases, remote-model/service clients, CUDA/GPU runtimes, SQLAlchemy/Psycopg, scheduler/IAM/policy/secret-manager SDKs or similar adapter dependencies to base runtime dependencies merely for one slice.

Any dependency requires explicit purpose/classification and compatibility/offline/network/security review.

## Verification

Once coding is explicitly authorized, tests derive their oracle from accepted authority and must not mock away the distributed, concurrency, security, persistence, runtime, recovery, Evidence or history property under test.

Portable/core tests use network denial where applicable. Never retry stochastic tests until green or weaken required architecture-fitness checks outside 005-B governance.

005-I future work primarily owns V9 and AF-02/11/12/14/15/16/17/18. Required scenarios include hidden-acquisition denial, exact dependency mismatch, untrusted/unauthorized dependencies, unsafe-codec denial, non-bearer handles, reauthorization after policy change, revocation plus fencing, secret non-persistence, truthful redaction, protected reverse-query/count behavior, withheld reproducibility reasons, cross-domain isolation, fail-closed authorization uncertainty and socket-denied offline execution.

## Package/import behavior

The root `syngan` import remains side-effect free and must not automatically import optional platform/runtime/persistence/scheduler/security SDKs, scan/load plugins, open network connections, create sessions, inspect credentials, initialize telemetry, acquire dependencies, or create a global mutable Session/Context.

## Documentation synchronization and completion

When a durable implementation decision changes, update canonical `docs/implementation/` authority. If architecture changes, update `docs/architecture/` and ADR rationale explicitly.

Do not claim a Phase 005 slice complete unless its authority mapping, future source-boundary compliance, verification/fitness obligations, dependency/migration/security/network implications and acceptance-evidence requirements are accounted for.

Do not claim production implementation exists merely because a Phase 005 plan is complete. Do not assume 005-K must authorize coding; it may require further Jackson/design refinement.
