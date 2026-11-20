import os
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

print("=== Task 13: Original Run ===")
# Hourly temperature measurements
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([16.5, 18.8, 21.2, 23.0, 24.4, 24.9, 24.2])

linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

# Estimate every 10 minutes = 1/6 hour
ten_minute_times = np.arange(8, 14 + 1/6, 1/6)
linear_estimates = linear(ten_minute_times)
cubic_estimates = cubic(ten_minute_times)

target_time = 10.5  # 10:30
print(f"Linear estimate at 10:30: {float(linear(target_time)):.2f} C")
print(f"Cubic estimate at 10:30:  {float(cubic(target_time)):.2f} C")

os.makedirs("figures", exist_ok=True)
plt.figure()
plt.scatter(hours, temperature, label="Hourly measurements")
plt.plot(ten_minute_times, linear_estimates, label="Linear")
plt.plot(ten_minute_times, cubic_estimates, label="Cubic spline")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (C)")
plt.title("Temperature interpolation")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_13_temp_interpolation.png", dpi=150, bbox_inches="tight")
plt.show()

# --- Part C: Modified Parameter Run ---
print("\n=== Task 13: Part C (Modified Parameter Run) ===")
# Spike the 11:00 AM reading from 23.0 C to 26.8 C
temperature_mod = temperature.copy()
temperature_mod[3] = 26.8
linear_mod = interp1d(hours, temperature_mod, kind="linear")
cubic_mod = CubicSpline(hours, temperature_mod)

print(f"Modified 10:30 -> Linear: {float(linear_mod(10.5)):.2f} C, Cubic: {float(cubic_mod(10.5)):.2f} C")
print(f"Modified 11:30 -> Linear: {float(linear_mod(11.5)):.2f} C, Cubic: {float(cubic_mod(11.5)):.2f} C")
