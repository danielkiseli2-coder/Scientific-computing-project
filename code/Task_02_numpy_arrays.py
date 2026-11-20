import numpy as np

print("=== Task 02: Original Run ===")
# 24 hourly temperature readings in degrees Celsius
temperatures_c = np.array([
    16.2, 15.8, 15.4, 15.1,
    15.6, 17.0, 19.4, 21.8,
    24.0, 25.5, 26.8, 27.6,
    28.1, 27.9, 27.2, 26.1,
    24.7, 23.2, 21.6, 20.3,
    19.1, 18.2, 17.4, 16.8
])

mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)

# Vectorized Celsius-to-Fahrenheit conversion
temperatures_f = 1.8 * temperatures_c + 32

print(f"Daily mean temperature: {mean_temp:.2f} C")
print(f"Minimum temperature: {min_temp:.2f} C")
print(f"Maximum temperature: {max_temp:.2f} C")
print("First six Fahrenheit readings:", temperatures_f[:6])

# --- Part C: Modified Parameter Run ---
print("\n=== Task 02: Part C (Modified Parameter Run) ===")
# Simulate an afternoon heatwave by adding +3.5 C to hours 12:00-15:00
temperatures_c_mod = temperatures_c.copy()
temperatures_c_mod[12:16] = temperatures_c_mod[12:16] + 3.5
temperatures_f_mod = 1.8 * temperatures_c_mod + 32

print(f"Modified daily mean temperature: {np.mean(temperatures_c_mod):.2f} C")
print(f"Modified minimum temperature:    {np.min(temperatures_c_mod):.2f} C")
print(f"Modified maximum temperature:    {np.max(temperatures_c_mod):.2f} C")
print(f"Peak Fahrenheit reading:         {np.max(temperatures_f_mod):.2f} F")
