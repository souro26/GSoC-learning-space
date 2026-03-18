# Decision Pipeline Overhead

## Setup

Two approaches were compared:

1. Flat agent using if/elif rules inside step()
2. Pipeline agent using staged decision logic: beliefs -> goal -> action

Both were run with:

- 100 agents
- 1000 steps

## Results

| Approach | Condition checks | Function calls | Actions |
|----------|----------------|----------------|---------|
| Flat     | 199000         | —              | 100000  |
| Pipeline | 300000         | 300000         | 100000  |

## Observations

- Both approaches produce identical behavior (same number of actions)
- The pipeline evaluates more conditions than the flat implementation
- The pipeline introduces additional function calls due to staged execution

## Key Insight

Decision pipelines do not reduce evaluation.  
They can increase it.

- flat logic benefits from early exit (if/elif short-circuiting)
- pipeline logic evaluates all conditions upfront (belief construction)

As a result:

- flat evaluation is partially selective
- pipeline evaluation is unconditional within each step

## Interpretation

The pipeline structure separates behavior into stages:

- observation (beliefs)
- decision (goal)
- execution (action)

However:

- all conditions are evaluated every step
- belief construction forces evaluation of all inputs
- early exit optim