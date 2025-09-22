# Range tilt
import numpy as np

theta_deg = 5
theta = np.deg2rad(theta_deg)
N = 9
extra = 0.61

R_true = np.sum([np.cos(i * theta) for i in range(1, N+1)]) + extra * np.cos((N+1) * theta)
R_meas = 9.61

percent_delta = (R_meas - R_true) / R_true * 100
print(f"ΔR_tilt: {percent_delta:.2f}%")
