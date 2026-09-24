import matplotlib.pyplot as plt

def loss(w):
    return (w - 3) ** 2

def gradient(w):
    return 2 * (w - 3)

def gradient_descent(start, learning_rate, steps):
    losses = []
    weights = []
    w = 0.0

    for step in range(steps):
        grad = gradient(w)
        w = w - learning_rate * grad

        losses.append(loss(w))
        weights.append(w)

        print(
            f"step:{step}, "
            f"w:{w},"
            f"loss:{loss}"
        )

    plt.plot(losses)
    plt.xlabel("Step")
    plt.ylabel("Loss")
    plt.title("Gradient descent")
    plt.grid()
    plt.show()

    plt.plot(weights)
    plt.xlabel("Step")
    plt.ylabel("Weights")
    plt.title("Gradient descent")
    plt.grid()
    plt.show()

    return w

print(gradient_descent(0, 0.1, 100))