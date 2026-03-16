from mesa import Model
from mesa.discrete_space import OrthogonalMooreGrid
from agent import RLAgent, Resource


class RLModel(Model):

    def __init__(self, width=20, height=20, num_agents=10, num_resources=25):
        super().__init__()

        self.grid = OrthogonalMooreGrid(
            (width, height),
            torus=True,
            random=self.random
        )

        for _ in range(num_resources):
            resource = Resource(self)
            resource.cell = self.random.choice(list(self.grid.all_cells))

        for _ in range(num_agents):
            agent = RLAgent(self)
            agent.cell = self.random.choice(list(self.grid.all_cells))

    def step(self):
        self.agents_by_type[RLAgent].shuffle_do("step")