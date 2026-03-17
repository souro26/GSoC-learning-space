class TriggerFlow:
    def __init__(self):
        self.state = 5
        self.log = []

    def step(self, step_num, new_state):
        if new_state is not None:
            self.state = new_state

            self.log.append(f"Step {step_num}: state changed -> evaluating")

            # evaluate only on change
            _ = self.state < 3
            _ = self.state > 7
            _ = self.state % 2 == 0

        else:
            self.log.append(f"Step {step_num}: skipped (no change)")