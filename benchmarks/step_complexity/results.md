# Step Complexity Analysis

## Setup

Agents were tested with increasing numbers of behavioral rules inside step().

Two evaluation modes were used:

- Early exit: mimics if/elif chains (stop after first match)
- Full scan: evaluates all rules every step

Test parameters:

- 100 agents
- 1000 steps

## Results

### Early Exit Mode (if/elif behavior)

| Rules | Total checks |
|------|-------------|
| 1    | 100000      |
| 3    | 219265      |
| 5    | 276403      |
| 10   | 323852      |
| 20   | 334912      |

### Full Scan Mode (worst case)

| Rules | Total checks |
|------|-------------|
| 1    | 100000      |
| 3    | 300000      |
| 5    | 500000      |
| 10   | 1000000     |
| 20   | 2000000     |

## Observations

- In full scan mode, evaluation cost increases linearly with the number of rules
- Every additional rule adds a fixed amount of work per step
- In early exit mode, evaluation cost grows more slowly due to short-circuiting
- However, even with early exit, more rules still increase total evaluations

## Key Insight

The cost of behavior evaluation is tied to the number of rules, not to whether those rules are relevant.

This means:

- conditions are evaluated because they exist
- not because their underlying state has changed

Early exit reduces the average number of checks, but does not change the structure of evaluation.

## Interpretation

Behavior logic implemented inside step() scales with rule count:

- more rules → more condition checks
- more condition checks → higher per-step cost

This scaling occurs regardless of whether:

- the agent’s state has changed
- the environment has changed
- the condition is actually relevant

## Implication

This demonstrates that step-based execution enforces:

evaluation = f(number of rules × time steps)

rather than:

evaluation = f(relevant state changes)

As a result, adding new behaviors increases cost globally,
even if those behaviors are rarely triggered.

## Conclusion

The step()-based execution model does not scale cleanly with increasing behavioral complexity.

Even with optimizations like early exit:

- evaluation cost still grows with rule count
- condition checks remain tied to time progression

This reinforces the need for execution models where behavior is evaluated selectively, based on relevant state changes rather than on every simulation step.