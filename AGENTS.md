# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Phase 005 is planning-only

Phase 005 does **not** authorize production implementation.

During 005-A through 005-K, agents may update requested planning/governance/documentation artifacts but MUST NOT create production source, package scaffolds, database schemas/migrations, runtime/Spark/security/platform adapters, Evidence/Provenance stores, verification suites, CI workflows or deployment infrastructure merely because a future plan describes them.

A Phase 005 group marked `complete` means its **plan** is complete.

005-K is the explicit Jackson/design-completeness gate. It may require another concept/synchronization/experience/architecture/planning phase. Even a positive result requires a later explicit implementation-authority phase before coding begins.

## Progressive disclosure

For material work:

1. read `docs/index.md`;
2. read `docs/architecture/phase-004-consolidated-architecture-contract.md`;
3. read `docs/implementation/index.md` and the active implementation plan;
4. read 005-B verification and 005-C topology authority;
5. load only the 005-D through 005-J plans whose boundaries the task touches;
6. follow only directly relevant concept/experience/architecture links;
7. use ADRs for rationale, not instead of current authority.

Do not load/copy the full documentation corpus by default.

## Authority order

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation planning
  > future code / deployment
```

Existing or future code never overrides upstream authority.

## Non-negotiable boundaries

Future implementation MUST preserve:

- one inward `src/syngan` topology: `foundation/domain/ports/application/api/adapters/bootstrap`;
- no universal `utils`, `Context`, `Metadata`, `Result`, `Manager`, `Registry`, Session or similar god-owner;
- one durable ResourceRef/revision/SnapshotId/StateVersion/SchemaVersion substrate;
- platform/job/path/DataFrame/model/process objects are never canonical SYNGAN identity;
- exact historical refs never silently resolve to current/latest;
- DataFrame/query/path/table selectors are access instructions, not durable source identity;
- candidate/sealed snapshot/checkpoint/runtime material are not semantic results;
- runtime/platform success does not establish Learning, Generation, Evaluation or Evidence completion;
- Strategy/method semantic revision, ImplementationBindingRef, RuntimeSpiVersion, package build, state codec and platform/runtime version remain distinct;
- direct Generation remains valid without fabricated Learning/Learned State;
- one stable Execution may have multiple Attempts; AttemptEpoch fencing is distinct from liveness/lease state;
- stale Attempts cannot register/adopt/seal/complete through obsolete writer authority;
- unknown external launch/effect state is reconciled before unsafe retry;
- cancellation that wins the authority race revokes late completion/promotion authority;
- Evidence is owner-established from exact Evaluation subjects and cannot exceed method/coverage/uncertainty support;
- canonical Provenance is typed relationship authority, not copied metadata or graph/search projection state;
- reproducibility is a qualified assessment, not a seed/Boolean;
- dependency existence, exact identity, integrity/authenticity, trust, compatibility, authorization and runtime capability remain distinct;
- runtime never auto-installs/downloads dependencies, queries public registries, enables telemetry or switches to remote fallback silently;
- handles are identifiers, never bearer credentials;
- bearer secret values remain ephemeral/non-canonical;
- redaction/withholding preserves `absent`, `unknown`, `unavailable`, `withheld` and authorized/redacted distinctions;
- derived indexes/counts/search/reverse traversal are inside the security boundary;
- security audit, runtime telemetry and canonical history remain separate;
- enterprise paths do not require complete source/output/Learned-State/diagnostic collection on the driver;
- platform fallback must preserve semantics or report limitation/incompatibility.

## 005-J deployment/platform rules

005-J establishes the future deployment reality contract.

Agents MUST NOT:

- treat `Databricks`, `Spark`, a cloud provider or another platform name as proof of a capability;
- use platform job/run IDs as Execution/Attempt identity;
- treat native scheduler retries/speculation as SYNGAN Attempts without explicit coordination;
- treat native lineage/catalog/ML metadata as canonical Provenance/Evidence;
- use native source versioning as `SourceStateRef` unless exact historical reread/retention guarantees satisfy the data contract;
- serialize live Spark DataFrame/SparkSession, SQL sessions, loaded models or SDK clients across durable service/API boundaries;
- require external telemetry exporters in offline/no-egress profiles;
- let telemetry loss corrupt canonical transition state;
- publish one global `supported=true` or generic `version` instead of multi-axis compatibility evidence;
- claim enterprise scale from row count alone or hide a source-size-proportional driver/single-process stage;
- resume normal authoritative operation immediately after a potentially regressive control-store restore;
- allow a restored old AttemptEpoch to revive stale writer authority;
- use `ControlPlaneIncarnation` as a domain concept, credential or semantic revision;
- omit provider credential/namespace/native-fence rotation when an external mutable target can otherwise accept pre-restore stale writers;
- delete payloads still required by promoted outputs, usable Learned State, checkpoints, Evidence support, retained history or reproducibility without truthful unavailability/tombstone treatment.

Future deployment profiles are local/development, portable Spark, managed Databricks-oriented and private/offline/no-egress, with hybrid composition only when its exact cross-boundary capability/security contracts are satisfied.

Future support is contextual: direct, semantics-preserving fallback, limited, incompatible or indeterminate.

OpenTelemetry is planned only as an optional vendor-neutral telemetry integration; it is not a base semantic/offline dependency.

## Dependencies and package import

The base/core distribution remains model/platform neutral. Do not place PySpark, PyTorch, Databricks/cloud SDKs, graph/lineage clients, scheduler/IAM/policy/secret-manager SDKs, telemetry exporters, SQL provider SDKs or similar adapter dependencies into base runtime dependencies merely for one slice.

`import syngan` must remain side-effect free: no plugin scan/load, network access, dependency acquisition, Spark/session creation, credential inspection, telemetry initialization or mutable global Session/Context.

## Verification

When a later phase explicitly authorizes coding, tests derive their oracle from accepted authority and must not mock away the distributed, concurrency, persistence, runtime, recovery, Evidence/history, security or platform property under test.

005-J future work primarily owns V10/V11 and exercises AF-01/02/03/07/09/10/11/12/13/14/15/17/18/20, including:

- exact-source native/fallback conformance;
- stale-writer/provider fencing;
- ambiguous launch reconciliation;
- platform retry duplication;
- coordinator/client restart;
- projection/telemetry outage;
- offline/no-egress operation;
- workload identity/secret revocation;
- tenant/query isolation;
- mixed-version/rolling upgrades;
- regressive backup restore with surviving workers and fresh `ControlPlaneIncarnation` rejection;
- multi-dimensional scale profiles and bounded driver/control memory.

Do not weaken/quarantine required fitness checks outside 005-B governance.

## Documentation synchronization

Durable implementation decisions belong in `docs/implementation/`. Architecture changes belong in `docs/architecture/` with ADR rationale where appropriate.

Do not claim production implementation exists merely because a Phase 005 plan is complete, and do not assume 005-K must authorize coding.
