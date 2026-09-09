# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Current authority state

**Phase 005 implementation planning is complete. Phase 006 design refinement is current. Production implementation is NOT authorized.**

During Phase 006, agents may update design/authority/planning documentation requested by the active phase group, but MUST NOT create production package scaffolding, source code, database schemas/migrations, runtime/Spark/security/platform adapters, verification suites, CI workflows, deployment infrastructure or benchmark harnesses.

A future implementation-authority phase may be created only after a positive design-readiness exit explicitly authorizes it.

## Progressive disclosure

For material work:

1. read `docs/index.md`;
2. read `docs/authority/design-methodology.md` for methodology-sensitive work;
3. for recovery/HA/current-authority work, read `docs/authority/operational-authority-continuity-regressive-recovery-contract.md`;
4. for runtime packaging/text/Spark worker closure, read `docs/authority/self-contained-execution-runtime-distribution-closure-contract.md`;
5. for scale/resource/admission/approximation/degraded-operation work, read `docs/authority/enterprise-scale-resource-admission-approximation-degraded-operation-contract.md`;
6. read `docs/synchronizations/core-synchronizations.md` for cross-concept coordination;
7. read `docs/architecture/phase-004-consolidated-architecture-contract.md`;
8. read `docs/implementation/phase-005-consolidated-implementation-planning-contract.md`;
9. read the active Phase 006 record/index and only the detailed 005 plan affected by the design question;
10. follow only directly relevant concept/synchronization/experience/architecture authority;
11. use ADRs for rationale/history rather than as replacement for current canonical authority;
12. consult `docs/backlog/index.md` for blocker/deferred classification, not as canonical design truth.

Do not load or copy the entire documentation corpus by default.

## Authority order

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation planning
  > future code / deployment
  > ADR rationale / phase history / backlog / examples
