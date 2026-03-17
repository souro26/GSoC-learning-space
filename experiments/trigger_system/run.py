from shared_env import generate_state_changes
from polling_flow import PollingFlow
from trigger_flow import TriggerFlow


if __name__ == "__main__":
    STEPS = 20
    CHANGE_RATE = 0.2

    changes = generate_state_changes(STEPS, CHANGE_RATE)

    polling = PollingFlow()
    trigger = TriggerFlow()

    for step, change in enumerate(changes):
        polling.step(step, change)
        trigger.step(step, change)

    print("=== Polling Flow ===")
    for line in polling.log:
        print(line)

    print("\n=== Trigger Flow ===")
    for line in trigger.log:
        print(line)