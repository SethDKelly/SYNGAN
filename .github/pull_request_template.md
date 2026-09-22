## Scope

- Selected task / implementation package (`IPKG-####`, if required):
- Entry commit / branch:
- Change classification: `0-local` / `1-realization` / `2-public-or-persisted-contract` / `3-architecture-affecting` / `4-semantic-or-experience`
- Human authorization basis:
- Current upstream `syngan://...` authority refs:

## Authorization check

- [ ] This change is inside the explicitly selected task.
- [ ] A package manifest, when present, is being used as scope/evidence metadata rather than as authorization.
- [ ] This change does not self-start the next package, phase, backlog item, deployment, or provider integration.
- [ ] Any Class 3/4 conflict was stopped and routed to the smallest upstream reopen rather than coded around.

## What changed

Describe the bounded implementation/documentation change and why it is required by the selected task.

## Traceability / verification

- [ ] Material obligations map current authority to implementation and verification evidence.
- [ ] `python tools/validate_implementation_packages.py` passes when a material package is present.
- [ ] Relevant deterministic/unit/contract/fitness/integration checks pass.
- [ ] Package evidence states do not exceed what the executed evidence proves.
- [ ] Complete-package claims contain no blocking/unresolved material obligation.

Implementation paths:

Verification paths / commands / CI evidence:

## Architecture and ADR change control

- [ ] Current canonical architecture remains controlling.
- [ ] Architecture ADRs are referenced as rationale only; they are not being used as implementation permission.
- [ ] Any ADR addition/material change/supersession is downstream of an explicitly authorized Class 3 architecture change and corresponding canonical architecture update.
- [ ] No platform/runtime/persistence convenience became semantic or architecture authority.

ADR references / architecture reopen:

## Compatibility / migration

- [ ] Class 2 changes include explicit compatibility and migration assessment, including explicit no-impact results.
- [ ] Persisted/public/wire/SPI changes preserve historical identity and accepted migration semantics.
- [ ] Existing consumers/data are not silently reinterpreted.

Assessment:

## Dependencies / network / security / scale

- [ ] Dependency/toolchain/version/support-surface changes run `python tools/verify.py preflight`.
- [ ] A preflight PASS is not being treated as release, legal, vulnerability, provider, or scale approval.
- [ ] Dependency/toolchain changes are disclosed for later/current governing review.
- [ ] Network/egress/offline behavior is unchanged or explicitly documented.
- [ ] No real secrets or sensitive payloads are committed.
- [ ] Scale/distributed implications and unsupported claims are explicit where material.

Impact / non-claims:

## Completion / follow-up

- [ ] Required failures, waivers, limitations, and deferred work remain explicit.
- [ ] Package completion does not claim broader support/qualification than evidence establishes.
- [ ] No next work item is treated as authorized merely because this one is complete.

Unresolved / deferred / follow-up:
