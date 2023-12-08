import numpy as np
from scipy.integrate import romberg

# Define the function
def f(x):
    return x**2 * np.exp(-x)

# Define the integration limits
a = 0
b = 1

# Calculate the integral using Romberg method
result = romberg(f, a, b, show=True)

print("Result:", result)
# from the result we can see R33 is = 0.160722