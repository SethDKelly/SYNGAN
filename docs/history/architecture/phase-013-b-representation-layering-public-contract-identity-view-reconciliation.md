---
type: Architecture Reconciliation Authority
title: Phase 013-B — Representation Layering, Public Contract, Identity, Revision, Handle & View Reconciliation
status: active
---

# Phase 013-B — Representation Layering, Public Contract, Identity, Revision, Handle & View Reconciliation

## Purpose

Reconcile SYNGAN's retained representation spine against the completed Jackson concept design and Phase 010 mapping authority before persistence, distributed-data, runtime, operational or deployment architecture is reconciled.

013-B answers:

> **Do the retained layering, public representation, identity/revision, handle and view contracts preserve current semantic ownership and package-first interaction without turning architectural roles into concepts, mandatory workflow stages, API products or shadow state owners?**

Current answer:

```text
YES — THE REPRESENTATION SPINE REMAINS SOUND WITH BOUNDED CLARIFICATIONS.
NO AMAT-2 REPRESENTATION DEFECT IS FOUND.
NO AMAT-3 BLOCKER OR AR-9 UPSTREAM CONTRADICTION IS FOUND.
```

This authority is downstream of the completed concept design and the [Phase 013 Architecture Reconciliation Authority](../authority/phase-013-architecture-reconciliation-authority.md).

---

## 1. Reconciliation subjects

Primary retained subjects reviewed here are:

- `architecture-authority-representation-layering.md`;
- `public-api-resource-handle-workflow-semantic-mapping.md`;
- identity/view portions of `control-plane-identity-revision-state-persistence-historical-reference.md`;
- `phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md`;
- ADR-0001 and ADR-0002 as rationale inputs;
- Phase 010 mapping/parity authority as the current interaction constraint.

Persistence mutation/transaction mechanics remain 013-C work.

---

## 2. Governing representation rule

Architecture represents and composes upstream authority; it does not become that authority.

The current representation spine is therefore:

```text
completed concept / synchronization / mapping authority
        ↓ represented by
stable logical identity + exact references
        ↓
owner-qualified bounded views / handles
        ↓
application coordination and optional convenience façades
        ↓
ports / adapters / host integration
```

The arrows are architecture dependency/representation direction, not a mandatory runtime pipeline.

A representation may combine facts from several owners for inspection or navigation. Combination does not transfer ownership.

---

## 3. Layering reconciliation

The retained Phase 004 inward-dependency architecture is retained with one qualification:

> **“Semantic/control contracts” at the architecture layer means representation contracts for upstream semantic authority; architecture does not redefine the concept state machines or become a second semantic owner.**

The logical responsibility layers remain useful:

```text
representation of semantic/control contracts
application coordination
ports / extension contracts
adapters / integrations
composition / bootstrap
```

They are not required to become:

- five Python packages;
- five services;
- five deployment processes;
- five database schemas;
- five API tiers;
- five D0-D4 disclosure levels.

One physical component may support multiple architecture responsibilities when dependency direction and authority remain explicit. One responsibility may span multiple physical components where scale/security/deployment requires it.

### Layer disposition

```text
core inward dependency principle      RETAIN
one concept -> one component           REJECTED
logical layer -> mandatory package     REJECTED
logical layer -> mandatory service     REJECTED
architecture layer owns semantics      REJECTED
```

---

## 4. Product/public-contract reconciliation

Current Phase 010 product form controls representation:

```text
P1  Python package / SDK                 PRIMARY
P2  notebook / interactive package use   PRIMARY
P3  embedded job / pipeline / automation PRIMARY
P4  CLI                                  OPTIONAL
P5  report / export                      OPTIONAL
P6  graphical presentation               OPTIONAL
P7  host/operator integration            HOST / INTEGRATION ROLE
P8  external handoff                     BOUNDARY
```

No representation contract may imply that REST, a standalone network service, CLI, graphical UI or dedicated admin application is required for the product to exist.

Cross-surface parity therefore means:

> **For every surface that exists for a capability, material semantics must remain equivalent for the same authorized context. It does not require every optional surface to exist.**

A Python-only deployment can satisfy the baseline architecture if it preserves the required semantics.

---

## 5. Representation roles remain roles, not concepts

The retained typed resource/handle model remains valid when interpreted as architectural roles.

