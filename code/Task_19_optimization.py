import numpy as np
from scipy.optimize import minimize

print("=== Task 19: Original Run ===")
# x = number/capacity units of Type A server
# y = number/capacity units of Type B server
#
# Cost per unit: A = 14, B = 20
# Capacity per unit: A = 120, B = 200
# Required total capacity: at least 1250

def cost(z):
    x, y = z
    return 14 * x + 20 * y

def capacity_constraint(z):
    x, y = z
    return 120 * x + 200 * y - 1250

constraints = {
    "type": "ineq",
    "fun": capacity_constraint
}
bounds = [(0, None), (0, None)]

solution = minimize(
    cost,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x
print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total capacity: {120*x + 200*y:.2f}")
print(f"Minimum planning cost: {solution.fun:.2f}")

# If whole servers are required, test nearby integer combinations.
best_integer = None
for a in range(0, 20):
    for b in range(0, 20):
        capacity = 120 * a + 200 * b
        if capacity >= 1250:
            total_cost = 14 * a + 20 * b
            if best_integer is None or total_cost < best_integer[0]:
                best_integer = (total_cost, a, b, capacity)

print("Best nearby integer solution:", best_integer)

# --- Part C: Modified Parameter Run ---
print("\n=== Task 19: Part C (Modified Parameter Run) ===")
# Increase required capacity to 1600 and reduce Type B cost from 20 to 17
def cost_mod(z):
    x, y = z
    return 14 * x + 17 * y

def capacity_mod(z):
    x, y = z
    return 120 * x + 200 * y - 1600

sol_mod = minimize(
    cost_mod,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints={"type": "ineq", "fun": capacity_mod}
)
xm, ym = sol_mod.x
print(f"Modified Continuous -> Type A: {xm:.3f}, Type B: {ym:.3f}, Cost: {sol_mod.fun:.2f}")

best_int_mod = None
for a in range(0, 20):
    for b in range(0, 20):
        cap = 120 * a + 200 * b
        if cap >= 1600:
            tc = 14 * a + 17 * b
            if best_int_mod is None or tc < best_int_mod[0]:
                best_int_mod = (tc, a, b, cap)
print("Modified best integer solution:", best_int_mod)
