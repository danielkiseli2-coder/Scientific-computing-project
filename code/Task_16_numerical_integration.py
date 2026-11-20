import numpy as np
from scipy.integrate import simpson

print("=== Task 16: Original Run ===")
# Smart-meter readings taken every two hours
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.7, 0.9, 1.3, 2.0, 1.7, 1.4, 0.8])

# Support both NumPy 2.x (trapezoid) and NumPy 1.x (trapz)
trap_fn = getattr(np, "trapezoid", getattr(np, "trapz", None))

energy_trapezoid = trap_fn(power_kw, time_hours)
energy_simpson = simpson(power_kw, x=time_hours)

print(f"Energy using trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule:   {energy_simpson:.3f} kWh")
print(f"Difference between estimates:  {abs(energy_simpson - energy_trapezoid):.3f} kWh")

# --- Part C: Modified Parameter Run ---
print("\n=== Task 16: Part C (Modified Parameter Run) ===")
# Increase afternoon power draw at hours 6, 8, and 10 to [2.8, 2.4, 1.7] kW
power_kw_mod = np.array([0.7, 0.9, 1.3, 2.8, 2.4, 1.7, 0.8])
e_trap_mod = trap_fn(power_kw_mod, time_hours)
e_simp_mod = simpson(power_kw_mod, x=time_hours)

print(f"Modified trapezoidal energy: {e_trap_mod:.3f} kWh")
print(f"Modified Simpson energy:     {e_simp_mod:.3f} kWh")
print(f"Modified difference:         {abs(e_simp_mod - e_trap_mod):.3f} kWh")
