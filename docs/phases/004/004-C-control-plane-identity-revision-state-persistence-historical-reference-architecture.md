---
type: Phase Record
title: 004-C — Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture
status: complete
---

# 004-C — Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture

## Objective

Define the durable control-plane architecture that allows 004-B resource/handle identities to survive process/cluster turnover while preserving exact semantic revisions/commitments, mutable owner-specific lifecycle state, historical reference resolution, concurrency safety, correction/auditability, bounded persistence, and implementation freedom across storage technologies.

## Governing authority

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](../../architecture/architecture-authority-representation-layering.md)
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../../architecture/public-api-resource-handle-workflow-semantic-mapping.md)
- [Phase 003 Consolidated Experience Contract](../../experience/phase-003-consolidated-experience-contract.md)
- [Provenance](../../concepts/provenance.md)
- [Reproducibility Contract](../../authority/reproducibility-contract.md)

## Canonical architecture created

- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)

## ADR created

- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](../../decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md)

## Main decisions

### 1. Four version/identity axes are separate

Control-plane resources distinguish:

```text
resource identity
semantic revision / commitment snapshot
current lifecycle state version
representation schema version
```

One generic `version` field is rejected as architecturally ambiguous.

### 2. Stable logical IDs are durable, typed and non-reusable

Committed activities, promoted results, Execution, revision families and other durable addressable control-plane state use stable logical identity independent of Python object identity, SparkSession, file/table locator, platform run ID or mutable alias.

Identity encoding remains deferred.

### 3. Historical references are namespace-capable and typed

References preserve target kind, stable identity, exact revision/snapshot when required, and authority/namespace where cross-installation or external resolution requires it.

Mutable locators may accompany references but cannot replace them.

### 4. Bindable semantic revisions are immutable

Data Meaning, Constraint, Strategy/configuration and Criterion revisions become immutable in material semantic content once bindable/effective.

Editable draft state may be persisted separately; material corrections create new revisions.

### 5. Committed activities are occurrences, not mutable revision families

A committed Learning/Generation/Evaluation has one stable activity identity and one immutable material commitment snapshot.

Changing material committed semantics creates a new activity occurrence rather than another revision of the same committed activity.

### 6. Persisted drafts remain distinct from committed activities

A draft/specification may have draft identity/version for collaboration/recovery, but saving it does not fabricate committed Learning/Generation/Evaluation history.

Commitment creates the durable activity occurrence and immutable snapshot.

### 7. Promoted result identity is independent of current lifecycle

Learned State, completed output and Evidence retain stable historical identity while current lifecycle/applicability changes separately.

Restriction, retirement, invalidation, staleness or supersession do not create replacement historical resources merely to express current-use state.

### 8. Mutable lifecycle state uses owner-specific state versions

Current state projections use a monotonic/conflict-detectable concurrency token.

Material writes validate against an expected state/version and stale/conflicting writes are rejected or reconciled rather than silently overwriting newer authority.

### 9. Silent last-writer-wins is prohibited for material authority

Promotion, terminal lifecycle transitions, restriction/invalidation, corrections and similar material transitions cannot rely on silent last-write-wins behavior.

Wall-clock timestamp alone is also insufficient as concurrency authority.

### 10. Material transition history is retained without requiring universal event sourcing

The control plane preserves enough significant transition/audit history to explain lifecycle/promotion/correction/reconciliation outcomes.

Full event sourcing is permitted but not required.

### 11. Logical persistence ownership is separated from physical database count

Distinct mutation ownership is preserved for:

- revisioned semantic authorities;
- committed activities;
- promoted results;
- Execution/Attempt state;
- Provenance relationships;
- derived search/read models.

Several owners may share one physical database technology without becoming one semantic `MetadataStore`.

### 12. Derived indexes/read models are not write authority

Search/list/dashboard/navigation indexes may denormalize selected fields and may be eventually consistent, but material actions must validate canonical owner state before mutation or promotion.

### 13. Coupled transitions require detectable/recoverable consistency

Commitment/snapshot creation, Learning→Learned State establishment, Generation→completed output promotion, Evaluation→Evidence establishment and required Provenance relationships must not silently diverge across crashes/retries.

004-C requires a recoverable consistency strategy but does not prescribe one global distributed transaction mechanism.

### 14. Historical resolution never silently substitutes latest/current state

An exact historical reference either resolves the exact target or returns an explicit resolution/disclosure defect such as withheld/redacted, unavailable, unknown/indeterminate or invalid/integrity failure.

The resolver cannot substitute the latest Data Meaning, Strategy, source alias target, Learned State, dependency or Evidence.

### 15. Known unavailable/withheld history is not ordinary null

