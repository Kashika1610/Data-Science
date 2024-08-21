import numpy as np

# Task 1: Array Creation
array_2d = np.random.randint(1, 11, size=(3, 4))  # 2D array with random integers between 1 and 10
array_1d = np.array([2, 4, 6, 8, 10])            # 1D array with specific values

# Task 2: Array Indexing and Slicing
second_row = array_2d[1]                          # Extract the second row
first_three_elements = array_1d[:3]               # Extract the first three elements

# Task 3: Array Operations
added_array = array_1d + 2                        # Element-wise addition with scalar value 2
array_2d_random = np.random.randint(1, 11, size=(4, 2))  # 2D array with random integers for multiplication
matrix_multiplication = np.dot(array_2d, array_2d_random)  # Matrix multiplication

# Task 4: Array Reshaping and Transpose
reshaped_array = array_2d.reshape(12)             # Reshape the 2D array to 1D with 12 elements
transposed_array = array_2d.T                     # Transpose the 2D array

# Task 5: Array Statistics
mean_1d = np.mean(array_1d)                       # Mean of the 1D array
median_1d = np.median(array_1d)                   # Median of the 1D array
std_dev_1d = np.std(array_1d)                     # Standard deviation of the 1D array
sum_2d = np.sum(array_2d)                         # Sum of all elements in the 2D array

# Task 6: Array Comparison
comparison_scalar = array_1d > 5                  # Compare 1D array with scalar value 5
array_2d_compare = np.random.randint(1, 11, size=(3, 4))  # Another 2D array with random integers for comparison
comparison_2d = array_2d == array_2d_compare      # Compare the two 2D arrays

# Output the results
array_2d, array_1d, second_row, first_three_elements, added_array, matrix_multiplication, reshaped_array, transposed_array, mean_1d, median_1d, std_dev_1d, sum_2d, comparison_scalar, array_2d_compare, comparison_2d
print("2D Array:\n", array_2d)
print("1D Array:", array_1d)
print("\nSecond Row of 2D Array:", second_row)
print("First Three Elements of 1D Array:", first_three_elements)

print("\nElement-wise Addition (1D Array + 2):", added_array)
print("Matrix Multiplication Result:\n", matrix_multiplication)

print("\nReshaped 2D Array to 1D Array:", reshaped_array)
print("Transposed 2D Array:\n", transposed_array)

print("\nMean of 1D Array:", mean_1d)
print("Median of 1D Array:", median_1d)
print("Standard Deviation of 1D Array:", std_dev_1d)
print("Sum of all elements in 2D Array:", sum_2d)

print("\nComparison of 1D Array with 5:", comparison_scalar)
print("Another 2D Array for Comparison:\n", array_2d_compare)
print("Comparison of 2D Arrays (element-wise):\n", comparison_2d)
