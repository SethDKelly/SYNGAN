---
type: Architecture Authority
title: Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture
status: active
---

# Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture

## Purpose

Define how SYNGAN identifies, resolves, materializes, validates, and promotes Spark-scale structured data without equating a Spark DataFrame, table/path, file set, or completed write with durable semantic identity.

This document establishes the canonical Phase 004-D distributed data-plane architecture beneath the typed resource/handle model and control-plane identity architecture. It defines logical reference, snapshot, manifest, materialization, sealing, and promotion contracts while leaving concrete Spark storage technology and file/table formats open.

## Governing authority

This architecture remains downstream of:

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md);
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](public-api-resource-handle-workflow-semantic-mapping.md);
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md);
- [Generation](../concepts/generation.md);
- [Provenance](../concepts/provenance.md);
- [Phase 003 Consolidated Experience Contract](../experience/phase-003-consolidated-experience-contract.md);
- [Generation Request, Condition, Validation & Output Promotion Experience](../experience/generation-request-condition-validation-output-promotion.md).

## Primary decision

SYNGAN SHALL separate four data-plane concerns that are often incorrectly collapsed:

```text
MUTABLE ACCESS / LOCATOR
Spark DataFrame, table name, path, query, catalog alias
        ↓ resolve / snapshot
DURABLE DATA-STATE REFERENCE
exact source or candidate state used by committed work
        ↓ materialize / seal
IMMUTABLE MANIFESTED PHYSICAL SNAPSHOT
bounded root identity + distributed representation/integrity basis
        ↓ semantic owner validation
PROMOTED LOGICAL RESULT
Learned State / completed output / Evidence according to owning concept
```

For Generation specifically:

```text
Generation commitment
        ↓
distributed candidate materialization
        ↓
sealed immutable candidate manifest
        ↓
required Condition / Constraint / integrity / provenance Evidence
        ↓
Generation semantic promotion
        ↓
one completed logical output identity
```

A manifest establishes the identity, physical extent, and integrity basis of the material being discussed. It does **not** by itself establish that Generation Conditions or Constraints were satisfied, that privacy is acceptable, or that Generation may complete.

## Spark boundary

### Spark DataFrame is an access representation, not durable identity

A Spark DataFrame MAY be accepted or returned at public/runtime boundaries as a distributed data access object.

A DataFrame object MUST NOT by itself serve as the durable historical identity of source or output state because its meaning may depend on:

- one SparkSession/process;
- an unresolved logical plan;
- mutable underlying tables/files;
- runtime catalog/session configuration;
- non-durable temporary views;
- provider-specific time/version defaults;
- nondeterministic query behavior.

A DataFrame can therefore participate in preparation, profiling, Learning, Generation, Evaluation, or payload consumption only through an architectural boundary that distinguishes the ephemeral access object from the stable state identity required by committed work.

### No implicit collection boundary

Resolving, snapshotting, manifesting, validating, or reading a source/output MUST NOT require ordinary full-corpus `collect()`, `toPandas()`, or equivalent driver-local materialization.

Spark-native data access remains distributed.

Small bounded summaries, structural descriptors, counts, digest roots, manifest metadata, and diagnostic samples may be returned to the control plane when appropriate.

### Driver versus executor boundary

A public SYNGAN handle or control-plane client SHOULD normally be resolved on the coordinating/driver side to produce bounded runtime specifications and distributed data references.

Architecture MUST NOT require serializing a stateful control-plane client, credentials, network policy engine, or mutable resource handle into arbitrary Spark executor closures merely to process data.

Runtime adapters may distribute bounded immutable execution material as defined later in 004-E/004-F.

## Distributed data-reference architecture

### Typed data references

SYNGAN SHALL use typed architectural references for data-plane roles rather than one unqualified `ArtifactRef` or path string.

Roles include equivalents of:

- source-state/snapshot reference;
- direct-generation input snapshot/reference;
- candidate-materialization reference;
- sealed candidate snapshot/manifest reference;
- completed-output representation reference;
- Evaluation diagnostic/violation dataset reference;
- Learned State component reference where 004-E requires it.

