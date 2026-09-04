---
type: Experience Specification
title: Enterprise Dependency, Offline/No-Egress & Safety Experience
status: active
---

# Enterprise Dependency, Offline/No-Egress & Safety Experience

## Purpose

Define how human and programmatic actors understand, validate, and safely act on external/local dependencies, network requirements, data-egress behavior, sensitive source-derived state, restricted diagnostics/Provenance/Evidence, and enterprise offline/no-egress operating constraints across SYNGAN workflows.

This experience is governed primarily by the [Network and External Dependency Policy](../authority/network-external-dependency-policy.md), accepted concept ownership, and the earlier Phase 003 workflow experiences. It does not introduce standalone `Security`, `Policy`, `Artifact`, `Trust`, `Approval`, `Data Classification`, `Egress`, `Deployment`, or `Access Control` concepts.

## Primary experience principle

> **Actors must be able to determine what a proposed or historical activity depends on, whether network access is required, whether source-derived or generated information may leave the local boundary, whether required dependencies are available and permitted, what sensitive information is being exposed, and why policy permits or blocks the next action—without hidden acquisition, hidden egress, or invented safety guarantees.**

The experience preserves several independent questions:

```text
What does the Strategy or method require?
        ↓
Dependency/network declaration

What is actually available in this environment?
        ↓
Dependency resolution

What does the current enterprise profile permit?
        ↓
Contextual policy compatibility

What information would cross a boundary?
        ↓
Egress disclosure

What may this actor inspect or operate on?
        ↓
External authorization / disclosure boundary
```

No one of these answers silently determines the others.

## Entry modes

Actors may encounter the enterprise safety experience while:

- preparing Data Meaning, Constraints, and Strategy selection;
- reviewing a Learning commitment;
- inspecting Learned State dependencies or reuse eligibility;
- preparing or fulfilling Generation;
- selecting or running Evaluation methods;
- monitoring Execution failures caused by dependency/network/access conditions;
- investigating a retry or recovery that may invoke an external dependency;
- inspecting historical Provenance or current reproducibility;
- reviewing sensitive Evidence, diagnostics, or source-derived state;
- operating in a fully offline/no-egress environment;
- diagnosing why an otherwise compatible Strategy/method cannot be used in the current deployment context.

The experience SHOULD surface these concerns before expensive work begins whenever enough information is available.

## Dependency profile experience

The actor should be able to identify the dependency profile declared by a Strategy, Evaluation method, or future extension using the semantic distinctions established by the network policy.

### Self-contained

```text
Runtime network: none
External runtime artifact: none beyond normal provisioned package/runtime
```

This does not imply the Strategy is safe for every dataset or every organization; it only describes its dependency posture.

### Local-artifact dependent

```text
Runtime network: none
Required local artifact(s): yes
Acquisition during execution: no
```

Examples may include pretrained weights, vocabularies, reference tables, or other approved local resources.

### Acquisition-network dependent

```text
Execution can be offline after provisioning
Ordinary setup may acquire external artifact(s)
Automatic acquisition must be controllable
```

An enterprise no-network profile must be able to require explicit pre-provisioning rather than runtime/setup download.

### Runtime-network dependent

```text
Material operation requires remote service/network resource
```

This requirement must remain explicit before commitment and throughout execution/recovery.

The experience may use friendlier labels, but it MUST preserve these distinctions where they affect compatibility, safety, or reproducibility.

## Dependency resolution versus permission

Availability and authorization are different.

The experience should preserve states conceptually equivalent to:

```text
Dependency B3
Identity: verified
Location: local approved repository
Availability: resolved
Permission for proposed activity: permitted
```

versus:

```text
Dependency B3
Identity: verified
Availability: resolved
Permission: not established / restricted
```

and:

```text
Dependency B3
Expected identity: hash/version X
Found local artifact: Y
Compatibility: mismatch
Permission: irrelevant until identity is resolved
```

A file being locally accessible does not prove that it is the correct, trusted, permitted, or historically equivalent dependency.

The exact approval/trust authority and artifact repository technology remain external/downstream design concerns.

## Identity and substitution experience

