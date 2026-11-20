import os
import numpy as np
import matplotlib.pyplot as plt

# 4x4 system for 4 interior pipeline pressure junctions
A_pipe = np.array([
    [ 2., -1.,  0.,  0.],
    [-1.,  2., -1.,  0.],
    [ 0., -1.,  2., -1.],
    [ 0.,  0., -1.,  2.]
])

# Left pump station = 75 psi, Right elevated storage tank = 25 psi
b_pipe = np.array([75., 0., 0., 25.])

def solve_jacobi(A, b, tol=1e-6, max_iter=300):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        err = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(err)
        if err < tol:
            return x_new, errors
        x = x_new
    return x, errors

def solve_gauss_seidel(A, b, tol=1e-6, max_iter=300):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        err = np.linalg.norm(x - old, ord=np.inf)
        errors.append(err)
        if err < tol:
            return x, errors
    return x, errors

p_jacobi, err_j = solve_jacobi(A_pipe, b_pipe)
p_gs, err_gs = solve_gauss_seidel(A_pipe, b_pipe)

print("Jacobi pressures (psi):      ", np.round(p_jacobi, 2), f"({len(err_j)} iterations)")
print("Gauss-Seidel pressures (psi):", np.round(p_gs, 2), f"({len(err_gs)} iterations)")

os.makedirs("figures", exist_ok=True)
plt.figure()
plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Max Pressure Change (psi)")
plt.title("Pipeline Pressure Iterative Convergence")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_08_pipeline_pressure.png", dpi=150, bbox_inches="tight")
plt.show()
