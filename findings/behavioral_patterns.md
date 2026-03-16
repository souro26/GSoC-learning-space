# Behavioral Patterns

These patterns showed up while building the test models.

## Pattern 1 — Threshold rules

A lot of behaviors are triggered when some internal value crosses a threshold.

Example from the predator–prey model:

energy < threshold → look for food

This is usually written directly inside "step()" as a simple "if" check.

## Pattern 2 — Scanning nearby cells

Agents often look at nearby cells to decide what to do.

Examples:

- sheep check if a wolf is nearby
- wolves check if sheep are nearby

This check happens every step.

## Pattern 3 — Behavior priority through code order

Agent decisions are usually written as a sequence of "if" statements.

Example:

1. predator nearby → flee
2. hungry → find food
3. otherwise → wander

The order of the conditions decides which behavior wins.