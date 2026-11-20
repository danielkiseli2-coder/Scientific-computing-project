import os
import numpy as np
import matplotlib.pyplot as plt

print("=== Task 08: Original Run ===")
# Simplified steady-state temperature model for five interior grid points.
# Diagonal dominance makes Jacobi and Gauss-Seidel converge.
A = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])

# Boundary influence: left boundary = 120 C, right boundary = 30 C
b = np.array([120., 0., 0., 0., 30.])

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new

    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (
                b[i]
                - A[i, :i] @ x[:i]
                - A[i, i+1:] @ old[i+1:]
            ) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors

    return x, errors

x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

print("Jacobi temperatures:", x_j)
print("Gauss-Seidel temperatures:", x_gs)
print("Direct solution:", x_exact)

os.makedirs("figures", exist_ok=True)
plt.figure()
plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Convergence of iterative temperature solution")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_08_iterative_convergence.png", dpi=150, bbox_inches="tight")
plt.show()

# --- Part C: Modified Parameter Run ---
print("\n=== Task 08: Part C (Modified Parameter Run) ===")
# Change right boundary temperature from 30 C to 95 C and tighten tolerance to 1e-12
b_mod = np.array([120., 0., 0., 0., 95.])
xj_mod, errj_mod = jacobi(A, b_mod, tol=1e-12)
xgs_mod, errgs_mod = gauss_seidel(A, b_mod, tol=1e-12)

print("Modified temperatures:", np.round(xgs_mod, 4))
print(f"Jacobi iterations (tol=1e-12):       {len(errj_mod)}")
print(f"Gauss-Seidel iterations (tol=1e-12): {len(errgs_mod)}")
