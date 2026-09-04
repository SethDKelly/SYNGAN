---
type: Architecture Authority
title: Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping
status: active
---

# Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping

## Purpose

Define the public representation architecture through which human-facing tools and programmatic users prepare, commit, observe, recover, inspect, and consume SYNGAN work while preserving accepted semantic ownership and the Phase 003 experience contract.

This document establishes architectural **roles and contracts**, not final Python class names, REST resources, CLI syntax, notebook widgets, package modules, or transport schemas.

## Governing authority

This architecture remains downstream of:

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md);
- [Phase 003 Consolidated Experience Contract](../experience/phase-003-consolidated-experience-contract.md);
- [Accepted Concepts](../concepts/index.md);
- [Accepted Synchronizations](../synchronizations/index.md).

Where examples below use names such as `GenerationSpec`, `GenerationHandle`, or `OutputHandle`, those names identify architectural roles unless a later phase explicitly accepts the concrete public spelling.

## Primary decision

SYNGAN's public architecture SHALL be **typed, resource/handle oriented, identity-first, and payload-separating**.

The public surface preserves at least four distinct representation roles:

```text
editable specification/value
        ↓ validate / review
contextual readiness result
        ↓ commit
committed activity handle
        ↓ operational realization
semantic result handle(s)
        ↓ explicit data/payload access
Spark/distributed/diagnostic physical representation
```

Operational inspection, Evidence, Provenance, reproducibility, dependency posture, and disclosure state remain available through typed views/resources rather than being compressed into one generic result object.

This model rejects both extremes:

- a universal mutable `Session`/`Context` object that becomes the owner of all state; and
- a payload-only API in which `fit()` returns a model object or `generate()` returns only a DataFrame and thereby hides semantic history.

## Public representation families

### 1. Stable references to existing authority

Public workflows need lightweight typed references to canonical/revisioned state owned elsewhere, for example:

- source/input identity;
- Data Meaning revision;
- Constraint revision;
- Synthesis Strategy/configuration revision;
- Evaluation Criterion revision;
- dependency/base artifact identity;
- Learned State;
- completed output;
- Evidence;
- Execution.

A reference carries enough type and stable logical identity to prevent confusing unrelated authority domains.

A mutable path/table/model alias MAY be included as locator/display information but MUST NOT substitute for the stable historical identity required by the owning contract.

The exact identifier syntax and persistence representation are deferred to 004-C/004-D.

### 2. Editable specification values

Before semantic commitment, Learning, Generation, and Evaluation are represented publicly through **editable or replaceable specification values**.

Architectural roles include equivalents of:

- `LearningSpec`;
- `GenerationSpec`;
- `EvaluationSpec`.

A specification MAY be assembled through immutable value construction, a mutable local builder, declarative configuration, or another ergonomic mechanism. Regardless of construction style:

- it is not yet a committed activity merely because a Python object exists;
- changes before commitment do not rewrite historical committed work;
- material defaults/inferences/recommendations remain inspectable;
- validation operates against the proposed specification and current context;
- committing produces a distinguishable committed activity identity/snapshot.

A local builder MAY be mutable for ergonomics, but its mutable state MUST NOT become canonical durable state by accident.

### 3. Contextual readiness/compatibility results

Validation before commitment returns an inspectable derived result rather than silently mutating shared authority.

A readiness/compatibility representation SHOULD expose, where material:

- ready / ready with limitations / blocked / indeterminate posture;
- reasons/issues;
- affected semantic requirement;
- Strategy/method capability result;
- dependency/network/egress compatibility;
- known completion/Evidence obligations;
- assumptions and unresolved facts;
- the specification revision/snapshot that was assessed.

The readiness result is contextual and may become stale when a material input changes.

It is not a durable global status on Data Meaning, Constraint, Strategy, Learned State, Criterion, or dependency.

### 4. Committed activity handles

Once semantic commitment succeeds, the public architecture exposes a **typed durable handle to the committed activity**.

There are distinct semantic roles for:

- Learning activity handles;
- Generation activity handles;
- Evaluation activity handles.

They MAY share an internal protocol or generic implementation, but the public contract MUST preserve their different semantic lifecycle, result cardinality, and owned actions.

A committed activity handle provides access to at least:

