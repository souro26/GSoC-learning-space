# System: Agents.jl

## Behavior Model

Behavior is defined as external functions:

agent_step!(agent, model)

This separates behavior from agent structure via multiple dispatch. However, behavior remains imperative and monolithic, expressed through if/else logic.

## Observation

Agents access environment state via:

- direct model queries
- helper functions (e.g., nearby_agents)

Observation is embedded inside decision logic. There is no explicit perception layer.

## Activation

### Step-based (default)

All agents are evaluated every step:

for agent in agents:
    agent_step!(agent, model)

This is pure polling.

### Event-based (EventQueueABM)

Supports:

- time-based scheduling
- probabilistic events

However: Events are time-driven, not state-driven, and behavior logic still executes imperatively.

## Decision Structure

Decision-making is implemented via:

- if/else rules
- policy-based branching

There is no abstraction for:

- staged reasoning
- behavior prioritization
- decision pipelines

## Scheduling

Supports:

- random order
- deterministic order
- event queues (continuous time)

However: Execution order affects behavior, and there is no abstraction for dependency control.

eat!(), move!(), etc.

Behavior is reusable at function level, but there is no behavior abstraction layer, composition system, or lifecycle control.

## Strength

- Clean separation via functional design
- Strong event queue (time-based simulation)
- Better RL structuring than Mesa

## Limitation

- No state-driven activation
- No behavior abstraction layer
- No decision architecture
- Observation tightly coupled to logic

## Relevance to Mesa

### Validates

- Polling is dominant across systems  
- Decision logic is unstructured  
- Observation is ad hoc  

### Contradicts

- “Mesa lacks events” -> false  
(Agents.jl already supports this)

### Missing in Both Systems

- State-triggered execution  
- Behavior-level activation  
- Structured decision pipelines  
- Composable behavior units