import numpy as np
from scipy.integrate import romberg

# Define the function
def f(x):
    return np.cos(x)**2

# Define the integration limits
a = 0
b = np.pi / 4

# Calculate the integral using Romberg method
result = romberg(f, a, b, show=True)

print("Result:", result)

# from the result we can see R33 = 0.642733