### Required dependency identity remains visible

Where a local/base/pretrained artifact materially affects behavior, the experience should expose enough identity to distinguish what is expected from what was found.

For example:

```text
Required base artifact
B3 / version 7 / expected identity H7

Resolved local artifact
B3 / version 7 / identity H7

Status
compatible
```

### Silent substitution is prohibited

If B3 is missing and B4 exists, the experience MUST NOT silently treat B4 as equivalent merely because it serves a similar purpose.

A material substitution may alter:

- Strategy behavior;
- Learned State compatibility;
- Generation output;
- Evaluation results;
- reproducibility;
- privacy/disclosure risk;
- resource behavior.

Therefore:

```text
required B3 unavailable
available B4 differs materially
```

should result in an explicit incompatibility or a request to create a new activity/commitment using B4, not a hidden fallback.

### Mutable locations are not sufficient identity

A URL, path, alias, registry tag, or service name may help locate a dependency but does not establish historical/equivalence identity when the underlying content can change.

This rule aligns with [Provenance](../concepts/provenance.md) and the [Reproducibility Contract](../authority/reproducibility-contract.md).

## Automatic acquisition experience

### Missing dependency must not trigger surprise network activity

When an artifact is absent, the experience must not silently:

- download from HuggingFace or another model hub;
- fetch from a public URL;
- call a remote model registry;
- install optional remote resources;
- invoke a service-based fallback;
- transmit telemetry in order to resolve the problem.

A missing dependency should instead surface a clear state such as:

```text
Required dependency B3 not available locally
Current profile: no outbound network
Automatic acquisition: prohibited
Next action: provision approved B3 locally or select a compatible self-contained/local strategy
```

### Acquisition is a distinct actor action when permitted

If the environment permits acquisition, the experience should make the transition explicit before the network action occurs.

It should identify at least:

- resource being acquired;
- expected identity/version where known;
- source/location/provider;
- whether acquisition itself transmits sensitive information;
- destination/local availability expected afterward;
- whether the resulting activity can execute offline;
- whether actor/policy authorization is required.

The exact confirmation mechanism is later UI/API design.

### Provisioning and execution remain distinguishable

An acquisition-network-dependent Strategy can legitimately become offline-executable after approved provisioning.

The experience should therefore distinguish:

```text
Provisioning network requirement
```

from:

```text
Runtime network requirement
```

rather than labeling both simply `network required`.

## Enterprise offline/no-egress profile experience

A no-egress operating posture should be visible as a binding activity/deployment context rather than a hidden infrastructure assumption.

A proposed activity may show, for example:

```text
Enterprise profile
Outbound network: prohibited
Automatic artifact acquisition: prohibited
Remote inference/services: prohibited
Telemetry egress: prohibited
Required dependencies: local only
Source/source-derived egress: prohibited
Generated-data egress: prohibited unless separately authorized
```

This is an experience representation, not a required configuration schema.

### Compatibility must be explicit

A Strategy or Evaluation method may be semantically suitable yet incompatible with the current enterprise profile.

For example:

```text
Strategy semantic compatibility: compatible
Dependency profile: runtime-network dependent
Current deployment profile: no outbound network
Overall activity readiness: blocked by deployment incompatibility
```

The experience should explain the blocker rather than marking the Strategy generically `unsupported`.

### Commitment binds the actual posture

Where network/dependency behavior materially affects an activity, the committed Learning, Generation, or Evaluation must retain the actual selected posture and dependency identities.

A later policy relaxation does not silently grant a committed no-egress activity permission to access the network.

A materially different network/dependency behavior requires a new explicit commitment or other owning-concept transition permitted by canonical semantics.

## Data-egress disclosure experience

Network connectivity and data egress are separate concerns.

A network-capable dependency/method should expose what kind of information could cross the execution boundary, preserving at least distinctions equivalent to:

1. **network access with no dataset/content egress**;
2. **non-sensitive metadata/configuration transfer**;
3. **source-derived information transfer**;
4. **source-record transfer**;
5. **generated-record transfer**.

These categories are disclosure semantics; they do not themselves authorize transmission.

### Source-derived state is not automatically non-sensitive

