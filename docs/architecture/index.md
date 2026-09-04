---
type: Architecture Index
title: SYNGAN Representation & Architecture Design
status: active
---

# SYNGAN Representation & Architecture Design

## Purpose

This directory is the canonical home for representation and architecture decisions that map SYNGAN's accepted semantic and experience contracts into modules, interfaces, identities, persistence boundaries, data/reference models, runtime integrations, execution/recovery mechanisms, provenance/evidence structures, security/disclosure controls, and deployment/platform architecture.

Architecture is downstream of:

1. [Design Authority](../authority/index.md)
2. [Accepted Concepts](../concepts/index.md)
3. [Accepted Synchronizations](../synchronizations/index.md)
4. [Experience & Workflow Design](../experience/index.md)
5. [Phase 003 Consolidated Experience Contract](../experience/phase-003-consolidated-experience-contract.md)

Architecture MUST preserve those authorities. It may choose representations and boundaries; it may not redefine the semantic owner merely because one class, module, table, API, service, or platform primitive is convenient.

## Current phase

**Phase 004 — Representation & Architecture Design** is current.

See [Phase 004 index](../phases/004/index.md).

Next:

**004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction**

## Architecture authority rules

Phase 004 architecture SHOULD:

- make concept and experience contracts implementable without one-class-per-concept dogma;
- define clear package/module/service boundaries and dependency direction;
- distinguish control-plane state from distributed data/model/output payloads;
- preserve stable logical identity independently of mutable physical location;
- preserve semantic commitment separately from operational Execution;
- preserve non-final/candidate/checkpoint state separately from semantic promotion;
- support one logical Execution across multiple Attempts/platform jobs;
- support typed Evidence/Provenance/reproducibility without copying every payload/log;
- support core offline/no-egress operation and explicit optional network integrations;
- support local artifact resolution without hidden model/resource acquisition;
- preserve withheld/redacted/unknown/absent/unavailable distinctions where security architecture permits disclosure;
- remain viable for Spark-scale source/output workloads without mandatory driver-local materialization;
- remain model-neutral and platform-portable where the semantic contract permits it.

## Prohibited architecture shortcuts

Architecture MUST NOT assume by default that:

- one concept equals one Python class or database table;
- one workflow equals one state-owning `Session` object;
- one Spark/Databricks job equals one Execution;
- one physical model file equals Learned State;
- one DataFrame equals a completed Generation result;
- one metric/Boolean equals Evidence;
- one graph/database becomes the master copy of all Provenance and domain state;
- a seed proves deterministic reproduction;
- a network-capable integration may acquire artifacts or transmit data silently;
- a mutable table/model/URL alias is sufficient historical identity;
- CTGAN, GANs, Spark ML, PyTorch, HuggingFace, LLMs, Databricks, or any one framework defines universal SYNGAN semantics.

## Decision recording

Material architecture decisions should be stated canonically under `docs/architecture/` and, where a durable decision record is useful, accompanied by a focused record under `docs/decisions/` once that layer is established.

Phase records under `docs/phases/004/` preserve design execution/rationale and should link to canonical architecture authority rather than become competing architecture truth.

## Current architecture status

No final package layout, persistence technology, public API model, provenance store, manifest/fingerprint mechanism, scheduler/orchestrator, plugin architecture, model registry, security engine, or deployment topology is yet accepted merely by creation of this index.

Those decisions begin with Phase 004.