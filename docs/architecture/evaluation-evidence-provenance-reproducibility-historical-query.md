---
type: Architecture Authority
title: Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture
status: active
---

# Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture

## Purpose

Define how semantically valid Evaluation results become durable Evidence, how material historical relationships are recorded as typed Provenance, how historical explanation/comparison is queried efficiently, and how current reproducibility assessments are assembled from canonical historical state without duplicating canonical concept ownership into a universal metadata graph.

This document establishes the canonical Phase 004-G architecture downstream of the accepted Evaluation, Evidence, Provenance, Reproducibility, historical-inspection, identity/persistence, distributed-data, runtime-adapter, and Execution/recovery contracts.

It defines Evidence establishment and identity, Evidence result representation, provenance-edge persistence and correction, coupled transition recording, historical query projections, explain/compare query semantics, reproducibility assessment assembly, and enterprise-scale/query boundaries. It does **not** select a graph database, SQL engine, warehouse, OpenLineage/MLflow integration, report format, visualization framework, or authorization implementation.

## Governing authority

This architecture remains downstream of:

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md);
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](public-api-resource-handle-workflow-semantic-mapping.md);
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md);
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md);
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](strategy-extension-learning-generation-evaluation-runtime-adapter.md);
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md);
- [Evaluation](../concepts/evaluation.md);
- [Evidence](../concepts/evidence.md);
- [Provenance](../concepts/provenance.md);
- [Reproducibility Contract](../authority/reproducibility-contract.md);
- [Evaluation, Evidence & Review Experience](../experience/evaluation-evidence-review.md);
- [Provenance, Reproducibility & Historical Inspection Experience](../experience/provenance-reproducibility-historical-inspection.md);
- [Core Synchronizations](../synchronizations/core-synchronizations.md), especially SYNC-09 through SYNC-15.

## Primary decision

SYNGAN SHALL separate four architectural responsibilities:

```text
Evaluation semantic result
        ↓ validate / normalize
Evidence establishment
immutable finding resources + mutable applicability state
        ↓
Typed Provenance relationships
historical bindings / derivations / realization / evaluation / recovery
        ↓
Historical query projections
explain / traverse / compare
        ↓
Reproducibility assessment assembler
current qualified claim over exact historical target
```

Evidence and canonical domain resources remain sources of substantive truth. Provenance owns typed historical relationship assertions. Historical query indexes and reproducibility assessments are derived views and MUST NOT become canonical write authority.

## Evaluation runtime result to Evidence establishment

### Runtime result is not Evidence

An Evaluation runtime adapter returns an implementation-facing result envelope under 004-E. That envelope may contain measurements, coverage summaries, uncertainty values, assumption diagnostics, bounded aggregates, and references to large diagnostic data.

The envelope is non-final until Evaluation/application logic verifies that:

- the exact committed Evaluation specification was realized;
- the exact Criterion revision was answered;
- exact subject/reference identities match the commitment;
- method/configuration and implementation binding match the commitment;
- achieved scope/coverage/sampling/approximation are known;
- assumptions required by the method remain valid enough for interpretation;
- uncertainty/error semantics can be represented;
- claim strength does not exceed method/scope/coverage/uncertainty support;
- required dependency/runtime/provenance facts are sufficiently available.

Operational success or a numeric metric does not bypass this validation.

### Evidence establishment boundary

Only a semantically valid Evaluation may establish Evidence.

Conceptually:

```text
Evaluation V7
   ↓ Execution / Attempts
method-runtime results
   ↓ Evaluation semantic validation
normalized finding descriptors
   ↓ idempotent Evidence establishment
Evidence E21 / E22 / ...
```

Evidence establishment is an owner-side control-plane transition. Runtime adapters do not insert canonical Evidence directly.

### One Evaluation may establish multiple Evidence resources

The accepted concept permits zero or more independently interpretable Evidence records from one Evaluation.

Architecture SHALL therefore support a bounded **Evidence establishment plan/result set** without promoting `Evidence Set` into a domain concept.

Each individual Evidence resource must remain independently identifiable and interpretable.

Examples of legitimate separate findings include:

- one finding for a universal Constraint result;
- one estimate with uncertainty for a fidelity Criterion;
- separate independently meaningful findings from one multi-output Evaluation method.

