import numpy as np
from matplotlib import pyplot as plt


def julia(z, c, max_iter):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


def plot_julia(width, height, x_min, x_max, y_min, y_max, c, max_iter):
    image = np.zeros((height, width))

    for x in range(width):
        for y in range(height):
            real = x_min + (x / width) * (x_max - x_min)
            imag = y_min + (y / height) * (y_max - y_min)
            z = complex(real, imag)
            color = julia(z, c, max_iter)
            image[y, x] = color

    plt.figure(figsize=(10, 10))
    plt.imshow(image, extent=(x_min, x_max, y_min, y_max), cmap='inferno')
    plt.colorbar()
    plt.show()


plot_julia(800, 800, -1.5, 1.5, -1.5, 1.5, complex(-0.5251993, 0.5251993), 1000)
