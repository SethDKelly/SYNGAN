---
type: Architecture Authority
title: Phase 007-D Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation
status: active
---

# Phase 007-D — Identity, Revision, Serialization, Typed Public Resource/Handle & Programmatic-View Foundation

## Purpose

Refine SYNGAN's representation architecture for durable identity, semantic revision, state/version separation, serialization, typed references/handles and programmatic views **without selecting production classes, wire formats, persistence schemas or executable tests**.

007-D consolidates and sharpens the Phase 004 public-resource and control-plane identity architecture under the Phase 006 reconciliation. It is a design authority, not an implementation slice.

## Governing authority

007-D is downstream of:

- [Concept Design Methodology](../authority/design-methodology.md);
- [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md);
- [Phase 006 Architecture Reconciliation Contract](phase-006-architecture-reconciliation-contract.md);
- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md);
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](public-api-resource-handle-workflow-semantic-mapping.md);
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md);
- accepted concepts, synchronizations and experience authority.

Where an earlier document uses names such as `ResourceRef`, `GenerationHandle`, `StateVersion` or `SchemaVersion`, 007-D treats them as architectural roles unless explicitly stated otherwise.

## Design result

007-D accepts the following foundation:

> **Identity says what logical thing is being referenced; semantic revision says which immutable meaning was bound; state version says which mutable current projection was observed; representation schema version says how a serialized representation is interpreted. None of these may substitute for another.**

It further accepts:

> **A handle resolves and presents authority; it does not become the authority merely because it is convenient to serialize, cache or mutate locally.**

And:

> **Serialization is representation, not mutation authority. Deserializing a resource view does not create a detached canonical object that can be saved wholesale as the new truth.**

## 1. Identity dimensions

SYNGAN architecture SHALL keep the following dimensions independently representable where they are material.

### 1.1 Authority / namespace scope

A reference must resolve in an unambiguous authority scope.

For local-only deployments this may be implicit. For cross-installation, tenant, export/import, federation or external-provider scenarios, architecture must have room for an explicit authority/namespace discriminator.

No specific URI, UUID namespace, tenant-key or federation format is selected here.

### 1.2 Stable logical resource identity

Durable addressable resources have stable logical identity independent of:

- process memory;
- SparkSession/DataFrame identity;
- table/path/URL alias;
- platform run/job ID;
- current storage location;
- current serialization schema.

Identity is never reused for materially different logical authority.

### 1.3 Exact semantic revision / commitment snapshot

Revisioned semantic authority must be referenceable at the exact immutable revision that historical work bound.

Committed Learning, Generation and Evaluation occurrences bind immutable commitment meaning. A later current revision does not retroactively alter that commitment.

### 1.4 Mutable state version / concurrency observation

A durable resource may have mutable current lifecycle or applicability state. The version/freshness of that mutable projection is separate from logical identity and immutable historical meaning.

007-D requires the distinction but leaves mutation/CAS/transaction mechanics to later persistence architecture refinement.

### 1.5 Representation schema version

Serialized/storage representation may evolve independently of semantic meaning.

A schema migration may change how bytes/fields are interpreted while preserving:

- logical identity;
- immutable semantic revision/commitment meaning;
- current lifecycle meaning;
- typed historical references.

Schema version is never a semantic revision number.

### 1.6 External/provider identity and locator

Where a resource is realized by or linked to an external provider, provider-native identity and mutable locator may be retained as typed context.

They do not replace SYNGAN logical identity unless the external system is explicitly the owning authority for that resource role.

## 2. Which things qualify as durable resources

007-D does not adopt a universal `Resource` concept. `Resource` remains a representation role.

Durable addressability is justified when an object has independent historical or operational identity that actors or other authorities must reference later.

### Resource families that require durable addressability

Architecture must support durable typed identity for roles equivalent to:

1. **revisioned semantic authorities** — for example Data Meaning, Constraint, Strategy/configuration and Evaluation Criterion families/revisions;
2. **committed activity occurrences** — Learning, Generation and Evaluation;
3. **promoted semantic results** — Learned State, completed logical output and Evidence;
4. **Execution** and material subordinate operational records where independent inspection/recovery requires it;
5. **Provenance assertions/relationships** when correction or precise historical navigation requires stable distinguishability;
6. **stable source/dependency/artifact identities** when commitments or reproducibility depend on exact historical binding.

