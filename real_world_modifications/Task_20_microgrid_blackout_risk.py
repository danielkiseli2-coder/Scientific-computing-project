import os
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(108)

battery_capacity_kwh = 60.0   # Available evening battery storage (kWh)
mean_evening_use = 49.5       # Average evening village demand (kWh)
std_evening_use = 7.2         # Demand standard deviation (kWh)
N = 100_000                   # Number of simulated evenings

evening_demand = rng.normal(mean_evening_use, std_evening_use, N)

blackout = evening_demand > battery_capacity_kwh
blackout_prob = blackout.mean()

print(f"Estimated blackout probability: {blackout_prob:.4%}")
print(f"Number of blackout evenings:    {blackout.sum()} out of {N}")

running_prob = np.cumsum(blackout) / np.arange(1, N + 1)
sample_points = np.unique(np.logspace(1, np.log10(N), 200).astype(int)) - 1

os.makedirs("figures", exist_ok=True)
plt.figure()
plt.semilogx(sample_points + 1, running_prob[sample_points], color="darkred")
plt.xlabel("Number of Simulated Evenings")
plt.ylabel("Estimated Blackout Probability")
plt.title("Monte Carlo Estimate of Microgrid Blackout Risk")
plt.grid(True)
plt.savefig("figures/Task_20_microgrid_blackout_mc.png", dpi=150, bbox_inches="tight")
plt.show()
