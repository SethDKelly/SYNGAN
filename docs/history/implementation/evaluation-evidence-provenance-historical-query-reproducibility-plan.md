---
type: Implementation Authority
title: Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan
status: active
---

# Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan

## Purpose

Define the concrete **future implementation plan** for SYNGAN's Evaluation-to-Evidence completion boundary, immutable Evidence findings and applicability state, typed canonical Provenance assertions, coupled transition/provenance persistence, bounded historical query/read projections, structural historical comparison, and qualified reproducibility assessment.

This document is the canonical Phase 005-H implementation-planning authority.

**Phase 005 remains planning-only.** This plan does not create production source, SQL tables, migrations, Evidence stores, Provenance graphs, query indexes, tests, CI workflows, reports, or integrations.

## Governing authority

005-H is downstream of:

- [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md);
- [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](../architecture/evaluation-evidence-provenance-reproducibility-historical-query.md);
- [005-B Verification Strategy](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [005-C Source Topology](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md);
- [005-D Public Resource/Control-Plane Plan](public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md);
- [005-E Spark Data Boundary Plan](spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md);
- [005-F Runtime/SPI/Learned-State Plan](strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md);
- [005-G Execution/Recovery Plan](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-plan.md).

The governing implementation-planning rule is:

> **Evidence is established only from a semantically validated Evaluation over exact historical subjects; Provenance owns typed relationships between canonical owners; history/query projections remain derived; reproducibility is assembled as a qualified assessment from preserved facts rather than stored as inherited truth.**

## Planning-only and Jackson-methodology boundary

005-H SHALL NOT be interpreted as permission to begin production implementation.

Names such as `EvidenceHandle`, `EvidenceFinding`, `ProvenanceAssertion`, `ExplainView`, and `ReproducibilityAssessment` below identify accepted future implementation roles and intended contracts only.

Completion of 005-H means this slice's implementation plan is sufficiently specified for later delivery planning. It does **not** mean Jackson-style concept/design work is necessarily complete. Phase 005-K must explicitly audit whether further concept, synchronization, experience, architecture, or implementation-planning refinement is required before any later phase may authorize coding.

## Accepted future implementation choices

005-H accepts the following baseline:

- `evidence` and `provenance_assertion` become durable 005-D `ResourceRef`-addressable canonical resources;
- the built-in relational implementation stores Evidence and canonical Provenance in the same SQL control-store family as other bounded control state, using SQLAlchemy Core/PostgreSQL under the 005-D plan;
- no graph database is required for the first implementation and no graph store becomes canonical semantic authority;
- Evidence establishment is an Evaluation-owner application transaction, never a runtime-adapter write;
- one Evaluation may establish zero or more independently identifiable Evidence resources in one atomic/recoverable establishment operation;
- Evidence identity is idempotently bound to the exact Evaluation plus a stable finding-slot key declared by the method/result contract;
- Evidence immutable finding content is stored separately from mutable current applicability/lifecycle state;
- claim strength is explicitly bounded and cannot exceed the committed method, achieved coverage, uncertainty, assumptions, or approximation semantics;
- large diagnostics remain exact distributed data references rather than control-row payloads;
- Generation completion retains an immutable bounded completion basis referencing the exact sealed candidate and exact Evidence used at promotion time;
- Provenance uses typed directed assertions over exact historical references, not duplicated canonical node payloads;
- provenance assertions are idempotent per originating transition/relationship slot and corrected by append/supersession rather than destructive rewrite;
- for the built-in SQL adapter, owner transition + required Evidence/Provenance records use one relational transaction where they share the control store; external projections/integrations use 005-D outbox/reconciliation;
- portability ports still permit another persistence adapter to use durable intent/reconciliation rather than requiring universal cross-store ACID;
- historical query starts from exact references and returns bounded/paginated typed views; unbounded graph dumps are not the primary API;
- canonical Provenance tables receive direct relational indexes for first-order traversal, while optional adjacency/search/materialized projections remain rebuildable and non-authoritative;
- historical comparison reports structural differences and does not infer causality, superiority, or quality without Evidence;
- reproducibility uses a derived `ReproducibilityAssessment` with historical contract/completeness and current feasibility reported separately;
- no canonical `reproducible: bool` field or standalone Reproducibility resource is introduced;
- query/disclosure seams are reserved so 005-I can authorize/redact canonical resources, Provenance paths, projections, counts, and reproducibility output without redesigning the history API;
- row-level/task-level lineage is not part of the bounded canonical Provenance default; large detailed lineage/diagnostics, if later needed, remain referenced data-plane material.

## Future package ownership

005-H refines the 005-C topology with responsibilities equivalent to:

```text
src/syngan/
├── domain/
│   ├── evidence/
│   │   ├── finding.py
│   │   ├── claim_support.py
│   │   └── applicability.py
│   └── provenance/
│       ├── relationships.py
│       └── assertions.py
├── ports/
│   └── history/
│       ├── evidence.py
│       ├── provenance.py
│       ├── query.py
│       └── projections.py
├── application/
│   └── history/
│       ├── establish_evidence.py
│       ├── record_provenance.py
│       ├── explain.py
│       ├── compare.py
│       └── reproducibility.py
├── api/
│   └── history.py
└── adapters/
    └── persistence/
        └── sql/
            └── history_records/
```

Exact leaf-file spelling may change during a later coding phase if cohesion improves. Ownership and import direction must remain equivalent.

History/query composition may use canonical repositories from other owner packages through application/port contracts. It does not move those resources into `domain.provenance`.

## Resource and historical-reference plan

### Additional `ResourceKind` roles

005-H reserves:

```text
evidence
provenance_assertion
```

`Evidence` and `Provenance` are already accepted concepts. A Provenance assertion is the durable representation of one canonical typed relationship assertion; it is not a new concept.

### `HistoricalRef`

Provenance and history must reference exact historical states rather than mutable aliases.

A future tagged `HistoricalRef`/equivalent value can contain one exact supported reference form, including:

- a `ResourceRef` for an occurrence whose resource identity itself denotes the historical occurrence;
- a `RevisionRef` for revisioned semantic authority;
- a resource + immutable `SnapshotId` for a commitment snapshot when that level of exactness is required;
- exact data/state representation references defined by 005-E/005-F/005-G.

A `HistoricalRef` is a serialization/query helper, not another identity system.

It MUST NOT resolve an exact historical reference to current/latest state silently.

## Evaluation runtime-result to Evidence establishment

### Runtime result remains non-final

005-F's `EvaluationRuntimeResult` supplies measurements, achieved coverage, uncertainty/error, assumptions/validity diagnostics, diagnostic references, runtime facts, and operational outcome.

005-H plans an Evaluation-owner normalization/validation step before Evidence establishment.

The future validation must prove, as applicable:

- exact Evaluation and commitment `SnapshotId`;
- exact Criterion revision;
- exact subject/reference identities;
- exact method/configuration and implementation binding;
- achieved scope/coverage/approximation;
- assumptions required for interpretation;
- uncertainty/error semantics;
- no retry-induced double counting under the 005-G contribution contract;
- supported claim strength;
- required dependency/runtime/provenance facts.

Operationally successful runtime output may still be semantically uninterpretable and therefore establish no Evidence.

### Evidence establishment operation

A future bounded `EvidenceEstablishmentPlan`/operation contains:

```text
Evaluation ResourceRef
Evaluation commitment SnapshotId
expected Evaluation StateVersion
exact operational-completion/runtime-result basis
normalized finding declarations
operation idempotency identity
required Provenance declarations
```

This is application/control coordination state, not a domain concept.

For the built-in SQL control adapter, establishing final Evidence for one Evaluation is planned as one bounded relational transaction that:

1. validates expected Evaluation state/version and exact commitment/runtime-result basis;
2. validates every normalized finding/claim boundary;
3. resolves/preallocates stable Evidence identities for finding slots;
4. inserts immutable Evidence finding rows/resources;
5. establishes initial Evidence applicability/current state;
6. updates Evaluation semantic completion under owner transition rules;
7. appends Evaluation transition history;
8. inserts required canonical Provenance assertions where all participating state is in the same control store;
9. records outbox/durable intents for external projections/integrations when required;
10. commits atomically.

A portability adapter that cannot place all canonical owners/provenance in one transaction must provide equivalent atomic-or-recoverable consistency through the 005-D transaction/outbox contract.

### Finding-slot identity

A stable future `EvidenceFindingSlot` is an opaque, method/result-contract-defined identifier such as a namespaced stable string. It is not display text or array position.

The canonical idempotency scope is equivalent to:

```text
exact Evaluation ResourceRef
+ finding slot
```

because the committed Evaluation already fixes Criterion, subject/reference, method and scope. The Evidence row also records those exact identities so the implementation can detect malformed/conflicting replay.

A unique persistence constraint on `(evaluation_id, finding_slot)` or an equivalent key prevents duplicate logical findings.

Repeated establishment with the same slot and equivalent immutable finding fingerprint resolves to the same Evidence identity. Reuse of the slot with materially different immutable content is an integrity conflict requiring reconciliation/new Evaluation, never overwrite.

### Stable Evidence identity

Evidence receives an ordinary opaque 005-D `ResourceId` before/within the establishment transaction.

Evidence identity is not a metric name, hash, Criterion ID, row position, or runtime result ID.

## Evidence representation plan

### `EvidenceHandle` and `EvidenceView`

005-H accepts the public `EvidenceHandle` anticipated by 005-D.

It contains only a typed `ResourceRef(kind=evidence)` and non-authoritative convenience metadata when explicitly freshness-qualified.

`EvidenceView` resolves immutable finding content plus current applicability state separately.

### Immutable finding record

A future immutable `EvidenceFinding` contains or references bounded facts equivalent to:

```text
Evidence ResourceRef
producing Evaluation ResourceRef
Evaluation commitment SnapshotId
finding slot
exact Criterion RevisionRef
exact subject HistoricalRef
exact reference/baseline HistoricalRef(s)
finding schema/type + version
finding payload/summary
scope/population/cohort descriptor
method/configuration identity
coverage mode + achieved coverage
sampling/approximation semantics
uncertainty/error semantics
assumptions
limitations
ClaimSupport
relevant Data Meaning / Constraint / Condition refs
diagnostic snapshot refs
implementation/runtime/dependency refs where material
established_at
SchemaVersion
```

The immutable finding is never updated because later Evidence disagrees or policy changes.

### Finding payload model

005-H does not force every Evidence result into one scalar or Boolean.

The future representation supports:

1. built-in typed finding forms for common generic cases such as satisfaction/violation, scalar/interval/bound, comparative, risk, indeterminate and diagnostic findings;
2. namespaced/versioned Criterion/method-specific finding schemas for extension-specific semantics.

Extension-specific payloads remain explicit schema-family/versioned JSON-compatible values rather than arbitrary pickled Python objects.

Generic query/report surfaces use the bounded claim/summary descriptors without pretending to understand every extension schema.

### `ClaimSupport`

A future claim-support value preserves at least:

```text
exhaustive
bounded_deterministic
statistical
approximate
diagnostic
```

plus method-relevant achieved coverage/uncertainty limitations.

Claim support is validated by Evaluation/application logic. Runtime adapters cannot choose a stronger value than the method result justifies.

### Applicability/current-use state

005-H plans a separately mutable, `StateVersion`-guarded Evidence applicability record.

Stored explicit states must preserve equivalents of:

```text
applicable
superseded
stale_or_obsolete
inapplicable
invalidated
```

The implementation SHOULD distinguish explicit owner disposition from a query-time contextual applicability assessment where staleness depends on the comparison/use context. A query may therefore report an Evidence resource as historically valid, explicitly applicable, but contextually stale for a requested current target.

Changing applicability never mutates the immutable finding.

### Evidence corrections

If the finding is materially wrong:

- preserve the original immutable Evidence;
- transition its current applicability to invalidated/superseded as appropriate;
- perform a new/corrected Evaluation when a corrected finding is needed;
- establish new Evidence under the new Evaluation;
- record typed correction/supersession Provenance where material.

If only a relationship assertion was wrong, correct Provenance without rewriting Evidence.

## Diagnostic-reference plan

Large Evaluation diagnostics remain distributed, exact data-plane resources.

When a diagnostic dataset materially supports the defensibility of an Evidence finding, the Evidence record must reference an immutable/sealed diagnostic snapshot or provider-equivalent exact state.

Mutable log locations or unsealed diagnostic workspaces cannot silently become the durable support basis of Evidence.

Optional best-effort troubleshooting logs may be referenced separately but are not required Evidence support.

## Generation completion-basis plan

005-H refines the exact Evidence basis deferred by 005-E.

A future immutable Generation-owned `GenerationCompletionBasis` record is stored as bounded promotion history keyed to the exact Generation/promotion operation. It need not become a separately public domain resource.

It contains or references enough facts equivalent to:

```text
Generation ResourceRef
Generation commitment SnapshotId
exact SealedDataSnapshotRef
completion requirement slots
exact Constraint / Condition / Criterion refs
exact Evidence ResourceRefs used
per-requirement sufficiency determination
claim-strength requirement vs achieved support
promotion idempotency operation
Generation StateVersion / WriterFence or authority basis used
established output ResourceRef
```

The promotion transaction validates these exact refs. Evidence established later cannot be silently inserted into the historical basis.

A negative or indeterminate Evidence finding remains valid Evidence even when it prevents Generation completion.

## Canonical Provenance assertion plan

### Relational canonical baseline

The first built-in implementation plans canonical Provenance as indexed relational assertions in the 005-D SQL control store.

This is deliberate:

- canonical bounded control facts already live there;
- coupled material transitions can often establish required relationships transactionally;
- ordinary inbound/outbound traversal maps cleanly to indexes;
- a separate graph database would introduce another consistency/security/backup authority boundary before it is demonstrated necessary.

A later adapter may use graph/document/other persistence if it satisfies the same port/conformance contract. The storage technology never changes Provenance meaning.

### Binary typed assertion

The future canonical representation uses one directed typed assertion per relationship:

```text
ProvenanceAssertion
    ResourceRef(kind=provenance_assertion)
    subject: HistoricalRef
    predicate: ProvenancePredicate
    object: HistoricalRef
    relationship_slot
    qualifiers schema/version + bounded values
    originating transition / operation ref
    assertion state
    recorded_at
    SchemaVersion
```

Multi-party material transitions produce a bounded set of binary assertions sharing the same originating transition/operation identity. This keeps traversal/indexing simple without turning the origin transition into a new domain concept.

### Predicate catalog

The initial canonical predicate families preserve the Phase 002/004 meanings and future concrete names equivalent to:

```text
bound_to / governed_by
derived_from / produced_by
used / depended_on
evaluated / referenced
operationally_realized_by
recovered_from / resumed_from
supersedes / restricts / retires / invalidates
```

Exact predicate spelling is stable wire/persistence contract once implemented and therefore requires compatibility governance. Role/qualifier values distinguish cases without creating an unbounded predicate for every implementation detail.

### Provenance idempotency

A provenance assertion's uniqueness/idempotency scope is equivalent to:

```text
originating material transition/operation
+ relationship slot
+ predicate
+ exact subject HistoricalRef
+ exact object HistoricalRef
```

Equivalent retry resolves to the same assertion. The same transition/slot attempting contradictory relationship content is an integrity conflict.

Runtime plugins, scheduler logs, OpenLineage, MLflow, or derived indexes cannot directly establish canonical Provenance merely because they observed an event.

### Assertion correction

Provenance finding/history correction is planned using:

```text
immutable provenance_assertion
+ mutable assertion applicability/current-state projection
+ append-only correction/supersession relation/record
```

The original assertion remains auditable. A replacement assertion becomes preferred for ordinary current historical queries according to current state.

Correcting Provenance never mutates the referenced canonical owners.

## Provenance materiality plan

Canonical Provenance records material semantic/historical relationships, not every runtime event.

Expected material capture points include:

- activity commitment bindings to exact Strategy/Data Meaning/Constraint/Criterion/data/state refs;
- Learning establishing a Learned State;
- Generation establishing an output representation;
- Evaluation establishing Evidence;
- Evidence used in a Generation completion basis;
- Execution operationally realizing an activity;
- materially relevant checkpoint resume/recovery relationships;
- actual dependency/base-artifact/runtime-binding identities when required for history/reproducibility.

The complete 005-G Attempt state-transition journal remains Execution-owned history. It is queried alongside Provenance rather than copied edge-for-edge into the graph.

No default provenance assertion is created per Spark task, row, file, heartbeat, metric sample, or log event.

## Coupled transition consistency

### Built-in SQL path

Where owner state, Evidence and required Provenance all use the built-in SQL control store, the future implementation SHOULD establish them in one SQL transaction when their ownership transaction naturally coincides.

Examples include:

```text
Evaluation completion + Evidence + produced_by/evaluated relationships
Learning -> Learned State + required produced_by/derived_from relationships
Generation output promotion + completion basis + required produced_by/used-Evidence relationships
```

This is not permission to merge concept ownership into one table or generic repository; it is a transactional implementation optimization beneath separate owner ports.

### Cross-store/derived integrations

External lineage systems, search projections, warehouses, graph projections, reporting stores, and telemetry are not required in the canonical transaction.

The owner transaction records sufficient canonical state plus 005-D outbox/durable intent so those projections can be materialized idempotently and repaired.

A third-party canonical Provenance adapter that cannot share the owner transaction must satisfy the same no-silent-gap invariant through durable intent and reconciliation.

## Historical query API plan

### Public history surface

005-H plans a public client surface equivalent to:

```text
client.history.provenance(...)
client.history.explain(...)
client.history.compare(...)
client.history.reproducibility(...)
```

and owner-specific conveniences such as `client.evaluation.evidence(...)` where useful.

These APIs return typed read views, not one generic mutable graph object.

### `ProvenancePage`

A bounded provenance traversal page contains:

```text
target exact HistoricalRef
direction
predicate/materiality filters
assertion views
next cursor
projection/canonical freshness metadata
```

Traversal is paginated and bounded. Exact history verification must be able to use canonical assertion indexes rather than trusting a stale projection silently.

### First implementation indexes

The canonical relational Provenance table should be indexed for at least:

```text
(subject exact-ref key, predicate)
(object exact-ref key, predicate)
originating transition/operation
predicate + recorded/order context
current assertion state
```

Exact index shape remains a later physical-schema tuning decision, but these query directions are contractual requirements.

Optional materialized/derived projections may additionally index activity/result/Evidence/dependency/recovery paths.

### `ExplainView`

An explain query is bounded by explicit options such as:

```text
max depth
allowed predicate families
materiality profile
include Execution detail?
page/breadth limits
current annotations?
```

The result includes exact resource links plus explicit gap/unavailable/withheld/invalid states. It does not require copying full source/output/Learned-State payloads into memory.

### `HistoricalComparisonView`

Comparison accepts two exact historical targets and reports categorized differences across source/state, semantic authorities, Strategy/configuration, dependencies, runtime binding, Execution/recovery, Evidence and representation where material.

Each difference carries the exact historical values/refs and provenance basis used to establish the difference.

The comparison layer MUST NOT infer causality or superiority. Such claims require explicit Evaluation/Evidence.

## Query consistency/freshness plan

Historical immutable facts are stable by exact identity. Current applicability, availability and disclosure state may change during a query.

A future query result therefore carries enough observation/freshness metadata to distinguish:

```text
exact immutable historical binding
current state observed at StateVersion N
projection observed at projection generation/cursor
current availability/disclosure annotation
```

No universal cross-store snapshot transaction is required for every read, but the response must not imply stronger global consistency than was actually observed.

Wall-clock timestamps are supplemental; per-resource revisions/state versions/origin transitions remain the stronger ordering basis where available.

## Resolution/gap states

Historical views preserve 005-D/004-G distinctions equivalent to:

```text
resolved
absent
unknown / indeterminate
unavailable
withheld / redacted
invalid
corrected / superseded
```

A projection miss is not automatically `absent` if canonical lookup has not established absence.

005-I owns authorization/redaction details and whether even relationship existence may be disclosed.

## Reproducibility assessment plan

### Derived assessment, not resource authority

A future `ReproducibilityAssessment` is a typed derived view/cacheable computation. It receives no canonical `ResourceId` merely because a result is serializable.

Its input is an exact target plus an explicit assessment request/context.

### Assessment inputs

The assembler resolves, as material:

- target ResourceRef / exact historical snapshot;
- original semantic commitment;
- exact source/input/subject/reference identity;
- Data Meaning/Constraint/Strategy/Criterion revisions;
- Learned State and representation/codec identity;
- implementation binding/package/build/runtime identities;
- external/base artifact identities;
- randomness/RNG/seed semantics;
- sampling/approximation/coverage semantics;
- declared nondeterminism;
- material Attempt/checkpoint/recovery facts from 005-G;
- physical representation/equivalence guarantees;
- current dependency/artifact availability;
- current authorization/network/no-egress capability as supplied by 005-I.

### Result model

The assessment reports at least:

```text
target exact HistoricalRef
requested reproduction goal/equivalence
strongest historically supportable class
historical-context completeness
current feasibility
missing/unavailable/withheld/invalid prerequisites
material nondeterminism/limitations
current environment/dependency compatibility observations
assessment context/freshness
reason codes / human explanation
```

Reproducibility classes preserve:

```text
exact_deterministic
semantic
statistical
bounded_or_approximate
comparative
not_reproducible
insufficient_context
```

Current feasibility remains a separate axis equivalent to:

```text
feasible
feasible_with_limitations
blocked
indeterminate
```

Thus an output may historically have enough information for statistical reproduction while reproduction is currently blocked because a dependency is unavailable or policy forbids required egress.

### Seed is not determinism

The assembler cannot promote a claim to exact reproduction merely because a seed is present.

Hardware/runtime nondeterminism, distributed ordering, algorithm characteristics, checkpoint/recovery path, external mutable services, codec/representation changes and unavailable artifacts may bound the strongest claim.

### Reproduction readiness versus reproduction result

`ReproducibilityAssessment` only determines whether and how reproduction can be attempted/qualified.

Actually reproducing a Generation/Learning/Evaluation is new domain work using new resources/Executions. Equivalence success is established by appropriate Evaluation/Evidence, not by the assessment itself.

## Reproducibility caching

A deployment MAY cache reproducibility assessments for performance.

A cache entry is non-authoritative and must be keyed by an assessment-context fingerprint that includes the historical target plus material current availability/compatibility/security inputs. It carries freshness/observed-at information and can be invalidated when relevant prerequisites change.

A stale cached assessment cannot overwrite canonical history or become the basis for semantic promotion without current revalidation.

## Security/redaction seam for 005-I

005-H deliberately plans history APIs so 005-I can enforce authorization without redesigning query semantics.

Future query resolution must be capable of applying disclosure policy to:

- Evidence immutable finding and applicability detail;
- canonical Provenance assertion existence/content;
- endpoint resource resolution;
- reverse lookup/traversal;
- explain paths;
- comparison fields;
- projection indexes and cached summaries;
- result counts/pagination where existence itself is protected;
- reproducibility prerequisites/reason text.

A query result can therefore retain `withheld`/redacted semantics rather than fabricating absence or leaking protected graph shape.

005-H does not select the policy engine or authorization model.

## Retention/tombstone behavior

If a source/output/diagnostic/state payload is legitimately removed under policy, historical identity and allowed tombstone facts remain resolvable according to 005-D/005-I retention/disclosure rules.

Provenance may continue to state that a historical relationship existed even when a payload is currently unavailable, unless current security policy also withholds that relationship.

Reproducibility assessment reports the missing prerequisite rather than rewriting the historical relationship.

## Scale boundaries

Canonical Evidence/Provenance control state scales with material findings/transitions/relationships, not raw data volume or platform task count.

The future implementation MUST NOT require:

- one Evidence row per source/generated record by default;
- one Provenance assertion per Spark task/file/row by default;
- full graph materialization in coordinator memory for ordinary explain/traversal;
- loading distributed diagnostic payloads to answer bounded Evidence/history queries;
- full source/output collection to assemble reproducibility context.

Large detailed diagnostics or future row-level lineage remain distributed referenced material with their own explicit coverage/retention semantics.

## Persistence and migration impact plan

Future bounded SQL responsibilities include equivalents of:

```text
evidence
evidence_finding
evidence_applicability
provenance_assertion
provenance_assertion_state
provenance_correction
generation_completion_basis
history/projection checkpoints where needed
```

Exact physical normalization may be refined during the later implementation phase while preserving owner boundaries and unique/idempotency constraints.

Every persisted envelope has an explicit `SchemaVersion`. Migration rules preserve immutable Evidence findings and Provenance assertions; migrations cannot rewrite historical meaning for convenience.

No SQL schema or migration is created during Phase 005.

## Verification mapping

005-H primarily owns future V8 and directly maps:

```text
AF-08 idempotent Evidence/provenance establishment
AF-09 runtime result != Evidence / semantic completion
AF-10 Provenance/query projection non-authority
AF-11 protected history/query paths honor authorization seam
AF-16 typed applicability/resolution/disclosure states remain distinct
AF-17 exact historical refs never silently resolve latest
AF-18 coupled transition/provenance crash consistency
AF-19 Evaluation retry contributions do not double-count
```

It also contributes to AF-03/04/05/12/13/20 where history references identity, non-final material, immutable commitments, remote integrations, bounded data-plane behavior and platform subordination.

### Required future Evidence scenarios

Future tests must include:

- runtime success cannot insert Evidence directly;
- same Evaluation/finding slot replay returns same Evidence;
- conflicting finding replay is rejected;
- multiple finding slots establish independently without partial visible completion;
- claim strength above achieved method/coverage/uncertainty is rejected;
- negative and indeterminate findings remain valid Evidence;
- applicability change does not mutate immutable finding;
- correction requires new Evaluation/Evidence when finding meaning changes;
- exact diagnostic support ref cannot silently resolve to a newer mutable diagnostic.

### Required future Provenance/history scenarios

Future tests must include:

- required owner transition and Provenance cannot silently diverge;
- retry does not duplicate equivalent assertions;
- contradictory assertion for one origin/slot conflicts;
- provenance correction preserves original assertion;
- query projection disagreement loses to canonical assertion state;
- explain traversal is bounded/paginated;
- comparison reports structural difference without causal claim;
- unavailable/unknown/withheld/invalid are not collapsed into absence;
- a graph/search integration cannot write canonical relationships merely by observing runtime events.

### Required future reproducibility scenarios

Future tests must include:

- seed alone does not imply exact deterministic class;
- missing artifact changes current feasibility without changing historical contract;
- recovery/checkpoint/runtime differences can bound the strongest class;
- current no-egress/security policy can block reproduction while history remains intact;
- cached assessment staleness is visible;
- reproduction assessment never creates a new Generation/Evaluation or claims equivalence success by itself.

## Future implementation sequence

Only after a later phase explicitly authorizes coding and the Jackson/design-completeness gate is passed:

```text
H1  exact HistoricalRef + Evidence finding/claim/applicability contracts
H2  Evidence establishment operation/idempotency/atomicity
H3  Generation completion-basis persistence contract
H4  Provenance predicate/assertion/correction contracts
H5  SQL canonical Evidence/Provenance adapter + transaction coupling
H6  canonical traversal indexes + derived projection ports
H7  explain / provenance / comparison public read models
H8  reproducibility assessment assembler + cache contract
H9  security/disclosure seam integration with 005-I
H10 V8 conformance/failure/history/reproducibility verification
```

None of H1-H10 is executed during Phase 005.

## Deferred ownership

005-H leaves to:

- 005-I — authorization, redaction/withholding policy, sensitive-history/query protection, dependency/artifact trust and no-egress enforcement;
- 005-J — concrete OpenLineage/MLflow/platform-lineage/search/observability integrations, deployment topology and performance/support matrices;
- 005-K — cross-slice design/implementation-plan audit, Jackson-methodology completeness decision, backlog closure and implementation-readiness exit.

External lineage systems may later receive/export normalized relationships, but they do not become canonical Provenance automatically.

## No new concepts or upstream revision

005-H adds no Evidence Set, Finding Slot, Provenance Edge, Lineage Graph, History Event, Historical View, Reproducibility Assessment, Reproduction Plan, or Metadata Graph concept.

No change is required to the eleven accepted concepts, fifteen synchronizations, Phase 003 experience contract, Phase 004 architecture/ADR set, or 005-C through 005-G implementation-planning authority.

No new architecture ADR is required.

## Exit criteria

- [x] planning-only/Jackson-completeness boundary preserved;
- [x] Evidence identity/establishment/idempotency plan defined;
- [x] immutable finding vs applicability state defined;
- [x] claim-support/finding representation plan defined;
- [x] exact diagnostic/reference support boundary defined;
- [x] Generation completion-basis plan defined;
- [x] canonical relational Provenance baseline defined;
- [x] exact typed relationship/idempotency/correction plan defined;
- [x] owner-transition/Provenance consistency plan defined;
- [x] bounded historical query/explain/compare plan defined;
- [x] non-authoritative projection/freshness contract defined;
- [x] reproducibility assessment/current-feasibility separation defined;
- [x] 005-I disclosure/security seams reserved;
- [x] retention/scale boundaries defined;
- [x] future persistence/migration responsibilities mapped without execution;
- [x] V8/fitness/failure scenarios mapped;
- [x] H1-H10 future coding sequence defined without execution.

## Exit decision

**005-H — implementation plan complete; no production implementation performed and no coding authority granted.**

Next:

**005-I — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan**.
