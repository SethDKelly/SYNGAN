---
type: Architecture Decision Record
title: ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion
status: active
---

# ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion

## Decision context

SYNGAN Generation may write hundreds of millions of records across many Spark partitions/files/table versions and may retry, speculate, resume, validate, or fail after substantial physical data exists.

The architecture therefore needs a stable way to identify the exact physical candidate that Evaluation examined and Generation may promote, without requiring row copying at promotion and without equating a path/table/DataFrame with semantic completion.

The same architecture must preserve enterprise-scale operation and tolerate duplicate physical computation while guaranteeing at most one authoritative completed output per successful Generation.

## Governing authority

- [Generation](../concepts/generation.md)
- [Generation Request, Condition, Validation & Output Promotion Experience](../experience/generation-request-condition-validation-output-promotion.md)
- [Architecture Authority, Representation Principles, Layering & Dependency Direction](../architecture/architecture-authority-representation-layering.md)
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../architecture/public-api-resource-handle-workflow-semantic-mapping.md)
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md)

## Decision

Generation output materialization will use an architectural boundary equivalent to:

```text
open distributed candidate materialization
        ↓
sealed immutable candidate snapshot / manifest
        ↓
Evaluation and completion checks bind exact sealed candidate
        ↓
Generation semantic promotion
        ↓
one completed logical output identity
```

A sealed manifest/provider-equivalent snapshot identifies the exact physical subject and establishes declared physical completeness/integrity. It does not grant Generation completion authority.

Generation promotion is a separately fenced/idempotent control-plane transition. It may reuse the sealed candidate bytes in place and therefore does not require copying the distributed output to create semantic finality.

The completed-output resource retains one stable logical identity independent of file/table/DataFrame layout and references the sealed candidate snapshot that formed its original promotion basis.

## Source-state companion rule

Committed source-dependent work must also resolve mutable Spark/table/path/DataFrame selectors to a stable source-state identity/read boundary before the source can be relied upon historically.

A provider-native immutable version, immutable materialized snapshot, manifest, external authoritative snapshot identity, or sufficiently strong equivalent may satisfy the source-state contract. One universal full-content hash is not required.

## Alternatives considered

### 1. Treat final storage path/table existence as completion

Rejected because physical writes may complete before required Condition/Constraint validation, and failed/cancelled work may leave readable data.

### 2. Return a Spark DataFrame as the canonical output identity

Rejected because DataFrame identity is process/session/runtime dependent and does not preserve Generation identity, promotion, history, Evidence, or durable exact snapshot semantics.

### 3. Copy candidate data to a separate final location during promotion

Rejected as a universal requirement because copying hundreds of millions of rows solely to express semantic finality is unnecessarily expensive. Copy-on-promotion remains compatible where a platform/deployment needs it, but semantic promotion can be metadata/control-plane based.

### 4. Require exactly-once physical writes

Rejected because distributed systems may recompute/speculate/retry legitimately. The semantic requirement is unambiguous candidate membership and single semantic promotion, not exactly-once computation.

### 5. Require a universal full-corpus content hash for all sources/outputs

Rejected because provider-native snapshot/version guarantees or immutable manifests may provide sufficient identity more efficiently, while some enterprise datasets make canonical row ordering/full hashing expensive or semantically unnecessary.

### 6. Allow Evaluation against an open/mutable candidate

Rejected for completion Evidence because later writes could make the evaluated subject differ from the promoted subject. Required completion Evaluation must bind an immutable sealed candidate snapshot.

### 7. Use one generic Artifact/Manifest resource as semantic owner

Rejected because manifests are representation mechanisms and must not absorb Generation, Evidence, Data Meaning, Provenance, authorization, or other semantic authority.

## Consequences

### Positive

- required Evaluation can identify exactly which candidate it examined;
- retries and speculative writes can occur without creating multiple final outputs;
- semantic promotion does not require expensive data copying;
- completed output remains durable and navigable independently of Spark DataFrame/session lifetime;
- source and output identity can exploit platform-native immutable snapshot capabilities;
- failed/cancelled candidate material remains visibly non-final;
- physical compaction/relocation can evolve independently when equivalence is established;
- control-plane state remains bounded while manifests/component indexes may remain distributed.

### Costs

- adapters need an explicit candidate materialization and sealing contract;
- output writers need fencing/ownership semantics so stale Attempts cannot mutate the sealed/current candidate;
- Evaluation and Evidence must carry exact candidate snapshot references;
- platforms without strong snapshot/isolation capabilities may require additional staging/materialization work;
- garbage collection must distinguish open, sealed, quarantined, and promoted physical material;
- implementations must preserve separate candidate snapshot and completed-output identities even when they reference the same physical bytes.

## Compatibility / migration impact

There is no implemented output architecture to migrate yet.

Future implementations must avoid making a mutable path, DataFrame object, table alias, or file-set listing the sole durable source/output identity. They must also avoid requiring physical row copying as the only way to express Generation promotion.

## Canonical architecture affected

- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md)

## Supersession

Supersedes: none.

Superseded by: none.
