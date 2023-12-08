import numpy as np
from scipy.integrate import simps

# Define the function
def f(x):
    return np.exp(x)

# Define the integration limits
a = 0
b = 1

# Number of points for Simpson's rule
n = 1000

# Generate the points for integration
x_values = np.linspace(a, b, n)

# Calculate the integral using Simpson's rule
result = simps(f(x_values), x=x_values)

print(result)
