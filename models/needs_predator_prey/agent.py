from mesa.agent import Agent
import random


class Sheep(Agent):

    def __init__(self, model):
        super().__init__(model)

        self.energy = random.randint(5, 10)
        self.hunger = random.randint(0, 5)
        self.fear = 0
        self.age = 0
        self.pos = None

    def step(self):

        self.age += 1
        self.energy -= 1
        self.hunger += 1

        if self.predator_nearby():
            self.flee()

        elif self.hunger > 7:
            self.eat_grass()

        elif self.energy > 12:
            self.reproduce()

        else:
            self.wander()

    def get_neighbor_cells(self):

        cell = self.model.grid._cells[self.pos]
        return list(cell.get_neighborhood(include_center=False))

    def predator_nearby(self):

        for cell in self.get_neighbor_cells():
            for agent in cell.agents:
                if isinstance(agent, Wolf):
                    return True

        return False

    def move_to_cell(self, new_cell):

        current_cell = self.model.grid._cells[self.pos]

        current_cell.remove_agent(self)
        new_cell.add_agent(self)

        self.pos = new_cell.coordinate

    def flee(self):

        neighbors = self.get_neighbor_cells()

        if neighbors:
            new_cell = random.choice(neighbors)
            self.move_to_cell(new_cell)

    def eat_grass(self):

        self.energy += 4
        self.hunger = max(0, self.hunger - 4)

    def reproduce(self):

        if random.random() < 0.04:

            lamb = Sheep(self.model)

            cell = self.model.grid._cells[self.pos]
            cell.add_agent(lamb)

            lamb.pos = self.pos

    def wander(self):

        neighbors = self.get_neighbor_cells()

        if neighbors:
            new_cell = random.choice(neighbors)
            self.move_to_cell(new_cell)


class Wolf(Agent):

    def __init__(self, model):
        super().__init__(model)

        self.energy = random.randint(10, 15)
        self.hunger = random.randint(0, 5)
        self.age = 0
        self.pos = None

    def step(self):

        self.age += 1
        self.energy -= 1
        self.hunger += 1

        if self.sheep_nearby():
            self.hunt()

        elif self.hunger > 7:
            self.search_prey()

        elif self.energy > 18:
            self.reproduce()

        else:
            self.wander()

    def get_neighbor_cells(self):

        cell = self.model.grid._cells[self.pos]
        return list(cell.get_neighborhood(include_center=False))

    def sheep_nearby(self):

        for cell in self.get_neighbor_cells():
            for agent in cell.agents:
                if isinstance(agent, Sheep):
                    return True

        return False

    def move_to_cell(self, new_cell):

        current_cell = self.model.grid._cells[self.pos]

        current_cell.remove_agent(self)
        new_cell.add_agent(self)

        self.pos = new_cell.coordinate

    def hunt(self):

        neighbors = self.get_neighbor_cells()

        sheep = []

        for cell in neighbors:
            for agent in cell.agents:
                if isinstance(agent, Sheep):
                    sheep.append(agent)

        if sheep:

            victim = random.choice(sheep)
            victim.remove()

            self.energy += 8
            self.hunger = max(0, self.hunger - 5)

        else:
            self.wander()

    def search_prey(self):

        neighbors = self.get_neighbor_cells()

        if neighbors:
            new_cell = random.choice(neighbors)
            self.move_to_cell(new_cell)

    def reproduce(self):

        if random.random() < 0.03:

            pup = Wolf(self.model)

            cell = self.model.grid._cells[self.pos]
            cell.add_agent(pup)

            pup.pos = self.pos

    def wander(self):

        neighbors = self.get_neighbor_cells()

        if neighbors:
            new_cell = random.choice(neighbors)
            self.move_to_cell(new_cell)