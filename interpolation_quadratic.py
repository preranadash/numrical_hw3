import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
import matplotlib.pyplot as plt

# Given data
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1.0, 2.0, 1.0, 0.5, 4.0, 8.0])

# Fit a quadratic spline
quadratic_spline = InterpolatedUnivariateSpline(x_data, y_data, k=2)

# Generate points for the spline curve
x_spline = np.linspace(0, 5, 100)
y_spline = quadratic_spline(x_spline)

# Plot the original data and the spline curve
plt.scatter(x_data, y_data, label='Original Data')
plt.plot(x_spline, y_spline, label='Quadratic Spline', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
