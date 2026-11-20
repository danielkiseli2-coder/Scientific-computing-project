import os
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Bi-hourly solar panel power readings (in kW) from 6:00 AM to 6:00 PM
hours = np.array([6, 8, 10, 12, 14, 16, 18], dtype=float)
power_kw = np.array([0.0, 1.5, 4.1, 5.6, 4.9, 2.5, 0.0])

linear_model = interp1d(hours, power_kw, kind="linear")
cubic_model = CubicSpline(hours, power_kw)

half_hour_grid = np.arange(6, 18.5, 0.5)
linear_kw = linear_model(half_hour_grid)
cubic_kw = cubic_model(half_hour_grid)

print(f"11:00 AM Estimate -> Linear: {float(linear_model(11.0)):.2f} kW | Cubic: {float(cubic_model(11.0)):.2f} kW")
print(f"1:00 PM Estimate  -> Linear: {float(linear_model(13.0)):.2f} kW | Cubic: {float(cubic_model(13.0)):.2f} kW")

os.makedirs("figures", exist_ok=True)
plt.figure()
plt.scatter(hours, power_kw, color="black", label="Measured (every 2 hrs)")
plt.plot(half_hour_grid, linear_kw, linestyle="--", label="Linear interpolation")
plt.plot(half_hour_grid, cubic_kw, label="Cubic spline")
plt.xlabel("Hour of Day")
plt.ylabel("Solar Power Output (kW)")
plt.title("Solar Generation Interpolation (30-Minute Intervals)")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_13_solar_interpolation.png", dpi=150, bbox_inches="tight")
plt.show()
