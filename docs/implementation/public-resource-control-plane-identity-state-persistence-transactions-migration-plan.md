---
type: Implementation Authority
title: Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan
status: active
---

# Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan

## Purpose

Define the concrete implementation plan for SYNGAN's public resource/reference surface and durable control-plane substrate before Spark/data, runtime, recovery, Evidence/history, security, and platform adapters are implemented.

This document is the canonical Phase 005-D implementation authority. It translates the accepted public-resource and control-plane architecture into concrete Python representations, persistence ports, a baseline SQL adapter, transaction/CAS rules, schema/serialization versioning, historical resolution, and migration verification.

It does **not** implement Spark materialization/manifests, Strategy runtime adapters, Attempt fencing/checkpoint recovery, Evidence/Provenance stores, authorization/security adapters, or Databricks/platform integration. Those remain owned by 005-E through 005-J.

## Governing authority

005-D is downstream of:

- [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md);
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../architecture/public-api-resource-handle-workflow-semantic-mapping.md);
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../architecture/control-plane-identity-revision-state-persistence-historical-reference.md);
- [005-A Implementation Authority](implementation-authority-delivery-governance-toolchain-repository-enforcement.md);
- [005-B Verification Strategy](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [005-C Source Topology](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md).

The governing implementation rule is:

> **One durable identity/version/persistence model SHALL serve every later implementation slice. Public ergonomics, SQL convenience, and platform-native identifiers MUST remain projections/adapters over that model rather than competing authority.**

## Accepted implementation choices

005-D accepts the following concrete baseline:

- immutable/frozen standard-library Python value objects for foundation/domain/public reference contracts;
- UUIDv4-based opaque logical identifiers generated independently of database/platform identity;
- an explicit authority/installation identifier in serialized durable references;
- monotonic integer revision numbers scoped to one revisioned semantic family;
- monotonic integer state versions scoped to one mutable canonical state boundary;
- explicit per-record/per-envelope schema versions independent of semantic revision/state version;
- owner-specific lifecycle enums and transition validators rather than a universal status state machine;
- value-only durable handles/references plus an ephemeral `SynGANClient` facade for resolution/actions;
- explicit JSON codecs for canonical control-plane/wire payloads; Python pickle is prohibited for canonical control records and durable public handles;
- SQLAlchemy **Core** 2.x as the built-in relational control-store adapter implementation technology;
- Alembic 1.x as the schema-migration mechanism for the built-in SQL adapter;
- PostgreSQL as the reference production SQL backend;
- SQLite as a local/developer/test backend only unless a later support profile proves stronger guarantees;
- Psycopg 3.x as the PostgreSQL driver family;
- compare-and-set/conditional update for ordinary lifecycle concurrency;
- relational transactions for coupled control-store mutations;
- a transactional outbox/durable-intent mechanism for required cross-boundary work that cannot complete in one database transaction;
- append-preserving material transition history plus mutable current-state projections; full event sourcing is not required.

These choices implement the Phase 004 contract without changing concept ownership.

## Dependency/package consequences

005-D introduces persistence capability packaging equivalent to:

```text
published optional extra: sql
published optional extra: postgres
repository group: persistence-test
repository group: migration
```

The intended responsibility is:

```text
syngan base
  foundation/domain/ports/application/api
  no SQLAlchemy import required

syngan[sql]
  built-in SQLAlchemy Core persistence adapter
  SQLite support via Python's sqlite driver

syngan[postgres]
  SQL adapter + Psycopg 3 PostgreSQL driver
```

Exact version constraints are recorded in `pyproject.toml` when the scaffold is implemented and locked through `uv.lock`.

SQLAlchemy, Alembic, and Psycopg MUST NOT be imported by `syngan.foundation`, `syngan.domain`, `syngan.ports`, `syngan.application`, `syngan.api`, or root `syngan.__init__` merely because the project ships a built-in SQL adapter.

Alembic is migration/deployment tooling and does not become a runtime semantic dependency.

## Concrete package ownership

005-D refines the 005-C topology with responsibilities equivalent to:

```text
src/syngan/
├── foundation/
│   ├── identity.py
│   ├── versioning.py
│   ├── resolution.py
│   └── issues.py
├── domain/
│   ├── data_meaning/
│   ├── constraint/
│   ├── strategy/
│   ├── criterion/
│   ├── learning/
│   ├── learned_state/
│   ├── generation/
│   └── evaluation/
├── ports/
│   └── control/
├── application/
│   └── control/
├── api/
│   ├── references.py
│   ├── specs.py
│   ├── handles.py
│   ├── views.py
│   ├── client.py
│   └── serialization.py
└── adapters/
    └── persistence/
        └── sql/
            ├── schema/
            ├── repositories/
            ├── codecs/
            └── migrations/
```

Exact leaf-file spelling MAY change during implementation when a smaller/cohesive structure is demonstrated, but ownership and import direction MUST remain equivalent.

005-D does not create empty subpackages for later Execution/Evidence/Provenance/security/runtime work merely for symmetry. Those are introduced by their owning slices.

## Foundation identity model

### `AuthorityId`

Every independently resolvable SYNGAN control-plane authority/deployment receives a stable opaque `AuthorityId`.

Initial encoding:

```text
UUID version 4
```

It identifies the authority namespace from which a durable resource reference is expected to resolve. It is not a tenant authorization token or deployment hostname.

A single deployment normally persists one authority identifier during bootstrap. Cloning/restoring a deployment must deliberately decide whether it is restoring the same logical authority or creating a distinct authority; it must not accidentally generate a new authority ID while claiming old serialized references remain local.

### `ResourceId`

Every durable logical resource receives an opaque UUIDv4 `ResourceId` generated before or independently of concrete database insertion.

Rules:

- never derive canonical resource identity from auto-increment primary key, table row address, path, Spark/Databricks job ID, model ID, or object memory address;
- never reuse a ResourceId for materially different authority;
- database-local surrogate keys MAY exist for performance but remain internal implementation details;
- tests should normally construct explicit stable IDs rather than depend on generated values.

UUIDv4 is selected because Python 3.11 provides it without another core dependency and because ordering is not semantic identity. Database locality/performance MUST use separate indexing/surrogate mechanisms rather than turning timestamp-ordering behavior into identity semantics.

### `ResourceKind`

`ResourceKind` is a stable string-valued infrastructure discriminator used by references, persistence, and resolution.

Initial values include semantic resources that already require durable identity, for example:

```text
data_meaning
constraint
synthesis_strategy
evaluation_criterion
learning
learned_state
generation
generation_output
evaluation
```

Later slices add `evidence`, `execution`, material subordinate operational/resource kinds, and `provenance_assertion` when their implementation contracts are introduced.

`ResourceKind` is not a concept catalog and does not grant semantic ownership to the reference layer.

### `ResourceRef`

The durable reference shape is equivalent to:

```text
ResourceRef
  authority_id: AuthorityId
  kind: ResourceKind
  resource_id: ResourceId
```

The kind and authority are part of resolution safety. A bare UUID is not the durable cross-boundary reference contract.

### Revisioned semantic references

Revisioned authorities use:

```text
RevisionRef
  family: ResourceRef
  revision: RevisionNumber
```

`RevisionNumber` is a positive monotonic integer scoped to one family identity.

For example:

```text
Data Meaning family DM7 / revision 3
```

is represented by the exact family ResourceRef plus revision number 3. Revision number is not globally meaningful.

Revision ordering is semantic-family history, not wall-clock ordering.

### Commitment snapshot identity

Committed Learning/Generation/Evaluation occurrences use a distinct opaque `SnapshotId` (UUIDv4) for the immutable commitment payload bound to the activity.

The activity `ResourceId` and `SnapshotId` remain different axes even when there is exactly one commitment snapshot per committed activity.

A commitment snapshot does not require an independent public handle; it must be stably addressable and preserved historically.

### `StateVersion`

Mutable canonical lifecycle/applicability state uses a positive monotonically increasing 64-bit integer `StateVersion` scoped to that owner/resource state boundary.

Initial state is version `1`. Every material successful canonical mutation produces a strictly newer version.

StateVersion is the ordinary compare-and-set token. Timestamps do not substitute for it.

### `SchemaVersion`

Persisted/wire representation families use explicit positive integer `SchemaVersion` values.

`SchemaVersion` MUST NOT be reused to mean semantic revision, commitment revision, state version, Attempt epoch, migration revision, or package version.

## Python value-object rules

Foundation/domain/public immutable value contracts SHALL prefer:

```python
@dataclass(frozen=True, slots=True)
```

plus `StrEnum`, explicit validation constructors/factories, and typed collections where appropriate.

They MUST NOT depend on ORM models, SQLAlchemy instrumentation, Spark/PyTorch/platform classes, or implicit mutable global state.

The domain object model is not an ORM object model.

A SQL row mapper reconstructs domain/value objects; SQLAlchemy rows are never exposed as public canonical resources.

## Public specification model

005-D accepts concrete public specification role names:

- `LearningSpec`;
- `GenerationSpec`;
- `EvaluationSpec`.

The specs are frozen/replacement-oriented values rather than mutable canonical records.

A convenience builder MAY later exist, but committing a spec always materializes a distinct immutable commitment snapshot. Mutating a Python builder cannot mutate an already committed activity.

Specs contain typed references/values and SHOULD avoid broad untyped `dict[str, Any]` configuration surfaces for authority-bearing fields.

Strategy/method-specific extension configuration may use explicitly namespaced/versioned payloads under the 005-F SPI contract rather than leaking arbitrary dictionaries across all specs.

## Public readiness representation

The derived pre-commit result uses an explicit representation equivalent to:

```text
ReadinessReport
  posture
  issues
  assessed_spec_fingerprint_or_identity
  limitations
  completion obligations
  dependency/network/egress summary
  assessed_at
```

Accepted posture values remain owner/context neutral only at the readiness level:

```text
ready
ready_with_limitations
blocked
indeterminate
```

`ReadinessReport` is derived and refreshable. It is not persisted as the lifecycle state of Strategy, Data Meaning, Constraint, or another authority merely because it can be serialized.

## Public handle and view model

### Concrete handle roles

005-D accepts these public handle names for current/later resources:

- `LearningHandle`;
- `GenerationHandle`;
- `EvaluationHandle`;
- `LearnedStateHandle`;
- `GenerationOutputHandle`;
- later `EvidenceHandle` and `ExecutionHandle` under their owning slices.

A public handle is a small immutable value containing its typed `ResourceRef` plus only non-authoritative convenience metadata that is explicitly marked as cached/freshness-qualified when present.

A handle is **not** a mutable copy of the resource.

### Handles do not carry a database/session/client

The durable handle object SHALL remain serializable without embedding:

- database connection/session;
- SparkSession;
- HTTP client;
- service locator;
- authorization bearer token;
- mutable cached domain object graph.

Actions are performed through the public client/facade using a handle/ref as input.

This avoids making handle serialization process-bound while still preserving ergonomic resource navigation.

### `SynGANClient`

005-D accepts `SynGANClient` as the outer programmatic facade name.

`SynGANClient` is a composition/use-case facade, not canonical state and not a universal mutable Session/Context.

Conceptually it exposes owner-specific surfaces equivalent to:

```text
client.learning
client.generation
client.evaluation
client.resources
```

These surfaces coordinate application services and ports. They MAY create/validate/commit specs, resolve/refresh handles/views, and later start operational realization, but the client itself is replaceable and process-local.

### Views separate current state from identity

Current resource inspection returns typed owner-specific view objects equivalent to:

```text
GenerationView
  handle
  immutable commitment reference/summary
  semantic_state
  state_version
  result association if established
  execution association if established
  fetched_at/freshness metadata
```

Equivalent owner-specific views exist for Learning, Evaluation, Learned State, revisioned authorities, and later Evidence/Execution.

A refreshed view can change state_version/current lifecycle while retaining the same handle/resource identity and immutable historical bindings.

## Owner-specific lifecycle model

Lifecycle enums remain under the owning `domain` package.

005-D SHALL implement distinct transition validators for at least:

- revisioned authority lifecycle (effective/superseded/retired/invalidated as defined by each owner);
- Learning semantic lifecycle;
- Generation semantic lifecycle;
- Evaluation semantic lifecycle;
- Learned State future-use lifecycle.

No single `Status` enum is accepted.

Transition validation occurs before persistence mutation and returns a typed transition decision/error. Persistence only enforces the resulting conditional write; it does not invent semantic transition legality.

Later 005-G/005-H add Execution/Evidence-specific lifecycle/application states without modifying the universal store contract.

## Resolution result model

Read/reference resolution uses a typed result rather than flattening all failure states into `None` or one exception.

The foundation role is equivalent to:

```text
Resolution[T]
  status:
    resolved
    absent
    unavailable
    unknown
    invalid
    withheld      # reserved for 005-I disclosure integration
  value: T | None
  issue/reason
```

Rules:

- `absent` means no referenced relationship/resource was established;
- `unavailable` means identity/history is known but retained payload is unavailable;
- `unknown` means resolution cannot currently establish the state;
- `invalid` indicates malformed/integrity-defective reference;
- `withheld` preserves a later authorization-aware result without forcing security logic into foundation.

Mutation conflicts use typed exceptions/results such as `StaleStateError`, `IntegrityConflict`, `InvalidTransition`, and `UnsupportedSchemaVersion` rather than converting them into `not found`.

## Public/wire serialization

### Explicit versioned codecs

Canonical serialized references/handles/spec snapshots use explicit codecs, not generic object pickling.

Each durable envelope contains a stable schema family identifier plus integer schema version, for example:

```json
{
  "schema": "syngan.resource-ref",
  "schema_version": 1,
  "authority_id": "...",
  "kind": "generation",
  "resource_id": "..."
}
```

A revision reference adds exact revision information; handle serialization wraps or directly uses the resource reference without embedding cached mutable state as authority.

### Encoding rules

Initial canonical wire conventions:

- UUID values serialize as canonical lowercase hyphenated strings;
- enum values serialize as stable lowercase snake-case strings;
- timestamps serialize as UTC RFC 3339/ISO-8601 values with explicit timezone/`Z` semantics;
- maps used in authority-bearing codecs have documented key semantics;
- no arbitrary Python object graph, callable, class name, or pickle payload appears in canonical control records;
- unsupported schema versions fail explicitly rather than being silently interpreted as current.

Python pickle MAY be used by a Strategy-specific ephemeral/runtime mechanism only if later explicitly allowed; it is prohibited for canonical resource references, commitment history, current-state records, migration metadata, and public durable handles.

## Persistence port model

### No universal semantic `MetadataStore`

005-D defines small technical persistence ports while retaining owner-specific repositories/application services.

The port family is equivalent to:

- `IdentityRepository` — establish/resolve technical identity anchors and tombstones;
- revisioned-authority repositories for exact immutable revisions/current future-use state;
- committed-activity repositories for Learning/Generation/Evaluation commitments and current semantic state;
- `LearnedStateRepository` for logical learned-result identity/current lifecycle;
- `TransitionJournal` for append-preserving material lifecycle history;
- `HistoricalResolver` for exact typed historical resolution;
- `ControlTransaction`/unit-of-work boundary for one atomic control-store operation;
- `ControlOutbox` for durable cross-boundary intent.

Generic repository helpers MAY reduce SQL duplication, but public/application code should depend on owner-meaningful ports rather than one generic CRUD interface accepting arbitrary resource kinds/payloads.

Persistence ports MUST NOT accept `set_status(kind, id, value)` or arbitrary dictionary mutations that bypass owner validators.

## Built-in SQL persistence adapter

### Technology

The built-in SQL control-store adapter uses SQLAlchemy Core rather than the ORM.

Rationale:

- keeps domain/value objects independent of ORM lifecycle/session semantics;
- keeps table/schema mapping explicit;
- supports PostgreSQL and SQLite through one SQL expression/transaction layer;
- makes compare-and-set updates and transactional boundaries explicit;
- avoids exposing ORM identity maps as canonical resource identity.

### Reference production backend — PostgreSQL

PostgreSQL is the reference production relational backend for the first implementation program.

The production conformance profile must exercise:

- real transactions;
- row-level conditional updates/CAS;
- uniqueness and referential constraints;
- concurrent writers;
- failure/rollback behavior;
- migration upgrade behavior;
- JSON/document columns used for immutable payloads where applicable.

005-J later defines the supported PostgreSQL version matrix.

### SQLite role

SQLite is supported for:

- fast local development;
- deterministic unit/component persistence tests;
- migration smoke testing;
- simple single-process examples.

SQLite success MUST NOT be used as evidence for enterprise concurrent-writer, multi-process, production failover, or PostgreSQL-specific behavior.

A deployment requiring those guarantees must pass the PostgreSQL persistence conformance profile or another later-approved production adapter profile.

### PostgreSQL driver

Psycopg 3 is the accepted PostgreSQL driver family. Driver packaging mode (`binary`, `c`, or system/libpq-backed installation) is a deployment/package concern that 005-J may profile; canonical persistence behavior cannot depend on one binary-wheel packaging mode.

## Relational schema pattern

005-D accepts a relational pattern, not one monolithic resource table.

### `authority_instance`

Persists the control-plane `AuthorityId` and installation-level persistence schema facts required to resolve local durable references.

It does not store tenant permissions or secrets.

### `resource_identity`

A narrow technical identity anchor contains facts equivalent to:

```text
authority_id
resource_id
resource_kind
created_at
```

This table exists for stable reference integrity and cross-owner foreign-key support. It is **not** a semantic registry and contains no universal status/config/metadata payload.

### Revisioned authority pattern

Data Meaning, Constraint, Synthesis Strategy, and Evaluation Criterion each retain owner-specific immutable revision payload tables plus owner-specific current/future-use lifecycle state.

A revision row includes facts equivalent to:

```text
family_resource_id
revision_number
payload_schema_version
immutable_payload
created_at
supersedes_revision_number? / correction relationship where owner permits
```

The current/future-use state row is separate and has its own `state_version`.

Implementation MAY share table-building/mapping helpers but MUST NOT replace owner-specific payload/lifecycle ownership with one arbitrary `metadata_json` table.

### Committed activity pattern

Learning, Generation, and Evaluation each use owner-specific immutable commitment and mutable current-state structures equivalent to:

```text
<activity>_commitment
  activity_resource_id
  snapshot_id
  snapshot_schema_version
  immutable_snapshot_payload
  committed_at

<activity>_current_state
  activity_resource_id
  owner_state
  state_version
  current result/execution association fields where owner permits
  updated_at
```

Commitment rows are insert-only under ordinary application behavior.

### Learned State pattern

The logical Learned State control record contains stable result identity/establishment facts separate from its mutable future-use lifecycle state and separate from large physical components introduced by 005-F.

### Transition journal

A shared **technical** transition journal may store append-preserving material state transitions across resource kinds, with fields equivalent to:

```text
transition_id
resource_ref
transition_kind
prior_state
new_state
resulting_state_version
operation/correlation id
reason code / bounded details
recorded_at
```

The journal records owner-approved transitions; it never validates or defines them.

### Tombstone/unavailability record

Deliberate retention/payload expiration uses explicit tombstone/unavailability data rather than deleting the identity row and letting missing joins look like `absent`.

A tombstone preserves only the minimal historical facts permitted by retention/security policy, such as resource identity/kind, unavailable-since time, reason class, and representation family/version where useful.

005-I later applies authorization/redaction to these facts.

### Derived indexes

Search/list/query projections live in separate tables/views/materializations with source identity/state-version freshness markers.

Canonical mutation services MUST NOT write semantic truth *through* a derived projection.

## JSON/document payload policy

Immutable commitment/revision bodies may use SQL JSON/document columns for bounded structured payloads where a fully normalized table would create brittle schema coupling without query value.

Rules:

- identity, revision numbers, state versions, owner lifecycle, major relationships, idempotency/correlation keys, and fields required for integrity/concurrency remain first-class columns/relations rather than being hidden entirely in JSON;
- the JSON document has its own payload schema version;
- owner codecs validate the payload at persistence boundaries;
- PostgreSQL MAY use JSONB while SQLite uses its compatible JSON/text representation through the SQL adapter;
- arbitrary plugin blobs and large data-plane payloads do not enter the control database merely because JSON/BLOB columns exist.

This is bounded control state, not a generic metadata bucket.

## Transaction and concurrency model

### Ordinary lifecycle mutation — CAS

Owner application service flow:

```text
1. resolve canonical state at version N
2. validate owner transition against immutable/history/current facts
3. begin control transaction
4. conditional UPDATE ... WHERE resource_id = ? AND state_version = N
5. require exactly one row updated
6. append transition journal fact in same transaction
7. add required intra-store coupled records/outbox intents
8. commit
```

If step 5 updates zero rows, the operation fails with `StaleStateError`/conflict and does not silently retry with new state unless the owning use case explicitly re-resolves and revalidates.

### Revision publication

Creating a bindable semantic revision occurs transactionally with family/current-pointer state under an expected family state version or row lock so concurrent publishers cannot both claim the same revision number/current transition.

Revision numbers are allocated under the family transaction, not by reading `MAX(revision)+1` without protection.

### Commitment transaction

Committing Learning/Generation/Evaluation atomically establishes within the control store:

- activity `resource_identity`;
- immutable commitment row and SnapshotId;
- initial owner current-state row/version;
- originating-draft link when one exists and is retained;
- material transition/history fact;
- required outbox/durable-intent records for downstream work where applicable.

Failure commits none of these canonical facts.

### Result establishment within the control database

When the logical result/control record and owning activity state live in the same SQL store, the implementation SHOULD establish them in one transaction where that satisfies the architecture.

Examples later include Learning completion plus Learned State control identity and Generation completion plus completed-output control identity after 005-E's candidate/promotion preconditions are satisfied.

Data-plane bytes/files/tables are not pulled into that SQL transaction.

### Isolation posture

The reference PostgreSQL adapter does not require global SERIALIZABLE isolation for every operation.

Use ordinary transactions plus:

- unique constraints;
- explicit expected state-version CAS;
- row locks for bounded multi-row invariants/revision allocation when required;
- operation-specific idempotency constraints;
- durable outbox/reconciliation when crossing store boundaries.

A later optimization may use stronger isolation for a bounded operation but cannot remove the explicit semantic conflict model.

## Transactional outbox / durable intent

005-D establishes a bounded technical outbox/durable-intent table as the baseline cross-boundary consistency mechanism.

It carries facts equivalent to:

```text
outbox_id
originating operation / resource reference
intent kind
idempotency/correlation key
payload schema version
bounded payload
created_at
current dispatch/reconciliation state
```

The outbox is written in the same relational transaction as the canonical transition that requires downstream realization.

Important boundaries:

- an outbox record is not Provenance;
- an outbox record is not Execution/Attempt identity;
- dispatch success is not semantic completion;
- 005-G refines attempt/retry/fencing and dispatch reconciliation;
- 005-H refines Provenance-coupled transition recording;
- 005-I applies authorization/sensitive payload constraints.

## Operation-scoped idempotency support

005-D provides an infrastructure pattern for operation receipts/idempotency reservations without defining one global Execution key.

The key namespace includes at least:

```text
operation type/scope
semantic target/resource
caller-provided or derived operation key
```

The store can record the canonical result/reference associated with a completed idempotent operation.

Later slices define exact operation keys for promotion, Evidence establishment, Attempt/checkpoint operations, Provenance assertion recording, and other transitions.

An idempotency match never overrides a stale state/fencing failure when the protected operation also requires current authority.

## Historical resolution

`HistoricalResolver` resolves the exact requested typed reference/revision/snapshot.

It MUST NOT substitute latest/current aliases.

Resolution order is equivalent to:

```text
validate reference envelope/kind/authority
        ↓
resolve exact identity anchor
        ↓
check explicit tombstone/unavailability
        ↓
load exact owner record/revision/snapshot
        ↓
validate representation schema/integrity
        ↓
return typed Resolution
```

The SQL adapter must test cases where:

- revision 1 exists while revision 3 is current;
- a resource identity exists but payload has been intentionally tombstoned;
- a dangling owner row/invalid kind indicates integrity defect;
- another AuthorityId owns the same UUID value;
- a stale cached handle refreshes current state without changing immutable historical refs.

Authorization-dependent withholding is composed by 005-I above/beside this resolver; the persistence layer does not invent authorization policy.

## Migration architecture

### Alembic revision != SYNGAN SchemaVersion

The implementation distinguishes:

```text
Alembic database migration revision
        !=
record/envelope SchemaVersion
        !=
semantic RevisionNumber
        !=
StateVersion
        !=
package version
```

All may coexist.

### Migration location

Built-in SQL migrations live with the SQL persistence adapter and are package-distributed so an installed SYNGAN release can inspect/execute/render the schema migration path it supports.

Migration CLI/tooling MAY wrap Alembic behind stable repository/deployment commands, but Alembic remains an implementation mechanism rather than a public semantic API.

### Autogenerate policy

Alembic autogenerate MAY create a draft migration diff.

Generated migrations MUST be reviewed and edited as necessary for:

- data preservation;
- constraint naming;
- downgrade/forward-repair behavior;
- PostgreSQL/SQLite profile differences;
- immutable-history guarantees;
- rolling-version compatibility;
- explicit data transforms.

A clean autogenerate diff is not evidence that semantic history remains correct.

Q1 SHOULD include Alembic schema-drift/check functionality once the schema exists so metadata changes without a migration are caught.

### Offline SQL generation

The production migration path SHOULD support Alembic offline SQL rendering for environments in which application identities cannot perform DDL directly and migrations require DBA review/execution.

Migration scripts must therefore avoid unnecessary dependence on live application-level Python reads when equivalent SQL/explicit migration logic can be used.

### Expand / migrate / contract

Public/persisted changes that require mixed-version operation SHOULD use an expand/migrate/contract sequence when feasible:

1. **expand** — add backward-compatible schema/read capability;
2. **migrate** — populate/verify new representation while old representation remains intelligible where required;
3. **contract** — remove obsolete representation only after the supported compatibility window permits it.

005-J later defines concrete rolling-upgrade/support windows.

### Immutable historical payload migration

Migration must not treat immutable semantic snapshots/revisions as mutable business documents.

Preferred order:

1. keep the original persisted payload and add/read a newer codec/view when possible;
2. if a physical representation conversion is required, preserve the original or a verifiable versioned replacement plus migration provenance/audit facts sufficient to demonstrate semantic equivalence;
3. never rewrite old commitments to current semantic authority merely to simplify code.

A representation migration changing JSON shape does not create a new Learning/Generation/Evaluation or semantic revision.

### Downgrade policy

Every migration must document downgrade/rollback posture.

A fully automatic Alembic downgrade is required only when it can be performed without destroying data/history required by accepted contracts.

For irreversible migrations, the supported rollback path may instead be restore/forward-fix with explicit operational procedure. An unsafe destructive downgrade must not be implemented merely to make every revision mechanically reversible.

## Persistence schema/security boundaries

005-D does not implement authorization, but the control schema must be compatible with later 005-I requirements.

Therefore:

- no plaintext passwords/API tokens/private keys/bearer secrets in canonical control tables;
- secret references MAY be stored later, not secret values;
- actor/tenant/security-domain identifiers MAY be added by 005-I without changing core resource identity semantics;
- error messages/resolution types reserve withholding/redaction without requiring SQL persistence to decide disclosure;
- SQL query logging in tests/dev must not normalize logging sensitive control payloads.

## Scale/control-plane constraints

Control persistence is bounded by resources/revisions/commitments/material transitions/Attempt summaries/Evidence/Provenance and related control facts, not by source/generated row count.

005-D therefore prohibits:

- storing source/generated rows in control JSON payloads;
- one control row per synthetic/source record;
- embedding model tensors/checkpoints in activity rows;
- storing complete Spark task/event logs in transition tables;
- serializing whole DataFrames into commitment snapshots.

Indexes are designed around bounded resource access patterns such as typed identity, family/revision, current state, creation time, owner association, and idempotency/correlation keys.

Data-plane scaling remains 005-E/005-F.

## Verification plan

005-D owns concrete implementation of substantial parts of V1, V2, V4 and the following architecture-fitness obligations:

### AF-03 — canonical identity is not platform/payload identity

Tests prove:

- ResourceRef rejects/does not use DataFrame/path/platform IDs as ResourceId;
- SQL surrogate keys are not emitted as canonical refs;
- serialized handle round-trip preserves AuthorityId/kind/ResourceId.

### AF-05 — immutable commitments/history

Tests prove:

- commitment/revision repository exposes no ordinary update path for immutable payload;
- SQL constraints/repository APIs prevent in-place rewrite through supported application paths;
- migration fixtures preserve old commitment meaning.

### AF-06 — stale lifecycle writes rejected

Real persistence tests run two observed state versions and prove only the expected-version writer succeeds.

The PostgreSQL profile includes true concurrent transaction cases; SQLite-only success is insufficient production evidence.

### AF-16 — typed status/disclosure contexts

Tests prove owner-specific lifecycle enums remain non-interchangeable and resolution/disclosure states serialize distinctly.

### AF-17 — exact history does not resolve to latest

Fixtures bind work to historical revision R1, advance current family state to R2/R3, and prove exact historical resolution still returns R1.

### Additional required verification

- ResourceId/AuthorityId/RevisionRef/SnapshotId codec round trips;
- invalid kind/authority/schema-version cases;
- commitment transaction rollback at every durable mutation seam;
- family revision allocation under concurrent publishers;
- coupled state+transition-journal atomicity;
- outbox written atomically with originating control transition;
- explicit tombstone versus absent resolution;
- SQLAlchemy adapter reusable repository/conformance tests;
- SQLite local profile plus PostgreSQL production-conformance profile;
- Alembic clean-database upgrade-to-head;
- upgrade from retained historical schema fixtures;
- schema-drift check;
- offline SQL render smoke;
- built wheel contains migrations/codecs needed for supported store operation;
- base `syngan` import remains SQLAlchemy/Psycopg-free when SQL extras are absent.

## Scenario/golden fixtures

005-D introduces small deterministic fixtures for:

- fixed AuthorityId/ResourceIds;
- at least three revisions of one Data Meaning/Constraint/Strategy/Criterion family;
- committed Learning/Generation/Evaluation snapshots at schema v1;
- state-version sequences with one stale writer;
- deliberate unavailable/tombstoned historical resource;
- cross-authority invalid resolution;
- serialized ResourceRef/RevisionRef/handle schema-v1 goldens;
- previous database migration revisions sufficient to exercise forward migration.

Golden updates that change durable wire/persistence representation are Class 2 changes and require compatibility analysis.

## Quality-gate mapping

### Q0

Once implemented:

- identity/version/reference unit tests;
- owner transition unit tests;
- public codec tests;
- AF-03/AF-16 fast checks;
- Import Linter/typing/lint remain required.

### Q1

Adds:

- control repository contract tests;
- SQLite deterministic adapter suite;
- AF-05/AF-06/AF-17;
- migration-to-head and schema-drift checks;
- built-wheel migration/resource-codec smoke;
- no-SQL-extra base import smoke.

A bounded PostgreSQL concurrency check SHOULD become Q1 when repository CI can provide a reliable service container; until then it is a required Q2 integration check and its absence blocks a PostgreSQL production-support claim rather than weakening AF-06.

### Q2+

- real PostgreSQL concurrent writer/revision allocation;
- database disconnect/rollback/failure injection;
- rolling/mixed-version migration scenarios when later support windows are defined;
- backup/restore/upgrade certification under 005-J release profiles.

## Implementation sequence

The coding slice should be delivered in this dependency order:

### D1 — foundation identity/version/resolution primitives

Implement and verify AuthorityId, ResourceId, ResourceKind, ResourceRef, RevisionNumber/RevisionRef, SnapshotId, StateVersion, SchemaVersion, Resolution and bounded issue/error types.

### D2 — owner lifecycle/value models

Implement revisioned-authority/activity/result state values and pure transition validators for the 005-D owners without persistence dependencies.

### D3 — public specs/refs/handles/views/codecs

Implement LearningSpec, GenerationSpec, EvaluationSpec, readiness representation, concrete typed handles/views, SynGANClient facade contracts and schema-v1 durable codecs.

### D4 — control persistence ports/application services

Define owner-meaningful repositories, HistoricalResolver, transaction/outbox boundaries and application commit/transition orchestration.

### D5 — SQLAlchemy Core adapter + SQLite conformance

Implement relational metadata/table mappings, SQL repositories, transactions/CAS, transition journal, tombstones, outbox, and deterministic adapter tests.

### D6 — PostgreSQL adapter profile

Add Psycopg-backed PostgreSQL engine configuration and real concurrency/transaction conformance without letting PostgreSQL-specific identifiers/types escape the adapter.

### D7 — Alembic migration baseline

Create migration environment, initial schema, schema-drift checks, offline SQL render, retained historical migration fixtures and upgrade verification.

### D8 — package/CI acceptance

Integrate Q0/Q1/Q2 profiles, built-package tests, optional dependency isolation, migration packaging, and delivery-evidence capture.

Each step must leave later steps dependent inward, not require placeholder Spark/runtime/security code.

## Deferred to later slices

005-D intentionally does not decide/implement:

- source snapshot/table/file identity and data manifests — 005-E;
- candidate output materialization/sealing and physical promotion — 005-E;
- Strategy/method plugin SPI and runtime state codecs — 005-F;
- Execution/Attempt persistence details beyond resource identity compatibility, fencing/checkpoints/retry/cancellation — 005-G;
- Evidence finding persistence, Provenance assertions and history query projections — 005-H;
- tenant/principal/authorization/redaction/secret-policy implementation — 005-I;
- final PostgreSQL support matrix, deployment topology, backup/restore operations and observability — 005-J.

Later slices may add owner-specific tables/ports beneath this substrate but MUST NOT create parallel ResourceId/StateVersion/schema-migration conventions.

## Rejected implementation alternatives

### Database-generated integers as canonical IDs

Rejected because they bind public/history identity to one store and make cross-authority serialization/restore/federation harder.

### UUID timestamp ordering as semantic history

Rejected. UUID generation/ordering is identity implementation; semantic revision/state ordering is carried explicitly by RevisionNumber/StateVersion.

### SQLAlchemy ORM models as domain/public resources

Rejected because ORM session/identity-map lifecycle would leak persistence concerns inward and invite mutable row objects to masquerade as canonical domain authority.

### Pydantic/ORM model as the universal domain representation

Rejected for the baseline. Standard-library frozen value objects plus explicit codecs keep domain/public contracts independent of serialization/framework magic. A later transport surface may use generated/adapter DTOs without changing canonical domain types.

### One universal `resources` JSON table

Rejected because it would erase owner-specific state/payload constraints and drift toward a semantic MetadataStore/Registry.

### Full event sourcing as the baseline

Rejected by Phase 004. Current projections plus append-preserving material transition history provide the required auditability without making event replay the only source of state.

### Silent last-writer-wins

Rejected. All material mutable state uses explicit expected-version conflict detection.

### PostgreSQL-only types in domain/ports

Rejected. PostgreSQL is a reference adapter/backend, not semantic identity.

## Current-tool validation note

The implementation choice was checked against current official project documentation during 005-D:

- SQLAlchemy 2.0 continues to provide a schema-centric Core API with explicit statements, transactions, schema description, and DBAPI integration suitable for an adapter boundary;
- Alembic remains the SQLAlchemy migration tool and supports `pyproject.toml`, migration autogeneration/diffing, and offline SQL script generation;
- Psycopg 3 remains the current PostgreSQL adapter generation and supports current Python/PostgreSQL versions relevant to the planned Python 3.11 baseline.

These tools implement the accepted contract; their behavior does not become semantic authority.

## No upstream revision required

005-D finds no persistence/API implementation requirement that requires changing the eleven accepted concepts, fifteen synchronizations, Phase 003 experience contract, Phase 004 architecture contract, ADR-0001 through ADR-0008, or 005-C dependency direction.

No new architecture ADR is required because the phase makes downstream implementation selections within the accepted control-plane architecture.

## Exit criteria

005-D is implementation-plan complete when:

- [x] concrete identity/reference/version encodings are selected;
- [x] public spec/handle/view/facade roles are concretely named;
- [x] canonical wire/control serialization policy is selected;
- [x] owner lifecycle versus persistence mutation responsibilities are separated;
- [x] control persistence port families are defined;
- [x] reference SQL adapter technology and production/local backends are selected;
- [x] relational schema ownership/pattern is defined;
- [x] CAS/transaction/outbox/idempotency patterns are defined;
- [x] exact historical resolution/tombstone behavior is defined;
- [x] Alembic migration/versioning/rollback policy is defined;
- [x] optional persistence dependency isolation is defined;
- [x] V1/V2/V4 and AF-03/05/06/16/17 verification obligations are mapped;
- [x] implementation sequence D1-D8 is dependency-safe;
- [x] downstream slices can reuse one identity/state/persistence substrate without inventing parallel conventions.

## Exit decision

**005-D — implementation plan complete.**

Next:

**005-E — Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan**.
