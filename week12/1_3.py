import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 2*np.pi, 0.01)
y1 = np.cos(x)
y2 = np.sin(x)
y3 = np.cos(x) * (-1)
y4 = np.sin(x) * (-1)
plt.plot(x, y1, color='orange')
plt.plot(x, y2, color='blue')
plt.plot(x, y3, color='red')
plt.plot(x, y4, color='green')
plt.show()