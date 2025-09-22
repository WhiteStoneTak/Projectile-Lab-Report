# Crank 3
import numpy as np

vi = 15.96
vi_low, vi_high = 14.51, 17.41
d_low, d_high = -0.98, -1.02
a = -9.8

def range_calc(v, d):
    t = np.sqrt(2 * abs(d) / abs(a))
    return v * t

R0 = range_calc(vi, -1)
Rmin = range_calc(vi_low, d_low)
Rmax = range_calc(vi_high, d_high)

uncertainty = max(abs(R0 - Rmin), abs(R0 - Rmax))
print(f"R0: {R0:.2f} m, Rmin: {Rmin:.2f} m, Rmax: {Rmax:.2f} m")
print(f"Crank-3 Report: {R0:.2f} ± {uncertainty:.2f} m")
