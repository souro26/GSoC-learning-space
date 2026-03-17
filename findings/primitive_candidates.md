# Primitive Candidates

These primitives are derived from patterns and pain points observed while implementing three behavioral models (needs-based agents, BDI agents, and RL-style agents) and supported by benchmarks.

The goal is not to introduce a new framework, but to identify small, reusable mechanisms that address specific issues in how behavioral logic is currently written in Mesa.

## Candidate 1 — Condition Triggers

### Problem

Many behaviors are driven by conditions:

- energy < threshold → seek food
- predator nearby → flee
- resource nearby → collect

These conditions are currently evaluated every step inside "step()".

From benchmarks:

- Step complexity grows with number of rules
- Repeated condition checks occur even when state does not change
- Trigger vs polling benchmark shows up to ~95% reduction in checks when state changes are sparse

### Idea

Introduce a small helper for registering condition → action rules.

Example:

energy < threshold → seek_food()

Instead of checking the condition every step, it is evaluated only when relevant state changes occur.

### Scope

- Helps with event-like behavior
- Does not replace all step logic
- Not useful for continuously changing systems (as shown in dense benchmarks)

## Candidate 2 — Observation Helpers

### Problem

Agents repeatedly scan their local environment:

- sheep scanning for wolves
- wolves scanning for sheep
- agents scanning for resources

This logic is:

- manually implemented
- repeated across models
- tightly coupled with decision logic

### Idea

Provide small helpers for common observation patterns.

Example:

observe_neighbors(type=Wolf)
observe_neighbors(type=Resource)

### Scope

- Reduces repeated code
- Keeps observation separate from decision logic
- Does not introduce new behavior systems

## Candidate 3 — Decision Pipelines

### Problem

Structured behavior (e.g. BDI) requires staged decision logic:

beliefs → goal → intention → action

Currently implemented manually inside "step()":

update_beliefs()
choose_goal()
form_intention()
act()

From experiments:

- Pipelines improve clarity
- But introduce overhead and must be manually structured

### Idea

Provide lightweight support for organizing staged decision logic.

This is not a full framework, but a small abstraction to make staged behavior explicit.

### Scope

- Improves readability and structure
- Does not enforce a specific architecture
- Does not replace "step()"

## Candidate 4 — Behavior Composition

### Problem

As behaviors increase, "step()" becomes long and hard to maintain.

Observed across models:

- escape logic
- foraging logic
- resource handling

All mixed inside a single function.

### Observation

This issue is not caused by lack of modularity features, but by the fact that:

- observation
- decision
- triggering

are all embedded inside "step()".

### Idea

By introducing primitives such as:

- condition triggers
- observation helpers
- structured decision stages

behavior logic can naturally be separated into smaller units.

### Example:

Foraging behavior and escape behavior can be written independently and combined at the agent level.

Scope

- This is not a new behavior framework
- Modularity emerges from better separation of concerns
- Keeps Mesa flexible while improving organization

## Notes

These primitives intentionally remain minimal.

Mesa 4.0 introduces an Actions API, which improves how actions are executed.

The primitives here focus on what is still missing:

- when actions should be triggered (observation)
- how decisions are structured

## Example:

hunger < threshold → eat()

In this case:

- trigger decides when behavior starts
- action system defines how it executes

The two are complementary, not competing.