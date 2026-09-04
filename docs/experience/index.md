---
type: Experience Index
title: SYNGAN Experience & Workflow Design
status: active
---

# SYNGAN Experience & Workflow Design

This directory contains canonical actor-visible and programmatic workflow/experience design derived from the accepted concept, synchronization, and authority layers.

Experience documents define how actors discover, prepare, commit, observe, inspect, recover, and understand SYNGAN work. They do **not** redefine concept ownership or select final UI/API/package architecture.

## Current experience authority

- [Workflow Entry, Source Context & Lifecycle Orientation](workflow-entry-source-context-lifecycle-orientation.md) — how actors enter new or existing work, orient around source/history, distinguish editable from committed state, and understand semantic versus operational lifecycle.
- [Data Meaning, Constraint & Strategy Preparation](data-meaning-constraint-strategy-preparation.md) — how actors review declared/inferred/unresolved meaning, determine Constraint applicability/handling, compare Strategy capabilities/dependencies, understand contextual compatibility, and reach a reviewable commitment-ready state.
- [Learning & Learned State Lifecycle](learning-learned-state-lifecycle.md) — how actors commit/observe/recover Learning, distinguish checkpoints from semantic results, establish/inspect Learned State, and manage reuse/restriction/retirement/invalidation without conflating logical state with model artifacts.
- [Generation Request, Condition, Validation & Output Promotion](generation-request-condition-validation-output-promotion.md) — how actors define/commit Generation intent, distinguish mandatory and best-effort Conditions, observe partial/candidate output, inspect requirement-specific validation Evidence, and promote exactly one authoritative completed logical output only at semantic completion.
- [Evaluation, Evidence & Review](evaluation-evidence-review.md) — how actors begin from evaluative questions, select compatible methods, understand coverage/uncertainty/claim strength, interpret and compare Evidence, review multidimensional fitness, and preserve the boundary between findings and external decisions.
- [Execution Monitoring, Failure, Recovery & Cancellation](execution-monitoring-failure-recovery-cancellation.md) — how actors monitor one logical Execution across Attempts/platform jobs, distinguish recoverable/terminal/unknown outcomes, qualify retry/resume, reconcile side effects, handle cancellation races, and preserve domain semantic authority during operational intervention.
- [Provenance, Reproducibility & Historical Inspection](provenance-reproducibility-historical-inspection.md) — how actors explain and compare historical derivations, distinguish historical truth from current state, inspect identity/provenance gaps, and assess exact/semantic/statistical/bounded/comparative/insufficient reproduction capability without duplicating canonical state.
- [Enterprise Dependency, Offline/No-Egress & Safety](enterprise-dependency-offline-no-egress-safety.md) — how actors understand dependency profiles, local/provisioning/runtime network behavior, egress categories, sensitive source-derived state, restricted Evidence/Provenance, policy incompatibilities, and safe blocked/fallback behavior without hidden acquisition or generic safety authority.

Additional experience authorities may be added by later phases where genuinely new actor-visible semantics require them.

## Authority boundary

For conflicts:

1. `docs/authority/` governs cross-cutting policy/contracts;
2. `docs/concepts/` governs concept purpose, lifecycle, state, actions, and invariants;
3. `docs/synchronizations/` governs cross-concept coordination;
4. `docs/experience/` governs how those semantics are exposed to actors/programmatic users;
5. phase records preserve design history and rationale.

An experience view MAY combine information from several concepts for comprehension or task flow. Such composition MUST NOT create a new canonical owner for the combined state.

## Experience design rules

Phase 003 experience authority MUST preserve these rules:

