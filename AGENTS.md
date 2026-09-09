# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Current authority state

**Phase 005 implementation planning is complete. Phase 006 design refinement is current. Production implementation is NOT authorized.**

During Phase 006, agents may update design/authority/planning documentation requested by the active group, but MUST NOT create production package scaffolding, source code, database schemas/migrations, runtime/Spark/security/platform adapters, verification suites, CI workflows, deployment infrastructure or benchmark harnesses.

A future implementation-authority phase may be created only after a positive design-readiness exit explicitly authorizes it.

## Progressive disclosure

For material work:

1. read `docs/index.md`;
2. read `docs/authority/design-methodology.md` for methodology-sensitive work;
3. read `docs/architecture/phase-004-consolidated-architecture-contract.md`;
4. read `docs/implementation/phase-005-consolidated-implementation-planning-contract.md`;
5. read the active Phase 006 record/index and only detailed authorities affected by the design question;
6. consult `docs/discovery/post-planning-concept-revalidation-structured-topology-candidates.md` for single-table/time-series/multi-table candidate evidence when topology is relevant;
7. consult `docs/backlog/index.md` for blocker/deferred classification, not as canonical design truth;
8. use ADRs for rationale/history rather than as replacement for current canonical authority.

Do not load or copy the entire documentation corpus by default.

## Authority order

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation planning
  > future code / deployment
  > ADR rationale / phase history / discovery / backlog / examples
```

Later feasibility evidence may justify reopening upstream authority. Do not patch a genuine design conflict only inside an implementation-plan document.

## Phase 006 design rules

Phase 006 exists because 005-K found four design-readiness blockers:

```text
BDR-001  regressive restore / temporal operational authority
BDR-002  post-planning adversarial end-to-end validation
BDR-003  representative Strategy/method + topology design probes
BDR-004  initial-scope / future-extensibility closure
```

Agents MUST:

- judge candidate concepts by purpose, independent state/actions, operational principle and genericity—not by whether a persistent record/class would be convenient;
- treat `ControlPlaneIncarnation`, `HistoricalRef`, finding slots, completion basis, capability grants, deployment profiles, support claims and similar structures as mechanisms/hypotheses unless concept review proves otherwise;
- preserve the eleven accepted concepts/fifteen synchronizations unless explicit Phase 006 authority revises them;
- use representative synthesis/evaluation methods as design probes, never as semantic templates;
- keep CTGAN/PyTorch/Spark/Databricks/provider behavior downstream of concept authority;
- preserve deliberate initial-scope exclusions without hard-coding them as permanent impossibilities;
- promote material changes to concept/synchronization/experience/architecture authority explicitly before back-propagating them into Phase 005 planning.

## Structured-data topology guardrails from 006-A

Current capability evidence explicitly considers:

```text
single-table generation
time-series table generation
multi-table generation with shared-key relationships
```

Current status:

- single-table is the existing baseline capability;
- time-series is a required Phase 006 design target but not yet guaranteed first-implementation scope;
- multi-table shared-key is a required Phase 006 design target but not yet guaranteed first-implementation scope;
- `Relationship` is reopened as a **candidate concept**, not an accepted one;
- accepted concept/synchronization counts remain eleven/fifteen until later authority changes them.

Agents MUST NOT:

- create `GenerationMode`, `DataTopologyMode`, `Table`, `Dataset`, `Series` or `TimeSeriesMode` as standalone concepts merely because an API may expose a mode parameter;
- treat a future `mode="single_table|time_series|multi_table"` parameter as the owner of semantic structure;
- hide shared-key relationships, series membership/order, cardinality or temporal semantics solely inside Strategy-private configuration, Spark metadata or generic `metadata` objects;
- assume `timestamp column` is sufficient time-series semantics;
- assume `two tables with matching column names` is sufficient relationship semantics;
- promote Relationship before 006-G proves a distinct purpose/boundary;
- reject future time-series/multi-table capability merely because the frozen Phase 005 plan focused on the current structured/single-table baseline.

When topology is relevant, preserve these provisional ownership hypotheses:

```text
field/scope semantic role                 -> Data Meaning
reusable descriptive cross-scope linkage  -> Relationship candidate (006-G decision)
prescriptive validity/integrity rule      -> Constraint
request-specific horizon/quantity/scope   -> Generation
support/limitations                       -> Synthesis Strategy
assessment/finding                        -> Evaluation / Evidence
historical derivation/use                 -> Provenance
```

A future function parameter or typed structure specification is an **experience/representation surface**, not concept authority.

## Frozen implementation-planning baseline

Until Phase 006 changes upstream authority, preserve:

- one future `src/syngan` package with inward `foundation/domain/ports/application/api/adapters/bootstrap` responsibilities;
- one durable ResourceRef/revision/SnapshotId/StateVersion/SchemaVersion substrate;
- exact SourceStateRef/candidate/sealed-snapshot/output boundaries;
- Strategy/method semantic revision separate from implementation binding/SPI/runtime version;
- Learning/Generation/Evaluation activity-specific runtime contracts;
- stable Execution with durable Attempts, AttemptEpoch/WriterFence, checkpoints, recovery and cancellation linearization;
- owner-established Evidence with bounded claim strength;
- typed canonical Provenance distinct from query projections, telemetry and security audit;
- qualified reproducibility rather than a Boolean/seed claim;
- dependency availability/identity/integrity/trust/compatibility/authorization/network/egress separation;
- non-bearer handles and non-canonical bearer secrets;
- Attempt capability no broader than semantic requirement ∩ current authorization ∩ deployment capability;
- no hidden acquisition, remote fallback or mandatory external telemetry in supported offline/no-egress profiles;
- enterprise paths without mandatory full-corpus driver-local materialization;
- provider/platform support through explicit capability negotiation;
- restore-safe recovery cannot let regressed control state resurrect stale writer authority.

Do not rewrite the historical Phase 005 implementation plans for provisional topology candidates during 006-A–006-H. 006-I owns controlled planning back-propagation after accepted upstream design decisions exist.

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

- concept changes go to `docs/concepts/`;
- synchronization changes go to `docs/synchronizations/`;
- actor/programmatic experience changes go to `docs/experience/`;
- architecture changes go to `docs/architecture/` and material rationale to ADRs when appropriate;
- only then update affected `docs/implementation/` plans;
- phase/discovery records preserve evidence/history and MUST NOT become the sole current authority.

Backlog items close only after the canonical owner reflects the accepted resolution.

## Current next group

**006-B — Temporal Authority, Disaster Recovery, Rollback, Fork & Historical-Truth Refinement**

In 006-B, `temporal` means authority over time after rollback/restore; it is distinct from time-series data semantics.