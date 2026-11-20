import numpy as np

# Tiny angular separations (in radians) between closely spaced GPS waypoints
angles_rad = [5e-4, 2e-6, 1e-8]

for theta in angles_rad:
    direct_formula = 1.0 - np.cos(theta)
    stable_formula = 2.0 * (np.sin(theta / 2.0) ** 2)
    rel_err = abs(direct_formula - stable_formula) / stable_formula
    print(f"theta={theta:.0e}: direct={direct_formula:.16e}, stable={stable_formula:.16e}, rel_err={rel_err:.2%}")
