---
type: Phase Record
title: 004-D — Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture
status: complete
---

# 004-D — Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture

## Objective

Translate the 004-A control/data-plane boundary, 004-B typed handle model, 004-C durable identity/state architecture, and Phase 003 Generation experience into a distributed Spark-scale source/output representation architecture.

004-D must make exact source state, candidate physical state, required Evaluation subject identity, and completed-output semantic authority distinguishable without requiring full driver-local materialization or prematurely selecting a storage provider/format.

## Governing authority

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](../../architecture/architecture-authority-representation-layering.md)
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../../architecture/public-api-resource-handle-workflow-semantic-mapping.md)
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)
- [Generation](../../concepts/generation.md)
- [Provenance](../../concepts/provenance.md)
- [Generation Request, Condition, Validation & Output Promotion Experience](../../experience/generation-request-condition-validation-output-promotion.md)

## Canonical architecture created

- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md)

## ADR created

- [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](../../decisions/ADR-0003-sealed-manifest-gated-output-promotion.md)

## Main decisions

### 1. Spark DataFrame is an access representation, not durable identity

Spark DataFrames are valid distributed input/output access objects but cannot serve as the sole historical identity of committed source state, candidate state, or completed output.

A DataFrame may depend on one SparkSession, logical plan, mutable source, temporary view, or runtime catalog context.

### 2. Mutable source selectors are resolved before commitment

Table names, paths, queries, DataFrames, aliases, and URLs may be used during preparation.

Before source-dependent committed work relies upon them, they must resolve to a stable source-state identity/read boundary strong enough for the owning semantic contract.

Supported architectural bases may include provider-native immutable snapshots, immutable materialized snapshots, immutable manifests, content/fingerprint identity with explicit strength, or external authoritative snapshot identities.

No universal hash technology is selected.

### 3. Historical source identity and stable read binding are both required

Recording a fingerprint/name is not enough if execution can later read different mutable contents.

Committed source-dependent work must read the exact bound source state through provider snapshot isolation, immutable objects/manifests, materialized snapshotting, or equivalent guarantees.

Where a source cannot be pinned sufficiently, readiness must expose the limitation or block commitment according to the owning contract.

### 4. Source snapshotting remains distributed and pre-domain

Snapshot/materialization preparation is allowed to perform large Spark-scale work without becoming Learning or another fabricated domain activity.

The operation must not require full driver collection.

### 5. Physical structure remains distinct from Data Meaning

Manifest/reference structural descriptors may include Spark/storage field types, nullability, partition information, or format metadata needed for resolution.

These do not become semantic Data Meaning authority.

### 6. Typed data-reference roles replace generic path/Artifact identity

Architecture distinguishes source-state references, candidate materialization references, sealed candidate snapshot references, completed-output representation references, and diagnostic/component references even where shared low-level resolver infrastructure exists.

### 7. Manifests are representation mechanisms, not new domain authority

A manifest identifies the physical/logical snapshot, extent, component-index/provider version, structural read requirements, integrity basis, resolver/locator, and relevant parent/reference context.

It does not own Generation Conditions, Constraints, Evidence, Data Meaning, privacy, or approval.

### 8. Manifest roots remain bounded at enterprise scale

The control plane may retain a bounded root manifest/reference while component-level detail remains in distributed indexes/manifests/provider transaction metadata.

The architecture does not require one canonical control-plane record per output file.

### 9. Candidate materialization has an open-to-sealed physical lifecycle

A committed Generation may create one or more distinguishable candidate materializations during fulfillment/recovery.

Mutable/open manifest state may advance while writers are active.

Before required Evaluation or promotion relies on candidate contents, one immutable sealed candidate snapshot/manifest must be established.

### 10. Sealing is physical authority, not Generation completion

A sealed candidate establishes frozen physical extent/identity/integrity to the declared representation strength.

It does not establish mandatory Condition fulfillment, Constraint satisfaction, privacy, external approval, or Generation completion.

### 11. Required Evaluation binds the exact sealed candidate

Evidence used for Generation completion must refer to the same immutable sealed candidate snapshot later considered for promotion.

Evidence about an earlier/different candidate cannot silently validate a replacement candidate.

### 12. Candidate visibility remains non-final by default

Open, sealed-unpromoted, failed, abandoned, and quarantined candidates must not appear in ordinary completed-output resolution.

Platforms unable to isolate candidate/final visibility must expose that limitation during compatibility/readiness.

### 13. Physical completeness/integrity is strength-scoped

Provider snapshot commitment, manifest closure, writer accounting, checksums/digests, row-count summaries, and structural consistency may establish the physical subject.

These facts do not establish semantic validity.

Manifest row counts are physical facts; Generation owns fulfillment of quantity semantics.

### 14. Stale writers must be fenceable

The candidate protocol requires a future mechanism for leases, epochs, unique namespaces, CAS manifest generations, transactional versions, or equivalent fencing so a losing/superseded Attempt cannot mutate the sealed/current candidate invisibly.

004-F will select/refine operational recovery/fencing architecture.

### 15. Duplicate physical work remains acceptable

Retry/speculation/recomputation can create duplicate transient components when candidate membership remains unambiguous and losing material cannot become authoritative.

Exactly-once physical computation is not required.

### 16. Generation promotion is separate, idempotent semantic authority

Promotion is a control-plane transition from one exact sealed candidate to one completed logical output only after all Generation completion obligations are satisfied.

