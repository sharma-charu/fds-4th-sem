# Importing the NumPy library with an alias 'np'
import numpy as np

# Creating a NumPy array 'X' containing elements 1, 7, 13, and 105
X = np.array([1, 7, 13, 105])

# Printing a message indicating the original array 'X'
print("Original array:")
print(X)

# Calculating the size of the memory occupied by the array 'X' (number of elements multiplied by the size of each element in bytes) and printing the result
print("Size of the memory occupied by the said array:")
print("%d bytes" % (X.size * X.itemsize)) 
