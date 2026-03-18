import random


class ManualScanAgent:
    def __init__(self, grid_size=5):
        self.grid_size = grid_size
        self.position = (random.randint(0, 4), random.randint(0, 4))

    def get_neighbors(self):
        x, y = self.position
        neighbors = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                    neighbors.append((nx, ny))

        return neighbors


class ManualSimulation:
    def __init__(self, resources, positions):
        self.agents = [ManualScanAgent() for _ in positions]

        for agent, pos in zip(self.agents, positions):
            agent.position = pos

        self.resources = resources
        self.total_checks = 0

    def step(self):
        for agent in self.agents:
            neighbors = agent.get_neighbors()

            # count actual work (number of neighbor checks)
            self.total_checks += len(neighbors)

            # perform observation manually
            for neighbor in neighbors:
                _ = neighbor in self.resources

    def run(self, steps=20):
        for _ in range(steps):
            self.step()

        return self.total_checks