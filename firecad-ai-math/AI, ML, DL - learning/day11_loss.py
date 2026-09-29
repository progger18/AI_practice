import numpy as np

eps = 1e-15

def mse(y_true, y_pred):
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return np.mean((y_true - y_pred) ** 2)

def mae(y_true, y_pred):
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return np.mean(np.abs(y_true - y_pred))

def bce(y_true, y_pred):
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return - np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def cross_entropy(y_true, y_pred):
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return -np.log(y_pred)

y_true = np.array([2, 4, 6])
y_pred = np.array([1, 5, 7])

# print(mse(y_true, y_pred))
# print(mae(y_true, y_pred))

y_true = np.array([1, 1, 0, 0])
y_pred = np.array([0.9, 0.8, 0.1, 0.2])
print(bce(y_true, y_pred))

y_pred = np.array([0.6, 0.6, 0.4, 0.4])
print(bce(y_true, y_pred))