These may share infrastructure, but their semantic role and final/non-final status remain distinguishable.

### Reference content

A distributed data reference conceptually preserves or can resolve enough information equivalent to:

- reference role/kind;
- stable logical identity or externally stable version token;
- authority/provider/namespace where required;
- resolution method/provider kind;
- physical locator(s) or a locator root;
- immutable snapshot/version/manfiest token when available;
- structural representation information needed to read safely;
- identity/integrity basis;
- logical scope/extent summary where material;
- representation schema/version where required;
- authorization/disclosure hooks by reference, refined in 004-H.

The exact public wire format is deferred.

### Locator is not identity

The following MAY be locators but are not sufficient durable identity when mutable:

- `catalog.schema.table`;
- `/mnt/data/customer`;
- `s3://bucket/prefix`;
- a SQL string;
- a temporary view;
- a DataFrame object;
- a model/data registry alias;
- a URL.

If a locator maps to a mutable target, commitment must bind a distinguishable immutable source state or fail/qualify according to the owning contract.

## Source-state architecture

### Source selector versus resolved source state

Preparation may begin from a mutable **source selector** such as a table name, path, query, DataFrame, catalog reference, or other user-facing locator.

Before committed work depends on that source, the architecture MUST produce a **resolved source-state reference** strong enough to identify the exact logical source state actually read.

Conceptually:

```text
source selector
  analytics.customer
        ↓ resolve
source state S17
  provider: versioned table
  immutable version token: V483
  locator: analytics.customer
```

or:

```text
ephemeral DataFrame
        ↓ distributed snapshot
source state S18
  manifest: M18
  immutable snapshot locator: ...
```

The selector may remain useful for display/current-state comparison, but committed history binds the resolved source state.

### Source identity basis

004-D does not mandate one identity technology. A valid source-state reference MAY be based on one or more mechanisms such as:

1. **provider-native immutable/versioned snapshot** — an external table/catalog/storage system exposes a version/snapshot token whose semantics are strong enough to reread the same logical state;
2. **immutable materialized snapshot** — SYNGAN or an approved adapter creates a durable distributed snapshot and manifests it;
3. **immutable object/component manifest** — a stable set of immutable physical components is identified by an immutable manifest;
4. **content/fingerprint identity** — a digest/fingerprint or hierarchical digest establishes distinguishability to a declared coverage/strength;
5. **external authoritative snapshot identity** — another trusted system owns the snapshot/version guarantee and SYNGAN records that exact authority/version.

These mechanisms can be combined.

A mutable locator plus a sampled profile or creation timestamp is not automatically strong enough to satisfy historical identity.

### Identity proof strength is explicit

A fingerprint is useful only to the strength of what it actually covers.

Architecture MUST NOT imply that:

- a schema hash identifies row content;
- a row count identifies content;
- a sampled fingerprint proves full-corpus equality;
- a path listing proves object immutability;
- a table name plus timestamp pins a transactional snapshot;
- a digest proves future resolvability if the referenced payload is later deleted.

Later implementations may expose provider-specific identity/integrity strength. The architectural requirement is that unsupported guarantees remain explicit.

### Stable read binding

Historical identity alone is insufficient if an activity can read a different/mixed source state during execution.

A committed source-state reference used by Learning, direct Generation, or Evaluation MUST support a read binding strong enough that execution accesses the committed state, not silently the mutable source's later contents.

This may rely on a provider-native snapshot read, immutable manifest/object set, materialized snapshot, or equivalent mechanism.

If a mutable source cannot provide a stable read boundary, the system SHOULD materialize/pin a distributed snapshot before commitment. If it cannot, readiness must expose the limitation or block commitment where the owning semantic contract requires exact source-state binding.

### Snapshot preparation is not Learning

Creating/resolving a stable source snapshot is a data-reference/preparation operation. It MUST NOT fabricate Learning or another domain activity merely because distributed work was required to snapshot data.

Operational work needed for snapshotting may later have its own infrastructure execution/telemetry, but it does not change the accepted concept model.

### Structural descriptor versus Data Meaning

