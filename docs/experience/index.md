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

Additional experience authorities will be added by later Phase 003 groups.

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
- network/external dependencies remain visible before commitment and across Learned State reuse;
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
