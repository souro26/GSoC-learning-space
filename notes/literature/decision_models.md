# Decision Models — Relevance to Behavioral Structure

## Overview

Agent behavior can be expressed through multiple decision models:

- rule-based systems (if/else conditions)
- policy-based systems (state → action mappings)
- structured models (e.g. BDI)

These define how agents select actions.

## Common Requirement

Across all decision models:

- decisions depend on agent and environment state
- logic must be evaluated to select an action

However, in current systems, this evaluation happens every step.

## Limitation in Current Systems

In Mesa and similar frameworks:

- decision logic is embedded inside step()
- evaluation is unconditional
- there is no control over when decisions should run

This applies to:

- rule-based conditions
- policy functions
- staged decision pipelines

## Implication

Different decision models share the same constraint, they are all executed within a time-driven loop.

This leads to:

- repeated evaluation
- unnecessary computation
- lack of separation between decision and execution

## Relevance to This Work

Improving behavioral modeling is not about introducing new decision models.

It requires:

- separating decision logic from execution timing
- controlling when decision evaluation occurs

## Key Takeaway

The limitation is not in how decisions are defined, but in how they are executed.

This supports the need for explicit decision layers and decoupling from step-based execution