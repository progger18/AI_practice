import numpy as np

def main():
    rng = np.random.default_rng(42)

    W1 = rng.normal(0, 0.1, size=(4, 2))
    b1 = np.zeros((1, 4))

    W2 = rng.normal(0, 0.1, size=(1, 4))
    b2 = np.zeros((1, 1))

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return (x > 0).astype(float)

def forward(X, W1, b1, W2, b2):
    z1 = X @ W1.T + b1
    a1 = relu(z1)

    z2 = a1 @ W2.T + b2
    y_pred = z2

    return z1, a1, z2, y_pred

def mse_loss(y_true, y_pred):
    n = y_true.shape[0]
    return np.sum((y_pred - y_true) ** 2) / (2 * n)

def backward(X, y, z1, a1, y_pred, W2):
    n = X.shape[0]

    dz2 = (y_pred - y) / n
    dW2 = dz2.T @ a1
    db2 = np.sum(dz2, axis=0, keepdims=True)
    da1 = dz2 @ W2
    dz1 = da1 * relu_derivative(z1)
    dW1 = dz1.T @ X
    db1 = np.sum(dz1, axis=0, keepdims=True)

    return dW1, db1, dW2, db2

def train(X, y, epochs, learning_rate):
    return 0

if __name__ == '__main__':
    main()