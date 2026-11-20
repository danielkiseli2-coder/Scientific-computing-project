import os
import numpy as np
import matplotlib.pyplot as plt

# Ultrasonic sensor timestamps (minutes) and cumulative tank volume (Liters)
minutes = np.array([0, 5, 10, 15, 20, 25], dtype=float)
volume_liters = np.array([120.0, 195.0, 285.0, 380.0, 465.0, 530.0])

flow_rate = np.zeros_like(volume_liters)

# Forward difference at t = 0 min
flow_rate[0] = (volume_liters[1] - volume_liters[0]) / (minutes[1] - minutes[0])

# Central differences for interior timestamps
for i in range(1, len(minutes) - 1):
    flow_rate[i] = (
        volume_liters[i + 1] - volume_liters[i - 1]
    ) / (
        minutes[i + 1] - minutes[i - 1]
    )

# Backward difference at t = 25 min
flow_rate[-1] = (
    volume_liters[-1] - volume_liters[-2]
) / (
    minutes[-1] - minutes[-2]
)

for t, vol, rate in zip(minutes, volume_liters, flow_rate):
    print(f"t={t:2.0f} min | Volume={vol:5.1f} L | Inflow Rate={rate:5.2f} L/min")

os.makedirs("figures", exist_ok=True)
plt.figure()
plt.plot(minutes, flow_rate, marker="s", color="teal")
plt.xlabel("Time (minutes)")
plt.ylabel("Estimated Inflow Rate (Liters/min)")
plt.title("Water Tank Inflow Rate via Numerical Differentiation")
plt.grid(True)
plt.savefig("figures/Task_15_water_tank_inflow.png", dpi=150, bbox_inches="tight")
plt.show()
