# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is currently in architecture/design refinement, not production implementation.**

Current authority:

- `docs/authority/phase-007-design-continuation-implementation-freeze.md`
- `docs/phases/007/index.md`
- current architecture documents relevant to the active design subgroup.

Current progression:

```text
007-A..007-C  historical/provisional bootstrap work
007-D         DESIGN COMPLETE
007-E         next eligible DESIGN subgroup — not started
implementation expansion   FROZEN
```

Accepted counts remain:

```text
concepts          11
synchronizations  15
ADRs              10
```

No `SYNC-16`.

## Primary rule

> **Design may invalidate provisional implementation; provisional implementation may not veto design.**

The existing `src/syngan`, tests, Import Linter rules, CI and package scaffold are retained feasibility/history artifacts from 007-B/007-C. They are not upstream architecture authority.

Do not reject or distort a sound design decision merely because existing code/tests would later need to change.

## What agents may do now

For an explicitly entered design subgroup, agents may:

- inspect current problem/concept/synchronization/experience/architecture authority;
- create or refine design/architecture documentation;
- compare alternatives and preserve unresolved questions;
- identify future implementation obligations or verification scenarios as **non-executable design requirements**;
- update canonical navigation/authority when a design decision is accepted;
- create an ADR only when a material architecture choice benefits from durable alternatives/rationale history.

## What agents must not do during the design freeze

Unless a later explicit implementation-reentry authority says otherwise, do **not**:

- add production source behavior;
- add persistence schemas/migrations;
- add Spark/runtime/model/platform/security adapters;
- add public API classes to crystallize a design hypothesis;
- add production serialization/wire schemas;
- add runtime/build dependencies for future capability work;
- add new tests or executable architecture/fitness restrictions for evolving design;
- add new Import Linter constraints for evolving design;
- add CI/deployment/release enforcement for evolving design;
- treat an existing test failure caused by a deliberate design change as evidence that the design itself is invalid.

Existing verification may remain in place. Do not expand it merely to encode documentation that is still under design.

## Progressive disclosure

For design work:

1. read `docs/index.md`;
2. read `docs/authority/phase-007-design-continuation-implementation-freeze.md`;
3. read `docs/phases/007/index.md`;
4. read only the concepts/synchronizations/experience/architecture directly relevant to the active design question;
5. use phase/discovery history only when rationale/history is needed.

Do not load or duplicate the full corpus by default.

## Authority order

```text
docs/authority/
  > concepts / synchronizations
  > experience
  > current architecture design
  > implementation planning
  > later explicit implementation-reentry authority
  > code / config / tests / migrations
  > runtime/platform/generated state
```

Code does not become authority because it exists or passes tests.

## Design discipline

Preserve these methodology rules:

- purpose before representation;
- concept boundaries before classes/modules/tables;
- explicit synchronizations rather than hidden coupling;
- unresolved alternatives stay visible until justified;
- representation convenience does not redefine semantic ownership;
- one concept does not imply one class/module/table/service;
- architecture mechanisms such as Resource, Reference, Handle, View and SchemaVersion are not concepts merely because they are useful;
- no universal Session/Context/Manager/Metadata/Result/Relationship/DataTopology god-owner;
- Spark-native means distributed data/control boundaries, not universal Spark ML;
- model-neutral core design must not become CTGAN/GAN/PyTorch/LLM-specific;
- enterprise scale is part of the semantic/architecture contract where it changes observable behavior.

## Non-negotiable semantic/architecture distinctions

Keep at minimum:

- restored stale control state != current mutation authority;
- driver import success != distributed worker readiness;
- topology preset != durable semantic topology;
- semantic completion != runtime/platform success;
- candidate/checkpoint/diagnostic material != promoted result;
- current state != exact historical revision/commitment;
- representation schema version != semantic revision;
- handle/view != canonical state owner;
- serialization != mutation authority;
- favorable empirical privacy Evidence != formal privacy guarantee != external release approval;
- directly retained/reconstructed/partial/unavailable/unknown history remain distinct.

## Current 007-D design result

007-D established a design foundation for:

- authority/namespace scope;
- stable logical identity;
- exact semantic revision/commitment snapshot;
- mutable state version/view freshness;
- representation schema version;
- typed references/handles;
- bounded orthogonal programmatic views;
- serialization roles without choosing a concrete wire format.

Do not implement these roles yet.

## Current next boundary

**007-E — Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline** is the next eligible **design** subgroup.

Do not begin 007-E until the user explicitly proceeds.