### Evidence slot / finding-key identity

Retries must not create duplicate Evidence merely because the same Evaluation result is normalized twice.

The Evidence establishment path SHALL use an idempotency identity scoped to the semantic finding being established, equivalent to:

```text
Evaluation identity
+ Criterion/result role
+ subject/reference/scope identity as material
+ stable finding slot/key within the Evaluation result contract
```

The exact encoding is deferred.

A stable finding slot identifies **which logical finding** is being established; it is not itself a domain concept and must not be derived solely from mutable display text or metric ordering.

Repeated establishment of the same finding slot with equivalent immutable content resolves to the same Evidence identity/result. A conflicting payload for an already-established slot is a consistency error requiring reconciliation rather than silent overwrite.

### Evidence immutable finding payload

Once established, an Evidence resource preserves immutable historical finding semantics including or referencing enough information equivalent to:

- stable Evidence identity;
- producing Evaluation identity;
- exact Criterion revision;
- exact subject and reference/baseline identities;
- finding/result representation;
- logical scope/population/cohort;
- method/configuration identity;
- coverage mode and achieved coverage;
- sampling/approximation semantics;
- uncertainty/confidence/error semantics;
- assumptions and limitations;
- supported claim-strength boundary;
- relevant Data Meaning/Constraint/Condition references;
- diagnostic data references where retained;
- producing implementation/runtime/dependency identities where material;
- provenance references/relationships.

The finding payload is not rewritten in place because a later Evaluation disagrees or policy changes.

### Evidence applicability state is separate

Evidence may have mutable future-use state such as applicable/current, superseded, stale/obsolete, inapplicable, or invalidated.

This state is conflict-versioned under 004-C and remains separate from the immutable historical finding.

A new threat model, newer output, newer Criterion, or discovered methodological defect can change current applicability without rewriting what the original Evaluation observed.

### Evidence correction semantics

A materially incorrect finding is not corrected by editing its immutable result fields.

Depending on cause, architecture supports:

- invalidating the Evidence for future reliance;
- performing a corrected/new Evaluation and establishing new Evidence;
- correcting only an incorrect Provenance assertion when the finding itself was valid;
- recording explicit supersession/current-preference relationships where appropriate.

Historical audit must remain able to distinguish the original finding from later correction/replacement.

## Evidence finding representation

### No universal scalar result

The Evidence representation MUST support different finding forms without reducing all results to `score`, `passed`, or `quality`.

A finding representation may encode or reference forms such as:

- satisfied / violated under an exact rule/scope;
- scalar/vector/statistical estimate with units/interpretation;
- interval/bound;
- comparative finding;
- risk estimate under a threat model;
- indeterminate/inconclusive result;
- diagnostic/partial observation.

The architecture may use typed value envelopes or method/Criterion-specific schemas. The exact class hierarchy is deferred.

### Claim-support descriptor

Evidence SHOULD carry a bounded claim-support descriptor sufficient for generic review/query surfaces to interpret strength without understanding every method implementation.

It should preserve distinctions equivalent to:

- exhaustive/universal;
- deterministic bounded/certificate-backed;
- statistical;
- approximate/sketch;
- diagnostic/partial.

This descriptor does not replace Criterion/method details and cannot inflate a claim beyond the producing Evaluation.

### Diagnostics remain separate data-plane resources

Large violation sets, nearest-neighbor records, attack traces, row-level observations, prediction outputs, or other detailed diagnostics remain referenced distributed data-plane material.

Evidence stores bounded summaries and stable diagnostic references rather than ingesting all details into control-plane rows.

A diagnostic dataset is not automatically Evidence merely because it was produced by an Evaluation.

## Evidence used by Generation completion

### Exact completion-basis binding

When Generation completion depends on Evidence, the promotion path SHALL preserve an immutable completion-basis record/reference set sufficient to identify:

- exact Generation;
- exact sealed candidate subject;
- exact committed Condition/Constraint completion requirement;
- exact Criterion revision;
- exact Evidence identity used;
- sufficiency/claim-strength determination made by Generation;
- promotion state/version/fence context where material.

This completion-basis representation is Generation-owned promotion history, not Evidence authority.

### Later Evidence does not enter historical promotion retroactively

Evidence created after Generation promotion may be historically related to the completed output but MUST NOT silently become part of the original completion basis.