The experience must treat potentially sensitive source-derived information broadly enough to include, where relevant:

- Learned State;
- embeddings;
- statistical summaries;
- distributions;
- model gradients/parameters;
- candidate synthetic data;
- generated data;
- Evidence/diagnostics derived from protected subjects;
- Provenance that reveals protected dataset/model/infrastructure relationships.

The system MUST NOT assume these are safe to transmit merely because they are not literal source rows.

### Egress preview before commitment

Where an activity could transmit information externally, pre-commit review should state what may leave the boundary and why.

For example:

```text
Remote Evaluation method
Network: required at runtime
Data sent externally:
- aggregate statistical summary
- no source records
- no generated records

Authorization:
not established

Result:
blocked until permitted or replaced by local method
```

The experience should not use a generic `network allowed` toggle as the only disclosure.

## Hidden fallback prevention

If a dependency fails during execution, the experience must preserve the committed behavior.

A local Strategy cannot silently become remote because:

- a GPU is unavailable;
- a local artifact disappeared;
- a service/library offers a convenient hosted alternative;
- local inference failed;
- a cache missed.

Recovery choices should be classified as either:

- same-semantics operational recovery allowed by the committed context; or
- a material Strategy/method/dependency change requiring a new domain commitment.

This aligns with the 003-F operator intervention boundary.

## Failure and blocked-state experience

Actors should be able to distinguish failures such as:

- dependency unavailable;
- dependency identity mismatch;
- dependency present but not permitted;
- network required but prohibited;
- egress category not permitted;
- remote service unavailable;
- remote behavior/version identity insufficient for required reproducibility;
- credential/access failure;
- policy decision unavailable/indeterminate;
- sensitive detail withheld from the current actor.

These conditions should not all collapse into `dependency error` or `permission denied` when the distinction affects the legitimate next action.

### Blocked is not failed semantic work

When an incompatibility is identified before commitment, the experience should generally present it as preparation/readiness blocked rather than as a failed Learning/Generation/Evaluation that never validly began.

When a committed activity encounters an unfulfilled dependency/network requirement during execution, the owning activity and Execution preserve their respective semantic/operational outcomes under existing lifecycle rules.

### Policy uncertainty remains uncertainty

If the system cannot establish whether a dependency or egress action is permitted, it must not optimistically assume permission.

An experience state equivalent to:

```text
Authorization/policy compatibility: indeterminate
Action: blocked pending resolution
```

is legitimate.

## Sensitive Learned State experience

Learned State is source-derived and may contain or encode sensitive information.

The experience should expose safety posture appropriate to the actor without implying that the state is anonymous/private merely because it is a model/statistical object.

Potentially relevant information includes:

- source context classification/reference where permitted;
- whether export/transmission is restricted;
- dependency/base-artifact requirements;
- known privacy/disclosure-risk Evidence;
- current lifecycle restrictions;
- approved execution boundaries where external policy supplies them.

A lack of known privacy-risk Evidence must remain `not evaluated`, not `safe`.

## Sensitive synthetic/candidate output experience

Synthetic origin does not imply unrestricted disclosure.

The experience must preserve:

```text
synthetic
    ≠ anonymous
    ≠ formally private
    ≠ approved to leave the environment
```

Candidate output is especially non-final: besides unresolved validity/Condition obligations, it may not have completed privacy/disclosure-risk Evaluation or governance review.

Completed Generation likewise does not itself authorize export or release.

External release/use authority remains outside Generation/Evidence.

## Sensitive Evidence and diagnostics experience

Evidence and diagnostic material may reveal sensitive information even when the final numeric finding looks innocuous.

Examples include:

- nearest-neighbor records;
- suspected memorized examples;
- violating rows;
- rare-category examples;
- source/synthetic record pairs;
- attack traces;
- detailed error samples;
- sensitive downstream-task labels;
- protected source/reference identities.

The experience should permit bounded summaries for actors who do not need raw diagnostics and expose detailed material only where external authorization permits.

A redacted/withheld diagnostic should remain visibly withheld rather than be replaced by fabricated sanitized content that could change interpretation.

