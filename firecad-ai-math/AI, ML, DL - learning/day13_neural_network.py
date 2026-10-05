import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [0.0, 1.0],
    [1.0, 1.0],
    [2.0, 1.0],
    [1.0, 2.0],
    [2.0, 2.0],
])

y = np.array([
    [1.0],
    [3.0],
    [4.0],
    [6.0],
    [8.0],
    [9.0],
    [11.0],
])

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return (x > 0).astype(float)

def initialize_parameters(input_size, hidden_size, output_size, seed=42):
    rng = np.random.default_rng(seed)

    W1 = rng.normal(
        loc=0.0,
        scale=0.1,
        size=(hidden_size, input_size)
    )

    b1 = np.zeros((1, hidden_size))

    W2 = rng.normal(
        loc=0.0,
        scale=0.1,
        size=(output_size, hidden_size)
    )

    b2 = np.zeros((1, output_size))

    return W1, b1, W2, b2

def forward(X, W1, b1, W2, b2):
    Z1 = X @ W1.T + b1

    A1 = relu(Z1)

    Z2 = A1 @ W2.T + b2

    y_pred = Z2

    return Z1, A1, Z2, y_pred

def mse_loss(y_true, y_pred):
    n = y_true.shape[0]

    return np.sum(
        (y_pred - y_true) ** 2
    ) / (2 * n)

def backward(X, y, Z1, A1, y_pred, W2):
    n = X.shape[0]

    dZ2 = (y_pred - y) / n

    dW2 = dZ2.T @ A1

    db2 = np.sum(
        dZ2,
        axis=0,
        keepdims=True
    )

    dA1 = dZ2 @ W2

    dZ1 = dA1 * relu_derivative(Z1)

    dW1 = dZ1.T @ X

    db1 = np.sum(
        dZ1,
        axis=0,
        keepdims=True
    )

    return dW1, db1, dW2, db2

def train(X, y, hidden_size=4, learning_rate=0.05, epochs=2000):
    input_size = X.shape[1]
    output_size = y.shape[1]

    W1, b1, W2, b2 = initialize_parameters(
        input_size=input_size,
        hidden_size=hidden_size,
        output_size=output_size
    )

    loss_history = []

    for epoch in range(epochs):
        Z1, A1, Z2, y_pred = forward(
            X,
            W1,
            b1,
            W2,
            b2
        )

        loss = mse_loss(
            y,
            y_pred
        )

        loss_history.append(loss)

        dW1, db1, dW2, db2 = backward(
            X,
            y,
            Z1,
            A1,
            y_pred,
            W2
        )

        W1 -= learning_rate * dW1
        b1 -= learning_rate * db1

        W2 -= learning_rate * dW2
        b2 -= learning_rate * db2

        if epoch % 100 == 0:
            print(
                f"Epoch {epoch:4d} | "
                f"Loss = {loss:.8f}"
            )

    return W1, b1, W2, b2, loss_history

W1, b1, W2, b2, loss_history = train(
    X,
    y,
    hidden_size=4,
    learning_rate=0.05,
    epochs=2000
)

Z1, A1, Z2, predictions = forward(
    X,
    W1,
    b1,
    W2,
    b2
)

print("\n" + "=" * 60)
print("FINAL PARAMETERS")
print("=" * 60)

print("\nW1:")
print(W1)

print("\nb1:")
print(b1)

print("\nW2:")
print(W2)

print("\nb2:")
print(b2)


print("\n" + "=" * 60)
print("SHAPES")
print("=" * 60)

print("X.shape         =", X.shape)
print("W1.shape        =", W1.shape)
print("b1.shape        =", b1.shape)
print("Z1.shape        =", Z1.shape)
print("A1.shape        =", A1.shape)
print("W2.shape        =", W2.shape)
print("b2.shape        =", b2.shape)
print("predictions.shape =", predictions.shape)

print("\n" + "=" * 60)
print("PREDICTIONS")
print("=" * 60)

for i in range(len(X)):
    print(
        f"X = {X[i]} | "
        f"Real = {y[i, 0]:.4f} | "
        f"Predicted = {predictions[i, 0]:.4f}"
    )

final_loss = mse_loss(
    y,
    predictions
)

print("\n" + "=" * 60)
print("FINAL LOSS")
print("=" * 60)

print(f"Final loss = {final_loss:.8f}")

plt.figure(figsize=(8, 5))

plt.plot(
    loss_history
)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss")

plt.grid(True)
plt.show()