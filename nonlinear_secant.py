from scipy.optimize import newton
import numpy as np

# Define the equation
def equation(x):
    return np.sin(np.cos(np.exp(x)))

# Initial guess for Secant method
initial_guess = -0.1

# Solve the equation using the Secant method (without specifying the derivative)
result_secant = newton(equation, initial_guess)

# Report the result
print("Solution using Secant method with initial guess -0.1:", result_secant)
