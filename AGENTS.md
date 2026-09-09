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
3. read `docs/architecture/phase-004-consolidated-architecture-contract.md`;
4. read `docs/implementation/phase-005-consolidated-implementation-planning-contract.md`;
5. read the active Phase 006 record/index and only the detailed 005 plan affected by the design question;
6. follow only directly relevant concept/synchronization/experience/architecture authority;
7. use ADRs for rationale/history rather than as replacement for current canonical authority;
8. consult `docs/backlog/index.md` for blocker/deferred classification, not as canonical design truth.

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

## Phase 006 design rules

Phase 006 exists because 005-K found four design-readiness blockers:

```text
BDR-001  regressive restore / temporal authority
BDR-002  post-planning adversarial end-to-end validation
BDR-003  representative Strategy/method design probes
BDR-004  initial-scope / future-extensibility closure
```

Agents MUST:

- judge candidate concepts by purpose, independent state/actions, operational principle and genericity—not by whether a persistent record/class would be convenient;
- treat `ControlPlaneIncarnation`, `HistoricalRef`, finding slots, completion basis, capability grants, deployment profiles, support claims and similar structures as mechanisms/hypotheses unless concept review proves otherwise;
- preserve the eleven concepts/fifteen synchronizations unless explicit Phase 006 evidence justifies revision;
- use representative synthesis/evaluation methods as design probes, never as semantic templates;
- keep CTGAN/PyTorch/Spark/Databricks/provider behavior downstream of concept authority;
- preserve deliberate initial-scope exclusions without hard-coding them as permanent impossibilities;
- promote material changes to concept/synchronization/experience/architecture authority explicitly before back-propagating them into Phase 005 planning.

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

## Non-negotiable anti-collapse rules

Do not:

- create universal `Context`, `Session`, `Manager`, `Registry`, `Metadata`, `State`, `Result`, `Quality`, `Run`, `Artifact`, `Security` or similar god-owner merely to simplify representation;
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

## Scope discipline

Current initial scope is structured/tabular synthesis.

Relational/multi-table synthesis, mechanism-specific formal privacy, external release/use governance and broad Strategy/Evaluation catalog breadth remain explicit scope decisions under Phase 006 review.

Do not expand those domains by accident, but do not introduce representation assumptions that permanently prevent future explicit design expansion.

## Verification and future implementation

005-B remains the accepted future verification architecture (V0-V11, AF-01..20, Q0-Q4). No executable verification suite should be created during Phase 006.

If Phase 006 ultimately approves later implementation, future tests derive their oracle from the then-current accepted authority and must not mock away the distributed, concurrency, security, persistence, recovery, history or scale property under test.

## Documentation synchronization

When Phase 006 changes accepted design:

- concept changes go to `docs/concepts/`;
- synchronization changes go to `docs/synchronizations/`;
- actor/programmatic experience changes go to `docs/experience/`;
- architecture changes go to `docs/architecture/` and material rationale to ADRs when appropriate;
- only then update affected `docs/implementation/` plans;
- phase records preserve history and MUST NOT become the sole current authority.

Backlog items close only after the canonical owner reflects the accepted resolution.

## Current next group

**006-A — Post-Planning Concept Completeness, Mechanism-vs-Concept & Scope-Boundary Revalidation**