- stable logical activity identity;
- exact committed specification/snapshot or a stable reference to it;
- semantic lifecycle/status owned by that activity;
- material limitations/issues;
- associated Execution when operational realization exists;
- resulting/promoted domain resource(s), when established;
- relevant Provenance/history inspection;
- dependency/network/egress posture retained for the commitment;
- reproducibility-relevant inspection where applicable.

The handle does not become a mutable local copy of all authoritative state.

### 5. Promoted result handles

Semantic results are represented independently of the transient computation that produced them.

Architectural roles include:

- Learned State result handle;
- completed synthetic-output handle;
- Evidence handle/resource.

A result handle carries stable logical identity and interpretation/lifecycle information while keeping potentially large payloads separate.

#### Learned State result handle

A Learned State handle exposes logical identity, producing Learning, lifecycle/restrictions, Strategy/dependency context, Provenance, and physical component references required for use.

It MUST NOT be defined as a PyTorch module, Spark ML `Model`, checkpoint, one file, or arbitrary model artifact.

#### Completed output handle

A completed-output handle represents the one authoritative logical output promoted by a successful Generation.

It may resolve to one or more Spark/table/file representations but MUST remain distinct from them.

The public contract SHOULD make the producing Generation and completion status directly inspectable.

#### Evidence handle/resource

Evidence is a durable finding resource rather than a scalar metric result.

Its public representation exposes the finding together with Criterion, subject/reference, scope, claim strength, uncertainty/limitations, applicability, producing Evaluation, and Provenance links appropriate to the actor.

Large diagnostic payloads remain separate referenced data-plane material.

### 6. Non-final materialization descriptors

Checkpoints, partial/candidate output, and diagnostic/intermediate Evaluation material need inspectable representations, but they are **not promoted result handles**.

The API MUST use type/state distinctions sufficient to prevent these from being accepted accidentally where a Learned State, completed output, or Evidence resource is required.

Examples of subordinate/non-final roles include:

- checkpoint/recovery descriptor owned through Execution/Learning context;
- partial/candidate output descriptor owned through Generation context;
- diagnostic material reference owned through Evaluation/Evidence context.

Concrete names and storage structures are deferred to 004-D/004-F/004-G.

### 7. Execution handle and Attempt views

Operational realization is exposed through a logical Execution handle distinct from its parent semantic activity.

The Execution handle exposes:

- stable Execution identity;
- operational lifecycle/status;
- current/latest Attempt summary;
- ordered Attempt history;
- progress/health summaries where meaningful;
- retry/resume/reconciliation/cancellation eligibility/action surfaces;
- checkpoint/recovery references;
- selected platform-job references;
- operational failure/unknown-state information.

Attempt remains subordinate to Execution. It MAY be individually addressable for inspection, but public addressability MUST NOT promote Attempt into independent domain authority.

The public API MUST NOT require users to use Spark/Databricks/native platform job IDs as the primary Execution or Attempt identity.

### 8. Historical and derived inspection views

Not every useful public object is a mutable resource.

Derived/query representations include, for example:

- Provenance path/view;
- historical comparison/difference view;
- reproducibility assessment;
- dependency-resolution/egress compatibility view;
- authorized redaction/disclosure view.

These representations are assembled from canonical state and references. They MUST NOT become shadow state owners merely because they are convenient to serialize or cache.

## Handle semantics

### Handles resolve authority; they do not embody it

A handle is an identity-bearing public reference/view onto canonical state.

Its durable meaning MUST NOT depend on:

- one Python process remaining alive;
- one SparkSession remaining alive;
- one local object-memory address;
- one client-side `Future` or thread;
- one platform job object remaining available.

A handle SHOULD be sufficiently lightweight/reference-oriented that it can be persisted or re-resolved after client/process turnover where authorization and deployment permit.

The exact serialization/token format is deferred.

### Snapshot versus refresh

A public handle MAY expose a snapshot of state for efficient interaction, but the architecture must distinguish:

- stable logical identity;
- immutable historical commitment/result facts;
- mutable current lifecycle/applicability/availability information;
- freshness of the local view.

A refresh/re-resolve operation SHOULD be possible without changing logical identity.

The exact consistency model, ETag/version field, optimistic-concurrency mechanism, and cache behavior are deferred to 004-C.

### Handles are typed by semantic role

