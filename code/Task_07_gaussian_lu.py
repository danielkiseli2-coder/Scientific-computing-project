import numpy as np
from scipy.linalg import lu_factor, lu_solve

print("=== Task 07: Original Run ===")
# The same coefficient matrix is reused for several measurement vectors.
A = np.array([
    [ 5.0, -1.0,  0.0],
    [-1.0,  5.0, -1.0],
    [ 0.0, -1.0,  4.0]
])

measurement_sets = [
    np.array([18.0, 12.0, 14.0]),
    np.array([20.0, 14.0, 11.0]),
    np.array([17.0, 15.0, 13.0])
]

# Factor A only once
lu, piv = lu_factor(A)

for i, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu, piv), b)
    residual = b - A @ x
    print(f"Measurement set {i}")
    print("Solution:", x)
    print("Residual norm:", np.linalg.norm(residual))
    print()

# Direct solution for comparison
print("Direct solution for first set:", np.linalg.solve(A, measurement_sets[0]))

# --- Part C: Modified Parameter Run ---
print("\n=== Task 07: Part C (Modified Parameter Run) ===")
# Increase A[0, 0] from 5.0 to 7.0 and add a 4th measurement vector
A_mod = A.copy()
A_mod[0, 0] = 7.0
measurement_sets_mod = measurement_sets + [np.array([24.0, 18.0, 15.0])]

lu_mod, piv_mod = lu_factor(A_mod)
for i, b in enumerate(measurement_sets_mod, start=1):
    x_mod = lu_solve((lu_mod, piv_mod), b)
    print(f"Modified Set {i} Solution: {np.round(x_mod, 4)}")
