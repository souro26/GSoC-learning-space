from mesa import Model
from mesa.discrete_space import OrthogonalMooreGrid
from agent import Sheep, Wolf


class NeedsPredatorPrey(Model):
    def __init__(self, width=20, height=20, sheep_count=40, wolf_count=10):
        super().__init__()

        self.grid = OrthogonalMooreGrid(
            (width, height),
            torus=True,
            random=self.random
        )

        for _ in range(sheep_count):
            sheep = Sheep(self)
            sheep.cell = self.random.choice(list(self.grid.all_cells))

        for _ in range(wolf_count):
            wolf = Wolf(self)
            wolf.cell = self.random.choice(list(self.grid.all_cells))

    def step(self):
        self.agents.shuffle_do("step")