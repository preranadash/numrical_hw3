import numpy as np
from scipy.interpolate import lagrange

# Given data
x_data = np.array([0, 0.6, 0.9])
y_data = np.log(x_data + 1)

# Data point for interpolation
x_interpolation = 0.45

# Calculate Lagrange interpolation polynomial
interpolation_poly = lagrange(x_data, y_data)

# Evaluate the interpolation polynomial at x_interpolation
result_interpolation = interpolation_poly(x_interpolation)

# Calculate the true value of f(0.45)
true_value = np.log(x_interpolation + 1)

# Calculate the absolute error
absolute_error = np.abs(result_interpolation - true_value)

print("Interpolation result:", result_interpolation)
print("True value:", true_value)
print("Absolute error:", absolute_error)
