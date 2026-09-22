# Contributing to SYNGAN

This file defines the repository workflow for maintainers and explicitly authorized
contributors. External contribution terms are not yet established because the project
distribution-license decision remains unresolved.

## Before starting work

1. Start from the current `main` branch.
2. Confirm the work item is explicitly selected by the applicable start gate, package, or
   bounded maintenance request.
3. Read [AGENTS.md](AGENTS.md), even for human-authored implementation work, because it
   summarizes the repository authority and stop/reopen rules.
4. Resolve the smallest current authority needed for the task through
   [docs/index.md](docs/index.md).
5. For material Class 1/2 implementation, use the
   [implementation package contract](docs/implementation/implementation-package-traceability-adr-change-control.md).

A backlog item, old phase branch, implementation package, or passing test does not itself
authorize new implementation scope.

## Branch strategy

Use a **short-lived branch per bounded work item**. Create it from the current verified
`main` head and delete it after the pull request is merged.

Preferred names:

- `impl/ipkg-####-short-topic` — material implementation with an implementation package;
- `fix/short-topic` — bounded defect correction;
- `docs/short-topic` — documentation-only correction;
- `chore/short-topic` — repository/tooling maintenance.

Avoid long-lived `phase-*` branches for ordinary implementation. A future numbered phase
may use phase-oriented naming only when its explicit start gate chooses that structure.

Each branch should normally produce one pull request. Do not accumulate unrelated cleanup
or a second delivery slice on an existing branch merely because it is convenient.

## Change classification

Use the repository's Class 0-4 model:

- **Class 0** — local/non-contractual maintenance;
- **Class 1** — implementation realization;
- **Class 2** — public/persisted/compatibility contract;
- **Class 3** — architecture-affecting;
- **Class 4** — semantic/experience-affecting.

Class 3/4 conflicts stop ordinary implementation and reopen the smallest owning authority.
Do not code around an upstream contradiction.

Current governance:
[Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](docs/implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md).

## Local verification

Provision the repository-owned environment:

```bash
uv sync --all-groups --locked --no-build-isolation
```

At minimum, run the verification appropriate to the change. The portable baseline is:

```bash
uv run --no-sync python tools/verify.py portable
python tools/run_agentic_conformance.py
```

When dependency, toolchain, compatibility, support-surface, benchmark, version, or release
hygiene changes are involved, also run:

```bash
uv run --no-sync python tools/verify.py preflight
```

Material implementation work must additionally execute the C-lanes and focused tests
required by its package/authority.

## Pull requests

Use the repository pull-request template. A material PR should identify:

- the selected task or `IPKG-####`;
- the human authorization basis;
- current `syngan://...` authority references;
- change classification;
- implementation and verification paths;
- compatibility/migration impact;
- dependency, network, security, and scale implications;
- explicit limitations and deferred work.

Required evidence must pass before merge. Do not weaken or remove a failing guard in the
same change merely to obtain a green result without explicit review of the governing rule.

The repository's established merge style is **squash merge**. After merge, remove the
short-lived head branch.

## Documentation and authority

Update the smallest current owner when implementation creates a durable realization
decision. Phase records and PR descriptions are evidence/provenance, not substitutes for
current authority.

Do not hand-edit generated `knowledge/` projection files except through the repository
generation workflow.

## Support and release claims

Do not claim provider support, Python compatibility, enterprise scale, security
certification, public compatibility, or release readiness beyond executed evidence.

Current residuals and non-claims are owned by
[Repository Implementation Readiness & Residual Risk](docs/implementation/repository-implementation-readiness-residual-risk.md).

## License and external contributions

No distribution license has been selected. Until that decision is made, this repository
workflow should not be interpreted as establishing external contribution or redistribution
terms.
