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

The policy logic is implemented as a function that maps a state to an action.

Example:

resource nearby -> collect
otherwise -> move

Even though this is conceptually a policy-based agent, the implementation still happens inside the agent step() method.

## Notes

Observation of the environment is still done by scanning nearby cells. Policy selection and action execution are written directly in code.

## Questions Raised

1. How easily can external policies (for example trained models) be integrated with Mesa agents?
2. Does policy logic remain inside the step() function like other models?
3. Would separating observation and action selection make agent code easier to manage?