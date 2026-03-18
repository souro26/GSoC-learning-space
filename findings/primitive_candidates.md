# Primitive Candidates

These primitives are derived from patterns and pain points observed while implementing three behavioral models (needs-based agents, BDI agents, and RL-style agents), and are supported by benchmarks and experiments conducted in this repository.

The goal is not to introduce a new framework, but to identify minimal, reusable mechanisms that address specific issues in how behavioral logic is currently expressed in Mesa.

## Core Direction

The primary limitation identified is that behavior execution in Mesa is time-driven rather than condition-driven. Behavior is evaluated because the scheduler advances, not because relevant conditions become true.

Among the candidates listed below, the central contribution is State-Triggered Execution (Candidate 1)

The remaining candidates:

- Observation Helpers
- Decision Pipelines
- Behavior Composition
- Evaluation Ordering

operate as supporting abstractions that become significantly more effective under a state-triggered execution model. They improve clarity and structure, but do not address execution semantics independently.

## Candidate 1 — State-Triggered Execution

### Problem

Many behaviors are driven by conditions:

- energy < threshold -> seek food
- predator nearby -> flee
- resource nearby -> collect

These conditions are currently evaluated at every step inside step().

From benchmarks:

- Step complexity increases with number of rules
- Conditions are checked repeatedly even when state does not change
- Trigger vs polling experiments show significant reduction in checks when changes are sparse

Additionally, agent behavior depends on scheduler activation order:

- fixed ordering can bias outcomes
- random ordering only partially mitigates this

### Implication

When behavior executes is determined by scheduler timing, not by when conditions become true. This creates a structural mismatch between state changes and behavior activation. 

### Idea

Introduce a state-triggered execution mechanism where behavior is evaluated only when relevant state changes occur.This is not a simple condition check, but a structured execution unit:

StateTrigger:
- condition: function(state) -> bool
- dependencies: set of variables the condition depends on
- activation rule: fires when condition transitions false -> true

Example:

energy < threshold -> seek_food()

Instead of evaluating this every step, the system tracks changes to energy and evaluates the condition only when energy is updated.

### Execution Semantics

Execution follows:

state change ->
    evaluate dependent triggers ->
        if condition becomes true ->
            schedule behavior execution

This introduces dependency-aware evaluation, where only relevant conditions are re-evaluated. This differs from event-based systems, where events are pre-scheduled in time. Here, activation emerges from state changes rather than from a predefined event timeline.

### Key Property

Execution is driven by state transitions with dependency tracking rather than  unconditional scheduler iteration. This is not an optimization layer. It introduces a different execution model.

### Additional Consideration

The system requires tracking dependencies between state variables and conditions. This can be implemented through explicit declaration of dependencies or automatic tracking mechanisms. The choice affects complexity and performance, and requires further evaluation. Incorrect or incomplete dependency specification can lead to missed activations or unnecessary evaluations. This introduces a trade-off between accuracy and overhead in dependency tracking.

## Candidate 2 — Observation Helpers

### Problem

Agents repeatedly scan their local environment:

- sheep scanning for wolves
- wolves scanning for sheep
- agents scanning for resources

This logic is:

- manually implemented
- repeated across models
- tightly coupled with decision logic

### Idea

Provide small helpers for common observation patterns.

Example:

observe_neighbors(type=Wolf)
observe_neighbors(type=Resource)

### Scope

- reduces repeated code
- separates observation from decision logic
- does not introduce new execution behavior

This operates at the observation layer and is independent of execution semantics.

Under step-based execution, these scans must be repeated every step. With state-triggered execution, observation can instead be updated in response to relevant environmental changes.

## Candidate 3 — Decision Pipelines

### Problem

Structured behavior (e.g. BDI) requires staged decision logic:

beliefs -> goal -> intention -> action

Currently implemented manually inside step():

update_beliefs()
choose_goal()
form_intention()
act()

From experiments:

- improves clarity
- introduces overhead
- remains manually structured

### Idea

Provide lightweight support for organizing staged decision logic. This is not a full framework, but a minimal abstraction to make staged behavior explicit. Also supports simple policy-based decision making (state -> action) by separating decision computation from execution.

### Scope

- improves readability and structure
- does not enforce a specific architecture
- does not change execution timing

This operates at the decision layer and does not affect when behavior is executed.

This becomes significantly more effective when combined with state-triggered execution, where individual stages can be activated based on relevant state changes rather than executed unconditionally.

## Candidate 4 — Behavior Composition

### Problem

As behaviors increase, step() becomes long and difficult to maintain.

Observed patterns:

- escape logic
- foraging logic
- resource handling

All combined in a single function.

### Observation

This is not simply a lack of modularity features. It arises because:

- observation
- decision
- execution

are all embedded together.

### Idea

By separating:

- execution (triggers)
- observation
- decision

behavior can be expressed as smaller, composable units.This is supported by the behavior_modularity experiment, where modular and flat implementations produced equivalent results with improved structure.

### Scope

- improves organization without enforcing a framework
- enables reuse across agents
- remains consistent with Mesa’s flexible design

This emerges from improved separation of concerns, not from a new execution model.

This relies on separating activation (when behavior runs) from logic (what behavior does), which is not possible under purely step-based execution.

## Candidate 5 — Evaluation Ordering

### Problem

From experiments:

- agent execution order affects outcomes
- fixed ordering introduces bias
- random ordering changes results but does not eliminate dependence

This means behavior depends not only on rules, but also on when agents are evaluated.

### Idea

Provide explicit control over evaluation ordering:

- random
- fixed
- priority-based

### Scope

- improves transparency of execution timing
- reduces unintended bias
- does not replace the scheduler

This is a secondary concern related to scheduler behavior and does not address execution semantics directly. This becomes particularly relevant when multiple triggers activate simultaneously, requiring explicit resolution of execution order.

## Notes

These primitives are intentionally minimal. Mesa 4.0 introduces an Actions API, which improves how actions are executed.

The primitives here focus on what is still missing:

- when behaviors should be triggered (execution)
- how decisions are structured (decision)

Example:

hunger < threshold -> eat()

In this case:

- the trigger determines when behavior starts
- the action system defines how it executes

These are complementary and do not overlap in responsibility. This separation ensures that execution semantics (when behavior runs) and action semantics (how behavior runs) remain distinct.

## Mapping: Pain Points -> Primitives

- Repeated condition checks -> State-Triggered Execution
- Behavior logic inside step() -> Decision Pipelines + Behavior Composition
- Manual decision pipelines -> Decision Pipelines
- Policy and decision logic inside agents -> Decision Pipelines
- Repeated environment scanning -> Observation Helpers
- Behavior depends on scheduler ordering -> Evaluation Ordering + State-Triggered Execution