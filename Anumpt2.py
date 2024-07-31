import numpy as np

# Universal Functions
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result_ufunc = np.multiply(array1, array2)
print("Universal Function - Element-wise Multiplication:")
print(result_ufunc)

# Aggregation
array3 = np.array([[1, 2, 3], [4, 5, 6]])
sum_agg = np.sum(array3, axis=1)  # Sum of each row
print("\nAggregation - Sum of Each Row:")
print(sum_agg)

# Broadcasting
array4 = np.array([10, 20, 30])
array5 = np.array([[1], [2], [3]])
broadcasted_result = array4 + array5
print("\nBroadcasting - Addition:")
print(broadcasted_result)

# Masking
array6 = np.array([0, 1, 2, 3, 4, 5])
masked_array = array6[array6 % 2 == 0]  # Even elements
print("\nMasking - Even Elements:")
print(masked_array)

# Fancy Indexing
array7 = np.array([100, 200, 300, 400, 500])
indices = [0, 3, 4]
fancy_indexed_array = array7[indices]
print("\nFancy Indexing - Selected Elements at Indices 0, 3, 4:")
print(fancy_indexed_array)

# Array Sorting
array8 = np.array([42, 35, 28, 91, 60])
sorted_array = np.sort(array8)
print("\nArray Sorting - Sorted Array:")
print(sorted_array)
