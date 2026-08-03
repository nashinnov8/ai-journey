import numpy as np


def grad(x):
    return 2 * x + 5 * np.cos(x)


def cost(x):
    return x**2 + 5 * np.sin(x)


def myGD1(eta, x0):
    x = [x0]
    it = 0
    for it in range(100):
        x_new = x[-1] - eta * grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x, it)


# Use what we built
(x1, it1) = myGD1(0.1, -5)
(x2, it2) = myGD1(0.1, 5)
print(f"Solution x1 = {x1[-1]:.6f}, cost = {cost(x1[-1]):.6f}, obtained after {it1} iterations")
print(f"Solution x2 = {x2[-1]:.6f}, cost = {cost(x2[-1]):.6f}, obtained after {it2} iterations")
