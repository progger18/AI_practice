import numpy as np
import matplotlib.pyplot as plt

def predict(x, weights, bias):
    return x * weights + bias


def MSE(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def gradient_w(x, y_true, y_pred):
    dw = -2 * np.mean(x * (y_true - y_pred))
    return dw


def gradient_b(x, y_true, y_pred):
    db = -2 * np.mean(y_true - y_pred)
    return db


def train(x, y, learning_rate, epochs):
    loss_history = []

    w = 0.0
    b = 0.0

    for i in range(epochs):
        y_prediction = predict(x, w, b)

        loss = MSE(y, y_prediction)

        dw = gradient_w(x, y, y_prediction)
        db = gradient_b(x, y, y_prediction)

        w = w - learning_rate * dw
        b = b - learning_rate * db

        print(f"Эпоха {i + 1} -> Loss: {loss:.4f} | w: {w:.4f} | b: {b:.4f}")
        loss_history.append(loss)

    return loss_history


def main():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2.5, 5, 7.5, 10, 12.5])

    loss_history = train(x, y, learning_rate = 0.001, epochs = 300)

    plt.plot(loss_history)
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()