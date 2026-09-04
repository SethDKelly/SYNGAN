---
type: Concept
title: Synthesis Strategy
status: accepted
---

# Synthesis Strategy

## Purpose

Enable actors to select, configure, compare, and inspect the synthesis behavior to be used without making one algorithm family universal SYNGAN semantics.

## Owns

- strategy identity and semantic version;
- synthesis-relevant configuration;
- declared capabilities and requirements;
- known semantic/operational limitations relevant to use.

Context-specific compatibility results belong to the activity performing validation.

## Actions

Select, configure/revise, inspect capabilities/limitations, compare, and validate for a proposed context.

## Invariants

1. Strategy MUST NOT be defined as an implementation class or plugin registry.
2. Strategy capability/limitation authority belongs here; contextual `compatible` state MUST NOT be globally accumulated here.
3. Activities MUST bind the exact Strategy/configuration revision they commit to.
4. A later Strategy revision MUST NOT rewrite historical Learning, Learned State, or Generation provenance.

## Operational principle

Before expensive work, a practitioner compares strategies against required semantics and capabilities, chooses one, configures it, and reuses that stable configuration across activities.

## Boundaries

Synthesis Strategy is not Learning, Learned State, Generation, Execution, or implementation registration.

## Synchronization

See [SYNC-02](../synchronizations/core-synchronizations.md#sync-02--strategy-selection-and-compatibility).
