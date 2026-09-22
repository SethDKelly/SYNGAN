---
type: Implementation Authority
title: Engineering Preflight — Dependency, Supply Chain, Secrets, Compatibility, Benchmark & Versioning
status: active
---

# Engineering Preflight — Dependency, Supply Chain, Secrets, Compatibility, Benchmark & Versioning

## Purpose

Define the repository-owned engineering preflight that must be satisfied before SYNGAN may make stronger release, compatibility, support, or scale claims.

This authority is downstream of current design/architecture, Phase 015 implementation/support scope, and the 016-H implementation-package/change-control contract.

## Core rule

> A deterministic repository PASS is necessary evidence for engineering hygiene; it is never by itself a release authorization, vulnerability clearance, provider certification, legal approval, or scale qualification.

The preflight keeps five evidence classes distinct:

~~~text
repository-deterministic evidence
current external/security-advisory evidence
human/legal/product release decisions
provider/runtime compatibility evidence
benchmark/support qualification evidence
~~~

One class cannot silently substitute for another.

## Dependency and lock provenance

The current package has no runtime project dependencies. Build, test, lint, typing, fitness, packaging, and CI actions are still material development supply-chain inputs.

Repository rules are:

- direct Python dependency constraints must be bounded rather than unconstrained/wildcard/VCS/URL references;
- `uv.lock` is required and `uv lock --check` remains the lock-consistency gate;
- external registry artifacts represented in the lock must carry integrity hashes;
- unsupported VCS, arbitrary URL, or local-path dependency sources fail preflight unless a future explicitly authorized package/change contract records why they are required;
- the repository's project package may remain editable/local inside the lock because it is the checkout under test;
- lock integrity proves reproducible selection/integrity metadata, not current vulnerability freedom or legal suitability;
- dependency upgrades are reviewed changes, not self-authorized merely because a newer version exists.

The current runtime-dependency count of zero is a fact about the current package, not a permanent architecture rule.

## CI action provenance

GitHub Actions used by repository verification MUST be pinned to immutable 40-character commit revisions.

Human-readable comments SHOULD retain the reviewed release label.

Current reviewed action mappings are machine-owned by `engineering-preflight-profile.json`.

A semantic version tag alone is not immutable provenance, even when it names an exact patch release.

Updating an action revision is a supply-chain change and must:

1. identify the upstream action/release;
2. update the reviewed release label and immutable revision together;
3. pass repository verification;
4. avoid broadening permissions or secret/network access merely because the new action permits it.

## Toolchain alignment

The current deterministic baseline is:

~~~text
package requires-python     >=3.11
repository verified Python  3.11
uv required range           >=0.12,<0.13
CI uv version               0.12.11
~~~

`requires-python >=3.11` expresses package install eligibility. It MUST NOT be read as evidence that every later Python version is verified.

Until additional executed matrix evidence exists, **Python 3.11 is the repository-verified Python line**.

Likewise, the uv requirement range expresses allowed tooling compatibility, while CI's exact uv version is the reproducible verified tool invocation.

## Checked-in secret and credential hygiene

Repository source, tests, documentation, generated routing, workflows, agent instructions, configuration, and fixtures MUST NOT contain real bearer credentials/private keys or credential-bearing local files.

`tools/scan_repository_secrets.py` provides a high-confidence deterministic guard for:

- private-key material;
- known high-confidence token/key forms;
- forbidden credential file names such as `.env`, private-key files, and common credential/secret JSON/YAML names.

The scanner intentionally avoids broad entropy or generic-word heuristics that would turn examples/tests such as `SecretRef` into false positives.

A scanner PASS is not proof that no secret exists. Organization/provider secret scanning and credential response remain separate controls.

Secrets required by future runtime/provider work remain governed by the current security architecture and SecretRef/bearer separation. 016-I does not choose a cloud secret manager.

## Compatibility evidence

Compatibility remains multi-axis under current architecture.

The preflight distinguishes at least:

- package/install metadata;
- verified Python/toolchain execution;
- public API/resource compatibility;
- persistence/schema readability/migration;
- wire/serialization compatibility;
- Strategy/SPI/extension compatibility;
- provider/adapter/runtime compatibility;
- scale/performance qualification.

