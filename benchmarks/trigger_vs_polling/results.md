# Trigger vs Polling Benchmarks

## Setup

Three scenarios were tested:

- Schelling model
- Wolf–Sheep model
- Synthetic sparse-event model

Goal: compare condition checking using polling vs triggers.

## Results

Schelling

Small improvement (5–6%).

Conditions still need to be checked often, so triggers don’t help much.

## Wolf–Sheep

No improvement (sometimes slightly worse).

Agents interact continuously, so conditions are always relevant.

## Sparse-event model

Large improvement (90%+ fewer evaluations).

Most agents don’t need to react every step, so triggers avoid unnecessary checks.

## Takeaway

Triggers help when:

- behavior depends on rare events
- conditions don’t change often

Triggers don’t help much when:

- interactions are continuous
- conditions are almost always true

So triggers are useful, but only for certain types of models.