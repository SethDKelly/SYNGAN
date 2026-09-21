---
type: Architecture Authority
title: Phase 007-I Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation
status: active
---

# Phase 007-I — Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation

## Purpose

Refine SYNGAN's architecture for semantically valid Evaluation completion, durable Evidence establishment, typed Provenance, exact historical inspection, qualified reproducibility assessment, and actor-safe disclosure **without selecting an Evidence schema, graph/SQL engine, query language, report/UI format, authorization product, redaction technology, lineage integration, or executable verification implementation**.

007-I continues the architecture/design track governed by the [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md). It is design authority, not permission to implement Evidence/history/query behavior.

## Governing authority

007-I is downstream of:

- [Concept Design Methodology](../authority/design-methodology.md);
- [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md);
- [Evaluation](../concepts/evaluation.md);
- [Evidence](../concepts/evidence.md);
- [Provenance](../concepts/provenance.md);
- [Reproducibility Contract](../authority/reproducibility-contract.md);
- [Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract](../authority/privacy-disclosure-formal-guarantee-release-boundary-contract.md);
- [Phase 006 Recovery, Security, Degraded, Historical & Topology Experience Contract](../experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md);
- [Evaluation, Evidence & Review Experience](../experience/evaluation-evidence-review.md);
- [Provenance, Reproducibility & Historical Inspection Experience](../experience/provenance-reproducibility-historical-inspection.md);
- [007-D Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation](phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md);
- [007-E Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline](phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md);
- [007-F Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation](phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md);
- [007-G Strategy/Method Binding, Dependency Trust, Authorization, Secrets & Distributed Runtime Closure Foundation](phase-007-g-strategy-method-binding-dependency-trust-authorization-secrets-distributed-runtime-closure-foundation.md);
- [007-H Execution/Attempt, Idempotency, Fencing, Non-Regressing Recovery, Checkpoint, Cancellation & Admission Foundation](phase-007-h-execution-attempt-idempotency-fencing-non-regressing-recovery-checkpoint-cancellation-admission-foundation.md);
- [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](evaluation-evidence-provenance-reproducibility-historical-query.md);
- [Phase 006 Architecture Reconciliation Contract](phase-006-architecture-reconciliation-contract.md);
- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](../decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md);
- [ADR-0006 — Typed Canonical Provenance & Derived Historical Projections](../decisions/ADR-0006-typed-provenance-canonical-derived-history-projections.md);
- [ADR-0007 — Explicit Dependency Resolution & Scoped Capability Security](../decisions/ADR-0007-explicit-dependency-resolution-scoped-capability-security.md);
- [ADR-0009 — Non-Regressing Authority After Regressive Control-State Recovery](../decisions/ADR-0009-non-regressing-authority-after-regressive-control-state-recovery.md);
- accepted synchronizations, especially SYNC-09 through SYNC-15.

The historical Phase 005-H implementation plan remains downstream feasibility/planning evidence. Its concrete `EvidenceHandle`, finding schema, relational assertion table, `HistoricalRef`, query API, SQL transaction, index, enum, package-layout and cache choices are not architecture premises during the current design freeze.

## Design result

007-I accepts the following foundation:

> **Evaluation owns whether an examination was semantically valid. Evidence owns the durable finding that valid examination established. Provenance owns typed historical relationships. Historical query composes exact historical authority without becoming authority. Reproducibility is a qualified assessment over preserved historical facts and current conditions. Disclosure governs what an actor may observe; it never rewrites the underlying truth.**

> **Historical knowledge quality, historical reproducibility support, current reproduction feasibility, current Evidence applicability, current payload/dependency availability, and actor-visible disclosure are independent axes. They may influence one another's presentation but must not be collapsed into one status or Boolean.**

> **After regressive recovery, independently observed surviving material may support reconstruction or current-authority adoption, but physical existence alone does not establish missing Evidence, Provenance, semantic promotion, or historical completeness. Reconstructed facts remain attributable as reconstructed.**

Conceptually:

```text
committed Evaluation
        ↓
007-H Execution / Attempts
        ↓
non-final method/runtime result
        ↓
Evaluation semantic validation
        ↓
idempotent Evidence establishment
        ↓
immutable Evidence finding + separate current applicability
        ↓
required typed Provenance
        ↓
exact historical query composition
        ↓
qualified reproducibility assessment
        ↓
actor-safe disclosure projection
```

No later layer gains authority to strengthen an earlier layer's claim merely because it is convenient to query or present.

