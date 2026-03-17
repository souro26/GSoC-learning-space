# System: GAMA

## Behavior Model

Behavior is defined using GAML constructs such as:

reflex move {
    ...
}

These appear declarative but are compiled into executable units.

Execution remains imperative under the hood.

## Observation

Agents access environment through:

- IScope interface
- spatial and population queries

Observation is:

- embedded in behavior logic
- not separated as a distinct phase

## Activation

Behavior execution is driven by simulation stepping:

stepAgents() → runner.step()

Reflex blocks are evaluated each simulation cycle.

→ Still polling-based execution

There is no true:

- state-triggered activation
- reactive execution model

## Decision Structure

Behavior logic is expressed via:

- reflex blocks
- conditional execution

However:

- no structured decision pipelines
- no explicit reasoning stages

## Scheduling

Execution is:

- centrally controlled
- step-based
- ordered via internal engine

Behavior execution order can influence outcomes.

## Modularity

GAMA provides higher-level constructs than Mesa:

- reflex blocks
- declarative syntax

However:

- behaviors are not independently composable
- no explicit lifecycle management
- limited reuse abstraction

## Strength

- Higher-level modeling abstraction
- Cleaner syntax than Mesa/NetLogo
- Better readability of behavior definitions

## Limitation

- Execution still polling-based
- No true reactive semantics
- No behavior composition model
- Observation tightly coupled to logic

## Relevance to Mesa

### Validates

- Even declarative systems remain step-driven  
- Behavior is not truly reactive  
- Observation and decision are tightly coupled  

### Contradicts

- “DSL solves behavior modeling” → false  
(GAMA improves syntax, not execution semantics)

### Missing in Both Systems

- State-driven activation  
- Behavior lifecycle management  
- Composable behavior architecture  
- Unified execution model