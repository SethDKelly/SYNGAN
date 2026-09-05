---
type: Phase Record
title: 005-E — Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan
status: complete
---

# 005-E — Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan

## Objective

Translate the accepted Phase 004-D distributed-data architecture and 005-D durable control substrate into a concrete **future implementation plan** for Spark selectors/access, exact source-state binding, manifests, Generation candidates, sealed snapshots, output representation, and promotion.

**No production implementation is authorized or performed by this phase.** Phase 005 remains implementation planning and delivery decomposition.

## Entry authority

005-E is downstream of:

- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md);
- [005-B Verification Strategy](../../implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [005-C Source Topology](../../implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md);
- [005-D Public Resource/Control-Plane Plan](../../implementation/public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md).

## Canonical authority created

005-E establishes:

[ Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan](../../implementation/spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md).

## Planning-only clarification

005-E explicitly records that Phase 005 does not create production code, package scaffolding, migrations, Spark jobs, tests, manifests, storage layouts, or CI workflows.

Names and package paths accepted here are future implementation responsibilities and intended interfaces only.

## Core data-boundary decisions

Accepted future implementation rules include:

- PySpark remains optional behind the `spark` capability extra;
- the base package remains importable without PySpark;
- Spark DataFrames, table names, paths and queries are selectors/access objects, not durable historical identity;
- exact committed source state is represented through durable 005-D `ResourceRef`-based `SourceStateRef` values;
- arbitrary DataFrame/query/mutable-locator inputs default to distributed snapshot materialization before commitment unless an adapter proves an exact stable native read binding;
- provider-native immutable/versioned snapshots may be referenced without copying when their guarantees satisfy the common contract;
- structural Spark/storage schema remains distinct from Data Meaning;
- one bounded manifest root references provider-native or distributed/hierarchical component detail;
- the control database never requires one canonical row per file/component;
- a portable manifested-Parquet profile is the first provider-neutral file representation planned;
- no Delta/Iceberg/Hudi/Databricks table format becomes universal semantics;
- Generation candidate materialization, sealed data snapshot and logical completed output are distinct typed roles;
- required Generation-completion Evaluation binds the exact sealed snapshot;
- sealing is physical identity/integrity closure, not Generation completion;
- promotion is an idempotent 005-D control-plane transition and may reuse the sealed candidate bytes without copy;
- writer-fencing and security/no-egress capability inputs are required seams, concretely defined by 005-G/005-I.

## Resource/reference roles

005-E reserves representation `ResourceKind` roles equivalent to:

```text
source_state
generation_candidate
data_snapshot
```

The accepted future reference roles are:

```text
SourceStateRef
CandidateMaterializationRef
SealedDataSnapshotRef
GenerationOutput -> representation binding -> SealedDataSnapshotRef
```

These are architecture/implementation representation roles, not new domain concepts.

## Source selector plan

Spark-specific future selectors include equivalents of:

```text
SparkDataFrameSelector
SparkTableSelector
SparkPathSelector
SparkQuerySelector
```

plus already-resolved `SourceStateRef`.

A live DataFrame is intentionally non-durable and cannot be stored in a committed activity snapshot.

The conservative source-resolution order is:

```text
exact SourceStateRef
    -> validate/reuse

provider-native exact snapshot
    -> exact no-copy binding

otherwise
    -> explicit distributed snapshot preparation
```

Snapshot preparation remains technical pre-commit work and does not fabricate Learning/Generation/Evaluation.

## Manifest plan

Future sealed data snapshots use a bounded `ManifestRootDescriptor` containing only control-scale facts and a reference to distributed/provider-native membership detail.

Component detail may be represented by:

- provider transaction/snapshot metadata;
- hierarchical manifest tree;
- partitioned Spark-readable component-index dataset;
- another conforming provider representation.

Full component membership must not be copied into bounded SQL control rows or a mandatory driver-local list.

## Portable Parquet profile

The first generic file-oriented plan is:

```text
unique materialization namespace
        ↓
Spark-written Parquet components
        ↓
distributed/hierarchical component index
        ↓
bounded sealed manifest root
```

The plan does not depend on atomic directory rename and does not treat path listing as identity.

Storage-specific checksums/version IDs/digests are recorded only to the strength they actually provide.

## Candidate and sealing plan

Candidate control state remains subordinate to Generation with a physical lifecycle equivalent to:

```text
allocated -> materializing -> sealed
                 ↘ quarantined / abandoned
```

It uses 005-D `StateVersion` CAS.

Every future write/seal API must accept an execution writer-authority/fence input so 005-G can add Attempt-epoch semantics without redesigning the data port.

Sealing establishes an immutable `SealedDataSnapshotRef` and exact physical subject; it does not establish Condition/Constraint fulfillment, privacy, release approval or Generation completion.

## Promotion plan

Future Generation promotion uses 005-D's transaction/CAS/idempotency/outbox substrate to establish:

```text
Generation + expected StateVersion
+ exact Candidate
+ exact SealedDataSnapshotRef
+ completion/Evidence basis
+ required security/dependency facts
        ↓
one GenerationOutput ResourceId
+ representation binding to the sealed snapshot
```

Repeated promotion for the same exact subject resolves idempotently to the same logical output.

A different snapshot after successful promotion is a conflict, not a second completed output.

Promotion may be metadata-only and must not require another full distributed copy.

## Output access plan

A `GenerationOutputHandle` remains logical control authority. Spark payload access is an optional adapter operation:

```text
GenerationOutputHandle
      ↓ representation binding
SealedDataSnapshotRef
      ↓ SparkDataAccess
DataFrame
```

The returned DataFrame does not become or inherit the output identity, and arbitrary downstream transformations do not automatically inherit that identity.

## Persistence impact plan

Future SQL control records are equivalent to:

```text
source_state
candidate_materialization
data_snapshot
output_representation_binding
```

These contain bounded control state only and reuse 005-D ResourceRef/StateVersion/SchemaVersion/transaction conventions.

No migration is created during Phase 005.

## Package/dependency plan

005-E reserves:

```text
published extra: spark
repository groups: spark-test, spark-integration
```

`syngan[spark]` does not imply Databricks, Delta/Iceberg/Hudi, cloud SDKs, or remote catalog clients.

Provider-specific dependencies remain isolated and owned by later provider/platform planning.

## Verification mapping

005-E maps future implementation primarily to V5 and the following fitness obligations:

```text
AF-03  canonical refs are not DataFrame/path/provider IDs
AF-04  candidate/snapshot != completed output
AF-08  seal/promotion idempotency
AF-13  no mandatory full-driver materialization
AF-17  exact historical refs never substitute latest aliases
AF-07  mandatory stale-writer-fence seam, completed by 005-G
AF-12/14 no hidden network/fallback and semantics-preserving provider fallback
```

Required future scenarios include mutable alias advancement, DataFrame/query snapshot preparation, distributed manifest membership, sealed-snapshot immutability, SC1 versus SC2 Evaluation subject separation, idempotent sealing/promotion, no-copy promotion, transformed-DataFrame identity non-inheritance and unavailable-versus-latest historical resolution.

## Future implementation sequence

Only after a later phase explicitly authorizes coding:

```text
E1  data reference/descriptor values and codecs
E2  source selector/resolution ports
E3  data-plane control records
E4  Spark selector/access adapter
E5  portable manifested-Parquet provider
E6  sealing/exact-subject boundary
E7  Generation output representation/promotion transaction
E8  conformance + Q1/Q2 Spark verification
E9  separately owned provider/table-format/platform adapters
```

None of E1-E9 is executed during Phase 005.

## Deferred ownership

005-E leaves to later planning:

- exact Spark/PySpark/JDK support matrix — 005-J;
- provider-native Delta/Iceberg/Hudi/Databricks mappings — 005-J/provider-specific work;
- Attempt epochs/fencing/recovery — 005-G;
- exact Evidence/promotion-basis structures and Provenance — 005-H;
- authorization/credentials/no-egress/encryption — 005-I;
- retention/cleanup orchestration — 005-J/005-K.

## No upstream revision required

005-E requires no change to the eleven accepted concepts, fifteen synchronizations, Phase 003 experience contract, Phase 004 architecture, ADR-0001 through ADR-0008, 005-C package direction, or 005-D durable identity/state model.

No new architecture ADR is required.

## Exit criteria

- [x] no-production-implementation boundary reaffirmed;
- [x] optional Spark dependency boundary defined;
- [x] source selector and exact SourceStateRef roles defined;
- [x] conservative snapshot-before-commit rule defined;
- [x] bounded manifest/distributed component-index model defined;
- [x] portable manifested-Parquet profile planned;
- [x] provider capability/conformance boundary defined;
- [x] candidate/sealed snapshot/output role separation defined;
- [x] 005-G writer-fencing seam reserved;
- [x] idempotent metadata-only promotion plan defined;
- [x] output payload/identity separation preserved;
- [x] future persistence/package impacts mapped;
- [x] V5/AF verification responsibilities mapped;
- [x] future E1-E9 sequence defined without execution.

## Exit decision

**005-E — implementation plan complete; no production implementation performed.**

Next:

**005-F — Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan**.
