import numpy as np
import timeit

# 600,000 vehicle speed camera readings in km/h
rng = np.random.default_rng(25)
speeds_kmh = rng.uniform(35, 120, 600_000)

mu = 0.65   # Asphalt friction coefficient
g = 9.81    # Acceleration due to gravity (m/s^2)

def loop_braking():
    distances = []
    for speed in speeds_kmh:
        v_ms = speed / 3.6
        d = (v_ms ** 2) / (2 * mu * g)
        distances.append(d)
    return distances

def vectorized_braking():
    v_ms = speeds_kmh / 3.6
    return (v_ms ** 2) / (2 * mu * g)

loop_time = timeit.timeit(loop_braking, number=1)
vector_time = timeit.timeit(vectorized_braking, number=3) / 3
distances_m = vectorized_braking()

print("First five braking distances (m):", np.round(distances_m[:5], 2))
print(f"Average braking distance: {np.mean(distances_m):.2f} m")
print(f"Loop time:       {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Speed-up:        {loop_time / vector_time:.1f}x")
