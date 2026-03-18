# Scheduler Behavior Experiment

## Setup

Two scheduling strategies were compared:

1. Fixed order: agents execute in the same sequence every step

2. Random order: agent execution order is shuffled each step

All agents are identical and follow the same rules:

- one shared resource is available per step
- only one agent can collect it
- the first agent to act acquires the resource

This setup isolates the effect of execution order under contention.

## Results

Fixed order:

[20, 0, 0, 0, 0]

Random order:

[1, 6, 3, 5, 5]

## Observations

- In fixed ordering, the first agent consistently acquires the resource
- All other agents are effectively excluded from interaction
- In random ordering, resource access is distributed across agents
- Outcomes differ despite identical agent logic and environment

This demonstrates that execution order directly affects agent outcomes.

## Key Insight

In step-based systems, behavior activation is tied to scheduler order.

This creates a structural dependency:

- agents act when they are scheduled
- not when conditions become true

Under contention:

- earlier agents systematically gain priority
- later agents may never act on available opportunities

This results in deterministic bias under fixed ordering.

## Limitation

Random scheduling reduces systematic bias but does not remove the underlying dependency on execution order:

- agents are still evaluated sequentially
- activation still depends on scheduler timing
- no mechanism exists for simultaneous or condition-based activation

## Conclusion

Scheduler ordering acts as an implicit control mechanism in time-driven execution. Behavior is not determined solely by rules, but also by when
agents are evaluated.

This introduces:

- deterministic bias (fixed order)
- stochastic variability (random order)
- outcome dependence on execution sequence

These effects arise from time-driven activation. A state-triggered execution model would reduce dependence on scheduler ordering by allowing behaviors to activate based on state changes rather than evaluation sequence.