The original promotion basis remains immutable historical state.

### Negative or indeterminate Evidence remains valid

Evidence establishment is independent of whether Generation may complete.

A valid negative or indeterminate Evidence resource may block Generation promotion when the committed completion requirement demands satisfaction/determination.

## Provenance persistence architecture

### Canonical typed edge/assertion store

Provenance SHALL be represented as durable typed relationship assertions over stable references.

A provenance assertion should contain or resolve enough information equivalent to:

```text
provenance_assertion_id
relationship_type
subject_ref(s)
object_ref(s)
role / qualifiers
historical order/time context
originating material transition/reference
assertion status / supersession when corrected
schema version
```

Material relationship families include at least:

- bound / governed by;
- derived from / produced by;
- used / depended on;
- evaluated / referenced;
- operationally realized by;
- recovered / resumed from;
- superseded / restricted / retired / invalidated context.

One physical persistence technology may represent these as rows, documents, edges, events, or another model. The typed semantics are canonical; a graph database is not required.

### References, not duplicated canonical payloads

Provenance assertions store stable references and relationship qualifiers, not wholesale copies of canonical concept state.

A query that needs the current or historical Data Meaning/Evidence/Generation/Learned State payload resolves that canonical owner through the appropriate repository/handle contract.

A denormalized query projection may cache selected display fields, but the projection remains non-authoritative and refreshable.

### Provenance assertion identity and idempotency

Material transitions can be retried. Recording required Provenance must therefore be idempotent.

An assertion's idempotency identity SHALL be scoped to the originating transition plus relationship role and exact referenced historical states strongly enough to prevent:

- duplicate equivalent edges from retry;
- one relationship being mistaken for another;
- a stale retry writing a relationship for a different semantic revision.

Equivalent repeated recording resolves to the same assertion or a recognized duplicate. Conflicting relationship content for the same transition/role is a consistency defect.

### Provenance correction is append/supersede, not destructive rewrite

When an assertion is found wrong or incomplete, correction SHALL preserve auditability through a replacement/supersession/invalidation relationship or equivalent durable correction record.

The corrected/current assertion may be preferred for ordinary historical queries while the earlier assertion remains retrievable where audit policy requires it.

Correcting a Provenance assertion does not mutate another canonical resource.

## Coupled transition and provenance consistency

### Required provenance participates in transition completion

Where upstream semantics require Provenance for a material transition, the transition SHALL NOT be considered durably complete while its required provenance is irreconcilably absent.

Examples include:

- Learning → Learned State establishment;
- Generation → completed output promotion;
- Evaluation → Evidence establishment;
- Evidence used as Generation completion basis.

### No universal distributed transaction requirement

004-G does not require every canonical owner and Provenance store to share one database transaction.

Compliant implementation patterns may include:

- same-store ACID transaction;
- durable transition intent plus idempotent provenance completion;
- transactional outbox;
- owner transition with a recoverable provenance-pending state;
- reconciliation of a known coupled transition;
- another mechanism satisfying detectable/recoverable consistency.

What is prohibited is silent divergence where a result appears fully authoritative but the traceability guaranteed by its semantic contract has been permanently lost without being detected.

### Provenance write authority remains narrow

Only application/control logic responsible for the material transition, or an explicitly authorized provenance-recording port acting on that transition, may establish canonical SYNGAN provenance assertions.

Runtime plugins, external lineage systems, and search indexes do not gain authority to rewrite canonical relationships merely by observing platform events.

## Historical query architecture

### Query service is a read composition layer

SYNGAN SHALL expose historical query capabilities through a read/composition layer over:

- canonical typed Provenance assertions;
- canonical resource repositories/handles;
- exact revision/commitment snapshots;
- Evidence applicability state;
- Execution/Attempt material history;
- distributed representation references;
- dependency/runtime identities;
- derived search/adjacency indexes where useful.

The query service does not own the underlying state it resolves.

### Canonical edge store plus derived adjacency/search projections

For efficient traversal, architecture SHOULD support derived projections/indexes such as:

- outgoing relationships by subject;
- incoming relationships by object;
- relationship-type indexes;
- resource-kind/time indexes;
- result-to-producing-activity indexes;
- activity-to-bound-authority indexes;
- Evidence-to-Criterion/subject/promotion-use indexes;
- dependency usage indexes;
- material Execution/recovery indexes.

