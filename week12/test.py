import matplotlib.pyplot as plt
import numpy as np

def star():
    star_vertices = np.array([
        [0, 0.5],
        [0.1, 0.2],
        [0.5, 0.2],
        [0.2, 0],
        [0.3, -0.3],
        [0, -0.1],
        [-0.3, -0.3],
        [-0.2, 0],
        [-0.5, 0.2],
        [-0.1, 0.2]
    ])
    plt.fill(star_vertices[:, 0], star_vertices[:, 1], color='yellow')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(-0.6, 0.6)
    plt.ylim(-0.4, 0.6)
    plt.show()
star()
