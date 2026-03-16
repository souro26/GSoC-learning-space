# Mesa Pain Points

These are things that felt awkward while implementing the models.

## Repeated condition checks

Agents check the same conditions every step.

Example:

predator_nearby()
energy < threshold

These checks run even if nothing has changed.

## Behavior logic stuck inside step()

Most behavior ends up inside the step() method.

As more rules are added, step() gets longer and harder to read.

There isn’t a simple built-in way to define behavioral rules outside this function.