A source reference/manifest MAY preserve a Spark/storage structural descriptor such as field names, physical types, nullability, partitioning hints, or format metadata needed for safe resolution.

That descriptor is not [Data Meaning](../concepts/data-meaning.md).

For example:

```text
Spark IntegerType
    != semantic numeric quantity
```

Structural information may support compatibility checks but cannot become semantic interpretation implicitly.

### No permanent single-table assumption

A source-state reference may represent one table/file set or a logical collection of components/scopes.

004-D does not introduce a relational `Relationship` concept, but its reference/manifest architecture MUST NOT make one Spark DataFrame/table a permanent invariant for future multi-component or relational work.

## Manifest architecture

### Manifest is an architectural contract, not a domain concept

A **manifest** is an immutable or versioned representation mechanism that identifies the physical/logical data-plane state belonging to a snapshot/materialization.

It is not a new `Artifact`, `Dataset`, `Output`, or `Metadata` concept.

### Root manifest and component detail

Enterprise output/source state may span thousands or millions of physical objects. The canonical control plane SHOULD NOT require one canonical row/object per data file merely to retain identity.

The manifest architecture therefore permits:

```text
bounded root manifest record/reference
        ↓
component index / manifest tree / provider snapshot
        ↓
distributed files / partitions / table versions / objects
```

The root carries bounded identity/integrity/extent facts and references deeper component detail when required.

A provider-native immutable table snapshot may require only a compact provider/version reference rather than an enumerated file list.

### Manifest information

An immutable sealed manifest or provider-equivalent snapshot should preserve or resolve enough information equivalent to:

- manifest/snapshot identity;
- role: source, candidate, completed representation, diagnostic, etc.;
- owning/parent resource reference where applicable;
- exact physical snapshot/version or component-index root;
- logical extent summary where meaningful;
- structural descriptor required for reading;
- integrity/digest/checksum basis and its strength where applicable;
- component count/partition summary where useful;
- creation/seal context and representation schema version;
- provider/format/resolver kind;
- provenance/Attempt associations by reference where material;
- locator(s) necessary for resolution;
- retention/availability state by reference where later architecture supplies it.

The manifest MUST NOT copy Conditions, Constraints, Evidence, or all Generation state merely to be self-describing. Those remain canonical elsewhere and are linked by stable references.

### Open versus sealed manifest state

A materialization may maintain mutable/open manifest state while distributed writers are still producing components.

Before the materialized data becomes a stable subject for required Evaluation or semantic promotion, architecture SHALL establish an immutable **sealed manifest snapshot** or provider-equivalent immutable snapshot token.

Conceptually:

```text
candidate materialization CM17
  manifest state v1 ... vN  [open / changing]
        ↓ seal
sealed candidate snapshot SC17
  immutable physical extent + identity basis
```

The mutable state version during materialization is distinct from the immutable sealed snapshot identity, following 004-C's version-axis rules.

### Seal semantics

Sealing establishes that:

- the candidate/source snapshot to be referenced is frozen under its representation contract;
- the physical extent claimed by the manifest is closed to ordinary writes under that identity;
- required component/index integrity checks needed to trust the manifest have succeeded to the declared strength;
- the snapshot can be resolved consistently enough for Evaluation/promotion checks;
- later writers cannot silently change that sealed snapshot.

Sealing does **not** establish:

- mandatory Condition fulfillment;
- Constraint satisfaction;
- privacy/disclosure safety;
- Generation semantic completion;
- external release/use approval.

If material changes are required after sealing, the system creates another distinguishable candidate snapshot/materialization rather than mutating the sealed snapshot in place.

## Candidate materialization architecture

### Candidate identity

Distributed Generation writes into one or more **candidate materializations** subordinate to the committed Generation.

A candidate materialization has stable distinguishability sufficient for recovery, sealing, Evaluation binding, and diagnosis, but it is not the completed-output result identity.

A single Generation MAY have more than one distinguishable candidate materialization/snapshot over its fulfillment history when retries/recovery/resynthesis semantics permit. Only zero or one may become the successful completed output under the current Generation cardinality.

