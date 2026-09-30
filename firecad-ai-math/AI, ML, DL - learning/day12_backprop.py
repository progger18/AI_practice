def forward(x, w, b):
    z = w * x + b
    a = max(0, z)
    return z, a

def relu_derivative(z):
    if z > 0: return 1
    else: return 0

def backward(x, y, z, a):
    dL_da = a - y
    da_dz = relu_derivative(z)

    dL_dz = dL_da * da_dz

    dL_dw = dL_dz * x
    dL_db = dL_dz

    return dL_dw, dL_db

