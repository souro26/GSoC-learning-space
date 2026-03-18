# Scheduler Behavior Experiment

## Setup

Two scheduling strategies were compared:

1. Fixed order:
   - agents execute in the same sequence every step

2. Random order:
   - agents are shuffled before each step

Both simulations use identical agents, environment, and rules. The only difference is the order in which agents are activated.

## Results

Both approaches follow the same behavioral rules, but produce different outcomes over time.

Fixed ordering:

- agents act in a consistent sequence
- earlier agents repeatedly get priority

Random ordering:

- execution order varies each step
- opportunity is distributed more evenly across agents

## Observations

- Agent outcomes depend on when they are evaluated, not just on their rules
- Fixed ordering introduces systematic bias toward earlier agents
- Random ordering reduces bias but introduces variability
- Behavior is influenced by scheduler mechanics rather than purely by state

This shows that execution timing is not neutral.

## Key Insight

In step-based systems, behavior activation is tied to scheduler order. This creates an implicit dependency:

- when an agent acts depends on when it is scheduled
- not on when its conditions become true

As a result:

- agents may miss opportunities because they are evaluated later
- outcomes depend on execution order, not only on behavior logic

## Limitation

Random scheduling reduces ordering bias but does not eliminate it.

- agents are still evaluated once per step
- activation is still tied to the global step loop
- no mechanism exists to trigger behavior at the exact moment conditions change

## Conclusion

Scheduler ordering acts as an implicit control mechanism in step-based execution. Behavior is not only determined by rules, but also by when agents are evaluated.

This introduces:

- ordering bias
- timing-dependent outcomes
- reduced predictability of behavior

This issue arises because execution is tied to time progression rather than state changes. A state-triggered execution model would allow behaviors to activate when conditions become true, removing dependence on scheduler ordering.