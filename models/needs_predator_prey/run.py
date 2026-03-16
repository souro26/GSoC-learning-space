from model import NeedsPredatorPrey
from agent import Sheep, Wolf


def run_model(steps=100):
    model = NeedsPredatorPrey()

    for step in range(steps):
        model.step()

        sheep = len(model.agents.select(agent_type=Sheep))
        wolves = len(model.agents.select(agent_type=Wolf))

        print(f"Step {step:3d} | Sheep: {sheep:3d} | Wolves: {wolves:3d}")

        if sheep == 0 or wolves == 0:
            print("Population collapsed.")
            break


if __name__ == "__main__":
    run_model()