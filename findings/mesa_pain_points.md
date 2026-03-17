# Mesa Pain Points

These are things that felt awkward while implementing the models. They describe the friction points that became the basis for the primitive candidates.

## Repeated condition checks

Agents check the same conditions every step.

Example:

predator_nearby()
energy < threshold

These checks run even if nothing has changed.

## Behavior logic stuck inside step()

Most behavior ends up inside the step() method.

As more rules are added, step() gets longer and harder to read.

There isn’t a simple built-in way to define behavioral rules outside this function.

## Manual decision pipelines

When implementing structured behavior like BDI, the developer has to manually build the decision flow.

Typical pattern:

update_beliefs()
choose_goal()
form_intention()
act()

Mesa does not provide built-in helpers for this structure, so the entire pipeline has to be written manually.

## Hard to separate behavior stages

Even when behavior has clear stages (beliefs, goals, intentions, actions), they still end up implemented inside step().

As behavior grows, this function becomes the place where everything happens, which makes it harder to organize the logic.

## Policy logic inside agents

Even when using a policy-based approach, the policy still ends up written inside the agent class.

Example from the RL-style model:

state = observe()
action = policy(state)

There is no built-in structure in Mesa for separating policy logic from the agent implementation.

## Note on the Actions API

Mesa 4.0.0a0 introduces an experimental Actions API which helps separate timed action logic from the agent step() method.

This improves how actions are defined, reused, and interrupted with progress tracking.

However, observation and decision logic are still usually implemented manually inside step().

The models in this repository focus on those parts of agent behavior.