## Sensitive Provenance experience

Provenance may reveal:

- protected dataset names;
- model/artifact identities;
- infrastructure/environment details;
- remote service providers;
- source-to-output relationships;
- security-sensitive execution history.

The experience therefore separates **traceability exists** from **every actor can see every detail**.

A restricted view may show:

```text
Generation G42
used source: [restricted]
used approved local base dependency: [restricted]
provenance relationship: present and verifiable
```

rather than either exposing the secret or pretending no source/dependency relationship existed.

The exact access-control/redaction mechanism is deferred.

## Withholding and redaction semantics

When detail is restricted, the experience should preserve enough state to distinguish:

- value/detail does not exist;
- value is unknown;
- value is unavailable due to dependency loss;
- value exists but is withheld from this actor;
- value has been redacted into an authorized summary.

These must not be conflated.

In particular:

```text
[withheld]
```

must not be interpreted programmatically as:

```text
null / absent / unknown
```

if the system knows that a material protected fact exists.

## Actor-specific safety orientation

### Data Practitioner

Needs actionable dependency/network/egress blockers, local alternatives where declared, sensitive-state warnings, and clear distinction between missing resources and forbidden resources.

### Platform Operator

Needs enough environment/dependency/network detail to diagnose and recover operational issues while remaining unable to change semantic commitments or external governance permissions silently.

### Data Owner / Steward

Needs source/semantic dependency posture, egress disclosure, historical bindings, current restrictions, and awareness of which source-derived states/results may expose sensitive information.

### Privacy / Risk / Governance Reviewer

Needs detailed egress categories, threat-model Evidence, external dependency identity, provenance/reproducibility limitations, withheld-detail indicators, and explicit separation between observation and approval.

### Synthetic Data Consumer

Needs enough information to understand whether output is appropriate/authorized for the intended environment/use. Synthetic origin or favorable fidelity alone must not appear as permission to export or share.

## Programmatic parity

A future SDK/CLI/API should allow programmatic users to inspect, where authorized:

- dependency profile;
- required dependency identities;
- resolution/availability state;
- contextual permission/policy result and reason;
- provisioning-network versus runtime-network requirement;
- egress categories;
- local/no-egress compatibility;
- automatic-acquisition prohibition/availability;
- dependency substitution mismatch;
- sensitive-state/diagnostic/provenance restrictions;
- withheld versus unknown versus absent state;
- relevant current/historical provenance and reproducibility limitations;
- legitimate next actions.

A generic `secure=true`, `offline=true`, `network_required=true`, or `permission_denied` scalar alone is insufficient.

## Historical inspection interaction

003-G established historical truth/current reproducibility separation. 003-H adds the rule that current actors may have only a restricted view of that history.

Historical inspection must therefore preserve:

```text
historical fact exists
        ↓
actor-specific disclosure boundary
        ↓
full detail / authorized summary / withheld marker
```

rather than allowing redaction to rewrite the provenance graph.

Where a dependency was historically network-acquired or remote, the historical record should preserve that fact and its material identity/egress context where required, even if current policy would prohibit the same behavior today.

Current policy affects new work/current reproduction feasibility; it does not rewrite historical execution.

## Reproducibility interaction

A reproduction assessment must include current availability and permission for material dependencies.

A historical target may be fully explained but currently unreproducible because:

- a required artifact no longer exists;
- a remote service no longer exposes the historical behavior;
- current policy prohibits network access required by the old method;
- current policy prohibits required source/source-derived egress;
- the actor lacks authorized access to required source/reference material.

The resulting weaker reproduction class is a current assessment, not a change to historical Provenance.

## Enterprise-scale safety experience

Safety/disclosure review must remain practical for Spark-scale workflows.

The experience SHOULD use bounded control-plane information such as:

- dependency manifests/references;
- egress declarations;
- source/result classifications or external policy references where available;
- Evidence summaries;
- sensitivity/restriction markers;
- aggregate diagnostic counts;
- selected protected diagnostic references;
- network/dependency events material to Execution;
- Provenance relationships.

