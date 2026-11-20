import os
import numpy as np
import matplotlib.pyplot as plt

print("=== Task 20: Original Run ===")
rng = np.random.default_rng(99)

capacity = 1200.0
mean_demand = 980.0
std_demand = 140.0
N = 100_000

# Random demand scenarios
demand = rng.normal(mean_demand, std_demand, N)
overloaded = demand > capacity
overload_probability = overloaded.mean()

print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

# Running probability to show convergence
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)
indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

os.makedirs("figures", exist_ok=True)
plt.figure()
plt.semilogx(
    indices + 1,
    running_probability[indices]
)
plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk")
plt.grid(True)
plt.savefig("figures/Task_20_server_overload_mc.png", dpi=150, bbox_inches="tight")
plt.show()

# --- Part C: Modified Parameter Run ---
print("\n=== Task 20: Part C (Modified Parameter Run) ===")
# Increase mean_demand from 980.0 to 1080.0 and std_demand from 140.0 to 175.0
rng_mod = np.random.default_rng(99)
demand_mod = rng_mod.normal(1080.0, 175.0, N)
overloaded_mod = demand_mod > capacity

print(f"Modified overload probability: {overloaded_mod.mean():.4%}")
print(f"Modified overload cases:       {overloaded_mod.sum()} out of {N}")
