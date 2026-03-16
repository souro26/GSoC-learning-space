from mesa.discrete_space import CellAgent


class Resource(CellAgent):
    """Passive resource that can be collected by agents."""
    pass


class BDICollector(CellAgent):
    """
    Simple BDI-style agent.
    beliefs   -> nearby resources
    desire    -> collect resource
    intention -> move or collect
    """

    def __init__(self, model):
        super().__init__(model)
        self.beliefs = []
        self.goal = None
        self.intention = None
        self.collected = 0

    def step(self):
        self.update_beliefs()
        self.choose_goal()
        self.form_intention()
        self.act()

    def update_beliefs(self):
        self.beliefs = []
        for neighbor in self.cell.neighborhood:
            for agent in neighbor.agents:
                if isinstance(agent, Resource):
                    self.beliefs.append(agent)

    def choose_goal(self):
        if self.beliefs:
            self.goal = "collect"
        else:
            self.goal = "explore"

    def form_intention(self):
        if self.goal == "collect":
            self.intention = "collect_resource"
        else:
            self.intention = "move"

    def act(self):
        if self.intention == "collect_resource":
            self.collect_resource()
        else:
            self.random_move()

    def collect_resource(self):
        for neighbor in self.cell.neighborhood:
            for agent in list(neighbor.agents):
                if isinstance(agent, Resource):
                    agent.remove()
                    self.collected += 1
                    return
        self.random_move()

    def random_move(self):
        new_cell = self.random.choice(list(self.cell.neighborhood))
        self.cell = new_cell