The transition is fenced/idempotent so retries cannot produce two completed outputs for one Generation.

### 17. Promotion may be metadata-only

SYNGAN does not require copying hundreds of millions of rows from staging to a final location just to express semantic finality.

A completed output may reference/reuse the exact sealed candidate bytes in place when the platform/storage contract safely permits it.

The sealed candidate identity and completed-output identity nevertheless remain different roles.

### 18. Completed output is one logical identity over distributed representation

One output may span one table snapshot, many files/partitions, multiple component roots, or provider-managed objects.

The Output handle resolves distributed payload through representation bindings; a returned DataFrame remains an access view, not the result identity.

### 19. Arbitrary downstream Spark transformations do not inherit output authority

A transformed DataFrame read from a completed output is new external/derived data unless a future explicit SYNGAN derivation workflow records otherwise.

Spark lineage alone does not mutate/extend output identity or Provenance.

### 20. Physical representation may evolve only under explicit equivalence

Replication, relocation, compaction, repartitioning, or format migration may preserve one output identity only when an explicit integrity/equivalence process establishes the same logical data under the relevant equality semantics.

The original promotion basis remains historical.

### 21. Logical identity does not require universal content addressing

Provider snapshot versions, immutable manifests, authoritative external snapshot IDs, or fingerprints may establish sufficient source/output distinguishability depending on their actual guarantees.

No universal global sort/full-row content hash is required.

### 22. Incidental Spark row/partition/file order does not define logical identity

Physical ordering is excluded from identity/equality unless the committed semantics explicitly make ordering material.

### 23. Reference resolution remains authorization/no-egress aware

Snapshotting, candidate writes, resolution, relocation, and promotion cannot silently copy data to unapproved destinations or become hidden egress paths.

Detailed authorization is deferred to 004-H.

## Alternatives rejected as universal architecture

- DataFrame or table/path identity as canonical source/output identity;
- final path/table existence as Generation completion;
- mandatory copy-on-promotion;
- exactly-once physical output writes as a semantic requirement;
- universal full-corpus content hashing;
- Evaluation against mutable/open candidate state for completion Evidence;
- generic `Artifact`/`Manifest` semantic ownership;
- control-plane enumeration of every physical file as a default requirement.

## Architecture consequences for later groups

### 004-E

Strategy runtime adapters consume resolved source/Learned-State inputs and write through candidate materialization interfaces. Runtime model objects cannot invent completed-output identity.

### 004-F

Execution/Attempt architecture must define writer epochs/fencing, recovery against open/sealed candidates, reconciliation of ambiguous writes, seal idempotency, promotion idempotency, and safe garbage/quarantine handling.

### 004-G

Evaluation must bind exact sealed candidate/output references; Evidence and Provenance retain those stable identities without copying row payloads.

### 004-H

Authorization/no-egress architecture must govern reference resolution, snapshot destinations, output staging/promotion destinations, locator disclosure, and replication/relocation.

### 004-I

Platform adapters must map provider snapshot/version/transaction/catalog features to this architecture and report guarantee gaps honestly.

## No new concept result

004-D does not introduce domain concepts for:

- Dataset;
- Data Reference;
- Source Snapshot;
- Manifest;
- Candidate Materialization;
- Candidate Snapshot;
- Output Artifact;
- Seal;
- Promotion;
- Partition;
- File Set;
- Table Snapshot.

These are representation/data-plane roles downstream of accepted concepts.

## Deferred decisions

004-D intentionally does not settle:

- concrete table/file/storage technology;
- Delta/Iceberg/Hudi/Parquet/provider selection;
- manifest serialization/physical schema;
- checksum/hash/fingerprint algorithm;
- precise snapshot-retention defaults;
- staging/final naming convention;
- exact writer-fence/CAS mechanism;
- output garbage-collection policy;
- representation-compaction mechanism;
- source snapshot default policy;
- exact Spark public method names;
- authorization/storage credential implementation.

## Exit criteria

- [x] Spark DataFrame separated from durable historical identity;
- [x] mutable source selector separated from resolved stable source state;
- [x] source identity/read-binding architecture established without mandatory full driver hashing;
- [x] structural Spark/storage metadata kept distinct from Data Meaning;
- [x] typed source/candidate/output data-reference roles established;
- [x] bounded root/distributed component manifest architecture established;
- [x] open candidate materialization separated from immutable sealed candidate snapshot;
- [x] seal distinguished from semantic promotion;
- [x] Evaluation completion Evidence bound to exact sealed candidate;
- [x] candidate/quarantine material excluded from normal completed-output discovery;
- [x] stale-writer fencing obligation established;
- [x] duplicate physical work permitted without duplicate authority;
- [x] idempotent single-output Generation promotion contract established;
- [x] promotion allowed to reuse physical bytes without mandatory row copy;
- [x] completed-output identity separated from physical layout/DataFrame;
- [x] representation migration/equivalence boundary established;
- [x] enterprise-scale/no-full-driver-materialization preserved;
- [x] no storage provider or domain god-concept prematurely selected;
- [x] ADR rationale recorded.

## Exit assessment

**Status: complete.**

SYNGAN now has a stable architecture for binding large mutable sources to exact distributed source state, identifying/sealing exact Generation candidates, binding required Evaluation to those immutable candidates, and promoting at most one completed logical output without requiring exactly-once physical computation or copy-on-promotion.

## Next phase

**004-E — Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture**