Roles may include equivalents of:

```text
editable specification / value
stable typed reference
contextual readiness / actionability view
committed activity handle
Execution handle / Attempt view
owner-specific established result handle
candidate / checkpoint / diagnostic descriptor
historical / Evidence / Provenance / reproducibility view
payload / distributed-material reference
```

None of the following is introduced as a concept by representation:

```text
Resource
Reference
Handle
Result
Status
Workflow
Session
Context
View
SchemaVersion
Readiness
Actionability
Candidate
Checkpoint
```

Addressability, serializability or public visibility does not create independent semantic purpose.

---

## 6. Stable identity and locator/provider separation

The retained identity model is retained.

Durable logical identity remains distinct from:

- Python object identity;
- SparkSession/DataFrame identity;
- path/table/URL aliases;
- provider run/job/model/artifact/catalog identities;
- current physical storage location;
- serialization representation.

Provider-native identity may be retained as typed integration context when useful. It becomes canonical identity only for a role the provider actually owns externally; it cannot substitute for a SYNGAN-owned identity by convenience.

An authority/namespace discriminator remains architecture room rather than a prescribed URI/UUID/federation scheme.

---

## 7. Four independent identity/version axes

013-B retains the core Phase 004/007-D separation:

```text
1. stable logical resource / occurrence identity
2. exact semantic revision or immutable commitment snapshot
3. current owner-specific state version / freshness observation
4. representation / serialization schema version
```

These axes MUST remain separately representable where material.

They answer different questions:

```text
identity          what logical thing is this?
semantic revision what exact meaning was bound?
state version      what mutable current observation/transition generation is this?
schema version     how is this representation interpreted?
```

No generic unqualified `version` field is sufficient when these meanings could be confused.

Current authorization/disclosure and provider/runtime version are additional contextual facts, not replacements for these four axes.

---

## 8. Exact historical binding and mutable current view

A historical relationship that binds an exact revision/snapshot remains exact and non-reactive.

A handle/view may simultaneously expose:

- immutable establishment/commitment facts;
- exact historical references;
- mutable current owner state;
- view freshness;
- actor-safe disclosure qualification.

A refreshed current view does not rewrite what historical work bound.

A stale view is a stale observation, not a different historical truth and not current mutation authority.

---

## 9. Handle contract

A public handle is an identity-bearing resolver/navigation/view role over canonical authority.

It is not:

- canonical state merely because it can be serialized;
- a detached mutable entity whose arbitrary fields can be saved as truth;
- a bearer credential by definition;
- a process-local Future;
- a platform job/run object;
- a universal polymorphic semantic owner.

A handle MAY cache bounded state. It MUST preserve identity versus immutable facts versus mutable current state versus freshness.

A shared internal handle protocol is compatible with this architecture, but public semantics must remain owner-qualified enough that unrelated roles cannot be interchanged accidentally.

---

## 10. Activity handle versus Execution action ownership

The retained public architecture contains historical wording that can be read as allowing a Learning/Generation/Evaluation activity handle itself to own cancellation.

013-B clarifies:

> **Retry, resume, reconciliation and cancellation of operational realization are owned by Execution when Execution exists. An activity-facing convenience action may navigate or delegate to that Execution action, but must not move operational state or authority into the semantic activity.**

Consequences:

```text
activity handle -> inspect semantic state             VALID
activity handle -> find associated Execution          VALID
activity facade -> forward cancel to Execution        VALID WHEN QUALIFIED
activity itself owns Attempt/cancel/retry state       INVALID
activity cancellation UI -> semantic owner transfer   INVALID
```

A committed activity with no Execution does not fabricate an Execution merely so a generic cancellation method can exist.

---

## 11. Result representation does not create a shared result lifecycle

The retained phrase `promoted result handle` is useful only as representation shorthand.

Current ownership remains distinct:

```text
Learning       establishes its completion relation to Learned State
Learned State owns reusable learned-state identity/lifecycle
Generation     owns candidate/finality and completed logical output
Evaluation     owns valid examination completion
Evidence       owns established finding identity/applicability
```

Therefore:

> **“Result handle” is a representation family, not a universal Result concept, lifecycle, promotion operation or state machine. Each represented result is established according to its owning concept.**

