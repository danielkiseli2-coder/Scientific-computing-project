import os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Bloodstream drug concentration model: dC/dt = D - k_el * C
D = 24.0       # IV infusion rate (mg/hr)
k_el = 0.30    # Elimination rate constant (1/hr)
C0 = 0.0       # Initial drug concentration (mg/L)

def drug_kinetics(t, C):
    return [D - k_el * C[0]]

t_hours = np.linspace(0, 12, 121)
sol = solve_ivp(
    drug_kinetics,
    (0, 12),
    [C0],
    t_eval=t_hours,
    rtol=1e-9,
    atol=1e-11
)

exact_conc = (D / k_el) * (1 - np.exp(-k_el * sol.t))

print("Solver success:", sol.success)
print(f"Drug concentration at 12 hrs: {sol.y[0, -1]:.4f} mg/L")
print(f"Maximum error vs exact model: {np.max(np.abs(sol.y[0] - exact_conc)):.3e} mg/L")

os.makedirs("figures", exist_ok=True)
plt.figure()
plt.plot(sol.t, sol.y[0], label="solve_ivp concentration")
plt.plot(sol.t, exact_conc, linestyle="--", label="Exact analytical curve")
plt.xlabel("Time (hours)")
plt.ylabel("Blood Concentration (mg/L)")
plt.title("IV Drug Concentration Over 12 Hours")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_18_iv_drug_concentration.png", dpi=150, bbox_inches="tight")
plt.show()