A generic internal handle mechanism MAY exist, but public APIs MUST preserve enough type information that users cannot accidentally interchange:

- a Generation handle with an Execution handle;
- a candidate-output descriptor with a completed-output handle;
- a checkpoint with a Learned State handle;
- an Evaluation result with Evidence;
- a source locator with stable source identity.

Runtime type systems, static typing, tagged unions, protocols, or resource-kind fields may realize this later. The architectural requirement is semantic distinguishability.

## Draft-to-commit public flow

The common public flow SHOULD preserve an explicit boundary equivalent to:

```text
create/compose specification
        ↓
validate / readiness inspection
        ↓
review material commitment
        ↓
commit
        ↓
receive committed activity handle
```

A future convenience operation may combine validation and commitment, but it MUST expose the committed specification/history afterward and MUST fail/block explicitly when prerequisites are insufficient.

A pre-commit block does not fabricate a failed Learning/Generation/Evaluation occurrence unless a committed activity actually exists under canonical semantics.

## Commitment versus execution initiation

Semantic commitment and operational initiation are separate architectural actions even if one high-level call commonly performs both.

The public model must permit implementations/workflows equivalent to:

```text
GenerationSpec
    ↓ commit
GenerationHandle (committed)
    ↓ start/submit
ExecutionHandle
```

This supports:

- inspection/approval between commitment and execution where deployments require it;
- durable recovery after client process loss;
- clear auditability of committed work that never started;
- separation between domain semantics and scheduler/platform submission.

A convenience `run`/`fit`/`generate` call MAY commit and start in one user action, but the resulting resources MUST still preserve the two transitions.

## Long-running and asynchronous behavior

Learning, Generation, and Evaluation may run for hours or days. The public API therefore MUST make long-running activity identity and asynchronous observation first-class.

The canonical model SHALL NOT be a process-local future/promise.

A public activity handle should support experience-equivalent operations such as:

- inspect semantic state;
- obtain associated Execution;
- refresh/re-resolve;
- wait/poll/subscribe through later-approved mechanisms;
- request cancellation where permitted;
- resolve promoted result resources when available.

A synchronous/blocking helper MAY wait for a terminal semantic state, but blocking is client convenience rather than the identity/lifecycle model.

## Payload access architecture

### Completed output payload access

A completed-output handle may provide explicit access to a Spark DataFrame, table reference, file set, or another approved distributed representation.

Payload access MUST NOT erase the result handle.

The API MUST NOT require implicit collection to pandas/driver memory.

Illustratively:

```text
completed output handle
     ├─ semantic identity / provenance / limitations
     └─ resolve/read as Spark-distributed payload
```

### Candidate output access

When policy/workflow permits actors to inspect candidate or failed/quarantined material, access MUST be explicitly non-final.

A candidate descriptor MUST NOT be transparently coercible into a completed-output handle merely because the underlying table/files are readable.

### Learned State payload access

A Learned State handle may resolve/load Strategy-specific physical components through a runtime adapter, but the loaded runtime object is not itself the Learned State identity.

The public core SHOULD NOT require every user to load the full Learned State payload merely to inspect its history/status/dependencies.

### Evidence diagnostics

Evidence summaries/findings are control-plane result state. Detailed violation datasets, record examples, attack traces, or similar diagnostics remain separately referenced and may be authorization-restricted.

## Convenience façade architecture

SYNGAN MAY provide one or more high-level clients/facades for ergonomic common workflows.

A façade may:

- create specifications;
- apply defaults/inference/recommendations;
- validate/readiness-check;
- commit activities;
- start operational realization;
- resolve handles by identity;
- wait for completion;
- retrieve promoted result handles;
- query history/Evidence/Provenance.

The façade MUST NOT:

- become the canonical mutable owner of all state;
- require one long-lived session for historical identity;
- hide committed specifications permanently;
- silently substitute dependencies or enable network access;
- return only raw payload when doing so makes semantic/result authority inaccessible;
- conflate activity, Execution, result, Evidence, and approval into one generic `Result`.

A high-level `generate(...)`-style convenience operation is compatible with this architecture if it returns or makes directly available the Generation handle and authoritative output handle rather than exposing only a DataFrame.

Likewise a `fit(...)`-style convenience operation may exist if it preserves the Learning handle and resulting Learned State identity rather than equating the result with a runtime model object.