```

Later feasibility evidence may justify reopening upstream authority. Do not patch a genuine design conflict only inside an implementation-plan document.

## Phase 006 state

Completed:

- **006-A** — post-planning concept/mechanism/scope revalidation;
- **006-B** — temporal authority/regressive-recovery/historical-truth refinement;
- **006-C** — end-to-end adversarial synchronization validation;
- **006-D** — representative Strategy/method/text/topology/runtime-distribution probes;
- **006-E** — enterprise scale/resource/approximation/backpressure/degraded-mode design validation.

Current next:

**006-F — Privacy, Disclosure, Release-Governance Boundary & Mechanism-Specific Scope Decision**.

Current design counts remain:

```text
accepted concepts             11
accepted synchronizations     15
reopened candidate concepts    Relationship
```

No `SYNC-16` is currently accepted.

## Phase 006 cross-cutting rules

Agents MUST preserve:

- restored historical persistence is not current mutation authority after potentially regressive recovery;
- stale Attempts/cancellations/capabilities cannot resurrect through rollback;
- history reconstruction is owner-gated and unresolved gaps remain explicit;
- the supported baseline includes a self-contained source-derived free-form-text synthesis path with no required pretrained artifact/runtime network service;
- optional pretrained/model-hub/LLM/service text capability remains explicit and cannot become a hidden fallback;
- driver import/discovery success is not proof that Spark executors can execute the same binding;
- every material worker, including dynamically allocated workers, must satisfy compatible exact runtime closure;
- missing worker dependencies/artifacts cannot trigger undeclared public-network acquisition;
- large Learned State/model artifacts cannot universally require full driver load/broadcast;
- enterprise compatibility is multidimensional and workload-specific rather than a row-count flag;
- an undisclosed source-size-proportional single-process/driver stage invalidates an enterprise-scale claim for that path;
- resource pressure may queue/block/retry work but MUST NOT silently weaken an existing committed semantic contract;
- approximation is explicit owner-bound semantics, never an implicit resource-pressure fallback;
- backpressure must not drop mandatory logical work, truncate quantity/horizon, omit required topology constituents or weaken Evaluation coverage;
- sampled/sketched Evaluation cannot become universal Evidence because exhaustive evaluation is expensive;
- cache presence/absence does not redefine exact artifact/runtime identity;
- degraded operation must be capability-specific: canonical-store loss, projection loss, telemetry loss, dependency loss, exact-reference loss, storage loss, worker loss and authorization loss have different consequences;
- security/authorization uncertainty fails closed for protected actions;
- progress/ETA/task completion is not semantic completion;
- storage pressure does not override authority-aware retention.

## Phase 006 design rules

The remaining blocking scope question is concentrated in **BDR-004 — initial-scope/future-extensibility closure**. BDR-001 still requires experience/architecture propagation through 006-H/006-I.

Agents MUST:

- judge candidate concepts by purpose, independent state/actions, operational principle and genericity—not by whether a persistent record/class would be convenient;
- treat `ControlPlaneIncarnation`, `HistoricalRef`, finding slots, completion basis, capability grants, runtime-distribution manifests, resource reservations, queues, caches, deployment profiles, support claims and similar structures as mechanisms/hypotheses unless concept review proves otherwise;
- preserve the eleven concepts/fifteen synchronizations unless explicit Phase 006 evidence justifies revision;
- use representative synthesis/evaluation methods as design probes, never as semantic templates;
- keep CTGAN/PyTorch/Hugging Face/Spark/Databricks/provider behavior downstream of concept authority;
- preserve deliberate initial-scope exclusions without hard-coding them as permanent impossibilities;
- promote material changes to concept/synchronization/experience/architecture authority explicitly before back-propagating them into Phase 005 planning.

## Structured-data topology rules

Phase 006 explicitly considers:

```text
single-table
time-series
multi-table shared-key
```

A future API `mode`/parameter may select a capability profile, but that parameter MUST NOT become the sole durable representation of participating scopes, shared-key linkage, temporal entity/series identity, temporal order/cadence, cardinality/participation, validity Constraints, coordinated completion semantics, or required Evaluation/Evidence.

`Relationship` is reopened only as a candidate pending 006-G. Do not treat it as accepted concept authority before that decision.

## 006-F privacy/disclosure/release discipline

006-F is design/scope refinement, not privacy-mechanism implementation.

Agents must explicitly test:

- memorization/disclosure risk from self-contained free-form text generation;
- optional pretrained/runtime-network text and egress implications;
- sample/statistical privacy Evidence at enterprise scale and its claim limits;
- the distinction between privacy-risk Evaluation/Evidence and a formal privacy guarantee;
- whether a mechanism such as differential privacy would have sufficiently independent purpose/state/actions to require concept discovery;
- the boundary between Generation completion, favorable Evidence and external release/use approval;
- truthful security redaction/withholding of sensitive Evidence/history.

Do not:

- equate synthetic data with anonymous/private data by default;
- equate successful privacy Evaluation with a formal guarantee unless the mechanism actually supports it;
- treat favorable Evidence as release/use authorization;
- let scale pressure weaken a privacy Criterion or inflate sampled Evidence;
- make a hosted text service an implicit privacy/release authority;
- implement DP, attack suites, DLP or governance workflows during Phase 006.

## Frozen implementation-planning baseline

Until 006-I deliberately back-propagates accepted Phase 006 authority, preserve the Phase 005 planning baseline rather than rewriting it ad hoc.

Key constraints include:

- durable identity distinct from database/path/DataFrame/platform identity;
- semantic completion distinct from runtime/platform completion;
- one stable Execution with multiple Attempts and stale-writer fencing;
- checkpoint/candidate/runtime material remains non-final;
- owner-established Evidence with bounded claim strength;
- typed canonical Provenance distinct from projections/telemetry/security audit;
- current authorization cannot broaden committed semantics;
- no hidden acquisition/remote fallback/required external telemetry in offline/no-egress profiles;
- enterprise paths cannot require full-corpus driver-local materialization;
- platform support is capability-negotiated and missing guarantees are explicit.

## Non-negotiable anti-collapse rules

Do not:

- create universal `Context`, `Session`, `Manager`, `Registry`, `Metadata`, `State`, `Result`, `Quality`, `Run`, `Artifact`, `Security`, `Resource`, `Backpressure`, `Approximation` or `DegradedMode` god-owner;
- make DataFrame, path/table alias, loaded model, database row, scheduler job or platform ID canonical semantic identity;
- equate runtime/platform/progress success with semantic completion;
- equate checkpoint/candidate/runtime material with Learned State/output/Evidence;
- replace fencing with lease expiry, scheduler retry or last-writer-wins;
- let hidden acquisition/network/egress appear because an adapter/provider makes it easy;
- let Evidence exceed Evaluation support;
- let graph/search/telemetry/security-audit projections become canonical Provenance/history;
- use current/latest values in place of exact historical refs;
- treat handle possession as authorization or persist bearer credentials in canonical history;
- infer causal/quality/privacy/release claims from structural history differences alone;
- claim enterprise scale while hiding source-size-proportional single-process stages.

## Documentation synchronization

When Phase 006 changes accepted design:

- cross-cutting authority changes go to `docs/authority/`;
- concept changes go to `docs/concepts/`;
- synchronization changes go to `docs/synchronizations/`;
- actor/programmatic experience changes go to `docs/experience/`;
- architecture changes go to `docs/architecture/` and material rationale to ADRs when appropriate;
- only then update affected `docs/implementation/` plans;
- phase records preserve history and MUST NOT become the sole current authority.

Backlog items close only after the canonical owner reflects the accepted resolution.

## Current next group

**006-F — Privacy, Disclosure, Release-Governance Boundary & Mechanism-Specific Scope Decision**
