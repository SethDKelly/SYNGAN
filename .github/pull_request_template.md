## Scope

- Implementation slice / phase:
- Change classification: `0-local` / `1-realization` / `2-public-or-persisted-contract` / `3-architecture-affecting` / `4-semantic-or-experience`
- Upstream authority implemented:

## What changed

Describe the bounded change and why it is needed.

## Verification / acceptance evidence

- [ ] Relevant automated tests pass.
- [ ] Required architecture fitness checks pass or an explicit bounded waiver is documented.
- [ ] Failure/recovery paths were tested where material.
- [ ] The change does not rely only on a one-off notebook/manual success.

Evidence / commands / CI links:

## Architecture and authority

- [ ] The change preserves the Phase 004 Consolidated Architecture Contract.
- [ ] Durable implementation decisions are reflected in `docs/implementation/` where needed.
- [ ] Any architecture-affecting change updates canonical architecture/ADR authority rather than hiding the change in code.
- [ ] No new generic Session/Context/Metadata/Manager/Registry/Result ownership boundary was introduced without explicit authority.

## Dependencies / toolchain

- [ ] New or changed direct dependencies have an explicit purpose and correct classification.
- [ ] Optional platform/runtime dependencies remain isolated from the supported portable/offline core.
- [ ] No hidden runtime package/model/artifact download or remote fallback was introduced.
- [ ] Material compatibility/offline/private-provisioning implications are documented.

Dependency/toolchain changes:

## Public, persisted, migration and compatibility impact

- [ ] Public API/SPI impact is documented.
- [ ] Persisted/wire/schema impact is documented.
- [ ] Migration/deprecation/backward-compatibility impact is documented where applicable.
- [ ] Historical committed state is not rewritten by a persistence migration.

Impact:

## Security / network / egress

- [ ] No real secrets or sensitive payloads are committed in code, fixtures, logs, or examples.
- [ ] Authorization/disclosure boundaries remain intact.
- [ ] Network and data-egress behavior is unchanged or explicitly documented/reviewed.
- [ ] Derived query/index paths do not bypass protected canonical resources.

Impact:

## Scale / platform behavior

- [ ] Enterprise paths do not introduce mandatory full driver-local materialization.
- [ ] Platform/runtime specialization remains behind accepted ports/adapters.
- [ ] Platform success/retry/identity is not substituted for SYNGAN semantic authority.

Impact:

## Deferred / follow-up work

List explicit deferred items, owner/phase/backlog location, and any temporary waiver/expiration condition.
