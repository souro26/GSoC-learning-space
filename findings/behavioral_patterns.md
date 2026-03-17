# Behavioral Patterns

These patterns showed up while building the test models (needs-based agents, BDI agents, and RL-style agents).

They describe the common ways behavior ends up being structured in Mesa models, and form the basis for identifying pain points and candidate improvements.

## Pattern 1 — Threshold rules

A lot of behaviors are triggered when some internal value crosses a threshold.

Example from the predator–prey model:

energy < threshold -> look for food

This is usually written directly inside step() as a simple if check.

## Pattern 2 — Scanning nearby cells

Agents often look at nearby cells to decide what to do.

Examples:

- sheep check if a wolf is nearby
- wolves check if sheep are nearby

This check happens every step.

## Pattern 3 — Behavior priority through code order

Agent decisions are usually written as a sequence of if statements.

Example:

1. predator nearby -> flee
2. hungry -> find food
3. otherwise -> wander

The order of the conditions decides which behavior wins.

## Pattern 4 — Decision pipelines

Some agents structure their behavior as a sequence of stages.

Example from the BDI model:

beliefs -> goal -> intention -> action

In code this ends up looking like:

update_beliefs()
choose_goal()
form_intention()
act()

Even though the logic is conceptually separated, it still runs inside the same step() method.

## Pattern 5 — Beliefs built by scanning the environment

In many models, an agent's beliefs are simply built by looking at nearby cells.

Examples:

- sheep scanning nearby cells to detect wolves
- BDI agents scanning nearby cells to detect resources

This scanning step happens every simulation tick.

## Pattern 6 — Policy-based decisions

Some agents choose actions based on a simple policy.

Example from the RL-style model:

state -> action

resource nearby -> collect
otherwise -> move

The policy is usually written as a function that takes the current state and returns an action.

## Pattern 7 — Observe -> decide -> act loop

Many agents follow a simple loop each step:

observe environment
decide what to do
execute the action

Example from the RL-style model:

state = observe()
action = policy(state)
act(action)

## Pattern 8 — Activation depends on scheduler order

Agents are executed in a specific order each step.

This order affects outcomes (not just behavior rules).

Earlier agents may act first and gain advantage.

Later agents may miss opportunities (e.g., starvation).

This shows that behavior depends not only on rules, but also on when agents are evaluated.