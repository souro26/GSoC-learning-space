import random


class PollingAgent:
    def __init__(self):
        self.energy = random.randint(1, 10)
        self.checks = 0

    def step(self):
        self.energy -= 1
        self.checks += 1

        if self.energy <= 0:
            self.energy = random.randint(1, 10)


class TriggerAgent:
    def __init__(self):
        self.energy = random.randint(1, 10)
        self.checks = 0

    def update(self, change_rate):
        # energy always changes, ignore rate
        self.energy -= 1
        return True

    def trigger(self):
        self.checks += 1
        if self.energy <= 0:
            self.energy = random.randint(1, 10)


def run_experiment(N=100, STEPS=1000):
    polling_agents = [PollingAgent() for _ in range(N)]
    trigger_agents = [TriggerAgent() for _ in range(N)]

    for _ in range(STEPS):
        for a in polling_agents:
            a.step()

    for _ in range(STEPS):
        for a in trigger_agents:
            if a.update(1.0):
                a.trigger()

    polling_checks = sum(a.checks for a in polling_agents)
    trigger_checks = sum(a.checks for a in trigger_agents)

    return polling_checks, trigger_checks


if __name__ == "__main__":
    polling, trigger = run_experiment()

    print("=== Wolf-Sheep-like (always changing) ===")
    print(f"Polling checks: {polling}")
    print(f"Trigger checks: {trigger}")