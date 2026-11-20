import numpy as np

# x = number of Standard Solar Units (4 kW power, 12 kWh storage)
# y = number of Heavy Solar Units    (6 kW power, 25 kWh storage)
# Target: 30 kW total power and 107 kWh total storage

A = np.array([
    [4.0,  6.0],
    [12.0, 25.0]
])
b = np.array([30.0, 107.0])

units = np.linalg.solve(A, b)
residual = b - A @ units

print(f"Standard Solar Units needed: {units[0]:.0f}")
print(f"Heavy Solar Units needed:    {units[1]:.0f}")
print("Total achieved [kW, kWh]:   ", A @ units)
print("Residual norm:              ", np.linalg.norm(residual))
