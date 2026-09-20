import numpy as np

def predict(x, weights, bias):
    return x * weights + bias

def MSE(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def gradients(x, y_true, y_pred):
    dw = -2 * np.mean(x * (y_true - y_pred))
    db = -2 * np.mean(y_true - y_pred)

def update(weight, bias):
    w = weight -

def train(x, y, learning_rate, epochs):
    for i in range(5):
        x = 0
        w = 0
        b = 0

        y_prediction = predict(x, w, b)

        loss = MSE(2*x - 1, y_prediction)

