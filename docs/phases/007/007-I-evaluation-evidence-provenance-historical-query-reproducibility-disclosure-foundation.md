---
type: Phase Record
title: 007-I — Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation
status: complete
---

# 007-I — Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation

## Objective

Refine the Evaluation-to-Evidence, Provenance, historical-query, reproducibility and disclosure architecture beneath 007-D through 007-H without allowing historical Phase 005-H planning or the provisional 007-A through 007-C scaffold to freeze Evidence types, relational/graph storage, query APIs, report formats, reproducibility objects, redaction technology or executable checks prematurely.

007-I remains architecture/design work under the Phase 007 implementation freeze.

## Governing authority reviewed

007-I reconciled and refined:

- `docs/concepts/evaluation.md`;
- `docs/concepts/evidence.md`;
- `docs/concepts/provenance.md`;
- `docs/authority/reproducibility-contract.md`;
- `docs/authority/privacy-disclosure-formal-guarantee-release-boundary-contract.md`;
- `docs/experience/evaluation-evidence-review.md`;
- `docs/experience/provenance-reproducibility-historical-inspection.md`;
- `docs/experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md`;
- 007-D through 007-H architecture authorities;
- `docs/architecture/evaluation-evidence-provenance-reproducibility-historical-query.md`;
- `docs/architecture/phase-006-architecture-reconciliation-contract.md`;
- ADR-0002, ADR-0006, ADR-0007 and ADR-0009;
- the historical Phase 005-H implementation plan as downstream feasibility/planning evidence.

## Result

**PASS — EVALUATION / EVIDENCE / PROVENANCE / HISTORICAL QUERY / REPRODUCIBILITY / DISCLOSURE FOUNDATION REFINED AS ARCHITECTURE DESIGN.**

Canonical result:

`docs/architecture/phase-007-i-evaluation-evidence-provenance-historical-query-reproducibility-disclosure-foundation.md`

## Core separation

007-I preserves this authority chain:

```text
committed Evaluation
        ↓
007-H Execution / Attempts
        ↓
non-final method result
        ↓
Evaluation semantic validation
        ↓
idempotent Evidence establishment
        ↓
immutable Evidence finding
        +
separate current applicability
        ↓
required typed Provenance
        ↓
exact historical query composition
        ↓
qualified reproducibility assessment
        ↓
actor-safe disclosure projection
```

Evaluation success, favorable Evidence, historical completeness, current applicability, current reproducibility feasibility and disclosure permission are not synonyms.

## Evaluation and Evidence

Runtime/platform success does not create Evidence.

Evidence establishment remains Evaluation-owner/application authority after validating the exact committed Criterion, subject/reference, method/configuration, scope/coverage, uncertainty, topology semantics, 007-G realization and 007-H retry/recovery contribution context.

One Evaluation may establish zero or more independently interpretable Evidence findings. Stable logical finding identity supports idempotent retry without requiring one concrete finding-key encoding yet.

Equivalent replay resolves to the same logical finding; conflicting immutable replay requires reconciliation rather than overwrite.

Evidence finding semantics remain immutable while current applicability may later be superseded, stale, inapplicable or invalidated.

Negative/unfavorable and indeterminate findings remain legitimate Evidence when the Evaluation itself was valid.

Large diagnostics remain separately referenced data-plane material.

## Generation completion basis

When Generation completion consumes Evidence, Generation retains an immutable bounded record of the exact candidate, completion requirement, Criterion, Evidence and sufficiency basis used at promotion.

Later Evidence does not retroactively enter that historical completion basis, and Evidence itself never owns Generation promotion.

## Privacy/disclosure Evidence

Privacy/disclosure-risk findings remain threat-model/method/scope/coverage/uncertainty specific.

007-I preserves:

```text
empirical disclosure Evidence
!= formal privacy guarantee
!= current disclosure authorization
!= external release/use approval
```

No generic privacy score or built-in differential-privacy accounting is introduced.

## Provenance

Provenance remains narrow typed historical relationship authority over exact references rather than a duplicated metadata graph.

Required assertions are transition-bound and idempotent. Corrections preserve auditability through append/supersede semantics.

After regressive recovery, reconstructed relationships remain distinguishable from directly retained canonical assertions. Surviving files, jobs, provider events and external lineage edges may support reconstruction but do not become canonical Provenance automatically.

## Historical resolution and knowledge quality

007-I explicitly separates object/reference resolution from historical knowledge quality.

Object-resolution/disclosure may be resolved, absent, unknown, unavailable, invalid or withheld/non-disclosing.

Historical knowledge may separately be directly retained, reconstructed from sufficient evidence, partially known or unknown.

Current applicability, payload availability, policy and reproduction feasibility are additional current annotations rather than rewritten historical truth.

Historical gaps after restore remain visible rather than being treated as proof that nothing happened.

## Historical query

