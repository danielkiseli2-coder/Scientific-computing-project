import os
import numpy as np
import matplotlib.pyplot as plt

print("=== Task 15: Original Run ===")
# GPS samples: time in seconds and position in metres
time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
position = np.array([0.0, 5.4, 11.5, 18.2, 25.6, 33.8, 42.7])

speed = np.zeros_like(position)

# Forward difference at the beginning
speed[0] = (position[1] - position[0]) / (time[1] - time[0])

# Central differences for interior points
for i in range(1, len(time) - 1):
    speed[i] = (
        position[i + 1] - position[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

# Backward difference at the end
speed[-1] = (
    position[-1] - position[-2]
) / (
    time[-1] - time[-2]
)

for t, x, v in zip(time, position, speed):
    print(f"t={t:.0f}s, position={x:.1f}m, estimated speed={v:.2f} m/s")

os.makedirs("figures", exist_ok=True)
plt.figure()
plt.plot(time, speed, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated speed (m/s)")
plt.title("Speed estimated from GPS position data")
plt.grid(True)
plt.savefig("figures/Task_15_gps_speed.png", dpi=150, bbox_inches="tight")
plt.show()

# --- Part C: Modified Parameter Run ---
print("\n=== Task 15: Part C (Modified Parameter Run) ===")
# Double the sampling interval from 1 s to 2 s while keeping positions unchanged
time_mod = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
speed_mod = np.zeros_like(position)
speed_mod[0] = (position[1] - position[0]) / (time_mod[1] - time_mod[0])
for i in range(1, len(time_mod) - 1):
    speed_mod[i] = (position[i + 1] - position[i - 1]) / (time_mod[i + 1] - time_mod[i - 1])
speed_mod[-1] = (position[-1] - position[-2]) / (time_mod[-1] - time_mod[-2])

print("Modified speeds with 2s interval (m/s):", np.round(speed_mod, 2))
