import random


def observe_neighbors(position, grid_size):
    x, y = position
    neighbors = []

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                neighbors.append((nx, ny))

    return neighbors


def count_resources(neighbors, resources):
    return sum(1 for n in neighbors if n in resources)


class HelperAgent:
    def __init__(self, grid_size=5):
        self.grid_size = grid_size
        self.position = (random.randint(0, 4), random.randint(0, 4))

    def scan_for_resource(self, resources):
        neighbors = observe_neighbors(self.position, self.grid_size)
        return neighbors


class HelperSimulation:
    def __init__(self, resources, positions):
        self.agents = [HelperAgent() for _ in positions]

        for agent, pos in zip(self.agents, positions):
            agent.position = pos

        self.resources = resources
        self.total_checks = 0

    def step(self):
        for agent in self.agents:
            neighbors = agent.scan_for_resource(self.resources)

            # count actual work (number of neighbor checks)
            self.total_checks += len(neighbors)

            # perform observation (not used, but keeps logic consistent)
            _ = count_resources(neighbors, self.resources)

    def run(self, steps=20):
        for _ in range(steps):
            self.step()

        return self.total_checks