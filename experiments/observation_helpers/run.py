from manual_scan import ManualSimulation
from helper_scan import HelperSimulation
import random


if __name__ == "__main__":
    STEPS = 20
    GRID_SIZE = 5
    NUM_AGENTS = 5
    NUM_RESOURCES = 5

    # FIXED shared environment
    random.seed(42)

    shared_resources = {
        (random.randint(0, 4), random.randint(0, 4))
        for _ in range(NUM_RESOURCES)
    }

    shared_positions = [
        (random.randint(0, 4), random.randint(0, 4))
        for _ in range(NUM_AGENTS)
    ]

    manual = ManualSimulation(shared_resources, shared_positions)
    helper = HelperSimulation(shared_resources, shared_positions)

    manual_checks = manual.run(STEPS)
    helper_checks = helper.run(STEPS)

    print("=== Observation Helpers Experiment ===\n")

    print("Manual Scan:")
    print(f"Total checks: {manual_checks}")

    print("\nHelper-based Scan:")
    print(f"Total checks: {helper_checks}")

    print("\nCheck:")
    if manual_checks == helper_checks:
        print("Same computational cost, different structure.")
    else:
        print("Mismatch detected.")