These projections may be eventually consistent if ordinary query surfaces expose freshness appropriately and canonical transitions never rely on them as sole mutation authority.

For correctness-sensitive historical verification, a query must be able to resolve through canonical Provenance/resource state rather than trusting a stale search cache silently.

### Explain query

An `explain`-style query starts from one stable target and returns a progressively disclosed material path rather than an unbounded graph dump.

It SHOULD support:

- typed relationship filtering;
- depth/path limits;
- materiality profiles;
- pagination;
- inclusion/exclusion of Execution detail;
- current-state annotations separately from historical bindings;
- explicit gap/withheld/unavailable indicators;
- canonical resource links for drill-down.

Typical target paths include completed output → Generation → Learned State → Learning → source/meaning/Strategy/dependencies and Evidence → Evaluation → Criterion/subject/reference/method.

### Historical comparison query

A comparison service resolves two exact historical targets and produces a structural/material diff across categories such as:

- source/input state;
- Data Meaning;
- Constraints/handling;
- Strategy/configuration;
- implementation/runtime bindings;
- Learning/sampling/approximation;
- Learned State;
- Generation Conditions/quantity/scope;
- Evaluation Criteria/methods;
- dependencies;
- Execution/Attempt/recovery facts;
- Evidence;
- current lifecycle/applicability state;
- physical representation differences where semantically relevant.

The comparison result is a derived view.

It MUST NOT infer that a difference caused an outcome or that one result is better without explicit Evaluation/Evidence supporting that claim.

### Historical versus current annotations

Historical queries SHALL preserve the distinction among:

- exact historical fact/binding;
- current lifecycle/applicability state;
- current resource availability;
- current authorization/disclosure status;
- current reproducibility assessment.

For example, one output path may show a historically exact base-artifact identity, current artifact unavailability, and a current reproduction-class degradation without modifying the original history.

## Provenance gaps and resolution states

Historical resolution must preserve states equivalent to:

- resolved;
- absent because the relationship/value never existed;
- unknown/indeterminate;
- unavailable because retained identity exists but payload/dependency cannot currently resolve;
- withheld/redacted because the current actor lacks disclosure permission;
- invalid/integrity defect;
- corrected/superseded assertion.

These states MUST NOT collapse into generic `null`.

004-H will define detailed authorization/redaction mechanics; 004-G requires query APIs and projections not to erase the semantic distinction.

## Reproducibility assessment architecture

### Reproducibility is assembled, not stored as master truth

A reproducibility assessment is a derived current interpretation for one exact target under one assessment context.

It SHALL be assembled from canonical facts such as:

- target resource and committed semantic snapshot;
- source/input/subject/reference stable identities;
- Data Meaning/Constraint/Strategy/Criterion revisions;
- Learned State and output representation identities;
- implementation binding/package/runtime/state-codec identities;
- dependency/base-artifact identities and current availability;
- randomness/RNG/seed policy;
- sampling/approximation/coverage semantics;
- nondeterminism characteristics;
- material Attempt/checkpoint/recovery facts where outcome-affecting;
- representation/equivalence guarantees;
- current authorization/network/dependency constraints where relevant to whether reproduction can be attempted.

Provenance supplies the historical relationships. Canonical owners supply substantive state.

### Assessment result shape

A reproducibility assessment should contain or resolve enough information equivalent to:

```text
assessment target
assessment time/context
supported reproduction class
accepted equivalence definition
preserved required conditions
missing / unavailable / mutable dependencies
known nondeterminism / approximation limitations
material withheld facts affecting certainty
reasons stronger classes are unsupported
reproduction-attempt readiness
```

The supported classes remain:

- exact deterministic;
- semantic;
- statistical;
- bounded/approximate;
- comparative;
- not reproducible / insufficient context.

### Strongest-defensible-class rule

The assessor MUST NOT select a stronger class than the weakest unresolved material dependency, nondeterminism, identity, approximation, or equivalence boundary permits.

A seed alone cannot establish exact determinism.

### Assessment may be cached, but cache is not canonical authority

A reproducibility assessment may be persisted/cached for performance or audit, but it must carry enough input/context identity and freshness information to determine when it is stale.