### Candidate physical lifecycle

Architecture preserves physical states equivalent to:

- **allocated/prepared** — candidate write target/reference established;
- **materializing/open** — distributed writes may still change the candidate;
- **sealed** — one immutable candidate snapshot is established for validation/promotion;
- **quarantined/abandoned** — retained for recovery/diagnosis but ineligible for ordinary completed-output discovery;
- **promoted-as-output** — the sealed candidate snapshot is the physical basis of the one semantic completed output.

These are data-plane/materialization states, not a replacement for Generation's semantic lifecycle.

### Candidate visibility

Default completed-output discovery MUST NOT discover an open, sealed-but-unpromoted, failed, cancelled, abandoned, or quarantined candidate as though it were the completed synthetic result.

Adapters SHOULD use physical isolation, namespace/version isolation, access labeling, catalog state, or another mechanism sufficient to uphold that contract.

If a target platform cannot prevent consumers from confusing candidate state with final output, that limitation must be exposed during readiness/compatibility rather than hidden.

### Candidate identity for Evaluation

Any Evaluation used to establish a Generation completion obligation MUST bind the exact sealed candidate snapshot/manifest identity it examined.

If the candidate changes or another candidate is produced, prior Evidence does not automatically apply to the new candidate.

Conceptually:

```text
SC17 --evaluated by--> V31 --produced--> E44
SC18 --new candidate-->

E44 does not automatically validate SC18
```

This makes Generation validation robust against retries and late writes.

## Distributed completeness and integrity

### Physical completeness is not semantic completeness

A sealed candidate must have enough physical completeness/integrity evidence to support statements about its manifested extent.

Examples may include:

- committed provider snapshot/version exists;
- all expected write units are accounted for under the manifest protocol;
- no unresolved writer owns an active lease/fence for the sealed snapshot;
- required component checksums/digests or provider integrity checks pass;
- manifest/index can be read consistently;
- logical row/cardinality summary can be established where required;
- structural descriptor is internally consistent enough for resolution.

These establish the **physical subject** Generation/Evaluation will reason about. They do not establish semantic validity.

### Quantity semantics remain Generation-owned

A manifest may report exact or estimated row counts/extent. Generation compares that physical extent against its committed exact/min/max/target/tolerance semantics.

Manifest row count therefore remains a physical fact; Generation owns whether the quantity requirement was fulfilled.

### Integrity checks are strength-scoped

Architecture MUST distinguish integrity guarantees from stronger content claims.

For example:

- file checksum validates bytes for that file but not semantic row validity;
- component manifest closure validates membership but not Condition fulfillment;
- provider transaction commit validates provider-level snapshot atomicity but not SYNGAN semantic completion;
- schema compatibility validates structure but not Data Meaning.

## Attempt/writer ownership and fencing boundary

004-D defines the data-plane obligation; detailed operational mechanics are refined in 004-F.

### Stale writer exclusion

A candidate/materialization protocol MUST have a way to prevent a superseded/stale Attempt or writer from silently modifying the candidate snapshot that current Execution/Generation treats as authoritative.

The mechanism may later use:

- leases;
- fencing tokens;
- Attempt epochs;
- unique write namespaces;
- compare-and-set manifest generations;
- transactional table versions;
- another mechanism.

No mechanism is selected here.

### Duplicate physical work is allowed

Retries/speculation MAY create duplicate/recomputed physical material.

The architecture requires only that such work cannot create ambiguous candidate membership or duplicate semantic output authority.

A component from a losing/stale Attempt may be ignored, fenced, garbage-collected, or retained diagnostically according to later implementation policy.

### Seal fencing

Sealing a candidate snapshot must close ordinary mutation under that sealed identity. If a stale writer can still alter the purportedly sealed contents, the manifest identity is not strong enough for required Evaluation or promotion.

## Promotion architecture

### Promotion is a control-plane semantic transition

Generation promotion associates one stable completed-output resource identity with one exact sealed candidate snapshot after Generation's semantic completion prerequisites are satisfied.

