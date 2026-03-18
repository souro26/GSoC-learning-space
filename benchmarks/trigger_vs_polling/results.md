# Trigger vs Polling

## Setup

We compare two evaluation strategies:

- Polling: conditions evaluated every step
- Trigger-based: conditions evaluated only when state changes

Simulation:

- 100 agents
- 1000 steps

The frequency of state change is varied to observe how evaluation cost scales.

## Results

### Varying state change rate

| Change rate | Polling checks | Trigger checks | Reduction |
|------------|---------------|----------------|-----------|
| 5%         | 100000        | 4975           | 95.03%    |
| 10%        | 100000        | 9960           | 90.04%    |
| 20%        | 100000        | 20181          | 79.82%    |
| 50%        | 100000        | 50039          | 49.96%    |
| 80%        | 100000        | 79891          | 20.11%    |

### Dense system (always changing)

| Case              | Polling checks | Trigger checks |
|-------------------|----------------|----------------|
| Wolf–Sheep-like   | 100000         | 100000         |

## Observations

- Polling evaluates conditions at every step, regardless of relevance
- Trigger-based evaluation only runs when state changes occur
- As state changes become sparse, unnecessary evaluations in polling become dominant
- In dense systems where state changes every step, both approaches converge

## Key Insight

The difference between polling and trigger-based evaluation is not only quantitative, but structural.

Polling scales with:

number of steps × number of agents

Trigger-based evaluation scales with:

number of state changes × number of agents

This shows that polling performs evaluation as a function of time, while trigger-based evaluation performs evaluation as a function of state transitions.

## Implication

Unnecessary condition evaluation in polling is not an implementation detail,
but a direct consequence of time-driven execution. Trigger-based evaluation avoids this by tying condition checks to relevant state changes. Efficiency gains emerge as a result of this difference in execution semantics.

## Conclusion

Trigger-based evaluation reduces unnecessary condition checks in systems
where behavior is driven by infrequent state changes. In systems where state changes occur every step, both approaches behave similarly.

This demonstrates that the benefit of trigger-based systems depends on the relationship between state change frequency and evaluation frequency. More importantly, it highlights that the inefficiency in polling arises from the underlying execution model rather than from specific implementation choices.