Exact public method names are deferred.

## Resource relationships exposed through navigation

The public architecture SHOULD make common semantic relationships navigable without requiring users to query a raw graph manually.

Examples:

```text
LearningHandle
  ├─ commitment
  ├─ execution -> ExecutionHandle
  └─ learned_state -> LearnedStateHandle (when established)

GenerationHandle
  ├─ commitment
  ├─ execution -> ExecutionHandle
  ├─ completion obligations / supporting Evidence
  └─ output -> CompletedOutputHandle (when promoted)

EvaluationHandle
  ├─ commitment
  ├─ execution -> ExecutionHandle
  └─ evidence -> EvidenceHandle(s)

CompletedOutputHandle
  ├─ producing_generation
  ├─ provenance
  └─ distributed payload access
```

Navigation is convenience over stable references and MUST NOT duplicate ownership.

## Typed status architecture

Public surfaces MUST NOT expose one ambiguous global status as the only lifecycle representation.

At minimum, the architecture preserves distinct contexts equivalent to:

- readiness/compatibility status for proposed work;
- Learning semantic status;
- Generation semantic status;
- Evaluation semantic status;
- Learned State future-use lifecycle;
- Evidence applicability/current-use status;
- Execution operational status;
- Attempt outcome;
- dependency/policy compatibility;
- disclosure state;
- reproducibility-assessment class/status.

Shared envelope fields such as timestamps, reason codes, or common severity MAY be reused, but owner/context remains explicit.

## Issues, failures, and errors

The public architecture must preserve actionable categories rather than relying on one generic exception string.

Programmatic users should be able to distinguish at least:

- pre-commit readiness/compatibility blocker;
- invalid semantic request/specification;
- committed domain semantic failure;
- recoverable operational Attempt failure;
- terminal Execution failure;
- cancellation requested versus terminal cancellation;
- operational state unknown/reconciliation required;
- dependency unavailable;
- dependency identity mismatch;
- policy/network/egress incompatibility;
- authorization/detail withheld;
- Evidence negative/indeterminate versus Evaluation failure.

The exact split between exceptions, typed result envelopes, issue objects, and transport error codes is deferred. Exceptions MUST NOT be the only durable representation of a long-running activity's terminal state.

## Actions and mutation boundaries

### Specification actions

Before commitment, public APIs may support editing/replacing specifications and re-running validation.

### Activity actions

Committed Learning/Generation/Evaluation handles expose only actions permitted by their semantic lifecycle, such as observation, operational initiation, or cancellation request.

Material semantic changes do not mutate the committed handle; they create a new specification/activity.

### Execution actions

Retry/resume/reconcile/cancel operations are exposed through the operational boundary and must preserve same-commitment safety semantics.

### Result actions

Result resources expose inspection/use/lifecycle actions appropriate to their owner, such as Learned State restriction/retirement/invalidation or Evidence applicability transitions. They do not absorb unrelated activity mutation.

The exact authorization model is deferred to 004-H.

## Search, listing, and resolution

The public architecture MAY provide typed lookup/list/search capabilities for historical resources.

Such capabilities MUST resolve canonical resource identities rather than creating a universal mutable Registry concept.

A generic infrastructure repository/index may support storage/query internally, but public semantic filtering and returned types should retain resource kind and authority.

## Programmatic parity across surfaces

Python, CLI, REST, notebook, and future web/managed-platform surfaces may use different syntax but should map to equivalent resource roles and transitions.

For example, all surfaces must be able to distinguish:

```text
specification
readiness result
commitment/activity identity
Execution identity/state
non-final material
promoted result
Evidence
historical/reproducibility view
```

A surface that only provides payload data without these distinctions is an incomplete convenience surface, not the full SYNGAN public contract.

## Distributed and notebook ergonomics

Public handles SHOULD be lightweight enough to use in notebooks and coordinator-side code without loading their data-plane payloads.

Architecture SHOULD avoid assumptions that a handle can be safely captured inside arbitrary Spark executor closures; distributed workers should receive the minimum immutable execution/runtime material required by an adapter rather than a control-plane client with hidden network/stateful behavior.

The exact serialization, executor-safe context, credential propagation, and Spark closure rules are deferred to 004-D/004-E/004-H/004-I.

## Compatibility with Spark ML and model-specific APIs

