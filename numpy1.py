import numpy as np
import matplotlib.pyplot as plt

# Seed for reproducibility
np.random.seed(42)

# Generate random data
data = np.random.normal(loc=0, scale=1, size=1000)

# Compute basic statistics
mean = np.mean(data)
std_dev = np.std(data)
median = np.median(data)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")
print(f"Median: {median}")
print(f"1st Quartile: {q1}")
print(f"3rd Quartile: {q3}")

# Generate a matrix and perform matrix operations
matrix = np.random.rand(5, 5)
print("Original Matrix:\n", matrix)

# Transpose the matrix
transpose = np.transpose(matrix)
print("Transposed Matrix:\n", transpose)

# Compute matrix inverse
inverse = np.linalg.inv(matrix)
print("Inverse Matrix:\n", inverse)

# Verify the inverse by multiplying the matrix with its inverse (should result in identity matrix)
identity_check = np.dot(matrix, inverse)
print("Identity Check (Matrix * Inverse):\n", identity_check)

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Plotting the data
plt.hist(data, bins=30, alpha=0.7, color='g')
plt.title("Histogram of Generated Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Create a 2D grid of points
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Plot the 2D grid
plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar()
plt.title("2D Contour Plot of Sine Function")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
