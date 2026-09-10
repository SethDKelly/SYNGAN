# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in architecture/design refinement, not production implementation.**

Current design authority includes:

- `docs/authority/phase-007-design-continuation-implementation-freeze.md`
- `docs/architecture/phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md`
- `docs/architecture/phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md`
- `docs/architecture/phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md`
- `docs/architecture/phase-007-g-strategy-method-binding-dependency-trust-authorization-secrets-distributed-runtime-closure-foundation.md`
- `docs/architecture/phase-007-h-execution-attempt-idempotency-fencing-non-regressing-recovery-checkpoint-cancellation-admission-foundation.md`
- `docs/architecture/phase-007-i-evaluation-evidence-provenance-historical-query-reproducibility-disclosure-foundation.md`
- `docs/phases/007/index.md`

Current progression:

```text
007-A..007-C  historical/provisional bootstrap work
007-D         DESIGN COMPLETE
007-E         DESIGN COMPLETE
007-F         DESIGN COMPLETE
007-G         DESIGN COMPLETE
007-H         DESIGN COMPLETE
007-I         DESIGN COMPLETE
007-J         next eligible DESIGN subgroup — scope re-evaluation required
implementation expansion   FROZEN
```

Accepted counts remain 11 concepts / 15 synchronizations / 10 ADRs. No `SYNC-16`.

## Primary rule

> **Design may invalidate provisional implementation; provisional implementation may not veto design.**

The existing `src/syngan`, tests, Import Linter rules and CI are retained feasibility/history artifacts from 007-B/007-C. They are not upstream architecture authority.

## What agents may do now

For an explicitly entered design subgroup, agents may inspect directly relevant authority, create/refine architecture documentation, compare alternatives, preserve unresolved choices, record future verification obligations non-executably, update canonical navigation, and create an ADR only when a durable architecture choice genuinely needs separate rationale.

## What agents must not do during the design freeze

Unless later implementation re-entry explicitly authorizes it, do not:

- add production source behavior;
- add persistence/data-plane schemas or migrations;
- add Spark/runtime/model/platform/security adapters;
- add execution/recovery/fencing/checkpoint/admission implementations;
- add Evidence/Provenance/history/query/reproducibility/disclosure implementations;
- add concrete public API classes merely to crystallize a hypothesis;
- add production serialization/wire/manifest/runtime-closure/Evidence-history schemas;
- add runtime/build dependencies for future capability work;
- add new tests or executable architecture/fitness restrictions for evolving design;
- add Import Linter constraints for evolving design;
- add CI/deployment/release enforcement for evolving architecture.

Existing verification may continue. Its assertions are provisional where they encode earlier delivery-state assumptions; do not churn tests merely to mirror design-phase navigation.

## Current design distinctions

Preserve at minimum:

- logical identity != semantic revision != mutable state version != representation schema version;
- handle/view != canonical state owner;
- persistence durability != semantic completion;
- exact historical reference != current/latest substitution;
- migration revision != semantic/state/schema/recovery version;
- logical data subject != physical representation;
- exact per-scope source state != guaranteed coherent cross-scope snapshot;
- physical schema/layout != Data Meaning;
- open/partial candidate != sealed whole subject != promoted logical output;
- seal success != Constraint/Evaluation/privacy/Generation completion;
- semantic Strategy/method identity != implementation binding != package/model/runtime identity;
- one implementation binding may resolve multiple exact components/artifacts;
- dependency requirement != concrete resolution != integrity/authenticity != trust/approval != current authorization;
- installed/discovered extension != trusted/authorized executable code;
- explicit provisioning/acquisition != material runtime execution;
- immutable Attempt invocation != live capability/secret credential;
- runtime network capability != data-egress permission;
- commitment-time permission != current use-time authorization;
- driver/coordinator readiness != distributed worker/runtime closure;
- dynamic worker admission must preserve role-specific closure;
- missing dependencies must not trigger hidden package/model acquisition or remote fallback;
- secret values != canonical semantic/history/Provenance material;
- implementation topology limitation != permission to simplify committed topology;
- Execution identity != platform job/run identity;
- Attempt observed physical state != current framework mutation authority;
- provider retry count != Attempt identity/epoch by definition;
- idempotency != fencing != authorization;
- lease/liveness evidence != stale-writer exclusion;
- Attempt epoch != sufficient post-restore authority after potentially regressive recovery;
- restored control state != current mutation authority;
- non-regressing recovery frontier + current Attempt/resource authority may be required before writes resume;
- surviving immutable effect != revived producer authority;
- checkpoint durability != current resume eligibility != semantic result;
- cancellation request != terminal cancellation and cannot be erased by restoring older control state;
- admission != semantic readiness != queue placement != write authority;
- temporary resource scarcity != true runtime/semantic incompatibility;
- semantic completion != runtime/platform success;
- runtime Evaluation result != semantic Evaluation completion != Evidence establishment;
- Evidence immutable finding != current Evidence applicability;
- negative/indeterminate finding != Evaluation failure;
- Evidence != Generation promotion authority;
- privacy/disclosure Evidence != formal privacy guarantee != current disclosure authorization != external release approval;
- Provenance relationship authority != duplicated canonical owner state;
- object/reference resolution != historical knowledge quality;
- directly retained history != reconstructed history != partial/unknown history;
- current lifecycle/availability/policy annotation != historical binding;
- projection/search absence != canonical historical absence;
- historical difference != causality/superiority/quality claim;
- disclosure/redaction != mutation of canonical history;
- canonical historical knowledge != actor-visible knowledge;
- historical reproducibility support != current reproduction feasibility != actor-visible assessability;
- seed presence != exact deterministic reproduction;
- reproduction readiness != reproduction success.

