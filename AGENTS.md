# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Phase 005 is planning-only

Phase 005 does **not** authorize production implementation.

During 005-A through 005-K, agents may update planning/governance/documentation artifacts requested by the active group, but MUST NOT create production source, package scaffolds, database schemas/migrations, runtime/Spark/platform adapters, Evidence/Provenance stores, verification suites, CI workflows, or deployment infrastructure merely because the future implementation plan describes them.

A Phase 005 group marked `complete` means its plan is complete, not that the planned code exists.

005-K is an explicit Jackson/design-completeness gate. It may require another concept/synchronization/experience/architecture/planning phase. Even a positive 005-K result does not authorize coding; implementation requires a later explicit implementation-authority phase.

## Start with authority, not repository-wide scanning

For any material task:

1. read `docs/index.md`;
2. read `docs/architecture/phase-004-consolidated-architecture-contract.md`;
3. read `docs/implementation/index.md` and the implementation authority relevant to the task;
4. read `docs/implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md`;
5. read `docs/implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md`;
6. for public handles/specs, durable identity, canonical state, persistence, transactions, historical resolution or migrations, read `docs/implementation/public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md`;
7. for Spark/data references, exact source state, manifests, candidates, sealed snapshots or output promotion, read `docs/implementation/spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md`;
8. for executable bindings, extension discovery, runtime invocation, Learning/Generation/Evaluation adapters or Learned-State physical representation/loading, read `docs/implementation/strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md`;
9. for Execution/Attempt lifecycle, writer authority, launch reconciliation, checkpoints, retry/resume/recovery, cancellation or operational completion, read `docs/implementation/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-plan.md`;
10. for Evidence establishment, Generation completion basis, Provenance, explain/compare/history query or reproducibility assessment, read `docs/implementation/evaluation-evidence-provenance-historical-query-reproducibility-plan.md`;
11. follow only the detailed concept/experience/architecture links needed for the active slice;
12. use ADRs for rationale when necessary, not as a replacement for current canonical authority.

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

Existing code does not override upstream authority. If implementation appears incompatible with an accepted contract, identify the conflict explicitly rather than silently redefining it in code.

## Current source topology contract

The accepted future production topology is rooted at `src/syngan/` with top-level responsibilities:

```text
foundation
domain
ports
application
api
adapters
bootstrap
```

Dependency direction is inward.

Agents MUST NOT:

- move concept-owned behavior into `foundation` merely to avoid an import boundary;
- create generic `utils`, `Context`, `Config`, `Metadata`, `State`, `Result`, `Manager`, `Registry`, or Session-like ownership as a shortcut;
- make `domain` depend on ports/application/API/adapters/bootstrap;
- make application/API depend on concrete adapters;
- make optional adapter SDKs import-time requirements of the base package;
- bypass Import Linter/architecture fitness by adding broad ignored imports without an accepted boundary revision.

`bootstrap` may wire the full graph but does not own canonical state.

## Foundational toolchain plan

When a later phase explicitly authorizes implementation, use the accepted baseline: Python >=3.11, `pyproject.toml`, uv + committed `uv.lock`, Hatchling, pytest + Hypothesis + pytest-socket, Ruff, mypy, Import Linter, coverage diagnostics and GitHub Actions.

Tool changes are governed implementation decisions.

## Durable identity and control-plane rules

005-D establishes one identity/version substrate for all later slices:

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

Do not use database IDs, paths, table names, Spark/Databricks run IDs, model IDs, timestamps or Python object identity as canonical ResourceId; overload one generic `version`; make ORM rows canonical resources; mutate immutable commitments; use last-writer-wins; silently resolve exact historical refs to latest; collapse typed resolution outcomes into `None`; put data-plane payloads or bearer secrets into bounded control records.

Material lifecycle mutation uses owner validation plus expected `StateVersion` CAS. Transactional outbox/durable-intent records are technical coordination state, not Provenance, Execution, or semantic completion.

## Spark/data-boundary rules

005-E establishes the future data-boundary plan.

Do not treat DataFrame/query/table/path as durable identity, confuse physical schema with Data Meaning, store mandatory per-file control rows, equate candidate/sealed snapshot with completed output, reuse Evidence across different sealed subjects, require a second full copy for metadata-only promotion, omit the writer-fence seam, or make a provider/table format semantic authority.

