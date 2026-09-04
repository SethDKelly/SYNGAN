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
- network/external dependencies remain visible before commitment;
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
