import numpy as np

print("=== Task 05: Original Run ===")
# Four corners of a rectangle: each row is [x, y]
points = np.array([
    [0.0, 0.0],
    [2.0, 0.0],
    [2.0, 1.5],
    [0.0, 1.5]
])

angle = np.deg2rad(60)
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

scale = np.array([
    [2.5, 0.0],
    [0.0, 1.2]
])

# Combined transformation
transformation = rotation @ scale

# Row-vector form requires multiplication by transpose
transformed_points = points @ transformation.T

print("Original points:\n", points)
print("Transformation matrix:\n", transformation)
print("Transformed points:\n", transformed_points)
print("Determinant:", np.linalg.det(transformation))

# --- Part C: Modified Parameter Run ---
print("\n=== Task 05: Part C (Modified Parameter Run) ===")
# Change rotation angle to 120 degrees and horizontal x-scale to 3.5
angle_mod = np.deg2rad(120)
rotation_mod = np.array([
    [np.cos(angle_mod), -np.sin(angle_mod)],
    [np.sin(angle_mod),  np.cos(angle_mod)]
])
scale_mod = np.array([
    [3.5, 0.0],
    [0.0, 1.2]
])
transformation_mod = rotation_mod @ scale_mod
transformed_points_mod = points @ transformation_mod.T

print("Modified transformation matrix:\n", np.round(transformation_mod, 4))
print("Modified transformed points:\n", np.round(transformed_points_mod, 4))
print("Modified determinant:", round(np.linalg.det(transformation_mod), 4))