## 1. Architecture roles and non-concepts

007-I uses architecture/query roles equivalent to:

- Evaluation method/runtime result;
- normalized finding declaration;
- Evidence establishment operation;
- stable finding slot/key;
- claim-support descriptor;
- Evidence applicability projection;
- diagnostic reference;
- Generation completion basis;
- Provenance assertion;
- provenance relationship role/qualifier;
- provenance correction/supersession record;
- historical reference/resolution result;
- historical knowledge quality/basis;
- historical query/explain/comparison view;
- derived adjacency/search projection;
- reproducibility assessment;
- reproduction feasibility/readiness assessment;
- disclosure decision/field state/authorized summary;
- external lineage observation.

These are representation, coordination, query or security mechanisms.

007-I does **not** create domain concepts named `Evidence Set`, `Finding`, `Finding Slot`, `Claim Support`, `History`, `Lineage`, `Historical View`, `Metadata Graph`, `Reproducibility`, `Reproduction`, `Disclosure`, `Redaction`, `Report`, `Scorecard`, `Approval`, `Privacy`, `Release Decision`, or `Quality`.

## 2. Evaluation result and Evidence establishment

### 2.1 Runtime success is not Evidence

A runtime/method result is non-final operational material until Evaluation validates that the exact committed examination was realized.

Validation must be able to establish, where material:

- exact Evaluation identity and commitment snapshot;
- exact Criterion revision/question;
- exact subject and reference/baseline identities;
- exact method/configuration and 007-G executable realization used;
- achieved logical scope/coverage/sampling/approximation;
- topology/structural assertions required to interpret the subject;
- method assumptions and known limitations;
- uncertainty/error semantics;
- retry/recovery contribution semantics under 007-H;
- required diagnostic/support state;
- claim strength actually supportable by the result;
- required historical/dependency/runtime facts sufficiently known for interpretation.

A successful platform job, metric value, complete candidate, or readable diagnostic dataset cannot bypass this semantic validation.

### 2.2 Evidence establishment is owner-controlled

Only Evaluation/application authority may establish durable Evidence from a semantically valid Evaluation result.

Runtime adapters, external metric systems, dashboards, notebooks, lineage collectors and platform jobs may supply observations/results. They do not insert canonical Evidence directly merely because they observed computation.

### 2.3 One Evaluation may establish zero or more independent findings

The architecture supports zero or more independently interpretable Evidence resources per Evaluation.

A bounded establishment operation may coordinate several findings atomically or recoverably, but `Evidence Set` is not promoted into a domain concept.

### 2.4 Finding identity supports retry without over-specifying encoding

Repeated semantic normalization/establishment of the same Evaluation result must not create ambiguous duplicate Evidence.

Architecture therefore requires a stable finding identity/slot scoped strongly enough to distinguish the logical finding within the exact Evaluation result contract.

Its responsibility is equivalent to:

```text
exact Evaluation
+ logical finding role/slot
+ any additional exact subject/scope/result-role identity needed to prevent collision
```

The exact key format, namespace, fingerprint and persistence constraint remain deferred.

Equivalent replay resolves to the same logical Evidence finding. A materially conflicting replay for the same logical slot is an integrity/consistency conflict requiring reconciliation rather than overwrite.

### 2.5 Evidence establishment and Evaluation completion must not silently diverge

When Evaluation completion requires durable Evidence and required Provenance, architecture must make partial completion detectable and recoverable.

Where one atomic owner boundary can commit all required canonical facts together, it may do so. Where boundaries differ, durable intent/idempotent completion/reconciliation under 007-E is sufficient.

No universal distributed transaction is required; silent permanent divergence is prohibited.

## 3. Evidence finding semantics

### 3.1 Immutable finding versus current applicability

Evidence preserves immutable historical finding semantics separately from mutable current reliance/applicability.

The immutable finding must retain or reference enough context to interpret what was established, including where material:

- exact producing Evaluation;
- exact Criterion revision;
- exact subject/reference/baseline;
- finding/result semantics;
- logical scope/population/cohort/topology;
- method/configuration;
- coverage/sampling/approximation;
- uncertainty/error/confidence;
- assumptions and limitations;
- supported claim-strength boundary;
- relevant Data Meaning/Constraint/Condition context;
- diagnostic support references;
- implementation/runtime/dependency identities where materially interpretive;
- establishment/provenance relationships.

