# Importing the NumPy library with an alias 'np'
import numpy as np

# Creating a NumPy array 'a' containing integers from 10 to 21 and reshaping it into a 3x4 matrix using np.arange() and .reshape()
a = np.arange(10, 22).reshape((3, 4))

# Printing a message indicating the original array 'a'
print("Original array:")
print(a)

# Printing a message indicating each element of the array using np.nditer() to iterate through the elements
print("Each element of the array is:")
for x in np.nditer(a):
    print(x, end=" ") 
