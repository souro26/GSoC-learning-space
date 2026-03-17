# Trigger System Experiment

## Setup

Two evaluation approaches were compared:

1. Polling:
   
   - Conditions evaluated every step

2. Trigger-based:
   
   - Conditions evaluated only when state changes

A single agent was simulated over 20 steps with a fixed change rate.

## Results

Polling

- Conditions evaluated at every step

Example:

Step 0: evaluated
Step 1: evaluated
...
Step 19: evaluated

## Trigger-based

- Conditions evaluated only when state changes
- Steps without state change are skipped

Example:

Step 0: state changed -> evaluating
Step 1: state changed -> evaluating
Step 2: skipped
Step 3: skipped
...

## Observations

- Polling performs evaluation continuously, regardless of whether state changes.
- Trigger-based evaluation skips steps where no relevant change occurs.
- Evaluation is tied to state transitions instead of simulation time.

## Key Difference

Polling:

- Time-driven evaluation
- Every step -> evaluate conditions

Trigger-based:

- State-driven evaluation
- Only evaluate when state changes

## Conclusion

This experiment shows that trigger-based systems change the execution model, not just performance.

Instead of repeatedly checking conditions every step, evaluation becomes tied to state changes.

This supports the use of triggers as a primitive for handling event-like behavior more directly.