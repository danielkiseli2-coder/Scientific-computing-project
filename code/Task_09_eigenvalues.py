import numpy as np

print("=== Task 09: Original Run ===")
# Adjacency matrix for a small undirected network.
# Node order: A, B, C, D
A = np.array([
    [0., 1., 0., 1.],
    [1., 0., 1., 1.],
    [0., 1., 0., 1.],
    [1., 1., 1., 0.]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

# Dominant eigenvalue/eigenvector
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
centrality = dominant_vector / dominant_vector.sum()

nodes = ["A", "B", "C", "D"]
print("Dominant eigenvalue:", dominant_value)
print("Eigenvector-based importance:")
for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")

# Verify Av = lambda*v
v = np.real(eigenvectors[:, index])
print("Verification error:", np.linalg.norm(A @ v - dominant_value * v))

# --- Part C: Modified Parameter Run ---
print("\n=== Task 09: Part C (Modified Parameter Run) ===")
# Add a direct link between Node A (0) and Node C (2)
A_mod = A.copy()
A_mod[0, 2] = 1.0
A_mod[2, 0] = 1.0

evals_mod, evecs_mod = np.linalg.eig(A_mod)
idx_mod = np.argmax(np.real(evals_mod))
dom_val_mod = np.real(evals_mod[idx_mod])
dom_vec_mod = np.abs(np.real(evecs_mod[:, idx_mod]))
centrality_mod = dom_vec_mod / dom_vec_mod.sum()

print("Modified dominant eigenvalue:", round(dom_val_mod, 4))
for node, score in zip(nodes, centrality_mod):
    print(f"{node}: {score:.4f}")