Adapters MAY offer familiar compatibility surfaces such as fit/transform/sample-style methods where appropriate.

Such compatibility APIs MUST be façades over SYNGAN resource semantics rather than redefining them.

In particular:

- a Spark ML `Model` cannot be the sole Learned State identity;
- a DataFrame returned by a sampler cannot be the sole completed-output representation;
- direct-generation Strategies must not fabricate an estimator/model lifecycle;
- model-specific methods must remain behind Strategy/runtime boundaries.

## No universal result object

A shared transport/result envelope MAY exist, but it MUST NOT collapse the semantic differences among:

- readiness assessment;
- committed activity;
- operational Execution;
- Learned State;
- candidate output;
- completed output;
- Evaluation completion;
- Evidence finding;
- reproducibility assessment;
- external approval.

The public architecture prefers typed resources/views with explicit relationships over a single polymorphic `Result` object carrying loosely typed metadata.

## API evolution and compatibility boundary

004-B establishes semantic public roles, not final versioning policy.

Later architecture/implementation planning must support evolution without changing historical meaning silently. In particular:

- serialized/resource references need a compatible evolution strategy;
- public status/issue types need extensibility without collapsing unknown future values;
- Strategy-specific extension data needs namespacing or equivalent isolation;
- older historical resources must remain inspectable after client/runtime upgrades where retention guarantees require it.

Exact wire/version negotiation is deferred to 004-C/004-I.

## Architecture invariants

1. Editable specifications MUST remain distinct from committed activity resources.
2. Readiness/compatibility MUST remain contextual derived results rather than global shared state.
3. Learning, Generation, and Evaluation MUST expose distinguishable committed activity handles/resources.
4. A public handle MUST represent stable logical identity rather than process-local object or platform-job identity.
5. Handles MUST resolve canonical state rather than become independent mutable copies of it.
6. Semantic lifecycle and Execution operational lifecycle MUST remain separately inspectable.
7. Checkpoint/candidate/diagnostic material MUST remain type/state-distinct from promoted result handles.
8. Learned State MUST remain distinct from a loaded model/runtime object.
9. Completed output MUST remain distinct from one DataFrame/table/file locator.
10. Evidence MUST remain richer than a scalar metric/Boolean and distinct from Evaluation completion.
11. Attempt may be inspectable/addressable but remains subordinate to Execution.
12. Long-running work MUST remain addressable after the submitting client/process exits.
13. Process-local Futures/promises MUST NOT be the canonical lifecycle identity.
14. Blocking helpers MAY exist but MUST be convenience over durable activity/resource semantics.
15. Convenience façades MUST NOT become canonical mutable state owners.
16. Payload-only return APIs MUST NOT be the only way to access successful Learning/Generation/Evaluation outcomes.
17. Public APIs MUST preserve owner-typed statuses/issues rather than one universal status enum.
18. Public errors/issues MUST distinguish semantic, operational, dependency/policy, indeterminate, and disclosure-restricted conditions where materially actionable.
19. Public resource navigation MUST follow stable references and MUST NOT duplicate authority into a shadow object graph.
20. Ordinary public inspection MUST NOT require loading full source/output/Learned State/diagnostic/telemetry payloads.
21. Human and programmatic surfaces MUST map to equivalent semantic transitions/resources even when syntax differs.
22. Spark/model-specific compatibility APIs MUST remain façades rather than universal semantic architecture.
23. A universal mutable Session/Context/Model/Result/Metadata object MUST NOT replace the typed resource model.
24. Direct-generation Strategies MUST remain representable without fabricated Learning/Learned State handles.

## Deferred decisions

004-B intentionally does not yet select:

- exact Python class names and inheritance hierarchy;
- exact top-level client/facade name;
- builder versus immutable-constructor syntax;
- REST resource URLs or wire schemas;
- CLI command names;
- synchronous versus async Python language primitives;
- handle serialization token format;
- identifier/version format;
- persistence repositories or database technology;
- source/output manifest format;
- Spark DataFrame/table resolution mechanism;
- concrete Strategy/plugin APIs;
- scheduler submission API;
- authentication/authorization mechanism;
- exact exception/error-code taxonomy;
- pagination/search implementation;
- event/subscription mechanism.

Those choices are refined by later Phase 004 groups and Phase 005 implementation planning.
