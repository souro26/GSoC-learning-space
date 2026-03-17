import random


class PollingAgent:
    def __init__(self):
        self.value = random.random()
        self.checks = 0

    def step(self):
        self.checks += 1
        if self.value < 0.3:
            self.value = random.random()


class TriggerAgent:
    def __init__(self):
        self.value = random.random()
        self.checks = 0

    def update(self, change_rate):
        if random.random() < change_rate:
            self.value = random.random()
            return True
        return False

    def trigger(self):
        self.checks += 1
        if self.value < 0.3:
            self.value = random.random()


def run_experiment(change_rate, N=100, STEPS=1000):
    polling_agents = [PollingAgent() for _ in range(N)]
    trigger_agents = [TriggerAgent() for _ in range(N)]

    # polling
    for _ in range(STEPS):
        for a in polling_agents:
            a.step()

    # trigger
    for _ in range(STEPS):
        for a in trigger_agents:
            if a.update(change_rate):
                a.trigger()

    polling_checks = sum(a.checks for a in polling_agents)
    trigger_checks = sum(a.checks for a in trigger_agents)

    return polling_checks, trigger_checks


if __name__ == "__main__":
    rates = [0.05, 0.1, 0.2, 0.5, 0.8]

    print("=== Trigger vs Polling (varying change rate) ===")
    print("Agents: 100 | Steps: 1000\n")

    for rate in rates:
        polling, trigger = run_experiment(rate)

        reduction = 100 * (1 - trigger / polling)

        print(f"Rate: {int(rate*100)}%")
        print(f"Polling checks: {polling}")
        print(f"Trigger checks: {trigger}")
        print(f"Reduction: {reduction:.2f}%\n")