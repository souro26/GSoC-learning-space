# Mesa Pain Points

These issues were observed while implementing behavioral models. They are not isolated inconveniences, but symptoms of how behavior execution is structured in Mesa.

## Repeated condition checks

Agents repeatedly evaluate the same conditions every step.

Example:

predator_nearby()
energy < threshold

These checks run even when no relevant state has changed. This happens because there is no mechanism for dependency-aware execution. The system does not track which variables affect which behaviors, so all conditions must be evaluated unconditionally. This leads to repeated evaluation of unchanged conditions, as confirmed by benchmarks comparing time driven and trigger based evaluations.

## Behavior logic accumulates inside step()

Most behavior is implemented inside the step() method.

As models grow:

- step() becomes longer
- logic becomes harder to maintain
- responsibilities become mixed

This is not just a structural issue. It happens because execution is tied to the scheduler, and there is no way to define independently activated behaviors. All behavior must therefore be placed inside a single entry point.

## Manual decision pipelines

Structured behaviors (e.g. BDI) require staged logic:

update_beliefs()
choose_goal()
form_intention()
act()

Mesa provides no abstraction for this. Developers must manually define and maintain the pipeline. Even though the logic is conceptually staged, execution remains part of the same step loop, with no control over when each stage should run.

## Policy and decision logic tightly coupled to agents

Policy-based approaches still embed logic inside the agent:

state = observe()
action = policy(state)

There is no mechanism to separate:

- policy definition
- policy execution
- activation conditions

As a result, policy evaluation is tied to the step loop, not to relevant state changes,

## Behavior depends on scheduler ordering

Agents act when the scheduler reaches them.

This introduces:

- ordering bias
- non-deterministic outcomes (under random scheduling)

Execution timing is determined by scheduler mechanics, not by when relevant state changes occur.

## Actions API does not address decision execution

Mesa 4.0 introduces an experimental Actions API.

It improves:

- action definition
- action reuse
- interruptible execution

However, it defines how actions execute, not when behaviors should be activated. Observation and decision logic remain inside step(). As a result, the core execution model remains time driven.

## Root Cause

The issues above are not independent. They arise from a shared limitation, which is behavior execution is tied to time driven scheduling rather than state changes.

As a result:

- all conditions are evaluated every step
- this leads to repeated evaluation of unchanged conditions
- behavior cannot be selectively activated
- logic accumulates inside a single execution point
- execution timing depends on scheduler order

This indicates that the limitation is not at the level of APIs, but at the level of execution semantics.