---
type: Phase Record
title: 004-B — Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping
status: complete
---

# 004-B — Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping

## Objective

Translate the accepted Phase 003 experience contract and 004-A architecture constitution into a public representation model that is ergonomic for Python/notebook/CLI/API use while preserving semantic commitment, operational realization, promotion, Evidence, history, reproducibility, safety, and enterprise-scale boundaries.

004-B focuses on public architectural roles rather than final class/method/package names.

## Governing authority

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](../../architecture/architecture-authority-representation-layering.md)
- [Phase 003 Consolidated Experience Contract](../../experience/phase-003-consolidated-experience-contract.md)
- [Learning](../../concepts/learning.md)
- [Learned State](../../concepts/learned-state.md)
- [Generation](../../concepts/generation.md)
- [Evaluation](../../concepts/evaluation.md)
- [Evidence](../../concepts/evidence.md)
- [Execution](../../concepts/execution.md)

## Canonical architecture created

- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../../architecture/public-api-resource-handle-workflow-semantic-mapping.md)

## ADR created

- [ADR-0001 — Typed Resource/Handle Public API](../../decisions/ADR-0001-typed-resource-handle-public-api.md)

## Main decisions

### 1. Public architecture is typed, resource/handle-oriented, identity-first, and payload-separating

The canonical public model preserves the progression:

```text
editable specification
      ↓
readiness/compatibility result
      ↓
committed activity handle
      ↓
Execution/Attempts
      ↓
promoted result handle
      ↓
explicit distributed payload access
```

Evidence, Provenance, reproducibility, dependency posture, and disclosure remain typed inspectable views/resources rather than generic metadata.

### 2. Editable specifications are not committed activities

Learning, Generation, and Evaluation have public specification roles before commitment.

A builder/object may be mutable locally for ergonomics, but object existence or mutation does not create/alter committed historical activity automatically.

Commitment produces a new durable activity identity and immutable semantic snapshot/reference.

### 3. Readiness is an inspectable derived result

Validation/readiness returns contextual reasons, limitations, blockers, indeterminacy, dependency/network/egress posture, and the exact proposed specification assessed.

Readiness is not persisted as global truth on shared semantic authorities.

### 4. Committed domain activities expose typed durable handles

Learning, Generation, and Evaluation each expose distinguishable committed-resource roles.

They may share common implementation protocols, but their semantic lifecycles/result cardinalities/actions remain typed.

### 5. Promoted results have durable identities independent of payload objects

Public result roles distinguish:

- Learned State;
- completed synthetic output;
- Evidence.

A Learned State is not a runtime model object; a completed output is not a DataFrame; Evidence is not a scalar metric.

### 6. Non-final material remains explicitly non-final

Checkpoint/recovery material, partial/candidate output, and Evaluation diagnostics use subordinate/non-final descriptors or references.

They cannot be transparently accepted where a promoted Learned State/output/Evidence resource is required.

### 7. Execution is exposed independently from the semantic activity

A committed activity may expose its associated Execution handle.

Execution has stable logical identity and ordered Attempt history independent of platform-native run/job identity.

Attempt can be addressable for inspection but remains subordinate to Execution.

### 8. Handles resolve canonical state rather than owning mutable copies

A handle represents stable logical identity plus an authorized view/resolver path.

Its meaning cannot depend on one Python process, SparkSession, local Future, platform job object, or memory address remaining alive.

Current mutable lifecycle/applicability state can be refreshed/re-resolved while historical commitment/result facts remain stable.

### 9. Semantic commitment and operational submission remain separate transitions

Architecture supports:

```text
spec -> commit -> activity handle -> submit/start -> Execution
```

A convenience call may combine commit/start, but the resulting state must still expose both boundaries historically.

### 10. Long-running work is resource-oriented, not Future-oriented

Hours/days-long Learning/Generation/Evaluation remain re-resolvable after submitting process turnover.

Blocking/wait/future helpers may exist as conveniences but are not canonical lifecycle identity.

### 11. Payload access is explicit and downstream of result authority

Completed-output handles may resolve Spark DataFrames/tables/files later, but raw payload does not replace result identity.

Candidate output access remains explicitly non-final.

Learned State payload loading remains Strategy/runtime specific and does not replace the logical Learned State handle.

Evidence diagnostics remain separately referenced data-plane material.

### 12. Convenience facades are allowed but cannot own canonical state

High-level `fit`/`generate`-style conveniences may assemble/validate/commit/start/wait, but must return or make directly available the durable activity and result identities.

They cannot make raw model/DataFrame payload the sole public result.

A universal mutable Session/Context remains rejected as canonical ownership.

### 13. Resource navigation follows semantic references

Common navigation is supported directly, for example:

```text
Learning -> Execution -> Attempts
Learning -> Learned State
Generation -> Execution
Generation -> completion Evidence
Generation -> completed output
Evaluation -> Execution
Evaluation -> Evidence
result -> Provenance / reproducibility
```

Navigation does not copy authority into an object graph.

### 14. Public lifecycle/status remains owner-typed

Readiness, domain semantic status, Learned State lifecycle, Evidence applicability, Execution state, Attempt outcome, policy compatibility, disclosure state, and reproducibility remain distinguishable.

One universal status enum is rejected.

