import numpy as np

# Exercise 1: Create two dimensional 3*3 array and perform ndim, shape, slicing operation on it.
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Exercise 1 Array:\n", arr2d)
print("ndim:", arr2d.ndim)
print("shape:", arr2d.shape)
print("slicing (first two rows, first two cols):\n", arr2d[:2, :2])


# Exercise 2: Create one dimensional array and perform ndim, shape, reshape operation on it.
arr1d = np.array([10,20,30,40,50,60])
print("\nExercise 2 Array:", arr1d)
print("ndim:", arr1d.ndim)
print("shape:", arr1d.shape)
reshaped = arr1d.reshape(2,3)
print("reshaped (2x3):\n", reshaped)
