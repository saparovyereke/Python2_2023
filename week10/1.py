# import numpy as np
# a = np.array([[64392, 31655], [32579, 0], [49248, 462], [0, 0]])
# print("Array Shape is:" , a.shape)
# print("Array dimensions are:", a.ndim)
# print("Length of each element of array in bytes is:", a.itemsize)

import numpy as np
x = int(input("Enter the number of row (x): "))
y = int(input("Enter the number of columns (x): "))

array = np.empty((x, y))

for i in range(x):
    for j in range(y):
        element = float(input(f"Enter the element at position i/j: "))
        array[i, j] = element
        
print(array)
print("Array Shape is:" , array.shape)
print("Array dimensions are:", array.ndim)
print("Length of each element of array in bytes is:", array.itemsize)