A later dependency loss, policy change, new Provenance correction, or newly discovered nondeterminism may change the current assessment without rewriting the historical target.

No generic mutable `reproducible=true` field is canonical.

### Reproduction readiness versus successful reproduction

The assessor may determine that context is sufficient to **attempt** a reproduction.

Actual success requires new Learning/Generation/Evaluation work as appropriate, plus an explicit equivalence Criterion/Evidence when the target cannot be proven identical by construction.

A reproduction attempt never overwrites the historical target.

## Historical Evidence and current applicability queries

Evidence query surfaces SHALL permit actors to inspect both:

```text
Historical finding
what Evaluation established then
```

and:

```text
Current applicability
whether the Evidence is presently preferred/stale/inapplicable/invalidated
```

A later Evidence resource may supersede another for current review but does not rewrite the older finding.

When Evidence was part of Generation promotion, historical query must be able to identify the exact completion-basis relationship.

## External lineage / metadata integration boundary

SYNGAN MAY export selected Provenance/Execution/resource identities to systems such as lineage catalogs, observability platforms, model registries, or metadata systems through adapters.

Such systems are projections/integrations unless a future explicit authority contract says otherwise.

An external lineage edge observed from Spark/OpenLineage/another platform MUST NOT automatically become canonical SYNGAN semantic provenance without validation against SYNGAN identities and relationship semantics.

Likewise, deleting or changing an external catalog record does not rewrite SYNGAN canonical history.

Detailed platform integration is refined in 004-I.

## Authorization/disclosure composition boundary

Historical/Evidence/Provenance queries must be designed to compose with 004-H authorization/redaction so that:

- sensitive references/qualifiers can be withheld independently;
- the existence of an authorized relationship need not be falsified when detail is restricted;
- indexes do not become an information-leak side channel;
- cached query projections honor disclosure scope or return opaque/withheld representations;
- reproducibility assessment can distinguish `missing` from `withheld`, and may downgrade certainty when required facts cannot be inspected by the actor.

004-G does not choose RBAC/ABAC/redaction technology.

## Query scalability and boundedness

Historical query architecture MUST remain practical when:

- source/output payloads contain hundreds of millions of rows;
- Learned State is distributed;
- one Execution maps to large numbers of platform tasks;
- Provenance contains many historical activities and relationships.

Canonical history SHOULD scale with material resources/revisions/transitions/relationships/Attempts/Evidence—not row count or task/log volume by default.

Query services SHOULD support:

- stable-reference traversal without payload materialization;
- indexed adjacency lookups;
- bounded path depth and pagination;
- materiality filters;
- asynchronous/streamed large query results where needed later;
- summary-first progressive disclosure;
- platform drill-down by reference rather than telemetry ingestion.

Historical explanation/reproducibility assessment MUST NOT require collecting source/output/Learned-State payloads or all logs into driver memory.

## Failure and integrity semantics

The architecture must preserve distinguishable failure conditions such as:

- Evidence establishment conflict for an existing finding slot;
- Evidence subject/reference mismatch;
- claim-strength validation failure;
- required Provenance missing/pending;
- conflicting Provenance assertion for one transition/role;
- unresolved Provenance correction;
- stale/incomplete query projection;
- broken historical reference;
- dependency unavailable;
- withheld historical detail;
- reproduction context insufficient;
- historical comparison only partially resolvable.

These are not all domain failures. The owning service/resource must expose the affected authority and recovery/interpretation consequence explicitly.

## Architecture invariants

