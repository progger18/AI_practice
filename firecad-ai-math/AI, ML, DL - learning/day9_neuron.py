import numpy as np

# def neuron(x, weights, bias):
#     return np.dot(x, weights) + bias
#
# def identity(x):
#     return x
#
# z = neuron([1,3], [2, 6], 10)
# a = identity(z)

# x = np.array([1, 2, 3])

# W = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
# ])

x = np.array([1, 2, 3])

W = np.array([3, 4, 5])

# b = np.array([1, 2])

b = 5

# print(x)
# print(W.T)
# print(b)

# print(np.dot(x, W.T))

# print(np.dot(x, W.T) + b)

print(W @ x + b)