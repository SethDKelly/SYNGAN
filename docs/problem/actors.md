---
type: Actor Inventory
title: SYNGAN Actors & Needs
status: active
---

# SYNGAN Actors & Needs

## Purpose of this inventory

This document identifies actor roles whose needs shape the problem. It does not define authorization concepts, software classes, or final personas.

One person may occupy several roles, and an enterprise may distribute one role across multiple teams.

## Primary actors

### Data Practitioner

A person who prepares, fits, generates, evaluates, or otherwise operates a synthetic-data workflow.

Needs include:

- working from Spark-resident structured data without mandatory full local materialization;
- understanding what the framework inferred versus what was explicitly declared;
- selecting or configuring synthesis behavior without needing to rewrite distributed infrastructure;
- observing long-running work and understanding failure state;
- reproducing or comparing prior runs;
- obtaining generated data in a form that composes naturally with Spark workflows;
- determining whether generated data is fit for the intended downstream use.

Examples may include data scientists, ML engineers, analytics engineers, data engineers, and researchers.

### Synthetic Data Consumer

A person or system that uses generated data downstream without necessarily operating the synthesis process.

Needs include:

- confidence that the dataset's intended semantics and limitations are documented;
- evidence about quality, validity, utility, and relevant privacy risk;
- stable schema and usable output representations;
- traceability to the synthesis configuration and evaluation evidence appropriate to the use case;
- clarity about what the generated data may and may not be assumed to preserve.

Examples may include application developers, testers, analysts, model developers, QA systems, benchmark systems, and training pipelines.

### Data Owner / Steward

A person or organizational function responsible for the meaning, permitted use, quality, or stewardship of source data.

Needs include:

- control over important source semantics and constraints;
- visibility into how sensitive or special fields are interpreted;
- traceability of synthesis activity involving governed data;
- the ability to distinguish inferred metadata from approved or declared semantics;
- evidence sufficient to review whether output is appropriate for a proposed use.

### Privacy / Risk / Governance Reviewer

A person or function responsible for reviewing privacy, compliance, disclosure, audit, or governance concerns.

Needs include:

- explicit avoidance of the assumption that synthetic means private;
- inspectable evidence for privacy or disclosure-risk claims;
- provenance for source interpretation, configuration, model/artifact lineage, generation, and evaluation;
- stable records sufficient to explain material decisions after execution;
- the ability to distinguish measured evidence from unsupported assurances.

## Operational actors

### Platform Operator

A person or team responsible for the Spark environment and computational resources on which SYNGAN runs.

Needs include:

- predictable and observable resource behavior;
- enough execution information to diagnose failures, skew, resource exhaustion, or abnormal runtime;
- compatibility with ordinary enterprise Spark operations;
- isolation of model/runtime-specific requirements where possible;
- operational controls appropriate to jobs that may run for extended periods and produce large outputs.

### Library Maintainer

A person or team responsible for evolving the SYNGAN package and its public contracts.

Needs include:

- concept and architecture boundaries that prevent model-specific behavior from leaking across the framework;
- stable documentation authority and provenance;
- testable compatibility contracts;
- a disciplined way to evolve capabilities without silently redefining existing semantics.

### Synthesizer / Extension Author

A developer who adds a synthesis strategy, evaluator, integration, or other extension to SYNGAN.

Needs include:

- explicit extension boundaries;
- clear requirements for distributed behavior, lifecycle, persistence, observability, and evaluation interoperability;
- the ability to implement algorithms with different computational needs without pretending all methods execute identically;
- enough framework support that extension authors do not need to recreate common enterprise controls.

## Actor distinctions that matter

The design MUST preserve several distinctions even when one person fills multiple roles:

- the operator of a synthesis job is not necessarily the owner of the source data;
- the producer of synthetic data is not necessarily its downstream consumer;
- a privacy reviewer is not necessarily the person who chose the synthesizer;
- the platform operator is concerned with execution health, not necessarily statistical validity;
- an extension author defines algorithm integration behavior but should not unilaterally redefine framework-wide semantics.

These distinctions are expected to influence later concept boundaries and synchronizations, but those concepts are intentionally not selected here.
