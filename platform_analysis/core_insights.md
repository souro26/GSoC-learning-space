# Core Insights from Platform Analysis

## 1. Common Execution Model

Across all analyzed frameworks (NetLogo, Agents.jl, GAMA, and Mesa), behavior execution follows the same structure:

loop → agent → evaluate → execute

Each agent is stepped as part of a global iteration, and all behavior logic is evaluated during that step. This means behavior is not selectively activated, but evaluated as part of a fixed execution cycle.

## 2. Time-Driven Execution

All analyzed frameworks execute behavior based on time progression:

- step-based loops (NetLogo, Mesa, Agents.jl)
- time-scheduled events (Agents.jl, Mesa)

In all cases: behavior is evaluated because time advances, not because conditions become true. Polling is one manifestation of this model, but the underlying issue is broader: execution is time-driven rather than condition-driven.

## 3. Behavior Execution is Agent-Centric

Behavior execution is embedded within the agent step function.

- behaviors do not exist as independently controlled execution units
- execution is triggered by agent activation
- there is no mechanism to control when a specific behavior should execute

As a result: behavior runs because the agent is scheduled, not because conditions are satisfied.

## 4. Observation, Decision, and Execution Are Coupled

Across frameworks:

- agents read environment state directly inside behavior logic
- decision logic is interleaved with execution
- there is no explicit separation of:
  - observe
  - decide
  - act

This leads to:

- tightly coupled logic
- limited reuse of behavior components
- lack of clarity around execution boundaries

More importantly, it reinforces the absence of explicit execution semantics.

## 5. Surface Improvements Do Not Change Execution Semantics

Different systems introduce improvements at the level of usability:

- NetLogo → simplified syntax
- GAMA → declarative DSL (reflex)
- Agents.jl / Mesa → time-based event scheduling

These improve:

- readability
- scheduling flexibility

However, they do not change the underlying execution model:

- behavior is still evaluated as part of time progression
- execution is not driven by state changes

As a result, the core limitation persists across systems.

## 6. Missing Execution Abstraction

Across all analyzed systems, the following abstraction is missing:

- behavior execution based on state transitions
- dependency-aware evaluation (only re-evaluate when relevant variables change)
- explicit control over when behavior should execute

Instead, all systems rely on a shared assumption:

«evaluate behavior as part of global time progression»

This reveals a fundamental gap: there is no formal model for condition-driven behavior execution.

## 7. Key Insight

The central limitation across systems is behavior execution is time-driven rather than state-driven

This is not a performance issue or a matter of API design. It is a limitation in how behavior execution is defined.

## 8. Direction

Addressing this limitation requires introducing an execution model where:

- behavior activation is driven by state changes
- evaluation is selective rather than global
- execution is decoupled from scheduler iteration

This motivates the exploration of state-triggered execution mechanisms, where behavior is activated when relevant conditions become true, rather than being evaluated at every step.