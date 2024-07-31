import numpy as np

# Universal Functions
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])
result_ufunc = np.add(array1, array2)  # Element-wise addition
print("Universal Function - Element-wise Addition:")
print(result_ufunc)

# Aggregation
array3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sum_agg = np.sum(array3)  # Sum of all elements
mean_agg = np.mean(array3)  # Mean of all elements
print("\nAggregation - Sum and Mean:")
print(f"Sum: {sum_agg}, Mean: {mean_agg}")

# Broadcasting
array4 = np.array([1, 2, 3])
array5 = np.array([[1], [2], [3]])
broadcasted_result = array4 + array5  # Broadcasting addition
print("\nBroadcasting - Addition:")
print(broadcasted_result)

# Masking
array6 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mask = array6 > 5  # Mask to select elements greater than 5
masked_array = array6[mask]
print("\nMasking - Elements Greater Than 5:")
print(masked_array)

# Fancy Indexing
array7 = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
fancy_indexed_array = array7[indices]
print("\nFancy Indexing - Selected Elements at Indices 0, 2, 4:")
print(fancy_indexed_array)

# Array Sorting
array8 = np.array([5, 3, 1, 4, 2])
sorted_array = np.sort(array8)
print("\nArray Sorting - Sorted Array:")
print(sorted_array)

# Additional code to demonstrate all in one example
print("\nAll in One Example:")
combined_array = np.array([[1, 3, 2], [9, 8, 7], [4, 6, 5]])

# Universal Function - Squaring elements
squared_array = np.square(combined_array)
print("Squared Array:")
print(squared_array)

# Aggregation - Sum of each column
sum_columns = np.sum(combined_array, axis=0)
print("Sum of Each Column:")
print(sum_columns)

# Broadcasting - Adding a constant to each element
broadcasted_add = combined_array + 10
print("Broadcasted Addition of 10:")
print(broadcasted_add)

# Masking - Elements greater than 5
masked_combined = combined_array[combined_array > 5]
print("Masked Elements Greater Than 5:")
print(masked_combined)

# Fancy Indexing - Selecting specific elements
fancy_indexed_combined = combined_array[[0, 2], [1, 2]]
print("Fancy Indexed Elements (0,1) and (2,2):")
print(fancy_indexed_combined)

# Array Sorting - Sorting each row
sorted_rows = np.sort(combined_array, axis=1)
print("Sorted Rows:")
print(sorted_rows)
