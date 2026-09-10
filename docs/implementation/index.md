---
type: Implementation Index
title: SYNGAN Implementation Planning & Delivery Authority
status: active
---

# SYNGAN Implementation Planning & Delivery Authority

## Current posture

Production implementation expansion is **frozen** under the [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md).

Phase 007-A through 007-C remain historical/provisional bootstrap work. Existing source/tests/tooling may remain for feasibility/history, but they do not constrain active architecture design.

Current implementation authorization state:

```text
007-A..007-C  retained historical/provisional scaffold
007-D and later  NOT AUTHORIZED FOR IMPLEMENTATION
```

No new production behavior, persistence/data-plane schema, serializer/manifest, public API class, Spark/runtime/model/security integration, dependency-acquisition mechanism, execution/recovery/fencing/checkpoint/admission mechanism, Evidence/Provenance/history/query/reproducibility/disclosure implementation, authorization/secret implementation, architecture-fitness restriction or CI enforcement is authorized while design continuation is active.

## Current architecture work

Completed design authorities:

- [007-D Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation](../architecture/phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md)
- [007-E Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline](../architecture/phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md)
- [007-F Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation](../architecture/phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md)
- [007-G Strategy/Method Binding, Dependency Trust, Authorization, Secrets & Distributed Runtime Closure Foundation](../architecture/phase-007-g-strategy-method-binding-dependency-trust-authorization-secrets-distributed-runtime-closure-foundation.md)
- [007-H Execution/Attempt, Idempotency, Fencing, Non-Regressing Recovery, Checkpoint, Cancellation & Admission Foundation](../architecture/phase-007-h-execution-attempt-idempotency-fencing-non-regressing-recovery-checkpoint-cancellation-admission-foundation.md)
- [007-I Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation](../architecture/phase-007-i-evaluation-evidence-provenance-historical-query-reproducibility-disclosure-foundation.md)

These documents introduce no implementation artifacts.

## Earlier concrete implementation choices are provisional

Historical Phase 005-D through 005-I planning selected candidates such as UUIDv4/JSON/SQLAlchemy/Alembic/PostgreSQL/SQLite/Psycopg, a PySpark/Parquet manifest profile, `typing.Protocol` runtime SPIs, Python entry-point discovery, named runtime/dependency/security/execution types, integer Attempt epochs, concrete package layouts, relational Evidence/Provenance storage, named history/query views and APIs, and `spark`/`torch` extras.

Under current architecture design:

- those choices remain useful feasibility/planning evidence;
- they are not current architecture requirements;
- they must be re-evaluated at implementation re-entry against the completed architecture and then-current ecosystem/deployment needs;
- no persistence/data/runtime/security/execution/Evidence/history/query/provider technology is currently authorized merely because Phase 005 planned it.

Current architecture requirements are expressed as responsibilities/invariants instead: exact logical identity, owner-controlled persistence, exact source/data-state representation, candidate/seal/promotion separation, semantic Strategy versus executable binding separation, explicit dependency/trust/authorization boundaries, use-time secret handling, role-specific distributed runtime closure, stable Execution/Attempt history, non-regressing recovery authority, operation-scoped idempotency, fenced canonical effects, qualified checkpoint reuse, durable cancellation intent, distinct operational admission, Evaluation-owner Evidence establishment, immutable findings with separate applicability, typed Provenance, exact historical knowledge, disclosure-safe query composition and qualified reproducibility.

## 007-G implementation consequences for later re-entry

Any future implementation must preserve at least:

- Strategy/method semantic identity separately from implementation binding/package/runtime identity;
- exact material implementation/dependency closure per Attempt;
- no silent dependency/component substitution inside an Attempt;
- explicit acquisition outside runtime execution;
- independent identity/integrity/trust/compatibility/authorization assessment;
- current action-specific authorization rather than permanent permission embedded in semantic commitments;
- bounded runtime capabilities instead of ambient canonical-store/network authority;
- secret references/requirements without persisting secret values in semantic/history/provenance records;
- role-specific distributed closure for all material workers, including dynamic workers;
- large state/model/artifact loading without universal driver broadcast;
- explicit topology/runtime limitations rather than semantic simplification;
- the self-contained source-derived text baseline without mandatory remote model/service dependencies.

## 007-H implementation consequences for later re-entry

Any future execution/recovery implementation must also preserve at least:

- stable Execution identity distinct from provider job/run identity;
- distinguishable Attempt history without equating provider retries to Attempt identity mechanically;
- Attempt observed physical state distinct from current mutation authority;
- operation-scoped idempotency that never bypasses current fences or authorization;
- fencing stronger than lease/liveness evidence;
- a non-regressing recovery-authority boundary strong enough that restored control state cannot resurrect old writer authority;
- recovery quarantine and reconciliation before ordinary writes after potentially regressive restore;
- surviving immutable effect adoption by current authority rather than revival of the producer;
- checkpoint integrity/identity distinct from current resume compatibility;
- cancellation intent that blocks ordinary new admission and survives restore semantics;
- admission distinct from semantic readiness, authorization, queue placement and write authority;
- capacity shortage distinct from permanent incompatibility;
- at-least-once physical realization with at-most-one authoritative semantic result transition.

## 007-I implementation consequences for later re-entry

Any future Evaluation/Evidence/history implementation must preserve at least:

- runtime/method output separately from Evaluation semantic validation and Evidence establishment;
- Evaluation-owner Evidence establishment against the exact committed Criterion, subject/reference, method, scope/coverage, uncertainty and material runtime/recovery context;
- independently interpretable logical findings with retry-idempotent identity and explicit conflict detection;
- immutable Evidence finding semantics separately from mutable current applicability;
- negative/unfavorable and indeterminate findings as legitimate Evidence when the examination is valid;
- exact immutable Generation completion basis identifying the candidate, requirement, Criterion and Evidence used at promotion;
- typed canonical Provenance over exact historical references without copying canonical owner payloads into a metadata graph;
- directly retained, reconstructed, partial and unknown historical knowledge as distinct states/bases;
- object/reference resolution separately from historical-knowledge quality;
- exact bounded explain/compare query composition with derived non-authoritative projections;
- projection absence never treated as proof of canonical historical absence;
- disclosure that can protect existence, relationship shape, reverse traversal, counts/cardinality and reason text as well as values;
- canonical historical knowledge separately from one actor's visible knowledge;
- historical reproducibility support separately from current reproduction feasibility and actor-visible assessability;
- strongest-defensible reproduction class constrained by actual identity, nondeterminism, approximation, equivalence and historical-knowledge limits;
- reproduction readiness separately from actual new reproduction work/equivalence Evidence.

The exact Evidence classes/findings, relational or graph persistence, SQL transaction design, query/index engine, public history API, redaction/policy mechanism, lineage integration, reproducibility cache, execution package layout, scheduler/queue, recovery-frontier mechanism, checkpoint format and other concrete technologies remain open implementation choices.

## Re-entry condition

Implementation may resume only after an explicit design-completion/re-entry decision identifies:

- current architecture authority;
- which provisional 007-A through 007-C choices remain compatible;
- which retained source/tests need revision/removal;
- which executable guardrails are justified;
- which bounded production subgroup is authorized next.

No phase number, earlier implementation-plan label, reference-slice name or green test suite substitutes for that decision.

## Current next boundary

The next active work is design, not implementation:

**007-J — Reference Vertical-Slice Scope Re-evaluation, Architecture Completeness & Implementation-Proof Boundary**.

007-J must first reassess whether and how a reference proof should exist without hard-coding single-table bias or bypassing the design/re-entry gate. No executable reference slice is authorized merely by entering 007-J.
