# Mesa Pain Points

These issues were observed while implementing behavioral models in Mesa. They are not isolated problems. They are direct consequences of the execution model, where behavior is evaluated on every step rather than triggered by state changes.

## Repeated condition evaluation

Agents repeatedly evaluate the same conditions every step.

Example:

predator_nearby()  
energy < threshold  

These checks run even when no relevant state has changed. This is a direct consequence of time-driven execution:

- the system does not track dependencies between state and behavior
- all conditions must be evaluated unconditionally
- evaluation is tied to time progression, not relevance

Benchmarks (trigger vs polling) show that this leads to large amounts of  unnecessary evaluation when state changes are sparse.


## Behavior logic accumulates inside step()

Most behavior is implemented inside the step() method.

As models grow:

- step() becomes longer
- responsibilities become mixed
- logic becomes harder to maintain

This is not just a structural issue. Because execution is tied to the scheduler:

- there is no mechanism to define independently activated behaviors
- all logic must be placed inside a single entry point

Step complexity benchmarks show that evaluation cost grows with the number of rules, even when most rules are not relevant.

## Manual decision pipelines

Structured behaviors (e.g. BDI) require staged logic:

update_beliefs()  
choose_goal()  
form_intention()  
act()  

Mesa provides no abstraction for this.

Developers must:

- implement the pipeline manually
- manage ordering explicitly
- execute all stages every step

Benchmarks show that this structure improves clarity but does not reduce evaluation cost, and may increase it due to additional overhead.

## Policy and decision logic tightly coupled to agents

Policy-based approaches still embed logic inside the agent:

state = observe()  
action = policy(state)  

There is no mechanism to separate:

- policy definition
- policy execution
- activation conditions

As a result:

- state is recomputed every step
- policy is evaluated every step
- execution remains tied to the step loop

---

## Behavior depends on scheduler ordering

Agents act when the scheduler reaches them.

This introduces:

- ordering bias (fixed scheduling)
- non-deterministic outcomes (random scheduling)

Execution timing is determined by scheduler mechanics, not by when relevant state changes occur. Experiments show that identical behavior can produce different outcomes depending on execution order.

## Actions API does not address decision execution

Mesa 4.0 introduces an experimental Actions API.

It improves:

- action definition
- action reuse
- interruptible execution

However it defines how actions execute over time, not when behaviors should be activated. Observation and decision logic remain inside step(). As a result, the execution model remains time-driven.

## Root Cause

These issues share a common origin: behavior execution is tied to time-driven scheduling rather than state changes.

As a result:

- conditions are evaluated every step
- evaluation is independent of relevance
- behavior cannot be selectively activated
- logic accumulates inside step()
- execution timing depends on scheduler order

This indicates that the limitation is not at the level of APIs, but at the level of execution semantics.