Promotion MAY be physically metadata-only. It does not require copying 500 million rows from a staging path to a final path if the underlying representation can be safely retained in place.

Conceptually:

```text
sealed candidate SC17
        +
Generation G17 completion obligations satisfied
        +
required provenance consistency
        ↓
compare/fence authoritative Generation state
        ↓
promote
        ↓
Completed Output O17
  physical basis -> SC17
```

### Promotion preconditions

Before promotion, architecture must be able to establish at least:

1. the candidate is an immutable sealed snapshot;
2. it belongs to the exact committed Generation being completed;
3. its physical extent/integrity is sufficient for the Generation's quantity/scope checks;
4. every mandatory Condition/Constraint/completion obligation has a sufficient basis according to Generation/Evidence semantics;
5. any Evidence consumed for completion binds the exact sealed candidate;
6. required dependency/no-egress facts do not expose a terminal violation;
7. required provenance can be recorded consistently;
8. the Generation has no different already-promoted completed output;
9. the caller/transition operates against the expected current Generation state/version/fence;
10. the completed-output logical identity can be established exactly once/idempotently.

A sealed manifest alone satisfies only a subset of these requirements.

### Single semantic promotion

For one Generation, the promotion operation MUST be idempotent/fenced so retries cannot create two authoritative outputs.

Conceptually:

```text
promote(G17, SC17)
  first successful call -> O17
  retry same intent      -> O17 / already promoted
  attempt promote SC18   -> conflict unless G17 has not yet promoted and owning semantics permit SC18
```

Once G17 is semantically completed with O17, later retries cannot attach O18 to the same Generation as another successful result.

The exact atomic/CAS/transaction mechanism is deferred to 004-F and implementation planning.

### Promotion does not imply external publication

A completed-output promotion means the Generation owns one authoritative synthetic result.

It does not automatically:

- publish the data outside the controlled environment;
- authorize a consumer;
- make the output public;
- mark privacy risk acceptable;
- copy it to another destination;
- approve downstream use.

External release/use remains outside Generation authority.

### Candidate-to-output physical reuse

The promoted output MAY reference the exact sealed candidate snapshot as its physical representation without rewriting/copying the data.

The completed-output resource and candidate snapshot still remain different architectural roles:

```text
SC17 = immutable physical snapshot used as promotion basis
O17  = authoritative logical Generation result
```

O17 references SC17; SC17 does not become semantically final merely by being sealed.

## Completed-output representation architecture

### Logical output identity is independent of layout

One completed output may physically contain:

- one table snapshot;
- many files;
- many partitions;
- multiple component roots;
- provider-managed objects;
- another distributed representation.

The output resource remains one logical identity under the current Generation model.

### Default payload resolution

A completed-output handle resolves its payload through an approved representation binding rooted in the promoted output identity.

Illustratively:

```text
CompletedOutput O17
  -> promoted basis SC17
  -> representation resolver
  -> Spark DataFrame bound to exact snapshot
```

The resulting DataFrame is an access view over O17's representation, not O17's identity.

### Transforming a returned DataFrame

If a caller performs arbitrary Spark transformations on a DataFrame read from O17, the transformed DataFrame is not automatically O17 and does not inherit O17's Provenance/Evidence/completion authority.

SYNGAN may later support explicit derived-data workflows, but ordinary Spark lineage does not mutate or extend the completed-output identity implicitly.

### Replication, relocation, compaction, and reserialization

A completed output may later gain an alternate physical representation while retaining the same logical output identity only when an explicit equivalence/integrity process establishes that the representation preserves the logical output under the required equality semantics.

Examples may include physical compaction, repartitioning, replication, or format migration.

The architecture MUST preserve:

- the original promotion basis;
- the new representation identity/reference;
- the equivalence basis;
- current preferred/available representation where relevant;
- historical provenance of the representation change.

If material logical values/multiplicity/scope change, the result cannot be silently relabeled as another representation of the same completed output.

Exact representation-migration APIs are deferred.

## Source/output identity and reproducibility

### Identity does not require universal content addressing

004-D does not require every enterprise dataset to be fully content-addressed or globally sorted/hashed.

