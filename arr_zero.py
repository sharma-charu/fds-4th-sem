# Importing the NumPy library with an alias 'np'
import numpy as np

# Creating a NumPy array 'x' containing elements 1, 2, 3, and 4
x = np.array([1, 2, 3, 4])

# Printing the original array 'x'
print("Original array:")
print(x)

# Checking if none of the elements in the array 'x' is zero and printing the result
print("Test if none of the elements of the said array is zero:")
print(np.all(x))

# Reassigning array 'x' to a new array containing elements 0, 1, 2, and 3
x = np.array([0, 1, 2, 3])

# Printing the new array 'x'
print("Original array:")
print(x)

# Checking if none of the elements in the updated array 'x' is zero and printing the result
print("Test if none of the elements of the said array is zero:")
print(np.all(x))
