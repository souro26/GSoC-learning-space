# Primitive Candidates

These are small ideas that might help with behavioral modeling in Mesa.
They come from patterns and problems seen in the three test models.
These are just possible helper tools that could make common behavior patterns easier to write.

## Candidate 1 — Condition Triggers

Many behaviors in the models are activated when some condition becomes true.

Examples:

energy < threshold -> seek food
predator nearby -> flee
resource nearby -> collect

Right now these conditions are written inside step() and checked every tick.

Example:

if energy < threshold:
seek_food()

if predator_nearby():
flee()

A trigger helper could allow registering rules like:

condition -> action

Example idea:

energy < threshold -> seek_food()

This would make behavior rules easier to read and could avoid repeating the same condition checks inside step().

Triggers would mainly help with event-like conditions.
They would not replace all behavior logic.

## Candidate 2 — Behavior Modules

In several models the step() function ends up containing most of the behavior logic.

Examples:

- predator escape logic
- food seeking logic
- resource collection logic

As more behaviors are added, step() becomes longer and harder to follow.

A simple idea is to allow behaviors to be grouped into small reusable modules.

Example:

ForagingBehavior
EscapeBehavior
CollectionBehavior

Agents could attach these modules instead of writing all rules directly inside step().

This could help with reuse across different agent types.

## Candidate 3 — Observation Helpers

Many models repeatedly scan nearby cells.

Examples:

- sheep scanning for wolves
- wolves scanning for sheep
- BDI agents scanning for resources
- RL agents scanning for resources

These checks are written manually each time.

Example pattern:

for neighbor in cell.neighborhood:
check agents in neighbor

A small helper for common observation tasks might reduce repeated code.

Example idea:

observe_neighbors(type=Wolf)
observe_neighbors(type=Resource)

This would simplify common environment checks.

## Candidate 4 — Decision Pipelines

Some models structure behavior as stages.

Examples:

BDI model:

beliefs -> goal -> intention -> action

RL-style model:

observe -> choose action -> act

These pipelines are currently implemented manually inside step().

Example:

update_beliefs()
choose_goal()
form_intention()
act()

A helper structure for simple decision pipelines might make this pattern clearer.

## Notes

These ideas are intentionally small.

Recent versions of Mesa introduce an Actions API, which helps organize how agents perform actions.

The primitives listed here focus on the parts that the Actions system does not address as much:

- observation of state and environment
- deciding when actions should start

For example, triggers could activate actions when certain conditions become true.

Example idea:

hunger < threshold -> eat()

In this case the trigger decides when the action should start, while the action system defines what the agent does.