- editable/pre-commit state remains distinguishable from historically committed state;
- current mutable aliases remain distinguishable from exact historical identities;
- semantic lifecycle remains distinguishable from Execution/Attempt/platform state;
- candidate/partial/checkpoint material remains distinguishable from promoted domain results;
- warnings/limitations/indeterminacy remain visible rather than coerced to success;
- Data Meaning, Constraint, and Synthesis Strategy remain distinct authorities even when preparation composes them;
- inferred meaning remains distinguishable from declared meaning and cannot silently overwrite it;
- Constraint handling remains distinguishable from output satisfaction;
- compatibility/readiness remain contextual derived assessments rather than global mutable concept state;
- Learning remains distinct from Learned State, and Execution completion does not establish Learning completion;
- Learning progress must be Strategy-meaningful rather than a fabricated universal percentage;
- checkpoints/intermediate state remain non-final until semantic Learning completion establishes Learned State;
- Learned State logical identity remains distinct from physical model/file/component representation;
- usable/restricted/retired/invalidated Learned State statuses remain distinct, and current future-use status does not rewrite history;
- Learned State reuse compatibility remains contextual to Generation rather than global mutable state;
- Generation Conditions remain request-specific and distinct from reusable Constraints;
- mandatory versus best-effort Condition strength and material tolerances remain visible before Generation commitment;
- physical output/materialization completion remains distinct from Generation semantic completion;
- partial, complete candidate, abandoned/quarantined, and completed output remain distinguishable;
- requirement-specific Evidence strength remains visible when it participates in Generation completion;
- final output promotion occurs only after all mandatory Generation completion obligations are satisfied;
- one successful Generation exposes one authoritative logical completed output even when physical realization is distributed/retried;
- Evaluation Criterion, Evaluation, Evidence, and external decision authority remain distinct;
- available metrics do not silently define the evaluative question;
- Evaluation success remains distinct from favorable subject Evidence;
- sampling/approximation/coverage/uncertainty and claim-strength limits remain inspectable;
- fidelity, utility, validity, privacy/disclosure risk, and other explicit Criteria remain distinct unless an explicit decision rule combines them;
- missing, conflicting, stale, superseded, inapplicable, and invalidated Evidence remain distinguishable;
- privacy/disclosure-risk Evidence remains threat-model scoped and does not imply approval or universal privacy;
- one logical Execution remains stable across valid retries/resumes while Attempt history stays inspectable;
- platform job/run identity remains a reference rather than SYNGAN Execution authority;
- retry/resume must preserve committed domain semantics and require contextual safety/compatibility validation;
- checkpoint existence does not imply resume safety or domain-result authority;
- unknown/indeterminate operational state remains explicit until reconciled or safely fenced;
- duplicate physical work may occur but must not create ambiguous duplicate authoritative semantic results;
- cancellation request remains distinct from terminal cancellation and its race outcome;
- operator intervention may repair operational realization but must not silently mutate committed semantic authority;
- canonical Execution monitoring references rather than copies complete platform telemetry;
- Provenance remains typed historical relationship authority and references rather than duplicates canonical state;
- historical inspection shows exact past bindings separately from current aliases/revisions/status;
- mutable aliases, URLs, or service names do not masquerade as sufficient historical identity when underlying state can change;
- provenance gaps/corrections remain inspectable and current-state substitution does not repair missing history silently;
- Reproducibility remains a target/conditions/equivalence contract with exact, semantic, statistical, bounded/approximate, comparative, and insufficient-context outcomes;
- seed presence alone does not imply exact deterministic reproduction;
- re-execution/reproduction-readiness remain distinct from successful reproduction;
- current reproducibility may degrade without rewriting historical truth;
- historical difference does not imply causality or superiority without Evaluation/Evidence;
- dependency profiles preserve self-contained, local-artifact, acquisition-network, and runtime-network distinctions where material;
- dependency availability remains distinct from identity, compatibility, and permission;
- missing dependencies never trigger hidden automatic acquisition or remote fallback;
- provisioning/acquisition network requirements remain distinguishable from runtime network requirements;
- network access remains distinguishable from source/source-derived/generated-data egress;
- egress disclosure does not itself authorize transmission;
- material dependency substitution is explicit rather than silently treated as equivalent;
- committed no-network/no-egress behavior remains binding through retry/recovery;
- Learned State, synthetic/candidate output, Evidence, diagnostics, and Provenance are not presumed non-sensitive merely because they are derived state;
- synthetic origin does not imply privacy, anonymity, export permission, or release approval;
- withheld/redacted, unknown, absent, and unavailable states remain distinguishable;
- restricted disclosure never rewrites historical Provenance or canonical state;
- current network/access policy may limit reproduction without rewriting historical truth;
- Evidence remains observation authority, not release/use approval;
- large-data workflows remain understandable without mandatory full driver-local materialization;
- programmatic and human-facing experiences preserve equivalent semantic distinctions even when their presentation differs.

## Representation boundary

These documents do not decide whether the experience is implemented through:

- Python objects or fluent builders;
- notebooks;
- CLI commands;
- REST/SDK resources;
- web UI pages;
- Spark DataFrame extensions;
- managed-platform integrations.

Later representation/API architecture may choose several surfaces while preserving this experience contract.
