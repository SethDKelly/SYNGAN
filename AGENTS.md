# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Current authority state

**Phase 007 is ACTIVE under a bounded implementation-authority lock.**

Current authorization:

```text
007-A  COMPLETE
007-B  AUTHORIZED / NEXT
007-C..007-K  NOT AUTHORIZED
```

Canonical implementation authority:

`docs/implementation/phase-007-implementation-authority-lock.md`

Agents may implement **007-B repository/toolchain/verification bootstrap only**. They MUST NOT create `src/syngan/`, substantive domain/application/port/adapter behavior, schemas/migrations, Spark/runtime/security/platform behavior, benchmark infrastructure, or release/deployment automation until the owning later subgroup is explicitly authorized.

## Progressive disclosure

For 007-B work:

1. read `docs/index.md`;
2. read `docs/implementation/phase-007-implementation-authority-lock.md`;
3. read `docs/phases/007/index.md`;
4. read `docs/implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md` for the authorized toolchain decisions;
5. read `docs/implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md` for verification semantics;
6. load Phase 006 authority/architecture only where a particular bootstrap rule needs it.

Do not load/copy the full design corpus by default.

## Authority order

```text
docs/authority/
  > concepts / synchronizations
  > experience
  > Phase 006-reconciled architecture
  > Phase 006-reconciled implementation planning
  > Phase 007 implementation authority + active subgroup
  > code / config / tests / migrations
  > runtime/platform/generated state
```

Code does not become authority because it exists or passes tests.

## Locked counts

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
```

No `SYNC-16`.

## 007-B authorized file/change surface

Agents MAY add/update, when needed for 007-B:

```text
pyproject.toml
uv.lock
.python-version
.gitignore
tools/verify.py
narrow verification/bootstrap scripts
bootstrap-only tests/unit, tests/fitness, tests/support
verification-only .github/workflows
.github/pull_request_template.md
README.md
AGENTS.md
docs/
```

Agents MUST NOT create `src/syngan/` in 007-B.

## 007-B authorized toolchain

Unless an explicit compatibility conflict is found and escalated:

```text
Python >=3.11
uv
Hatchling
pytest
Hypothesis
pytest-socket
Ruff
mypy
Import Linter
coverage.py / pytest-compatible coverage integration
GitHub Actions verification-only workflow if introduced
```

No production/runtime PySpark, PyTorch, Hugging Face, Databricks, MLflow, cloud SDK, database/ORM, remote-model/service, or telemetry-export dependency is authorized in the 007-B base closure.

## Network/offline posture

Explicit environment/dependency provisioning may use network access.

Portable/core verification itself must deny undeclared outbound Python sockets by default and must not trigger hidden installation, public model-hub access, hosted inference, or remote fallback.

## Change classification

- Class 0 — local/non-contractual: allowed inside active scope.
- Class 1 — implementation realization: allowed only when traced to active authority and verified.
- Class 2 — public/persisted/compatibility: requires explicit implementation-authority + compatibility/migration evidence.
- Class 3 — architecture-affecting: **STOP** and reopen the smallest architecture/ADR authority.
- Class 4 — semantic/experience: **STOP** and reopen the appropriate upstream design authority.

Do not code around Class 3/4 conflicts.

## Evidence gate

Every material subgroup must retain:

- entry repository/branch/commit;
- authority implemented;
- bounded files and change classes;
- dependencies and rationale;
- commands/tests/fitness results;
- migration/compatibility impact;
- network/offline/security/disclosure impact;
- distributed/recovery/scale implications where relevant;
- explicit non-claims;
- waivers/debt;
- Class 3/4 conflicts;
- explicit next-subgroup authorization decision.

A subgroup is not complete because a command exits zero once.

## Branch/review posture

At 007-A entry, `main` was unprotected and had no required status checks.

Direct-to-main is permitted for explicitly authorized 007-B work, but it is not independent review or CI evidence. 007-B must establish repository-owned verification entry points. 007-C must revisit review/PR enforcement once executable checks exist.

## Non-negotiable design rules

Preserve at minimum:

- restored stale control state != current mutation authority;
- driver import success != distributed worker readiness;
- no hidden dependency/model acquisition or remote fallback;
- topology presets != durable semantic topology;
- 007-B/007-C implementation must not preclude time-series/multi-table shared-key support;
- resource pressure cannot silently weaken committed semantics;
- synthetic/offline/favorable Evidence != formal privacy guarantee/release approval;
- directly retained/reconstructed/partial/unavailable/unknown history remain distinct;
- semantic completion != runtime/platform success;
- no universal Session/Context/Manager/Metadata/Result/Relationship/DataTopology god-owner.

## Current next subgroup

**007-B — Repository/Toolchain Bootstrap, Reproducible Environment & Verification Harness**

Do not begin 007-C until 007-B has acceptance evidence and an explicit proceed decision.
