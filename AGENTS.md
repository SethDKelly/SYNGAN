# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**Phase 007 architecture is complete and consolidated. Controlled implementation re-entry is approved for R0/008-A only. Feature implementation is not yet authorized.**

Start with:

- `docs/index.md`
- `docs/architecture/phase-007-consolidated-architecture-contract.md`
- `docs/authority/phase-007-consolidated-architecture-implementation-reentry-readiness-contract.md`
- `docs/phases/007/007-K-phase-007-consolidation-architecture-fitness-audit-evidence-review-implementation-reentry-readiness-decision.md`

Read 007-D through 007-J only as needed for detail.

Current progression:

```text
007-A..007-C  historical/provisional bootstrap work
007-D..007-J  DESIGN COMPLETE
007-K         COMPLETE — consolidation / re-entry decision
008-A / R0    NEXT ELIGIBLE after explicit proceed
R1+           NOT AUTHORIZED
```

Accepted counts remain 11 concepts / 15 synchronizations / 10 active ADRs. No `SYNC-16`.

## Primary design rule

> **Implementation realizes current design; historical implementation does not veto current design merely because it already exists or passes an old test.**

The existing `src/syngan`, tests, Import Linter rules and CI are retained feasibility/history artifacts from 007-B/007-C until R0 explicitly revalidates them.

## Current R0 / 008-A boundary

008-A is **not active merely because it is next eligible**. It requires an explicit proceed decision.

When active, its purpose is only:

**Implementation Re-entry Authority, Scaffold Reconciliation & Verification Re-baseline.**

### Agents may in 008-A

- reconcile/supersede historical Phase 007 implementation-authority documents;
- inspect every retained package/test/tool/fitness constraint against the Phase 007 consolidated architecture;
- retain, revise, relax or remove exact top-level package constraints after documented review;
- retain, revise, relax or remove Import Linter contracts based on durable dependency direction;
- update stale Phase 007 delivery-state fitness tests;
- re-baseline package/root-import/build smoke tests;
- revalidate current build/test/lint/type/fitness tool versions and the locked environment;
- update `pyproject.toml`, `uv.lock`, `tools/verify.py` and verification CI only when required for a truthful current gate;
- define narrowly scoped local-Spark socket/process test exceptions if later test plumbing requires them, without implementing Spark feature behavior;
- record current change classes, stop/reopen rules, waivers and evidence gates for the next tranche.

### Agents must not in 008-A

Do not:

- implement concept lifecycle/domain behavior;
- implement public resource/identity/reference APIs except changes strictly necessary to reconcile existing scaffold metadata;
- add persistence schemas/migrations;
- add source/output data-state representation;
- add Spark/DataFrame synthesis/runtime behavior;
- add Strategy/Learning/Generation/Evaluation algorithms;
- add dependency resolver/runtime plugin behavior;
- add IAM/secret/security-provider integration;
- add Execution/Attempt/fencing/recovery/checkpoint/admission behavior;
- add Evidence/Provenance/history/query/reproducibility/disclosure behavior;
- add platform/deployment adapters;
- add benchmarks/release qualification;
- implement the 007-J reference vertical slice.

Those require later explicit authorization.

## Known scaffold debt

R0 begins with at least these known facts:

- `tests/fitness/test_phase_007_authority_boundary.py` is stale and still asserts the historical 007-C-era progression in which 007-D is next;
- `tests/fitness/test_source_package_topology.py` makes the exact seven top-level package set and import-free root executable assertions that now require explicit architectural justification rather than automatic retention;
- `pyproject.toml` contains exact Import Linter contracts created before 007-D through 007-J;
- the development/tool version ranges are implementation choices to revalidate, not design authority;
- `main` was unprotected with no required status checks at the 007-K entry baseline, so do not claim required-check enforcement without current repository evidence.

## Durable architecture distinctions

Preserve at minimum:

- logical identity != semantic revision != mutable state version != representation schema version;
- handle/view != canonical state owner;
- persistence durability != semantic completion;
- CAS != semantic transition validation;
- exact historical reference != current/latest substitution;
- logical data subject != physical representation;
- physical schema/layout != Data Meaning/topology semantics;
- open/partial candidate != sealed whole subject != promoted logical output;
- semantic Strategy/method identity != implementation binding != package/model/runtime identity;
- dependency requirement != concrete resolution != integrity/trust != current authorization;
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
- historical reproducibility support != current reproduction feasibility != reproduction success;
- seed presence != exact deterministic reproduction;
- architecture-conformance proof != capability proof != runtime/platform-profile proof != resilience/adversarial proof != scale/release qualification;
- single-table proof != complete structured-data baseline support;
- Spark-local proof != distributed-cluster/managed-platform proof;
- learning-based reference path != mandatory Learning/Learned State lifecycle;
- small Spark fixture != enterprise-scale qualification.

## Complete baseline boundary

The complete structured-data target remains:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

The supported baseline also requires a source-derived/local free-form-text-capable path without mandatory pretrained model, public model hub, first-use model download or runtime inference service.

No early implementation may hard-code single-table or `fit/sample` assumptions that make the other required paths structurally impossible.

## Change classification after re-entry

Implementation must retain a stop/reopen discipline:

- local/non-contractual implementation maintenance may proceed inside the active tranche;
- public/persisted compatibility decisions require explicit tranche authority and compatibility analysis;
- architecture-affecting conflict stops ordinary implementation and reopens the smallest affected architecture authority;
- concept/synchronization/experience conflict stops ordinary implementation and reopens the smallest affected upstream design authority.

Passing code/tests does not override a Class 3/4 conflict.

## Progressive disclosure

For implementation-reentry work:

1. read `docs/index.md`;
2. read the Phase 007 consolidated architecture;
3. read the Phase 007 re-entry readiness contract;
4. read the active implementation subgroup authority;
5. read only the detailed 007-D through 007-J/concept/synchronization/experience documents directly relevant to the change;
6. use Phase 005/006/007-A..C history for rationale/feasibility evidence, not current authority.

Do not load or duplicate the full corpus by default.

## Current next boundary

**008-A — Implementation Re-entry Authority, Scaffold Reconciliation & Verification Re-baseline** is the next eligible tranche.

Do not begin 008-A until explicitly instructed to proceed. Do not begin R1 or any reference Strategy/vertical slice merely because 008-A becomes active.
