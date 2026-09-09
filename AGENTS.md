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
4. for runtime packaging, text/self-contained behavior, Spark executor/runtime availability or model/artifact distribution, read `docs/authority/self-contained-execution-runtime-distribution-closure-contract.md`;
5. read `docs/synchronizations/core-synchronizations.md` for cross-concept coordination—the 006-C refinements are canonical;
6. read `docs/architecture/phase-004-consolidated-architecture-contract.md`;
7. read `docs/implementation/phase-005-consolidated-implementation-planning-contract.md`;
8. read the active Phase 006 record/index and only the detailed 005 plan affected by the design question;
9. follow only directly relevant concept/synchronization/experience/architecture authority;
10. use ADRs for rationale/history rather than as replacement for current canonical authority;
11. consult `docs/backlog/index.md` for blocker/deferred classification, not as canonical design truth.

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
- **006-D** — representative Strategy/method/text/topology/runtime-distribution probes.

Current next:

**006-E — Enterprise Scale, Resource/Approximation, Backpressure & Degraded-Mode Design Validation**.

Current design counts remain:

```text
accepted concepts             11
accepted synchronizations     15
reopened candidate concepts    Relationship
```

No `SYNC-16` is currently accepted.

## 006-B operational-authority rules

Agents MUST preserve:

- restoring older persistence is not proof that its `current` Attempt/fence/cancellation/security state is actually current;
- a potentially regressive restore enters recovery quarantine / continuity-unverified semantics before ordinary write-capable operation resumes;
- a fresh non-regressing authority boundary is required before write capability resumes;
- a superseded writer cannot regain authority merely because restored state predates the supersession;
- a cancellation omitted from an old backup cannot reactivate pre-cancellation write authority;
- pre-recovery capability grants/credentials are not current permission merely because they reappear in restored state;
- surviving external effects are observations until their exact canonical meaning is reconciled;
- absence of a post-backup transition from restored persistence does not prove it never happened;
- physical bytes/provider success do not by themselves reconstruct Learned State, completed Generation output or Evidence authority;
- historical reconstruction requires evidence sufficient for the owning concept's normal transition/completion invariants;
- unresolved post-restore history remains explicitly unknown/unavailable rather than silently coerced;
- current post-recovery authority may adopt verified immutable effects, but old writers never regain authority through adoption;
- `ControlPlaneIncarnation` or equivalent remains a downstream realization mechanism, not a domain concept.

## 006-C synchronization rules

The 006-C adversarial pass retained fifteen synchronization IDs and refined the canonical rules.

Agents MUST preserve:

- same-Execution retry/resume requires unchanged committed semantics **and** current authorization/dependency/platform/recovery qualification;
- current inability to continue does not authorize silent source/Strategy/Learned-State/dependency/method/network substitution;
- after potentially regressive recovery, restored Attempt/current-state values do not authorize continuation by themselves;
- a coordinated logical Generation output is completed only when the whole committed scope is completion-sufficient, not when one constituent table/sequence is complete;
- missing restored history is not proof of non-occurrence;
- surviving external/physical effects are not automatic proof of a missing semantic transition;
- reconstruction of missing canonical history is owner-gated and auditable;
- unresolved continuity/history gaps constrain the strongest reproducibility/comparison claim rather than rewriting historical commitments.

BDR-002 is resolved for the current eleven-concept/fifteen-sync baseline. If 006-G later accepts `Relationship` or changes coordination materially, replay affected scenarios before 006-J readiness approval.

## 006-D self-contained/runtime-distribution rules

The active Self-Contained Execution & Runtime Distribution Closure contract is non-negotiable.

Agents MUST preserve:

- the supported baseline includes at least one source-derived/local free-form-text synthesis path that requires no externally acquired pretrained model or runtime network service;
- Hugging Face/model hubs/LLM APIs/remote inference are optional integrations, never hidden baseline requirements or automatic fallbacks;
- a locally provisioned pretrained model/tokenizer is a distinct local-artifact-dependent capability, not package-only self-containment;
- `Text`, `LanguageModel`, `Tokenizer`, `CompositeStrategy`, `RuntimeEnvironment` and `Distribution` are not accepted standalone concepts merely because implementations have corresponding objects;
- one top-level Strategy implementation binding may resolve multiple exact implementation/runtime/model/tokenizer/codec components;
- material component choice cannot silently change during runtime;
- driver import/discovery success is **not** proof that Spark executors can execute the same binding;
- every worker that may execute material code, including dynamically allocated workers, must inherit/prove a compatible exact runtime closure;
- missing worker code/dependencies/artifacts MUST NOT trigger undeclared public-network installation/download during an Attempt;
- large Learned State/model artifacts MUST NOT require universal driver-local loading or broadcast; scalable distributed/provider-native loading must remain possible;
- implementation/artifact presence does not override current trust/authorization policy;
- platform support must report a distribution capability gap as limited/incompatible/indeterminate rather than silently weakening behavior.

BDR-003 is resolved by 006-D. If 006-G/006-I materially changes Strategy/topology/runtime architecture, replay affected probes before 006-J readiness approval.

## Phase 006 design rules

The remaining blocking scope question is concentrated in BDR-004 — initial-scope/future-extensibility closure. BDR-001 still requires experience/architecture propagation through 006-H/006-I.

Agents MUST:

- judge candidate concepts by purpose, independent state/actions, operational principle and genericity—not by whether a persistent record/class would be convenient;
- treat `ControlPlaneIncarnation`, `HistoricalRef`, finding slots, completion basis, capability grants, runtime-distribution manifests, deployment profiles, support claims and similar structures as mechanisms/hypotheses unless concept review proves otherwise;
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

## 006-E scale/degraded-mode discipline

006-E is design validation, not benchmark implementation.

Agents must challenge the design across rows/bytes/width/cardinality/skew/partitions, large/sharded state, text/model/runtime-distribution pressure, dynamic workers, multi-table fan-out, time-series entity/horizon scale, Evaluation approximation, concurrent workloads, backpressure/admission and degraded dependencies/platform services.

Do not:

- claim enterprise scale from row count alone;
- hide source-size-proportional driver/coordinator stages;
- solve cluster artifact pressure with universal driver broadcast;
- let approximation/sampling silently strengthen Evidence claims;
- let backpressure drop canonical transitions/outbox/security obligations;
- map degraded/unknown capability to success merely to keep work running;
- turn resource scarcity into a semantic change or hidden Strategy fallback.

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

- create universal `Context`, `Session`, `Manager`, `Registry`, `Metadata`, `State`, `Result`, `Quality`, `Run`, `Artifact`, `Security` or similar god-owner;
- make DataFrame, path/table alias, loaded model, database row, scheduler job or platform ID canonical semantic identity;
- equate runtime/platform success with semantic completion;
- equate checkpoint/candidate/runtime material with Learned State/output/Evidence;
- replace fencing with lease expiry, scheduler retry or last-writer-wins;
- let hidden acquisition/network/egress appear because an adapter/provider makes it easy;
- let Evidence exceed Evaluation support;
- let graph/search/telemetry/security-audit projections become canonical Provenance/history;
- use current/latest values in place of exact historical refs;
- treat handle possession as authorization or persist bearer credentials in canonical history;
- infer causal/quality claims from structural history differences alone;
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

**006-E — Enterprise Scale, Resource/Approximation, Backpressure & Degraded-Mode Design Validation**
