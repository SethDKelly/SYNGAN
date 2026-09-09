# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Current authority state

**Phase 005 implementation planning is complete. Phase 006 design refinement is current. Production implementation is NOT authorized.**

During Phase 006, agents may update design/authority/planning documentation requested by the active phase group, but MUST NOT create production package scaffolding, source code, database schemas/migrations, runtime/Spark/security/platform adapters, executable verification suites, CI workflows, deployment infrastructure or benchmark harnesses.

A future implementation-authority phase may be created only after a positive design-readiness exit explicitly authorizes it.

## Progressive disclosure

For material work:

1. read `docs/index.md`;
2. read `docs/authority/design-methodology.md` for methodology-sensitive work;
3. read only the directly relevant cross-cutting authority:
   - recovery/HA → `operational-authority-continuity-regressive-recovery-contract.md`;
   - packaging/text/Spark worker closure → `self-contained-execution-runtime-distribution-closure-contract.md`;
   - scale/backpressure/approximation/degraded operation → `enterprise-scale-resource-admission-approximation-degraded-operation-contract.md`;
   - privacy/disclosure/formal guarantee/release boundary → `privacy-disclosure-formal-guarantee-release-boundary-contract.md`;
4. read `docs/synchronizations/core-synchronizations.md` for cross-concept coordination;
5. read `docs/architecture/phase-004-consolidated-architecture-contract.md`;
6. read `docs/implementation/phase-005-consolidated-implementation-planning-contract.md`;
7. read the active Phase 006 record/index and only affected detailed authorities/plans;
8. use ADRs for rationale/history, not as a replacement for current canonical authority;
9. use `docs/backlog/index.md` only for blocker/deferred classification.

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

If feasibility evidence exposes a genuine upstream problem, reopen/promote the upstream authority explicitly rather than patching only an implementation plan.

## Phase 006 state

Completed:

- **006-A** — concept/mechanism/scope revalidation;
- **006-B** — regressive-recovery/current-authority refinement;
- **006-C** — adversarial synchronization validation;
- **006-D** — Strategy/method/text/topology/runtime-distribution probes;
- **006-E** — enterprise scale/resource/approximation/backpressure/degraded-mode validation;
- **006-F** — privacy/disclosure/formal-guarantee/release-boundary validation.

Current next:

**006-G — Structured-Data Topology: Single-Table, Time-Series & Multi-Table Relationship Concept/Extensibility Audit**.

Current design counts:

```text
accepted concepts             11
accepted synchronizations     15
reopened candidate concepts    Relationship
```

No `SYNC-16` is currently accepted.

## Non-negotiable Phase 006 authority

Agents MUST preserve:

### Recovery/current authority

- restored persistence is not proof of current writer/cancellation/security authority;
- potentially regressive recovery enters continuity-unverified/recovery-quarantine semantics;
- a fresh non-regressing authority boundary is required before write-capable work resumes;
- missing post-backup canonical history is not proof of non-occurrence;
- surviving physical effects are not automatic proof of semantic transition;
- reconstruction is owner-gated and auditable;
- stale writers never regain authority merely because their immutable effects may be adopted.

### Execution/synchronization

- same-Execution retry/resume requires unchanged committed semantics **and** current authorization/dependency/platform/recovery qualification;
- current inability to continue does not authorize silent source/Strategy/Learned-State/dependency/method/network substitution;
- coordinated logical Generation completion applies to the whole committed scope;
- runtime/platform success remains distinct from Learning/Generation/Evaluation semantic completion;
- checkpoint/candidate/runtime material remains non-final.

### Self-contained/runtime distribution

- the supported baseline includes at least one source-derived/local free-form-text synthesis path requiring no externally acquired pretrained model or runtime network service;
- Hugging Face/model hubs/LLM APIs/remote inference remain optional, explicit integrations—not hidden baseline requirements/fallbacks;
- one Strategy implementation binding may resolve multiple exact implementation/runtime/model/tokenizer/codec components;
- driver import/discovery success is not proof that Spark executors can execute the same closure;
- every material worker, including dynamically allocated workers, must inherit/prove compatible runtime closure;
- missing worker dependencies/artifacts must not trigger undeclared public-network acquisition;
- large Learned State/model artifacts must not require universal driver-local loading/broadcast.

### Enterprise scale/resource/degraded operation

