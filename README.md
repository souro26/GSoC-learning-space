# State-Triggered Behavioral Execution in Agent-Based Models

## Core Idea

Most agent-based modeling frameworks evaluate agent behavior at every time step, regardless of whether anything relevant has changed. This leads to repeated evaluation of unchanged conditions, unnecessary computation, and execution semantics tied to scheduler iteration rather than actual state changes.

This repository explores an alternative, evaluating behavior only when relevant state changes occur.

## Problem

Across major ABM frameworks (Mesa, NetLogo, Agents.jl, GAMA), behavior execution follows the same structure:

loop -> agent -> evaluate -> execute

Agents are stepped every cycle, and all behavior logic is re-evaluated even when nothing relevant has changed.

This results in:

- repeated condition checks
- execution driven by time instead of state
- behavior tightly coupled to scheduler ordering

Behavior is evaluated because time advances, not because conditions are met.

## Approach

This repository investigates a state-triggered execution model. Instead of evaluating behavior every step:

- conditions are evaluated when relevant state changes occur
- behaviors activate when conditions become true
- evaluation is performed only when relevant state changes occur

This is explored through:

- experiments (isolated behavior testing)
- benchmarks (quantitative validation)
- model implementations (real use cases)
- platform analysis (cross-system comparison)

## Experiments

Experiments isolate specific behavioral issues and test alternatives:

- trigger_system -> polling vs trigger-based evaluation
- behavior_modularity -> modular vs monolithic behavior
- observation_helpers -> structured vs manual observation
- scheduler_behavior -> impact of execution order

Each experiment focuses on one dimension of behavior.

## Benchmarks

Benchmarks quantify the cost of current approaches:

- trigger_vs_polling -> condition evaluation frequency
- step_complexity -> growth of step() logic
- decision_pipelines_overhead -> cost of structured decisions

Example result:

Time-driven (polling-based) execution evaluates 60 condition checks over 20 steps.

Trigger-based evaluation performs 24 checks under the same conditions, a 60% reduction.

Both approaches produce identical behavior.

## Models

Three models were implemented to test behavioral patterns:

- needs_predator_prey -> threshold-driven behavior
- bdi_agents -> staged decision pipelines
- rl_agents -> policy-based decisions

These expose how behavior is currently structured and where limitations appear.

## Findings

Across experiments and models:

- behavior is evaluated even when state is unchanged
- observation, decision, and execution are tightly coupled
- behavior logic accumulates inside step()
- execution order affects outcomes

These are not isolated issues. They come from the execution model. These issues arise from repeated evaluation of unchanged conditions.

## Primitive Candidates

Based on these findings, several minimal primitives are explored:

- condition triggers -> run behavior on state change
- observation helpers -> reusable perception logic
- decision pipelines -> structured decision stages
- behavior composition -> modular behavior units
- evaluation ordering -> explicit control over execution order

These are small, composable improvements made to the current framework.

## Platform Analysis

NetLogo, Agents.jl, and GAMA were analyzed. All follow time-driven execution:

- behavior evaluated every step or cycle
- no dependency-aware execution
- no state-driven activation

Differences exist in syntax and scheduling flexibility, but not in execution semantics.

## Key Insight

The limitation is not in APIs or syntax. It is in the execution model.Current systems evaluate behavior as part of time progression, regardless of whether relevant state has changed. This repository explores evaluation only when it matters.

## Repository Structure

- experiments/ -> isolated behavioral experiments
- benchmarks/ -> quantitative evaluation
- models/ -> agent implementations
- findings/ -> patterns and pain points
- platform_analysis/ -> cross-framework study
- notes/ -> architectural exploration

## Status

This repository represents the research and validation phase:

- problem identified through work with mesa.time
- validated across models and platforms
- supported by experiments and benchmarks

The next step is formalizing this into a system that integrates with Mesa
without breaking existing models.

For a concise project plan and proposal-style roadmap, see `proposal.md`.