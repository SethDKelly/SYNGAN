---
type: Implementation Authority
title: Phase 007 Implementation Authority Lock
status: active
---

# Phase 007 Implementation Authority Lock

## Purpose

Convert the positive Phase 006 design-readiness decision into the first **actual, bounded implementation authority** for SYNGAN.

This contract activates Phase 007 governance and authorizes **007-B — Repository/Toolchain Bootstrap, Reproducible Environment & Verification Harness only**.

It does **not** grant blanket authority for 007-C through 007-K and does not authorize production domain/runtime/platform behavior beyond the explicitly bounded 007-B bootstrap surface.

## Entry baseline

Phase 007-A was entered against:

```text
repository: SethDKelly/SYNGAN
branch:     main
commit:     843a518c12f7482229cfb012da658887cb92dfaa
```

At entry, GitHub reported `main` as unprotected with no required status checks.

This SHA is the **Phase 007 entry baseline**, not a semantic version and not a frozen forever branch head. Every later subgroup must record its own implementation/evidence baseline when it begins.

## Governing authority precedence

Implementation work SHALL use this precedence:

```text
1. docs/authority/
   including Phase 006 Consolidated Design Readiness
        ↓
2. accepted concepts + synchronizations
        ↓
3. current experience authority
   Phase 003 baseline + Phase 006 overlay
        ↓
4. current architecture authority
   Phase 006 reconciliation + Phase 004 where not refined
        ↓
5. current implementation planning
   Phase 006 reconciliation + Phase 005 where not refined
        ↓
6. THIS Phase 007 implementation authority
   + active subgroup authority/evidence gate
        ↓
7. production source/config/migrations/tests
        ↓
8. derived/generated/runtime/platform state
```

ADRs explain rationale but do not outrank newer canonical architecture. Phase/discovery records preserve history but do not replace promoted authority.

## Locked design counts

At 007-A entry:

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
```

No `SYNC-16` exists.

The complete structured-data target remains:

```text
single-table
time-series
multi-table shared-key
```

Phase 007 must not hard-code a representation that makes the latter two impossible merely because 007-J proves only a single-table Strategy.

## Implementation rule

> **Implementation realizes accepted authority. Working code, library conventions, platform behavior, test convenience, performance pressure, or model-library APIs do not silently redefine SYNGAN semantics.**

If implementation reveals genuine infeasibility, the smallest affected authority layer is reopened explicitly before the conflicting behavior is accepted.

## Change classification and stop/reopen rules

007-A carries forward the 005-A change classes, updated for Phase 006 authority.

### Class 0 — local/non-contractual maintenance

Examples: typo/comment cleanup, behavior-preserving internal rename, bounded fixture cleanup.

May proceed inside the active subgroup when it does not widen scope.

### Class 1 — implementation realization

Examples: internal module implementing an accepted contract, approved dependency addition, test/tool implementation, adapter implementation inside an already-authorized slice.

Requirements:

- trace to current authority and active subgroup;
- verification evidence;
- dependency/network/security implications recorded where material.

### Class 2 — public/persisted/compatibility contract

Examples: public API/SPI shape, persisted schema/wire encoding, migration behavior, support/compatibility contract, security-capability boundary.

Requirements:

- explicit implementation-authority update in the active slice;
- compatibility/migration analysis;
- contract/golden/conformance evidence as applicable.

### Class 3 — architecture-affecting

Any change that weakens, relocates, contradicts, or materially reinterprets current architecture—including Phase 006 recovery, runtime-closure, topology, scale, privacy/release, history, or experience-preservation obligations.

**STOP ordinary implementation.** Document the conflict and reopen the smallest canonical architecture/ADR authority before coding around it.

### Class 4 — semantic/experience

Any change to concept purpose/ownership/lifecycle/invariant, synchronization responsibility, or required actor/programmatic meaning.

**STOP ordinary implementation.** Reopen the appropriate design/concept/synchronization/experience authority explicitly.

A convenient API, vendor SDK, model object, schema, table layout, runtime result, or passing test does not downgrade a Class 3/4 conflict into Class 1.

## Phase-wide authorization model

Phase 007 uses **incremental authority**.

```text
007-A complete
    ↓
007-B AUTHORIZED

007-C .. 007-K
    NOT AUTHORIZED YET
```

Each later subgroup requires:

1. prior subgroup completion evidence;
2. explicit review of unresolved issues/waivers;
3. an explicit proceed/authorization decision.

The existence of the Phase 007 plan is not blanket implementation permission.

## 007-B authorized scope

007-B may create or update only repository/toolchain/verification/bootstrap material necessary to establish a reproducible implementation environment.

### Authorized repository surfaces

007-B MAY introduce/update, as needed:

```text
pyproject.toml
uv.lock
.python-version              # optional developer convenience; not semantic authority
.gitignore                    # bounded build/cache/tool entries only
tools/verify.py
other narrowly scoped tools/bootstrap verification scripts

tests/unit/                  # bootstrap/tooling smoke tests only in 007-B
tests/fitness/               # repository/authority/toolchain fitness only in 007-B
tests/support/               # only if required by bootstrap verification

.github/workflows/           # verification-only CI; no publish/deploy workflow
.github/pull_request_template.md

