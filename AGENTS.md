# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current authority state

**Phase 006 design refinement is current. Production implementation is NOT authorized.**

Phase 005 completed implementation planning only. During Phase 006, agents may update accepted design/authority/experience/architecture/planning documentation requested by the active group, but MUST NOT create production package scaffolding, source code, database schemas/migrations, runtime/Spark/security/platform adapters, executable verification suites, CI workflows, deployment infrastructure or benchmark harnesses.

A later implementation-authority phase may exist only after a positive explicit design-readiness exit.

## Progressive disclosure

For material work:

1. read `docs/index.md`;
2. read `docs/authority/design-methodology.md` for methodology-sensitive work;
3. read only the relevant current cross-cutting authority:
   - recovery/HA → `operational-authority-continuity-regressive-recovery-contract.md`;
   - packaging/text/Spark-worker closure → `self-contained-execution-runtime-distribution-closure-contract.md`;
   - scale/backpressure/approximation/degraded operation → `enterprise-scale-resource-admission-approximation-degraded-operation-contract.md`;
   - privacy/disclosure/formal guarantee/release → `privacy-disclosure-formal-guarantee-release-boundary-contract.md`;
   - structured topology/relationship semantics → `structured-data-topology-relationship-semantics-contract.md`;
4. read `docs/synchronizations/core-synchronizations.md`;
5. for experience work, read both Phase 003 and Phase 006 consolidated experience contracts;
6. for architecture work, read the Phase 004 consolidated architecture contract;
7. for implementation-planning reconciliation, read the Phase 005 consolidated plan and only affected detailed plans;
8. read the active Phase 006 record/index;
9. use ADRs for rationale/history and backlog only for classification.

Do not load/copy the whole documentation corpus by default.

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

If later feasibility reveals a genuine upstream issue, reopen upstream authority explicitly rather than patching only implementation planning.

## Phase 006 state

Completed:

- 006-A — concept/mechanism/scope revalidation;
- 006-B — regressive-recovery/current-authority refinement;
- 006-C — adversarial synchronization validation;
- 006-D — Strategy/method/text/topology/runtime-distribution probes;
- 006-E — enterprise scale/resource/approximation/backpressure/degraded validation;
- 006-F — privacy/disclosure/formal-guarantee/release-boundary validation;
- 006-G — structured-topology/Relationship and baseline-scope decision;
- 006-H — human/programmatic experience closure.

Current next:

**006-I — Architecture/ADR Reconciliation, Canonical Authority Promotion & Planning Back-Propagation**.

Current design counts remain **11 accepted concepts / 15 synchronizations**. No `SYNC-16` or provisional concept candidate exists.

## Non-negotiable current authority

### Recovery/current authority

- restored persistence is not proof of current writer/cancellation/security authority;
- potentially regressive recovery enters continuity-unverified/recovery-restricted semantics;
- a fresh non-regressing authority boundary is required before write-capable work resumes;
- missing post-backup history is not proof of non-occurrence;
- surviving physical effects are not automatic proof of semantic transition;
- reconstruction is owner-gated/auditable;
- stale writers never regain authority merely because immutable effects may be adopted.

### Execution/synchronization

- retry/resume requires unchanged committed semantics **and** current authorization/dependency/platform/recovery qualification;
- inability to continue never authorizes silent source/Strategy/Learned-State/dependency/method/network substitution;
- coordinated Generation completion applies to the whole committed logical scope;
- runtime/platform success remains distinct from Learning/Generation/Evaluation semantic completion;
- checkpoint/candidate/runtime material remains non-final.

### Self-contained/runtime distribution

- supported baseline includes at least one source-derived/local free-form-text synthesis path requiring no externally acquired pretrained model or runtime network service;
- model hubs/LLM APIs/remote inference are optional explicit integrations, never hidden baseline fallback;
- one Strategy binding may resolve multiple exact code/runtime/model/tokenizer/codec components;
- driver import/discovery is not proof of Spark-executor readiness;
- every material worker, including dynamically allocated workers, must satisfy compatible exact runtime closure;
- missing worker dependencies/artifacts must not trigger undeclared public-network acquisition;
- large Learned State/model artifacts must not require universal driver-local loading/broadcast.

### Scale/resource/degraded operation

- enterprise scale is multidimensional; row count alone is not a support claim;
- undisclosed source-size-proportional single-process/driver stages invalidate enterprise-scale claims for that path;
- resource pressure may queue/block/retry but cannot silently weaken committed semantics;
- approximation is owned by the concept whose semantics it changes;
- backpressure must preserve mandatory records/scope/coverage/security obligations;
- sampled/sketched Evaluation cannot become universal Evidence because exhaustive validation is expensive;
- degraded operation is capability-specific, not one global status;
- progress/ETA/task completion does not establish semantic completion.

