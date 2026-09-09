# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Current authority state

**Phase 005 implementation planning is complete. Phase 006 design refinement is current. Production implementation is NOT authorized.**

During Phase 006, agents may update requested design/authority/planning documentation, but MUST NOT create production package scaffolding, source code, database schemas/migrations, runtime/Spark/security/platform adapters, executable verification suites, CI workflows, deployment infrastructure or benchmark harnesses.

A future implementation-authority phase may be created only after a positive design-readiness exit explicitly authorizes it.

## Progressive disclosure

For material work:

1. read `docs/index.md`;
2. read `docs/authority/design-methodology.md` for methodology-sensitive work;
3. read only directly relevant cross-cutting authority:
   - recovery/HA → `operational-authority-continuity-regressive-recovery-contract.md`;
   - packaging/text/Spark worker closure → `self-contained-execution-runtime-distribution-closure-contract.md`;
   - scale/backpressure/approximation/degraded operation → `enterprise-scale-resource-admission-approximation-degraded-operation-contract.md`;
   - privacy/disclosure/formal guarantee/release → `privacy-disclosure-formal-guarantee-release-boundary-contract.md`;
   - structured topology/relationship semantics → `structured-data-topology-relationship-semantics-contract.md`;
4. read `docs/synchronizations/core-synchronizations.md` for cross-concept coordination;
5. read the Phase 003 consolidated experience contract for experience work;
6. read the Phase 004 consolidated architecture contract for architecture work;
7. read the Phase 005 consolidated planning contract and only affected detailed plans for planning work;
8. read the active Phase 006 record/index;
9. use ADRs for rationale/history, not as replacement current authority;
10. use `docs/backlog/index.md` only for blocker/deferred classification.

Do not load/copy the entire documentation corpus by default.

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

If later feasibility exposes a genuine upstream issue, reopen the upstream authority explicitly rather than patching only an implementation plan.

## Phase 006 state

Completed:

- **006-A** — concept/mechanism/scope revalidation;
- **006-B** — regressive-recovery/current-authority refinement;
- **006-C** — adversarial synchronization validation;
- **006-D** — Strategy/method/text/topology/runtime-distribution probes;
- **006-E** — enterprise scale/resource/approximation/backpressure/degraded-mode validation;
- **006-F** — privacy/disclosure/formal-guarantee/release-boundary validation;
- **006-G** — structured-topology/Relationship concept and baseline-scope decision.

Current next:

**006-H — Human/Programmatic Experience Closure for Recovery, Security, Degraded & Historical Workflows**.

Current design counts:

```text
accepted concepts             11
accepted synchronizations     15
reopened candidate concepts     0
```

No `SYNC-16` is accepted.

## Non-negotiable Phase 006 authority

### Recovery/current authority

Agents MUST preserve:

- restored persistence is not proof of current writer/cancellation/security authority;
- potentially regressive recovery enters continuity-unverified/recovery-quarantine semantics;
- a fresh non-regressing authority boundary is required before write-capable work resumes;
- missing post-backup canonical history is not proof of non-occurrence;
- surviving physical effects are not automatic proof of semantic transition;
- reconstruction is owner-gated and auditable;
- stale writers never regain authority merely because verified immutable effects may be adopted.

### Execution/synchronization

Agents MUST preserve:

- same-Execution retry/resume requires unchanged committed semantics **and** current authorization/dependency/platform/recovery qualification;
- inability to continue does not authorize silent source/Strategy/Learned-State/dependency/method/network substitution;
- coordinated logical Generation completion applies to the whole committed scope;
- runtime/platform success remains distinct from Learning/Generation/Evaluation semantic completion;
- checkpoint/candidate/runtime material remains non-final.

### Self-contained/runtime distribution

Agents MUST preserve:

- the supported baseline includes at least one source-derived/local free-form-text synthesis path requiring no externally acquired pretrained model or runtime network service;
- model hubs/LLM APIs/remote inference are optional explicit integrations, never hidden baseline fallback;
- one Strategy implementation binding may resolve multiple exact code/runtime/model/tokenizer/codec components;
- driver import/discovery success is not proof that Spark executors can execute the same closure;
- every material worker, including dynamically allocated workers, must inherit/prove compatible runtime closure;
- missing worker dependencies/artifacts must not trigger undeclared public-network acquisition;
- large Learned State/model artifacts must not require universal driver-local loading/broadcast.

### Enterprise scale/resource/degraded operation

Agents MUST preserve:

