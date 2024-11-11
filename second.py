import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def plot_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    image = np.zeros((height, width))
    for x in range(width):
        for y in range(height):
            real = x_min + (x / width) * (x_max - x_min)
            imag = y_min + (y / height) * (y_max - y_min)
            c = complex(real, imag)
            color = mandelbrot(c, max_iter)
            image[y, x] = color

    plt.figure(figsize=(10, 10))
    plt.imshow(image, extent=(x_min, x_max, y_min, y_max), cmap='hot')
    plt.colorbar()
    plt.show()

plot_mandelbrot(800, 800, -2.0, 1.0, -1.5, 1.5, 100)
