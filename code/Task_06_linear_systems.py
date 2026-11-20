import numpy as np

print("=== Task 06: Original Run ===")
# x = number of Type A servers
# y = number of Type B servers
#
# Type A uses 6 CPU units and 16 GB memory
# Type B uses 4 CPU units and 24 GB memory
# Total observed usage: 34 CPU units and 144 GB memory
A = np.array([
    [6.0,  4.0],
    [16.0, 24.0]
])
b = np.array([34.0, 144.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))

# --- Part C: Modified Parameter Run ---
print("\n=== Task 06: Part C (Modified Parameter Run) ===")
# Increase observed resource usage b to 44 CPU units and 184 GB memory
b_mod = np.array([44.0, 184.0])
solution_mod = np.linalg.solve(A, b_mod)
residual_mod = b_mod - A @ solution_mod

print(f"Modified Type A servers: {solution_mod[0]:.0f}")
print(f"Modified Type B servers: {solution_mod[1]:.0f}")
print("Verification A @ solution_mod:", A @ solution_mod)
print("Residual norm:", np.linalg.norm(residual_mod))
