---
type: Architecture Authority
title: Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture
status: active
---

# Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture

## Purpose

Define how SYNGAN represents and persists durable control-plane identity, immutable semantic revisions/commitments, mutable lifecycle state, concurrency, historical references, corrections, and derived indexes beneath the typed public resource/handle model established in 004-B.

This architecture establishes logical persistence and consistency contracts. It does **not** select a database engine, ORM, event store, graph store, identifier encoding, storage vendor, or distributed-data manifest technology.

## Governing authority

This architecture remains downstream of:

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md);
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](public-api-resource-handle-workflow-semantic-mapping.md);
- [Phase 003 Consolidated Experience Contract](../experience/phase-003-consolidated-experience-contract.md);
- [Accepted Concepts](../concepts/index.md);
- [Provenance](../concepts/provenance.md);
- [Reproducibility Contract](../authority/reproducibility-contract.md).

## Primary decision

SYNGAN control-plane persistence SHALL distinguish four independent identity/version axes:

```text
1. RESOURCE IDENTITY
   Which logical authority/activity/result is this?

2. SEMANTIC REVISION / COMMITMENT SNAPSHOT
   Which exact immutable meaning/configuration was bound?

3. CURRENT STATE VERSION
   Which mutable lifecycle view/transition generation is current?

4. REPRESENTATION SCHEMA VERSION
   Which serialization/storage schema interprets these persisted bytes/fields?
```

These axes MUST NOT be collapsed into one generic `version` field.

The control plane SHALL preserve immutable semantic history through stable typed references while allowing owner-specific current lifecycle state to advance through concurrency-controlled transitions.

## Identity model

### Resource identity

Every durable committed activity, promoted result, Execution, material subordinate operational record, revisioned authority family, and durable Evidence/Provenance assertion that requires independent reference SHALL have stable logical identity sufficient for its architectural role.

A resource identity MUST:

- be stable for the lifetime of the represented logical resource;
- never be reused for a materially different resource;
- remain independent of one client process, Python object, SparkSession, file path, table alias, platform run ID, or physical storage location;
- be typed or resolvable with enough kind/context to prevent accidental cross-kind interpretation;
- remain usable as a historical reference after current lifecycle state changes;
- support authorization-aware resolution without changing the underlying identity.

The exact encoding may later be UUID-like, ULID-like, content-derived, database-generated, composite, or another form. 004-C does not choose the encoding.

### Identity scope / namespace

A durable reference MUST be unambiguous within the authority/deployment scope in which it is expected to resolve.

Where identities may cross installations, tenants, external systems, exports, or federated catalogs, the reference architecture MUST have room for an authority/namespace discriminator rather than assuming a local integer or bare name is globally meaningful.

The exact namespace format is deferred.

### Typed reference

A durable typed reference conceptually carries enough information equivalent to:

```text
reference kind / authority kind
logical resource identity
authority or namespace when required
exact revision/snapshot identity when the relationship binds one
optional external-provider identity when the target is externally owned
```

A locator MAY accompany a reference for resolution convenience but is not the semantic identity.

### Identity is not a display name

Human-friendly aliases, names, labels, paths, table names, model aliases, URLs, and platform IDs MAY be indexed/displayed, but MUST NOT be the sole durable identity when their target may change materially.

## Semantic revision architecture

### Revisioned semantic authorities

Authorities whose concepts explicitly support material revisions—such as Data Meaning, Constraint, Synthesis Strategy/configuration, and Evaluation Criterion—require stable logical family identity plus exact immutable semantic revision identity where historical work binds them.

Conceptually:

```text
Data Meaning family DM7
  ├─ revision R1  [historical]
  ├─ revision R2  [supersedes R1]
  └─ revision R3  [current effective]
```

Committed Learning that bound R1 continues to reference R1 even when R3 is current.

### Draft versus immutable semantic revision

Editable draft state MUST NOT masquerade as an immutable bindable semantic revision.

A draft MAY have its own draft/work identity and mutable draft state version for collaboration/persistence. When a revision becomes bindable/effective under the owning concept, its material semantic content MUST become immutable under that semantic revision identity.

