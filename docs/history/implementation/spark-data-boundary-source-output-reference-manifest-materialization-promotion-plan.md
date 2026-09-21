---
type: Implementation Authority
title: Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan
status: active
---

# Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan

## Purpose

Define the concrete **future implementation plan** for SYNGAN's distributed Spark data boundary: source selection and exact source-state binding, Spark DataFrame access, distributed snapshot/materialization references, candidate lifecycle, sealed snapshot/manifest representation, completed-output representation binding, and Generation promotion coordination.

This document is the canonical Phase 005-E implementation-planning authority.

**Phase 005 remains planning-only.** This document specifies future source/package responsibilities, interfaces, persistence representations, sequencing, and verification obligations. It does **not** create `pyproject.toml`, production source, tests, Spark jobs, manifests, storage paths, migrations, CI workflows, or platform configuration.

## Governing authority

005-E is downstream of:

- [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md);
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md);
- [Public Resource API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../architecture/public-api-resource-handle-workflow-semantic-mapping.md);
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../architecture/control-plane-identity-revision-state-persistence-historical-reference.md);
- [005-B Verification Strategy](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [005-C Source Topology](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md);
- [005-D Public Resource/Control-Plane Plan](public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md).

The governing implementation-planning rule is:

> **Spark DataFrames and physical storage are access/realization mechanisms. Every committed source and completed Generation result must remain anchored to the durable identity, exact-state, CAS, historical-resolution, and promotion model established by 005-D.**

## Planning-only boundary

005-E SHALL NOT be interpreted as authorization to begin production implementation.

During Phase 005, repository changes remain limited to planning/governance/documentation artifacts unless a later explicit phase formally authorizes coding.

Names below such as `SourceStateRef`, `CandidateMaterializationRef`, and `SparkDataAccess` identify accepted future implementation roles and intended public/internal spelling. They are not classes currently present in the repository.

## Accepted implementation choices

005-E accepts the following future implementation baseline:

- PySpark remains an **optional** capability, isolated behind the published `spark` extra and Spark-specific adapter packages;
- the base `syngan` package remains importable without PySpark;
- arbitrary Spark DataFrames, SQL queries, mutable paths, and mutable table/catalog aliases are selectors/access objects, never durable historical identity;
- arbitrary DataFrame/query selectors default to distributed snapshot materialization before commitment unless an adapter can prove an exact stable read binding;
- provider-native immutable/versioned snapshots may be referenced without physical copy when their exact reread/retention guarantees satisfy the contract;
- a portable manifested-file profile is planned around Spark-readable Parquet data under unique materialization namespaces plus a bounded sealed manifest root and distributed/hierarchical component index;
- no table format (Delta Lake, Apache Iceberg, Apache Hudi, or other) becomes universal SYNGAN semantics;
- provider/table-format adapters may exploit stronger native snapshot/transaction capabilities when they satisfy the common conformance contract;
- open candidate materialization, sealed candidate snapshot, and logical completed Generation output remain distinct typed roles;
- a sealed candidate snapshot is immutable under its identity and is the exact subject required for Generation-completion Evaluation;
- Generation promotion is a 005-D control-plane transition binding one logical output to one exact sealed snapshot; it may be metadata-only and must not require a second full row copy;
- candidate/output data remains distributed; control persistence stores only bounded identities, descriptors, state, and manifest roots/summaries;
- writer fencing is a required port seam but its Attempt-epoch mechanics remain owned by 005-G;
- authorization/no-egress checks are required seams but enforcement policy remains owned by 005-I.

## Dependency/package consequences

005-E reserves capability packaging equivalent to:

```text
published optional extra: spark
repository group: spark-test
repository group: spark-integration
```

The intended future boundary is:

```text
syngan base
    no pyspark dependency/import requirement

syngan[spark]
    PySpark-backed selectors/access/materialization adapters

provider/table-format extras
    introduced only by their owning adapter/platform plan
    and never implied by syngan[spark]
```

The `spark` extra SHOULD contain only the dependencies genuinely required for the generic Spark adapter boundary. A Databricks SDK, Delta/Iceberg/Hudi client, cloud SDK, remote catalog client, or similar provider dependency MUST NOT enter `spark` merely because one integration can use it.

Exact PySpark version constraints belong to the implementation support matrix finalized by 005-J and locked when implementation begins.

## Future package ownership

005-E refines the 005-C topology with future responsibilities equivalent to:

```text
src/syngan/
├── ports/
│   └── data/
│       ├── references.py
│       ├── descriptors.py
│       ├── source.py
│       ├── snapshots.py
│       ├── candidates.py
│       └── representations.py
├── application/
│   └── data/
│       ├── source_resolution.py
│       ├── snapshot_preparation.py
│       ├── candidate_materialization.py
│       └── promotion.py
├── api/
│   └── data.py
└── adapters/
    ├── persistence/
    │   └── sql/
    │       └── data_plane_records/
    └── spark/
        ├── selectors.py
        ├── access.py
        ├── readers.py
        ├── writers.py
        ├── manifest.py
        └── providers/
            └── parquet_manifest/
```

Exact leaf-file spelling may be refined during the later coding phase, but ownership and dependency direction must remain equivalent.

`syngan.domain` does not gain a generic Dataset/Artifact/Manifest concept merely because the data plane needs technical representation types.

## Data-reference roles

005-E introduces typed future implementation roles beneath 005-D's `ResourceRef` model.

### Additional `ResourceKind` values

The following infrastructure kinds are reserved:

```text
source_state
generation_candidate
data_snapshot
```

They are representation/resource kinds, not additions to the accepted concept catalog.

`generation_output` remains the logical promoted Generation result kind accepted by 005-D.

### `SourceStateRef`

A `SourceStateRef` is the durable exact-state binding used by committed Learning, direct Generation, or Evaluation.

Conceptually:

```text
SourceStateRef
    resource: ResourceRef(kind=source_state)
    representation: DataRepresentationDescriptor
    exact_read_binding: SnapshotReadBinding
    identity_basis: IdentityBasis
    structural_descriptor: StructuralDescriptor
```

The local `ResourceRef` provides SYNGAN historical identity. The representation descriptor may point to an external/provider-native versioned snapshot or to a SYNGAN-materialized manifested snapshot.

### `CandidateMaterializationRef`

A `CandidateMaterializationRef` identifies one non-final physical Generation materialization workspace/state.

It wraps:

```text
ResourceRef(kind=generation_candidate)
parent Generation ResourceRef
current materialization state + StateVersion
provider/materialization descriptor
```

It is not accepted where a completed output is required.

### `SealedDataSnapshotRef`

A `SealedDataSnapshotRef` identifies an immutable physical data snapshot:

```text
ResourceRef(kind=data_snapshot)
owner/parent reference
bounded ManifestRootDescriptor
```

For Generation, the sealed snapshot is produced from one candidate materialization and becomes the exact subject for required Evaluation.

### Completed output representation binding

A logical `GenerationOutputHandle`/`generation_output` resource remains separate from physical representation.

The future control model is equivalent to:

```text
GenerationOutput O17
    representation_binding
        -> SealedDataSnapshotRef SC17
```

The same sealed physical bytes may back O17 after promotion. Promotion does not require a row-for-row copy.

## Source selector model

Selectors are proposed access instructions, not historical identity.

Spark-specific future selector roles include equivalents of:

- `SparkDataFrameSelector` — ephemeral DataFrame access object;
- `SparkTableSelector` — table/catalog identifier plus explicit read options/version hints;
- `SparkPathSelector` — path/URI plus format/read options;
- `SparkQuerySelector` — SQL/logical query plus required catalog/session context;
- an already-resolved `SourceStateRef` for callers that possess exact state.

### Selector durability rule

`SparkDataFrameSelector` is intentionally non-serializable as a durable reference. It may carry/process a live DataFrame during preparation, but a committed activity snapshot cannot contain that Python DataFrame object.

A mutable table/path/query selector may be serialized for preparation/audit convenience, but it cannot appear as the sole committed source identity.

### Conservative resolution rule

The default future resolution policy is:

```text
already exact SourceStateRef
    -> validate/resuse exact state

provider-native exact snapshot available
    -> bind exact provider snapshot without copy

arbitrary DataFrame/query/mutable locator
    -> materialize/pin distributed snapshot before commitment
       unless provider adapter proves exact stable read binding
```

This means an arbitrary Spark logical plan is not presumed historically stable merely because Spark can execute it again.

## Source-state resolution pipeline

The future application flow is equivalent to:

```text
source selector
      ↓
inspect provider/capabilities
      ↓
resolve exact native snapshot
OR
plan explicit distributed snapshot materialization
      ↓
validate identity/read/integrity strength
      ↓
create/resolve SourceStateRef
      ↓
commitment may bind SourceStateRef
```

Source snapshot preparation remains a technical data-reference operation, not Learning, Generation, or Evaluation.

If pre-commit snapshot preparation requires long-running external work, it may use technical platform correlation/telemetry; it MUST NOT fabricate a committed domain activity. A durable user-facing orchestration model for such preparation is deferred unless later implementation work demonstrates it is necessary.

## Source identity/read-binding strength

Future descriptors must distinguish how exact-state identity is established.

`IdentityBasis` values are planned equivalent to:

```text
provider_snapshot
manifested_snapshot
content_digest
external_authoritative_snapshot
```

A source can combine bases.

The descriptor must also preserve the guarantee strength separately from locator text.

Examples that remain invalid proof by themselves:

```text
schema hash
row count
sample fingerprint
mutable path listing
table + wall-clock timestamp
```

### Read binding

A source-state record must include enough provider/read information for a runtime adapter to read the exact bound state.

For a provider-native table this may be an immutable snapshot/version token.

For a manifested file snapshot it may be the sealed root/component index plus immutable object/version identities.

If the provider cannot actually reread the historical state it claims to identify, readiness must surface that limitation rather than overstate reproducibility.

## Structural descriptor

A `StructuralDescriptor` captures only physical/read requirements such as:

- column/field names;
- Spark/storage physical types;
- nullability;
- nested structure;
- format/provider kind;
- partitioning/bucketing/read hints where required.

It is explicitly not Data Meaning.

Structural compatibility may support readiness checks but never replaces semantic interpretation.

## Manifest representation

### Bounded root

A future `ManifestRootDescriptor` is a frozen, versioned control-plane value equivalent to:

```text
ManifestRootDescriptor
    schema_version
    snapshot_ref
    provider_kind
    representation_kind
    physical_root / provider_snapshot token
    component_index_ref? 
    structural_descriptor
    extent_summary
    identity_basis
    integrity_descriptor
    created_at / sealed_at
```

The root remains bounded in size.

### Component index

Large file/component membership lives outside ordinary canonical SQL rows.

The component index may be:

- a provider-native snapshot index/transaction log;
- a hierarchical manifest tree;
- a partitioned Spark-readable manifest dataset;
- another provider-specific distributed structure satisfying the same contract.

The SQL/control store retains only the root descriptor/reference and bounded summary.

### No control-plane file enumeration requirement

The future implementation MUST NOT require loading millions of component paths into the SQL control store or one driver list merely to establish snapshot identity.

Provider/manifests must support bounded roots and distributed/hierarchical detail.

## Portable Parquet manifest profile

005-E selects a **portable manifested-Parquet profile** as the first provider-neutral file representation to plan, without making Parquet a semantic requirement.

The profile is equivalent to:

```text
unique materialization namespace
    ↓
Spark-written Parquet components
    ↓
distributed/hierarchical component index
    ↓
bounded sealed manifest root
```

Key rules:

- each source snapshot/candidate uses a unique immutable namespace or provider-versioned namespace;
- sealing does not depend on directory rename being atomic;
- the manifest, not mutable path listing, defines membership/identity;
- component integrity uses only guarantees the storage provider can actually establish;
- object/file version IDs, checksums, ETags, sizes, or digests are recorded only with their true declared strength;
- if storage cannot prevent or detect mutation strongly enough for the requested guarantee, readiness reports limitation/incompatibility rather than claiming an immutable snapshot;
- Parquet's physical schema remains structural representation, not Data Meaning.

A provider-native table adapter may supersede this physical mechanism for one deployment while still satisfying the same `SourceStateRef`/sealed-snapshot contract.

## Provider capability contract

Every future data provider adapter must declare capabilities equivalent to:

```text
exact historical snapshot resolution
exact historical reread
snapshot retention semantics
provider-side atomic snapshot commit
immutable/versioned object support
distributed component index support
candidate isolation
seal/immutability support
writer-fence support seam
metadata-only promotion support
representation-equivalence support
exact/estimated extent support
integrity basis/strength
```

Capability claims are evidence inputs to readiness/compatibility; provider brand names are not guarantees.

A table-format/platform adapter that lacks a required property must use a semantics-preserving fallback or report limitation/incompatibility.

## Spark DataFrame access boundary

PySpark `DataFrame` appears only in Spark-specific optional adapter/runtime interfaces.

Core `foundation`, `domain`, `ports`, `application`, and base `api` modules do not import `pyspark.sql.DataFrame`.

Future Spark access is equivalent to:

```text
SourceStateRef / SealedDataSnapshotRef
       ↓
SparkDataAccess + configured SparkSession
       ↓
DataFrame
```

and:

```text
live DataFrame
       ↓
SparkDataFrameSelector
       ↓
source-resolution/snapshot preparation
       ↓
SourceStateRef
```

`SparkDataAccess` is an adapter service, not a durable handle.

Arbitrary downstream operations such as `df.filter(...)` produce a new Spark view/plan and do not inherit SYNGAN output identity automatically.

## Candidate materialization control model

The future SQL/control state for a Generation candidate remains bounded and uses 005-D CAS.

A physical lifecycle equivalent to the following is planned:

```text
allocated
    ↓
materializing
    ↓
sealed

or

quarantined / abandoned
```

`promoted` may be recorded as representation association after Generation output promotion, but does not replace Generation's semantic lifecycle.

Candidate current state carries a `StateVersion` and exact parent Generation reference.

### Candidate write target

A future adapter receives a bounded `CandidateWriteTarget` containing only what it needs, such as:

- candidate ResourceRef;
- approved provider/physical namespace;
- structural/write descriptor;
- expected materialization generation/state;
- opaque writer-authority/fence input supplied by 005-G;
- security/no-egress capability context supplied by 005-I.

The runtime adapter does not receive direct permission to mark Generation complete.

### Attempt/writer fencing seam

005-E requires every write/seal mutation interface to accept and validate an execution-authority/fence input.

The concrete Attempt epoch/fencing token semantics are intentionally deferred to 005-G.

The data API MUST NOT be designed so this parameter can later be added only by breaking every provider implementation.

## Sealing protocol

Sealing is a conditional physical-state transition, not semantic completion.

Future seal logic must establish, to the provider's declared strength:

1. candidate ownership matches the exact Generation;
2. caller has current writer/seal authority;
3. candidate state/version permits sealing;
4. no unresolved authoritative writer can mutate the sealed membership;
5. component/index closure succeeds;
6. structural descriptor is coherent;
7. required physical integrity/accounting checks succeed;
8. immutable `SealedDataSnapshotRef` and manifest root are established;
9. repeated seal request for the same exact candidate generation is idempotent;
10. a materially different post-seal write requires a new candidate/snapshot identity.

A sealed candidate is then suitable as an exact Evaluation subject. It is not yet a completed output.

## Physical completeness and extent

`ExtentSummary` may include bounded facts such as:

- exact/estimated row count;
- component count;
- byte-size summary;
- partition summary;
- coverage/accounting completeness;
- count/estimate method.

The descriptor must say whether a fact is exact, provider-reported, approximate, or unknown.

Generation—not the manifest—decides whether that physical extent satisfies committed quantity semantics.

## Generation promotion plan

### Promotion precondition inputs

The future promotion application service consumes exact references/facts including:

- Generation ResourceRef and expected Generation `StateVersion`;
- CandidateMaterializationRef;
- exact `SealedDataSnapshotRef`;
- physical integrity/closure status;
- completion-obligation/Evidence basis supplied by 005-H;
- required dependency/security completion facts from later slices;
- operation-scoped idempotency identity;
- required Provenance/outbox intents.

005-E does not implement Evidence semantics early; it defines the required input seam so 005-H can supply exact Evidence bindings later.

### Atomic control transition

Using 005-D's transaction/CAS model, future promotion is planned to atomically establish the control-plane facts equivalent to:

```text
validate Generation expected state
validate sealed snapshot belongs to the Generation candidate
verify no output already exists
create generation_output ResourceId
bind output representation -> exact sealed snapshot
update Generation semantic state/result association
append material transition
record required outbox/provenance intents
commit
```

The unique semantic slot is one completed output per Generation.

Repeated promotion with the same exact Generation/snapshot is idempotent and resolves to the established output.

Attempting to promote a different snapshot after the Generation already has a completed output is a conflict, not a second output.

### Promotion does not copy rows

Promotion may be metadata/control-plane only.

The `GenerationOutput` resource and sealed physical snapshot remain distinct roles even when they reference the same physical bytes.

## Output representation and payload access

The future `GenerationOutputHandle` resolves to:

```text
logical output identity
producing Generation
current availability/lifecycle facts
representation binding -> SealedDataSnapshotRef
```

A Spark-specific payload access service may resolve that representation to a DataFrame.

The DataFrame is a current access view, not the Output identity.

### Representation evolution

Relocation, compaction, repartitioning, format conversion, or replication may preserve the same logical Output only through an explicit representation-equivalence decision.

The future implementation must record:

- old and new representation refs;
- equivalence basis/strength;
- transition/history;
- retention/availability effect.

If logical row values, multiplicity, or scope materially change, a new physical representation cannot simply be relabeled as the same Output.

Detailed historical/Provenance recording is finalized by 005-H.

## Control-store persistence additions

005-E plans new owner/technical SQL records under the 005-D adapter, equivalent to:

```text
source_state
candidate_materialization
data_snapshot
output_representation_binding
```

These tables/records contain bounded control facts only.

They do not store Spark rows, Parquet bytes, file lists at enterprise scale, or full manifest component detail.

All use 005-D ResourceRef/SchemaVersion/StateVersion/transaction conventions.

The actual Alembic migration is created only when the later implementation phase begins.

## Historical resolution

`SourceStateRef`, `SealedDataSnapshotRef`, and output representation bindings participate in 005-D exact historical resolution.

A historical read must not silently replace:

```text
source table version V12 -> current V19
sealed candidate SC17 -> newer SC18
output representation R1 -> latest mutable path contents
```

Known expired payload remains `unavailable`, not `absent`.

Security-aware `withheld` behavior is integrated later by 005-I without changing the underlying identities.

## No hidden egress or storage relocation

Source snapshotting/materialization is a physical copy operation when it actually copies data.

Therefore the future application must expose the target storage/security domain to 005-I authorization/no-egress evaluation before materialization begins.

005-E does not assume:

```text
snapshotting is internal
therefore egress-safe
```

A provider-native version binding that performs no copy remains distinct from a snapshot materialization that moves rows into another location.

## Verification mapping

005-E owns the future implementation of major V5 verification and contributes to V2/V3/V7/V10/V11.

Primary architecture-fitness mapping:

- **AF-03** — DataFrame/path/table/platform snapshot IDs cannot replace canonical refs;
- **AF-04** — candidate/sealed snapshot cannot satisfy completed-output contracts;
- **AF-08** — sealing and Generation promotion are idempotent;
- **AF-13** — supported enterprise paths do not require full driver collection;
- **AF-17** — exact source/snapshot refs do not silently resolve current aliases;
- **AF-07** seam — stale writer fencing is mandatory, concretely exercised after 005-G defines Attempt epochs;
- **AF-12/AF-14** — provider resolution/fallback must not hide network behavior or weaken semantics.

Required future scenario families include:

1. mutable table alias resolves to exact provider snapshot and continues reading that version after alias advances;
2. arbitrary DataFrame selector cannot be committed until resolved/materialized to exact source state;
3. query selector with unstable inputs defaults to snapshot materialization rather than replay-as-history;
4. manifested file source retains bounded root while component index remains distributed;
5. open candidate is not discoverable as completed output;
6. candidate sealing produces immutable SC1; later writes cannot mutate SC1;
7. SC1 and SC2 remain distinguishable and completion validation for SC1 cannot silently apply to SC2;
8. repeated same seal is idempotent;
9. repeated same promotion returns the one output;
10. competing different promotion after output exists is rejected;
11. promotion reuses sealed bytes without requiring copy;
12. arbitrary Spark transform of a completed-output DataFrame does not inherit Output identity;
13. exact historical source/snapshot resolution returns unavailable/invalid rather than latest fallback;
14. portable Parquet manifest profile works without collecting all rows/components into the driver;
15. provider capability fallback either preserves semantics or reports limitation/incompatibility.

### Full-driver-collection fitness

Future AF-13 enforcement should combine:

- targeted static checks for `collect`, `toPandas`, large `toLocalIterator`/equivalent calls in enterprise coordination paths;
- behavior tests using generated data large enough to expose accidental driver assumptions;
- bounded-memory/driver observations in integration/scale profiles;
- explicit allowlisting for genuinely bounded samples/summaries with rationale.

A blanket ban on all `collect()` anywhere is not required; the protected property is absence of mandatory full-corpus driver materialization in supported enterprise paths.

## Test profiles

Future verification profiles are planned as:

```text
Q1 / spark-contract
    bounded local Spark contract tests
    selector/ref/type separation
    package extra isolation

Q2 / spark-manifest
    real filesystem/object-store-like materialization
    candidate seal/promote contracts
    provider conformance

Q3 / spark-compatibility
    selected Spark/provider/version matrix
    failure/recovery seams

Q4 / spark-scale-certification
    explicit scale/workload/environment profiles
```

Local Spark tests do not prove production object-store/table-format semantics by themselves.

## Future implementation sequence

When a later coding phase explicitly begins, 005-E should be implemented in dependency order equivalent to:

```text
E1  data reference/descriptor value contracts + codecs
E2  source selector/resolution ports and application service
E3  source-state/candidate/snapshot SQL control records
E4  Spark selector/access adapter and local exact-read contracts
E5  portable manifested-Parquet snapshot/candidate provider
E6  sealing + exact snapshot subject boundary
E7  Generation output representation/promotion transaction
E8  provider conformance + Q1/Q2 Spark verification
E9  provider-native table-format/platform adapters as separately owned capabilities
```

This sequence is **future implementation guidance only**. None of E1-E9 is executed during Phase 005.

## Deferred implementation decisions

005-E intentionally leaves the following to their owning later planning/implementation work:

- exact supported PySpark/Spark versions and JDK matrix — 005-J;
- Delta/Iceberg/Hudi/provider-specific adapters and Databricks mapping — 005-J or provider-specific later work;
- concrete Attempt epoch/fence token and stale-writer mechanism — 005-G;
- checkpoint/recovery interaction with candidate namespaces — 005-G;
- exact Evaluation/Evidence completion-basis types — 005-H;
- Provenance assertions for representation changes/promotion — 005-H;
- authorization, credentials, object-store permissions, encryption, no-egress enforcement — 005-I;
- cloud filesystem SDKs/catalog clients — optional provider/platform ownership only;
- garbage collection/retention periods and cleanup orchestration — 005-J/005-K;
- future multi-table/relational structured synthesis representation — explicit later extension, with 005-E avoiding a permanent one-table invariant.

## Rejected alternatives

005-E rejects as future implementation baseline:

- DataFrame object as source/output identity;
- table/path/query string as sufficient historical identity when mutable;
- replaying arbitrary DataFrame/query plans as if that proved exact historical source binding;
- one generic `ArtifactRef` for source/candidate/output/diagnostic roles;
- file/path existence as Generation completion;
- mutable candidate being evaluated as required completion subject;
- copy-on-promotion as a universal requirement;
- exactly-once physical Spark work as a semantic requirement;
- one SQL row per physical file as mandatory manifest architecture;
- full-corpus content hashing as universal identity requirement;
- Delta/Iceberg/Hudi/Databricks as universal SYNGAN semantics;
- adding PySpark to the base portable-core dependency set;
- storing full manifest/file membership in the bounded control database;
- silently snapshotting/copying data into a different security domain.

## No upstream revision required

005-E finds no planning requirement that changes the eleven accepted concepts, fifteen synchronizations, Phase 003 experience contract, Phase 004 architecture, ADR-0001 through ADR-0008, 005-C dependency direction, or 005-D durable identity/state model.

No new architecture ADR is required because the plan selects downstream realization boundaries within the accepted architecture.

## Exit criteria

- [x] Phase 005 planning-only boundary explicitly preserved;
- [x] Spark remains optional and isolated from base core;
- [x] durable source/candidate/sealed-snapshot roles mapped onto 005-D ResourceRef;
- [x] conservative DataFrame/query/mutable-locator resolution policy defined;
- [x] structural descriptor separated from Data Meaning;
- [x] bounded manifest-root/distributed component-index model defined;
- [x] portable manifested-Parquet profile selected as first provider-neutral file plan;
- [x] provider capability/conformance contract defined;
- [x] candidate lifecycle and future writer-fencing seam defined;
- [x] sealing semantics and exact Evaluation-subject boundary defined;
- [x] metadata-only/idempotent single-output promotion plan defined;
- [x] output logical identity remains separate from physical Spark representation;
- [x] control-store persistence additions and exact historical resolution mapped;
- [x] no-egress/security hooks preserved for 005-I;
- [x] V5/AF verification obligations mapped;
- [x] future E1-E9 implementation order defined without executing it.

## Exit decision

**005-E — implementation plan complete; no production implementation performed.**

Next:

**005-F — Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan**.
