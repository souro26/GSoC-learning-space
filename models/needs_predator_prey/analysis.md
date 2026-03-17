# Needs-Based Predator–Prey Behavioral Model

# Purpose

This model explores how Mesa handles agents whose behavior is driven by internal needs and simple rule-based decisions. The goal is not to build a realistic ecological simulation but to observe how behavioral rules are implemented in Mesa and how the code structure scales as behaviors increase.

Agents
Sheep
Wolf

## Behavioral Structure

Sheep behavior priority

1. predator nearby -> flee
2. hunger high -> seek food
3. energy high -> reproduce
4. otherwise -> wander

Wolf behavior priority

1. sheep nearby -> hunt
2. hunger high -> search for prey
3. energy high -> reproduce
4. otherwise -> wander

These priorities are implemented directly inside the agent step() method using conditional statements.

Example pattern:

````python
if predator_nearby():
    flee()

elif energy < threshold:
    seek_food()

else:
    random_move()
````
The order of these checks implicitly defines behavior priority.

## Observation Mechanisms

Agents detect conditions in two ways:

Internal state checks
Example: energy < threshold

Environmental scanning
Example: checking nearby cells for predators or prey.

Both of these checks happen every simulation step. Even when the agent’s state has not changed, the same conditions are evaluated again.

## Decision Logic

Decision logic is procedural and embedded inside the step() method. Each behavior is expressed as a condition followed by an action.

There is no explicit representation of behavioral rules such as:

- rule objects
- behavior modules
- decision policies

Instead, rules are implemented directly in code. Behavior priority is determined by the order of conditional statements.

## Coupling of Responsibilities

Several responsibilities are mixed inside step():

state updates
environment observation
decision logic
action execution

Example flow inside step():

1. update internal state (energy decreases)
2. scan nearby cells for predators
3. evaluate hunger condition
4. choose behavior
5. execute movement or interaction

Because all of this logic is located in one function, step() becomes the central location for behavioral code. As more behaviors are added, the method grows longer and harder to reason about.

## Repeated Condition Evaluation

All behavioral conditions are checked every simulation step.

Examples:

- checking whether a predator is nearby
- checking hunger thresholds
- deciding whether to move randomly

These checks are performed even when nothing relevant has changed. This leads to repeated polling of behavioral conditions. For simple models this overhead is small, but in larger simulations it can lead to unnecessary evaluation.

## Behavior Reusability

Behavior rules are not easily reusable.

For example, the logic for:

- detecting predators
- evaluating hunger
- selecting movement

is embedded directly inside agent code. If another agent type needs similar behavior, the logic must be copied or rewritten. There is no built-in abstraction in Mesa for defining reusable behavioral rules.

## Step Complexity

The complexity of step() grows as new behaviors are added. Each additional rule introduces:

- another conditional check
- additional state observation
- new action logic

This leads to step methods that gradually accumulate behavioral logic. This pattern appears in many Mesa models and can make agent code difficult to maintain when behaviors become more complex.

## Research Questions

1. How complex does the step() method become as more behavioral rules are added?
2. Are behavioral conditions evaluated even when no relevant state change occurs?
3. How reusable are behavioral rules across different agent types?
4. Does Mesa provide abstractions for defining behavioral rules outside the step() method?
5. What patterns emerge across different behavioral architectures implemented in Mesa?
6. These questions guide the evaluation of Mesa’s support for behavioral modeling.