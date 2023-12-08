import numpy as np
from scipy.integrate import romberg

# Define the function
def f(x):
    return np.exp(x)

# Define the integration limits
a = 0
b = 1

# Calculate the integral using Romberg method
result, error = romberg(f, a, b, show=True)

print("Result:", result)
print("Error estimate:", error)
