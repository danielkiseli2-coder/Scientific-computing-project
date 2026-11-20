import numpy as np
import timeit

print("=== Task 03: Original Run ===")
# Simulated network latency readings in milliseconds
rng = np.random.default_rng(77)
latency_ms = rng.uniform(8, 220, 800_000)

def loop_version():
    squared = []
    for value in latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)
    return squared

def vectorized_version():
    seconds = latency_ms / 1000.0
    return seconds ** 2

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3
result = vectorized_version()

print("First five squared latency values:", result[:5])
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")

# --- Part C: Modified Parameter Run ---
print("\n=== Task 03: Part C (Modified Parameter Run) ===")
# Increase dataset size to 4,000,000 samples and latency range to [12, 450] ms
rng_mod = np.random.default_rng(77)
latency_ms_mod = rng_mod.uniform(12, 450, 4_000_000)

def loop_mod():
    squared = []
    for value in latency_ms_mod:
        seconds = value / 1000.0
        squared.append(seconds ** 2)
    return squared

def vectorized_mod():
    seconds = latency_ms_mod / 1000.0
    return seconds ** 2

loop_time_mod = timeit.timeit(loop_mod, number=1)
vector_time_mod = timeit.timeit(vectorized_mod, number=3) / 3
result_mod = vectorized_mod()

print("First five modified squared values:", result_mod[:5])
print(f"Modified loop time:       {loop_time_mod:.4f} s")
print(f"Modified vectorized time: {vector_time_mod:.4f} s")
print(f"Modified speed-up:        {loop_time_mod/vector_time_mod:.1f}x")
