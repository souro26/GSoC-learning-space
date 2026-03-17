# Scheduler Behavior Experiment

## Setup

Two scheduling approaches were compared:

1. Fixed order:
   
   - Agents act in the same sequence every step

2. Random order:
   
   - Agent execution order is shuffled every step

All agents follow the same rules:

- A shared resource is available each step
- Only one agent can collect it
- The first agent to act gets the resource

## Results

Random Order:

[1, 6, 3, 5, 5]

Fixed Order:

[20, 0, 0, 0, 0]

## Observations

- In fixed order, the first agent consistently collects all resources.
- Other agents never get a chance to act on the resource.
- In random order, resource collection is distributed across agents.
- Outcomes vary even though agent logic is identical.

## Key Insight

Behavior is affected not only by rules, but also by execution order.

Even with identical agents and decision logic, different scheduling leads to different outcomes.

## Implication

This introduces a form of order sensitivity:

- Results depend on when agents are evaluated
- Behavior is not purely determined by rules

## Conclusion

Scheduler choice directly influences simulation outcomes.

This highlights the need for more explicit control over evaluation and execution order, especially when designing structured behavioral systems.