import numpy as np
rg = np.random.default_rng()
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values, indices_list, returns_count = np.unique(a, return_index=True, return_counts=True)
print(returns_count)
