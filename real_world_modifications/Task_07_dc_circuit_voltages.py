import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Fixed conductance matrix G (in Siemens) for a 3-node DC microgrid
G = np.array([
    [ 6.0, -2.0,  0.0],
    [-2.0,  7.0, -3.0],
    [ 0.0, -3.0,  6.0]
])

# Three current demand scenarios (in Amps)
load_scenarios = [
    ("Morning Load",   np.array([12.0,  6.0,  9.0])),
    ("Afternoon Peak", np.array([18.0, 15.0, 12.0])),
    ("Night Low Load", np.array([ 8.0,  5.0,  6.0]))
]

# Factor G once using LU decomposition
lu, piv = lu_factor(G)

for name, current_vec in load_scenarios:
    voltages = lu_solve((lu, piv), current_vec)
    error = np.linalg.norm(current_vec - G @ voltages)
    print(f"{name}: Node Voltages = {np.round(voltages, 3)} V | Error = {error:.2e}")
