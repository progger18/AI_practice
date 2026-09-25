import numpy as np
import matplotlib.pyplot as plt

# Построить графики для визуального понимания

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

x = np.linspace(-10, 10, 400)

y_sigmoid = sigmoid(x)

y_relu = relu(x)

y_tanh = tanh(x)

def neuron(x, weights, bias):
    z = weights.T @ x + bias
    a = relu(z)
    return a

# Sigmoid
# plt.plot(x, y_sigmoid)
# plt.grid()
# plt.show()

# ReLU
# plt.plot(x, y_relu)
# plt.grid()
# plt.show()

# Tanh
# plt.plot(x, y_tanh)
# plt.grid()
# plt.show()