A provider-native immutable version, immutable manifest, snapshot token, or other strong identity mechanism may satisfy historical binding more efficiently than a full row-level digest.

### Logical equality versus physical equality

Physical representation equality and logical dataset equality are distinct.

Repartitioning or compaction may change:

- file names;
- object checksums;
- partition count;
- physical row ordering;

while preserving the same logical tabular content.

Where exact deterministic reproduction requires physical equality, that stronger rule must be stated explicitly. Otherwise semantic/logical reproduction may use a weaker equivalence contract under the [Reproducibility Contract](../authority/reproducibility-contract.md).

### Row ordering

Spark tabular data is generally unordered unless the semantic contract explicitly gives order meaning.

Output identity/reproducibility MUST NOT accidentally depend on incidental Spark partition/file/order behavior unless ordering is part of the committed domain semantics.

## Failure and recovery states

### Materialization failure

A failed or unknown distributed write may leave:

- partial components;
- open manifest state;
- stale Attempt namespaces;
- a sealed snapshot whose semantic validation later fails;
- unknown side-effect state requiring reconciliation.

These remain non-final.

### Unknown state

If architecture cannot determine whether a write/seal/promotion side effect occurred, it MUST preserve unknown/reconciliation-required state rather than infer success from visible files or infer failure from missing coordinator confirmation.

Detailed reconciliation belongs to 004-F.

### Quarantine

Failed/cancelled/ineligible candidate material may be retained under explicit quarantine/diagnostic semantics.

Quarantined material is not returned by normal completed-output resolution and must not be relabeled final through a path rename or catalog alias alone.

## Security, access, and no-egress boundary

004-D reserves hooks needed by 004-H without selecting an authorization engine.

Data references/manifests may expose sensitive locators, storage topology, source identities, or output content. Resolution therefore must be authorization-aware.

A resolver MUST NOT silently copy/materialize/replicate data to an unapproved location merely because the preferred representation is unavailable.

Source snapshotting or output promotion cannot become a hidden egress mechanism.

`withheld`, `unavailable`, `unknown`, and `absent` reference-resolution outcomes remain distinct according to 004-C/003-H.

## Platform adapter obligations

Concrete Spark/storage/catalog adapters must implement the common contracts without redefining them.

An adapter may exploit provider capabilities such as:

- snapshot/version reads;
- atomic table commits;
- object immutability/versioning;
- catalog aliases/views;
- optimized manifest generation;
- partition pruning;
- transaction logs;
- checksums;
- table cloning/snapshotting;
- platform-native access controls.

But an adapter MUST NOT claim a stronger SYNGAN guarantee than the provider capability actually supplies.

Examples:

- a table commit is not Generation completion;
- a Delta/iceberg/provider version is useful historical identity only according to its actual retention/read guarantees;
- a renamed staging path is not semantic promotion;
- an object-store prefix listing is not immutable identity if objects can change;
- a DataFrame can represent a promoted output for reading but cannot replace the output resource identity.

No specific provider is mandatory.

## Enterprise-scale manifest rules

The architecture MUST remain practical for hundreds of millions of rows and large distributed representations.

Therefore:

- manifest creation/integrity checks may be distributed;
- the control-plane root SHOULD remain bounded;
- component detail MAY be stored in a distributed manifest/index;
- full component/file lists need not be loaded into the driver to establish identity;
- counts/digests/checks may be reduced distributively;
- default inspection should use summaries and stable references;
- exact source/output resolution must not require full payload transfer to the control plane;
- a platform-native snapshot token may replace explicit per-file enumeration where its guarantee is sufficient.

## Anti-god-object rules

004-D MUST NOT create a universal `Dataset`, `Artifact`, `Manifest`, `DataRef`, or `StorageObject` semantic owner that absorbs:

- Data Meaning;
- source semantics;
- Generation Conditions;
- Constraint satisfaction;
- Evidence;
- Learned State;
- Execution;
- Provenance;
- authorization;
- release approval.

Shared low-level reference/manifest infrastructure is acceptable only when the semantic role remains typed by its owning workflow/resource.