A completed output handle remains a Generation-owned representation role, not evidence for a standalone Output concept.

---

## 12. Readiness/actionability representation

Contextual readiness/actionability remains a derived assessment over a proposed action and current environment/authority.

It is not:

- a durable global status on Data Meaning, Strategy, Constraint, Learned State, Criterion or dependency;
- a universal Validation concept;
- a substitute for semantic preconditions;
- a guarantee that operational realization will later succeed.

A readiness view may be persisted/cached as an observation for audit or usability, but doing so does not make it the owner of the facts from which it was derived.

When a material input changes, the assessment may become stale.

---

## 13. Orthogonal bounded views

013-B retains the Phase 007-D bounded-view architecture.

Useful view roles include:

```text
semantic/current owner view
historical/as-bound view
actionability/readiness view
operational Execution/Attempt view
Evidence/Provenance explanation view
disclosure-safe view
topology/subject summary view
```

They are composable projections rather than mandatory resources/classes/endpoints.

A composed view may show multiple owners together but MUST preserve the owner of each material fact.

Caching or serialization cannot turn a projection into canonical write authority.

---

## 14. Progressive disclosure reconciliation

Phase 010 D0-D4 is presentation depth:

```text
D0  task intent / immediate semantic action
D1  material semantic basis
D2  optional capability detail
D3  historical / explanatory depth
D4  distributed / host operational drill-down
```

013-B explicitly rejects interpreting D0-D4 as:

- architecture layers;
- API versions;
- REST resources;
- Python package tiers;
- database projections that must always exist;
- UI pages/screens;
- security classification levels.

The durable rule remains:

> **A decision-material qualifier must surface at D0/D1 when omitting it could change the actor's immediate semantic decision or make the state appear stronger than the owner supports.**

Architecture may defer explanatory depth, not material truth.

---

## 15. Draft, commitment and operational initiation

The retained draft/commit distinction remains valid.

An editable or saved specification is not a committed Learning, Generation or Evaluation merely because a Python object or persisted draft exists.

Commitment establishes a distinct occurrence and exact immutable commitment meaning.

Operational initiation remains distinct from semantic commitment even when a convenience call performs both in one user gesture.

This distinction does not require every activity to pass through a visible multi-step wizard or to have an Execution. Execution remains capability/occurrence-conditional.

---

## 16. Long-running/asynchronous representation

Durable identity and re-resolution remain required for work that outlives a client process.

This does not require:

- a remote service;
- an always-running control daemon;
- all activities to execute asynchronously;
- all callers to poll;
- a provider job for every activity.

Synchronous/blocking helpers remain valid client ergonomics over the same durable semantic identities where appropriate.

---

## 17. Payload separation and scale

The retained payload-separation rule remains valid.

Control interaction must remain bounded/reference-first. A handle/view may navigate a distributed Spark-scale output, Learned State or diagnostic payload without embedding/collecting it.

No public representation contract may make full `collect()`, `toPandas()`, driver-local model loading or complete telemetry materialization an ordinary prerequisite for inspection.

Physical payload readability remains distinct from semantic result establishment.

---

## 18. Findings and dispositions

### A13-B-001 — Layer-A semantic/control wording

```text
origin       Phase 004-A representation/layering
observation  “semantic/control contracts” could be read as architecture owning semantic contracts
current      architecture represents upstream semantic authority
class        AR-2 / AR-3
materiality  AMAT-1
disposition  CLARIFY
result       RESOLVED BY 013-B
upstream     NONE
```

### A13-B-002 — Activity-handle cancellation wording

```text
origin       Phase 004-B public resource/handle architecture
observation  activity-facing wording can imply cancellation is an activity-owned action
current      operational cancellation/retry/recovery belongs to Execution
class        AR-3
materiality  AMAT-1
disposition  CLARIFY
result       RESOLVED BY 013-B
upstream     NONE
```

### A13-B-003 — Optional-surface parity wording

```text
origin       retained public/cross-surface representation language
observation  listing Python/CLI/REST/notebook/web together can be misread as requiring all surfaces
current      package/notebook/automation primary; other surfaces optional/integration roles
class        AR-7
materiality  AMAT-1
disposition  CLARIFY
result       RESOLVED BY 013-B
upstream     NONE
```

### A13-B-004 — Generic “promoted result” wording

