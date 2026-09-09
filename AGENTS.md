# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Current authority state

**Phase 006 is complete. Phase 007 logical subgroup design exists, but Phase 007 is NOT active and production implementation is still NOT authorized.**

No agent may create production package scaffolding, source code, database schemas/migrations, Spark/runtime/security/platform adapters, executable verification suites, CI workflows, deployment infrastructure or benchmark harnesses until **007-A is explicitly entered and completes the implementation-authority lock**.

The planned Phase 007 structure is `docs/phases/007/index.md`.

## Progressive disclosure

For material work:

1. read `docs/index.md`;
2. read `docs/authority/phase-006-consolidated-design-readiness-contract.md`;
3. read only directly relevant cross-cutting authority under `docs/authority/`;
4. read `docs/synchronizations/core-synchronizations.md` for coordination-sensitive work;
5. read `docs/experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md`;
6. read `docs/architecture/phase-006-architecture-reconciliation-contract.md` before affected Phase 004 architecture;
7. read `docs/implementation/phase-006-implementation-planning-reconciliation.md` before affected Phase 005 planning;
8. use ADRs for rationale/history, not as replacement normative authority;
9. use `docs/backlog/index.md` for deferred implementation/release debt;
10. read `docs/phases/007/index.md` only for planned implementation-authority sequencing until Phase 007 is explicitly activated.

Do not load/copy the entire documentation corpus by default.

## Authority order

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation planning
  > explicit implementation authority
  > code / deployment
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

This means known design blockers are closed. It does **not** grant implementation permission by itself.

## Planned Phase 007 authorization model

Phase 007 is designed around incremental authority:

```text
007-A authority lock
   ↓
007-B toolchain / verification bootstrap
   ↓
007-C source/package topology
   ↓
007-D identity/public contracts
   ↓
007-E persistence/history
   ↓
007-F distributed data/topology
   ↓
007-G runtime/dependency/security closure
   ↓
007-H Execution/recovery
   ↓
007-I Evidence/history/reproducibility
   ↓
007-J bounded single-table vertical proof
   ↓
007-K exit
```

No subgroup is authorized merely because it appears in this plan.

007-A is governance-only. It should normally authorize **007-B only** after locking the exact baseline, change-control rules, allowed file/change surface and required evidence gates.

Agents MUST NOT interpret `Phase 007 planned` or `subgroup design complete` as blanket permission to implement A-K.

## Change-classification stop rule

When implementation authority eventually exists:

- Class 0/1 work proceeds only within the active authorized slice;
- Class 2 public/persisted/compatibility changes require the prescribed plan/migration/contract evidence;
- a Class 3 architecture conflict stops ordinary implementation and reopens architecture authority;
- a Class 4 semantic/experience conflict stops ordinary implementation and reopens the appropriate design layer.

`The code/library/platform already works this way` is not authority to bypass this rule.

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

Phase 007-J is intentionally only a bounded single-table implementation proof. Its code MUST NOT hard-code the shared substrate so that time-series or multi-table support later requires semantic redesign.

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

## Anti-collapse rules

Do not create universal `Context`, `Session`, `Manager`, `Registry`, `Metadata`, `State`, `Result`, `Quality`, `Run`, `Artifact`, `Security`, `Privacy`, `Resource`, `DegradedMode`, `Relationship`, `DataTopology` or similar god-owner.

Do not make DataFrame, table/path alias, provider foreign-key metadata, loaded model, database row, scheduler job, platform ID, topology preset or restored stale state canonical semantic authority.

Do not equate runtime success, Evidence, current authorization, release approval, physical artifact existence or reconstructed history with another owner's state.

Do not use current/latest values in place of exact historical refs.

## Current next step

**007-A — Implementation Authority Lock, Canonical Baseline, Change Control & Slice Authorization** is the proposed next subgroup.

It is not active until explicitly entered. Until that happens and 007-A completes its governance lock, production coding remains prohibited.