A package version or green test suite MUST NOT collapse these axes into one `compatible=true`.

### Current state

For the current unreleased `0.0.0` baseline:

- Python 3.11 is verified by repository CI;
- broader Python versions are not claimed verified;
- current portable/reference implementation contracts are verified to the current test boundary;
- no public release compatibility window is declared;
- no production Spark or Databricks compatibility/support claim is established;
- persisted/wire/plugin compatibility windows for a public release are not yet declared.

A future Class 2 change to public/persisted compatibility follows the 016-H package compatibility/migration assessment contract.

## Benchmark and support qualification

The Phase 015 C8 implementation contains typed `BenchmarkEvidence`, `WorkloadProfile`, and layered support-qualification contracts.

Those contracts and their unit/fitness fixtures prove the **qualification mechanism**, not a real workload result.

The preflight therefore enforces:

~~~text
synthetic test fixture        != real benchmark evidence
row count                     != complete workload profile
benchmark PASS                != provider support
conformance verified          != scale qualified
scale qualified profile A     != scale qualified profile B
~~~

Enterprise-scale or provider-specific claims require actual evidence tied to the exact workload, package/build, runtime, adapter, provider/environment/configuration, run set, metrics, acceptance criteria, and limitations required by current C8 contracts.

The current repository remains **NOT QUALIFIED for enterprise-scale support** and retains the explicit unclaimed support entries in `current-support-scope.md`.

## Package/API versioning and release state

The current project version is `0.0.0`.

016-I interprets that value as:

~~~text
development baseline   YES
published release      NO CLAIM
compatibility promise  NO PUBLIC WINDOW DECLARED
release candidate      NO
~~~

No automatic SemVer stability promise is inferred from `0.0.0`.

A future release task must explicitly select a non-placeholder version and determine the compatibility/release policy appropriate to that release. Public/persisted contract changes remain Class 2 under 016-H; architecture/semantic impacts remain Class 3/4 stop/reopen conditions.

## Release-candidate preflight

A future release-candidate claim requires all applicable evidence below:

- deterministic repository Verify/agentic/preflight checks pass;
- project version is intentionally selected and is not `0.0.0`;
- distribution license decision/metadata is complete;
- public compatibility/readability/migration windows are explicitly stated for the release scope;
- a current external vulnerability/advisory review of the resolved release dependency set exists;
- package build/install verification passes;
- support/provider/scale claims are limited to exact available evidence;
- release notes/non-claims do not convert architecture compatibility into implemented/provider/scale support;
- human release authorization exists.

Where a release does not claim provider or scale support, absence of provider/scale qualification is a limitation/non-claim rather than a reason to fabricate such evidence.

## Current residuals

The current preflight intentionally records:

~~~text
EP-R01 distribution license selection        UNRESOLVED / RELEASE-CANDIDATE BLOCKER
EP-R02 current vulnerability/advisory review EXTERNAL EVIDENCE REQUIRED / RELEASE-CANDIDATE BLOCKER
EP-R03 public compatibility windows          NOT DECLARED / RELEASE-CANDIDATE BLOCKER
EP-R04 Python >3.11 executed verification    NOT ESTABLISHED / SUPPORT NON-CLAIM
EP-R05 real enterprise-scale benchmark       NOT ESTABLISHED / SCALE-CLAIM BLOCKER
EP-R06 production provider qualification     NOT ESTABLISHED / PROVIDER-CLAIM BLOCKER
~~~

These are evidence/decision residuals. None currently requires a P16-3/P16-4 semantic or architecture reopen.

## Validator semantics

`tools/validate_engineering_preflight.py` verifies repository-deterministic facts only:

- machine profile consistency;
- bounded direct dependency constraints;
- lock source/hash integrity;
- immutable CI action revisions;
- Python/uv/project-version alignment;
- explicit current support non-claims;
- release-state/residual consistency;
- secret scanner success.

`tools/test_engineering_preflight_guards.py` introduces isolated defects and requires the owning validators to reject them.

## Phase boundary

016-I does not:

- select a distribution license;
- query or certify current external vulnerability/advisory databases;
- create provider/runtime integrations;
- execute or claim real enterprise-scale benchmarks;
- publish packages, tags, releases, images, or deployments;
- authorize 016-J or a post-Phase-016 implementation program.
