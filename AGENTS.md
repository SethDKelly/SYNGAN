# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Current authority state

**Phase 006 is complete. The design is complete enough for a later explicit implementation-authority phase, but production implementation is still NOT authorized.**

No agent may create production package scaffolding, source code, database schemas/migrations, Spark/runtime/security/platform adapters, executable verification suites, CI workflows, deployment infrastructure or benchmark harnesses until a later explicit implementation-authority phase is entered and authorizes defined slices.

## Progressive disclosure

For material work:

1. read `docs/index.md`;
2. read `docs/authority/phase-006-consolidated-design-readiness-contract.md` for the current readiness/implementation boundary;
3. read only directly relevant cross-cutting authority under `docs/authority/`;
4. read `docs/synchronizations/core-synchronizations.md` for coordination-sensitive work;
5. read `docs/experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md` for current experience semantics;
6. read `docs/architecture/phase-006-architecture-reconciliation-contract.md` before the Phase 004 baseline for affected architecture;
7. read `docs/implementation/phase-006-implementation-planning-reconciliation.md` before affected Phase 005 planning;
8. use ADRs for rationale/history, not as replacement normative authority;
9. use `docs/backlog/index.md` for deferred implementation/release debt;
10. read Phase 006 records only for design history/evidence.

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

## Final design counts

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
```

No `SYNC-16`.

## Current readiness decision

```text
DESIGN COMPLETE ENOUGH FOR A LATER
EXPLICIT IMPLEMENTATION-AUTHORITY PHASE
```

This means the known design blockers are closed and remaining uncertainty is primarily representational/delivery work. It does **not** grant implementation permission by itself.

## Current implementation-facing precedence

```text
Phase 006 design authority / experience
        ↓
Phase 006 Architecture Reconciliation
        ↓
Phase 004 baseline where not refined
        ↓
Phase 006 Implementation-Planning Reconciliation
        ↓
Phase 005 planning where not refined
        ↓
future explicit implementation-authority phase
```

## Non-negotiable recovery authority

Preserve:

- restored persistence is not proof of current writer/cancellation/security authority;
- potentially regressive recovery enters recovery-restricted/quarantine semantics;
- a fresh non-regressing recovery-authority frontier is required before mutation resumes;
- restored AttemptEpoch/StateVersion/cancellation/grant state is insufficient by itself;
- surviving workers never regain old writer authority merely because they remain alive;
- verified immutable effects may be adopted only by fresh current authority after reconciliation;
- reconstructed/partial/unknown/unavailable history must remain distinguishable;
- provider credential/namespace/native-fence rotation may be required when stale workers can bypass framework fencing.

## Non-negotiable runtime/package closure

Preserve:

- acquisition closure and distributed runtime closure are separate requirements;
- driver/coordinator import success is not proof of worker/executor readiness;
- every material worker role, including dynamically added workers, must inherit/prove exact compatible closure;
- missing dependencies/artifacts must not trigger undeclared installation, public model-hub lookup, remote inference or fallback;
- one implementation binding may resolve multiple packages/native libraries/codecs/model/tokenizer/state components;
- large Learned State/model artifacts must not universally require driver loading/broadcast;
- the supported baseline includes at least one source-derived/local free-form-text path needing no pretrained model or runtime network service.

## Structured-data topology authority

The complete structured-data capability target includes:

```text
single-table
time-series
multi-table shared-key
```

Preserve:

- `Relationship` is not a standalone concept/resource owner;
- structural shared-key/sequence semantics are Data Meaning-owned;
- referential/temporal validity remains Constraint authority;
- requested topology/scope/horizon remains Generation authority;
- Strategy owns topology capability/limitations;
- topology presets are ergonomic input, not durable semantic authority;
- topology remains composable, including multi-table subjects with time-series children;
- source/output/manifests support logical multi-scope representation;
- whole-result completion covers every mandatory constituent/validation;
- physical partition/file order is not time-series semantic order.

## Scale/admission/degraded authority

Preserve:

- enterprise scale is multidimensional;
- source-size-proportional driver stages invalidate enterprise-scale claims for that path;
- resource pressure may queue/block/retry but cannot silently reduce quantity, horizon, topology scope, Evaluation coverage, Constraint strength or security posture;
- approximation belongs to the semantic owner and cannot arise as undeclared runtime fallback;
- degraded operation is capability-specific rather than one global state;
- queued/deferred, blocked, incompatible, denied and indeterminate remain distinct;
- progress/task completion does not establish semantic completion.

## Privacy/disclosure/release authority

Preserve:

- synthetic origin or offline operation does not imply privacy/anonymization/safe release;
- privacy/disclosure findings remain Criterion/Evaluation/Evidence scoped;
- favorable empirical Evidence is not a formal privacy guarantee;
- differential privacy is not part of the initial baseline;
- future composable DP with independent accounting state MUST reopen concept discovery before implementation;
- do not add generic epsilon/delta/privacy-budget/guarantee fields as implementation shortcuts;
- external Use/Release Decision remains outside current SYNGAN concept authority;
- current authorization/redaction may shape access without rewriting canonical history;
- existence-protected outward responses may intentionally be non-disclosing while internal audit remains precise;
- no universal `private`, `safe`, `safe_to_release` or privacy score is accepted.

## Human/programmatic experience authority

Surfaces preserve equivalent material distinctions for semantic state, operational state, actionability, authority continuity, compatibility/limitations, disclosure and historical-knowledge quality.

Do not collapse these into one universal status/result/error.

Programmatic clients must be able to determine safe reason/category, retry/resume qualification and legitimate next action where disclosure permits.

## Current future planning

The current future wave sequence is recorded in `docs/implementation/phase-006-implementation-planning-reconciliation.md`.

No wave is authorized yet.

A complete-baseline implementation must eventually provide at least one supported self-contained Strategy path for single-table, time-series and multi-table shared-key generation, with baseline source-derived/local text support.

## Anti-collapse rules

Do not create universal `Context`, `Session`, `Manager`, `Registry`, `Metadata`, `State`, `Result`, `Quality`, `Run`, `Artifact`, `Security`, `Privacy`, `Resource`, `DegradedMode`, `Relationship`, `DataTopology` or similar god-owner.

Do not make DataFrame, table/path alias, provider foreign-key metadata, loaded model, database row, scheduler job, platform ID, topology preset or restored stale state canonical semantic authority.

Do not equate runtime success, Evidence, current authorization, release approval, physical artifact existence or reconstructed history with another owner's state.

Do not use current/latest values in place of exact historical refs.

## Recommended next phase

**Phase 007 — Implementation Authority, Controlled Bootstrap & Evidence-Gated Delivery** is recommended but not active.

When explicitly entered, its first subgroup must lock current authority and state exactly which implementation slices are authorized and what evidence gates each slice. Until then, production coding remains prohibited.
