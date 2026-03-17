# Behavior Layers

While building the test models, a similar structure kept showing up in how agents behave.

The models were different (needs-based, BDI, policy-based), but the agent logic usually followed the same stages.

These layers are a way to describe what the agent code is doing in existing Mesa models. This pattern appeared across the three models built in this repository.

## 1. State

Agents keep track of internal variables and information about their environment.

Examples from the models:

energy
location
resources collected
nearby objects

In Mesa this is usually stored as normal attributes on the agent.

Example variables used in the models:

energy
inventory
resources_collected

## 2. Observation

Agents check their surroundings or internal state.

Examples from the models:

checking if a predator is nearby
checking if energy is below a threshold
checking if resources exist in nearby cells

Most of the time this is done by scanning neighboring cells.

Example pattern:

look at neighboring cells
check which agents are there

This logic is usually written directly inside step().

## 3. Decision

After observing the state, the agent decides what to do.

Different models handled this differently.

Examples:

Predator–prey model
if predator nearby → flee
if hungry → find food

BDI model
beliefs → goal → intention

Policy model
state → action

Even though the approaches are different, this stage always exists.

# 4. Action

Finally the agent performs an action.

Examples from the models:

move to another cell
collect a resource
flee from a predator

Actions usually change the environment or the agent’s state.

# Notes

In Mesa, these stages are usually all written inside the step() method.

That means step() ends up doing several things at once:

update state
observe the environment
decide what to do
execute the action

As models grow more complex, step() becomes the place where most behavior logic lives.

The layers described above simply help explain this structure.
They do not replace Mesa’s normal agent execution model.

Recent Mesa version introduce an Actions API which improves the action layer.

The layers described here focus mainly on observation and decision logic, which still tend to be implemented manually inside step().