import numpy as np
from pprint import pprint

arr1 = np.random.randint(1, 10, size=(2, 2, 2))
print("Matrix 1:\n")
pprint(arr1)

arr2 = np.random.randint(1, 10, size=(2, 2, 2))
print("\nMatrix 2:\n")
pprint(arr2)

summ = np.matmul(arr1, arr2)
print("\nMatrix Multiplication:\n")
pprint(summ)
