# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in architecture/design refinement and consolidation, not production implementation.**

Current design authority includes:

- `docs/authority/phase-007-design-continuation-implementation-freeze.md`
- `docs/architecture/phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md`
- `docs/architecture/phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md`
- `docs/architecture/phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md`
- `docs/architecture/phase-007-g-strategy-method-binding-dependency-trust-authorization-secrets-distributed-runtime-closure-foundation.md`
- `docs/architecture/phase-007-h-execution-attempt-idempotency-fencing-non-regressing-recovery-checkpoint-cancellation-admission-foundation.md`
- `docs/architecture/phase-007-i-evaluation-evidence-provenance-historical-query-reproducibility-disclosure-foundation.md`
- `docs/architecture/phase-007-j-reference-vertical-slice-scope-re-evaluation-architecture-completeness-implementation-proof-boundary.md`
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
007-J         DESIGN COMPLETE
007-K         next eligible consolidation/re-entry audit
implementation expansion   FROZEN
```

Accepted counts remain 11 concepts / 15 synchronizations / 10 ADRs. No `SYNC-16`.

## Primary rule

> **Design may invalidate provisional implementation; provisional implementation may not veto design.**

The existing `src/syngan`, tests, Import Linter rules and CI are retained feasibility/history artifacts from 007-B/007-C. They are not upstream architecture authority.

## What agents may do now

For an explicitly entered design/governance subgroup, agents may inspect directly relevant authority, create/refine architecture and consolidation documentation, compare alternatives, preserve unresolved implementation choices, record future verification obligations non-executably, update canonical navigation, and create an ADR only when a durable architecture choice genuinely needs separate rationale.

## What agents must not do during the design freeze

Unless implementation re-entry is explicitly authorized, do not:

- add production source behavior;
- add persistence/data-plane schemas or migrations;
- add Spark/runtime/model/platform/security adapters;
- add execution/recovery/fencing/checkpoint/admission implementations;
- add Evidence/Provenance/history/query/reproducibility/disclosure implementations;
- add reference Strategy or vertical-slice implementation merely because 007-J defined the proof boundary;
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
- persistence durability != semantic completion;
- exact historical reference != current/latest substitution;
- logical data subject != physical representation;
- physical schema/layout != Data Meaning;
- open/partial candidate != sealed whole subject != promoted logical output;
- semantic Strategy/method identity != implementation binding != package/model/runtime identity;
- dependency requirement != concrete resolution != trust/approval != current authorization;
- explicit provisioning/acquisition != material runtime execution;
- immutable Attempt invocation != live capability/secret credential;
- driver/coordinator readiness != distributed worker/runtime closure;
- missing dependencies must not trigger hidden package/model acquisition or remote fallback;
- implementation topology limitation != permission to simplify committed topology;
- Execution identity != platform job/run identity;
- Attempt observed physical state != current framework mutation authority;
- idempotency != fencing != authorization;
- lease/liveness evidence != stale-writer exclusion;
- restored control state/Attempt epoch != current post-restore authority;
- checkpoint durability != current resume eligibility != semantic result;
- cancellation request != terminal cancellation;
- admission != semantic readiness != queue placement != write authority;
- runtime Evaluation result != semantic Evaluation completion != Evidence establishment;
- Evidence immutable finding != current Evidence applicability;
- negative/indeterminate finding != Evaluation failure;
- privacy/disclosure Evidence != formal privacy guarantee != current disclosure authorization != external release approval;
- Provenance relationship authority != duplicated canonical owner state;
- object/reference resolution != historical knowledge quality;
- directly retained history != reconstructed history != partial/unknown history;
- projection/search absence != canonical historical absence;
- historical difference != causality/superiority/quality claim;
- disclosure/redaction != mutation of canonical history;
- canonical historical knowledge != actor-visible knowledge;
- historical reproducibility support != current reproduction feasibility;
- seed presence != exact deterministic reproduction;
- reproduction readiness != reproduction success;
- architecture-conformance proof != capability proof != runtime/platform-profile proof != resilience/adversarial proof != scale/release qualification;
- single-table proof != complete structured-data baseline support;
- Spark-local proof != cluster/runtime-closure or managed-platform proof;
- learning-based reference path != mandatory Learning/Learned State lifecycle;
- small Spark fixture != enterprise-scale qualification.

## 007-J design result

007-J is design/delivery-boundary authority, not executable proof authority.

It concludes that architecture through 007-I is complete enough to define controlled implementation evidence and recommends, after later re-entry, a self-contained learning-based single-table/Spark-local path as the first bounded user-visible reference proof.

That recommendation is intentionally narrow. Agents must not let the reference Strategy, its algorithm, one-table representation, Spark-local behavior or `fit/sample` flow become framework semantics.

Separate evidence remains required for:

- direct-generation neutrality;
- source-derived/local free-form-text support;
- time-series capability;
- multi-table shared-key capability;
- composite-topology representability;
- deterministic/bounded and statistical/approximate Evaluation forms;
- adversarial retry/fencing/recovery/cancellation/history/disclosure behavior;
- distributed worker runtime closure;
- managed/private platform guarantees where claimed;
- enterprise scale and release qualification.

## Provisional scaffold rule

The 007-B/007-C scaffold is not automatically retained unchanged at re-entry.

007-K/re-entry must explicitly reassess at least:

- exact top-level package set;
- Import Linter contracts;
- build/test/tool versions;
- root import restrictions;
- local Spark socket/process exceptions;
- fitness checks that encode historical phase state instead of durable architecture invariants.

## Progressive disclosure

For current work:

1. read `docs/index.md`;
2. read the Phase 007 design-continuation/freeze authority;
3. read `docs/phases/007/index.md`;
4. read 007-J for proof/claim boundaries when discussing implementation evidence;
5. read only the concepts/synchronizations/experience/architecture directly relevant to the active question;
6. use phase/implementation history only for rationale/feasibility evidence.

Do not load or duplicate the full corpus by default.

## Current next boundary

**007-K — Phase 007 Consolidation, Architecture-Fitness Audit, Evidence Review & Implementation-Reentry Readiness Decision** is the next eligible design/governance subgroup.

Do not resume production implementation, create the reference slice, or add executable conformance gates until 007-K explicitly decides re-entry and identifies the bounded authorized tranche.