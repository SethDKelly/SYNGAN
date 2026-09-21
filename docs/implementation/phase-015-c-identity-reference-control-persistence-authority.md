
---
type: Implementation Authority
title: 015-C — Identity, References, Representation, Durable Owner-State & Control Persistence
status: complete-current
---

# 015-C — Identity, References, Representation, Durable Owner-State & Control Persistence

## Purpose

Implement the minimum durable control substrate required by later Phase 015 slices while preserving the completed Phase 013 identity/persistence architecture.

015-C owns implementation of:

- stable logical identity and authority scope;
- exact typed references;
- distinct semantic-revision, current-state, representation-schema and recovery-frontier axes;
- strict reference representation/serialization;
- immutable revision persistence and exact historical resolution;
- owner-specific current-state persistence with compare-and-set conflict detection;
- append-preserving material transition history;
- bounded durable coordination intent;
- schema bootstrap/versioning and migration-neutral persistence seams;
- a portable reference durable adapter and C2 conformance evidence.

015-C does **not** implement concept-specific state machines or decide semantic transition legality.

## Governing architecture

Primary current authority:

- Phase 013-B representation/identity reconciliation;
- Phase 013-C control persistence/history/concurrency/migration/recovery reconciliation;
- Phase 013 Consolidated Architecture Contract;
- Phase 014-F adversarial scenarios, especially S08/S09/S11;
- Phase 015-B verification authority.

Historical Phase 005-D and Phase 007-D/E implementation material is feasibility/rationale evidence only.

## Core ownership rule

> Persistence durably records facts accepted by an owning semantic or operational authority. It does not decide that those facts are semantically valid merely because it can store them.

Therefore the 015-C control store exposes no generic semantic operation such as:

~~~text
set_status(...)
mark_complete(...)
approve(...)
promote(...)
mark_valid(...)
~~~

Later owning slices must validate semantic transitions before requesting durable mutation.

## Representation model

015-C implements these distinct axes:

~~~text
AuthorityScope
ResourceKind
LogicalId
SemanticRevisionId / exact revision binding
StateVersion
RepresentationSchemaVersion
RecoveryFrontier
MigrationRevision
~~~

No generic unqualified `version` field may substitute for them.

### ResourceKey

A stable logical resource key contains:

~~~text
authority scope
resource kind
logical id
~~~

It is independent of provider ID, storage locator, Python object identity or process identity.

### TypedReference

A typed reference contains a ResourceKey and may additionally bind an exact SemanticRevisionId.

A reference with an exact revision is non-reactive. Resolution never substitutes a newer revision.

### Encoding decision

Locally minted opaque logical/revision identifiers use UUID4 strings by default.

This is an implementation default, not a semantic identity rule:

- constructors accept any validated non-empty opaque identifier;
- public semantics do not depend on UUID bit layout;
- later federation/external-reference work may use other authority-qualified identifiers.

## Payload representation

Control-store payloads are canonical JSON objects.

The storage layer treats payload contents as opaque owner data.

Canonical JSON is selected because it is:

- standard-library portable;
- deterministic for equality/idempotency checks;
- representation-oriented rather than semantic;
- compatible with later relational/document encodings.

A canonical JSON payload is not automatically the public Python/wire view.

## Concrete persistence choice

015-C selects the Python standard-library `sqlite3` engine as the **portable reference control-store adapter**.

Rationale:

- real durable transactions;
- uniqueness and referential constraints;
- compare-and-set updates;
- crash rollback semantics;
- persistent file-backed integration tests;
- no new runtime dependency;
- available in the baseline Python runtime;
- sufficient to prove the current control-store contract.

Qualification:

~~~text
SQLite reference adapter           IMPLEMENTED / CONFORMANCE TARGET
enterprise production persistence  NOT YET CLAIMED
PostgreSQL / SQLAlchemy / Alembic  NOT SELECTED
provider support                   NOT IMPLIED
scale qualification                NOT IMPLIED
~~~

015-I later owns support/provider qualification. A later storage adapter may replace or supplement SQLite without changing the port if it preserves the same contracts.

## Durable records

### Immutable revision record

Stores:

- exact TypedReference with required revision;
- representation schema version;
- canonical JSON payload;
- availability state.

Insertion is idempotent only when the same exact identity carries the same representation.

A conflicting payload under the same exact revision is rejected.

### Current owner-state record

Stores:

- ResourceKey;
- StateVersion;
- representation schema version;
- last-mutation RecoveryFrontier;
- canonical JSON payload.

The store does not interpret payload lifecycle values.

### Material transition history

A successful current-state CAS records append-preserving technical history containing:

- stable transition ID;
- resource key;
- from/to state version;
- transition kind;
- recovery frontier used;
- bounded canonical JSON transition detail.

