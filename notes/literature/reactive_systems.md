# Reactive Systems — Relevance to Behavioral Execution

## Overview

Reactive systems respond to changes in state or events.

Execution is triggered by:

- state transitions
- events
- signals

rather than continuous evaluation.

## Key Property

In reactive systems:

- computation happens only when relevant changes occur
- components are activated based on dependencies
- unnecessary evaluation is avoided

This contrasts with polling-based systems,
where all logic is evaluated repeatedly.

## Comparison to Current ABM Frameworks

In Mesa, NetLogo, and Agents.jl:

- agents are evaluated every step
- conditions are checked repeatedly
- behavior execution is tied to time progression

Even when event systems exist, they are:

- time-based (scheduled)
- not tied to condition satisfaction

As a result:

- behavior is evaluated even when nothing changes
- execution is not directly driven by state

## Implication

These systems follow a polling-based model,
not a reactive execution model.

This leads to:

- redundant computation
- implicit execution semantics
- tight coupling between behavior and scheduling

## Relevance to This Work

State-triggered execution aligns behavior with reactive principles:

- behavior activates when conditions become true
- evaluation is limited to relevant changes
- execution becomes explicitly defined

## Key Takeaway

The limitation in current systems is not the absence of events,
but the absence of reactive behavior execution.

This supports the need for:

- condition-driven activation
- dependency-aware evaluation