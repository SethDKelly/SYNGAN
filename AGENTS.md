# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Current authority state

**Phase 006 design/planning refinement is current. Production implementation is NOT authorized.**

006-I has completed architecture/ADR reconciliation and implementation-planning back-propagation. Current next is **006-J**.

Agents MUST NOT create production package scaffolding, source code, database schemas/migrations, runtime/Spark/security/platform adapters, executable verification suites, CI workflows, deployment infrastructure or benchmark harnesses until a later explicit implementation-authority phase authorizes them.

## Progressive disclosure

For material work:

1. read `docs/index.md`;
2. read only directly relevant cross-cutting authority under `docs/authority/`;
3. read `docs/synchronizations/core-synchronizations.md` for coordination-sensitive work;
4. read `docs/experience/phase-006-recovery-security-degraded-history-topology-experience-contract.md` for current experience semantics;
5. read `docs/architecture/phase-006-architecture-reconciliation-contract.md` **before** the Phase 004 baseline for affected architecture;
6. read `docs/implementation/phase-006-implementation-planning-reconciliation.md` **before** affected Phase 005 planning;
7. use ADRs for rationale/history, not as replacement normative authority;
8. use `docs/backlog/index.md` only for blocker/deferred classification;
9. read the active Phase 006 record/index.

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

## Current design counts

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
```

No `SYNC-16` is accepted.

## Current architecture/planning precedence

```text
Phase 006 upstream authority / experience
        ↓
Phase 006 Architecture Reconciliation
        ↓
Phase 004 architecture baseline
        ↓
Phase 006 Implementation-Planning Reconciliation
        ↓
Phase 005 planning details
```

Where a Phase 004/005 statement conflicts with an explicit Phase 006 reconciliation rule, the Phase 006 rule governs.

## Non-negotiable recovery authority

Agents MUST preserve:

- restored persistence is not proof of current writer/cancellation/security authority;
- potentially regressive recovery enters recovery-restricted/quarantine semantics;
- a fresh non-regressing recovery-authority frontier is required before write/promote/retry authority resumes;
- restored `AttemptEpoch`, `StateVersion`, cancellation generation or grant state is insufficient by itself;
- surviving workers never regain old writer authority merely because they remain alive;
- verified immutable effects may be adopted only by fresh current authority after reconciliation;
- missing post-backup canonical facts may be reconstructed/partial/unknown/unavailable and must not be fabricated;
- provider credential/namespace/native-fence rotation may be required when stale workers can bypass framework fencing.

ADR-0009 extends ADR-0005; both remain active.

## Non-negotiable runtime/package closure

Agents MUST preserve:

- acquisition closure and distributed runtime closure are separate requirements;
- driver/coordinator import or implementation resolution is not proof of worker/executor readiness;
- every material worker role, including dynamically added workers, must inherit/prove compatible exact implementation closure;
- missing dependencies/artifacts must not trigger undeclared installation, public model-hub lookup, remote inference or other fallback;
- one implementation binding may resolve multiple packages/native libraries/codecs/model/tokenizer/state components;
- large Learned State/model artifacts must not universally require driver loading/broadcast;
- the supported baseline includes at least one source-derived/local free-form-text path needing no pretrained model or runtime network service.

ADR-0010 extends ADR-0004 and ADR-0008.

## Structured-data topology authority

The first complete structured-data capability target includes:

```text
single-table
time-series
multi-table shared-key
```

Preserve:

- `Relationship` is not a standalone concept/resource owner;
- structural shared-key/sequence semantics are Data Meaning-owned descriptive state;
- referential/temporal validity remains Constraint authority;
- requested topology/scope/horizon remains Generation authority;
- Strategy owns topology capability/limitations;
- topology presets may be ergonomic input but are not durable semantic authority;
- topology must remain composable, including multi-table subjects with time-series children;
- source/output/manifests must support logical multi-scope representation;
- whole-result completion covers every mandatory constituent and cross-scope requirement;
- physical partition/file order is not time-series semantic order;
- per-table/per-row Evidence does not automatically establish whole-topology claims.

## Scale/admission/degraded authority

Agents MUST preserve:

- enterprise scale is multidimensional;
- source-size-proportional driver stages invalidate enterprise-scale claims for that path;
- resource pressure may queue/block/retry but cannot silently reduce quantity, horizon, topology scope, Evaluation coverage, Constraint strength or security posture;
- approximation belongs to the semantic owner and cannot arise as an undeclared runtime fallback;
- degraded operation is capability-specific rather than one global state;
- queue/deferred, blocked, incompatible, denied and indeterminate remain distinct;
- progress/task completion never establishes semantic completion by itself.

## Privacy/disclosure/release authority

Agents MUST preserve:

- synthetic origin does not imply privacy/anonymization/safe release;
- self-contained/offline does not imply privacy;
- privacy/disclosure findings remain Criterion/Evaluation/Evidence scoped;
- favorable empirical Evidence is not a formal privacy guarantee;
- differential privacy is not part of the initial baseline;
- future composable DP with independent accounting state MUST reopen concept discovery before implementation;
- do not add generic `epsilon`, `delta`, privacy-budget or guarantee fields as implementation shortcuts;
- external Use/Release Decision remains outside current SYNGAN concept authority;
- current authorization/redaction may block/shape access without rewriting Generation/Evidence/Provenance history;
- when existence is protected, outward errors/views may intentionally be non-disclosing while internal audit remains precise;
- no universal `private`, `safe`, `safe_to_release` or privacy score is accepted.

## Human/programmatic experience authority

Surfaces must preserve equivalent material distinctions for:

- owner semantic state;
- operational state;
- current actionability;
- authority continuity;
- compatibility/limitations;
- disclosure state;
- historical-knowledge quality.

Do not collapse these into one universal status/result/error.

Programmatic clients must be able to determine safe reason/category, retry/resume qualification and legitimate next action where disclosure permits.

Historical fact, reconstructed fact, partial history, unavailable retained material and unknown occurrence remain distinct.

## Frozen/current planning rule

The current planning overlay is:

`docs/implementation/phase-006-implementation-planning-reconciliation.md`

It refines 005-A through 005-J without rewriting Phase 005 history.

Future delivery waves remain **unauthorized**. The reconciled Wave 5 target eventually includes at least one supported self-contained path for each baseline topology family.

## Anti-collapse rules

Do not create universal `Context`, `Session`, `Manager`, `Registry`, `Metadata`, `State`, `Result`, `Quality`, `Run`, `Artifact`, `Security`, `Privacy`, `Resource`, `DegradedMode`, `Relationship`, `DataTopology`, or similar god-owner.

Do not make DataFrame, table/path alias, provider foreign-key metadata, loaded model, database row, scheduler job, platform ID, topology preset or restored stale state canonical semantic authority.

Do not equate runtime success, Evidence, current authorization, release approval, physical artifact existence or reconstructed history with another owner's state.

Do not use current/latest values in place of exact historical refs.

## Documentation synchronization

When current design changes:

- cross-cutting rules → `docs/authority/`;
- concepts → `docs/concepts/`;
- synchronizations → `docs/synchronizations/`;
- experience → `docs/experience/`;
- architecture → `docs/architecture/` and ADR rationale where warranted;
- implementation planning → `docs/implementation/` only after upstream authority;
- phase records remain history, not sole current authority.

## Current next group

**006-J — Phase 006 Consolidation, Residual Design-Debt Audit & Implementation-Authority Readiness Decision**

006-J must not assume a positive result. If residual design evidence reveals a blocker, another design phase is required. Even a positive 006-J result only permits creation of a later explicit implementation-authority phase; it does not authorize coding.
