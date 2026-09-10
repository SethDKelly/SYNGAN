---
type: Actor Inventory
title: SYNGAN Actors & Needs
status: active
---

# SYNGAN Actors & Needs

## Purpose of this inventory

This document identifies actor roles whose needs shape the problem. It does not define authorization concepts, software classes, or final personas.

One person may occupy several roles, and an enterprise may distribute one role across multiple teams. Actor needs justify functionality; they do not imply that every actor receives a dedicated concept or interface.

## Primary actors

### Data Practitioner

A person who prepares, learns from, generates, evaluates, or otherwise operates a synthetic-data workflow.

Needs include:

- working from Spark-resident structured data without mandatory full local materialization;
- working with supported single-table, time-series, and multi-table shared-key subjects without manually flattening away material semantics;
- understanding what the framework inferred versus what was explicitly declared, including structural, temporal, identifier, categorical, and free-form-text meaning;
- selecting or configuring synthesis behavior without needing to rewrite distributed infrastructure;
- understanding Strategy-specific capabilities, limitations, resource needs, and dependency/network requirements before committing expensive or sensitive work;
- observing long-running work and understanding failure, cancellation, retry/recovery, and uncertainty without confusing platform state with semantic completion;
- reusing source-derived learned state when appropriate without being forced into Learning when a direct-generation Strategy is valid;
- reproducing or comparing prior work with qualified rather than overstated reproducibility claims;
- obtaining generated data in a form that composes naturally with Spark workflows;
- determining what Evidence exists about fitness for an intended downstream use.

Examples may include data scientists, ML engineers, analytics engineers, data engineers, and researchers.

### Synthetic Data Consumer

A person or system that uses generated data downstream without necessarily operating the synthesis process.

Needs include:

- confidence that the dataset's intended semantics, topology, and limitations are documented;
- Evidence about fidelity, validity, utility, and relevant privacy/disclosure risk without those dimensions being collapsed into one score;
- stable, usable output representations appropriate to the promised structured topology;
- traceability to the synthesis context and Evaluation Evidence appropriate to the use case;
- clarity about what the generated data may and may not be assumed to preserve;
- clarity that synthetic origin alone does not imply anonymity, privacy, or release approval.

Examples may include application developers, testers, analysts, model developers, QA systems, benchmark systems, and training pipelines.

### Data Owner / Steward

A person or organizational function responsible for the meaning, permitted use, quality, or stewardship of source data.

Needs include:

- control over important source semantics and prescriptive rules;
- visibility into how sensitive or special fields are interpreted;
- visibility into shared-key, relationship, entity/series, and temporal/order semantics where those affect synthesis;
- the ability to distinguish inferred interpretations from approved or declared meaning;
- traceability of synthesis activity involving governed data;
- Evidence sufficient to review whether output is suitable for a proposed use without making SYNGAN itself the organizational release authority.

### Privacy / Risk / Governance Reviewer

A person or function responsible for reviewing privacy, compliance, disclosure, audit, or governance concerns.

Needs include:

- explicit avoidance of the assumption that synthetic means private;
- inspectable Evidence for privacy or disclosure-risk claims, including text memorization or multi-table/longitudinal linkage risk where relevant;
- provenance for source interpretation, Strategy/configuration, Learned State, Generation, Execution, and Evaluation;
- stable records sufficient to explain material historical work after execution;
- the ability to distinguish measured Evidence from formal guarantees and unsupported assurances;
- explicit visibility into material dependency, network, and egress posture when it affects sensitive-data handling;
- preservation of the distinction between Evidence and external release/use authority.

## Operational actors

### Platform Operator

A person or team responsible for the Spark environment and computational resources on which SYNGAN runs.

Needs include:

- predictable and observable resource behavior;
- enough operational information to diagnose failures, skew, resource exhaustion, stalled work, or abnormal runtime;
- compatibility with ordinary enterprise Spark operations;
- isolation and explicit declaration of Strategy/runtime-specific requirements where possible;
- no hidden first-use package/model acquisition or remote inference fallback in profiles that claim offline/no-egress or self-contained operation;
- operational controls appropriate to work that may run for extended periods and produce large or multi-part outputs;
- confidence that worker/runtime readiness is not inferred solely from driver-local availability.

### Library Maintainer

A person or team responsible for evolving the SYNGAN package and its public contracts.

Needs include:

- concept and later architecture boundaries that prevent model-specific, topology-specific, or provider-specific behavior from leaking into universal framework semantics;
- stable documentation authority and design provenance;
- explicit compatibility and extension obligations;
- a disciplined way to evolve capabilities without silently redefining existing semantics;
- the ability to support new Strategies, topology shapes, Evaluation methods, and platforms without weakening the core conceptual model.

### Synthesizer / Extension Author

A developer who adds a synthesis Strategy, Evaluation method, integration, or related extension to SYNGAN.

Needs include:

- explicit extension boundaries;
- clear declarations of supported semantic/topology scope, Learning requirements, Generation behavior, Constraints, resource needs, reproducibility properties, dependencies, network/egress behavior, and known limitations;
- the ability to implement algorithms with different computational needs without pretending all methods execute identically;
- the ability to support direct Generation or Learning-based approaches according to actual method semantics;
- enough framework support that extension authors do not need to recreate common enterprise lifecycle, Evidence, Provenance, or operational controls;
- freedom to use optional local artifacts or explicit network services without making them hidden requirements for the supported baseline.

## Actor distinctions that matter

The design MUST preserve several distinctions even when one person fills multiple roles:

- the operator of a synthesis job is not necessarily the owner of the source data;
- the producer of synthetic data is not necessarily its downstream consumer;
- a privacy reviewer is not necessarily the person who chose the synthesis Strategy;
- the platform operator is concerned with execution health and environment readiness, not necessarily statistical validity;
- an extension author defines extension behavior but should not unilaterally redefine framework-wide semantics;
- a steward's authority over source meaning/rules is not the same as a reviewer's authority to assess Evidence;
- Evidence supporting a use decision is not itself the organizational authority to approve that use.

## Current actor-model assessment

Phase 008-B finds no new actor role required to justify the current accepted concept set.

Later concept mapping may introduce more specific interaction roles or personas, but those should be mappings of these needs unless a genuinely distinct authority/purpose is discovered. Likewise, organizational approval/release authority remains an external boundary under current evidence rather than a SYNGAN concept merely because some actors participate in that decision.