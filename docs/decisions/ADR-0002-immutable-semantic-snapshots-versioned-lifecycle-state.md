---
type: Architecture Decision Record
title: ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State
status: active
---

# ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State

## Decision context

SYNGAN needs durable resources that can be re-resolved across process/cluster turnover while preserving exact historical commitments and allowing current lifecycle state to advance. A single mutable record/version field would risk rewriting history, conflating semantic revision with concurrency, or allowing stale clients to overwrite material state.

At the other extreme, requiring full event sourcing for every authority and every state field would impose a storage/implementation pattern before the architecture demonstrates that it is necessary.

## Governing authority

- [Phase 003 Consolidated Experience Contract](../experience/phase-003-consolidated-experience-contract.md)
- [Architecture Authority, Representation Principles, Layering & Dependency Direction](../architecture/architecture-authority-representation-layering.md)
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../architecture/public-api-resource-handle-workflow-semantic-mapping.md)
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)
- [Provenance](../concepts/provenance.md)

## Decision

SYNGAN will preserve four distinct axes in its durable control-plane architecture:

1. stable logical resource identity;
2. immutable semantic revision or commitment-snapshot identity/content;
3. mutable owner-specific lifecycle state with a conflict-detectable state version/concurrency token;
4. representation/serialization schema version.

Bindable semantic revisions and committed Learning/Generation/Evaluation snapshots are immutable in material meaning.

Current lifecycle/applicability state may advance independently and must use stale-write/conflict detection for material mutations. Silent last-writer-wins is not acceptable for semantic promotion, lifecycle terminal state, restriction/invalidation, correction, or other material authority transitions.

SYNGAN does not mandate full event sourcing. Implementations must retain enough material transition/audit history and coupled-transition intent to explain and reconcile significant changes.

## Alternatives considered

### 1. One mutable record with one `version` field

Rejected because one field would ambiguously serve semantic revision, concurrency, and schema migration, and in-place updates could rewrite what historical work actually bound.

### 2. Full event sourcing as universal persistence model

Rejected as a universal architectural requirement because it is stronger than current semantics require, would constrain storage/platform choices prematurely, and risks operational/documentation complexity. Event-sourced implementations remain compatible if they satisfy the canonical contracts.

### 3. Immutable resources only; every lifecycle change creates a new resource ID

Rejected because Learned State restriction/retirement/invalidation, Evidence applicability changes, and Execution/domain lifecycle advances are changes to the current state of the same historical resource, not new Learned States/Evidence/Executions.

### 4. Mutable semantic snapshots with historical audit log

Rejected because an audit trail cannot make a mutated commitment snapshot equivalent to the exact immutable state historically bound by downstream work.

### 5. Timestamp-based optimistic concurrency

Rejected because clock skew, equal timestamps, and cross-system timing uncertainty make wall-clock time insufficient as the sole material-write authority.

## Consequences

### Positive

- historical commitments remain exact and independently referenceable;
- handles can refresh current state without changing historical identity;
- concurrency conflicts become explicit rather than silently destructive;
- schema migrations can evolve independently from domain semantics;
- revisioned semantic authorities map naturally to immutable bindable revisions;
- current lifecycle status can evolve without fabricating new domain resources;
- implementations remain free to choose relational, document, key-value, event, or other persistence technologies.

### Costs

- persistence schemas need more than one notion of version;
- clients/services must carry or retrieve state-version tokens for material mutation;
- migrations must preserve identity/revision/state-version distinctions;
- cross-resource semantic promotion requires recoverable consistency rather than casual independent writes;
- implementation and testing must account for stale-write conflicts explicitly.

## Compatibility / migration impact

There is no implemented package schema to migrate yet.

Future persisted records and serialized handles must avoid a generic unqualified `version` field when its meaning is ambiguous. Public/wire formats should use semantically distinct names or typed structures for semantic revision/snapshot, lifecycle state version, and representation schema version.

## Canonical architecture affected

- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)

## Supersession

Supersedes: none.

Superseded by: none.
