# RL Agent Model

## Purpose

This model tests agents whose behavior is driven by a simple policy instead of rule checks or staged reasoning. The goal is to see how policy-style decision making fits into Mesa's agent structure.

## Scenario

Agents move on a grid that contains resources. When an agent detects a nearby resource it collects it. If no resource is detected it moves randomly. The simulation ends when all resources have been collected.

## Decision Structure

Agent behavior follows a simple loop:

observe state
choose action from policy
execute action

Example structure inside step():

state = observe()
action = policy(state)
act(action)

## Observations

The agent follows a policy-based decision structure:

state -> action

However, in Mesa:

- observation is recomputed every step through environment scanning
- policy evaluation is executed unconditionally each step
- action selection is tied directly to the step() loop

This means that even in a policy-based setup, decision evaluation remains time-driven rather than state-driven.

## Structural Limitation

Even though the decision logic is expressed as a policy, the execution model does not change:

- observation is still performed through repeated scanning
- policy evaluation is not triggered by state changes
- execution remains tied to the scheduler loop

This shows that adopting a policy-based structure does not address the nderlying execution semantics.

## Implications for Design

This model shows that even when behavior is expressed as a policy, execution remains step-based:

- observation is repeatedly recomputed
- policy evaluation is unconditional
- behavior cannot be activated based on state changes

This motivates:

- State-Triggered Execution: to evaluate policies only when relevant state changes occur

- Observation Helpers: to avoid repeated environment scanning

- Decision Pipelines: to separate observation, policy evaluation, and action execution

Without these, policy-based agents remain tightly coupled to the step() loop, limiting efficiency and modularity.