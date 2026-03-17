# Decision Pipeline Overhead

## Setup

Two approaches were compared:

1. Flat agent using if/elif rules inside step()
2. Pipeline agent using stages:
   beliefs -> goal -> action

Both were run with:

- 100 agents
- 1000 steps

## Results

Flat agent:

- Condition checks: 190000
- Actions: 100000

Pipeline agent:

- Function calls: 300000
- Actions: 100000

## Observations

Both approaches produce the same number of actions.

However, the internal work differs:

- Flat approach performs fewer operations (condition checks)
- Pipeline approach performs more operations (function calls)

The pipeline introduces extra structure, but also extra overhead.

## Interpretation

The flat approach keeps everything inside step(), which is simple but mixes all logic together.

The pipeline approach separates decision stages (beliefs, goal, action), which is easier to reason about, but requires more function calls.

## Conclusion

Structured decision pipelines improve clarity of behavior, but require manual implementation and introduce additional overhead.

Mesa does not provide built-in support for this structure, so developers must implement it themselves inside step().