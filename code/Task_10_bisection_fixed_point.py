import os
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

print("=== Task 10: Original Run ===")
# Heat-balance model:
# f(T) = 0 means heat gain equals heat loss.
def heat_balance(T):
    return T - 22 - 12 * np.exp(-T / 25)

# Bisection: bracket a sign change
solution = root_scalar(
    heat_balance,
    bracket=[20, 40],
    method="bisect",
    xtol=1e-10
)

# Fixed-point form:
# T = 22 + 12*exp(-T/25)
def g(T):
    return 22 + 12 * np.exp(-T / 25)

T = 28.0
history = [T]
for _ in range(100):
    T_new = g(T)
    history.append(T_new)
    if abs(T_new - T) < 1e-10:
        break
    T = T_new

print(f"Bisection equilibrium temperature: {solution.root:.6f} C")
print(f"Fixed-point equilibrium temperature: {history[-1]:.6f} C")
print("Fixed-point iterations:", len(history) - 1)

os.makedirs("figures", exist_ok=True)
temps = np.linspace(20, 40, 300)
plt.figure()
plt.plot(temps, heat_balance(temps))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--")
plt.xlabel("Temperature (C)")
plt.ylabel("Heat-balance function")
plt.title("Equilibrium temperature")
plt.grid(True)
plt.savefig("figures/Task_10_equilibrium_temp.png", dpi=150, bbox_inches="tight")
plt.show()

# --- Part C: Modified Parameter Run ---
print("\n=== Task 10: Part C (Modified Parameter Run) ===")
# Increase ambient base from 22 to 28 and heating factor from 12 to 18
def heat_balance_mod(T):
    return T - 28 - 18 * np.exp(-T / 25)

def g_mod(T):
    return 28 + 18 * np.exp(-T / 25)

sol_mod = root_scalar(heat_balance_mod, bracket=[25, 45], method="bisect", xtol=1e-10)
T_mod = 32.0
hist_mod = [T_mod]
for _ in range(100):
    T_next = g_mod(T_mod)
    hist_mod.append(T_next)
    if abs(T_next - T_mod) < 1e-10:
        break
    T_mod = T_next

print(f"Modified Bisection temperature:   {sol_mod.root:.6f} C")
print(f"Modified Fixed-point temperature: {hist_mod[-1]:.6f} C ({len(hist_mod) - 1} iterations)")