Retained identity and relationship semantics survive disclosure restrictions or payload/detail expiry sufficiently to avoid falsely implying that a known historical relationship never existed.

### 16. Corrections preserve authority boundaries

Provenance corrections can supersede/invalidate Provenance assertions without mutating the underlying domain authority.

Data Meaning corrections create new revisions; historical commitments continue referencing the revision actually used.

### 17. Representation schema migration is independent of semantic revision

Persisted record schema evolution can occur without creating new Learning/Generation/Evidence identities or changing immutable commitments.

Schema migrations must preserve stable identity, semantic revisions/snapshots, lifecycle meaning and historical references.

### 18. Control-plane state remains bounded

Canonical persistence scales with resources, revisions, commitment snapshots, material transitions, Attempts, Evidence summaries and material Provenance—not rows, tensors, all tasks/logs or diagnostic records.

## Alternatives rejected as universal architecture

### One mutable record / one version field

Rejected because it conflates semantic revision, lifecycle concurrency and storage-schema migration and encourages historical mutation.

### Universal full event sourcing

Rejected as a mandatory pattern because current semantics require durable material history and recoverability, not one storage paradigm.

### Every lifecycle update creates a new resource identity

Rejected because current-use lifecycle changes often belong to the same historical Learned State, Evidence or Execution.

### Mutable commitment snapshots plus audit log

Rejected because audit cannot make a destructively changed commitment equivalent to the exact historical state originally bound.

### Timestamp-only concurrency

Rejected because wall clocks are insufficient for authoritative concurrent mutation ordering.

### Monolithic MetadataStore/Registry as semantic owner

Rejected because shared persistence infrastructure does not justify ownership of unrelated semantic state.

## Architecture consequences for later groups

### 004-D

Must provide stable source/direct-input/candidate/completed-output identities and distributed payload references/manifests compatible with the typed historical reference and promotion model.

### 004-E

Must bind Strategy/configuration/runtime implementation identities without conflating implementation package version with semantic Strategy revision.

### 004-F

Must implement Execution/Attempt state versions, retry/reconciliation/fencing and coupled promotion consistency beneath the logical state model.

### 004-G

Must define typed Provenance assertion identity/correction and historical query representation using the exact-reference model rather than reconstructing domain truth from graph copies.

### 004-H

Must apply authorization/redaction so exact references can resolve as withheld/redacted versus unavailable/unknown without falsifying history.

### 004-I

Must define deployment, backup/restore, schema compatibility, client refresh and platform integration behavior compatible with durable namespace/resource identity.

## No new concept result

004-C does not introduce domain concepts for:

- Resource ID;
- Revision ID;
- Snapshot;
- State Version;
- Schema Version;
- Draft ID;
- Tombstone;
- Repository;
- Store;
- Index;
- Transaction;
- Event;
- Aggregate;
- Namespace.

These are representation/persistence architecture roles downstream of accepted concepts.

## Deferred decisions

004-C intentionally does not settle:

- UUID/ULID/other ID syntax;
- namespace/tenant wire format;
- database technology;
- physical schema/table layout;
- ORM/repository library;
- event sourcing versus row-oriented implementation;
- exact CAS/transaction/outbox/fencing technology;
- retention period;
- backup/restore implementation;
- source fingerprint/manifest technology;
- output promotion mechanism;
- Provenance physical store;
- authorization/encryption implementation;
- serialized handle token format.

## Exit criteria

- [x] stable resource identity separated from locators/platform IDs;
- [x] semantic revision/commitment snapshot separated from lifecycle state version;
- [x] representation schema version separated from semantic versioning;
- [x] immutable bindable semantic revisions established;
- [x] committed activity occurrence/snapshot model established;
- [x] persisted drafts kept distinct from committed history;
- [x] promoted result identity separated from current lifecycle/applicability;
- [x] concurrency/stale-write detection contract established;
- [x] material transition history required without universal event sourcing;
- [x] logical persistence ownership boundaries established;
- [x] derived indexes prevented from acquiring write authority;
- [x] recoverable cross-resource consistency obligation established;
- [x] exact historical reference resolution semantics established;
- [x] withheld/unavailable/unknown/absent distinction preserved;
- [x] correction/supersession authority boundaries preserved;
- [x] enterprise-scale bounded control-plane persistence preserved;
- [x] ADR rationale recorded.

## Exit assessment

**Status: complete.**

SYNGAN now has an accepted control-plane identity/state architecture capable of supporting re-resolvable long-lived handles, immutable historical commitments, mutable typed lifecycle state, concurrency safety, exact historical resolution, corrections and bounded persistence without selecting a database or collapsing all state into a generic metadata registry.

## Next phase

**004-D — Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture**
