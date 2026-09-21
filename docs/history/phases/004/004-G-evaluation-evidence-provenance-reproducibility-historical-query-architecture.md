---
type: Phase Record
title: 004-G — Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture
status: complete
---

# 004-G — Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture

## Objective

Translate Phase 002 Evaluation/Evidence/Provenance semantics, the Phase 003 review/historical-inspection experience, and the Phase 004 identity/runtime/recovery architecture into an implementation-facing evidence/history/query architecture that remains bounded, exact-reference based, idempotent, and non-duplicative.

004-G must make Evaluation-result interpretation, Evidence establishment, Generation completion Evidence binding, typed Provenance recording, historical explanation/comparison, and reproducibility assessment implementable without creating a universal Quality/Metadata/Lineage/Reproducibility god-object or selecting a graph database prematurely.

## Governing authority

- [Evaluation](../../concepts/evaluation.md)
- [Evidence](../../concepts/evidence.md)
- [Provenance](../../concepts/provenance.md)
- [Reproducibility Contract](../../authority/reproducibility-contract.md)
- [Evaluation, Evidence & Review Experience](../../experience/evaluation-evidence-review.md)
- [Provenance, Reproducibility & Historical Inspection Experience](../../experience/provenance-reproducibility-historical-inspection.md)
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md)
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](../../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md)

## Canonical architecture created

- [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](../../architecture/evaluation-evidence-provenance-reproducibility-historical-query.md)

## ADR created

- [ADR-0006 — Typed Canonical Provenance & Derived Historical Projections](../../decisions/ADR-0006-typed-provenance-canonical-derived-history-projections.md)

## Main decisions

### 1. Evaluation runtime results remain non-final until semantic validation

Runtime result envelopes are normalized only after Evaluation/application logic verifies exact Criterion, subject/reference, method/configuration, coverage, assumptions, uncertainty, and claim-strength support.

Runtime success/metric output does not establish Evidence directly.

### 2. Evidence establishment is owner-side and idempotent

One semantically valid Evaluation may establish zero or more independently interpretable Evidence resources.

A stable Evaluation-scoped finding slot/key prevents retries or repeated normalization from creating ambiguous duplicate Evidence.

Equivalent repeated establishment resolves to the same Evidence; conflicting content for an established slot is a consistency defect.

### 3. Evidence finding semantics are immutable

Evidence preserves the historical finding and interpretation context immutably.

Current applicability states such as applicable, superseded, stale, inapplicable, or invalidated remain separate conflict-versioned lifecycle/applicability state.

Materially correcting a finding requires invalidation/new Evaluation/new Evidence as appropriate rather than in-place rewrite.

### 4. Evidence representation remains typed and multidimensional

Evidence cannot collapse universally to `score`, `passed`, or `quality`.

Architecture permits typed finding forms, bounded claim-support descriptors, uncertainty, assumptions, limitations, and separately referenced large diagnostics.

### 5. Generation promotion preserves exact completion Evidence basis

When Evidence participates in Generation completion, promotion history binds the exact Generation, sealed candidate, committed requirement, Criterion, Evidence identity, and sufficiency determination used at that time.

Later Evidence cannot enter the historical promotion basis retroactively.

### 6. Provenance is a canonical typed relationship assertion layer

Provenance stores typed assertions over stable references, with relationship identity, subject/object refs, relationship meaning, qualifiers, originating transition, historical context, and correction/supersession state.

It does not copy canonical concept/result payloads.

### 7. Provenance recording is idempotent

Retries of the transition that requires Provenance must not create ambiguous duplicate edges.

Assertion idempotency is scoped to originating transition + relationship role + exact historical refs.

Conflicting content is a consistency defect rather than last-writer-wins.

### 8. Provenance correction is append/supersede

Corrections preserve auditability and do not authorize rewriting another concept's historical authority.

### 9. Required Provenance and material transitions are recoverably coupled

Learning→Learned State, Generation→output, Evaluation→Evidence, and completion-Evidence relationships cannot silently diverge.

004-G does not mandate one distributed transaction; same-store ACID, outbox, durable intent, pending/reconciliation, or another recoverable consistency mechanism may comply.

### 10. Historical query is a read-composition layer

Explain/traverse/compare queries compose canonical resources, canonical Provenance, exact snapshots/revisions, Evidence applicability, Execution history, dependency identities, and derived indexes.

The query service does not own the underlying state.

### 11. Query indexes are derived projections

Outgoing/incoming adjacency, relationship-type indexes, resource/time indexes, Evidence/subject/promotion-use indexes, and dependency/recovery indexes may improve query performance.

They can be rebuildable/eventually consistent, and correctness-sensitive historical verification can fall back to canonical state rather than silently trusting stale projections.

### 12. Explain queries are bounded/progressively disclosed

Historical explanation starts from a stable target and traverses typed material relationships with depth limits, materiality filters, pagination, current-state annotations, and explicit gap/withheld/unavailable states instead of returning an unbounded graph dump.

### 13. Historical comparison is structural, not causal