Enterprise paths must not require complete source/output/component collection on the driver merely to establish identity, sealing, promotion or payload access.

## Runtime extension and Learned-State rules

005-F establishes the future executable extension boundary.

Keep Strategy/method revision, ImplementationBindingRef revision, RuntimeSpiVersion, implementation package/build version, Learned-State codec/version, representation SchemaVersion and runtime/platform version distinct.

Agents MUST NOT treat discovered entry points as trusted/selected authority; create a global mutable plugin registry; eager-load optional runtimes; collapse all runtime activities into generic `run(context) -> Result`; expose unrestricted canonical repositories to adapters; let runtime success establish semantic results; equate checkpoint/candidate representation/loaded model with Learned State; fabricate Learning for direct Generation; choose one universal state format; require universal full-driver state loading; silently alter committed invocation semantics; auto-install/download missing runtime artifacts; or choose concrete launcher semantics inside the SPI.

## Execution/recovery/fencing rules

005-G establishes the future operational-realization plan.

Keep these axes/roles distinct:

```text
Execution ResourceRef
Execution StateVersion
AttemptRef
AttemptEpoch
Attempt observed state
current mutation authority
cancellation generation
resource-local candidate/checkpoint generation
platform job/run identity
```

Agents MUST NOT:

- use platform job/run/native retry identity as Execution or Attempt identity;
- equate a failed Attempt with failed Execution automatically;
- use lease/heartbeat expiry as proof a writer stopped or as a substitute for fencing;
- create a newer Attempt without first ensuring prior side effects are fenceable/reconcilable enough for safe overlap;
- let stale Attempts register candidate/state/checkpoint effects after their epoch is superseded;
- force a database fence check on every Spark row/file when Attempt-isolated immutable namespaces can enforce authority at registration/seal boundaries;
- allow shared mutable targets without a real provider fence/version/CAS guarantee where stale-writer safety is required;
- blindly resubmit after an unknown external launch acknowledgement;
- collapse unknown/indeterminate external state into failure merely to retry;
- treat checkpoint bytes/file existence as a committed resumable checkpoint;
- resume another Execution from a checkpoint while calling it same-Execution recovery;
- use one global idempotency key for every operation;
- allow same idempotency key with materially different request payload to reuse an old effect;
- let a fenced Attempt's late success automatically become authoritative; current authority must explicitly verify/adopt immutable effects;
- double-count repeated Evaluation work units after retry;
- treat provider `SUCCESS`, `CANCELLED`, `KILLED`, or cancel-request acknowledgement as semantic completion/cancellation;
- allow late completion/promotion after cancellation won the control-plane authority race;
- change committed Strategy/source/state/method/network semantics through retry policy;
- equate `completed_operationally` with Learning/Generation/Evaluation semantic completion.

The preferred stale-writer pattern is Attempt-isolated physical work plus `WriterFence` validation at bounded registration/adoption/seal/completion boundaries. A cancellation-generation change revokes old write/promotion authority without pretending the physical process has terminated.

## Evidence, Provenance, history and reproducibility rules

005-H establishes the future Evidence/history plan.

Agents MUST NOT:

- let `EvaluationRuntimeResult`, scheduler success, diagnostics, or a metric row become Evidence directly;
- identify Evidence by metric name, display text, array position, Criterion ID, or runtime result ID instead of stable ResourceRef + Evaluation/finding-slot identity;
- overwrite immutable Evidence finding content because a later Evaluation disagrees or policy changes;
- inflate claim strength beyond method, achieved coverage, uncertainty, assumptions or approximation semantics;
- collapse all findings into one generic `score`/`passed` result;
- copy large diagnostic datasets into bounded Evidence/control rows instead of exact distributed references;
- let Evidence from a later Evaluation enter an already-established Generation completion basis retroactively;
- make a graph/search/lineage store the canonical owner of Provenance or canonical resource payloads;
- use mutable aliases/latest resolution inside exact historical Provenance assertions;
- destructively rewrite incorrect Provenance assertions instead of append/supersede correction;
- record one canonical Provenance edge per Spark task/row/heartbeat/log event by default;
- treat a projection/index miss as proof that a historical relationship was absent;
- let derived adjacency/search/materialized projections overwrite canonical Provenance;
- infer causality, quality, or superiority merely from structural history differences;
- reduce reproducibility to `true/false` or treat presence of a seed as exact determinism;
- conflate historical reproducibility support with whether reproduction is currently feasible;
- let a cached reproducibility assessment become canonical history or semantic promotion authority;
- hide withheld/redacted history as ordinary absence when security policy applies.