- enterprise scale is multidimensional; row count alone is not a support claim;
- undisclosed source-size-proportional driver/single-process stages invalidate enterprise-scale claims for that path;
- resource pressure may queue/block/retry but must not silently weaken committed semantics;
- approximation is owned by the concept whose semantics it changes, not a generic runtime fallback;
- backpressure must preserve mandatory records/scope/coverage/security obligations;
- sampled/sketched Evaluation cannot become universal Evidence merely because exhaustive validation is expensive;
- caches are performance mechanisms, not dependency identity;
- degraded operation is capability-specific; canonical-store loss, projection loss, telemetry loss, dependency loss, source loss and storage loss remain distinct;
- progress/ETA/task completion does not establish semantic completion.

### Privacy/disclosure/release boundary

- synthetic origin does not imply privacy, anonymization or safe release;
- self-contained/offline execution is not a privacy guarantee;
- disclosure/memorization questions remain Criterion/Evaluation/Evidence concerns unless later concept discovery proves otherwise;
- privacy-related Evidence must remain threat-model/method/scope/coverage/uncertainty specific;
- favorable empirical Evidence does not become a formal privacy guarantee;
- per-row/per-table favorable Evidence does not automatically establish joined multi-table or longitudinal-trajectory privacy;
- differential privacy is not part of the initial implementation baseline;
- any future composable formal DP/privacy mechanism with independent budget/accounting state MUST reopen Jackson-style concept discovery before implementation;
- do not add `epsilon`, `delta`, privacy-budget/accounting counters to generic Strategy metadata, Evidence, deployment quota or implementation config as a shortcut;
- Use/Release Decision remains external to current SYNGAN concept authority;
- current authorization/redaction may block or transform a view without rewriting canonical Generation/Evidence/Provenance history;
- no universal privacy score or `safe_to_release=true` semantic authority is accepted.

## Structured-data topology rules — 006-G

Phase 006 explicitly considers:

```text
single-table
time-series
multi-table shared-key
```

A future API `mode`/parameter may select a capability profile, but that parameter MUST NOT become the sole durable representation of:

- participating logical scopes;
- shared-key linkage;
- temporal entity/series membership;
- order/cadence/continuity;
- cardinality/participation;
- validity Constraints;
- coordinated completion semantics;
- Evaluation/privacy subject scope.

`Relationship` is reopened only as a candidate. Do not treat it as accepted before 006-G completes the Jackson tests for purpose, independence, genericity, lifecycle/actions and synchronization burden.

006-G must specifically distinguish descriptive linkage from prescriptive rules:

```text
orders.customer_id relates to customers.customer_id
        ≠
all orders.customer_id values must resolve
```

The former may support a Relationship concept; the latter remains Constraint authority.

Time-series sequence membership/order must be tested against the same candidate without assuming that a relational-table abstraction automatically fits temporal structure.

## Frozen implementation-planning baseline

Until 006-I deliberately back-propagates accepted Phase 006 authority, preserve the Phase 005 planning baseline rather than rewriting it ad hoc.

Key constraints include:

- durable identity distinct from database/path/DataFrame/platform identity;
- semantic completion distinct from runtime/platform completion;
- one stable Execution with multiple Attempts and stale-writer fencing;
- owner-established Evidence with bounded claim strength;
- typed canonical Provenance distinct from projections/telemetry/security audit;
- current authorization cannot broaden committed semantics;
- no hidden acquisition/remote fallback/required external telemetry in offline/no-egress profiles;
- enterprise paths cannot require full-corpus driver-local materialization;
- platform support is capability-negotiated and missing guarantees are explicit.

## Anti-collapse rules

Do not create universal `Context`, `Session`, `Manager`, `Registry`, `Metadata`, `State`, `Result`, `Quality`, `Run`, `Artifact`, `Security`, `Privacy`, `Resource`, `DegradedMode` or similar god-owner.

Do not make DataFrame, path/table alias, loaded model, database row, scheduler job or platform ID canonical semantic identity.

Do not equate runtime success, Evidence, security authorization, external governance approval, or physical artifact existence with another owner's semantic state.

Do not use current/latest values in place of exact historical refs, and do not infer causal/quality/privacy/release claims from structural history alone.

## Documentation synchronization

When Phase 006 changes accepted design:

- cross-cutting authority → `docs/authority/`;
- concept changes → `docs/concepts/`;
- synchronization changes → `docs/synchronizations/`;
- actor/programmatic experience → `docs/experience/`;
- architecture + material rationale → `docs/architecture/` / ADRs;
- only then back-propagate into affected `docs/implementation/` plans;
- phase records preserve history and must not become the sole current authority.

Backlog items close only after canonical authority reflects the accepted resolution.

## Current next group

**006-G — Structured-Data Topology: Single-Table, Time-Series & Multi-Table Relationship Concept/Extensibility Audit**
