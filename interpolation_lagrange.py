import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

# Given data
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1.0, 2.0, 1.0, 0.5, 4.0, 8.0])

# Find the fifth-order polynomial using Lagrange's method
fifth_order_poly = lagrange(x_data, y_data)

# Generate points for the polynomial curve
x_poly = np.linspace(0, 5, 100)
y_poly = fifth_order_poly(x_poly)

# Plot the original data and the polynomial curve
plt.scatter(x_data, y_data, label='Original Data')
plt.plot(x_poly, y_poly, label='Fifth-order Polynomial', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
