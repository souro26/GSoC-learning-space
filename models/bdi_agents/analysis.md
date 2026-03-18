# BDI Resource Collection Model

## Purpose

This model explores how Mesa supports agents that follow a simple Belief–Desire–Intention decision structure. Agents observe their surroundings, choose a goal, form an intention, and execute an action. The goal is not to implement a full BDI system but to observe how Mesa code is structured when this style of behavior is implemented.

## Scenario

Agents move on a grid containing resource objects. When an agent detects a nearby resource it tries to collect it. If no resource is detected the agent explores randomly. The simulation ends when all resources have been collected.

## Decision Structure

Agent behavior follows a simple BDI loop inside step():

update beliefs
choose goal
form intention
execute action

Example structure:

update_beliefs()
choose_goal()
form_intention()
act()

## Observations

The BDI structure introduces clear conceptual stages:

beliefs -> goals -> intentions -> actions

However, in Mesa:

- all stages are executed unconditionally every step
- belief updates require repeated scanning of the environment
- goal and intention logic are tightly coupled to execution

This leads to two issues:

1. No selective activation: Even when no new information is available, the full decision pipeline is executed every step.

2. Execution tied to step(): The BDI loop cannot be expressed as independently activated stages. All logic must remain inside a single step() method.

## Structural Limitation

Although the behavior is conceptually structured, the execution model does not support this structure.

- stages cannot be independently activated
- observation, decision, and execution are tightly coupled
- the entire pipeline runs on every scheduler step

This shows that structured behavior can be expressed, but not natively supported at the execution level.

## Implications for Design

This model highlights the need for:

- Decision Pipelines: to represent staged behavior explicitly

- Observation Helpers: to avoid repeated environment scanning

- State-Triggered Execution: to activate decision stages only when relevant state changes occur

Without these, structured behavior remains manually implemented and tied to step-based execution.