Historical query remains a bounded read-composition layer over canonical owners and typed Provenance.

Explain/traversal is progressive, bounded and paginated rather than a default unbounded graph dump.

Historical comparison reports material differences without inferring causality, superiority or quality absent explicit Evaluation/Evidence.

Derived adjacency/search/warehouse/graph projections remain rebuildable and non-authoritative. Projection absence does not establish canonical historical absence.

Query responses must not imply one global atomic snapshot when immutable historical facts and current applicability/availability/disclosure observations were read at different freshness boundaries.

## Disclosure

Disclosure is current view-time authority and does not mutate canonical Evidence/Provenance/history.

Protection may apply to values, resource existence, relationship existence, graph shape, reverse traversal, endpoint identity, qualifiers, diagnostics, dependency/runtime identities, counts, pagination/cardinality and reproducibility reason text.

Existence-protected outward responses may intentionally avoid distinguishing absent from forbidden/withheld while internal audit remains more precise where permitted.

Authorized summaries/redacted views remain explicitly derived rather than masquerading as original canonical values.

Canonical historical knowledge and one actor's visible knowledge remain distinct.

## Reproducibility

Reproducibility remains a contextual derived assessment for one exact target and declared equivalence goal.

007-I separates:

```text
historical supportability
what reproduction class the preserved record can defend
```

from:

```text
current feasibility
whether reproduction can be attempted now under current dependency, authorization, network, runtime and admission conditions
```

and from actor-visible disclosure of that assessment.

Accepted support classes remain exact deterministic, semantic, statistical, bounded/approximate, comparative, and not reproducible/insufficient context.

Seed presence never proves exact determinism.

Reconstructed history may support only the strength its independent basis justifies. Partial/unknown material history constrains the strongest defensible class rather than being filled with current/latest state.

Current blocked reproduction does not rewrite a historically supportable class.

Actual reproduction remains new Learning/Generation/Evaluation work, with equivalence established through appropriate Evaluation/Evidence where not guaranteed by construction.

## Phase 005-H technology disposition

Earlier planning proposed concrete choices including:

- `EvidenceHandle`, `EvidenceFinding`, `ClaimSupport`, `ProvenanceAssertion`, `HistoricalRef`, `ExplainView`, `HistoricalComparisonView`, `ReproducibilityAssessment`;
- relational SQL canonical Evidence/Provenance storage;
- SQLAlchemy/PostgreSQL transaction assumptions;
- binary assertion rows and predicate enums;
- concrete finding-slot uniqueness constraints;
- exact traversal indexes and `client.history.*` API spelling;
- concrete history package structure and cache fingerprints.

007-I retains their responsibility intent but reclassifies those concrete names/technologies/shapes as implementation candidates to reassess at explicit implementation re-entry.

## Concept / synchronization / ADR audit

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
new concepts               0
new synchronizations       0
new ADRs                    0
SYNC-16                     absent
```

Finding slots, claim support, historical knowledge quality, query views, reproducibility assessment and disclosure state remain architecture/query mechanisms.

ADR-0002, ADR-0006, ADR-0007 and ADR-0009 remain sufficient.

## Explicitly deferred

007-I intentionally does not select:

- Evidence schema/serialization or finding class hierarchy;
- finding-slot/idempotency encoding;
- relational/graph/document/event Provenance persistence;
- exact predicate enum/qualifier schema;
- graph/query/search/index technology;
- public history/query API names;
- report/dashboard/visualization format;
- authorization/policy/redaction technology;
- existence-protection transport/error encoding;
- lineage/catalog/MLflow/OpenLineage integration;
- reproducibility cache/storage technology;
- reproduction automation API;
- Evidence/Provenance retention defaults;
- privacy attack implementations;
- formal differential-privacy mechanism/accounting;
- Evidence/history/reproducibility/disclosure tests or executable enforcement.

## Repository change boundary

007-I changes architecture/documentation only.

It introduces no production Evidence/Evaluation/Provenance source behavior, persistence schema, graph/query/search implementation, API/UI/report implementation, lineage integration, reproducibility engine, authorization/redaction behavior, privacy mechanism, dependency, test, Import Linter rule or CI/deployment enforcement.

The retained Phase 007-A through 007-C scaffold remains provisional implementation evidence.

## Exit decision

**007-I DESIGN: COMPLETE.**

**007-I IMPLEMENTATION: NOT AUTHORIZED.**

The previously named 007-J reference vertical-slice proof is not automatically eligible for implementation. Its scope must first be re-evaluated under the design-first freeze and against the architecture now completed through 007-I.

The next eligible **design** subgroup is:

**007-J — Reference Vertical-Slice Scope Re-evaluation, Architecture Completeness & Implementation-Proof Boundary**.

007-J does not begin automatically; explicit proceed authority is required. Production implementation remains frozen independently of design progression.
