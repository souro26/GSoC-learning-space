from mesa.discrete_space import CellAgent


class Sheep(CellAgent):
    def __init__(self, model, energy=10):
        super().__init__(model)
        self.energy = energy

    def step(self):
        self.energy -= 1

        if self.energy <= 0:
            self.remove()
            return

        if self.predator_nearby():
            self.flee()
            return

        if self.energy < 5:
            self.seek_food()
        else:
            self.random_move()

    def predator_nearby(self):
        for neighbor in self.cell.neighborhood:
            for agent in neighbor.agents:
                if isinstance(agent, Wolf):
                    return True
        return False

    def seek_food(self):
        self.cell = self.random.choice(list(self.cell.neighborhood))
        self.energy += 2

    def flee(self):
        self.cell = self.random.choice(list(self.cell.neighborhood))

    def random_move(self):
        self.cell = self.random.choice(list(self.cell.neighborhood))


class Wolf(CellAgent):
    def __init__(self, model, energy=15):
        super().__init__(model)
        self.energy = energy

    def step(self):
        self.energy -= 1

        if self.energy <= 0:
            self.remove()
            return

        sheep = self.find_sheep()

        if sheep:
            self.hunt(sheep)
        else:
            self.random_move()

    def find_sheep(self):
        for neighbor in self.cell.neighborhood:
            for agent in neighbor.agents:
                if isinstance(agent, Sheep):
                    return agent
        return None

    def hunt(self, sheep):
        sheep.remove()
        self.energy += 10

    def random_move(self):
        self.cell = self.random.choice(list(self.cell.neighborhood))