import numpy as np
import matplotlib.pyplot as plt

# Построить графики для визуального понимания

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

x = np.array([-3, -2, -0.5, 5, 10])

print(relu(x))

x = np.array([-2, 0, 2])

print(sigmoid(x))

x = np.array([-100, 0, 100])

print(tanh(x))