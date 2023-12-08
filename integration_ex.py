import numpy as np
from scipy.integrate import trapezoid

# Define the function
def f(x):
    return np.exp(x)

# Define the integration limits
a = 0
b = 1

# Number of points for trapezoidal rule
n = 1000

# Generate the points for integration
x_values = np.linspace(a, b, n)

# Calculate the integral using the trapezoidal rule
result = trapezoid(f(x_values), x=x_values)

print(result)
