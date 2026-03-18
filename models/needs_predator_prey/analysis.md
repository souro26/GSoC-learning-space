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
The order of these checks implicitly defines behavior priority. The priority is not represented explicitly. It is encoded through the order of conditional statements, which makes behavior harder to modify, reason about and extend. 

## Observation Mechanisms

Agents detect conditions in two ways:

Internal state checks
Example: energy < threshold

Environmental scanning
Example: checking nearby cells for predators or prey.

Both of these checks happen every simulation step, regardless of whether the underlying state or environment has changed. This reflects a polling-based execution model, where conditions must be repeatedly evaluated because there is no mechanism to react to state changes directly.

## Decision Logic

Decision logic is procedural and embedded inside the step() method. Each behavior is expressed as a condition followed by an action.

There is no explicit representation of behavioral rules such as:

- rule objects
- behavior modules
- decision policies

As a result, behavioral rules are tightly coupled to execution.There is no way to define conditions independently from the step() loop, making it difficult to control when behavior should be evaluated.

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

Because all of this logic is located in one function, step() becomes the central location for behavioral code. As more behaviors are added, the method grows longer and harder to reason about. This coupling arises because execution is centralized in step(), with no mechanism to separate activation from behavior logic.

## Repeated Condition Evaluation

All behavioral conditions are checked every simulation step.

Examples:

- checking whether a predator is nearby
- checking hunger thresholds
- deciding whether to move randomly

These checks are performed even when nothing relevant has changed. This leads to repeated evaluation of unchanged conditions. From benchmarks, this results in unnecessary computation when state changes are sparse, as the same conditions are
checked even when no relevant updates occur. For simple models this overhead is small, but in larger simulations it can lead to unnecessary evaluation.

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

This leads to step methods that gradually accumulate behavioral logic. This pattern appears in many Mesa models and can make agent code difficult to maintain when behaviors become more complex. This leads to linear growth in condition evaluation within step(), increasing both complexity and maintenance overhead as models scale.

## Implications for Design

This model highlights several limitations of step-based execution:

- behavioral conditions are evaluated through repeated polling
- behavior priority is implicit in code structure
- observation, decision, and execution are tightly coupled
- behavior cannot be activated based on state changes

This motivates the need for:

- State-Triggered Execution: to evaluate conditions only when relevant state   hanges occur

- Observation Helpers: to structure and reuse environment scanning logic

- Behavior Composition: to separate behavioral units from the step() method

Without these, behavior remains tightly coupled to the
scheduler and difficult to scale as complexity increases.
