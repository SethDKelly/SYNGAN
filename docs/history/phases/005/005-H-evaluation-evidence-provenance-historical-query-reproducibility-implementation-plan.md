---
type: Phase Record
title: 005-H — Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan
status: complete
---

# 005-H — Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan

## Objective

Translate the accepted 004-G Evidence/Provenance/history architecture plus the 005-D through 005-G exact control/data/runtime/operational facts into a concrete **future implementation plan** for Evidence establishment, canonical Provenance assertions, historical query projections and reproducibility assessment.

**No production implementation is authorized or performed by this phase.** Phase 005 remains planning-only and Jackson/design completeness remains a prerequisite to any later coding authority.

## Entry authority

005-H is downstream of:

- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](../../architecture/evaluation-evidence-provenance-reproducibility-historical-query.md);
- [005-B Verification Strategy](../../implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [005-D Public Resource/Control-Plane Plan](../../implementation/public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md);
- [005-E Spark Data Boundary Plan](../../implementation/spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md);
- [005-F Runtime/SPI/Learned-State Plan](../../implementation/strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md);
- [005-G Execution/Recovery Plan](../../implementation/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-plan.md).

## Canonical authority created

005-H establishes:

[Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan](../../implementation/evaluation-evidence-provenance-historical-query-reproducibility-plan.md).

## Planning-only/Jackson clarification

005-H creates no Evidence classes, SQL tables, migrations, Provenance graph/index, query service, reproducibility engine, tests, CI workflow or external lineage integration.

All resource roles, ports, persistence responsibilities and H1-H10 steps are future implementation contracts only.

Completion of Phase 005 must not be interpreted as automatic coding authorization. 005-K must explicitly decide whether the Jackson-style concept/synchronization/experience/architecture work is actually complete enough for implementation or whether another design-refinement phase is required.

## Core Evidence decisions

Accepted future rules include:

- `EvidenceHandle` uses the existing 005-D ResourceRef/handle model;
- runtime Evaluation output remains non-final and cannot insert Evidence directly;
- one Evaluation may establish zero or more independently identifiable Evidence resources;
- Evidence establishment is one Evaluation-owner atomic/recoverable operation;
- a stable method/result-contract finding slot plus exact Evaluation identity provides idempotent logical finding identity;
- replay of the same finding resolves to the same Evidence; conflicting content for the same slot is an integrity conflict;
- Evidence immutable finding content remains separate from mutable current applicability state;
- finding representation supports typed generic forms plus namespaced/versioned method-specific schemas rather than one universal score/Boolean;
- claim support remains bounded to exhaustive, deterministic-bounded, statistical, approximate or diagnostic strength and cannot be inflated by runtime code;
- large diagnostics remain exact distributed references;
- materially incorrect findings require invalidation/supersession and a new/corrected Evaluation/Evidence rather than in-place rewrite.

## Generation completion basis

005-H refines 005-E promotion history using a bounded immutable `GenerationCompletionBasis`/equivalent record tied to the exact promotion operation.

It preserves:

```text
Generation + commitment SnapshotId
exact SealedDataSnapshotRef
completion requirement slots
exact Constraint / Condition / Criterion refs
exact Evidence refs used
sufficiency/claim-strength determination
promotion authority/idempotency basis
established GenerationOutput ref
```

Later Evidence does not enter an already-established historical promotion basis retroactively.

## Canonical Provenance decisions

The first built-in implementation plans Provenance as indexed relational canonical assertions in the same 005-D SQL control-store family as other bounded control state.

No graph database is required for the first implementation and a graph/search store cannot become canonical authority.

A future canonical assertion is equivalent to:

```text
ProvenanceAssertion ResourceRef
subject exact HistoricalRef
predicate
object exact HistoricalRef
relationship slot / bounded qualifiers
originating transition or operation
assertion state
SchemaVersion
```

Typed predicate families preserve bound/governed, derived/produced, used/depended, evaluated/referenced, operational-realization, recovery/resume and supersession/restriction/retirement/invalidation meanings.

Assertions are idempotent by originating transition/relationship slot/predicate/exact endpoints.

Correction uses append/supersession plus current assertion state; it never destructively rewrites the original relationship or referenced canonical resources.

## Coupled transition consistency

Where the built-in SQL adapter owns both the canonical transition and required Provenance/Evidence control rows, the future implementation should use one relational transaction when the ownership transaction naturally coincides.

Examples include:

```text
Evaluation completion + Evidence + required Provenance
Learning -> Learned State + required Provenance
Generation promotion + completion basis + required Provenance
```

This transactional choice does not merge domain ownership into a generic metadata table.

External search/graph/lineage/reporting projections remain outside the canonical transaction and are fed by durable outbox/reconciliation.

Portable alternative persistence adapters may satisfy the same no-silent-gap invariant through durable intent rather than universal same-store ACID.

## Historical query decisions

Future public read surfaces are equivalent to:

```text
client.history.provenance(...)
client.history.explain(...)
client.history.compare(...)
client.history.reproducibility(...)
```

They return typed bounded views rather than one mutable graph object.

The first implementation can query canonical relational Provenance using inbound/outbound/predicate/origin indexes. Optional adjacency/search/materialized projections are rebuildable and non-authoritative.

Explain/traversal is depth/breadth limited and paginated. Historical comparison reports categorized structural differences and cannot infer causality or superiority without Evaluation/Evidence.

Historical exact facts remain separate from current applicability, payload availability, disclosure status and current reproducibility assessment.

## Resolution/freshness decisions

History views preserve:

```text
resolved
absent
unknown / indeterminate
unavailable
withheld / redacted
invalid
corrected / superseded
```

A projection miss does not prove absence unless canonical resolution establishes it.

Query responses preserve exact historical refs plus observed current StateVersion/projection freshness information where relevant instead of implying universal cross-store snapshot isolation.

005-I owns authorization/redaction policy and whether relationship existence itself may be disclosed.

## Reproducibility decisions

`ReproducibilityAssessment` is a derived view/cacheable computation, not a canonical Resource or Boolean flag.

It assembles exact historical facts from commitments, source/state/subject refs, semantic revisions, implementation/runtime/codec/dependency identities, randomness/approximation, 005-G Attempt/checkpoint/recovery history and current availability/security/network context.

It reports two independent dimensions:

1. strongest historically supportable reproduction class:

```text
exact_deterministic
semantic
statistical
bounded_or_approximate
comparative
not_reproducible
insufficient_context
```

2. current feasibility:

```text
feasible
feasible_with_limitations
blocked
indeterminate
```

Thus history can remain sufficient for statistical reproduction while current policy or missing artifacts block an attempt today.

A seed alone never proves exact deterministic reproduction.

Actually performing a reproduction is new domain work, and equivalence success requires appropriate Evaluation/Evidence.

## Scale decisions

Canonical Provenance scales with material semantic/operational relationships, not every row/file/task/heartbeat/log event.

Evidence remains bounded and references distributed diagnostics.

Normal explain/traversal/reproducibility assembly cannot require full source/output/Learned-State/diagnostic/graph materialization on the coordinator.

Detailed row-level lineage, if later required, remains separate distributed referenced material rather than default canonical edge volume.

## Persistence impact plan

Future bounded SQL responsibilities include equivalents of:

```text
evidence
evidence_finding
evidence_applicability
provenance_assertion
provenance_assertion_state
provenance_correction
generation_completion_basis
history/projection checkpoints when needed
```

They reuse 005-D ResourceRef/StateVersion/SchemaVersion/CAS/transaction/outbox/tombstone conventions.

No schema or migration is created during Phase 005.

## Security seam

005-H plans history/query contracts so 005-I can protect:

- Evidence finding/applicability content;
- canonical Provenance existence and endpoints;
- inbound/outbound traversal;
- reverse indexes;
- explain paths;
- comparison fields;
- projection counts/pagination;
- reproducibility prerequisites/reason text.

Withheld/redacted results remain distinct from absent/unknown/unavailable rather than fabricating history.

## Verification mapping

005-H primarily owns future V8 and directly maps:

```text
AF-08 idempotent Evidence/Provenance establishment
AF-09 runtime result != Evidence / semantic completion
AF-10 Provenance/query projection non-authority
AF-11 security-aware history/query seam
AF-16 typed applicability/resolution/disclosure states
AF-17 exact historical refs never silently resolve latest
AF-18 coupled transition/Provenance crash consistency
AF-19 Evaluation retry contribution deduplication
```

Required future scenarios include idempotent/conflicting finding replay, atomic multi-finding establishment, claim-strength rejection, immutable finding/applicability separation, exact diagnostic support, Provenance retry/correction, canonical-vs-projection disagreement, bounded explain traversal, non-causal comparison, distinct gap states, seed-vs-determinism, dependency disappearance, recovery-path reproducibility degradation and cached assessment staleness.

## Future implementation sequence

Only after a later explicit coding phase and a positive Jackson/design-completeness decision:

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

- 005-I — authorization, redaction/withholding, protected query/index semantics, dependency/artifact trust and no-egress enforcement;
- 005-J — concrete platform lineage/OpenLineage/MLflow/search integrations, deployment topology, performance and support matrices;
- 005-K — cross-slice integration audit, Jackson-methodology completeness decision, backlog closure and implementation-readiness exit.

## No upstream revision required

005-H requires no change to the eleven accepted concepts, fifteen synchronizations, Phase 003 experience contract, Phase 004 architecture/ADR set, or 005-C through 005-G implementation-planning authority.

No new architecture ADR is required.

## Exit criteria

- [x] planning-only/Jackson-completeness boundary preserved;
- [x] Evidence identity/establishment/idempotency plan defined;
- [x] immutable finding/applicability separation defined;
- [x] claim-support/finding representation plan defined;
- [x] exact diagnostic and Generation completion-basis plan defined;
- [x] canonical relational Provenance baseline defined;
- [x] typed assertion/idempotency/correction plan defined;
- [x] coupled transition consistency plan defined;
- [x] bounded history/explain/compare plan defined;
- [x] derived projection/freshness contract defined;
- [x] reproducibility historical-class/current-feasibility split defined;
- [x] security/redaction seams reserved;
- [x] scale/retention boundaries defined;
- [x] V8/fitness scenarios mapped;
- [x] H1-H10 future sequence defined without execution.

## Exit decision

**005-H — implementation plan complete; no production implementation performed and no coding authority granted.**

Next:

**005-I — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan**.
