import numpy as np

# Original 4 patrol waypoints of a warehouse robot (in meters)
waypoints = np.array([
    [0.0, 0.0],
    [3.0, 0.0],
    [3.0, 2.5],
    [0.0, 2.5]
])

# Expand patrol zone by 1.8x along x and 1.6x along y
scale_matrix = np.array([
    [1.8, 0.0],
    [0.0, 1.6]
])

# Rotate patrol zone by 45 degrees counter-clockwise
theta = np.deg2rad(45)
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

combined_matrix = rotation_matrix @ scale_matrix
new_waypoints = waypoints @ combined_matrix.T

print("Original waypoints (m):\n", waypoints)
print("New waypoints (m):\n", np.round(new_waypoints, 3))
print("Patrol area multiplier (determinant):", round(np.linalg.det(combined_matrix), 2))