It MUST NOT require loading complete source data, Learned State payloads, generated output, detailed attack examples, all violating rows, or platform logs into one UI/driver merely to decide dependency/no-egress compatibility.

## Next-action guidance

Derived guidance may include:

```text
Missing local dependency under no-network profile
  → provision the exact approved artifact locally
  → or select a semantically compatible local/self-contained Strategy

Runtime-network Strategy under no-egress profile
  → incompatible with current profile
  → select local alternative or establish a new permitted deployment/commitment externally

Resolved artifact identity mismatch
  → do not substitute silently
  → resolve exact artifact or create new activity with explicit replacement

Egress behavior not authorized
  → block commitment/execution
  → expose exact egress category requiring decision

Sensitive diagnostic withheld
  → show bounded authorized summary
  → preserve that underlying detail exists

Historical dependency now prohibited
  → historical provenance unchanged
  → current reproduction assessment limited/blocked
```

Guidance remains derived from existing authority and external policy results; it does not create a generic Security/Safety workflow authority.

## Experience invariants

1. Core supported structured/tabular workflows MUST remain experience-compatible with no outbound network operation after approved provisioning.
2. Dependency profile MUST remain explicit and distinguish self-contained, local-artifact, acquisition-network, and runtime-network semantics where material.
3. Dependency availability MUST remain distinct from dependency identity, compatibility, and permission.
4. A locally accessible artifact MUST NOT be presumed trusted/permitted/equivalent solely because it can be opened.
5. Missing dependencies MUST NOT trigger hidden automatic acquisition or remote fallback.
6. Provisioning/acquisition network requirements MUST remain distinguishable from runtime network requirements.
7. Network access MUST remain distinguishable from data egress.
8. Egress disclosure MUST distinguish no-content network access, metadata/config transfer, source-derived information, source records, and generated records where material.
9. Egress disclosure MUST NOT itself authorize transmission.
10. Learned State, synthetic output, Evidence, diagnostics, and Provenance MUST NOT be presumed non-sensitive merely because they are derived rather than raw source records.
11. Synthetic origin MUST NOT imply privacy, anonymity, export permission, or release authorization.
12. A committed no-network/no-egress activity MUST NOT silently enable network access, substitute a remote method, or weaken semantic requirements to proceed.
13. Material dependency substitution MUST NOT occur silently; replacement behavior requires explicit compatibility and commitment semantics.
14. Retry/recovery MUST preserve committed dependency/network/egress semantics and MUST NOT become a backdoor for remote fallback.
15. Policy/authorization uncertainty MUST remain explicit and MUST NOT be coerced to permission.
16. Sensitive Evidence/diagnostics SHOULD support bounded summaries and protected detail without falsifying the underlying finding.
17. Restricted Provenance/detail MUST be shown as withheld/redacted rather than absent, unknown, or fabricated when the distinction is known.
18. Redaction/access limitation MUST NOT rewrite historical Provenance or canonical concept state.
19. Historical dependency/network behavior MUST remain inspectable as historical fact even if current policy differs.
20. Current reproduction capability may be limited by present access/network/egress policy without rewriting historical truth.
21. Programmatic and human-facing experiences MUST preserve equivalent dependency/network/egress/withholding distinctions.
22. Enterprise safety review MUST NOT require full source/output/Learned State/diagnostic/log collection to driver-local memory.
23. Experience convenience MUST NOT create generic Security, Safety, Policy, Trust, Artifact, Data Classification, Egress, Deployment, Access Control, or Approval god-concepts.

## Representation questions intentionally deferred

003-H does not decide:

- identity/authentication system;
- role/permission model;
- authorization engine;
- data-classification taxonomy;
- secret-management system;
- artifact-signing/trust-store implementation;
- malware/supply-chain scanning technology;
- model registry/artifact repository;
- network firewall/service-mesh implementation;
- egress gateway/DLP technology;
- encryption/key-management implementation;
- sandbox/container policy;
- telemetry implementation;
- redaction/tokenization technology;
- policy language/engine;
- approval workflow;
- deployment topology;
- exact UI confirmations;
- retention/cleanup policy.

Later architecture/security design may select those mechanisms while preserving the experience semantics defined here.
