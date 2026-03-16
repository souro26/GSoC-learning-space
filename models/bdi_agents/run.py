from model import BDIModel
from agent import BDICollector, Resource


def run_model(steps=100):
    model = BDIModel()

    for step in range(steps):
        model.step()

        collectors = len(model.agents_by_type[BDICollector])
        resources = len(model.agents_by_type[Resource])

        total_collected = sum(
            a.collected for a in model.agents_by_type[BDICollector]
        )

        print(f"Step {step:3d} | Agents: {collectors:2d} | "
              f"Resources: {resources:2d} | Collected: {total_collected:3d}")

        if resources == 0:
            print("All resources collected.")
            break


if __name__ == "__main__":
    run_model()