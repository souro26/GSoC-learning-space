# System: NetLogo

## Behavior Model

Behavior is defined inside agent execution blocks:

ask agents [
    move
    eat
    reproduce
]

Each behavior is explicitly invoked and executed every tick. Behavior is procedural, not modular.

## Observation

Agents query environment using:

- local context (e.g., sheep-here)
- global agent sets

Observation is embedded within behavior procedures. No abstraction layer exists.

## Activation

All behaviors are evaluated every tick:

to go
  ask agents [ ... ]
  tick
end

This is a pure polling model.  There is no support for condition-triggered execution or event-driven activation.

## Decision Structure

Decision logic is written using:

- if conditions inside procedures

Example:

if prey != nobody [
    eat prey
]

There is no abstraction for decision pipelines, prioritization, or staged reasoning.

## Scheduling

Execution is:

- globally controlled
- step-based
- sequential

Order of behavior execution is manually defined and affects outcomes.

## Modularity

Behaviors are:

- plain procedures
- tightly coupled to execution flow

There is no support for composable behaviors, reusable behavior units, or dynamic attachment.

## Strength

- Extremely simple execution model
- Fast prototyping
- Clear mental mapping of simulation

## Limitation

- Inefficient polling-based execution
- No reactive behavior support
- No modularity
- No temporal flexibility

## Relevance to Mesa

### Validates

- Polling-based execution is standard  
- Behavior is scheduler-driven  
- Decision logic is embedded and unstructured  

### Contradicts

- No major contradictions identified. NetLogo follows the same step-driven execution model and is generally more constrained than Mesa in terms of extensibility and abstraction.

### Missing in Both Systems

- Behavior-level activation semantics  
- State-driven execution  
- Modular behavior composition  
- Structured decision architecture