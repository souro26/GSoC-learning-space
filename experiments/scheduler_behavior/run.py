from random_order import RandomOrderSimulation
from fixed_order import FixedOrderSimulation


if __name__ == "__main__":
    STEPS = 20

    random_sim = RandomOrderSimulation()
    fixed_sim = FixedOrderSimulation()

    random_result = random_sim.run(STEPS)
    fixed_result = fixed_sim.run(STEPS)

    print("=== Scheduler Behavior Experiment ===\n")

    print("Random Order Results:")
    print(random_result)

    print("\nFixed Order Results:")
    print(fixed_result)