A later material correction creates another revision rather than changing the already-bound revision in place.

This rule does not require every draft to be persisted.

### Semantic revision versus lifecycle status

The immutable meaning of a semantic revision is separate from its current future-use lifecycle.

For example, a Data Meaning revision can retain identical historical content while its current status changes from effective to superseded or invalidated.

That lifecycle change increments current state version; it does not create a different historical interpretation pretending to have been bound by past work.

## Commitment snapshot architecture

### Activity identity is occurrence identity

Each committed Learning, Generation, and Evaluation is a distinct durable activity occurrence.

Committed activity identity is not a revisioned mutable document. Material changes after commitment create a new activity occurrence.

Conceptually:

```text
Generation G17
  commitment snapshot CS17   [immutable]
  current semantic state     [mutable/versioned]
  Execution reference        [separate authority]
  completed output reference [only after promotion]
```

### Commitment snapshot

At semantic commitment, the owning activity persists or references an immutable commitment snapshot containing enough exact bound information to reconstruct the material semantic commitment later.

The snapshot SHOULD consist primarily of typed stable references plus activity-owned committed values rather than wholesale copies of other canonical authorities.

For Generation, for example, the immutable commitment may include references/values equivalent to:

- exact Data Meaning revision;
- exact Strategy/configuration revision or snapshot;
- exact Learned State or direct-input/source identity;
- applicable Constraint revisions/handling;
- Conditions, quantity, scope, and tolerances;
- dependency/base-artifact identities;
- network/no-egress posture;
- randomness/reproducibility intent;
- other material committed values.

The exact physical schema is deferred.

### Commitment snapshot identity

A commitment snapshot MUST be stably addressable as part of the historical activity contract, whether implemented as a separate object, immutable embedded state, or another later representation.

The architecture does not require a globally independent user-facing handle for every snapshot. It requires historical distinguishability and stable referenceability.

### Pre-commit drafts do not fabricate committed history

A persisted draft/specification MAY have a draft identity for collaboration or recovery, but it is not a Learning/Generation/Evaluation activity identity merely because it was saved.

Commitment creates the durable committed activity occurrence and binds its immutable snapshot.

An implementation MAY preserve a link from the committed activity to an originating draft for audit/user convenience, but draft identity and activity identity remain different architectural roles.

## Result identity and mutable current state

### Promoted result identity

Learned State, completed Generation output, and Evidence each receive stable result identity only according to their owning semantic establishment/promotion rules.

Result identity MUST remain independent of mutable current lifecycle/applicability state.

Examples:

- a Learned State remains the same historical Learned State as it moves from usable to restricted, retired, or invalidated;
- Evidence remains the same historical finding as its current applicability becomes stale, superseded, inapplicable, or invalidated;
- a completed output retains its producing Generation identity even if physical storage is relocated or later becomes unavailable.

### Current state projection

Durable resources with mutable lifecycle state SHALL expose a current state projection containing the owner's current lifecycle/applicability facts and a state version suitable for concurrency control.

The current projection is not the historical semantic snapshot.

Conceptually:

```text
Resource ID: LS17
Immutable establishment facts: ...
Current state: restricted
State version: 8
```

A current projection MAY be materialized for efficient reads and may be rebuilt/reconciled from retained authoritative transition/history facts where the chosen persistence architecture supports that. Full event sourcing is not required.

## State transition architecture

### Owner-specific state machines

Lifecycle transitions remain owned and validated by their semantic/operational authority.

There is no universal state machine for all SYNGAN resources.

Shared transition infrastructure MAY exist, but a generic persistence layer MUST NOT decide that a Generation transition is valid merely because an enum value can be written.

### State version / concurrency token

Mutable canonical lifecycle state SHALL have a monotonic or otherwise conflict-detectable state version/concurrency token per resource/owned state boundary.

A material mutation SHOULD be applied against the version/state the caller observed or explicitly expects.

Conceptually:

```text
read Generation G17 at state_version = 12
request transition expecting 12

if current is still 12:
    validate transition
    persist transition
    state_version -> 13
else:
    reject/reconcile stale write
```

The exact token may be a counter, ETag, database version, compare-and-set token, transaction version, or another mechanism.

