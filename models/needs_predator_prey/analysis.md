Needs-Based Predator–Prey Behavioral Model

Purpose
Study how Mesa supports agents driven by internal needs and behavioral rules.

Agents
Sheep
Wolf

Sheep behavior priority
1. predator nearby -> flee
2. hunger high -> eat grass
3. energy high -> reproduce
4. otherwise -> wander

Wolf behavior priority
1. sheep nearby -> hunt
2. hunger high -> search prey
3. energy high -> reproduce
4. otherwise -> wander

Research questions
How complex does step() become as rules increase?
Are conditions evaluated every step?
How reusable are behavioral rules across agents?
Does Mesa provide abstractions for behavioral rule systems?