The transition kind describes the owner-approved transition; it does not make persistence the owner.

### Durable coordination intent

A bounded coordination-intent record may retain a required technical follow-up across a transaction boundary.

Its state describes technical delivery/reconciliation only.

It never establishes target semantic success or synchronization-owned canonical state.

## Concurrency contract

Current-state mutation requires:

~~~text
exact ResourceKey
expected StateVersion
current RecoveryFrontier token
new representation schema version
new opaque owner payload
material transition record
~~~

The SQLite adapter executes current-state update plus transition-history append atomically.

Stale StateVersion causes a conflict.

A stale RecoveryFrontier causes a conflict.

No silent last-writer-wins behavior is allowed.

## Recovery-frontier boundary

015-C represents and checks a RecoveryFrontier, but it does **not** claim RR-03 closure.

The SQLite database can durably remember its observed frontier, but a database restored to an older snapshot can restore that value too.

Therefore:

~~~text
015-C
  implements frontier representation and mutation-time qualification

015-F
  must establish/prove a genuinely non-regressing authority source or equivalent
  stale-writer exclusion across potentially regressive restore
~~~

This prevents the foundational adapter from overstating its recovery guarantee.

## Exact historical resolution

The store resolves only the exact requested revision.

Store-level outcomes are:

~~~text
RESOLVED
UNAVAILABLE
ABSENT
~~~

The wider architecture also reserves withheld/redacted, unknown/indeterminate, invalid and unsupported outcomes. Those are layered by later authorization/disclosure/representation responsibilities where applicable.

Marking an immutable revision unavailable preserves its identity/tombstone and removes the retained payload; it does not retarget the reference.

## Migration contract

The reference adapter maintains a technical MigrationRevision separately from all semantic/version axes.

015-C implements:

- schema bootstrap;
- persisted migration revision;
- rejection of unsupported future schema revisions;
- restart-safe open/bootstrap behavior for the initial schema.

No semantic migration is performed.

A future representation migration must preserve identity/history and may not manufacture semantic transitions.

## Authority scope / clone boundary

Every store is bound to one AuthorityScope.

Opening a store with a different expected scope fails rather than silently treating copied bytes as the caller's authority.

This provides the representation needed to distinguish continuation from clone/fork behavior without claiming a full federation model.

## Verification activation

015-C activates C2.

~~~text
C0  ACTIVE
C1  DEFINED
C2  ACTIVE — persistence/concurrency/migration
C3-C9 DEFINED
~~~

A new required `control` verification profile will exercise file-backed SQLite integration behavior in addition to the required `portable` gate.

C2 acceptance scenarios include:

1. identity/version-axis validation;
2. strict reference round-trip;
3. immutable revision idempotency/conflict;
4. exact R1/R2 resolution without latest substitution;
5. tombstone/unavailable distinction;
6. state creation and CAS advancement;
7. stale state-version rejection;
8. recovery-frontier advancement and stale-token rejection;
9. atomic rollback when history append fails;
10. durable reopen;
11. authority-scope mismatch rejection;
12. migration-revision bootstrap/future-version rejection;
13. coordination-intent idempotency/conflict.

## Historical implementation disposition

015-C decisions:

~~~text
UUID4 default identifier minting    RETAIN, qualified as opaque default
JSON control payload encoding       RETAIN as reference representation
SQLite                              RETAIN as portable reference adapter only
PostgreSQL                          DEFER
SQLAlchemy Core                     DEFER
Alembic                             DEFER
Psycopg                             DEFER
generic Repository/UnitOfWork API   REJECT as required architecture
one table per concept               REJECT
universal event sourcing            REJECT
global transaction                  REJECT
~~~

## Completion evidence

~~~text
stable identity / reference primitives       IMPLEMENTED
four version/authority axes                  IMPLEMENTED
exact historical resolution                  IMPLEMENTED
owner-state CAS + transition history         IMPLEMENTED
durable coordination intent                  IMPLEMENTED
SQLite reference adapter                     IMPLEMENTED
C2 control integration profile               PASS
concept-specific state machines              NOT IMPLEMENTED
enterprise persistence support               NOT CLAIMED
RR-03 full non-regressing recovery proof     DEFERRED TO 015-F
ICLASS-3                                     0
ICLASS-4                                     0
upstream reopen                              NONE
~~~

## Current authorization

~~~text
015-A        COMPLETE
015-B        COMPLETE
015-C        COMPLETE
015-D        NEXT ELIGIBLE / NOT AUTHORIZED
015-E..015-J NOT AUTHORIZED
IMPLEMENTATION START  STARTED
~~~


## Current next boundary

**015-D — Distributed Data-State, Structured Topology, Candidate/Seal & Generation Promotion** is next eligible but remains **NOT AUTHORIZED** pending explicit proceed.