### No last-writer-wins for material authority

Material lifecycle, commitment, promotion, restriction/invalidation, correction, and recovery decisions MUST NOT use silent last-writer-wins semantics when concurrent writes conflict.

A stale or conflicting write must be rejected, retried after refresh, or explicitly reconciled according to the owning contract.

### Time is not concurrency identity

Wall-clock timestamps are useful historical facts but MUST NOT be the sole concurrency/ordering mechanism for material transitions.

Clock skew or equal timestamps cannot be allowed to silently choose semantic authority.

### Transition history

The control plane MUST retain enough material transition history to explain significant lifecycle changes, promotion, restriction/retirement/invalidation, correction, cancellation/reconciliation, and other historically relevant state movement.

This does not require retaining every read, cache refresh, UI interaction, or non-material internal write.

The exact representation may be transition records, audit records, event records, append-preserving rows, or another mechanism.

## Persistence ownership boundaries

### Logical ownership before physical database choice

004-C defines **logical persistence ownership boundaries**, not one database per concept.

Several authority families MAY share the same physical database/schema technology if their ownership and mutation contracts remain explicit.

Conversely, one concept MAY require more than one physical store when control-plane/data-plane/security/scale concerns justify it.

### Required logical ownership partitions

Architecture SHALL preserve distinct mutation authority equivalent to the following boundaries:

1. **Revisioned semantic-authority persistence** — Data Meaning, Constraint, Strategy/configuration, Criterion revisions and current lifecycle.
2. **Committed activity persistence** — Learning, Generation, Evaluation identities, immutable commitment snapshots, semantic lifecycle, owned result associations.
3. **Promoted-result persistence** — Learned State lifecycle/representation references, completed-output logical authority, Evidence finding/applicability state.
4. **Execution persistence** — Execution identity/current operational state and subordinate Attempt history, refined in 004-F.
5. **Provenance relationship persistence** — typed historical relationships/assertions and correction state, refined in 004-G.
6. **Derived indexes/read models** — search/listing/navigation/query acceleration that may combine authority but do not own canonical mutation.

These are responsibility boundaries, not accepted package names or physical database count.

### Mutation through owner contracts

Canonical state MUST be mutated through the owning application/control contract rather than by arbitrary cross-module table updates.

A query/read model MAY join or project several authority families for actor convenience without acquiring write authority over them.

### Shared infrastructure is not shared authority

A common persistence library, transaction engine, relational database, key-value store, or document store MAY support many resource kinds.

That technical sharing MUST NOT create a `MetadataStore` or `Registry` that semantically owns all state simply because it stores rows for several owners.

## Cross-resource consistency

### Required coupled facts must not silently diverge

Some semantic transitions require several durable facts to remain consistent, for example:

- commitment plus its immutable snapshot;
- Learning completion plus Learned State establishment/reference;
- Generation completion plus completed-output association;
- Evaluation completion plus established Evidence;
- material transition plus required Provenance relationship(s).

The architecture MUST provide a consistency strategy such that a crash or retry cannot leave these facts silently contradictory.

### No universal distributed transaction requirement

004-C does not require one global ACID transaction across all stores/adapters.

A later implementation MAY use, depending on boundary and deployment:

- one local atomic transaction;
- compare-and-set plus durable transition intent;
- transactional outbox/inbox style coordination;
- idempotent promotion records;
- durable reconciliation/fencing;
- another mechanism that satisfies the same invariants.

The requirement is **detectable and recoverable consistency**, not a specific transaction technology.

### Transitional/uncertain consistency state is explicit

When a cross-boundary transition cannot yet be known complete because of failure or partial persistence, the control plane MUST retain enough durable state to reconcile rather than optimistically marking the semantic transition successful.

Detailed retry/fencing mechanics are refined in 004-F and 004-G.

## Historical reference resolution

### Exact historical target first

Resolving a historical reference MUST attempt to resolve the exact referenced identity/revision/snapshot.

The resolver MUST NOT silently substitute:

- the current Data Meaning revision;
- the latest Strategy version;
- a newer Learned State;
- the current source alias target;
- a replacement dependency;
- the latest Evidence;