### 15. Errors/issues remain typed and actionable

The public contract must distinguish pre-commit blockers, semantic request problems, domain failures, recoverable/terminal operational failures, cancellation races, unknown state, dependency/policy problems, withheld detail, and negative/indeterminate Evidence.

Exact exception/result-envelope mechanics are deferred.

### 16. Search/lookup does not create a Registry god-concept

Typed historical lookup/list/search may exist over canonical identity/persistence services.

A generic registry implementation may support indexing internally but cannot become new semantic ownership.

### 17. Human and programmatic surfaces share one resource semantics

Python, CLI, REST, notebook, and later web/managed-platform surfaces may differ in syntax, but all map to the same distinctions among spec/readiness/commitment/Execution/non-final material/promoted result/Evidence/history.

### 18. Distributed ergonomics remain control-plane safe

Handles are lightweight/reference-oriented and do not require data-plane payload loading for inspection.

SYNGAN should not encourage shipping a stateful control-plane client with hidden network/credentials into arbitrary Spark executor closures; runtime adapters receive bounded execution material through later architecture.

## Alternatives rejected as canonical model

### Universal mutable Session/Context

Rejected because it would consolidate unrelated semantic authority and historical mutation into one object.

### Payload-first `fit -> model`, `generate -> DataFrame`

Rejected because payloads cannot express committed identity, semantic/operational state, candidate/promotion, Evidence, Provenance, or restrictions adequately.

### Spark ML Estimator/Model as universal public abstraction

Rejected because direct-generation and non-Spark-ML Strategies are valid.

### One polymorphic Result resource

Rejected as primary public model because it encourages universal status/metadata and semantic interchange.

### Process-local Future as durable work handle

Rejected because distributed activities outlive client/process lifetimes.

## Illustrative public workflow

The accepted architecture permits a future experience conceptually equivalent to:

```text
spec = define_generation(...)
readiness = validate(spec)
activity = commit(spec)
execution = start(activity)
...
activity = refresh(activity)
output = activity.completed_output
payload = output.read_as_spark()
```

or a convenience flow equivalent to:

```text
activity = generate(...)
activity.wait()
output = activity.completed_output
payload = output.read_as_spark()
```

These are explanatory shapes, not accepted method/class names.

## Architecture consequences for later groups

### 004-C

Must define durable identity/version/reference/persistence semantics so handles can be refreshed/re-resolved and commitment snapshots remain immutable.

### 004-D

Must define how source/candidate/completed-output handles resolve Spark-scale distributed payloads and how candidate/promoted distinctions are enforced.

### 004-E

Must define Strategy/runtime adapters that translate activity specifications/results into model/runtime-specific execution without exposing runtime objects as semantic identity.

### 004-F

Must define Execution/Attempt/checkpoint/retry/recovery/cancellation actions beneath the public Execution handle.

### 004-G

Must define Evidence/Provenance/reproducibility query/resource structures beneath the public inspection surface.

### 004-H

Must define authorization/redaction so resource resolution preserves withheld/unknown/absent/unavailable distinctions.

### 004-I

Must define transport/deployment/client compatibility, async observation, portability, and platform-specific convenience surfaces.

## No new concept result

004-B does not introduce domain concepts for:

- Handle;
- Resource;
- Specification;
- Builder;
- Client;
- Session;
- Result;
- Readiness;
- Registry;
- Future;
- Payload;
- Candidate Descriptor.

These are representation/application architecture roles downstream of accepted semantics.

## Deferred decisions

004-B intentionally does not settle:

- exact Python public names;
- inheritance/protocol hierarchy;
- top-level client name;
- REST/wire schema;
- CLI syntax;
- exact async primitive;
- handle serialization/token format;
- ID/revision format;
- persistence technology;
- Spark payload resolution mechanism;
- Strategy/plugin implementation API;
- scheduler API;
- authorization implementation;
- exact error-code/exception taxonomy.

## Exit criteria

- [x] editable specifications separated from committed activity identity;
- [x] contextual readiness/compatibility result role established;
- [x] typed Learning/Generation/Evaluation committed handle roles established;
- [x] Learned State/output/Evidence promoted result roles established;
- [x] non-final checkpoint/candidate/diagnostic roles kept distinct;
- [x] Execution/Attempt inspection separated from semantic activity state;
- [x] handles defined as stable identity resolvers rather than mutable canonical objects;
- [x] semantic commitment separated from operational initiation;
- [x] long-running work made resource-oriented rather than process-Future-oriented;
- [x] payload access kept explicit/downstream;
- [x] convenience façades allowed without canonical ownership;
- [x] typed status/error distinctions preserved;
- [x] human/programmatic semantic parity preserved;
- [x] distributed inspection avoids full-payload materialization;
- [x] no Session/Result/Registry/Model/DataFrame god abstraction introduced;
- [x] ADR rationale recorded.

## Exit assessment

**Status: complete.**

SYNGAN now has an accepted public representation architecture based on typed specifications, durable activity handles, promoted result handles, subordinate operational/non-final views, and derived historical/safety inspection. This provides an ergonomic path toward Python/Spark usage without sacrificing semantic ownership, long-running durability, enterprise-scale payload separation, or auditability.

## Next phase

**004-C — Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture**
