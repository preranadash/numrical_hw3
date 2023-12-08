from scipy.optimize import bisect
import numpy as np

# Define the equation
def equation(x):
    return np.sin(np.cos(np.exp(x)))

# Define the bracket
a = -1
b = 1

# Solve the equation using the bisection method
root = bisect(equation, a, b)

# Evaluate sin(cos(exp(x))) at the root
value_at_root = equation(root)

# Report the root and the value at the root
print("Root:", root)
print("Value at the root:", value_at_root)