- enterprise scale is multidimensional; row count alone is not a support claim;
- undisclosed source-size-proportional driver/single-process stages invalidate enterprise-scale claims for that path;
- resource pressure may queue/block/retry but must not silently weaken committed semantics;
- approximation is owned by the concept whose semantics it changes, not a generic runtime fallback;
- backpressure must preserve mandatory records/scope/coverage/security obligations;
- sampled/sketched Evaluation cannot become universal Evidence because exhaustive validation is expensive;
- degraded operation is capability-specific rather than one global `degraded` state;
- progress/ETA/task completion does not establish semantic completion.

### Privacy/disclosure/release

Agents MUST preserve:

- synthetic origin does not imply privacy/anonymization/safe release;
- self-contained/offline execution is not a privacy guarantee;
- disclosure/memorization remain Criterion/Evaluation/Evidence concerns under current scope;
- favorable empirical Evidence does not become a formal privacy guarantee;
- differential privacy is not in the initial baseline;
- future composable DP/formal privacy mechanisms with independent accounting state MUST reopen concept discovery before implementation;
- Use/Release Decision remains external to current SYNGAN concept authority;
- authorization/redaction may shape current access without rewriting canonical Generation/Evidence/Provenance history.

## Structured-data topology authority — 006-G

The complete structured-data capability target includes:

```text
single-table
time-series
multi-table shared-key
```

`Relationship` is **not** a standalone concept. Material structural relationship semantics are descriptive state owned by Data Meaning.

Agents MUST preserve:

- descriptive shared-key correspondence and sequence membership/order are Data Meaning semantics;
- referential integrity, temporal monotonicity, mandatory participation and other prescriptive validity remain Constraint authority;
- requested topology, scope, horizon and topology-specific Conditions remain Generation authority;
- Strategy owns topology capability/limitations rather than relationship meaning;
- single-table work does not fabricate Relationship state;
- time-series is not reduced to a timestamp physical type;
- multi-table is not reduced to provider/foreign-key metadata;
- whole-result completion covers all mandatory coordinated scopes;
- per-table/per-row Evidence does not automatically establish joined/trajectory claims;
- a topology convenience parameter/preset is not the sole durable semantic representation;
- topology must remain composable, including multi-table subjects with time-series children;
- relationship corrections create new Data Meaning revision semantics for future work rather than rewriting history;
- architecture may later provide a stable relationship-assertion reference scoped to a Data Meaning revision without creating an independent Relationship resource/concept.

The first complete baseline claim requires at least one supported self-contained Strategy path for each of the three capability families. Implementation may be staged and individual Strategies may support subsets.

Do NOT create standalone `Relationship`, `Table`, `Series`, `Sequence`, `TimeSeries`, `Dataset` or `DataTopology` concepts/classes as semantic owners merely for implementation convenience.

## 006-H experience obligations

006-H must make the accumulated authority understandable to both human and programmatic actors without exposing internal implementation jargon as the user contract.

Experience must preserve distinctions including:

- current vs historical state;
- recovery quarantine vs ordinary failure;
- unknown vs unavailable vs withheld/redacted;
- queued vs blocked vs incompatible vs limited;
- semantic compatibility vs current runtime/worker readiness;
- synthetic vs privacy-related Evidence vs formal guarantee vs release approval;
- supported topology vs unsupported Strategy shape;
- physical completion vs semantic completion.

## Frozen implementation-planning baseline

Until 006-I deliberately back-propagates Phase 006 authority, preserve the Phase 005 planning baseline rather than rewriting it ad hoc.

Key constraints include durable identity, semantic/runtime separation, stable Execution with fenced Attempts, bounded Evidence/Provenance, explicit authorization/network semantics, no hidden acquisition, no full-corpus driver collection and capability-negotiated platforms.

## Anti-collapse rules

Do not create universal `Context`, `Session`, `Manager`, `Registry`, `Metadata`, `State`, `Result`, `Quality`, `Run`, `Artifact`, `Security`, `Privacy`, `Resource`, `DegradedMode`, `Relationship` or `DataTopology` god-owners.

Do not make DataFrame, path/table alias, loaded model, database row, scheduler job, provider foreign-key metadata or platform ID canonical semantic identity.

Do not equate runtime success, Evidence, security authorization, external governance approval, topology preset or physical artifact existence with another owner's semantic state.

Do not use current/latest values in place of exact historical refs.

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

**006-H — Human/Programmatic Experience Closure for Recovery, Security, Degraded & Historical Workflows**
