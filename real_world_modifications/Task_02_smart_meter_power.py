import numpy as np

# 24 hourly household smart-meter power readings in Watts
hourly_watts = np.array([
    410, 380, 360, 345, 370, 460, 620, 790,
    910, 980, 1040, 1090, 1120, 1080, 1010, 940,
    860, 800, 750, 690, 610, 540, 480, 430
])

# Vectorized conversion from Watts to kilowatts (kW)
hourly_kw = hourly_watts / 1000.0

average_kw = np.mean(hourly_kw)
lowest_kw = np.min(hourly_kw)
peak_kw = np.max(hourly_kw)
total_kwh = np.sum(hourly_kw)

print(f"Average hourly power: {average_kw:.3f} kW")
print(f"Lowest power draw:    {lowest_kw:.3f} kW")
print(f"Peak power draw:      {peak_kw:.3f} kW")
print(f"Total daily energy:   {total_kwh:.2f} kWh")
