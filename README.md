# SYNGAN

SYNGAN is a design-first synthetic-data generation framework with a portable Python
reference foundation and an architecture intended to support Spark-scale execution.

The current repository **does not yet claim production Spark/Databricks/provider support
or enterprise-scale qualification**. Those claims require future implementation and
evidence under an explicitly authorized program.

## Current status

```text
Jackson concept design                COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013 architecture                COMPLETE
Phase 014 whole-design/readiness      COMPLETE
Phase 015 implementation foundation   COMPLETE
Phase 016 repository hardening        COMPLETE
C0-C9                                 ACTIVE / PASS
repository implementation readiness   100 / 100
Phase 017 planning                     AUTHORIZED / ACTIVE — PLANNING ONLY
product implementation execution      NOT AUTHORIZED
public release                         NOT READY / NOT AUTHORIZED
```

The readiness score means the repository has the current authority, verification,
documentation, agentic-development, implementation-package, supply-chain, and preflight
controls needed to begin a separately authorized implementation program. Phase 017 is
currently authorized to design that program only; coding remains unauthorized.

## Start here

- [Current knowledge entry](docs/index.md)
- [Current repository status](docs/authority/current-repository-status.md)
- [Current implementation governance](docs/implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md)
- [Current implementation and support scope](docs/implementation/current-support-scope.md)
- [Repository readiness and residual risk](docs/implementation/repository-implementation-readiness-residual-risk.md)
- [Implementation package / traceability contract](docs/implementation/implementation-package-traceability-adr-change-control.md)
- [Engineering preflight](docs/implementation/engineering-preflight-dependency-supply-chain-secrets-compatibility-benchmark-versioning.md)
- [Contributor and branch workflow](CONTRIBUTING.md)
- [Agent instructions](AGENTS.md)

Completed design, architecture, audit, and implementation-phase evidence is retained under
[documentation history](docs/history/index.md). Historical phase wording does not override
the current owners linked above.

## Development setup

The verified repository baseline is Python 3.11 with the locked `uv` environment.

```bash
uv sync --all-groups --locked --no-build-isolation
uv run --no-sync python tools/verify.py portable
python tools/run_agentic_conformance.py
```

Run the more specific verification profiles required by the selected implementation
package or change. Dependency, toolchain, compatibility, support-surface, or release
hygiene changes must also run:

```bash
uv run --no-sync python tools/verify.py preflight
```

CI runs the repository Verify suite and Agentic conformance on pull requests as applicable.

## Development workflow

Development should use short-lived branches from current `main`, one bounded authorized
work item per branch, reviewable pull requests, and squash merging. Material Class 1/2
implementation work uses an `IPKG-####` manifest when required by the implementation
package contract.

Do not infer authorization from an available backlog item, an existing branch, a package
manifest, or this README. The selected task/start gate defines the implementation envelope.

See [CONTRIBUTING.md](CONTRIBUTING.md) for branch naming, verification, and pull-request
expectations.

## Current non-claims

The repository does not currently claim:

- production Spark or Databricks support;
- enterprise-scale performance qualification;
- Python support beyond the executed 3.11 baseline;
- public compatibility guarantees;
- deployment/IaC or SLO/SLA readiness;
- current vulnerability clearance for a release candidate;
- public-release readiness.

The exact residuals and evidence required to make those claims are maintained in the
[repository readiness authority](docs/implementation/repository-implementation-readiness-residual-risk.md).

## License / distribution

No distribution license has been selected. Distribution/public-release authorization
remains blocked by **RR-016-01 / EP-R01** until an explicit human/legal/product decision is
made and repository metadata is updated.
