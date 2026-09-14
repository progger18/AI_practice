def f(x):
    return x ** 2

x = 3
h = 0.001

derivative = (f(x + h) - f(x)) / h

print(derivative)

analytical = 2 * x

print(analytical)