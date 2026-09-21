---
type: Phase Record
title: 005-D — Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan
status: complete
---

# 005-D — Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan

## Objective

Translate the accepted public-resource/control-plane architecture into a dependency-safe concrete implementation plan for Python identity/reference types, public specs/handles/views, owner state, persistence ports, relational persistence, transaction/CAS semantics, historical resolution and migration behavior.

005-D is the first behavioral implementation-planning slice. It defines the shared durable substrate later Spark/runtime/recovery/history/security/platform slices must reuse.

## Entry authority

005-D is downstream of:

- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../../architecture/public-api-resource-handle-workflow-semantic-mapping.md);
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../../architecture/control-plane-identity-revision-state-persistence-historical-reference.md);
- [005-A Implementation Authority](../../implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md);
- [005-B Verification Strategy](../../implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [005-C Source Topology](../../implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md).

## Canonical authority created

005-D establishes:

[Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan](../../implementation/public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md).

## Concrete identity/version decisions

Accepted implementation primitives:

```text
AuthorityId      = opaque UUIDv4 installation/authority namespace identity
ResourceId       = opaque UUIDv4 logical resource identity
ResourceKind     = stable typed infrastructure discriminator
ResourceRef      = AuthorityId + ResourceKind + ResourceId
RevisionNumber   = positive monotonic integer scoped to one semantic family
RevisionRef      = exact family ResourceRef + RevisionNumber
SnapshotId       = opaque UUIDv4 immutable commitment-snapshot identity
StateVersion     = positive monotonic integer scoped to one mutable owner state
SchemaVersion    = explicit representation/envelope version
```

These axes remain independent.

Database-generated keys, paths, Spark/Databricks IDs, timestamps and object identity are not canonical ResourceId.

## Python representation decisions

Foundation/domain/public value contracts use immutable standard-library structures equivalent to:

```python
@dataclass(frozen=True, slots=True)
```

plus owner-specific `StrEnum` values, explicit validation and explicit codecs.

SQLAlchemy ORM/Pydantic models are not accepted as universal domain/public representations.

Python pickle is prohibited for canonical control records and durable public handles.

## Public API decisions

Concrete specification names:

- `LearningSpec`;
- `GenerationSpec`;
- `EvaluationSpec`.

Concrete handle roles:

- `LearningHandle`;
- `GenerationHandle`;
- `EvaluationHandle`;
- `LearnedStateHandle`;
- `GenerationOutputHandle`;
- later `EvidenceHandle` and `ExecutionHandle` from their owning slices.

Current state is returned through owner-specific view objects carrying the durable handle, immutable historical bindings, typed lifecycle state and `StateVersion`.

`SynGANClient` is accepted as the outer process-local composition/use-case facade. It is not canonical state and not a universal mutable Session/Context.

Handles remain serializable identity values and do not embed database sessions, Spark sessions, bearer credentials or mutable object graphs.

## Resolution decisions

Historical/resource lookup preserves typed outcomes equivalent to:

```text
resolved
absent
unavailable
unknown
invalid
withheld (reserved for security composition)
```

`None` is not allowed to erase the difference among known unavailable, unknown, invalid and absent history.

Exact references never silently resolve to latest/current revisions.

## Persistence technology decision

005-D selects:

| Responsibility | Technology |
|---|---|
| built-in relational mapping/transactions | SQLAlchemy Core 2.x |
| schema migration | Alembic 1.x |
| reference production backend | PostgreSQL |
| local/dev/test backend | SQLite |
| PostgreSQL driver family | Psycopg 3.x |

SQLAlchemy uses Core rather than ORM so database session/row lifecycle remains outside domain/public resource semantics.

PostgreSQL is the first production-conformance backend. SQLite is not evidence for enterprise concurrent-writer/failover guarantees.

## Persistence dependency isolation

005-D introduces capability packaging equivalent to:

```text
syngan[sql]
syngan[postgres]
```

plus repository-only migration/persistence-test groups.

Base `syngan` remains importable without SQLAlchemy/Alembic/Psycopg.

Concrete persistence dependencies stay under `syngan.adapters.persistence.sql` and cannot leak inward through 005-C package boundaries.

## Relational ownership model

Accepted persistence pattern includes:

- narrow `authority_instance` record;
- narrow technical `resource_identity` anchor;
- owner-specific immutable revision tables for revisioned semantic authorities;
- separate owner-specific mutable current-state rows with `StateVersion`;
- owner-specific immutable Learning/Generation/Evaluation commitment records and separate current-state records;
- logical Learned State control identity/lifecycle separate from physical state payloads;
- append-preserving technical transition journal;
- explicit tombstone/unavailability records;
- separate derived read/index projections;
- transactional outbox/durable-intent records for required downstream work.

One universal `resources`/`metadata` JSON table is rejected.

## Transaction/CAS decisions

Ordinary material lifecycle mutation uses expected-version compare-and-set:

```text
read at state_version N
validate owner transition
conditional write WHERE state_version = N
increment to N+1
append transition history
commit atomically
```

A zero-row conditional update is a stale-state conflict, not permission to last-write-win.

Revision publication allocates the next revision number under a protected family transaction/lock/CAS.

Learning/Generation/Evaluation commitment atomically establishes resource identity, immutable commitment snapshot, initial owner state, material transition and required durable intents inside the control store.

Global SERIALIZABLE isolation is not required; explicit unique constraints, CAS, bounded row locks, idempotency constraints and outbox/reconciliation are the baseline.

## Cross-boundary consistency decision

A transactional outbox/durable-intent mechanism is accepted as the baseline bridge for work that must follow a control transition but cannot occur inside the same SQL transaction.

The outbox is technical infrastructure only:

```text
outbox != Provenance
outbox != Execution
outbox dispatch success != semantic completion
```

005-G refines Attempt/recovery/fencing; 005-H refines Provenance consistency.

## Migration decisions

Alembic database revision remains distinct from:

```text
SchemaVersion
RevisionNumber
StateVersion
package version
```

Migration policy includes:

- migration scripts packaged with the SQL adapter;
- autogenerate permitted only as draft/diff assistance;
- Q1 schema-drift verification once schema exists;
- offline SQL generation for DBA-controlled environments;
- expand/migrate/contract for rolling-compatible changes where applicable;
- immutable historical payloads preserved or version-converted with explicit equivalence/audit evidence rather than rewritten as current semantics;
- downgrade supported only where safe; otherwise restore/forward-fix is explicitly documented.

## Serialization decisions

Durable resource refs/handles/control envelopes use explicit versioned JSON-compatible codecs with stable schema family identifiers.

Initial conventions:

- lowercase hyphenated UUID strings;
- stable lowercase snake-case enum strings;
- UTC RFC3339/ISO-8601 timestamps;
- explicit unsupported-schema failure;
- no arbitrary class names/callables/pickle payloads.

## Implementation sequence

005-D implementation is planned as:

```text
D1  foundation identity/version/resolution primitives
D2  owner lifecycle/value models
D3  public specs/handles/views/client/codecs
D4  control persistence ports/application services
D5  SQLAlchemy Core + SQLite adapter/conformance
D6  PostgreSQL/Psycopg production-conformance profile
D7  Alembic migration baseline and retained upgrade fixtures
D8  Q0/Q1/Q2 package/CI acceptance integration
```

This sequence prevents later storage/runtime adapters from inventing parallel identity/state conventions.

## Verification mapping

005-D owns substantial V1/V2/V4 verification and specifically maps:

- AF-03 — canonical IDs not raw payload/platform IDs;
- AF-05 — immutable commitments/history;
- AF-06 — stale lifecycle writes rejected;
- AF-16 — typed status/resolution distinctions;
- AF-17 — historical exact refs never substitute latest.

Required scenarios include real PostgreSQL concurrent writers, transaction rollback seams, revision allocation races, exact historical resolution, tombstone versus absent, codec/golden migration compatibility, Alembic upgrade/offline rendering and base-install persistence-dependency isolation.

## Security/scale preservation

The control store must contain bounded control state only.

It does not store source/generated rows, DataFrames, tensors, checkpoints, full diagnostic datasets or Spark event/task logs.

No bearer secrets are accepted in canonical control records.

005-I later adds current authorization/redaction/security-domain concerns without changing ResourceId semantics.

## Rejected alternatives

005-D rejects:

- database-generated integer canonical IDs;
- timestamp/UUID ordering as semantic revision/state ordering;
- SQLAlchemy ORM objects as canonical domain/public resources;
- Pydantic/ORM as one universal representation model;
- one generic metadata/resources JSON table;
- full event sourcing as required baseline;
- last-writer-wins concurrency;
- PostgreSQL types/IDs escaping persistence adapters.

## External implementation-tool validation

Current official documentation was checked during planning:

- SQLAlchemy 2.0 remains a schema-centric Core/transaction toolkit suitable for an adapter boundary;
- Alembic remains the SQLAlchemy migration system with current support for `pyproject.toml`, schema diff/autogeneration and offline SQL script generation;
- Psycopg 3 remains the current PostgreSQL Python adapter generation.

These are implementation tools, not semantic authority.

## No upstream revision required

005-D found no requirement to change the eleven accepted concepts, fifteen synchronizations, Phase 003 experience contract, Phase 004 architecture, ADR-0001 through ADR-0008, or 005-C package dependency direction.

No new architecture ADR was needed.

## Exit criteria

- [x] identity/reference/version encodings selected;
- [x] public specs/handles/views/facade named;
- [x] owner lifecycle and persistence responsibilities separated;
- [x] durable serialization policy selected;
- [x] persistence ports/pattern selected;
- [x] SQLAlchemy Core/Alembic/PostgreSQL/SQLite/Psycopg baseline selected;
- [x] optional persistence dependency isolation defined;
- [x] relational ownership/tombstone/index pattern defined;
- [x] CAS/transaction/outbox/idempotency strategy defined;
- [x] historical resolution semantics defined;
- [x] migration/rollback/offline-SQL policy defined;
- [x] V1/V2/V4 and AF-03/05/06/16/17 obligations mapped;
- [x] D1-D8 implementation order defined;
- [x] later slices have one shared durable substrate.

## Exit decision

**005-D — implementation plan complete.**

Next:

**005-E — Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan**.