### Things that are not automatically durable resources

The following remain values, projections, subordinate descriptors or runtime objects unless another authority gives them independent identity:

- local builders;
- unpersisted draft values;
- readiness/actionability projections;
- list/search pages;
- UI view models;
- Spark DataFrames;
- loaded runtime model objects;
- convenience topology presets;
- candidate/checkpoint/diagnostic payloads merely because they are physically durable;
- one serialized copy of a view.

Addressability does not promote a subordinate mechanism into a domain concept.

## 3. Typed reference architecture

A durable reference carries only the identity context required for its relationship.

Conceptually, a reference may need:

```text
resource / authority kind
logical identity
authority or namespace scope when required
exact semantic revision / snapshot when the relationship is exact
external/provider identity when externally owned or needed for resolution
```

This is a responsibility model, not a committed field list.

### Reference rules

1. A reference is not the referenced payload.
2. A reference is not a mutable locator.
3. A reference is not a bearer credential.
4. A reference to historical meaning must not silently resolve to `latest`.
5. A reference may remain valid even when the payload becomes unavailable.
6. A reference may resolve differently for different actors because disclosure/authorization differs, without changing underlying identity.
7. Cross-kind substitution is invalid even if raw identifier strings happen to match.

### Structural assertion references

Where Data Meaning owns addressable structural assertions, a stable relationship reference must bind both:

```text
exact Data Meaning revision
+
assertion identity within that revision
```

A bare assertion ID detached from the semantic revision is insufficient historical identity.

## 4. Identity, equality and equivalence

007-D distinguishes several comparisons that implementation must not collapse.

### Same logical identity

Two references identify the same logical resource.

### Same exact semantic revision/snapshot

Two references bind the same immutable meaning.

### Same current-state observation

Two views observed the same mutable state version/freshness boundary.

### Representation equivalence

Two serialized representations preserve equivalent logical meaning even if their schema versions or field ordering differ.

### Physical payload equivalence

Two physical artifacts may have equivalent content/integrity while remaining different physical locations or provider objects.

None of these equivalence claims follows automatically from another.

## 5. Handle architecture

A public handle is an identity-bearing resolver/navigation/view role over canonical authority.

### Handle properties

A handle SHOULD be reconstructible from a stable typed reference plus an authorized client/resolution context.

A handle MAY cache a bounded current view, but must preserve distinction among:

- stable logical identity;
- immutable historical facts;
- mutable current state;
- view freshness;
- actor-safe disclosure state.

Refreshing a handle changes the local view, not the logical identity.

### Handle is not credential

A serialized reference/handle representation must not require embedding long-lived secrets merely to preserve identity.

Authorization is evaluated at resolution/action time under the current actor/deployment authority. If a transport uses a signed or capability-bearing token later, that is a security mechanism layered onto the reference role and requires separate design.

### Handle is not a detached mutable entity

Changing fields on a local handle/view cannot by itself mutate canonical state.

Canonical actions must remain explicit owner/application operations. This prevents an ORM-like `load object -> change arbitrary fields -> save whole object` pattern from bypassing owner-specific lifecycle and synchronization rules.

### Typed handle families

Public architecture must preserve semantic role distinctions among handles equivalent to:

- Learning activity;
- Generation activity;
- Evaluation activity;
- Learned State;
- completed output;
- Evidence;
- Execution;
- other accepted durable resource roles.

A common internal mechanism is allowed, but one universal public `Handle`/`Result` object must not erase owned actions, lifecycle or result cardinality.

## 6. Serialization architecture

007-D defines serialization obligations without selecting JSON, MessagePack, Protobuf, Pydantic, Avro, Arrow or another concrete format.

### Three serialization concerns

Architecture distinguishes:

1. **portable reference serialization** — enough information to re-resolve a durable identity;
2. **bounded view serialization** — an actor-safe representation of selected current/historical fields and references;
3. **persistence representation** — storage-oriented encoding owned by later control-plane persistence architecture.

A deployment MAY use one physical encoding for several concerns, but their contracts remain distinct.

### Conceptual serialized envelope

A serialized resource/view may need information equivalent to:

```text
representation kind
representation schema identity/version
resource kind
logical identity
authority/namespace scope when material
exact revision/snapshot identity where material
bounded selected fields
state/freshness context where current state is represented
typed references
actor-safe disclosure/limitation context where required
```

