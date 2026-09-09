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
4. read `docs/synchronizations/core-synchronizations.md` for cross-concept coordination—the 006-C refinements are canonical;
5. read `docs/architecture/phase-004-consolidated-architecture-contract.md`;
6. read `docs/implementation/phase-005-consolidated-implementation-planning-contract.md`;
7. read the active Phase 006 record/index and only the detailed 005 plan affected by the design question;
8. follow only directly relevant concept/synchronization/experience/architecture authority;
9. use ADRs for rationale/history rather than as replacement for current canonical authority;
10. consult `docs/backlog/index.md` for blocker/deferred classification, not as canonical design truth.

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
- **006-C** — end-to-end adversarial synchronization validation.

Current next:

**006-D — Reference Strategy/Method and Topology Design Probes & Algorithm-Neutrality Stress Test**.

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

BDR-002 is resolved for the current eleven-concept/fifteen-sync baseline. If 006-G later accepts `Relationship` or changes coordination materially, replay the affected scenarios before 006-J readiness approval.

## Phase 006 design rules

Remaining blocking questions are concentrated in:

```text
BDR-003  representative Strategy/method/topology design probes
BDR-004  initial-scope / future-extensibility closure
```

BDR-001 has semantic/synchronization closure with experience/architecture propagation pending 006-H/006-I.

Agents MUST:

- judge candidate concepts by purpose, independent state/actions, operational principle and genericity—not by whether a persistent record/class would be convenient;
- treat `ControlPlaneIncarnation`, `HistoricalRef`, finding slots, completion basis, capability grants, deployment profiles, support claims and similar structures as mechanisms/hypotheses unless concept review proves otherwise;
- preserve the eleven concepts/fifteen synchronizations unless explicit Phase 006 evidence justifies revision;
- use representative synthesis/evaluation methods as design probes, never as semantic templates;
- keep CTGAN/PyTorch/Spark/Databricks/provider behavior downstream of concept authority;
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

## 006-D probe discipline

006-D is **design probing, not algorithm implementation**.

Agents may analyze concrete method shapes such as CTGAN-like Learning, direct/statistical generation, sequence/time-series synthesis, multi-table relational synthesis, deterministic validation, and statistical/approximate Evaluation only to test whether existing concepts/contracts remain generic.

Do not:

- create model/runtime source code;
- select one probe as canonical SYNGAN behavior;
- infer a concept merely because one library exposes a class/object for it;
- hide full-corpus driver collection, centralized model-state assumptions, or algorithm-specific checkpoint semantics behind generic SPI names;
- assume all Strategies require Learning/Learned State;
- assume one file/object is the universal Learned-State representation.

## Frozen implementation-planning baseline

Until Phase 006 changes upstream authority and 006-I deliberately back-propagates it, preserve the Phase 005 planning baseline rather than rewriting it ad hoc.

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

**006-D — Reference Strategy/Method and Topology Design Probes & Algorithm-Neutrality Stress Test**
