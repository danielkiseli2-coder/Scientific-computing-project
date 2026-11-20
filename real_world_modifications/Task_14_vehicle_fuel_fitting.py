import os
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Steady vehicle speeds (km/h) and measured fuel consumption (L/100km)
speeds_kmh = np.array([40, 60, 80, 100, 120, 140], dtype=float)
fuel_usage = np.array([7.4, 6.3, 6.6, 7.6, 9.2, 11.4], dtype=float)

def fuel_model(v, a, b, c):
    return a * v**2 + b * v + c

params, _ = curve_fit(fuel_model, speeds_kmh, fuel_usage)
a, b, c = params

predicted = fuel_model(speeds_kmh, a, b, c)
rmse = np.sqrt(np.mean((fuel_usage - predicted) ** 2))

print(f"Fitted fuel model: y = {a:.6f}v^2 + {b:.4f}v + {c:.2f}")
print(f"RMSE: {rmse:.3f} L/100km")
print(f"Predicted consumption at 150 km/h: {fuel_model(150, a, b, c):.2f} L/100km")

os.makedirs("figures", exist_ok=True)
v_grid = np.linspace(40, 150, 200)
plt.figure()
plt.scatter(speeds_kmh, fuel_usage, color="darkblue", label="Road test measurements")
plt.plot(v_grid, fuel_model(v_grid, a, b, c), color="orange", label="Fitted quadratic curve")
plt.xlabel("Speed (km/h)")
plt.ylabel("Fuel Consumption (L/100km)")
plt.title("Vehicle Fuel Consumption Curve Fitting")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_14_vehicle_fuel_fit.png", dpi=150, bbox_inches="tight")
plt.show()
