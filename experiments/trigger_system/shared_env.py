import random


def generate_state_changes(steps, change_rate):
    changes = []

    for _ in range(steps):
        if random.random() < change_rate:
            changes.append(random.randint(0, 10))
        else:
            changes.append(None)

    return changes