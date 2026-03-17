# Trigger vs Polling

## Setup

We compare two approaches:

- Polling: condition checked every step
- Trigger-based: condition checked only when state changes

Simulation:

- 100 agents
- 1000 steps

We vary how often the agent’s state changes.

## Results

Varying state change rate

Change rate| Polling checks| Trigger checks| Reduction
5%| 100000| 4975| 95.03%
10%| 100000| 9960| 90.04%
20%| 100000| 20181| 79.82%
50%| 100000| 50039| 49.96%
80%| 100000| 79891| 20.11%

## Dense system (always changing)

Case| Polling checks| Trigger checks
Wolf–Sheep-like| 100000| 100000

## Observations

- Polling always evaluates conditions every step.
- Trigger-based evaluation runs only when state changes.
- As state changes become rarer, trigger checks drop significantly.
- When state changes every step, triggers provide no benefit.

## Key takeaway

Trigger-based evaluation reduces condition checks proportionally to how rarely state changes occur.

- At 5% change rate -> 95% reduction
- At 50% change rate -> 50% reduction
- At 80% change rate -> 20% reduction
- At 100% change rate -> no reduction

## Conclusion

Trigger-based systems are effective for models where behavior is driven by infrequent state transitions.

They do not provide benefits in models where state changes continuously.

This explains why trigger-based approaches work well for some behavioral systems but not others.