from model import RLModel
from agent import RLAgent, Resource


def run_model(steps=100):
    model = RLModel()

    for step in range(steps):
        model.step()

        agents = len(model.agents_by_type[RLAgent])
        resources = len(model.agents_by_type[Resource])
        collected = sum(a.collected for a in model.agents_by_type[RLAgent])

        print(f"Step {step:3d} | Agents: {agents} | "
              f"Resources: {resources} | Collected: {collected}")

        if resources == 0:
            print("All resources collected.")
            break


if __name__ == "__main__":
    run_model()