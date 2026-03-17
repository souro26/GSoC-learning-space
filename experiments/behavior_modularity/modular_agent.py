class EscapeBehavior:
    def check(self, agent):
        return agent.energy < 3

    def act(self, agent):
        agent.actions_taken.append("flee")


class ForageBehavior:
    def check(self, agent):
        return agent.energy < 6

    def act(self, agent):
        agent.actions_taken.append("eat")
        agent.energy += 2


class ReproduceBehavior:
    def check(self, agent):
        return agent.energy > 12

    def act(self, agent):
        agent.actions_taken.append("reproduce")
        agent.energy -= 5


class WanderBehavior:
    def check(self, agent):
        return True  # fallback

    def act(self, agent):
        agent.actions_taken.append("wander")
        agent.energy -= 1


class ModularAgent:
    def __init__(self):
        self.energy = 10
        self.alive = True
        self.actions_taken = []

        self.behaviors = [
            EscapeBehavior(),
            ForageBehavior(),
            ReproduceBehavior(),
            WanderBehavior()
        ]

    def step(self):
        if not self.alive:
            return

        # iterate behaviors
        for behavior in self.behaviors:
            if behavior.check(self):
                behavior.act(self)
                break