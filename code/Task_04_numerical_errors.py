import numpy as np

print("=== Task 04: Original Run ===")
# Floating-point comparison
calculated = 0.2 + 0.4
expected = 0.6
print("0.2 + 0.4 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:", np.isclose(calculated, expected))

# Absolute and relative error
true_value = np.sqrt(3)
approx_value = 1.732
absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)
print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.8%}")

# Numerically unstable vs stable formulation
for x in [1e-3, 1e-7, 1e-11]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.12f}, stable={stable:.12f}")

# --- Part C: Modified Parameter Run ---
print("\n=== Task 04: Part C (Modified Parameter Run) ===")
# Push x closer to double-precision machine epsilon (~2.22e-16)
for x in [5e-14, 2e-15, 1e-16]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.12f}, stable={stable:.12f}")
