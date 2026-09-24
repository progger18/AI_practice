import numpy as np

A = np.array([2, 1])
B = np.array([6, 1])
v1 = B - A

C = np.array([6, 1])
D = np.array([6, 5])
v2 = D - C

print(v1@v2)