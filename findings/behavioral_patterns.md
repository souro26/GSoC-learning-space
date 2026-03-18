# Behavioral Patterns

## Framing

These patterns describe how behavior is expressed in Mesa models. They are not independent design choices. They are consequences of the execution model: behavior is evaluated on every step.

This means:

- conditions are evaluated regardless of relevance
- observation, decision, and execution are recomputed each step
- behavior is driven by time progression rather than state changes

Experiments and benchmarks in this repository show that this leads to repeated evaluation and scaling issues as models grow.

## Pattern 1 — Threshold rules

Many behaviors depend on internal thresholds:

energy < threshold -> seek food

These conditions are implemented inside step() using if statements.

Because evaluation is step-based:

- conditions are checked every step
- even when the underlying state has not changed

This contributes to repeated condition evaluation observed in benchmarks.

## Pattern 2 — Environment scanning

Agents repeatedly scan their local environment:

- sheep detect nearby wolves
- wolves detect nearby sheep
- agents detect resources

This scanning is performed every step. There is no mechanism to react to environment changes directly, so agents must recompute observations continuously. This leads to unnecessary repeated work when the environment is unchanged.

## Pattern 3 — Behavior priority through code order

Behavior is often expressed as ordered conditions:

1. predator nearby -> flee  
2. hungry -> eat  
3. otherwise -> wander  

Priority is encoded implicitly through code order. This happens because:

- there is no explicit prioritization mechanism
- all conditions are evaluated within the same step

As a result, behavior becomes harder to modify and reason about.

## Pattern 4 — Decision pipelines

Some models introduce staged logic:

beliefs -> goal -> intention -> action  

This improves conceptual clarity.

However:

- all stages are still executed every step
- evaluation remains unconditional
- execution is still tied to the step loop

Benchmarks show that this structure does not reduce evaluation cost, and may increase it due to additional overhead.

## Pattern 5 — Observation-driven belief construction

Agent beliefs are built by scanning the environment:

- detecting nearby agents
- identifying resources
- constructing local state

This process is repeated every step. There is no mechanism to update beliefs only when relevant state changes occur. As a result:

- perception is recomputed even when nothing changes
- observation cost scales with time, not with events

## Pattern 6 — Policy-based decisions

Agents may use policies:

state -> action  

Even in this case:

- state is recomputed every step
- the policy is evaluated every step

There is no mechanism to trigger policy evaluation selectively. This means policy-based approaches do not change execution behavior, only how decisions are expressed.

## Pattern 7 — Observe -> decide -> act loop

Many agents follow observe -> decide -> act . This structure is conceptually clean, but:

- all stages are executed every step
- no stage is conditionally activated
- evaluation remains unconditional

This reinforces that structure does not change execution semantics.

## Pattern 8 — Scheduler-dependent activation

Agents are evaluated in a specific order each step. This leads to:

- ordering bias (fixed schedules)
- non-deterministic outcomes (random schedules)

Behavior depends not only on rules, but on when agents are evaluated. Since activation is tied to scheduler iteration:

- timing is determined by execution order
- not by when conditions become true

## Summary

Across all patterns:

- behavior is evaluated as a function of time steps
- not as a function of state changes

This leads to:

- repeated evaluation of unchanged conditions
- scaling with number of rules and agents
- coupling between behavior and scheduler execution

Experiments and benchmarks in this repository show that:

- structural changes (modularity, pipelines) do not fix this
- the limitation originates from the execution model itself

This motivates the need for state-driven execution, where behavior is evaluated only when relevant conditions change.