Current applicability may later become superseded, stale, inapplicable or invalidated without rewriting what the original finding said.

### 3.2 No universal score/pass model

Evidence representation must support differing finding forms without coercing all Evidence to one scalar or Boolean.

The architecture must preserve forms such as:

- satisfied/violated under an exact rule/scope;
- scalar/vector/statistical estimate with interpretation;
- interval or bound;
- comparison;
- threat-model-specific risk finding;
- indeterminate/inconclusive result;
- diagnostic/partial observation.

A generic summary may be provided, but it cannot erase the underlying finding semantics or imply comparability where none exists.

### 3.3 Claim support is bounded by the examination

A generic claim-support descriptor may summarize whether support is exhaustive/universal, deterministic bounded/certificate-backed, statistical, approximate/sketch, diagnostic/partial or indeterminate.

The descriptor is derived from the exact Criterion/method/scope/coverage/uncertainty context. It cannot strengthen the Evaluation's actual result.

### 3.4 Negative and indeterminate Evidence are legitimate

A valid Evaluation can establish unfavorable, violated, risky, degraded or inconclusive Evidence.

Evaluation success means the examination was validly performed. It does not mean the subject passed.

`indeterminate` remains a substantive Evidence outcome when the method cannot support a stronger answer; it must not be converted to favorable satisfaction for workflow convenience.

### 3.5 Large diagnostics remain separate

Violation records, nearest-neighbor results, attack traces, row-level observations, model predictions and other large diagnostic payloads remain separately referenced data-plane material.

Evidence retains bounded interpretive facts plus exact diagnostic references where those diagnostics materially support the finding.

Readable diagnostic bytes alone are not Evidence.

## 4. Generation completion basis

When Generation completion depends on Evidence, the owning Generation transition preserves an immutable bounded completion basis sufficient to identify:

- exact Generation/commitment;
- exact sealed candidate subject from 007-F;
- exact committed completion requirement/Constraint/Condition;
- exact Criterion revision;
- exact Evidence identities used;
- claim-strength requirement and achieved support;
- requirement-specific sufficiency determination;
- owner-state/fencing/idempotency basis where material.

This completion basis belongs to Generation promotion history, not Evidence.

Later Evidence may be related historically to the completed output, but it does not retroactively enter the original promotion basis.

Evidence cannot promote Generation by itself.

## 5. Privacy/disclosure Evidence boundary

Privacy/disclosure-risk Evidence remains ordinary Evidence with unusually important scope/claim constraints.

It must preserve the exact threat model, attacker assumptions, subject, reference, method, scope/coverage and uncertainty needed to interpret the result.

The architecture preserves these separations:

```text
empirical disclosure-risk Evidence
    != formal privacy guarantee
    != current disclosure authorization
    != external release/use approval
```

A favorable membership-inference, nearest-neighbor, duplication or other attack result cannot become a generic `private`, `anonymous`, `safe`, or `safe_to_release` property.

No initial-baseline differential-privacy accounting/guarantee fields are introduced. Future formal mechanism state with independent lifecycle/accounting still requires mechanism-specific concept discovery.

## 6. Provenance foundation

### 6.1 Provenance remains narrow typed relationship authority

Canonical Provenance stores typed historical assertions over exact stable references.

It does not duplicate canonical Evidence, Evaluation, Generation, Learning, Learned State, Data Meaning, Strategy, Constraint, Execution or dependency payloads into a universal graph.

A provenance assertion preserves or resolves enough information equivalent to:

```text
assertion identity
relationship meaning
exact subject reference
exact object reference
material role/qualifier context
originating transition/history basis
historical ordering/time context where useful
current assertion validity/correction state where applicable
representation schema context
```

This is a responsibility model, not a committed graph/table schema.

### 6.2 Relationship meaning remains typed

Architecture preserves distinctions equivalent to:

- bound/governed by;
- derived/produced by;
- used/depended on;
- evaluated/referenced;
- operationally realized by;
- recovered/resumed from;
- superseded/restricted/retired/invalidated context;
- reconstruction/adoption relationships where material to recovery history.

A generic `related_to` edge is insufficient where relationship meaning affects interpretation.

### 6.3 Provenance recording is idempotent and transition-bound

Required provenance may be retried physically. Its logical identity must be scoped to the exact originating material transition plus relationship role and exact historical references strongly enough to prevent duplicate or stale contradictory assertions.

The exact assertion-key encoding remains deferred.

### 6.4 Provenance correction is append/supersede

