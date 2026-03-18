# Behavioral Patterns

## Framing

These patterns describe how behavior is actually expressed in Mesa models. They are not independent design choices. They emerge from the underlying execution model: behavior is evaluated on every step. As a result, many of these patterns exist not because they are ideal, but because there is no mechanism for condition-driven execution. This leads to repeated evaluations of unchanged conditions across all patterns.

## Pattern 1 — Threshold rules

Many behaviors are triggered when an internal value crosses a threshold.

Example:

energy < threshold -> look for food

This is typically implemented inside step() using an if condition. There is no mechanism to register conditions as independent activation rules. As a result, threshold checks are evaluated every step, even when the underlying state has not changed.

## Pattern 2 — Scanning nearby cells

Agents repeatedly scan their local environment to make decisions.

Examples:

- sheep check if a wolf is nearby
- wolves check if sheep are nearby

These checks run every step. Since there is no mechanism to react to enviroment changes, agents must rescan the enviroment on every iteration.

## Pattern 3 — Behavior priority through code order

Agent decisions are often written as sequential if statements:

1. predator nearby -> flee
2. hungry -> find food
3. otherwise -> wander

The order of conditions determines which behavior executes. This pattern emerges because there is no explicit mechanism for behavior prioritization or conflict resolution. Priority is implicitly encoded in code structure, making behavior implicit and harder to reason about.

## Pattern 4 — Decision pipelines

Some models structure behavior into stages:

beliefs -> goal -> intention -> action

In code:

update_beliefs()
choose_goal()
form_intention()
act()

Although conceptually modular, all stages are executed inside the same step() function. This pattern shows an attempt to introduce structure, but execution remains tied to the global step loop. Execution is still tied to the global step loop instead of relevant state changes.

## Pattern 5 — Beliefs built through repeated scanning

Agent beliefs are often constructed by scanning the environment. This happens every step, even when no relevant changes have occurred. There is no observation layer that updates based on state changes, so perception is recomputed repeatedly.

## Pattern 6 — Policy-based decisions

Agents may use policies:

state -> action

Example:

resource nearby -> collect
otherwise -> move

The policy is typically implemented as a function, but is still evaluated every step. There is no mechanism to trigger policy evaluation only when the relevant state changes.

## Pattern 7 — Observe -> decide -> act loop

Many agents follow:

observe -> decide -> act

Example:

state = observe()
action = policy(state)
act(action)

This structure is conceptually clean, but execution remains unconditional. All stages are executed every step, regardless of whether new information is available.

## Pattern 8 — Activation depends on scheduler order

Agents are executed in a specific order each step.

This affects outcomes:

- earlier agents may act first and gain advantage
- later agents may miss opportunities

This shows that behavior depends not only on rules, but on when agents are evaluated. Since activation is tied to the scheduler, timing is driven by execution order, not state changes.

## Summary

All patterns reflect the same underlying constraint: behavior is evaluated as part of time-driven execution, not triggered by state changes. This results in repeated evaluation of unchanged conditions and implicit execution semantics across models.