### Privacy/disclosure/release

- synthetic origin/offline execution does not imply privacy, anonymization or safe release;
- disclosure/memorization remain Criterion/Evaluation/Evidence concerns under current scope;
- favorable empirical Evidence is not a formal privacy guarantee;
- differential privacy is not in the initial baseline;
- future composable formal DP/privacy mechanisms with independent accounting state MUST reopen concept discovery before implementation;
- Use/Release Decision remains external to current SYNGAN concept authority;
- authorization/redaction may shape current access without rewriting canonical history.

### Structured-data topology

The complete structured-data capability target includes:

```text
single-table
time-series
multi-table shared-key
```

`Relationship` is not a standalone concept. Material structural relationship semantics are descriptive Data Meaning state.

Preserve:

- shared-key correspondence and sequence membership/order → Data Meaning;
- referential integrity, temporal monotonicity, mandatory participation → Constraint;
- requested topology/scope/horizon/Conditions → Generation;
- topology capability/limitations → Strategy;
- single-table work does not fabricate relationship state;
- time-series is not reduced to a timestamp physical type;
- multi-table is not reduced to provider/foreign-key metadata;
- whole-result completion covers every mandatory coordinated scope;
- per-table/per-row Evidence does not automatically establish joined/trajectory claims;
- topology presets are convenience syntax, not sole durable semantics;
- composite topology must remain representable;
- relationship correction creates new Data Meaning revision semantics for future work.

A complete baseline claim requires at least one supported self-contained Strategy path for each family. Delivery may be staged and Strategies may support subsets.

### Phase 006 experience authority

Human/programmatic surfaces MUST preserve equivalent material distinctions among:

- owner semantic state;
- operational state;
- current actionability;
- recovery/current-authority continuity;
- compatibility/limitations;
- disclosure state;
- historical-knowledge quality.

In particular:

- `queued` remains distinct from blocked/incompatible/denied/indeterminate/failure;
- regressive recovery must expose current mutation authority as unverified until continuity is re-established;
- reconstructed/partial/unknown history remains explicit;
- capability-specific outages identify the affected capability/consequence rather than `degraded=true`;
- driver readiness is not cluster runtime readiness;
- withheld/redacted/unknown/unavailable/absent remain distinct where disclosure policy allows;
- when existence itself is protected, outward responses may intentionally avoid distinguishing absent from forbidden while internal audit remains precise;
- synthetic origin, privacy Evidence, formal privacy guarantee, current export authorization and external release approval remain separate;
- topology presets cannot hide actual logical scopes/structural semantics;
- constituent progress does not imply whole-result completion;
- normal queueing/readiness blockage cannot rely only on generic exception handling;
- next-action guidance must not disguise semantic change as retry.

## 006-I reconciliation rules

006-I is the controlled point for promoting accepted Phase 006 authority into architecture/ADRs and then back-propagating it into Phase 005 planning.

Agents MUST:

- preserve Phase 001–005 historical phase records rather than rewriting them;
- update current canonical architecture/ADR authority where Phase 006 materially changes architecture requirements;
- then update only affected current implementation-planning authority;
- decide explicitly whether existing ADRs can be refined or a new/superseding ADR is required;
- replay affected architecture fitness/scenario obligations when the reconciliation changes a material seam;
- keep production implementation unauthorized.

At minimum 006-I must address recovery authority, runtime distribution closure, scale/degraded operation, privacy/release boundaries, structured topology, the Phase 006 experience dimensions, non-disclosing security views/errors, and resulting verification/conformance obligations.

## Anti-collapse rules

Do not create universal `Context`, `Session`, `Manager`, `Registry`, `Metadata`, `State`, `Result`, `Quality`, `Run`, `Artifact`, `Security`, `Privacy`, `Resource`, `DegradedMode`, `Relationship`, `DataTopology`, `Readiness` or `Actionability` god-owners.

Do not make DataFrame, path/table alias, loaded model, database row, scheduler job, provider foreign-key metadata, topology preset or platform ID canonical semantic identity.

Do not equate runtime success, Evidence, security authorization, external governance approval, physical artifact existence or constituent completion with another owner's semantic state.

Do not use current/latest values in place of exact historical refs.

## Documentation synchronization

When accepted design changes:

- cross-cutting authority → `docs/authority/`;
- concepts → `docs/concepts/`;
- synchronizations → `docs/synchronizations/`;
- actor/programmatic experience → `docs/experience/`;
- architecture/rationale → `docs/architecture/` and ADRs;
- only then back-propagate current rules into `docs/implementation/`;
- phase records remain history, not sole current authority.

## Current next group

**006-I — Architecture/ADR Reconciliation, Canonical Authority Promotion & Planning Back-Propagation**