when the historical reference points elsewhere.

### Resolution outcome is typed

Historical resolution MUST distinguish outcomes equivalent to:

- **resolved** — exact referenced state is available and authorized for the actor;
- **withheld/redacted** — target exists but disclosure is restricted;
- **unavailable** — target identity is known but required retained representation can no longer be resolved;
- **unknown/indeterminate** — the system cannot currently establish whether/how the target resolves;
- **invalid reference / integrity defect** — a reference is malformed, contradictory, or fails required integrity checks.

`absent` remains different: it means no such relationship/value was established, not that a known target failed resolution.

Authorization/redaction details are refined in 004-H, but 004-C reserves these distinguishable resolution semantics.

### No null-based history erasure

A historical resolver MUST NOT convert known-withheld or known-unavailable history into ordinary `null` when doing so would falsely imply the relationship never existed.

### Retention and tombstone identity

Retention policy MAY allow some detailed state or data-plane payload to expire.

When a durable retained historical reference still points to an expired resource, the control plane SHOULD preserve enough tombstone/reference metadata to state that the identity existed and is now unavailable rather than reusing the ID or silently retargeting it.

004-C does not define retention periods or deletion policy.

## Provenance correction and canonical correction boundaries

### Provenance assertion identity

A material Provenance assertion that can later be corrected/superseded requires stable distinguishability so correction can identify which assertion is being replaced or invalidated.

004-G will define the detailed relationship/query representation.

### Correction is non-destructive history

Where current reliance changes because a prior assertion or current-use status was wrong, correction should append/supersede/invalidate through an explicit transition or replacement reference rather than silently rewriting audit history.

### Correction does not cross authority boundaries automatically

Correcting a Provenance assertion does not mutate the referenced Learning/Generation/Evidence/etc.

Correcting Data Meaning creates a new semantic revision; it does not mutate historical activity snapshots.

The owning authority must perform any canonical correction permitted by its own rules.

## Representation schema versioning

### Schema version is not semantic revision

Persisted records/serialized handles require a representation schema version when their structural format may evolve.

Migrating:

```text
Generation record schema v1 -> schema v2
```

MUST NOT by itself create a new Generation or change its commitment snapshot.

Likewise, changing a semantic Strategy revision does not imply the storage schema changed.

### Backward/forward compatibility

Later implementation SHALL define supported migration/read compatibility for persisted control-plane schemas and public serialized references/handles.

Migrations MUST preserve:

- stable resource identity;
- immutable semantic revision/snapshot meaning;
- current lifecycle state meaning;
- historical typed references;
- correction/supersession relationships;
- disclosure-state fidelity.

Exact migration tooling is deferred to Phase 005 implementation planning after Phase 004 boundaries are complete.

## Derived indexes and search

Search, listing, dashboards, relationship navigation, and historical summaries MAY use denormalized read models or indexes.

Derived indexes:

- MAY copy selected fields for query performance;
- MUST identify their source resource identities/versions sufficiently for freshness interpretation;
- MUST NOT become the write authority for canonical semantic state;
- SHOULD be rebuildable or repairable from canonical owners plus retained history;
- MAY be eventually consistent where the user-facing contract exposes/accepts that freshness.

A search-index record is not Proof that a semantic transition occurred if canonical owner state says otherwise.

## Read consistency and handle refresh

### Handle snapshots may be stale

A 004-B handle may cache a current view for efficiency.

The view SHOULD expose enough version/freshness information for clients to determine whether a refresh may be required before a mutation or high-consequence decision.

### Historical facts and current facts differ

A refreshed handle may legitimately show:

```text
same resource ID
same immutable commitment/result facts
newer current lifecycle state
higher state version
```

Refreshing MUST NOT substitute a newer semantic revision for an exact historical reference embedded in the resource.

### Read models may lag

Derived read models/indexes MAY lag canonical writes, but material actions MUST validate against canonical owner state or an equivalently authoritative concurrency token before mutation/promotion.

## Identity and persistence examples

### Example 1 — Data Meaning correction

