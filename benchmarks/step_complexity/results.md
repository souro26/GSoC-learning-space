# Step Complexity Analysis

## Setup

Agents were tested with increasing numbers of rules inside step().

Two modes were used:

- Early exit (similar to if/elif chains)
- Full scan (evaluate all conditions every step)

Test parameters:

- 100 agents
- 1000 steps

## Results

Early Exit Mode

Rules: 1 -> 100000 checks
Rules: 3 -> 219265 checks
Rules: 5 -> 276403 checks
Rules: 10 -> 323852 checks
Rules: 20 -> 334912 checks

Full Scan Mode

Rules: 1 -> 100000 checks
Rules: 3 -> 300000 checks
Rules: 5 -> 500000 checks
Rules: 10 -> 1000000 checks
Rules: 20 -> 2000000 checks

## Observations

In full scan mode, the number of condition checks increases linearly with the number of rules.

Each additional rule adds a fixed amount of work every step.

In early exit mode, the number of checks still increases as rules increase, but the growth slows down due to early termination.

However, even with early exit, adding more rules still increases the total number of evaluations.

## Interpretation

All behavioral rules are evaluated inside the step() method.

As more rules are added:

- more conditions are checked every step
- the amount of work per step increases
- logic becomes harder to manage

Even in optimized cases (early exit), the structure still scales with the number of rules.

## Conclusion

The step() method scales with the number of behavioral rules.

This leads to:

- repeated condition evaluation
- increasing per-step workload
- growing complexity of agent logic

This supports the observation that behavior implemented inside step() does not scale cleanly as models become more complex.