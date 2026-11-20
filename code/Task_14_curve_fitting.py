import os
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

print("=== Task 14: Original Run ===")
# Concurrent users and measured server response time (milliseconds)
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([75, 88, 108, 136, 174, 224, 288], dtype=float)

# A simple quadratic model for increasing delay
def model(x, a, b, c):
    return a * x**2 + b * x + c

parameters, covariance = curve_fit(model, users, response_ms)
a, b, c = parameters

predicted = model(users, a, b, c)
rmse = np.sqrt(np.mean((response_ms - predicted) ** 2))

print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 400 users: {model(400, a, b, c):.2f} ms")

os.makedirs("figures", exist_ok=True)
x_plot = np.linspace(users.min(), 400, 300)
plt.figure()
plt.scatter(users, response_ms, label="Measurements")
plt.plot(x_plot, model(x_plot, a, b, c), label="Fitted curve")
plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fitting")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_14_server_curve_fit.png", dpi=150, bbox_inches="tight")
plt.show()

# --- Part C: Modified Parameter Run ---
print("\n=== Task 14: Part C (Modified Parameter Run) ===")
# Increase high-load response times at 300 and 350 users to [250, 340] ms
response_ms_mod = np.array([75, 88, 108, 136, 174, 250, 340], dtype=float)
params_mod, _ = curve_fit(model, users, response_ms_mod)
am, bm, cm = params_mod
rmse_mod = np.sqrt(np.mean((response_ms_mod - model(users, am, bm, cm)) ** 2))

print(f"Modified model: y = {am:.6f}x^2 + {bm:.4f}x + {cm:.2f}")
print(f"Modified RMSE: {rmse_mod:.2f} ms")
print(f"Modified prediction at 400 users: {model(400, am, bm, cm):.2f} ms")
print(f"Modified prediction at 450 users: {model(450, am, bm, cm):.2f} ms")
