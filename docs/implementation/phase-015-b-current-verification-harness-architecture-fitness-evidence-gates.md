
---
type: Implementation Authority
title: 015-B — Current Verification Harness, Architecture-Fitness & Evidence-Gate Foundation
status: active-current
---

# 015-B — Current Verification Harness, Architecture-Fitness & Evidence-Gate Foundation

## Purpose

Establish the **current** Phase 015 verification authority from completed Phase 013/014 design and the reconciled 015-A repository baseline.

015-B does not implement product/domain behavior. It defines and enforces the harness through which later slices prove that their implementation preserves already-accepted authority.

The governing rule is:

> A verification oracle comes from current design/architecture authority, not from current code, provider behavior, historical Phase 005 expectations, or a previously captured output.

## Authorized scope

015-B may:

- define current verification lanes and quality gates;
- normalize test markers/profiles;
- add authority/static architecture-fitness checks;
- normalize repository verification commands;
- define failure/security/provider/scale/stochastic test entry semantics;
- define slice acceptance-evidence requirements;
- demote superseded historical verification authority;
- add non-domain harness/configuration/tests needed to protect those rules.

015-B may not implement concept state/actions, persistence, distributed data, Strategy/runtime behavior, Execution/recovery behavior, Evaluation/Evidence/Provenance behavior, authorization/provider behavior, or scale features.

## Governing current authority

Primary inputs:

- Phase 013 Consolidated Architecture Contract;
- Phase 014-F adversarial whole-design audit;
- Phase 014-G residual readiness register;
- Phase 014-H R2/R3 decision;
- Phase 015 Start Gate;
- completed 015-A baseline reconciliation.

The historical Phase 005 verification strategy remains useful scenario/rationale evidence only and is not current implementation authority.

## Verification principles

### VP-01 — authority-derived oracle

Tests protect current authority. They do not bless current implementation merely because it exists.

### VP-02 — strongest relevant seam

A test must exercise the seam where the protected property can actually fail.

A fake or unit test may support a property, but it cannot replace required persistence, distributed, provider, failure, or security conformance evidence.

### VP-03 — current lane activation

A verification lane may be defined before implementation exists, but it is not considered satisfied by placeholder tests.

A later slice activates the lanes relevant to its implemented responsibilities.

### VP-04 — default-deny portable network posture

Portable/core verification denies outbound sockets by default.

Explicit network/service tests require an opt-in marker/profile and must not become a hidden prerequisite of portable verification.

### VP-05 — deterministic before stochastic

Identity, lifecycle, ownership, recovery authority, authorization, serialization and other deterministic contracts use deterministic oracles.

Statistical/stochastic behavior declares its hypothesis, fixture/profile, seed policy, threshold/confidence rule and failure interpretation before execution.

### VP-06 — support claims follow evidence

Architecture compatibility, implementation, conformance verification and scale qualification remain distinct.

A provider/profile/support claim cannot exceed its retained verification evidence.

### VP-07 — delivery evidence is not domain Evidence

CI/run/fixture/benchmark records are implementation delivery evidence. They must not be confused with the accepted SYNGAN Evidence concept.

## Current verification lanes

### C0 — authority / repository / static architecture

**ACTIVE NOW.**

Protects:

- current authority discoverability and slice gating;
- repository/toolchain consistency;
- packaging/import integrity;
- inward responsibility boundaries;
- no generic hidden-owner package;
- no production-to-test dependency;
- no eager outer/provider integration from the root package;
- default-deny portable network posture;
- active synchronization/status assumptions in executable gates.

C0 may execute before domain implementation exists.

### C1 — semantic / unit / state-machine

**DEFINED; activated by 015-C/015-E/015-G responsibilities.**

Protects owner semantics, lifecycle transitions, application-family optionality, direct vs Learned-State-assisted Generation, Evaluation/Evidence cardinality and historical/current distinctions.

### C2 — persistence / concurrency / migration

**DEFINED; activated by 015-C.**

Protects stable logical identity, distinct version axes, exact historical binding, CAS/transaction invariants, migration neutrality and owner-history immutability.

### C3 — distributed data / topology / physical closure

**DEFINED; activated by 015-D.**

Protects exact physical subject boundaries, structured topology, candidate/seal/finality separation and no mandatory full-driver materialization.

### C4 — runtime / dependency / no-egress

**DEFINED; activated by 015-E and strengthened by 015-H.**

Protects Strategy/binding distinction, dependency identity/trust/compatibility, role-specific runtime closure and absence of hidden acquisition/hosted fallback.

### C5 — Execution / failure / recovery

**DEFINED; activated by 015-F.**

Protects stable Execution vs Attempts, mutation authority/fencing, ambiguous provider effects, idempotency, checkpoint/resume, cancellation races and non-regressing recovery.

### C6 — Evaluation / Evidence / Provenance / history

**DEFINED; activated by 015-G.**

Protects Evaluation validity, Evidence interpretation/cardinality, exact completion basis, typed Provenance, historical reconstruction qualifications and reproducibility bounds.

### C7 — security / disclosure / protected existence

**DEFINED; activated by 015-H.**

Protects action-specific authorization, fail-closed uncertainty, protected existence, redaction/disclosure parity, secret exclusion and canonical-history immutability.

### C8 — provider / portability / scale

**DEFINED; activated by 015-I.**

Protects capability evidence at actual strength, semantics-preserving fallback, capability freshness, platform-independent identity and workload/profile support qualification.

### C9 — end-to-end adversarial replay

**DEFINED; activated incrementally and required for 015-J consolidation.**

Replays the complete Phase 014-F scenario family against implemented slices.

