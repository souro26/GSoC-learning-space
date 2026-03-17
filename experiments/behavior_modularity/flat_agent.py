class FlatAgent:
    def __init__(self):
        self.energy = 10
        self.alive = True
        self.actions_taken = []

    def predator_nearby(self):
        # simulate condition
        return self.energy < 3

    def food_nearby(self):
        return self.energy < 6

    def step(self):
        if not self.alive:
            return

        # everything inside step()

        # escape logic
        if self.predator_nearby():
            self.actions_taken.append("flee")
            return

        # foraging logic
        if self.food_nearby():
            self.actions_taken.append("eat")
            self.energy += 2
            return

        # reproduction logic
        if self.energy > 12:
            self.actions_taken.append("reproduce")
            self.energy -= 5
            return

        # default
        self.actions_taken.append("wander")
        self.energy -= 1