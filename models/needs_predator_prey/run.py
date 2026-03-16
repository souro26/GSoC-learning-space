from model import PredatorPreyModel


model = PredatorPreyModel()

for i in range(100):
    model.step()

print("Simulation finished")