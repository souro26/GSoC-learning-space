RL Agent Model

Purpose

Test how Mesa handles agents whose behavior is determined by a policy instead of rule checks or staged reasoning.

Scenario

Agents move around a grid trying to collect resources.

Each agent chooses actions based on a simple policy:
move toward resource if seen, otherwise explore.

The goal is not to train a real reinforcement learning model but to mimic a policy-based decision process.

Decision structure

observe state
choose action from policy
execute action

Questions

How easy is it to plug policy-based decision making into Mesa agents?

Does the policy logic end up inside step() like other models?