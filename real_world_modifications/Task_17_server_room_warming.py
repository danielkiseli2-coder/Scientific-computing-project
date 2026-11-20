import os
import numpy as np
import matplotlib.pyplot as plt

# Server room warming model after AC failure: dT/dt = r * (T_max - T)
T_max = 45.0      # Equilibrium temperature without cooling (C)
T_start = 19.0    # Initial room temperature (C)
r = 0.075         # Warming rate constant (1/min)
h = 1.0           # Time step (minutes)
end_min = 40.0    # Simulation duration (minutes)

def warming_rate(T):
    return r * (T_max - T)

time = np.arange(0, end_min + h, h)
T_euler = np.zeros_like(time)
T_euler[0] = T_start

for i in range(len(time) - 1):
    T_euler[i + 1] = T_euler[i] + h * warming_rate(T_euler[i])

T_exact = T_max - (T_max - T_start) * np.exp(-r * time)

print(f"Euler room temperature at 40 min: {T_euler[-1]:.2f} C")
print(f"Exact room temperature at 40 min: {T_exact[-1]:.2f} C")
print(f"Absolute error at 40 min:         {abs(T_euler[-1] - T_exact[-1]):.4f} C")

os.makedirs("figures", exist_ok=True)
plt.figure()
plt.plot(time, T_euler, marker="o", label="Euler approximation")
plt.plot(time, T_exact, label="Exact solution")
plt.axhline(36.0, color="red", linestyle="--", label="Server warning threshold (36 C)")
plt.xlabel("Time After AC Failure (minutes)")
plt.ylabel("Room Temperature (C)")
plt.title("Server Room Warming Simulation")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_17_server_room_warming.png", dpi=150, bbox_inches="tight")
plt.show()
