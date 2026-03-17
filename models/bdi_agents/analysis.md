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

Beliefs are constructed by scanning neighboring cells for resources. Goals are derived directly from those beliefs. Intentions are implemented as simple action choices such as moving toward a resource or wandering. All of this logic is implemented inside the agent step() method.

## Notes

Even though the behavior is structured conceptually as
beliefs -> goals -> intentions -> actions,
the implementation still relies on procedural code
inside step().

Each stage of the BDI loop must be implemented manually.

## Questions Raised

1. How easy is it to reuse belief or intention logic across agents?
2. Does Mesa provide built-in support for separating beliefs,
goals, and actions?
3. How complex does the agent step() method become
when implementing richer BDI behavior?