from flat_agent import FlatAgent
from modular_agent import ModularAgent


def run_simulation(agent_class, steps=50, n_agents=5):
    agents = [agent_class() for _ in range(n_agents)]

    for _ in range(steps):
        for agent in agents:
            agent.step()

    total_actions = sum(len(a.actions_taken) for a in agents)

    return total_actions, agents


if __name__ == "__main__":
    flat_actions, flat_agents = run_simulation(FlatAgent)
    modular_actions, modular_agents = run_simulation(ModularAgent)

    print("=== Behavior Modularity Experiment ===\n")

    print("Flat Agent:")
    print(f"Total actions: {flat_actions}")

    print("\nModular Agent:")
    print(f"Total actions: {modular_actions}")

    print("\nCheck consistency:")
    print(f"Flat example actions: {flat_agents[0].actions_taken[:10]}")
    print(f"Modular example actions: {modular_agents[0].actions_taken[:10]}")