The first built-in Provenance plan is indexed relational canonical assertions in the bounded SQL control-store family. Graph/search/lineage systems remain derived/integration surfaces. Evidence establishment and required same-store Provenance may share one control transaction without collapsing their concept ownership.

## Dependencies and optional integrations

The base/core distribution remains model/platform neutral.

Do not add PySpark, PyTorch, Databricks/cloud SDKs, MLflow, OpenLineage clients, graph databases, remote-model/service clients, CUDA/GPU runtimes, SQLAlchemy/Psycopg, scheduler SDKs or similar adapter dependencies to base runtime dependencies merely for one implementation slice.

Any new direct dependency requires explicit purpose/classification and compatibility/offline/network/security review. Committed runtime execution must never install missing packages or download missing models/artifacts as an undocumented fallback.

## Scope and change discipline

Before material work, identify the Phase 005 planning slice or later implementation slice, upstream authority, change classification, affected verification layers/AF fitness IDs and quality gates.

Keep changes bounded to the requested slice. Avoid opportunistic refactors, dependency additions, package moves, terminology changes, or API/schema changes outside scope.

## Non-negotiable architecture guardrails

Do not make runtime/platform/payload objects canonical identity; collapse typed semantic/operational/security/history state; equate checkpoints/candidates/runtime material with semantic results; allow runtime/platform adapters to establish semantic completion; replace Attempt fencing with lease expiry/scheduler retry/last-writer-wins; hide dependency acquisition/remote fallback/telemetry/egress; require full driver collection on enterprise paths; make one runtime/platform universal semantics; let derived indexes/telemetry/security audit/outbox become domain authority; treat handle possession as authorization; or weaken Evidence/Provenance/historical/disclosure contracts for convenience.

## Verification

Once coding is authorized, tests derive their oracle from accepted authority and must not mock away the distributed, concurrency, security, persistence, runtime, recovery, Evidence or history property under test.

Portable/core tests use default network denial where applicable. Never retry stochastic tests until green or weaken required fitness checks without 005-B governance.

005-H future work directly contributes to V8 and AF-08/09/10/11/16/17/18/19. Critical evidence includes idempotent/conflicting Evidence replay, atomic multi-finding establishment, claim-strength rejection, Evidence correction/applicability separation, exact diagnostic support, Provenance retry/correction, canonical-vs-projection disagreement, bounded traversal, non-causal comparison, distinct gap states and reproducibility feasibility degradation without historical rewrite.

## Package/import behavior

The root `syngan` import remains side-effect free and must not automatically import optional platform/runtime/persistence/scheduler/lineage/graph SDKs, scan plugins, open network connections, create sessions, inspect credentials, initialize telemetry, or create a global mutable Session/Context.

## Secrets and sensitive data

Never commit real credentials, tokens, passwords, private keys, bearer secrets, sensitive source rows, protected Learned-State payloads or protected diagnostics in ordinary fixtures/logs/examples.

Evidence, Provenance and historical-query results may themselves be sensitive; 005-I owns the future authorization/redaction rules and derived-index side-channel protections.

## Documentation synchronization

When a durable implementation decision changes, update canonical `docs/implementation/` authority. If architecture itself changes, update `docs/architecture/` and ADR rationale explicitly rather than leaving the new rule only in code or phase notes.

## Completion

Do not claim an implementation-planning slice complete unless its authority mapping, future source-boundary compliance, verification/fitness obligations, dependency/migration/security/network implications, and acceptance-evidence requirements are accounted for.

Do not claim production implementation exists merely because a Phase 005 plan is complete. Do not assume Phase 005-K must authorize coding; it may require further Jackson/design refinement.
