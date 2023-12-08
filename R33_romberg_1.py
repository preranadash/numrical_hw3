import numpy as np
from scipy.integrate import romberg

# Define the function
def f(x):
    return x**2 * np.log(x)

# Define the integration limits
a = 1
b = 1.5

# Calculate the integral using Romberg method
result = romberg(f, a, b, show=True)

print("Result:", result)

#from the result we can see R33=0.192258