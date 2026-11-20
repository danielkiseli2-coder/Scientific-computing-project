import os
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Net profit balance: f(q) = 0 at monthly break-even production volume q
def profit_balance(q):
    return q - 60 - 35 * np.exp(-q / 45)

bisect_sol = root_scalar(profit_balance, bracket=[50, 90], method="bisect", xtol=1e-8)

def next_q(q):
    return 60 + 35 * np.exp(-q / 45)

q = 70.0
steps = 0
for _ in range(100):
    q_new = next_q(q)
    steps += 1
    if abs(q_new - q) < 1e-8:
        q = q_new
        break
    q = q_new

print(f"Bisection break-even volume:   {bisect_sol.root:.4f} units")
print(f"Fixed-point break-even volume: {q:.4f} units (in {steps} iterations)")

os.makedirs("figures", exist_ok=True)
units = np.linspace(50, 90, 200)
plt.figure()
plt.plot(units, profit_balance(units), label="Net profit balance f(q)")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(bisect_sol.root, color="red", linestyle="--", label=f"Break-even = {bisect_sol.root:.2f}")
plt.xlabel("Monthly Units Produced (q)")
plt.ylabel("Net Profit Balance")
plt.title("Workshop Break-Even Analysis")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_10_breakeven_volume.png", dpi=150, bbox_inches="tight")
plt.show()