A wrong or incomplete provenance assertion is corrected through durable replacement/supersession/invalidation or equivalent audit-preserving representation.

Correction does not rewrite another concept's canonical history.

### 6.5 Reconstructed provenance remains epistemically attributable

After regressive recovery, a missing relationship may be reconstructed only when independent retained evidence proves the relationship strongly enough under the normal owning invariants.

Historical query must be able to distinguish:

```text
directly retained canonical assertion
reconstructed assertion with basis
partially supported relationship
unknown / not established
```

A surviving file, platform job, external lineage edge or provider event is evidence that may support reconstruction; it does not automatically become canonical Provenance.

## 7. Historical reference and resolution foundation

### 7.1 Exact historical target first

Historical inspection resolves the exact identity/revision/snapshot/representation that actually participated.

It must never silently substitute:

- current/latest semantic revision;
- current source alias target;
- newer Learned State;
- newer Evidence;
- replacement dependency/model/service;
- another output with superficially equivalent content.

### 7.2 Resolution state and historical knowledge quality are separate axes

007-I sharpens a distinction that earlier history APIs could otherwise collapse.

A reference may have an **object-resolution/disclosure state** equivalent to:

```text
resolved
absent
unknown / indeterminate
known identity but payload unavailable
invalid / integrity-defective
withheld / redacted / non-disclosing outward result
```

Separately, a historical fact/relationship may have a **knowledge basis/quality** equivalent to:

```text
directly retained canonical fact
reconstructed from sufficient independent evidence
partially known
unknown / occurrence not establishable
```

For example, a reconstructed relationship may resolve to a currently unavailable dependency. These dimensions must remain composable rather than one enum attempting to encode every combination.

### 7.3 Current annotations remain separate from historical truth

A historical view may additionally annotate current:

- lifecycle/applicability state;
- dependency/payload availability;
- authorization/disclosure state;
- reproduction feasibility;
- current alias/revision context.

Those annotations do not replace the historical binding.

### 7.4 Recovery gaps remain visible

After a restore or historical-data loss, a bounded historical interval may be incomplete even though older and newer facts resolve.

Historical query must be able to expose a gap/continuity limitation without fabricating that nothing happened during the interval.

## 8. Historical query composition

### 8.1 Query is a read-composition layer

Historical query composes:

- canonical typed Provenance assertions;
- exact resource/revision/commitment owners;
- Evidence findings/applicability;
- Execution/Attempt/recovery history;
- distributed representation references;
- dependency/runtime identities;
- derived indexes/projections where useful;
- current authorization/disclosure decisions.

It does not become the canonical owner of the underlying facts.

### 8.2 Explain is bounded progressive disclosure

An explain-style query begins from one exact target and returns a bounded material path rather than an unbounded graph dump.

Architecture supports controls such as relationship/materiality filters, direction, depth/breadth limits, pagination, optional Execution detail, current annotations, and explicit gap/disclosure states.

The exact public method names are deferred.

### 8.3 Historical comparison reports difference, not cause

A comparison resolves two exact historical targets and can categorize differences across source/input state, semantic authorities, Strategy/configuration, topology, Learned State, conditions, Evaluation Criteria/methods, dependencies/runtime, Attempts/recovery, Evidence, and physical representation where material.

Difference alone does not establish causality, superiority or quality. Those claims require explicit Evaluation/Evidence.

### 8.4 Query consistency must not be overstated

Exact immutable historical facts can be stable while current applicability, availability, policy and projections change during query assembly.

A historical/query view must therefore carry enough freshness/observation context to avoid implying one global atomic snapshot unless the provider actually supplies one.

A query may legitimately combine:

```text
exact immutable historical binding
+ current owner state observed at one version
+ projection observed at another generation
+ current disclosure decision
```

The architecture requires truthful observation boundaries, not universal cross-store serializability for every read.

### 8.5 Derived projections remain disposable/non-authoritative

Adjacency, search, denormalized history, graph, report or warehouse projections may accelerate traversal and presentation.

A projection miss does not prove historical absence. A stale projection does not override canonical Provenance/resource state. Projections must be rebuildable or repairable without changing historical authority.

## 9. Disclosure foundation

### 9.1 Disclosure is view-time/current authority

Authorization/disclosure determines what the current actor may observe or traverse.

It does not mutate canonical Evidence, Provenance, history, reproducibility facts or the underlying resource.

### 9.2 Field, relationship and graph-shape disclosure are all material

