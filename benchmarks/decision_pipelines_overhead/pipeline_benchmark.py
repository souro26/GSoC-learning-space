import random


class FlatAgent:
    def __init__(self):
        self.energy = random.randint(0, 20)
        self.predator_near = random.choice([True, False])
        self.resource_near = random.choice([True, False])

        self.checks = 0
        self.actions = 0

    def step(self):
        # simulate flat decision logic (if/elif style)

        self.checks += 1
        if self.predator_near:
            self.actions += 1
            return

        self.checks += 1
        if self.energy < 5:
            self.actions += 1
            return

        self.checks += 1
        if self.resource_near:
            self.actions += 1
            return

        # default action
        self.actions += 1


class PipelineAgent:
    def __init__(self):
        self.energy = random.randint(0, 20)
        self.predator_near = random.choice([True, False])
        self.resource_near = random.choice([True, False])

        self.checks = 0
        self.actions = 0
        self.function_calls = 0

    def update_beliefs(self):
        self.function_calls += 1

        # count condition evaluations explicitly
        self.checks += 3

        return {
            "predator": self.predator_near,
            "low_energy": self.energy < 5,
            "resource": self.resource_near,
        }

    def choose_goal(self, beliefs):
        self.function_calls += 1

        if beliefs["predator"]:
            return "escape"
        if beliefs["low_energy"]:
            return "eat"
        if beliefs["resource"]:
            return "collect"
        return "wander"

    def act(self, goal):
        self.function_calls += 1
        self.actions += 1

    def step(self):
        beliefs = self.update_beliefs()
        goal = self.choose_goal(beliefs)
        self.act(goal)


def run_simulation(agent_class, steps=1000, n_agents=100):
    agents = [agent_class() for _ in range(n_agents)]

    total_checks = 0
    total_actions = 0
    total_function_calls = 0

    for _ in range(steps):
        for agent in agents:
            agent.step()

            total_actions += agent.actions
            agent.actions = 0

            if hasattr(agent, "checks"):
                total_checks += agent.checks
                agent.checks = 0

            if hasattr(agent, "function_calls"):
                total_function_calls += agent.function_calls
                agent.function_calls = 0

    return total_checks, total_actions, total_function_calls


if __name__ == "__main__":
    steps = 1000
    agents = 100

    flat_checks, flat_actions, _ = run_simulation(FlatAgent, steps, agents)
    pipe_checks, pipe_actions, pipe_calls = run_simulation(PipelineAgent, steps, agents)

    print("=== Flat Agent ===")
    print(f"Condition checks: {flat_checks}")
    print(f"Actions: {flat_actions}")

    print("\n=== Pipeline Agent ===")
    print(f"Condition checks: {pipe_checks}")
    print(f"Function calls: {pipe_calls}")
    print(f"Actions: {pipe_actions}")