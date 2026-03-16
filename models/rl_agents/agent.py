from mesa.discrete_space import CellAgent


class Resource(CellAgent):
    pass


class RLAgent(CellAgent):
    """
    Simple policy-based agent.
    Observe state → apply policy → act.
    """

    def __init__(self, model):
        super().__init__(model)
        self.collected = 0

    def step(self):
        state = self.observe()
        action = self.policy(state)
        self.act(action)

    def observe(self):
        for neighbor in self.cell.neighborhood:
            for agent in neighbor.agents:
                if isinstance(agent, Resource):
                    return "resource_nearby"
        return "nothing"

    def policy(self, state):
        if state == "resource_nearby":
            return "collect"
        return "move"

    def act(self, action):
        if action == "collect":
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
        self.cell = self.random.choice(list(self.cell.neighborhood))