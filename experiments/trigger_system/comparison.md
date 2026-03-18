# Polling vs Trigger-Based Evaluation — Comparison

## Setup

We compare two evaluation approaches using the same environment and behavior logic:

- polling-based evaluation (conditions checked every step)
- trigger-based evaluation (conditions checked only on state change)

A single-agent system is simulated over 20 steps with a fixed state change rate. Each evaluation consists of 3 condition checks.

## Measurement

We count the total number of condition evaluations performed. This reflects the computational cost of decision logic.

## Results

Polling-based evaluation:

- total condition checks: 60
- evaluated every step (20 steps × 3 conditions)

Trigger-based evaluation:

- total condition checks: 24
- evaluated only on state changes (8 changes × 3 conditions)

## Observation

Both approaches produce identical behavior.

However:

- polling evaluates conditions continuously
- trigger-based evaluation skips steps where no relevant state change occurs

This results in a significant reduction in unnecessary evaluations.

## Key Insight

The difference is not in correctness, but in execution semantics. Polling evaluates conditions as part of time progression, while trigger-based evaluation ties condition checks to state changes. Efficiency gains emerge as a consequence of this difference.

## Implication

As the number of conditions increases, polling scales with:

number of steps × number of conditions

Trigger-based evaluation scales with:

number of state changes × number of conditions

This becomes important in models where state changes are sparse and agents evaluate multiple behavioral rules.

## Conclusion

Trigger-based evaluation reduces condition checks by ~60% in this setup, without changing agent behavior. This demonstrates that step-based polling performs unnecessary evaluation, which can be avoided through state-triggered execution.

This indicates that unnecessary evaluation is not an implementation issue, but a direct consequence of the time-driven execution model.