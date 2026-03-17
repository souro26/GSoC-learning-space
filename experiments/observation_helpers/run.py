from manual_scan import ManualSimulation
from helper_scan import HelperSimulation


if __name__ == "__main__":
    STEPS = 20

    manual = ManualSimulation()
    helper = HelperSimulation()

    manual_scans = manual.run(STEPS)
    helper_scans = helper.run(STEPS)

    print("=== Observation Helpers Experiment ===\n")

    print("Manual Scan:")
    print(f"Total scans: {manual_scans}")

    print("\nHelper-based Scan:")
    print(f"Total scans: {helper_scans}")

    print("\nCheck:")
    if manual_scans == helper_scans:
        print("Same behavior, different structure.")
    else:
        print("Mismatch detected.")