import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate random data
data = np.random.randn(1000)

# Calculate basic statistics
mean = np.mean(data)
std_dev = np.std(data)
median = np.median(data)
percentile_25 = np.percentile(data, 25)
percentile_75 = np.percentile(data, 75)

# Apply a simple moving average filter
window_size = 10
moving_avg = np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Output results
print(f"Mean: {mean:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Median: {median:.2f}")
print(f"25th Percentile: {percentile_25:.2f}")
print(f"75th Percentile: {percentile_75:.2f}")

# Display first 10 values of the original data and the moving average
print("\nOriginal data (first 10 values):")
print(data[:10])
print("\nMoving average (first 10 values):")
print(moving_avg[:10])
