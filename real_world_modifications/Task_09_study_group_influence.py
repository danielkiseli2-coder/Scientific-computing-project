import numpy as np

# Undirected study-partner network: Alice, Brian, Carol, David
students = ["Alice", "Brian", "Carol", "David"]
study_network = np.array([
    [0., 1., 1., 1.],  # Alice studies with Brian, Carol, and David
    [1., 0., 1., 0.],  # Brian studies with Alice and Carol
    [1., 1., 0., 1.],  # Carol studies with Alice, Brian, and David
    [1., 0., 1., 0.]   # David studies with Alice and Carol
])

eigenvalues, eigenvectors = np.linalg.eig(study_network)

top_idx = np.argmax(np.real(eigenvalues))
lambda_max = np.real(eigenvalues[top_idx])
v_max = np.abs(np.real(eigenvectors[:, top_idx]))
influence_scores = v_max / v_max.sum()

print(f"Dominant eigenvalue: {lambda_max:.4f}")
print("Peer influence ranking:")
for name, score in zip(students, influence_scores):
    print(f"  {name}: {score:.4f} ({score*100:.1f}%)")

v_raw = np.real(eigenvectors[:, top_idx])
print("Verification error:", f"{np.linalg.norm(study_network @ v_raw - lambda_max * v_raw):.2e}")