```text
origin       retained public handle architecture
observation  umbrella result wording could imply one shared result lifecycle/promotion owner
current      Learned State, Generation output and Evidence retain owner-specific establishment semantics
class        AR-3 / AR-6
materiality  AMAT-1
disposition  CLARIFY
result       RESOLVED BY 013-B
upstream     NONE
```

### A13-B-005 — Phase 007-D synchronization count

```text
origin       007-D concept/synchronization audit
observation  retained text states accepted synchronization count = 15
current      15 historical IDs / 13 active cross-concept synchronizations
class        AR-1
materiality  AMAT-1
disposition  CLARIFY / SUPERSEDE HISTORICAL COUNT
result       SEMANTICALLY RESOLVED; CORPUS CLEANUP CARRIES TO 013-I
upstream     NONE
```

### A13-B-006 — Historical representation precedence

```text
origin       Phase 004/007-D and ADR governing-authority wording
observation  pre-Phase-012 documents present themselves as current direct architecture authority
current      013-A precedence reset + this 013-B authority govern current representation interpretation
class        AR-2
materiality  AMAT-1
disposition  CLARIFY; final historical-status cleanup in 013-I
result       CURRENT AMBIGUITY REMOVED BY PHASE 013 PRECEDENCE
upstream     NONE
```

### A13-B-007 — D0-D4 architecture-tier risk

```text
origin       Phase 010 mapping carried into architecture
observation  future architecture could mistake disclosure depth for technical tiers
current      D0-D4 is semantic presentation depth only
class        AR-0 preventive guardrail
materiality  AMAT-0
disposition  RETAIN GUARDRAIL
result       CLOSED
upstream     NONE
```

---

## 19. Retained subject disposition

```text
architecture-authority-representation-layering.md
  ALIGNED-WITH-CLARIFICATION

public-api-resource-handle-workflow-semantic-mapping.md
  ALIGNED-WITH-CLARIFICATION

control-plane identity/revision/view rules
  ALIGNED
  persistence/concurrency details continue to 013-C

phase-007-d identity/revision/serialization/handle/view foundation
  ALIGNED-WITH-CLARIFICATION
  historical synchronization count cleanup remains for 013-I

ADR-0001 typed resource/handle public API
  PROVISIONAL 013-B DISPOSITION: RETAIN
  final ADR status sweep: 013-I

ADR-0002 immutable semantic snapshots/versioned lifecycle state
  PROVISIONAL 013-B DISPOSITION: RETAIN
  persistence implications continue to 013-C
  final ADR status sweep: 013-I
```

No ADR amendment is required by 013-B's representation conclusions. 013-I retains final lifecycle/status authority for ADRs.

---

## 20. Reconciliation result

```text
representation subjects materially reviewed     4 authority groups
ADRs provisionally reviewed                     2
AMAT-2 defects                                  0
AMAT-3 blockers                                 0
AR-9 upstream contradictions                    0
upstream reopen                                 NONE
new concept                                     NONE
new synchronization                             NONE
mandatory new product surface                   NONE
mandatory package/service topology              NONE
```

All 013-B AMAT-1 issues are resolved semantically by this current authority. Historical frontmatter/count/wording cleanup remains tracked for 013-I where changing the old records themselves is necessary to remove residual corpus ambiguity.

---

## 21. Downstream handoff to 013-C

013-C receives these current representation invariants:

- architecture represents but does not own semantic truth;
- stable identity is separate from locator/provider identity;
- identity, semantic revision/commitment, current state version and schema version are distinct;
- exact historical binding remains non-reactive;
- handles/views are resolvers/projections, not detached canonical entities;
- owner-qualified views may compose without transferring ownership;
- Execution owns retry/resume/reconcile/cancel operational state;
- result-handle grouping does not create a shared Result lifecycle;
- optional surfaces remain optional while preserving parity when present;
- D0-D4 remains presentation depth, not technical architecture tiers;
- bounded/reference-first interaction is required at Spark scale.

013-C must determine how persistence/history/concurrency/migration can realize these invariants without creating generic CRUD authority or rewriting historical truth.

---

## Current next boundary

**013-C — Control Persistence, Historical Reference, Transaction/Concurrency, Migration & Recovery-State Reconciliation** becomes eligible after the 013-B phase record is accepted.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
