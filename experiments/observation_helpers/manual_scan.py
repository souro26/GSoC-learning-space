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

    def scan_for_resource(self, resources):
        count = 0

        for neighbor in self.get_neighbors():
            if neighbor in resources:
                count += 1

        return count


class ManualSimulation:
    def __init__(self, num_agents=5):
        self.agents = [ManualScanAgent() for _ in range(num_agents)]
        self.resources = {(random.randint(0, 4), random.randint(0, 4)) for _ in range(5)}
        self.total_scans = 0

    def step(self):
        for agent in self.agents:
            found = agent.scan_for_resource(self.resources)
            self.total_scans += 1

    def run(self, steps=20):
        for _ in range(steps):
            self.step()

        return self.total_scans