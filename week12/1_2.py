import matplotlib.pyplot as plt
import numpy as np
import random

x = [0.98, 0.0169]
line = np.linspace(0.016, 0.9, 20)
y = []
for points in line:
    y.append(random.uniform(points - 0.1, points + 0.1))

plt.plot(x, x, color = 'r')
plt.scatter(line, y)
plt.title("Best fit line using regression method")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()