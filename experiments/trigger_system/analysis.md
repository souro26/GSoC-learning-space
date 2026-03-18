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
- Both approaches produce equivalent behavior, ensuring that differences arise from evaluation strategy rather than logic.
- Trigger-based evaluation assumes knowledge of which state variables affect each condition (dependency awareness).

## Key Difference

Polling:

- evaluation triggered by scheduler iteration
- conditions evaluated regardless of relevance
- execution frequency tied to time steps

Trigger-based:

- evaluation triggered by state changes
- conditions evaluated only when relevant variables change
- execution frequency tied to system state

This represents a shift from unconditional evaluation to dependency aware evaluation.

## Conclusion

This experiment shows that polling evaluates behavioral conditions as a function of time progression, not state changes. As a result conditions are evaluated even when no relevant state change occurs and evaluation is performed unnecessarily in steps where behavior would not change.

In contrast, trigger-based evaluation ties condition evaluation directly to state transitions. This demonstrates that the difference is not only computational, but structural:

polling -> time-driven evaluation  
trigger-based -> state-driven evaluation

This supports the need for a mechanism that decouples behavior evaluation from the step-based scheduler.