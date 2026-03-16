from mesa.model import Model
from mesa.discrete_space import OrthogonalMooreGrid
from agent import Sheep, Wolf
import random


class PredatorPreyModel(Model):

    def __init__(
        self,
        width=20,
        height=20,
        initial_sheep=50,
        initial_wolves=20
    ):
        super().__init__()

        self.grid = OrthogonalMooreGrid(
            (width, height),
            random=self.random
        )

        # create sheep
        for _ in range(initial_sheep):

            sheep = Sheep(self)

            x = random.randrange(width)
            y = random.randrange(height)

            cell = self.grid._cells[(x, y)]
            cell.add_agent(sheep)
            sheep.pos = (x, y)

        # create wolves
        for _ in range(initial_wolves):

            wolf = Wolf(self)

            x = random.randrange(width)
            y = random.randrange(height)

            cell = self.grid._cells[(x, y)]
            cell.add_agent(wolf)
            wolf.pos = (x, y)

    def step(self):

        for agent in self.agents.copy():
            agent.step()