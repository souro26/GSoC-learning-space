# Trigger System — Execution Model (Repository-Level Design)

## Overview

This system introduces state-triggered execution for agent behavior.

Instead of evaluating behavior every step, conditions are evaluated
only when relevant state changes occur.

This shifts execution from time-driven to condition-driven activation.

## Core Concept

A trigger represents a condition that activates behavior.

Each trigger consists of:

- condition — a function over agent/environment state
- dependencies — variables the condition depends on
- activation rule — fires only on False → True transitions

## Dependency Tracking

Triggers explicitly declare the variables they depend on.

Example:

energy < threshold → depends on: energy

When a state variable changes:

- only triggers depending on that variable are evaluated
- unrelated triggers are not re-evaluated

This avoids evaluating all conditions every step.

## Edge-Based Activation

Triggers activate only when their condition transitions:

False → True

This prevents repeated execution when a condition remains true
across multiple steps.

## Execution Flow

The system follows this flow:

1. state change occurs
2. affected variables are identified
3. triggers depending on those variables are selected
4. selected triggers are evaluated
5. triggers that activate enqueue behaviors
6. behaviors are executed via the scheduler

This integrates with Mesa’s existing execution model.

## Integration with Mesa

This system does not replace Mesa’s scheduler.

- triggers act as an activation layer
- activated behaviors are passed to the scheduler
- execution is handled by existing mechanisms (e.g. Actions API)

This ensures compatibility with existing models.

## Ordering of Execution

When multiple triggers activate simultaneously:

- execution order must be defined
- possible strategies include:
  - insertion order
  - priority-based ordering

The exact policy is not fixed at this stage,
but must be explicitly controlled.

## Cascading and Cycles

Triggers can cause cascading activation chains:

A → B → C → A

Edge-based activation reduces repeated triggering,
but does not eliminate all cycles.

Handling cascading execution requires:

- limiting repeated activations within a cycle
- controlling execution depth or ordering

This is acknowledged as a limitation of the current design.

## Performance Considerations

Triggers reduce unnecessary condition evaluation
in systems where state changes are sparse.

However:

- tracking dependencies introduces overhead
- highly dynamic systems may reduce benefits

The effectiveness depends on the structure of the model.

## Limitations (Current Scope)

This design does not yet fully address:

- complete prevention of cascading loops
- automatic dependency tracking
- optimal execution ordering strategies

These are identified as areas for further refinement.

## Summary

The trigger system introduces:

- condition-driven activation
- dependency-aware evaluation
- explicit execution semantics

This addresses limitations of step-based polling,
while remaining compatible with Mesa’s existing architecture.