## 007-G design result

007-G is technology-neutral. It does **not** mandate Python Protocols/ABCs, entry points, a particular plugin catalog, Spark/PyTorch versions, package/environment distribution, containers, artifact registries, SBOM/signing systems, IAM/policy products, secret managers, firewalls/service meshes, or concrete runtime/security types.

A material Attempt binds one exact executable/dependency realization. Runtime may not hot-swap missing components. A later Attempt may use another compatible binding only when the unchanged semantic commitment permits implementation-neutral realization and the new realization is independently attributable.

## 007-H design result

007-H is likewise technology-neutral. It does **not** mandate a scheduler, queue, lease/lock service, fencing-token encoding, Attempt epoch encoding, recovery-frontier mechanism, checkpoint format, retry/backoff policy, idempotency store, admission algorithm, provider launcher, persistence schema, or concrete execution classes/enums.

Operational design must preserve stable Execution identity and distinguishable Attempts, operation-scoped idempotency, stale-writer fencing stronger than leases, a non-regressing authority frontier after potentially regressive restore, recovery quarantine/reconciliation, immutable checkpoint identity with contextual resume qualification, durable cancellation intent, and operational admission distinct from semantic readiness and write authority.

## 007-I design result

007-I is technology-neutral. It does **not** mandate an Evidence schema, finding class hierarchy, finding-slot encoding, relational or graph Provenance store, query language/index engine, report/UI format, public history API, authorization/redaction product, lineage integration, reproducibility cache, or privacy mechanism.

Design must preserve Evaluation semantic validation before Evidence establishment; independently interpretable retry-idempotent findings; immutable findings separately from current applicability; typed canonical Provenance; directly retained/reconstructed/partial/unknown historical knowledge; exact bounded historical queries with derived non-authoritative projections; view-time disclosure including existence/graph-shape protection; historical reproducibility support separately from current feasibility and actor-visible assessability; and reproduction readiness separately from actual new reproduction work.

Earlier Phase 005-G/H concrete types, enums, SQL choices, package/repository layouts, query APIs and cache designs remain implementation-planning evidence to reconsider only after explicit implementation re-entry.

## Progressive disclosure

For design work:

1. read `docs/index.md`;
2. read the Phase 007 design-continuation/freeze authority;
3. read `docs/phases/007/index.md`;
4. read only the concepts/synchronizations/experience/architecture directly relevant to the active design question;
5. use phase/implementation history only for rationale/feasibility evidence.

Do not load or duplicate the full corpus by default.

## Current next boundary

**007-J — Reference Vertical-Slice Scope Re-evaluation, Architecture Completeness & Implementation-Proof Boundary** is the next eligible **design** subgroup.

Do not begin executable vertical-slice/proof implementation merely from the earlier 007-J name. 007-J must first be explicitly entered as design and re-evaluate the proof boundary. Do not resume production implementation unless a separate implementation-reentry decision is made.