```text
Data Meaning DM7
  Revision R2 (effective, immutable content)

Learning L9 commits -> binds DM7/R2

later:
Data Meaning DM7
  Revision R3 corrects R2
  R2 current status -> superseded

Learning L9 still binds R2
```

R2's content never changes to pretend L9 used R3.

### Example 2 — Generation lifecycle

```text
Generation G17
Commitment snapshot CS17 [immutable]

state_version 1: committed
state_version 2: fulfilling
state_version 3: awaiting required validation
state_version 4: completed

Completed output O17 associated at promotion
```

Changing the Conditions after `CS17` would require a new Generation, not `G17 state_version 5` with different commitment semantics.

### Example 3 — Evidence staleness

```text
Evidence E31
Historical finding [immutable]
Current applicability: applicable  (state v3)

later threat model changes
Current applicability: stale       (state v4)
```

The finding is not rewritten.

### Example 4 — unavailable historical payload

```text
Completed output O17
producing Generation G17
historical identity retained
payload retention expired

resolution:
identity/history -> resolved
payload -> unavailable
```

The system does not silently point O17 at a newer output.

## Enterprise-scale rule

Control-plane persistence must remain bounded by resources, revisions, commitments, material lifecycle transitions, typed references, Evidence summaries, Attempts, and material Provenance relationships.

It MUST NOT scale automatically with:

- source row count;
- generated row count;
- Learned State tensor/parameter count;
- all Spark tasks;
- all log lines;
- every diagnostic row.

Large physical material remains referenced in the data plane or platform-native systems.

## Architecture invariants

1. Resource identity, semantic revision/commitment snapshot, mutable state version, and representation schema version MUST remain distinct.
2. Durable logical IDs MUST NOT be reused for materially different resources.
3. Mutable aliases/locations/platform IDs MUST NOT replace stable historical identity.
4. Bindable semantic revisions and committed activity snapshots MUST be immutable in material meaning.
5. Material changes after activity commitment create a new activity occurrence rather than revising the committed activity in place.
6. Current lifecycle/applicability state MAY evolve independently of immutable semantic/history facts.
7. Material lifecycle writes MUST detect conflicting/stale concurrent mutation; silent last-writer-wins is prohibited.
8. Wall-clock time MUST NOT be the sole ordering/concurrency authority for material transitions.
9. Owner-specific state machines MUST validate transitions; generic persistence infrastructure MUST NOT invent semantic validity.
10. Logical persistence ownership MUST remain explicit even if multiple owners share one physical database technology.
11. Derived indexes/read models MUST NOT become canonical mutation authority.
12. Required coupled transition facts MUST have detectable/recoverable consistency across crashes/retries.
13. Historical references MUST resolve the exact bound target or return an explicit non-resolution/disclosure state; they MUST NOT silently substitute current/latest state.
14. Known withheld/unavailable history MUST NOT be serialized as ordinary absence/null when that would falsify existence.
15. Retained historical identity MUST NOT be reused after payload/detail retention expires.
16. Corrections/supersession MUST preserve auditability and MUST NOT silently mutate other authority owners.
17. Representation-schema migration MUST preserve semantic identity/history and MUST NOT masquerade as semantic revision.
18. Control-plane canonical state MUST remain bounded rather than grow with row/task/log/tensor volume by default.
19. Handle refresh MAY update current lifecycle view but MUST NOT change stable resource identity or historical bound revisions.
20. The architecture MUST remain viable without one monolithic semantic `MetadataStore`/Registry becoming the owner of every resource kind.

## Deferred decisions

004-C intentionally does not yet choose:

- exact ID encoding or UUID/ULID scheme;
- tenant/namespace wire format;
- database engine;
- relational versus document versus key-value versus event-store implementation;
- ORM/data-access library;
- physical table/collection layout;
- exact transaction/outbox/CAS technology;
- retention periods;
- backup/restore implementation;
- encryption/access-control implementation;
- source snapshot/fingerprint format;
- output manifest/promotion format;
- Learned State component manifest;
- provenance graph/table/event physical schema;
- public handle token serialization;
- exact REST/CLI transport representation.

Those choices are addressed by later Phase 004 groups or Phase 005 implementation planning under this identity/state contract.