README.md
AGENTS.md
docs/                        # authority/evidence/navigation updates
```

007-B MUST NOT create `src/syngan/` or substantive domain/application/port/adapter behavior. Source/package topology and executable dependency-direction enforcement are owned by 007-C.

007-B MUST NOT create database schemas/migrations, Spark runtime behavior, model/Strategy implementation, secrets/security provider integration, deployment infrastructure, benchmark harnesses, or release/publishing automation.

### Authorized toolchain baseline

Unless 007-B proves an explicit compatibility conflict requiring authority review, it SHALL realize the Phase 005-C selections:

- Python floor: `>=3.11`;
- project/environment/lock manager: `uv`;
- build backend: Hatchling;
- test runner: pytest;
- property/stateful verification: Hypothesis;
- portable-core Python socket deny: pytest-socket;
- lint/format: Ruff;
- static typing: mypy;
- import/dependency fitness: Import Linter;
- coverage diagnostics: coverage.py / pytest-compatible coverage integration;
- CI surface: GitHub Actions verification only, if introduced.

These are implementation tools, not semantic dependencies.

### Dependency authorization for 007-B

007-B may add only build/development/verification dependencies required for the above toolchain.

No new production runtime dependency is authorized in 007-B beyond what the packaging mechanism itself requires for build metadata.

In particular, 007-B does **not** authorize base/runtime installation of:

- PySpark;
- PyTorch;
- Hugging Face/Transformers;
- Databricks SDKs/connectors;
- MLflow;
- cloud-provider SDKs;
- remote-model/service clients;
- database drivers/ORMs;
- telemetry exporters.

Those belong to later explicitly authorized slices/optional groups.

## Development network/offline posture

SYNGAN distinguishes explicit **environment provisioning** from **runtime/test acquisition**.

007-B may use network access during an explicit developer/CI dependency-provisioning step needed to create/use the repository lock and install declared tooling.

Once the portable/core verification profile begins, tests MUST NOT silently download/install packages, fetch models, call public model hubs, invoke hosted inference, or use undeclared external network fallback.

pytest-socket or equivalent repository-owned checks must establish the Python-socket-denied portable-core profile, with narrowly named exceptions only for local process/runtime plumbing when later Spark profiles require it.

## Branch/review policy at 007-A entry

At the Phase 007 entry baseline, `main` is unprotected and no required checks are configured.

007-A therefore adopts a transparent transitional policy:

- direct-to-main changes are technically and procedurally permitted for **007-B only** when the user explicitly authorizes the subgroup;
- direct-to-main does not count as independent review or CI evidence;
- every 007-B change must remain inside the authorized surface and must record the verification commands/results used;
- 007-B should establish at least one repository verification workflow/command so later subgroups can be gated by executable checks;
- 007-C must revisit whether material production-source changes should require a PR/review workflow once the verification substrate exists;
- no document may claim GitHub branch protection or required checks are enabled unless repository state actually confirms it.

## Verification authority

The test oracle comes from accepted authority, not current code.

007-B must bootstrap enough verification infrastructure to support later V0-V11 work and must begin executable protection of the architecture fitness model.

The existing Phase 005-B AF-01..AF-20 obligations remain active. Phase 006 adds required future obligations equivalent to:

- **AF-21** non-regressing recovery authority;
- **AF-22** distributed worker runtime closure;
- **AF-23** topology semantic preservation;
- **AF-24** whole-topology completion;
- **AF-25** lossless admission/backpressure;
- **AF-26** privacy/release boundary;
- **AF-27** historical-knowledge fidelity;
- **AF-28** orthogonal programmatic state.

007-B does not need executable domain tests for AF-21..AF-28 before domain/source code exists. It must, however, create a verification structure in which those checks can later be added without bypassing the normal gate.

## Required acceptance evidence for every material subgroup

Before a subgroup may be marked complete, its phase record/evidence must identify, where applicable:

- exact entry repository/branch/commit baseline;
- upstream authority implemented;
- bounded files changed;
- change classification(s);
- dependencies added/removed and rationale;
- commands/tests/fitness checks executed and their results;
- migration/public/compatibility impact;
- network/offline/egress implications;
- security/disclosure implications;
- distributed/recovery implications;
- scale/resource assumptions and explicit non-claims;
- waivers/failures/deferred work with owner/backlog reference;
- whether any Class 3/4 conflict was found;
- explicit decision whether the next subgroup is authorized.

A subgroup is not complete merely because code compiles, a command exits zero once, or a platform/model demo works.

## 007-B completion gate

007-B may be considered complete only when, at minimum:

1. repository-owned Python project/build/test/tool metadata exists;
2. dependency resolution is reproducible from committed metadata/lock state;
3. the Python `>=3.11` floor is explicit;
4. lint/format/type/test/fitness/bootstrap commands are stable and documented;
5. portable-core Python tests deny undeclared outbound sockets by default;
6. the verification harness can run from a clean declared environment without hidden global prerequisites;
7. no substantive `syngan` production package/domain behavior has been introduced early;
8. no unauthorized production runtime dependency has entered the base closure;
9. CI/repository verification evidence is available if a workflow is introduced, without claiming enforcement that does not exist;
10. 007-B records its evidence and explicitly requests/receives authority before 007-C begins.

## Non-negotiable inherited invariants

007-B and every later subgroup remain bound by current Phase 006 authority, including:

- restored stale control state != current mutation authority;
- driver import success != distributed worker readiness;
- no hidden dependency/model acquisition;
- topology presets != durable semantic topology;
- single-table implementation must not preclude time-series/multi-table shared-key support;
- resource pressure cannot silently weaken committed semantics;
- synthetic/offline/favorable Evidence != formal privacy guarantee/release approval;
- direct/reconstructed/partial/unavailable/unknown history remain distinct;
- semantic completion != runtime/platform success;
- no universal Session/Context/Manager/Metadata/Result/Relationship/DataTopology god-owner.

## 007-A exit decision

**007-A authority lock: COMPLETE.**

**Phase 007: ACTIVE.**

**007-B: AUTHORIZED.**

**007-C through 007-K: NOT YET AUTHORIZED.**

Production implementation authority currently extends only to the bounded repository/toolchain/verification bootstrap described above.
