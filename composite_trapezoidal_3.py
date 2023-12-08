import numpy as np

# Define the function
def f(x):
    return np.tan(x)

# Define the integration limits
a = 0
b = 3 * np.pi / 8

# Number of subintervals (evaluations)
n = 8

# Calculate the step size
h = (b - a) / n

# Calculate the composite trapezoidal rule
result = h * (0.5 * (f(a) + f(b)) + np.sum(np.fromiter((f(a + i * h) for i in range(1, n)), dtype=float)))

print(result)
