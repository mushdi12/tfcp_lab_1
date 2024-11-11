import numpy as np
import matplotlib.pyplot as plt


def f(z):
    return z ** 3 - 1


def f_prime(z):
    return 3 * z ** 2


def newton_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    roots = np.zeros(Z.shape, dtype=int)
    colors = np.zeros(Z.shape, dtype=float)

    for i in range(max_iter):
        Z -= f(Z) / f_prime(Z)

        for k, root in enumerate([1, -0.5 + 0.5j * np.sqrt(3), -0.5 - 0.5j * np.sqrt(3)]):
            mask = np.abs(Z - root) < 1e-3
            roots[mask] = k + 1
            colors[mask] = i / max_iter

    return roots, colors


xmin, xmax, ymin, ymax = -2, 2, -2, 2
width, height = 800, 800
max_iter = 50

roots, colors = newton_fractal(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.figure(figsize=(8, 8))
plt.imshow(roots, extent=(xmin, xmax, ymin, ymax), cmap='viridis', origin='lower')
plt.colorbar(label='Iterations')
plt.title("Newton's Fractal for f(z) = z^3 - 1")
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()
