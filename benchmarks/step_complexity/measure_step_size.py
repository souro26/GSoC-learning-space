import random


class Agent:
    def __init__(self, n_rules, mode="early_exit"):
        self.n_rules = n_rules
        self.mode = mode
        self.checks = 0

    def step(self):
        """
        Simulate rule evaluation inside step().

        Modes:
        - early_exit: break when first condition is true
        - full_scan: evaluate all rules every step
        """

        if self.mode == "early_exit":
            for _ in range(self.n_rules):
                self.checks += 1
                if random.random() < 0.3:  # 30% chance to trigger
                    break

        elif self.mode == "full_scan":
            for _ in range(self.n_rules):
                self.checks += 1
                _ = random.random() < 0.3  # evaluate but never break


def run_simulation(n_rules, steps=1000, n_agents=100, mode="early_exit"):
    agents = [Agent(n_rules, mode) for _ in range(n_agents)]

    total_checks = 0

    for _ in range(steps):
        for agent in agents:
            agent.step()
            total_checks += agent.checks
            agent.checks = 0

    return total_checks


def main():
    steps = 1000
    agents = 100
    rule_counts = [1, 3, 5, 10, 20]

    print("=== Step Complexity Benchmark ===")
    print(f"Agents: {agents}, Steps: {steps}\n")

    print("---- Early Exit Mode (realistic if/elif behavior) ----")
    for rules in rule_counts:
        checks = run_simulation(rules, steps, agents, mode="early_exit")
        print(f"Rules: {rules:2d} | Total checks: {checks}")

    print("\n---- Full Scan Mode (worst case) ----")
    for rules in rule_counts:
        checks = run_simulation(rules, steps, agents, mode="full_scan")
        print(f"Rules: {rules:2d} | Total checks: {checks}")


if __name__ == "__main__":
    main()