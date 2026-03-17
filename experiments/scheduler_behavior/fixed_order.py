class FixedOrderSimulation:
    def __init__(self, num_agents=5):
        self.resources = 1
        self.agents = [{"id": i, "collected": 0} for i in range(num_agents)]

    def step(self):
        for agent in self.agents:
            if self.resources > 0:
                agent["collected"] += 1
                self.resources -= 1

    def run(self, steps=10):
        for _ in range(steps):
            self.resources = 1  # reset each step
            self.step()

        return [a["collected"] for a in self.agents]