## Architecture invariants

1. A Spark DataFrame MUST remain an access representation rather than durable semantic identity.
2. Committed work that depends materially on source data MUST bind a stable source-state reference strong enough to identify/read the intended source state.
3. Mutable table/path/query aliases MUST NOT silently substitute for exact historical source state.
4. Source snapshotting/manifesting MUST remain distributed and MUST NOT require full driver collection.
5. Physical structural schema MUST remain distinct from Data Meaning authority.
6. A manifest is a representation mechanism and MUST NOT become a generic domain concept or metadata god-object.
7. Enterprise manifests MAY use bounded roots plus distributed component indexes/provider snapshots rather than control-plane per-file enumeration.
8. A candidate must become an immutable sealed snapshot before required Evaluation/promotion relies on its exact contents.
9. Sealing a candidate MUST NOT imply semantic Generation completion.
10. Evidence used for Generation completion MUST bind the exact sealed candidate it evaluated.
11. Candidate/open/quarantined material MUST remain excluded from normal completed-output discovery.
12. Stale/superseded writers MUST NOT be able to mutate the sealed/current candidate invisibly.
13. Duplicate physical computation/writes MAY occur but MUST NOT create ambiguous candidate membership or multiple authoritative outputs.
14. Generation promotion MUST be idempotent/fenced and produce at most one completed-output identity.
15. Promotion MAY reuse candidate physical bytes in place; semantic promotion does not require row copying.
16. Completed output identity MUST remain distinct from files, table names, Spark DataFrames, and other physical representations.
17. Physical relocation/compaction/replication preserves output identity only when explicit equivalence/integrity semantics establish the same logical content.
18. Arbitrary downstream Spark transformations MUST NOT inherit completed-output identity automatically.
19. Output/source identity MUST NOT depend on incidental physical row order unless ordering is semantically material.
20. Data reference resolution MUST preserve exact/withheld/unavailable/unknown/invalid-reference distinctions and MUST NOT silently retarget history.
21. Platform-native snapshot/transaction guarantees MAY be used but MUST NOT be overstated as SYNGAN semantic guarantees.
22. Source snapshotting/output promotion MUST NOT introduce hidden network acquisition, egress, or unapproved replication.
23. Canonical control-plane state MUST remain bounded by logical references/manifests/summaries rather than source/output row or file count by default.
24. No 004-D rule may introduce a permanent single-table invariant.

## Deferred decisions

004-D intentionally does not select:

- Delta Lake, Iceberg, Hudi, Parquet, object-store layout, or another storage format;
- Unity Catalog or another catalog as universal authority;
- exact source snapshot/fingerprint algorithm;
- hash/checksum algorithm;
- manifest serialization format;
- whether component manifests use files, tables, trees, logs, or provider metadata;
- exact staging/final namespace convention;
- transaction/CAS/fencing implementation;
- garbage-collection/retention period;
- output compaction/repartitioning mechanism;
- source snapshot materialization policy defaults;
- relational/multi-table semantic model;
- exact Spark DataFrame public method names;
- authorization/credential/storage-policy implementation.

These decisions remain constrained by this architecture and are refined in 004-E through 004-I and Phase 005 implementation planning.

## Consequences for later Phase 004 groups

### 004-E

Strategy runtimes must consume resolved source/Learned-State references and write through candidate materialization contracts rather than inventing runtime-specific final-output identity.

### 004-F

Execution architecture must define Attempt epochs/fencing, writer ownership, retry/resume reconciliation, seal/promotion idempotency, and unknown side-effect recovery against this manifest/materialization model.

### 004-G

Evaluation/Evidence architecture must bind sealed candidate/output identities and Provenance must reference manifests/results without copying data-plane payloads.

### 004-H

Dependency/security architecture must authorize reference resolution, snapshot/materialization destinations, data movement, withheld locator disclosure, and no-egress enforcement.

### 004-I

Platform integration architecture must map Spark/storage/catalog provider capabilities to these snapshot/manifest/promotion contracts and expose capability limitations explicitly.
