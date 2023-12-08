from scipy.optimize import newton
import numpy as np

# Define the equation and its derivative
def equation(x):
    return np.sin(np.cos(np.exp(x)))

def derivative(x):
    return -np.exp(x) * np.sin(np.exp(x)) * np.cos(np.cos(np.exp(x)))

# Initial guess for Newton-Raphson method
initial_guess = -1

# Solve the equation using the Newton-Raphson method
result_newton = newton(equation, initial_guess, fprime=derivative)

# Report the result
print("Solution using Newton-Raphson method:", result_newton)
