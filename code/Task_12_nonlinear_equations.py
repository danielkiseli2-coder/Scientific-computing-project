import numpy as np
from scipy.optimize import root

print("=== Task 12: Original Run ===")
# Find intersections of:
# Circle: x^2 + y^2 = 5
# Parabola: y = x^2 - 2
def equations(z):
    x, y = z
    return [
        x**2 + y**2 - 5,
        y - (x**2 - 2)
    ]

for guess in ([1.5, 1.0], [-1.5, 1.0]):
    solution = root(equations, guess)
    print("Initial guess:", guess)
    print("Intersection:", solution.x)
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)
    print()

# --- Part C: Modified Parameter Run ---
print("=== Task 12: Part C (Modified Parameter Run) ===")
# Expand circle radius to 4 (x^2 + y^2 = 16) and shift parabola vertex to y = x^2 - 1
def equations_mod(z):
    x, y = z
    return [
        x**2 + y**2 - 16,
        y - (x**2 - 1)
    ]

for guess in ([2.0, 3.0], [-2.0, 3.0]):
    sol_mod = root(equations_mod, guess)
    print("Modified guess:", guess, "-> Intersection:", np.round(sol_mod.x, 6), "| Converged:", sol_mod.success)
