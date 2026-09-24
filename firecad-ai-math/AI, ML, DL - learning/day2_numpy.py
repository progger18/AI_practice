import numpy as np

# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# print(A)
# print(A.shape)
# print(A[0])
# print(A[1])

# a = np.array([10, 20, 30, 40, 50])

# print(a)
# print(a.shape)
# print(a[0])
# print(a[a.size - 1])

# b = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
#
# print(b.shape)
# print(b[0])
# print(b[:,1])
# print(b[2][1])
# print(b[1][1])

# c = np.array([1, 2, 3])
# d = np.array([4, 5, 6])
#
# print(c + d)
# print(c * 2)
# print(np.dot(c, d))

image = np.array([
 [0,   0,   0,   0],
 [0, 255, 255, 0],
 [0, 255, 255, 0],
 [0,   0,   0,   0]
])

print(image)
print(image.shape)
print(image[1,1])
print(image.size)
print(image.max())
print(image.mean())