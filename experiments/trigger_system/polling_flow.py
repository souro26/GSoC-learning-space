class PollingFlow:
    def __init__(self):
        self.state = 5
        self.log = []

    def step(self, step_num, new_state):
        if new_state is not None:
            self.state = new_state

        # always evaluate
        self.log.append(f"Step {step_num}: evaluated conditions")

        # simulate 3 rules
        _ = self.state < 3
        _ = self.state > 7
        _ = self.state % 2 == 0