Comparison resolves two exact historical paths and classifies material differences across source, semantic revisions, Strategy, Learned State, Conditions, methods, dependencies, runtime/recovery, Evidence, and representation where relevant.

Difference does not imply causality, quality, or superiority without Evaluation/Evidence.

### 14. Reproducibility is assembled as current assessment

A reproducibility assessor combines the target's historical bindings, dependencies, implementation/runtime identities, randomness, approximation, representation equivalence, and material recovery facts.

It returns the strongest defensible accepted class and why stronger classes are unsupported.

No canonical `reproducible=true` state is introduced.

### 15. Reproduction readiness differs from successful reproduction

Sufficient retained context can mean an attempt is possible. Actual reproduction success requires new domain work and, where needed, explicit equivalence Evaluation/Evidence.

### 16. Historical fact/current state/availability/disclosure/reproducibility remain distinct

A historical dependency can be precisely known, currently unavailable, withheld from a particular actor, and therefore limit current reproducibility without changing the historical relationship.

### 17. Resolution states remain typed

`absent`, `unknown`, `unavailable`, `withheld/redacted`, `invalid`, and `corrected/superseded` cannot collapse into generic null/missing state.

### 18. External lineage systems remain integrations

OpenLineage/MLflow/catalog/platform lineage may be exported to or consulted by adapters, but observed external edges do not automatically become canonical SYNGAN semantic Provenance.

### 19. Authorization must compose with query/index architecture

004-H must prevent sensitive historical/index data from leaking while preserving truthful withheld-versus-unknown semantics.

### 20. History remains bounded at enterprise scale

Canonical Provenance/Evidence/query state scales with material resources/revisions/transitions/Attempts/findings/relationships rather than source/output rows, every diagnostic record, every Spark task, or every log line.

## Alternatives rejected as universal architecture

- runtime result envelope directly equals Evidence;
- one generic scalar Quality/Pass result;
- one Evidence record per Evaluation regardless of independent finding semantics;
- duplicate Evidence creation on every retry;
- mutable in-place Evidence findings;
- one master metadata/lineage graph containing copied canonical state;
- reconstructing canonical state from Provenance;
- external lineage/catalog authority as SYNGAN canonical truth;
- mandatory graph database;
- mutable global `reproducible` Boolean/status;
- historical comparison that infers causality from differences;
- full payload/log/task collection for historical query.

## Architecture consequences for later groups

### 004-H

Authorization/redaction must protect Evidence payload/context, diagnostic refs, dependency identities, Provenance relationship detail, query indexes, and reproducibility assessment inputs without falsifying historical existence or creating index side channels.

### 004-I

Platform integration must map external lineage/catalog/telemetry identities through adapters and support query/index scale without transferring canonical semantic authority to those platforms.

### 004-J

Exit audit must verify coupled consistency across Evidence establishment, Provenance recording, semantic promotion, Attempt idempotency, exact historical resolution, derived projections, and security disclosure.

## No new concept result

004-G does not introduce domain concepts for:

- Evidence Set;
- Evidence Slot / Finding Key;
- Claim Support;
- Provenance Edge;
- Lineage Graph;
- History;
- Explain Plan;
- Historical Diff;
- Reproducibility Assessment;
- Reproduction Readiness;
- Query Projection;
- Completion Basis;
- Metadata Graph.

These are representation, query, coordination, or derived-assessment roles downstream of accepted concepts.

## Deferred decisions

004-G intentionally does not settle:

- graph vs relational/document/event persistence;
- Evidence serialization/class hierarchy;
- finding-slot encoding;
- exact provenance relationship enum spelling;
- historical query/index engine;
- public query API names;
- report/dashboard visualization;
- OpenLineage/MLflow/catalog mapping;
- provenance retention policy;
- authorization/redaction implementation;
- reproduction automation workflow/API.

## Exit criteria

- [x] Evaluation runtime result versus Evidence boundary established;
- [x] idempotent multi-Evidence establishment architecture established;
- [x] immutable finding/current applicability split established;
- [x] typed finding/claim-support/diagnostic-reference boundary established;
- [x] exact Generation completion-Evidence basis established;
- [x] canonical typed Provenance assertion architecture established;
- [x] provenance idempotency and correction semantics established;
- [x] recoverable transition/provenance consistency established;
- [x] historical explain/query composition architecture established;
- [x] derived index/projection boundary established;
- [x] historical comparison/difference-no-causality boundary established;
- [x] reproducibility assessment architecture established;
- [x] reproduction readiness versus actual reproduction separated;
- [x] historical/current/availability/disclosure distinctions preserved;
- [x] external lineage integrations kept non-authoritative;
- [x] enterprise-scale bounded history preserved;
- [x] ADR rationale recorded.

## Exit assessment

**Status: complete.**

SYNGAN now has an implementation-facing architecture for durable Evidence, typed non-duplicative Provenance, exact historical explanation/comparison, and qualified current reproducibility assessment that composes with the prior identity, distributed data, runtime adapter, and recovery/fencing architecture.

## Next phase

**004-H — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture**
