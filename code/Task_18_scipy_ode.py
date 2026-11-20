import os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

print("=== Task 18: Original Run ===")
# RC charging circuit:
# dV/dt = (Vs - V) / (R * C)
Vs = 6.0      # supply voltage (V)
R = 1200.0    # resistance (ohms)
C = 0.001     # capacitance (farads)
V0 = 0.0      # initial capacitor voltage

def rc_circuit(t, V):
    return [(Vs - V[0]) / (R * C)]

t_eval = np.linspace(0, 5, 200)
solution = solve_ivp(
    rc_circuit,
    (0, 5),
    [V0],
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-11
)

# Exact RC charging curve for validation
exact = Vs * (1 - np.exp(-solution.t / (R * C)))

print("Solver success:", solution.success)
print(f"Capacitor voltage at 5 s: {solution.y[0, -1]:.4f} V")
print(f"Maximum error against exact solution: {np.max(np.abs(solution.y[0] - exact)):.3e} V")

os.makedirs("figures", exist_ok=True)
plt.figure()
plt.plot(solution.t, solution.y[0], label="solve_ivp")
plt.plot(solution.t, exact, linestyle="--", label="Exact")
plt.xlabel("Time (s)")
plt.ylabel("Capacitor voltage (V)")
plt.title("RC circuit charging")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_18_rc_charging.png", dpi=150, bbox_inches="tight")
plt.show()

# --- Part C: Modified Parameter Run ---
print("\n=== Task 18: Part C (Modified Parameter Run) ===")
# Increase supply voltage Vs to 12.0 V and resistance R to 3000.0 ohms
Vs_mod = 12.0
R_mod = 3000.0

def rc_circuit_mod(t, V):
    return [(Vs_mod - V[0]) / (R_mod * C)]

sol_mod = solve_ivp(rc_circuit_mod, (0, 5), [V0], t_eval=t_eval, rtol=1e-9, atol=1e-11)
exact_mod = Vs_mod * (1 - np.exp(-sol_mod.t / (R_mod * C)))

print(f"Modified voltage at 5 s (Vs=12V, R=3000 ohm): {sol_mod.y[0, -1]:.4f} V")
print(f"Modified max error against exact solution:    {np.max(np.abs(sol_mod.y[0] - exact_mod)):.3e} V")
