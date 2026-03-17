# BDI Architecture — Relevance to Behavioral Modeling

## Overview

The Belief–Desire–Intention (BDI) model structures agent behavior into distinct decision stages:

- beliefs — information about the environment
- desires — possible goals
- intentions — selected goals to act upon

This creates an explicit decision process instead of ad-hoc rules.

## Typical Implementation Pattern

When implemented in Mesa, BDI agents usually follow:

update_beliefs()
choose_goal()
form_intention()
act()

All stages are executed sequentially inside the agent’s step() method.

## Structural Limitation

Although BDI is conceptually structured, its implementation in Mesa
reveals a constraint:

- all stages are evaluated every step
- there is no control over when each stage should run
- decision logic is tied to scheduler-driven execution

This collapses a structured decision model into a single execution flow.

## Implication

This highlights a broader issue: Mesa does not support decision stages as independently controlled units.

Instead:

- decision stages are manually defined
- execution timing is fixed
- evaluation is unconditional

As a result, structured models lose their intended modularity.

## Relevance to Behavioral Structure

BDI demonstrates the need for:

- explicit decision structure
- separation between decision and execution
- control over when decision stages are evaluated

This directly supports the idea of a decision layer that is
independent from execution timing.

## Key Insight

The limitation is not in the BDI model itself. It arises from how execution is defined in the framework.

This reinforces the need for decoupling decision logic from step-based execution and selectively evaluating decision stages based on state