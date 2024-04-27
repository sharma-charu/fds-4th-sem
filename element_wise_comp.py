# Importing the NumPy library with an alias 'np'
import numpy as np

# Creating NumPy arrays 'x' and 'y' containing numbers for comparison
x = np.array([3, 5])
y = np.array([2, 5])

# Printing the original numbers stored in arrays 'x' and 'y'
print("Original numbers:")
print(x)
print(y)

# Performing element-wise comparison (greater than) between arrays 'x' and 'y', and printing the result
print("Comparison - greater")
print(np.greater(x, y))

# Performing element-wise comparison (greater than or equal to) between arrays 'x' and 'y', and printing the result
print("Comparison - greater_equal")
print(np.greater_equal(x, y))

# Performing element-wise comparison (less than) between arrays 'x' and 'y', and printing the result
print("Comparison - less")
print(np.less(x, y))

# Performing element-wise comparison (less than or equal to) between arrays 'x' and 'y', and printing the result
print("Comparison - less_equal")
print(np.less_equal(x, y)) 
