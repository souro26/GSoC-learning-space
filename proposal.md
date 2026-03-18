# GSoC Proposal Draft — Behavioral Modeling Support in Mesa

## Project Overview

This project evaluates how Mesa currently supports behavioral agent models and identifies small, practical improvements that make these patterns easier to implement and reason about.

The work is based on implementation, not assumptions:

- multiple behavioral models were built (needs-based, BDI-style, policy-based)
- experiments and benchmarks were created to measure execution patterns
- recurring issues were identified across models
- minimal abstractions were derived from those observations

The goal is not to introduce a new framework, but to improve how behavioral logic is expressed and executed using Mesa’s existing design.

## Target Audience & Use Cases

### Primary audience

- Mesa users building behavior-driven simulations (ecological, social, economic)
- Students and researchers who need structured and explainable agent logic
- Users porting models from NetLogo, GAMA, or Agents.jl

### Core use cases

- Agents reacting to conditions (hunger, threats, nearby agents)
- Multi-stage reasoning (belief → goal → action)
- Policy-based agents (state → action)
- Models where behavior should depend on state changes rather than being evaluated every step

In current Mesa usage, these patterns are typically implemented inside step(), leading to repeated condition checks and tightly coupled logic.


## Problem

Across all implemented models and supported by benchmarks:

- conditions are evaluated every step (polling)
- observation is recomputed every step
- behavior logic accumulates inside step()
- execution depends on scheduler order

These are not isolated issues. They come from a shared assumption:

behavior is evaluated because time advances, not because relevant state changes.

## What Has Been Done (Current Repo State)

The repository already contains:

### Models
- Needs-based predator–prey model
- BDI-style decision model
- Policy-based agent model

### Experiments
- Trigger vs polling evaluation
- Behavior modularity vs flat logic
- Scheduler ordering effects
- Observation helpers

### Benchmarks
- Condition evaluation cost (trigger vs polling)
- Step complexity growth
- Decision pipeline overhead

### Findings
- Behavioral patterns across models
- Mesa-specific pain points
- Primitive candidates derived from observations

These are used as the basis for the proposal, not as future work.

## Proposed Direction (Primitives)

From the findings, the following minimal primitives are identified:

### 1. State-triggered execution

- evaluate behavior only when relevant state changes
- avoid repeated condition checks
- decouple behavior activation from scheduler iteration

This is the only primitive that changes execution semantics.

### 2. Observation helpers

- reusable environment queries (neighbors, resources)
- separate observation from decision logic

### 3. Decision pipelines

- structured decision flow (belief → goal → action)
- improves clarity of behavior logic

### 4. Behavior composition

- modular, reusable behavior units
- reduce reliance on large step() functions

### 5. Evaluation ordering

- explicit control over execution order
- reduce unintended bias from scheduler ordering

These are intentionally small and composable. They do not require changes to Mesa’s core.

## User API Direction (Not Final)

The exact API is not finalized yet, but the direction is clear.

### Current pattern

python
def step(self):
    if predator_nearby():
        flee()
    elif energy < threshold:
        seek_food()