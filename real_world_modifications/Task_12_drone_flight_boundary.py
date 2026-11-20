import numpy as np
from scipy.optimize import root

# Drone radio range circle (radius = 6 km): x^2 + y^2 = 36
# Parabolic flight corridor: y = 0.4 * x^2 - 2.5
def flight_boundary(coords):
    x, y = coords
    return [
        x**2 + y**2 - 36,
        y - (0.4 * x**2 - 2.5)
    ]

for start_guess in ([3.0, 4.0], [-3.0, 4.0]):
    res = root(flight_boundary, start_guess)
    print("Initial guess (km):", start_guess)
    print("Boundary exit (km):", np.round(res.x, 4))
    print("Residuals:         ", np.round(flight_boundary(res.x), 10))
    print("Converged:         ", res.success)
    print()
