import numpy as np
from scipy.optimize import minimize

# vans = number of Cargo Vans ($45/day, 350 kg capacity)
# trucks = number of Box Trucks ($75/day, 650 kg capacity)
# Goal: Minimize daily cost while carrying at least 2,900 kg

def fleet_cost(z):
    vans, trucks = z
    return 45 * vans + 75 * trucks

def cargo_constraint(z):
    vans, trucks = z
    return 350 * vans + 650 * trucks - 2900

constraints = {"type": "ineq", "fun": cargo_constraint}
bounds = [(0, None), (0, None)]

sol = minimize(fleet_cost, x0=[4, 2], method="SLSQP", bounds=bounds, constraints=constraints)
v_opt, t_opt = sol.x

print("Optimization success:", sol.success)
print(f"Continuous Vans:   {v_opt:.3f}")
print(f"Continuous Trucks: {t_opt:.3f}")
print(f"Minimum continuous cost: ${sol.fun:.2f}")

best_fleet = None
for v in range(0, 15):
    for t in range(0, 15):
        total_cargo = 350 * v + 650 * t
        if total_cargo >= 2900:
            daily_cost = 45 * v + 75 * t
            if best_fleet is None or daily_cost < best_fleet[0]:
                best_fleet = (daily_cost, v, t, total_cargo)

print("Best whole-vehicle plan (Cost, Vans, Trucks, Capacity kg):", best_fleet)
