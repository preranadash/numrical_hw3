import numpy as np
from scipy.integrate import simps

# Define the function
def f(x):
    return 2 / (x**2 + 4)

# Define the integration limits
a = 0
b = 2

# Number of subintervals (evaluations)
n = 6

# Generate the points for integration
x_values = np.linspace(a, b, n+1)

# Calculate the composite Simpson's rule
result = simps(f(x_values), x=x_values)

print(result)
