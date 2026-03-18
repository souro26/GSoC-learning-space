# Behavior Modularity Experiment

## Setup

Two versions of the same agent were implemented:

1. Flat agent:
   
   - All behavior written inside step()
   - Uses if/elif style rules

2. Modular agent:
   
   - Behavior split into small units (escape, forage, reproduce, wander)
   - Each unit defines check() and act()

Both versions use the same rules and priority order.

## Results

Flat Agent:

- Total actions: 250

Modular Agent:

- Total actions: 250

Example behavior sequences (first 10 steps):

Flat:
['wander', 'wander', 'wander', 'wander', 'wander', 'eat', 'wander', 'wander', 'eat', 'wander']

Modular:
['wander', 'wander', 'wander', 'wander', 'wander', 'eat', 'wander', 'wander', 'eat', 'wander']

## Performance Note

The modular approach introduces an additional loop over behaviors:

- Flat: sequential if/elif checks
- Modular: iteration over behavior objects with check() calls

This adds a small overhead due to:
- function calls (check, act)
- iteration over behavior list

However, in this experiment:
- no measurable difference in total actions
- overhead remains constant per step

This indicates that modular structure changes organization, not execution outcome, with minimal cost at this scale.

## Observations

- Both implementations produce identical behavior.
- Action counts match exactly.
- Behavior sequences follow the same pattern.

This confirms that both approaches implement the same logic.

## Differences

Flat approach:

- All logic is inside step()
- As rules grow, the function becomes longer
- Observation, decision, and action are mixed together

Modular approach:

- Behavior is separated into smaller units
- Each behavior is easier to read and modify
- Logic is organized, but execution remains centrally controlled by step()

## Limitation

The modular structure does not come from Mesa itself.

Developers must:

- define behavior classes manually
- manage execution order
- integrate everything inside step()

## Conclusion

Separating behavior into modules improves clarity without changing outcomes.  However, this modularity is structural, not semantic.

- behaviors are still evaluated every step
- execution is still controlled by the agent step() loop
- behavior activation is not independent

This means modularity alone does not change how behavior executes. 

To make behaviors truly independent units, execution must be decoupled from the step loop. This connects directly to state-triggered execution, where behaviors can be activated based on conditions rather than evaluated unconditionally.