This is not a committed production schema.

### Schema evolution rules

A later serialization design must preserve these invariants:

- schema migration does not create a new logical resource;
- semantic revision does not imply serialization schema change;
- unsupported schema must fail/qualify explicitly rather than be misread;
- unknown extension data must not be silently reinterpreted as semantic absence;
- historical exact references survive compatible reserialization;
- deserialization cannot upgrade `current` or `latest` into an immutable historical fact;
- actor-safe redaction cannot mutate canonical meaning.

### Canonical byte representation is not yet required

007-D does not require deterministic canonical bytes, content-addressed IDs or cryptographic signatures.

Those may be justified later for integrity, export, caching or reproducibility, but must not be introduced merely because serialization exists.

## 7. Programmatic-view foundation

The public/programmatic model SHALL use **orthogonal bounded views** rather than one universal resource payload or status.

Architecture must support view roles equivalent to:

### Semantic/current view

Owner-specific lifecycle/current applicability and immutable establishment/commitment facts appropriate to the resource.

### Historical view

Exact retained historical revision/snapshot/transition context without substituting current state.

### Actionability/readiness view

Current ability to commit/start/retry/resume/use, including blocked/incompatible/limited/indeterminate outcomes where applicable.

### Operational view

Execution/Attempt progress, recovery/cancellation/reconciliation state and platform references without redefining semantic lifecycle.

### Evidence/Provenance view

Findings, claim strength, typed historical relationships and explanation paths appropriate to the actor.

### Disclosure-safe view

A policy-filtered projection that may withhold/redact or intentionally avoid revealing existence while preserving precise internal canonical state where permitted.

### Topology/subject summary view

A bounded description of the exact logical scopes/structural assertions needed to interpret a resource or Evaluation subject without copying distributed payload.

These are composable projection roles, not necessarily separate public classes or endpoints.

## 8. View freshness and historical truth

A view must make it possible to distinguish immutable facts from mutable/current observations.

A stale current view is not false historical data; it is a possibly outdated projection.

Architecture therefore needs room for freshness context such as a state version, observation token, resolved-at boundary or equivalent. 007-D does not choose the exact mechanism.

Historical references remain exact even when current views change.

## 9. Resolution outcomes

Reference/handle resolution must preserve meaningful non-success outcomes rather than collapsing them to `None` or generic not-found.

Architecture must be able to represent outcomes equivalent to:

- resolved;
- withheld/redacted or intentionally non-disclosing;
- known identity but retained representation unavailable;
- unknown/indeterminate;
- invalid/integrity-defective reference;
- unsupported representation/schema.

`Absent` is different: it means the relationship/value was never established in the relevant authority context.

Where existence itself is protected, the outward actor-safe result may intentionally combine several internal cases; this does not erase the internal distinction.

## 10. Cross-surface parity

Python, CLI, REST, notebooks and future managed/web surfaces may use different syntax, but they should map to equivalent architectural roles:

```text
reference
bounded view
editable specification
readiness/actionability result
committed activity handle
Execution view/handle
promoted result handle
historical/Evidence/Provenance view
```

No surface may gain semantic authority merely because it exposes more convenient object mutation or richer platform-native identifiers.

## 11. Large/distributed payload separation

Resource/handle serialization remains control-plane bounded.

A completed output, Learned State or diagnostic dataset may refer to distributed physical representations without embedding them into a serialized public handle/view.

This preserves the enterprise-scale rule that normal control interaction must not require whole payload collection into driver/client memory.

For multi-table/time-series outputs, one logical result identity may navigate several mandatory logical scopes/physical representations while remaining one promoted Generation result.

## 12. Design scenarios / falsification probes

007-D was checked against the following architectural scenarios.

### Scenario A — revision advances after historical commitment

A Generation committed against Data Meaning revision R1 remains bound to R1 after R2 becomes current. A refreshed Generation handle may show current contextual information, but its commitment cannot silently change to R2.

**Result:** supported by separate logical identity + exact revision reference + current view.

### Scenario B — client process restarts

A saved typed reference is re-resolved in a new Python process. No original object identity or SparkSession survives.

**Result:** handle semantics remain valid because identity is durable and the live handle is reconstructed rather than persisted as process state.

### Scenario C — representation schema migrates

