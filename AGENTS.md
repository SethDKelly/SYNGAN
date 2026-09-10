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
- `docs/phases/007/index.md`

Current progression:

```text
007-A..007-C  historical/provisional bootstrap work
007-D         DESIGN COMPLETE
007-E         DESIGN COMPLETE
007-F         DESIGN COMPLETE
007-G         DESIGN COMPLETE
007-H         DESIGN COMPLETE
007-I         next eligible DESIGN subgroup — not started
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
- add concrete public API classes merely to crystallize a hypothesis;
- add production serialization/wire/manifest/runtime-closure schemas;
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
- favorable empirical privacy Evidence != formal privacy guarantee != external release approval.

## 007-G design result

007-G is technology-neutral. It does **not** mandate Python Protocols/ABCs, entry points, a particular plugin catalog, Spark/PyTorch versions, package/environment distribution, containers, artifact registries, SBOM/signing systems, IAM/policy products, secret managers, firewalls/service meshes, or concrete runtime/security types.

A material Attempt binds one exact executable/dependency realization. Runtime may not hot-swap missing components. A later Attempt may use another compatible binding only when the unchanged semantic commitment permits implementation-neutral realization and the new realization is independently attributable.

## 007-H design result

007-H is likewise technology-neutral. It does **not** mandate a scheduler, queue, lease/lock service, fencing-token encoding, Attempt epoch encoding, recovery-frontier mechanism, checkpoint format, retry/backoff policy, idempotency store, admission algorithm, provider launcher, persistence schema, or concrete execution classes/enums.

Operational design must preserve stable Execution identity and distinguishable Attempts, operation-scoped idempotency, stale-writer fencing stronger than leases, a non-regressing authority frontier after potentially regressive restore, recovery quarantine/reconciliation, immutable checkpoint identity with contextual resume qualification, durable cancellation intent, and operational admission distinct from semantic readiness and write authority.

Earlier Phase 005-G concrete execution types, enums, integer epoch assumptions and package/repository layouts remain implementation-planning evidence to reconsider only after explicit implementation re-entry.

## Progressive disclosure

For design work:

1. read `docs/index.md`;
2. read the Phase 007 design-continuation/freeze authority;
3. read `docs/phases/007/index.md`;
4. read only the concepts/synchronizations/experience/architecture directly relevant to the active design question;
5. use phase/implementation history only for rationale/feasibility evidence.

Do not load or duplicate the full corpus by default.

## Current next boundary

**007-I — Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation** is the next eligible **design** subgroup.

Do not begin 007-I until explicitly requested. Do not resume production implementation unless a separate implementation-reentry decision is made.
