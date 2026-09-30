# RESILIENT INTELLIGENCE

> **Status: under development.** This project is in an early, exploratory
> research phase. Concepts, architecture, and terminology described below
> are subject to change as the work progresses.

## Overview

RESILIENT INTELLIGENCE is a research project investigating human-centered
intelligence for maintaining traceable knowledge in evolving software
codebases.

The current concrete validation domain for this research is **software
codebases**.

## Research Direction

The project investigates whether explicit representation of evidence,
claims, beliefs, temporal state, provenance, and semantic dependencies can
support targeted revalidation of derived knowledge when an evolving
software codebase changes.

This is an open research question. No claims are made here about novelty,
completeness, or superiority relative to other systems or approaches. The
findings, architecture, and scope described in this repository will evolve
as the work continues.

## Conceptual Flow

The research explores a knowledge lifecycle roughly following this flow:

```
Evidence
  -> Claim
  -> Belief
  -> Temporal State
  -> Provenance
  -> Semantic Dependency
  -> Change
  -> Impact
  -> Targeted Revalidation
  -> Updated State
  -> Human-facing Explanation
```

The intent is to trace how a piece of evidence becomes a claim, how a
claim is held as a belief with a temporal and provenance context, how
semantic dependencies link beliefs to parts of a codebase, and how a
change to that codebase can trigger targeted revalidation of only the
affected knowledge, ending in an updated state with a human-facing
explanation.

## Repository Structure

```
archives/   preserved project/archive material
docs/       RI research and project documentation
graphify/   preserved Graphify-based codebase baseline
images/     project diagrams and visual assets
```

## Role of Graphify

The `graphify/` directory contains a preserved third-party Graphify
codebase snapshot that is being studied as an existing software
codebase/graph substrate and baseline for RI research.

RESILIENT INTELLIGENCE is **not** simply a rename of Graphify. The two
projects address different, related concerns:

- **Graphify** focuses on structural codebase intelligence: building a
  graph representation of a codebase's structure.
- **RESILIENT INTELLIGENCE** focuses on semantic evidence-to-belief
  knowledge maintenance: how derived knowledge about a codebase is formed,
  tracked over time, and selectively revalidated as the codebase changes.

Graphify is treated as an existing baseline to study, compare against, and
learn from during RI research. See `THIRD_PARTY_NOTICES.md` for provenance
details on the preserved Graphify material.

## Documentation

Research and project documentation live under `docs/`, including
reverse-engineering notes on Graphify, capability gap analysis, and
architecture planning documents.

## Status Notes

This repository is currently being bootstrapped. Installation and usage
instructions will be added once there is RI-original code to support them.
