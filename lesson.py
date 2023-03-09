import numpy as np

# We use concatenate to combine two arrays
grid = np.array([[1, 2, 3], [4, 5, 6]])
print(np.concatenate([grid, grid], axis=1))