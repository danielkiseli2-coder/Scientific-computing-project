import numpy as np
from scipy.integrate import simpson

# Speedometer readings (km/h) recorded every 0.5 hours during a 3-hour delivery trip
trip_hours = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
speed_kmh = np.array([0.0, 50.0, 75.0, 85.0, 72.0, 55.0, 0.0])

trap_fn = getattr(np, "trapezoid", getattr(np, "trapz", None))
distance_trap = trap_fn(speed_kmh, trip_hours)
distance_simp = simpson(speed_kmh, x=trip_hours)

print(f"Estimated distance (Trapezoidal rule): {distance_trap:.2f} km")
print(f"Estimated distance (Simpson's rule):   {distance_simp:.2f} km")
print(f"Difference between methods:            {abs(distance_simp - distance_trap):.2f} km")
