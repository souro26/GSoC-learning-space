class TriggerFlow:
    def __init__(self):
        self.state = 5
        self.log = []
        self.condition_checks = 0

    def step(self, step_num, new_state):
        if new_state is not None:
            self.state = new_state
            self.condition_checks += 3

            self.log.append(f"Step {step_num}: state changed -> evaluating")

            # evaluate only on change
            _ = self.state < 3
            _ = self.state > 7
            _ = self.state % 2 == 0

        else:
            self.log.append(f"Step {step_num}: skipped (no change)")