1. Runtime Evaluation results MUST NOT become Evidence without Evaluation semantic validation.
2. Evidence immutable finding semantics MUST remain separate from mutable current applicability state.
3. Retried Evaluation/result normalization MUST NOT establish ambiguous duplicate Evidence for the same logical finding.
4. Evidence claim strength MUST NOT exceed method/scope/coverage/uncertainty support.
5. Large diagnostics MUST remain separately referenced data-plane material by default.
6. Generation completion must preserve the exact Evidence/candidate/requirement basis used at promotion.
7. Later Evidence MUST NOT enter an earlier promotion basis retroactively.
8. Provenance MUST store typed historical relationships over stable references rather than duplicate canonical resource payloads.
9. Required Provenance recording MUST be idempotent and recoverably consistent with the transition it explains.
10. Provenance correction MUST preserve auditability and MUST NOT mutate another concept's authority.
11. Historical query indexes/projections MUST remain derived and non-authoritative.
12. Historical inspection MUST resolve exact historical identities rather than substitute current aliases/latest revisions.
13. Historical comparison MUST distinguish difference from causality/quality claims.
14. Reproducibility MUST be assembled as a qualified current assessment rather than stored as universal Boolean truth.
15. Reproduction strength MUST NOT exceed the weakest unresolved material identity/dependency/nondeterminism/equivalence boundary.
16. Reproduction readiness MUST remain distinct from actual successful reproduction.
17. `absent`, `unknown`, `unavailable`, `withheld`, `invalid`, and `corrected/superseded` historical states MUST remain distinguishable.
18. External lineage/metadata systems MUST NOT become canonical SYNGAN authority merely through integration.
19. Provenance/Evidence/history control-plane state MUST remain bounded rather than scaling with every row/task/log by default.
20. Ordinary historical explanation/comparison/reproducibility assessment MUST NOT require full driver-local payload or telemetry collection.

## No new concept result

004-G does not introduce domain concepts for:

- Evidence Set;
- Finding Key / Evidence Slot;
- Claim Support;
- Provenance Edge;
- Lineage Graph;
- History;
- Historical View;
- Explain Plan;
- Comparison/Diff;
- Reproducibility Assessment;
- Reproduction Readiness;
- Metadata Graph;
- Query Projection;
- Completion Basis.

These are representation/query/coordination roles downstream of accepted concepts and the Reproducibility Contract.

## Deferred decisions

004-G intentionally does not settle:

- relational versus graph/document/event provenance storage;
- physical Evidence schema/serialization;
- exact typed finding-value class hierarchy;
- exact provenance relationship enum spelling;
- Evidence-slot/key encoding;
- query/index technology;
- graph query language;
- OpenLineage/MLflow/catalog integration details;
- report/dashboard/visualization format;
- provenance retention policy;
- detailed authorization/redaction mechanics;
- public SDK query method names;
- external export/import schemas;
- reproduction automation API.

## Consequences for later groups

### 004-H

Authorization/redaction must protect Evidence, diagnostics, dependency identities, Provenance qualifiers, historical indexes, and reproducibility-assessment inputs without falsifying historical existence or leaking sensitive detail through query indexes.

### 004-I

Platform integration must map external lineage/telemetry/catalog identities into adapter references without making those systems canonical semantic authority. Deployment architecture must support bounded query/index scale and optional integrations.

### 004-J

The architecture exit audit must verify consistency among control-plane transition atomicity, result promotion, runtime adapter results, Attempt fencing/idempotency, Evidence establishment, required Provenance recording, historical resolution, and security disclosure boundaries.

## Exit criteria

- [x] Evaluation runtime results separated from semantic Evidence establishment;
- [x] independently interpretable Evidence identity/cardinality architecture established;
- [x] retry-idempotent Evidence finding-slot semantics established;
- [x] immutable finding versus mutable applicability state separated;
- [x] bounded typed finding/claim-support/diagnostic-reference representation established;
- [x] Generation completion-basis binding architecture established;
- [x] canonical typed Provenance assertion model established;
- [x] provenance idempotency/correction/recoverable consistency established;
- [x] historical query read-composition layer established;
- [x] derived adjacency/search projection boundary established;
- [x] explain and historical comparison query semantics established;
- [x] difference-versus-causality boundary preserved;
- [x] reproducibility assessment assembler and strongest-defensible-class rule established;
- [x] reproduction readiness separated from actual reproduction success;
- [x] historical/current/applicability/availability/disclosure distinctions preserved;
- [x] external lineage integration kept non-authoritative;
- [x] enterprise-scale bounded-history/no-full-driver-materialization preserved;
- [x] no graph database, metadata god-concept, or universal reproducibility object selected.

## Exit assessment

**Status: complete.**

SYNGAN now has a coherent architecture for establishing durable Evidence from semantically valid Evaluation results, recording typed Provenance without duplicating canonical state, querying exact historical derivations and differences efficiently, and assembling current qualified reproducibility assessments from preserved historical facts.

## Next phase

**004-H — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture**
