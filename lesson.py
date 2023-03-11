import numpy as np

# 1. We use concatenate to combine two arrays
grid = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.concatenate([grid, grid], axis=1))

# 2. Vstack
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7], [6, 5, 4]])

# - Босоо тэнхлэгт нэгтгэх
# print(np.vstack([x, grid]))

# - Хэвтээ тэнхлэгт нэгтгэх
y = np.array([99, 99])
# print(np.vstack([grid, y]))

# 3. Split, hsplit, vsplit
x = [1, 2, 3, 99, 99, 3, 2, 1]
print(x[3 : 5])
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)