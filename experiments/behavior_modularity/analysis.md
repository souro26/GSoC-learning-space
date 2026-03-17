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

## Observations

- Both implementations produce identical behavior.
- Action counts match exactly.
- Behavior sequences follow the same pattern.

This confirms that both approaches implement the same logic.

---

Differences

Flat approach:

- All logic is inside step()
- As rules grow, the function becomes longer
- Observation, decision, and action are mixed together

Modular approach:

- Behavior is separated into smaller units
- Each behavior is easier to read and modify
- Logic is organized, but still manually structured

## Limitation

The modular structure does not come from Mesa itself.

Developers must:

- define behavior classes manually
- manage execution order
- integrate everything inside step()

## Conclusion

Separating behavior improves clarity without changing outcomes.

However, this structure must currently be implemented manually.

This supports the need for small primitives that help separate:

- observation
- decision
- action

rather than introducing a full behavioral framework.