Protection may apply not only to field values but also to:

- resource existence;
- provenance relationship existence;
- endpoint identities;
- relationship qualifiers;
- diagnostic references;
- dependency/model/runtime identity;
- result counts;
- pagination/cardinality information;
- reverse traversal/incoming-edge discovery;
- comparison fields;
- reproducibility reason text/prerequisites;
- cached summaries/projections.

The query architecture must not leak protected graph shape merely because payload fields were redacted.

### 9.3 Existence-protected outward responses may be intentionally ambiguous

When policy protects existence, actor-facing results may intentionally avoid distinguishing absent from forbidden/withheld.

Internal canonical/security-audit state remains precise where policy permits.

This outward ambiguity is a disclosure behavior, not a change to historical truth.

### 9.4 Authorized summary is not the original value

An actor-safe summary/redacted representation is a derived view and must remain identifiable as such.

For example, revealing `diagnostic details withheld; bounded finding summary available` is not equivalent to serializing the missing diagnostic as `null` or claiming no diagnostic exists.

### 9.5 Disclosure is contextual and non-transitive

Permission to inspect one Evidence summary does not automatically grant access to its subject rows, diagnostics, source identity, model/dependency identity, reverse Provenance path or external platform logs.

Likewise, seeing one endpoint of a relationship does not automatically authorize disclosure of the other endpoint or the relationship itself.

### 9.6 Caches/projections must honor disclosure scope

A derived search/history/report cache may be shared physically only if it can serve actor-safe results without leaking protected existence/fields/path shape through cached data, counts or stale authorization.

A cached authorization/disclosure result cannot become permanent permission; current sensitive access is re-evaluated as required by 007-G.

## 10. Historical knowledge versus actor-visible knowledge

Canonical historical knowledge and one actor's visible knowledge are distinct.

The system may internally know an exact dependency/provenance relationship while an actor is authorized to see only a redacted summary or non-disclosing response.

Therefore:

```text
canonical fact withheld from actor
    != canonical fact missing
```

and:

```text
actor cannot inspect prerequisite
    != system has no prerequisite identity
```

Actor-facing explanations and reproducibility views must qualify what is withheld without converting canonical completeness into absence. When existence is protected, the outward response may remain intentionally less precise.

## 11. Reproducibility foundation

### 11.1 Reproducibility remains a derived contextual assessment

Reproducibility is assembled for one exact historical target and one declared reproduction/equivalence goal.

It is not a universal mutable property of the target and does not receive canonical authority merely because an assessment can be serialized or cached.

### 11.2 Separate historical supportability from current feasibility

007-I requires at least two independent assessment axes.

**Historical supportability** asks:

> Given the historical facts that can be established, what reproduction class can the record defensibly support?

It considers semantic commitments, exact identities, Strategy/method characteristics, dependency/runtime identity, randomness/nondeterminism, approximation/coverage, recovery facts, representation equivalence and historical knowledge gaps.

**Current feasibility** asks:

> Can an authorized actor/deployment attempt that reproduction now under current availability, trust, security, network, runtime and admission conditions?

A target may therefore be historically well-specified for statistical reproduction while current execution is blocked because an artifact is unavailable or current no-egress policy forbids a required service.

### 11.3 Historical support classes remain bounded

The accepted conceptual classes remain:

- exact deterministic;
- semantic;
- statistical;
- bounded/approximate;
- comparative;
- not reproducible / insufficient historical context.

The strongest-defensible-class rule applies: no stronger class than the weakest unresolved material identity, nondeterminism, approximation, equivalence or historical-knowledge boundary permits.

Seed presence alone never proves exact determinism.

### 11.4 Current feasibility remains a separate result

Current feasibility may be equivalent to:

- feasible;
- feasible with explicit limitations;
- queued/deferred by current admission/resource conditions;
- blocked by current authorization/dependency/network/runtime state;
- incompatible with the current environment;
- indeterminate because required current facts cannot be established.

These are current operational/actionability observations, not changes to the historical reproduction contract.

### 11.5 Actor-visible assessability is not canonical supportability

Disclosure adds another layer.

An actor may lack permission to see a material prerequisite or the reason a stronger reproduction class is unsupported. The outward assessment may therefore be redacted/withheld or intentionally non-disclosing.

That does not force the internal historical supportability assessment to pretend the prerequisite is missing. Conversely, a privileged internal assessment must not leak restricted facts through reason text or path structure.