## Phase 014-F scenario registry

The current end-to-end scenario families are:

~~~text
S01 direct Generation without Learning/Learned State
S02 Learned-State-assisted Generation
S03 structured-topology family
S04 text-bearing structured data under no-egress
S05 Evaluation favorable/unfavorable/indeterminate/no-finding
S06 evidence-gated Generation + later Evidence invalidation
S07 retry/cancellation/checkpoint/provider-unknown race
S08 regressive restore + stale-writer exclusion
S09 partial availability/disclosure/historical reconstruction
S10 scale/resource pressure + approximation attack
S11 provider capability change + portability fallback
S12 authorization/protected-existence conflict
S13 external governance handoff
S14 combined adversarial composition
~~~

These IDs are Phase 015 verification references. They do not create new product semantics.

## Architecture-fitness baseline

Current Phase 013 invariants are the authoritative source. 015-B groups their executable enforcement as follows.

### AF-C0 executable now

~~~text
AF-C0-01 current authority/slice state is discoverable
AF-C0-02 production code never imports test support
AF-C0-03 semantic core cannot depend on coordination/outer integration
AF-C0-04 portable core cannot depend on concrete adapters/bootstrap
AF-C0-05 root package cannot eagerly activate outer/provider integrations
AF-C0-06 generic hidden-owner packages are prohibited
AF-C0-07 package build/import integrity follows current source tree
AF-C0-08 portable verification denies sockets by default
AF-C0-09 deferred runtime/provider dependencies remain absent until owning slice
AF-C0-10 historical Phase 007 progression/exact-tree assumptions are not executable authority
~~~

### AF-C1..C9 deferred enforcement

Later slices must add behavioral enforcement for the relevant Phase 013 invariants rather than treating the C0 static checks as proof.

Examples include exact-history resolution, stale-writer fencing, Generation-owned finality, Strategy/binding semantics, distributed closure, Evaluation/Evidence separation, disclosure parity and provider qualification.

## Test marker taxonomy

The current harness recognizes:

~~~text
network      intentionally requires socket/network access
external     intentionally requires an external service
integration  crosses a component/process/storage boundary
spark        requires a Spark/local-distributed runtime
failure      exercises explicit fault/retry/recovery injection
security     exercises authorization/disclosure/secret boundaries
provider     runs provider capability/conformance behavior
scale        executes declared workload/performance evidence
stochastic   uses statistical/stochastic acceptance rules
~~~

Markers classify evidence. A marker does not itself authorize the dependency/service or satisfy a verification lane.

## Verification profiles

### profile: authority

Fast C0 authority/scaffold checks.

Includes current authority fitness and bootstrap metadata checks.

### profile: static

Includes:

- bootstrap/lockfile;
- Ruff lint;
- Ruff format;
- mypy;
- Import Linter;
- C0 authority/fitness checks.

### profile: portable

The required default merge profile while later lanes are not active.

Includes:

- static profile;
- deterministic unit tests;
- portable fitness tests;
- package import/build verification;
- default socket denial.

It excludes tests marked as requiring network, external services, Spark, provider environments, scale, stochastic behavior or explicit failure/security integration profiles unless later slice authority promotes one into the required portable gate.

### profile: integration

Reserved entry point for currently authorized integration tests. 015-B defines the marker/profile contract but does not invent integration behavior.

### profile: certification

Reserved umbrella for later provider/compatibility/security/scale support evidence. It is not active as a release claim in 015-B.

## Gate semantics

~~~text
G0  authority/static repository gate      ACTIVE
G1  portable required merge gate          ACTIVE
G2  bounded integration/conformance       DEFINED; slice-activated
G3  scheduled compatibility/resilience    DEFINED; later activated
G4  support/release certification          DEFINED; later activated
~~~

A later slice cannot claim acceptance when its required G2+ evidence is absent merely because G1 is green.

## Acceptance-evidence contract

Every implementation slice after 015-B must retain a bounded record containing:

~~~text
slice identifier
upstream authority
implementation change set
verification lanes activated
verification profiles executed
architecture-fitness obligations addressed
Phase 014-F scenarios exercised
Phase 014 readiness risks addressed
environment/runtime/provider versions when material
pass/fail/waiver outcomes
known limitations / deferred evidence
CI run references when available
reopen decision, if any
~~~

No line-coverage threshold is accepted as a substitute for contract evidence.

## Flakiness / retry / quarantine

- infrastructure failure before test execution may be rerun;
- assertion failure remains visible even if a diagnostic rerun passes;
- stochastic tests may not use retry-until-green;
- quarantine requires protected obligation, reason, owner, risk, expiry/review and compensating control;
- an obligation with no remaining valid enforcement blocks the affected support/delivery claim.

## Waiver boundary

A waiver cannot authorize semantic contradiction, historical corruption, hidden egress, deliberate stale-writer acceptance, duplicate semantic promotion, secret disclosure, false Evidence/Provenance, or provider success being treated as semantic completion.

Such cases require correction or the smallest upstream reopen.

## 015-B executable objective

015-B will complete when:

~~~text
C0 current authority checks               executable
marker taxonomy                            registered
authority/static/portable profiles         executable
default-deny portable network posture      retained
historical Phase 005 verification status   demoted
current architecture-fitness baseline      documented
later C1-C9 activation rules               explicit
acceptance-evidence contract               explicit
repository Verify workflow                 green on current head
domain implementation                      NONE
~~~

## Current authorization state

~~~text
015-A        COMPLETE
015-B        AUTHORIZED / ACTIVE
015-C..015-J NOT AUTHORIZED
IMPLEMENTATION START  NOT STARTED
~~~
