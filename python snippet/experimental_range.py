# Experimental range 
import numpy as np

ranges = np.array([9.625, 9.862, 9.665, 9.695, 9.180])

mean_range = ranges.mean()
std_range = ranges.std(ddof=0)

print(f"Mean Range: {mean_range:.3f} m")
print(f"Standerd Deviation: {std_range:.3f} m")
