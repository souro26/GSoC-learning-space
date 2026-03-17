# Core Insights from Platform Analysis

## 1. Common Execution Model

Across all analyzed frameworks (NetLogo, Agents.jl, GAMA), behavior execution follows the same pattern:

loop → agent → evaluate → execute

Each agent is stepped every cycle, and all behavior logic is re-evaluated regardless of whether anything relevant has changed.

This is the default assumption across systems.

## 2. Time-Driven Execution

All analyzed frameworks execute behavior based on time progression:

- step-based loops (NetLogo, Mesa, Agents.jl)
- time-scheduled events (Agents.jl, Mesa)

In all cases behavior is evaluated because time advances, not because conditions become true

Polling is one manifestation of this model, but the core issue is execution is time-driven rather than condition-driven

## 3. Behavior is Not a First-Class Unit

## 3. Behavior Execution is Agent-Centric

Behavior execution is embedded within the agent step function.

- behaviors do not exist as independently controlled execution units
- execution is tied to agent activation by the scheduler
- there is no mechanism to control when a specific behavior should execute

This reinforces the time-driven model, where behavior runs because the agent is stepped, not because conditions are met.

## 4. Observation, Decision, Execution Are Mixed

Across frameworks:

- agents read environment state directly inside behavior code
- decision logic is mixed with execution
- no clear separation of:
  - observe
  - decide
  - act

This makes:
- behavior harder to reuse
- logic harder to test
- systems harder to extend

This further reinforces the lack of explicit execution semantics, as there is no clear boundary between when behavior should run and how it is computed.

## 5. Existing Improvements Don’t Solve It

Different systems try to improve things, but only at the surface:

- NetLogo → simple but fully polling
- Agents.jl → adds time-based events, not state-driven execution
- GAMA → adds DSL (reflex), but still step-based underneath

These systems introduce improvements in:

- syntax (NetLogo, GAMA)
- scheduling flexibility (Mesa, Agents.jl)

However, they do not change the fundamental execution model:

- behavior is still evaluated as part of time progression
- execution is not tied to state changes

As a result, the core limitation remains unaddressed.

## 6. Missing Execution Abstraction

Across all analyzed systems, the following abstraction is missing:

- behavior execution based on state transitions
- dependency-aware evaluation (only re-evaluate when relevant variables change)
- explicit control over when a behavior should execute

Instead, all systems assume evaluate behavior as part of global time progression. This reveals a fundamental gap: there is no formal model for condition-driven behavior execution.


## 7. Direction

The limitation identified is not related to syntax, APIs, or individual features. It is rooted in how behavior execution is defined.

Addressing this requires introducing an execution model where:

- behavior activation is driven by state changes
- evaluation is selective rather than global
- execution is decoupled from scheduler iteration

This forms the basis for exploring state-triggered execution mechanisms.