A serialized resource view moves from schema S1 to S2 with no semantic change.

**Result:** same logical identity and semantic revision; different representation schema.

### Scenario D — current state changes after view serialization

A serialized view observed state version 8; canonical state later advances to 9.

**Result:** the serialized view remains a historical observation of version 8, not current write authority.

### Scenario E — physical output moves

A completed output moves from one table/path/provider location to another while its logical promoted result remains the same and integrity/equivalence is established.

**Result:** logical identity survives physical relocation; locator is not identity.

### Scenario F — retained payload expires

A historical output identity remains known while payload retention makes the physical representation unavailable.

**Result:** reference resolves to known-but-unavailable rather than `null` or a new current replacement.

### Scenario G — activity and execution differ

A committed Generation exists but has not started operational realization.

**Result:** Generation handle exists without requiring an Execution handle; the two identities remain distinct.

### Scenario H — candidate data is readable

Candidate output files are readable before semantic promotion.

**Result:** physical readability does not create a completed-output handle.

### Scenario I — cross-installation identity collision

Two installations happen to generate the same local identifier text.

**Result:** architecture has room for authority/namespace scope and does not assume bare local IDs are globally unique.

### Scenario J — existence-protected resource

An actor requests a resource whose existence may not be disclosed.

**Result:** outward view may intentionally avoid distinguishing absent/forbidden while canonical security/audit state remains precise.

No scenario requires a new concept or synchronization.

## 13. Deferred architecture choices

007-D intentionally leaves these open for later design refinement where needed:

- concrete identifier encoding;
- exact namespace/federation/export identity format;
- exact Python class/protocol/dataclass spelling;
- concrete JSON/Protobuf/Avro/Pydantic/etc. wire representation;
- compatibility/version-negotiation policy;
- canonical-byte or content-addressing rules;
- signing/capability-token mechanisms;
- persistence table/document schema;
- CAS/transaction/outbox implementation;
- client caching/refresh protocol;
- REST/CLI/notebook syntax;
- transport pagination/search envelopes;
- migration tooling.

These are not authorized implementation work by this document.

## 14. Concept and synchronization audit

007-D introduces **no new concept**.

`Resource`, `Reference`, `Handle`, `View`, `SchemaVersion` and serialization envelope remain architecture roles/mechanisms.

Accepted concept count remains **11**.

007-D introduces **no new synchronization**. Existing commitments, result establishment, Execution handoff, Evidence and Provenance synchronizations remain sufficient.

Accepted synchronization count remains **15**. No `SYNC-16` is created.

## 15. Architecture invariants

1. Logical identity is distinct from physical location and provider/runtime identity.
2. Authority/namespace scope must be representable where bare local identity is insufficient.
3. Exact semantic revision/commitment is distinct from mutable current state.
4. State/freshness version is distinct from semantic revision.
5. Representation schema version is distinct from every semantic/state identity axis.
6. Historical references never silently substitute `latest`.
7. References are typed and cannot be cross-kind substituted merely because identifiers match.
8. A locator may aid resolution but cannot become semantic identity where its target can change materially.
9. A handle resolves authority; it does not own canonical state.
10. A handle/reference is not inherently a credential.
11. Local object mutation does not constitute canonical mutation.
12. Serialization is representation, not write authority.
13. Deserialization cannot transform stale/current observations into immutable historical truth.
14. Schema migration preserves semantic identity unless an explicit semantic change independently occurs.
15. Unsupported/unknown serialization must remain explicit rather than be misread as absence.
16. Programmatic views preserve owner/context rather than collapsing lifecycle, actionability, operation, disclosure and history into one status.
17. Actor-safe disclosure may hide detail/existence outwardly without falsifying canonical state.
18. Candidate/checkpoint/diagnostic material does not become a promoted result because it is addressable or serializable.
19. Control-plane resource/view serialization remains bounded and references large/distributed payloads rather than absorbing them.
20. Existing provisional source/tests do not outrank this architecture design.

## Exit decision

**007-D architecture design: COMPLETE.**

The identity/revision/serialization/resource-handle/programmatic-view foundation is coherent enough for the next design group to build on without committing production representation spelling.

**007-D production implementation: NOT AUTHORIZED.**

The next eligible design subgroup is **007-E — Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline**, but it requires an explicit proceed decision.