### 11.6 Reconstructed/partial history constrains the claim

Reconstructed facts may legitimately support a reproduction claim when their basis establishes the required history strongly enough.

The assessment must remain able to explain that part of its basis was reconstructed rather than directly retained.

Partial/unknown history weakens the strongest defensible class where the missing fact is material. It is not repaired by substituting current/latest state.

### 11.7 Reproduction readiness is not reproduction success

A reproducibility assessment may conclude that a reproduction attempt is feasible.

Actual reproduction is new Learning/Generation/Evaluation work as appropriate. Where equality/equivalence is not guaranteed by construction, success is established through explicit Evaluation/Evidence under the declared equivalence Criterion.

A reproduction attempt never overwrites the historical target.

### 11.8 Cached assessments remain derived

A reproducibility assessment may be cached with target, input/basis identity and freshness context.

Changes in dependency availability, policy, current runtime capability, Provenance correction or newly discovered nondeterminism may change the current assessment without rewriting historical work.

A stale cached assessment cannot become semantic or security authority.

## 12. Regressive-recovery integration

007-H recovery and 007-I history compose as follows:

```text
potentially regressive restore
        ↓
current authority continuity unverified
        ↓
fresh non-regressing authority boundary
        ↓
reconcile surviving Execution/material/provider facts
        ↓
reconstruct/adopt only where normal owner proof is sufficient
        ↓
record reconstruction/recovery relationships
        ↓
historical query shows direct vs reconstructed vs gap/unknown
        ↓
reproducibility assessment uses strongest defensible history
```

Important consequences:

- absence from the restored store is not proof a later transition never occurred;
- surviving physical output is not proof Generation promoted;
- surviving diagnostic/method bytes are not proof Evidence was established;
- external lineage events are not proof canonical Provenance was recorded;
- reconstruction is performed by current authority and remains auditable;
- unresolvable gaps remain explicit and may limit reproducibility.

## 13. External lineage / metadata integration

External systems such as platform lineage collectors, metadata catalogs, observability tools, model registries or warehouses may receive or expose SYNGAN references through adapters.

They remain integrations/projections unless a future explicit authority contract says otherwise.

An external edge/event may be:

- a useful correlation;
- independent evidence during recovery/reconstruction;
- a source for a derived search/report projection;

but it cannot automatically become canonical SYNGAN Provenance or Evidence merely because it was emitted by a trusted platform.

Likewise, deletion or mutation of the external metadata record does not rewrite SYNGAN canonical history.

## 14. Scale and boundedness

Evidence/Provenance/history control state scales with material findings, relationships, activities, revisions, Attempts and summaries—not raw row count, file count, task count, tensor count or log volume by default.

007-I preserves enterprise-scale requirements including:

- topology-aware Evaluation without full output collection;
- bounded Evidence findings with distributed diagnostic references;
- no default Evidence record per row;
- no default Provenance edge per Spark task/file/row;
- indexed/bounded/paginated traversal rather than full graph materialization;
- summary-first explanation with drill-down;
- reproducibility assessment from stable references/manifests rather than bulk payload collection;
- no requirement to collect source/output/Learned-State payloads or complete telemetry into driver/coordinator memory.

Row-level lineage or exhaustive diagnostics may exist as explicitly scoped distributed data-plane material without becoming the canonical Provenance default.

## 15. Failure and integrity semantics

007-I does not freeze a public exception hierarchy.

Architecture must preserve enough structure to distinguish, where material:

- Evaluation result not semantically interpretable;
- claim-strength validation failure;
- Evidence finding replay conflict;
- partial/recoverable Evidence establishment;
- required Provenance pending/missing/conflicting;
- provenance correction/reconstruction conflict;
- exact historical reference unavailable/invalid;
- historical gap/partial knowledge;
- stale or incomplete query projection;
- actor-visible detail withheld/non-disclosing;
- reproducibility historical context insufficient;
- current reproduction blocked/incompatible/indeterminate;
- comparison only partially resolvable.

These conditions affect different owners and must not collapse into one generic `history failed` or `not reproducible` result.

## 16. Falsification scenarios reviewed

007-I was checked against at least these scenarios:

1. a platform Evaluation job succeeds but examined the wrong source/reference revision;
2. a valid exhaustive Evaluation finds violations;
3. a valid statistical Evaluation returns an interval crossing the required threshold;
4. Evidence establishment is retried after the caller loses the response;
5. the same logical finding slot is replayed with conflicting immutable content;
6. one Evaluation produces several independently meaningful findings;
7. Generation completed using Evidence E1 and later Evidence E2 is created;
8. a privacy attack Evaluation is favorable under one threat model but another threat was never evaluated;
9. detailed privacy diagnostics exist but the actor may see only a bounded summary;
10. policy protects the existence of a Provenance edge and reverse traversal could otherwise leak it;
11. a projection is stale and omits an assertion present canonically;
12. a historical dependency identity is known but its payload is no longer available;
13. a provenance assertion was reconstructed after regressive recovery;
14. a restore loses Evidence/Provenance rows while physical diagnostic/output material survives;
15. external lineage reports an edge not yet validated as canonical SYNGAN history;
16. a historical target supports statistical reproduction but current no-egress policy blocks the required service;
17. a privileged internal assessment knows a dependency identity that the current actor is not permitted to see;
18. a seed is retained while GPU/distributed nondeterminism prevents exact deterministic reproduction;
19. two outputs differ in Strategy and runtime but no Evaluation establishes which difference affected quality;
20. a multi-table/time-series privacy Evaluation covers only one constituent scope;
21. a historical query spans immutable facts plus current applicability/disclosure observations from different freshness boundaries;
22. a reconstructed historical relationship is sufficient for explanation but a separate missing runtime fact still limits reproduction strength.

The architecture remains coherent without a new concept, synchronization or ADR.

## 17. Architecture invariants

1. Runtime/platform Evaluation success does not establish Evidence.
2. Evidence may be established only from a semantically valid Evaluation over the exact committed subject/question/method context.
3. Repeated establishment of one logical finding must not create ambiguous duplicate Evidence.
4. Conflicting replay of one logical finding is not silently overwritten.
5. Evidence immutable finding semantics remain separate from mutable current applicability.
6. Evidence claim strength never exceeds method/scope/coverage/uncertainty support.
7. Negative/unfavorable Evidence from a valid Evaluation remains valid Evidence.
8. Indeterminate Evidence cannot be converted to favorable satisfaction automatically.
9. Large diagnostics remain separately referenced data-plane material by default.
10. Generation promotion preserves the exact Evidence/requirement/candidate basis used at completion.
11. Later Evidence does not retroactively enter an earlier Generation completion basis.
12. Privacy/disclosure Evidence remains threat-model/method/scope specific and does not become a formal privacy guarantee or release approval.
13. Provenance remains typed historical relationship authority and does not duplicate canonical resource payloads wholesale.
14. Required Provenance recording is idempotent and recoverably consistent with the transition it explains.
15. Provenance correction/reconstruction preserves auditability and cannot rewrite another concept's authority.
16. External lineage/metadata observation does not automatically become canonical Provenance or Evidence.
17. Historical queries resolve exact historical identity rather than current/latest substitutions.
18. Object-resolution state and historical-knowledge quality remain independently representable.
19. Directly retained, reconstructed, partial and unknown historical knowledge remain distinguishable where material.
20. Current applicability/availability/policy annotations do not rewrite historical bindings.
21. Query projections/indexes remain derived and non-authoritative.
22. Projection absence cannot establish canonical historical absence by itself.
23. Historical comparison reports difference without inventing causality/superiority claims.
24. Query composition does not imply one global atomic snapshot unless such a guarantee actually exists.
25. Disclosure/redaction is a current view decision and does not mutate canonical Evidence/Provenance/history.
26. Existence, graph shape, counts and reverse traversal may themselves be protected disclosure surfaces.
27. Authorized summaries remain identifiable as derived/redacted views rather than original canonical values.
28. Canonical historical knowledge and one actor's visible knowledge remain distinct.
29. Reproducibility is a contextual derived assessment, not a canonical Boolean/resource authority.
30. Historical reproducibility support and current reproduction feasibility remain separate axes.
31. Actor-visible assessability/disclosure does not redefine the internally supportable reproduction class.
32. Reproduction strength cannot exceed the weakest material historical identity/nondeterminism/approximation/equivalence/knowledge boundary.
33. Seed presence alone never establishes exact deterministic reproduction.
34. Reconstructed history may support a claim only to the strength its reconstruction basis actually establishes.
35. Current dependency/security/admission failure may block reproduction without rewriting historical supportability.
36. Reproduction readiness/feasibility is not reproduction success.
37. Actual reproduction is new domain work and never overwrites the historical target.
38. Regressive recovery cannot infer missing Evidence, Provenance or semantic promotion solely from surviving physical material.
39. Canonical Evidence/Provenance/history remains bounded rather than scaling with every row/task/log by default.
40. Ordinary historical/reproducibility/disclosure views do not require full source/output/state/diagnostic/telemetry materialization in driver/coordinator memory.

