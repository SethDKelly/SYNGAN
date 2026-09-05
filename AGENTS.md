# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents, including Codex-style agents.

## Start with authority, not repository-wide scanning

For any material task:

1. read `docs/index.md`;
2. read `docs/architecture/phase-004-consolidated-architecture-contract.md` for implementation-facing architecture;
3. read `docs/implementation/index.md` and the implementation authority relevant to the task;
4. follow only the detailed concept/experience/architecture links needed for the active slice;
5. use ADRs for rationale when necessary, not as a replacement for current canonical authority.

Do not load or copy the entire documentation corpus by default.

## Authority order

Treat conflicts using this direction:

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation authority / accepted plan
  > code / deployment
  > examples / generated artifacts / runtime state
```

Existing code does not override upstream authority.

If implementation appears incompatible with an accepted contract, identify the conflict explicitly. Do not silently redefine the contract in code.

## Scope and change discipline

Before material implementation work, identify:

- the Phase 005 implementation slice;
- upstream architecture/implementation authority;
- whether the change is local, implementation-realization, public/persisted-contract, architecture-affecting, or semantic/experience-affecting.

Keep changes bounded to the requested slice. Avoid opportunistic refactors, dependency additions, package moves, terminology changes, or API/schema changes outside scope.

## Non-negotiable architecture guardrails

Do not:

- make Spark DataFrames, PyTorch/Spark model objects, platform runs, paths, aliases, or process-local objects canonical SYNGAN identity;
- collapse typed semantic/operational/security/history state into one generic `status`, `Result`, `Session`, `Context`, `Metadata`, `Manager`, or `Registry` owner;
- equate checkpoint/candidate/runtime material with Learned State/completed output/Evidence;
- let runtime/platform adapters establish semantic completion directly;
- replace Attempt fencing with lease expiry, scheduler retry, or last-writer-wins;
- hide dependency/model/package downloads, remote fallback, telemetry, or egress;
- require full source/output/Learned-State/diagnostic collection to the driver on enterprise paths;
- make Databricks, PyTorch, Spark ML, CTGAN, or another runtime/platform universal semantics;
- let derived query indexes, telemetry, or security audit become canonical domain state;
- treat resource-handle possession as authorization;
- weaken Evidence claim strength, Provenance history, exact historical binding, or disclosure distinctions for convenience.

## Dependencies and network behavior

Do not add a dependency solely because it simplifies generated code.

Any new direct dependency must have an explicit purpose and correct classification (core, development/verification, optional adapter/runtime, or build/release) and must be reviewed for compatibility, offline/private provisioning, network/telemetry behavior, and material security/supply-chain implications.

Committed runtime execution must never install missing packages or download missing models/artifacts as an undocumented fallback.

## Verification

Material behavior changes require verification appropriate to the implementation slice.

Never weaken or delete a required architecture-fitness check merely to make a change pass without explicitly documenting the conflict and rationale.

A successful local run is not sufficient completion evidence for a material slice.

## Secrets and sensitive data

Never commit real credentials, tokens, passwords, private keys, or bearer secrets.

Do not place sensitive source rows, Learned State payloads, protected diagnostics, or secret-bearing configuration in ordinary fixtures/logs/examples. Use synthetic/non-sensitive fixtures and explicit test/integration profiles.

## Documentation synchronization

When a durable implementation decision changes, update its canonical `docs/implementation/` authority in the same change where practical.

If the architecture itself changes, update `docs/architecture/` and relevant ADR rationale explicitly. Do not leave the new rule only in code, a PR description, or phase notes.

## Completion

Do not claim an implementation slice complete unless its required authority mapping, tests/fitness checks, dependency/migration/security/network implications, and acceptance evidence are accounted for.

Canonical governance: `docs/implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md`.
