import matplotlib.pyplot as plt

weights = []
losses = []

def loss(w):
    return (w - 3) ** 2

def gradient(w):
    return 2 * (w - 3)

w = 0.0
learning_rate = 2

for step in range(100):
    grad = gradient(w)
    w = w - learning_rate * grad

    weights.append(w)
    losses.append(loss(w))

    print(
        f"step={step}, "
        f"w={w}, "
        f"loss={loss(w)}"
    )

# На графике видно, что с каждым шагом значение loss стремится к нулю.
plt.plot(losses)
plt.xlabel("Step")
plt.ylabel("Loss")
plt.title("Gradient Descent")
plt.grid()
plt.show()