## 18. Phase 005-H implementation-planning disposition

007-I retains the responsibility intent of the Phase 005-H plan, including:

- Evaluation-owner Evidence establishment;
- independently identifiable Evidence findings;
- retry-idempotent finding identity;
- immutable finding versus mutable applicability separation;
- bounded claim-support/diagnostic-reference semantics;
- exact Generation completion basis;
- typed canonical Provenance over historical references;
- provenance idempotency and append/supersede correction;
- bounded historical explain/compare query composition;
- derived/non-authoritative query projections;
- qualified reproducibility assessment;
- disclosure/security seams across Evidence/history/reproducibility.

007-I reclassifies the following as implementation candidates rather than current architecture requirements:

- concrete `EvidenceHandle`, `EvidenceFinding`, `ClaimSupport`, `ProvenanceAssertion`, `HistoricalRef`, `ExplainView`, `HistoricalComparisonView`, `ReproducibilityAssessment` names;
- specific `ResourceKind` additions;
- relational SQL as the built-in canonical Evidence/Provenance store;
- SQLAlchemy/PostgreSQL transaction assumptions;
- binary assertion row shape and exact predicate enum spelling;
- unique `(evaluation_id, finding_slot)`-style constraints;
- exact index definitions;
- `client.history.*` API spelling;
- exact reproducibility/current-feasibility enums;
- specific `src/syngan/domain|ports|application|api|adapters` history package layout;
- concrete cache-key/fingerprint design;
- exact persistence normalization and migration shape.

The stronger 007-I requirements are authority separation, historical epistemic precision, actor-safe disclosure, and reproducibility qualification independent of any particular storage/query technology.

## 19. Explicitly deferred

007-I intentionally does not select:

- Evidence physical schema/serialization;
- finding-payload class hierarchy;
- finding-slot/idempotency-key encoding;
- relational/graph/document/event provenance storage;
- graph/query language;
- exact Provenance predicate enum/qualifier schema;
- query/index/search engine;
- projection technology/freshness protocol;
- report/dashboard/visualization format;
- public SDK/REST/CLI method names;
- authorization/RBAC/ABAC/policy engine;
- redaction/field-mask/tokenization technology;
- existence-protection transport/error encoding;
- lineage/catalog/MLflow/OpenLineage integration;
- reproducibility cache/storage technology;
- reproduction automation API;
- Evidence/Provenance retention defaults;
- diagnostic data format/storage;
- privacy attack implementation;
- formal differential-privacy mechanism/accounting;
- execution/evidence/history/reproducibility/disclosure tests or executable enforcement.

## 20. Repository change boundary

007-I changes architecture/documentation only.

It introduces:

- no Evidence/Evaluation/Provenance production source behavior;
- no persistence schema or migration;
- no graph/query/search/index implementation;
- no report/UI/API implementation;
- no lineage/metadata integration;
- no reproducibility engine/cache;
- no authorization/redaction implementation;
- no privacy mechanism;
- no new dependency;
- no new test;
- no Import Linter rule;
- no CI/deployment enforcement.

The retained Phase 007-A through 007-C executable scaffold remains provisional feasibility/history evidence.

## 21. Concept / synchronization / ADR audit

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
new concepts               0
new synchronizations       0
new ADRs                    0
SYNC-16                     absent
```

Finding-slot, claim-support, historical-knowledge quality, explain/comparison view, reproducibility assessment and disclosure state remain architecture/query mechanisms.

ADR-0002, ADR-0006, ADR-0007 and ADR-0009 remain sufficient. 007-I composes/refines their consequences rather than superseding them.

## 22. Exit decision

**007-I DESIGN: COMPLETE.**

**007-I IMPLEMENTATION: NOT AUTHORIZED.**

Before entering the previously named 007-J vertical-slice proof, its scope must be re-evaluated against the design-first freeze and the still-unresolved architecture-completion sequence.

The next eligible **design** subgroup is therefore:

**007-J — Reference Vertical-Slice Scope Re-evaluation, Architecture Completeness & Implementation-Proof Boundary**.

007-J remains design-only unless a later explicit implementation re-entry decision separately authorizes executable work.
